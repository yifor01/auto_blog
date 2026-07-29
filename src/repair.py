"""歷史資料修復：HF 摘要黏字重抓 + Layer A 清洗回補（entity / 媒體標記 / 簡→繁）
＋ `data/scored` 依 `data/raw` 對齊。

why 合併成一支：所有修復都要翻 data/raw、data/scored、output/lists、output/posts
同一批檔案，分成多支等於把每個檔案改多遍、產生多次巨量 diff。

why 這裡是清洗的唯一歸屬：讀取端（`models.item_from_raw()` /
`models.scored_from_raw()`）刻意**無損還原**存檔原值，不做二次清洗——否則每讀一次
就多套一層 s2twp 而漂移。分工是「讀取端無損，清洗歸資料層」，資料層就是本模組。

修復目標與判定依據見 docs/superpowers/specs/2026-07-28-raw-data-box-design.md
"""

from __future__ import annotations

import html
import json
import re
import time
from collections.abc import Callable
from datetime import date, timedelta
from functools import lru_cache
from pathlib import Path

from src.collectors.hf_papers import (
    _ENRICH_DELAY_SECONDS,
    _extract_arxiv_id,
    _fetch_arxiv_abstract,
    fetch_paper_abstract,
    looks_unspaced,
)
from src.logger import get_logger
from src.models import _LAYER_A_FIELDS, strip_media_tags
from src.utils import normalize_url_light, save_json, to_traditional_shape_only

_logger = get_logger(__name__)

_RAW_DIR = Path("data/raw")
_SCORED_DIR = Path("data/scored")
_LISTS_DIR = Path("output/lists")
_POSTS_DIR = Path("output/posts")

# output/lists 的條目沒有 tags 欄位，只有 title / abstract
_LIST_FIELDS = ("title", "abstract")

_DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")
# 只吃 frontmatter 的 title 行；body 不動（可能含程式碼區塊裡字面意義的 &amp;）。
# `_FRONTMATTER_RE` 先把搜尋範圍夾在開頭的 `---` … `---` 之間再找 title——只用
# MULTILINE 的話，`search()` 會咬到**全檔第一個行首 `title:`**，正文（尤其是
# 引用 YAML 的程式碼區塊）出現一行 `title: ...` 就會被當成 frontmatter 改掉。
# 實測 2757 篇 post 目前 0 篇會踩到，這是廉價保險而非救火。
_FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)^---[ \t]*\r?$", re.DOTALL | re.MULTILINE)
_TITLE_LINE_RE = re.compile(r'^title:[ \t]*(.*)$', re.MULTILINE)


def _within_days(path: Path, days: int | None) -> bool:
    if days is None:
        return True
    m = _DATE_RE.match(path.stem)
    if not m:
        return False
    return date.fromisoformat(m.group(1)) >= date.today() - timedelta(days=days)


# ──────────────────────────────────────────────────────────
# 單一欄位的清洗：entity 解碼 → 剝媒體標記 → 簡→繁（只修字形）
#
# 順序刻意與 `ContentItem` 的 Layer A validator 一致（unescape → strip → 轉繁）：
# `&lt;img src=...&gt;` 要解碼後才認得出是標記，剝完再轉繁也少餵 OpenCC 一段標記。
# ──────────────────────────────────────────────────────────


