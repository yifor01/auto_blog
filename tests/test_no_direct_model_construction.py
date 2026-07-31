"""Meta-test：靜態掃描 src/，禁止在讀取路徑上直接 `Model(**dict)` 重建。

why 要機械檢查而不是靠人記：`ContentItem(**raw)` / `ScoredItem(**rec)` 會重複
套用 Layer A 的 s2twp（對繁體刻意不冪等），退回去是**完全靜默**的——不拋錯、
沒有 log，只是每讀一次文字就漂一格。逐一針對呼叫端寫的測試守得住現況，卻對
「有人新增第 N+1 個呼叫點」毫無感覺，而那正是上一輪失手的同一類盲點。
本專案 `tests/` 不進 repo、CI 也不跑測試，本機測試是唯一守門員。

正確的讀取路徑：`models.item_from_raw()` / `models.scored_from_raw()`。
"""

import ast
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src"
TARGET_MODELS = ("ContentItem", "ScoredItem")

# `Model(**dict)` 的唯一合法實作點——兩個 *_from_raw() 就住在這裡
UNPACK_ALLOWED = {"models.py"}

# 以 keyword 建構（`ContentItem(title=..., url=...)`）是**新建**而非重建，
# 不經過存檔 dict，也就沒有二次套用 Layer A 的問題：
#   - collectors/  ：把外部 API 回應轉成 ContentItem，Layer A 正是要在這裡生效
#   - pinned.py / scoring/rules.py：把「已經建好的」ContentItem 包成 ScoredItem。
#     Pydantic v2 預設不 revalidate model 實例（已實測 `si.item is ci`），
#     所以巢狀欄位不會被再跑一次 validator。
KWARG_ALLOWED = UNPACK_ALLOWED | {
    "collectors",
    "pinned.py",
    "scoring/rules.py",
}


def _alias_map(tree: ast.AST) -> dict[str, str]:
    """`from src.models import ScoredItem as SI` → {"SI": "ScoredItem"}。

    why 要追蹤別名：只比對 `ast.Name.id in TARGET_MODELS` 的話，`SI(**x)` 完全
    看不見（實測 MISSED）。別名匯入是繞過本規則最省事的寫法，掃描器對它視而不見
    等於整條規則形同虛設。
    """
    aliases: dict[str, str] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            for alias in node.names:
                if alias.name in TARGET_MODELS and alias.asname:
                    aliases[alias.asname] = alias.name
    return aliases


def _called_model(func: ast.expr, aliases: dict[str, str]) -> str | None:
    """回傳這個 call 目標對應的 model 名稱，不是就回 None。

    兩種寫法都要認：
      - `ScoredItem(**x)` / `SI(**x)`        → ast.Name（含別名）
      - `models.ScoredItem(**x)`             → ast.Attribute，比對 `.attr`
    `ast.Attribute` 那條實測原本 MISSED——模組限定的呼叫是完全合法的 Python，
    掃描器漏掉它，規則就只擋得住「照著慣例寫」的人。
    """
    if isinstance(func, ast.Name):
        name = aliases.get(func.id, func.id)
        return name if name in TARGET_MODELS else None
    if isinstance(func, ast.Attribute):
        return func.attr if func.attr in TARGET_MODELS else None
    return None


def _constructions_in_source(source: str, rel: str) -> list[tuple[str, int, str, bool]]:
    """掃單份原始碼，回傳 (相對路徑, 行號, 類別名, 是否為 **unpacking)。

    抽出來是為了讓 AST 規則本身可被測試——`_constructions()` 只掃真實 src/，
    「掃描器認不認得某種寫法」無法用它驗證（上一版的盲點正是這樣被放過的）。
    """
    tree = ast.parse(source, filename=rel)
    aliases = _alias_map(tree)
    found = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        name = _called_model(node.func, aliases)
        if name is None:
            continue
        unpacking = any(kw.arg is None for kw in node.keywords)
        found.append((rel, node.lineno, name, unpacking))
    return found


