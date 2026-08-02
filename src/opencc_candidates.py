"""簡→繁修正表候選累積（方案 A）：從語料掃出「OpenCC 可能挑錯繁體分支」的候選。

設計與鐵則見 `docs/superpowers/plans/2026-07-31-opencc-candidate-accumulation.md`。
三條不可破的鐵則摘要：

- **(a)** 產出終點是 `src/utils.py` 的 `_VARIANT_FIXES`（Layer A 持續生效），
  不是 `repair.py`——`repair` 對同一批資料只有一次機會，補晚了就無效
- **(b)** 寧可少修也不要造新錯。不確定一律 `rejected`
- **(c)** 驗收標準不可從自己的修法導出。本模組**只產生候選、永不自動改表**

## 為什麼是「無狀態掃描 + 有狀態裁決帳本」

`data/raw/` 每天 commit 進 repo，掃描可隨時對既有存檔重算，不需要每天寫佇列。
原設計要寫的 `data/review/*.jsonl` **會被 daily pipeline 的 `git add` 白名單丟掉且
無 log 無報錯**（白名單只有 `data/raw/`、`data/scored/`、`data/bookmarks.json` 與三個
output 目錄），正是本專案反覆踩到的靜默失效形狀。重算的設計順帶讓去重免費（已裁決
的 pattern 天然被帳本濾掉）、且 OpenCC 升版後可直接重掃全部歷史。

## 假陽性是前提，不是缺陷

2026-07-31 巡邏實測假陽性率 **90–95%**：`回/迴`、`复/複→復`、`制/製`、`布/佈` 這幾組
的少數分支 100% 是正確用字，噪音主體是專有名詞（阿里、周鴻禕）與固定術語（自迴歸、
遞迴、復盤）。任何設計都必須以「大部分候選是誤報」為前提，靠 `decisions.jsonl` 逐輪
收斂，而不是靠更聰明的過濾器。

**已試過並否決的過濾器**：對脈絡片段做 `t2s` → `s2twp` round-trip，只留 OpenCC 真的
會產生該少數分支的位置。2026-08-02 實測 7 天 437 個候選只濾掉 12 個（**2.7%**）——
語料主體本來就是簡體來源，繞一圈會原樣重現同一個分支，等於在確認而非鑑別。
"""

from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path

from src.logger import get_logger
from src.utils import DATA_DIR, OUTPUT_DIR, RAW_DIR

_logger = get_logger(__name__)

OPENCC_DIR = DATA_DIR / "opencc"
GROUPS_PATH = OPENCC_DIR / "ambiguity-groups.json"
DECISIONS_PATH = OPENCC_DIR / "decisions.jsonl"
REPORT_DIR = OUTPUT_DIR / "opencc-candidates"

# 基本區 + 擴展 A。歧義組的來源是 **OpenCC 自己的字典**，不是任何外部常用字表——
# 「哪些字會產生一簡對多繁分歧」完全由 `STCharacters`/`TSCharacters` 定義，拿教育部
# 字表去框是用外部代理猜一件函式庫已經精確定義的事。實測（1.3.1）2802 組 / 5758 字，
# 對比「只用語料出現過的字建表」的 39 組，冷啟動缺口 72 倍。
_CJK_RANGES = ((0x4E00, 0x9FFF), (0x3400, 0x4DBF))

_CONTEXT_RADIUS = 15
_MAX_CONTEXTS = 5

# 掃描範圍是全部 source 的這三個欄位（`_LAYER_A_FIELDS`）——不是只有 RSS，
# 巡邏實測中文 GitHub README 也會餵進 Layer A。
_SCAN_FIELDS = ("title", "abstract", "tags")


class OpenCCVersionMismatch(RuntimeError):
    """歧義組表與實裝的 OpenCC 版本不符。

    這是**拒跑**而不是警告：表過期代表新歧義組整批漏掉，而漏掉是無聲的。
    """


def _installed_opencc_version() -> str:
    import opencc

    return opencc.__version__