# 明明是**正字繁體**、OpenCC 卻在單字元層級就會改寫的字，不採計為「這個欄位含簡體」
# 的證據。這兩個字在台灣繁體是天天出現的正常用字（干擾 / 干預、托盤 / 委托），
# 但 `s2tw('干') == '幹'`、`s2tw('托') == '託'`——把它們當簡體證據，等於讓一整個
# 純繁體欄位過門，接著被詞組規則改壞。實測 `data/raw` 全量：不排除的話有 11 個純繁體
# 的量子位摘要唯一觸發條件就是這兩個字，落地結果是 `干預`→`幹預`、`托盤`→`託盤`、
# `安托資訊`→`安託資訊`，全部是錯的。排除後改動欄位 804 → 793、非冪等仍為 0，
# 且 `互不干扰`→`互不干擾`、`托盘`→`托盤` 這些**真簡體**的欄位照樣轉得對
# （欄位裡還有別的簡體字撐著 gate，過門後 OpenCC 仍會處理 `干`/`托`）。
#
# 代價：若出現「整段簡體、且唯一簡體字就是 `干` 或 `托`」的欄位（如孤立的 `委托`）
# 會漏轉。現有語料 0 筆，且新資料走 Layer A 不經這裡。
#
# 加字進來前先實測：擴到 `里` 會讓 22 個**真簡體**欄位整個不轉（`里` 常是唯一 gate），
# 擴到 `占` 則 0 影響（沒必要）。
_NOT_SIMPLIFIED_EVIDENCE = frozenset("干托")


@lru_cache(maxsize=None)
def _is_simplified_char(ch: str) -> bool:
    """這個字元是否可作為「該欄位含簡體」的證據。

    「單字元」是關鍵：OpenCC 的詞組規則要有上下文才會觸發，餵單一字元等於只問
    「這個字本身會不會被改寫」。注意**別把它想成「是不是簡體字」**——實測
    `s2tw('里')='裡'`、`s2tw('干')='幹'`、`s2tw('托')='託'` 都會變，但這三個字在繁體
    正文裡本來就大量出現；只有 `了` / `面` / `杆` / `只` 這類才是真的單字元不動、
    純靠詞組規則才被改寫。誤把前者當「不會動」正是 `幹擾` / `託盤` / `幹預` 落地的
    根源，故另立 `_NOT_SIMPLIFIED_EVIDENCE` 排除集（理由見該處）。

    OpenCC 不可用時 `to_traditional_shape_only()` 原樣回傳 → 一律判定為非簡體 →
    `_to_traditional_safe()` 整個退化成 no-op，這是刻意的安全降級。
    """
    if ch in _NOT_SIMPLIFIED_EVIDENCE:
        return False
    return to_traditional_shape_only(ch) != ch


def _has_control_chars(text: str) -> bool:
    return any(ord(c) < 32 and c not in "\n\r\t" for c in text)