def _constructions() -> list[tuple[str, int, str, bool]]:
    """回傳 (相對路徑, 行號, 類別名, 是否為 **unpacking) 清單。"""
    found = []
    for path in sorted(SRC.rglob("*.py")):
        found += _constructions_in_source(
            path.read_text(encoding="utf-8"), path.relative_to(SRC).as_posix()
        )
    return found


def _violations(unpacking_only: bool) -> list[str]:
    allowed = UNPACK_ALLOWED if unpacking_only else KWARG_ALLOWED
    out = []
    for rel, lineno, name, unpacking in _constructions():
        if unpacking_only and not unpacking:
            continue
        if unpacking and not unpacking_only:
            continue  # 交給另一條規則管，不重複回報
        if any(rel == a or rel.startswith(a + "/") for a in allowed):
            continue
        out.append(f"src/{rel}:{lineno} {name}")
    return out


def test_premise_scan_actually_finds_constructions():
    """前提：掃描器真的看得到東西。掃到 0 筆代表 AST 規則寫壞了，而非專案很乾淨。"""
    assert len(_constructions()) >= 10


def test_no_dict_unpacking_construction_outside_models():
    """`ContentItem(**raw)` / `ScoredItem(**rec)` 只准出現在 src/models.py。

    命中就代表有人繞過 item_from_raw() / scored_from_raw() 直接從存檔 dict 重建，
    該路徑產出的每一段文字都會比存檔多漂一格 s2twp。
    """
    bad = _violations(unpacking_only=True)
    assert not bad, (
        "以下位置直接從 dict 重建 model，請改走 "
        "models.item_from_raw() / models.scored_from_raw()：\n  " + "\n  ".join(bad)
    )


def test_no_unexpected_keyword_construction():
    """keyword 建構只准在既知的新建點（collectors / pinned / rules）。

    新增建構點本身未必是錯，但必須是有意識的決定：這條測試逼人回來看一眼
    「這裡到底是新建還是重建」，順手把新位置寫進 KWARG_ALLOWED。
    """
    bad = _violations(unpacking_only=False)
    assert not bad, (
        "新的 model 建構點，請確認是新建（非從存檔重建）後補進 KWARG_ALLOWED：\n  "
        + "\n  ".join(bad)
    )


# ── 掃描器本身的盲點回歸測試 ─────────────────────────────────
#
# 這幾條測的是「掃描器認不認得這種寫法」，不是「src/ 現在乾不乾淨」。
# 前者壞掉時後者照樣全綠——上一版的 ast.Name-only 實作就是這樣把
# `models.ScoredItem(**x)` 與別名匯入兩種寫法完全放行的（實測皆 MISSED）。

def test_scanner_sees_plain_name_call():
    found = _constructions_in_source("ContentItem(**raw)\n", "x.py")
    assert found == [("x.py", 1, "ContentItem", True)]


def test_scanner_sees_module_attribute_call():
    """`models.ScoredItem(**x)` —— 模組限定呼叫，原本 MISSED。"""
    src = "import src.models as models\nmodels.ScoredItem(**rec)\n"
    found = _constructions_in_source(src, "x.py")
    assert found == [("x.py", 2, "ScoredItem", True)]


def test_scanner_sees_aliased_import_call():
    """`from src.models import ScoredItem as SI; SI(**x)` —— 別名，原本 MISSED。"""
    src = "from src.models import ScoredItem as SI\nSI(**rec)\n"
    found = _constructions_in_source(src, "x.py")
    assert found == [("x.py", 2, "ScoredItem", True)]


def test_scanner_distinguishes_kwargs_from_unpacking():
    src = "ContentItem(title='t', url='u')\n"
    assert _constructions_in_source(src, "x.py") == [("x.py", 1, "ContentItem", False)]


def test_scanner_ignores_unrelated_names():
    src = "from src.models import GeneratedContent as GC\nGC(**x)\nfoo.bar(**x)\nother(**x)\n"
    assert _constructions_in_source(src, "x.py") == []