# ──────────────────────────────────────────────────────────
# 歧義組表（靜態，僅 OpenCC 升版時重建）
# ──────────────────────────────────────────────────────────

def build_ambiguity_groups() -> dict:
    """對整個 CJK 範圍逐字跑 `t2s`，依簡體像分組，組內 ≥2 字的即歧義組。

    `default` 是 `s2tw(簡體字)` 的輸出，也就是**字元層級的預設分支**；組內其餘
    皆為「少數分支」。用 s2tw 而非 s2t 是為了跟專案既有的兩個 converter 一致
    （Layer A 的 s2twp 在字元層級等同 s2tw）。

    有 2 組（`腭/齶`、`鮎/鲇`）的 s2tw 輸出不在自己組內，無法定義少數分支，
    直接排除——強行取一個分支只會製造假候選。
    """
    from opencc import OpenCC

    t2s = OpenCC("t2s")
    s2tw = OpenCC("s2tw")

    by_simplified: dict[str, list[str]] = defaultdict(list)
    for low, high in _CJK_RANGES:
        for code_point in range(low, high + 1):
            ch = chr(code_point)
            simplified = t2s.convert(ch)
            if len(simplified) == 1:
                by_simplified[simplified].append(ch)

    groups: dict[str, dict] = {}
    for simplified, chars in sorted(by_simplified.items()):
        if len(chars) < 2:
            continue
        default = s2tw.convert(simplified)
        if len(default) != 1 or default not in chars:
            continue
        groups[simplified] = {"default": default, "chars": sorted(chars)}

    return {"opencc_version": _installed_opencc_version(), "groups": groups}