# ──────────────────────────────────────────────────────────
# 變體修正表：把 OpenCC 在「一簡對多繁」上選錯的分支改回來。
#
# why 需要它（守門調整做不到的事）：`_NOT_SIMPLIFIED_EVIDENCE` 只能決定「這個欄位
# 要不要進轉換器」，管不到「進去之後 OpenCC 挑哪個繁體」。實測全語料 85601 個欄位，
# 加了排除集之後仍有兩類錯誤落地：① **守門失效**——欄位靠**別的**合法繁體字
# （`云`/`里`/`台`/`范`/`卷`/`合`）過門，接著純繁體被詞組規則改壞（`受到干擾`→`受到幹擾`）；
# ② **OpenCC 消歧錯誤**——欄位確實整段簡體、該轉，但 `托盘`/`复杂`/`只写` 這些被挑成
# 了 `託盤`/`復雜`/`隻寫`。①②合計 39 處。繼續擴大排除集治不了②，而且已實測不可行
# （把 `里` 加進去會讓 22 個真簡體欄位整個不轉）。
#
# why 這個形狀是對的：沿用 `src/utils.py` 的 `_TERM_FIXES` 既有 pattern（轉換後套一張
# 修正表），表在收斂迴圈**之後**跑，所以冪等性由建構保證——重跑時前面的轉換會重新
# 產生同樣的中間結果，再被同一張表導成同樣的輸出。
#
# ## 每一條都必須在本語料裡無歧義（全部逐條實測過）
#
# 表是從**實際觀察到的汙染**導出的，不是抄通用異體字清單：先掃出本 pass 新造的所有
# 一簡對多繁變體（`瞭隻麵髮鍾復歷齣穀醜佈儘幹乾託臺遊裡捲佔…`），再逐字看上下文，
# 只收「這個字串在整份語料裡 100% 是錯的」的條目。刻意**沒有**收進來的：
#   - `瞭解` / `一目瞭然` / `糊裡糊塗` / `佔比` / `捲到` / `平臺` / `幹活` / `麵包`
#     ——這些是**正確**的台灣繁體，不是汙染
#   - `阿裡巴巴` / `公裡` / `裡程碑` / `隻在`——本語料 0 次出現（前兩者 OpenCC 本來就
#     轉得對），收進來就變成沒有證據的通用清單；`隻在` 還會弄壞「一隻在樹上的鳥」
#
# 幾條刻意加長以避開誤傷（都在註解標出被擋掉的反例）。
_VARIANT_FIXES = {
    # ① 守門失效：純繁體被詞組規則改壞
    "幹擾": "干擾",        # 受到干擾 / 抗干擾 / 過濾干擾（11 處，語料內 0 個合法「幹擾」）
    "幹預": "干預",        # 人工干預 / 接管干預（17 處）
    "臺積電": "台積電",    # 專有名詞；一般的 `平臺` 是正確台灣用法，不在表內
    "穀底": "谷底",        # 士氣跌至 20 年谷底（`穀` 是穀物，語料內 0 個合法用法）
    "託馬斯": "托馬斯",    # Thomas Kurian
    "藍色遊標": "藍色游標",  # 公司名；不寫成通用的 `遊標→游標`，那會弄壞「旅遊標籤」
    "/遊資": "/游資",      # 只在 `政策/遊資追蹤` 這種列舉裡；前綴 `/` 擋掉「旅遊資訊」
    # ② OpenCC 消歧錯誤：整段簡體該轉，但挑錯分支
    # 托盤三條刻意帶左側脈絡：本語料雖然 0 個「委託盤」，但語料裡就有股市工具的
    # README，`委託盤` / `信託盤` 是這個領域裡很可能出現的近似字串，通用的
    # `託盤→托盤` 會把它們改壞（已由測試釘住）。
    "/託盤": "/托盤",      # 代理組/托盤圖標 ×6
    "金屬託盤": "金屬托盤",
    "載物託盤": "載物托盤",
    "復雜": "複雜",        # `複雜` 是唯一正確寫法，`復雜` 恆錯
    "證明瞭": "證明了",    # 動詞 + 了；`瞭解` / `一目瞭然` 不受影響
    "說明瞭": "說明了",
    "目睹瞭": "目睹了",
    "一齣來": "一出來",    # `齣` 只用於戲曲量詞
    "乾的就是": "幹的就是",  # 以下三條是「幹（做）」被挑成「乾（dry）」；
    "乾的是": "幹的是",      # 不用通用的 `乾的→幹的`，那會弄壞「曬乾的衣服」
    "乾的活": "幹的活",
    # 「不是只寫 / 只面向 / 只在 / 只返回…」共 13 處，語料內 0 個量詞用法。
    # 已知殘餘風險：「不是隻身一人」會被改壞——本語料 0 次出現「隻身」，且那是
    # 文學用語，不是 AI 新聞語料會有的東西；真出現時補一條反向條目即可。
    "不是隻": "不是只",
    "這隻會": "這只會",    # 「這只會營造出…」；語料內 0 個「這隻會飛的鳥」
}


def _apply_variant_fixes(text: str) -> str:
    for wrong, right in _VARIANT_FIXES.items():
        if wrong in text:
            text = text.replace(wrong, right)
    return text


def _convert_once(text: str) -> str:
    """單輪簡→繁，含兩道守門（理由見 `_to_traditional_safe()`）。"""
    if _has_control_chars(text):
        return text
    if not any(_is_simplified_char(c) for c in text):
        return text
    return to_traditional_shape_only(text)


# 收斂上限。實測全庫 71765 個欄位最多 2 輪就穩定，留餘裕但不無限跑。
_MAX_CONVERT_ROUNDS = 5


def _to_traditional_safe(text: str) -> str:
    """簡→繁，但只在「這個欄位真的含簡體字」時才動手，且收斂到不動點。

    ## why 用 s2tw（shape only）而不是 Layer A 的 `to_traditional()`（s2twp）

    s2twp 帶台灣詞庫、對繁體**不冪等**（文件→檔案→…）。歷史 raw 混著兩種資料：
    2026-06-20 之前是未經 Layer A 的真簡體，之後是已經 Layer A 過的繁體。對全量
    套 s2twp，等於把後半段再轉一次——實測一輪 round-trip 就漂 731 個欄位 / 521 筆
    記錄（3.00%），正是前幾輪從讀取路徑移除的那個 bug。

    ## why 還要加「含簡體字」這道門

    s2tw 對**純繁體**輸入不是無害的：OpenCC 的詞組規則會誤觸發，實測
    `說明了一件事` → `說明瞭一件事`（明了→明瞭）、`裡面包括` → `裡麵包括`
    （面包→麵包）。`了` / `面` 這類字單獨看不會被改，只有在詞組規則下才中招——
    所以「欄位裡至少要有一個**單字元層級**就會被改寫的字」正好把「整段簡體的舊資料」
    與「已是繁體的新資料」分開。實測 data/raw：894 個欄位會被 s2tw 改動，這道門
    擋掉 101 個（其中 37 個是純繁體被詞組規則誤改、11 個是只被 `干`/`托` 誤觸發的
    純繁體欄位），放行 793 個。

    **注意 `里` / `干` / `托` 單字元就會被改寫**（`裡` / `幹` / `託`），不屬於上面
    那類；其中 `干` / `托` 因為在繁體正文太常見而列入 `_NOT_SIMPLIFIED_EVIDENCE`
    排除集，理由見該處。

    **這道門治不了「過門之後 OpenCC 挑錯分支」**——它是欄位層級的准入測試，不是
    字級的正確性保證。純繁體欄位靠**別的**合法繁體字（`云`/`里`/`台`/`范`）過門、
    以及真簡體欄位被挑成 `託盤`/`復雜`/`隻寫`，這兩類合計 39 處錯誤都由收斂後的
    `_VARIANT_FIXES` 收尾。不再繼續收緊守門的理由：放行的欄位裡有 90 個要靠詞組
    規則才轉得對（关系→關係、制作→製作），而 Layer A 對新資料本來就是全詞組轉換；
    「只換簡體字位置」的手術式做法已實測否決——`to_traditional_shape_only('干')`
    單字就是 `幹`（問題完全沒解），還會新增 120 個全錯欄位（`阿里巴巴`→`阿裡巴巴`）、
    150 個欄位失去一簡對多繁的消歧（`复杂`→`復雜`、`分钟`→`分鍾` 皆錯），
    並繞過整張 `_TERM_FIXES`。

    ## 附帶效果：這個 pass 同時也是 `_TERM_FIXES` 改寫 pass

    `to_traditional_shape_only()` 每次轉換都會呼叫 `utils._apply_term_fixes()`，
    所以只要欄位過了門，`引數`→`參數`、`擴充套件`→`擴展`、`繫結`→`綁定`、
    `控制元件`→`控制項` 也會一併被改掉。實測落地欄位裡有 **27 個純 OpenCC 差異為 0**
    （data/raw 24、data/scored 2、output/lists 1）——它們完全是被 `_TERM_FIXES`
    改的，一個簡體字都沒轉。
    更要緊的是這件事**不均勻**：`data/raw` 有 108 個欄位含 `_TERM_FIXES` 的 key，
    其中 27 個過門被修、81 個被守門擋著沒修；一個欄位的 `引數` 會不會被修好，
    取決於它**碰巧有沒有夾一個無關的簡體字**。
    這是既有 `to_traditional_shape_only()` 的行為，不是本模組決定的；要讓它一致
    就得把 `_TERM_FIXES` 提升成無條件 pass，那是另一個設計決定，不在本次範圍。
    CLI 的「簡→繁 N 欄」因此**包含了「沒有任何簡體被轉換」的欄位**。

    ## why 擋掉含控制字元的欄位

    少數 abstract 是被當成文字存進來的 PNG / JPEG 位元組。OpenCC 遇到 NUL 會
    **靜默截斷**——實測 1543 字的欄位轉完只剩 7 字。那些欄位本來就是壞資料，
    但靜默截斷是不可逆的破壞，一律不碰（data/raw 17 個、data/scored 1 個）。

    ## why 要收斂到不動點（而不是轉一次就收工）

    OpenCC 的詞組規則吃上下文，而第一輪把周邊字轉繁之後**上下文就變了**，於是
    第二輪還會再動一次：`互不干扰` →（1）`互不干擾` →（2）`互不幹擾`。實測全庫
    71765 個欄位有 16 個是這種兩輪才穩定的，涉及 21 個字元，全部是「一簡對多繁」
    的歧義字（干→幹 9、托→託 6、里→裡 2、了/出/占/卷 各 1）。

    轉一次就收工的話，這 16 個欄位會在**下一次跑 repair-content 時**再變一格——
    正是本專案一路在修的「每跑一次漂一格」。所以這裡直接收斂，把不動點寫進檔案，
    之後再跑幾次都不會再動。

    收斂本身會挑錯分支（`互不干擾`→`互不幹擾`）——那不是靠「不收斂」解決的（停在
    非不動點只是把同一批錯誤延後一輪，還賠掉整個設計賴以成立的冪等性），而是交給
    收斂後的 `_VARIANT_FIXES` 修回來。另一個被否決的選項是「不穩定就整個欄位不轉」，
    那會讓十幾篇**整段簡體**的長摘要原封留著簡體，遠比個位數異體字糟。
    超過 `_MAX_CONVERT_ROUNDS` 仍不收斂就整個欄位不動並記 warning（實測 0 筆）。

    ## 最後一步：變體修正表

    迴圈跑完才套 `_VARIANT_FIXES`（見該處）。**只在真的轉過的欄位上套**——沒過門的
    欄位連碰都不碰，維持「守門擋下的就是原封不動」這個不變量。
    """
    out = text
    for _ in range(_MAX_CONVERT_ROUNDS):
        nxt = _convert_once(out)
        if nxt == out:
            break
        out = nxt
    else:
        _logger.warning("簡→繁轉換未收斂，該欄位保持原值", extra={"preview": text[:80]})
        return text
    if out == text:
        return text
    return _apply_variant_fixes(out)