# 下面幾支的路徑參數一律 `None` → 進函式才解析模組常數，而不是寫在預設值上。
# 預設值在 def 時就綁死，測試 monkeypatch 模組常數會完全無效（然後靜默去讀真實
# `data/`、寫真實 `output/`）——本專案已有 backfill 打真實 HF 的前例。
def save_ambiguity_groups(doc: dict, path: Path | None = None) -> Path:
    path = path or GROUPS_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(doc, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def load_ambiguity_groups(path: Path | None = None) -> dict:
    """讀歧義組表並**強制**版本相符，不符即拋 `OpenCCVersionMismatch`。

    比對對象是**實裝的 opencc 版本**而不是 `constraints.txt` 的字串：真正決定
    分組結果的是實際跑的那份字典，而「實裝版本 == constraints 鎖的版本」已由
    `tests/test_to_traditional.py::TestOpenCCVersionGuard` 守住。
    """
    path = path or GROUPS_PATH
    if not path.exists():
        raise FileNotFoundError(
            f"{path} 不存在，先跑 `python -m src.cli opencc-candidates --rebuild-groups`"
        )
    doc = json.loads(path.read_text(encoding="utf-8"))
    table_version = doc.get("opencc_version")
    installed = _installed_opencc_version()
    if table_version != installed:
        raise OpenCCVersionMismatch(
            f"歧義組表建於 OpenCC {table_version}，目前實裝 {installed}；"
            "字典已變動，先跑 `--rebuild-groups` 重建，並把 decisions.jsonl 整批視為需重審"
        )
    return doc


def minority_map(doc: dict) -> dict[str, tuple[str, str]]:
    """少數分支字元 → (簡體字, 預設分支)。"""
    return {
        ch: (simplified, group["default"])
        for simplified, group in doc["groups"].items()
        for ch in group["chars"]
        if ch != group["default"]
    }


# ──────────────────────────────────────────────────────────
# 三表覆蓋 / 裁決帳本
# ──────────────────────────────────────────────────────────

def table_keys() -> tuple[str, ...]:
    """三張修正表的 key。`_TYPO_FIXES` 在 `repair.py`，其餘兩張在 `utils.py`。"""
    from src.repair import _TYPO_FIXES
    from src.utils import _TERM_FIXES, _VARIANT_FIXES

    return tuple(_TERM_FIXES) + tuple(_VARIANT_FIXES) + tuple(_TYPO_FIXES)


def covered_positions(text: str, keys: tuple[str, ...]) -> set[int]:
    """回傳 `text` 中被任一 key **完整字串**覆蓋的字元索引。

    ⚠️ 判定必須是「key 的出現區間涵蓋該位置」，**不可退化成單字元子字串比對**
    （`ch in some_key`）——巡邏過程中這個 bug 讓所有候選都被誤判為已覆蓋，整個
    掃描靜默回報 0 筆。`tests/test_opencc_candidates.py` 有一條會紅的測試釘住。
    """
    covered: set[int] = set()
    for key in keys:
        start = text.find(key)
        while start != -1:
            covered.update(range(start, start + len(key)))
            start = text.find(key, start + 1)
    return covered


def load_decisions(path: Path | None = None) -> dict[str, dict]:
    """讀 append-only 裁決帳本，回傳 pattern → 最後一筆紀錄。"""
    path = path or DECISIONS_PATH
    if not path.exists():
        return {}
    decisions: dict[str, dict] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        # `#` 開頭是註解：這個帳本是**人手寫**的（每週審查一次），檔案本身要能
        # 帶著自己的欄位說明，否則下一個審查者得回頭翻程式碼才知道要填什麼。
        if not line or line.startswith("#"):
            continue
        record = json.loads(line)
        decisions[record["pattern"]] = record
    return decisions


# ──────────────────────────────────────────────────────────
# 掃描
# ──────────────────────────────────────────────────────────

@dataclass
class Occurrence:
    day: str
    source: str
    snippet: str


@dataclass
class Candidate:
    pattern: str
    char: str
    default: str
    simplified: str
    count: int = 0
    articles: set[str] = field(default_factory=set)
    days: set[str] = field(default_factory=set)
    contexts: list[Occurrence] = field(default_factory=list)

    @property
    def article_count(self) -> int:
        return len(self.articles)

    @property
    def day_count(self) -> int:
        return len(self.days)


@dataclass
class ScanResult:
    days_scanned: int
    files: list[str]
    items: int
    candidates: list[Candidate]
    suppressed: dict[str, int]


def _iter_raw_files(days: int | None, raw_dir: Path) -> list[Path]:
    files = sorted(raw_dir.glob("*.json"))
    if days is None:
        return files
    cutoff = (date.today() - timedelta(days=days - 1)).isoformat()
    return [f for f in files if f.stem >= cutoff]


def _field_texts(item: dict) -> list[str]:
    texts: list[str] = []
    for name in _SCAN_FIELDS:
        value = item.get(name)
        if isinstance(value, str):
            texts.append(value)
        elif isinstance(value, list):
            texts.extend(v for v in value if isinstance(v, str))
    return texts


def scan(
    days: int | None = 7,
    *,
    raw_dir: Path | None = None,
    groups_doc: dict | None = None,
    decisions: dict[str, dict] | None = None,
    keys: tuple[str, ...] | None = None,
) -> ScanResult:
    """掃出未被三表覆蓋、也未被帳本裁決過的少數分支出現位置。

    排序依**跨文章數**而非總次數——同一篇文章重複 10 次的價值低於 3 篇各 1 次。
    """
    raw_dir = raw_dir or RAW_DIR
    doc = groups_doc if groups_doc is not None else load_ambiguity_groups()
    minority = minority_map(doc)
    decided = decisions if decisions is not None else load_decisions()
    table = keys if keys is not None else table_keys()

    builders: dict[str, Candidate] = {}
    suppressed: dict[str, int] = defaultdict(int)
    files = _iter_raw_files(days, raw_dir)
    items_seen = 0

    for path in files:
        day = path.stem
        try:
            items = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            _logger.warning("skip unreadable raw file", extra={"file": str(path), "error": str(e)[:160]})
            continue
        for index, item in enumerate(items):
            if not isinstance(item, dict):
                continue
            items_seen += 1
            article = item.get("url") or f"{day}#{index}"
            source = item.get("source") or "?"
            for text in _field_texts(item):
                if not text:
                    continue
                covered = covered_positions(text, table)
                for position, ch in enumerate(text):
                    if ch not in minority or position in covered:
                        continue
                    simplified, default = minority[ch]
                    pattern = f"{ch}→{default}"
                    if pattern in decided:
                        suppressed[pattern] += 1
                        continue
                    candidate = builders.get(pattern)
                    if candidate is None:
                        candidate = builders[pattern] = Candidate(
                            pattern=pattern, char=ch, default=default, simplified=simplified
                        )
                    candidate.count += 1
                    candidate.articles.add(article)
                    candidate.days.add(day)
                    if len(candidate.contexts) < _MAX_CONTEXTS:
                        snippet = text[
                            max(0, position - _CONTEXT_RADIUS) : position + _CONTEXT_RADIUS + 1
                        ]
                        candidate.contexts.append(Occurrence(day=day, source=source, snippet=snippet))

    candidates = sorted(
        builders.values(), key=lambda c: (-c.article_count, -c.count, c.pattern)
    )
    return ScanResult(
        days_scanned=len(files),
        files=[f.stem for f in files],
        items=items_seen,
        candidates=candidates,
        suppressed=dict(suppressed),
    )


# ──────────────────────────────────────────────────────────
# 報告
# ──────────────────────────────────────────────────────────

def render_report(result: ScanResult, decisions: dict[str, dict] | None = None) -> str:
    """產出給人審的 markdown。核准條件與反例欄位直接印在報告裡，不靠審查者記得。"""
    decided = decisions if decisions is not None else {}
    lines = [
        "# 簡→繁修正表候選",
        "",
        f"掃描 {result.days_scanned} 天 / {result.items} 筆 / "
        f"{len(result.candidates)} 個未裁決 pattern",
        "",
        "核准一條候選必須**同時**滿足（鐵則 (c)，不可循環驗證）：",
        "1. ≥2 則脈絡且來自**不同文章**（單篇多次不算）",
        "2. 反例檢查欄位非空——寫不出「這個 key 在什麼情況下會誤傷」就不能核准",
        "3. 外部來源交叉核對（教育部重編國語辭典或兩個獨立繁中語料庫詞頻），"
        "**不得只憑語感**",
        "",
        "核准者手動把條目加進 `src/utils.py` 的 `_VARIANT_FIXES`（有守門），"
        "並補錨定與反例註解。本工具**永不自動改表**。",
        "",
    ]

    for candidate in result.candidates:
        lines.append(
            f"## `{candidate.char}` "
            f"({candidate.simplified}→{candidate.default}/{candidate.char} 組，少數分支)"
        )
        lines.append("")
        lines.append(
            f"- 出現 {candidate.count} 次，跨 {candidate.article_count} 篇文章，"
            f"跨 {candidate.day_count} 天"
        )
        lines.append(f"- 建議：`{candidate.char}` → `{candidate.default}`")
        lines.append("- 脈絡：")
        for i, occurrence in enumerate(candidate.contexts, 1):
            lines.append(
                f"  {i}. [{occurrence.day} {occurrence.source}] …{occurrence.snippet}…"
            )
        lines.append("- ⚠️ 反例檢查（審查者必填）：本組正確用 "
                     f"`{candidate.char}` 的情形 = ______")
        lines.append("")

    if result.suppressed:
        # 已裁決的不能完全隱形：`rejected` 會永久壓住一個 pattern，若當初判錯，
        # 這行是唯一能讓人再想起它的地方（另一條防線是 OpenCC 升版時整批重審）。
        lines.append("## 已裁決（本次略過）")
        lines.append("")
        for pattern, count in sorted(result.suppressed.items(), key=lambda kv: -kv[1]):
            record = decided.get(pattern, {})
            verdict = record.get("verdict", "?")
            when = record.get("date", "?")
            lines.append(f"- `{pattern}` — {verdict}（{when}），本次仍出現 {count} 次")
        lines.append("")

    return "\n".join(lines)


def save_report(text: str, target: date | None = None, out_dir: Path | None = None) -> Path:
    out_dir = out_dir or REPORT_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{(target or date.today()).isoformat()}.md"
    path.write_text(text, encoding="utf-8")
    return path