def _clean_value(value: str, stats: dict) -> str:
    """單一字串跑完三道清洗，並分類累計統計。

    統計單位是**欄位數**不是出現次數：一個 title 裡有 3 個 entity 只計 1
    （tags 則逐個元素各算一個欄位）。CLI 文案的「N 欄」與此一致。
    """
    unescaped = html.unescape(value)
    if unescaped != value:
        stats["entities_fixed"] += 1

    stripped = strip_media_tags(unescaped)
    if stripped != unescaped:
        stats["media_stripped"] += 1

    converted = _to_traditional_safe(stripped)
    if converted != stripped:
        stats["simplified_converted"] += 1

    return converted


def _clean_field(value, stats: dict):
    """回傳 (新值, 是否改動)。字串與字串陣列（tags）都處理，其餘型別原樣返回。"""
    if isinstance(value, str):
        new = _clean_value(value, stats)
        return new, new != value
    if isinstance(value, list):
        out, changed = [], False
        for v in value:
            nv, c = _clean_field(v, stats)
            out.append(nv)
            changed = changed or c
        return out, changed
    return value, False


def _clean_fields_in_place(container: dict, fields, stats: dict) -> bool:
    """就地清洗 dict 的指定欄位，回傳是否有改動。"""
    changed = False
    for field in fields:
        if field not in container:
            continue
        new_val, ch = _clean_field(container[field], stats)
        if ch:
            container[field] = new_val
            changed = True
    return changed


# ──────────────────────────────────────────────────────────
# HF 摘要重抓
# ──────────────────────────────────────────────────────────


def _build_default_fetchers() -> tuple[Callable[[str], str], Callable[[str], str]]:
    """建立生產用的真實 HTTP fetcher（每次請求前先節流）。

    why 每次請求前 sleep：本模組會在迴圈裡連續打 HF 論文頁（全期約 192 次），
    沿用 collectors/hf_papers.py 的 collect() 對同一端點的既有節流慣例，
    刻意 import `_ENRICH_DELAY_SECONDS` 而非另立常數——兩處調的是同一個端點，
    分成兩個常數只會日後各自漂移。

    why sleep 放在 fetcher 內而非呼叫迴圈：注入 stub 的測試因此完全不會 sleep，
    節流只發生在真的要連網的路徑上。
    """
    from src.utils import get_http_client

    client = get_http_client()

    def _fetch_hf(url: str) -> str:
        time.sleep(_ENRICH_DELAY_SECONDS)
        return fetch_paper_abstract(client, url)

    def _fetch_arxiv(arxiv_id: str) -> str:
        time.sleep(_ENRICH_DELAY_SECONDS)
        return _fetch_arxiv_abstract(arxiv_id, client)

    return _fetch_hf, _fetch_arxiv


def _repair_hf_abstract(
    url: str,
    fetcher: Callable[[str], str],
    arxiv_fetcher: Callable[[str], str],
) -> str:
    """重抓單筆 HF 摘要，修不好回 ""。

    三段式（依設計 spec §6）：重抓論文頁 → 失敗或結果仍判定為破損則走 arXiv
    fallback → 兩者皆失敗才回空字串，由呼叫端保留原值。

    why 一定要有 arXiv 這層：192 筆破損項全部抽得出 arxiv_id（覆蓋率 192/192），
    而它正是 HF 端被限流時唯一的救生索——少了它，一旦 HF 開始擋就整批修不動。
    """
    new_abs = fetcher(url)
    if new_abs and not looks_unspaced(new_abs):
        return new_abs

    arxiv_id = _extract_arxiv_id(url)
    if not arxiv_id:
        return ""
    alt = arxiv_fetcher(arxiv_id)
    if alt and not looks_unspaced(alt):
        _logger.info("HF abstract repaired via arXiv fallback", extra={"arxiv_id": arxiv_id})
        return alt
    return ""


# ──────────────────────────────────────────────────────────
# 各層檔案的修復
# ──────────────────────────────────────────────────────────


def _load_json_list(path: Path, label: str):
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        _logger.warning(f"Skipping unreadable {label} file", extra={"path": str(path)})
        return None
    return data if isinstance(data, list) else None


def _repair_raw_file(
    path: Path,
    stats: dict,
    dry_run: bool,
    fetcher: Callable[[str], str] | None,
    arxiv_fetcher: Callable[[str], str],
    fetched: dict[str, str],
) -> list | None:
    """修 `data/raw/{date}.json`，回傳清洗後的 items（供同日 scored 對齊）。

    回傳的是**記憶體中已清洗**的 items，即使 dry_run 沒寫檔也一樣——scored 的
    候選數因此在 dry-run 下也反映「raw 修乾淨之後」的狀態，不會把髒 raw 當基準。
    """
    items = _load_json_list(path, "raw")
    if items is None:
        return None

    changed = False
    for it in items:
        if not isinstance(it, dict):
            continue
        # 1) HF 黏字重抓
        #    source 限定是硬約束：looks_unspaced() 對其他來源不保證正確，
        #    全來源掃描會誤判 hackernews 26 筆 / reddit 8 筆（整串 URL 的留言）。
        #    那些若被拿去 fetch_paper_abstract，等於把 gist 頁 / 圖片 URL 的
        #    任意 <p> 寫進真實 abstract —— 是寫壞資料，不是修不完。
        refetched = False
        if it.get("source") == "hf_papers" and looks_unspaced(it.get("abstract") or ""):
            if dry_run:
                stats["hf_candidates"] += 1
            else:
                new_abs = _repair_hf_abstract(it.get("url", ""), fetcher, arxiv_fetcher)
                if new_abs:
                    it["abstract"] = new_abs
                    stats["hf_refetched"] += 1
                    changed = refetched = True
                else:
                    stats["hf_failed"] += 1
                    _logger.warning(
                        "HF abstract refetch failed (page + arXiv)",
                        extra={"url": it.get("url")},
                    )
        # 2) Layer A 清洗（entity / 媒體標記 / 簡→繁）
        if _clean_fields_in_place(it, _LAYER_A_FIELDS, stats):
            changed = True
        # 重抓值同樣先清洗完才進對照表——output/lists 要拿到與 raw 逐字相同的成品
        if refetched:
            fetched[normalize_url_light(it.get("url", ""))] = it["abstract"]

    if changed and not dry_run:
        save_json(items, path)
        stats["files_written"] += 1
    return items


def _repair_scored_file(
    path: Path, raw_items: list | None, stats: dict, dry_run: bool
) -> None:
    """把 `data/scored/{date}.json` 的 Layer A 欄位對齊同日 `data/raw`。

    why 需要這一步：`data/scored` 的 item 是 collect 當下的副本，從未被 repair 掃過。
    實測全庫 2712 筆與 raw 的一致率 97.46%（69 筆不一致：17 筆未解碼 entity、
    52 筆 abstract 空白被吃掉），而讀取端改成無損還原之後，這些落差就直接變成
    使用者可見的回歸（同一頁的「原始資料 box」讀 raw、列表讀 scored，兩處對不上）。

    配對用 `normalize_url_light()`：兩端拿的是同一個 `ContentItem.url` 原值，只需要
    吸收 scheme / 尾斜線這類無害差異。實測配對率 100%（2712/2712，0 缺 raw 檔、
    0 對不上 URL）。

    **評分欄位一律不動**——只覆寫 `_LAYER_A_FIELDS`。配對不到的記錄（實測 0 筆）
    仍會跑一次清洗，不會因為缺 raw 就整筆放生。
    """
    recs = _load_json_list(path, "scored")
    if recs is None:
        return

    raw_map: dict[str, dict] = {}
    for it in raw_items or []:
        if isinstance(it, dict):
            raw_map[normalize_url_light(it.get("url", ""))] = it

    changed = False
    for rec in recs:
        if not isinstance(rec, dict):
            continue
        item = rec.get("item")
        if not isinstance(item, dict):
            continue

        source = raw_map.get(normalize_url_light(item.get("url", "")))
        if source is not None:
            for field in _LAYER_A_FIELDS:
                if field not in source or item.get(field) == source[field]:
                    continue
                value = source[field]
                # list 要複製再塞：直接指派會讓 raw 與 scored 共用同一個 list 物件
                item[field] = list(value) if isinstance(value, list) else value
                stats["scored_backfilled"] += 1
                changed = True

        if _clean_fields_in_place(item, _LAYER_A_FIELDS, stats):
            changed = True

    if changed and not dry_run:
        save_json(recs, path)
        stats["files_written"] += 1


def _repair_lists_file(
    path: Path, fetched: dict[str, str], stats: dict, dry_run: bool
) -> None:
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return
    if not isinstance(doc, dict):
        return

    changed = False
    buckets = [doc.get("github") or []]
    papers = doc.get("papers") or {}
    buckets += [papers.get("hf") or [], papers.get("others") or []]
    for entries in buckets:
        for e in entries:
            if not isinstance(e, dict):
                continue
            repaired = fetched.get(normalize_url_light(e.get("url", "")))
            if repaired and e.get("abstract") != repaired:
                e["abstract"] = repaired
                changed = True
            if _clean_fields_in_place(e, _LIST_FIELDS, stats):
                changed = True

    if changed and not dry_run:
        save_json(doc, path)
        stats["files_written"] += 1


def _repair_post_file(path: Path, stats: dict, dry_run: bool) -> None:
    """只改 frontmatter 的 `title:` 行。

    body 一律不動：那是 LLM 生成內容，裡面的 `&amp;` 可能是字面意義、`<script>`
    可能在程式碼區塊裡。檔名也不動——slug 是 Astro 頁面 id，改名會斷連結與
    localStorage 已讀記錄。
    """
    text = path.read_text(encoding="utf-8")
    fm = _FRONTMATTER_RE.match(text)
    if not fm:
        return
    # 在 frontmatter 區塊內找，但位移一律換算回全檔座標（切片時才不會錯位）
    m = _TITLE_LINE_RE.search(text, fm.start(1), fm.end(1))
    if not m:
        return
    new_title, changed = _clean_field(m.group(1), stats)
    if not changed or dry_run:
        return
    path.write_text(text[: m.start(1)] + new_title + text[m.end(1) :], encoding="utf-8")
    stats["files_written"] += 1


def repair_all(
    days: int | None = None,
    dry_run: bool = False,
    fetcher: Callable[[str], str] | None = None,
    arxiv_fetcher: Callable[[str], str] | None = None,
) -> dict:
    """修復歷史資料（raw / scored / lists / posts 四處）。

    fetcher(url) / arxiv_fetcher(arxiv_id) 為注入點，測試必須注入以避免真實 HTTP。

    why 注入 fetcher 就不再建立任何真實 client：只要呼叫端注入了 fetcher（＝測試
    路徑），未注入的 arxiv_fetcher 會退化成永遠回 "" 的 no-op，而不是偷偷建一個
    真的 arXiv client。測試因此不可能意外連網。生產路徑（兩者皆 None）才建真的。

    dry_run 完全不連網：只清點待修候選數，不重抓也不寫檔。

    why raw 與 scored 同日成對處理（而非各掃各的）：scored 的對齊來源必須是
    **修乾淨之後**的 raw，否則等於把髒資料原封抄過去。成對處理同時把記憶體
    上限壓在單日（data/raw 全量 33MB，整批載入沒必要）。
    """
    stats = {
        "hf_candidates": 0,
        "hf_refetched": 0,
        "hf_failed": 0,
        "entities_fixed": 0,
        "media_stripped": 0,
        "simplified_converted": 0,
        "scored_backfilled": 0,
        "files_written": 0,
    }
    fetched: dict[str, str] = {}  # normUrl -> 修好的 abstract，供 lists 同步

    if dry_run:
        # dry-run 的用途是確認規模，不需要真的抓；官方流程是「先 dry-run 再實跑」，
        # 若這裡也連網，光是預覽就把總請求數翻倍。
        fetcher = arxiv_fetcher = None
    elif fetcher is None:
        fetcher, default_arxiv = _build_default_fetchers()
        if arxiv_fetcher is None:
            arxiv_fetcher = default_arxiv
    if arxiv_fetcher is None:
        arxiv_fetcher = lambda _arxiv_id: ""  # noqa: E731

    # ── data/raw + data/scored（同日成對）───────────────────
    stems: set[str] = set()
    for directory in (_RAW_DIR, _SCORED_DIR):
        if directory.exists():
            stems |= {p.stem for p in directory.glob("*.json") if _within_days(p, days)}
    for stem in sorted(stems):
        raw_items = _repair_raw_file(
            _RAW_DIR / f"{stem}.json", stats, dry_run, fetcher, arxiv_fetcher, fetched
        )
        _repair_scored_file(_SCORED_DIR / f"{stem}.json", raw_items, stats, dry_run)

    # ── output/lists ──────────────────────────────────────
    for path in sorted(_LISTS_DIR.glob("*.json")) if _LISTS_DIR.exists() else []:
        if _within_days(path, days):
            _repair_lists_file(path, fetched, stats, dry_run)

    # ── output/posts（只動 frontmatter title 行）─────────────
    for path in sorted(_POSTS_DIR.glob("*.md")) if _POSTS_DIR.exists() else []:
        if _within_days(path, days):
            _repair_post_file(path, stats, dry_run)

    return stats
