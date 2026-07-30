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
# ## ⚠️ 這張表是**一次性機會**，不是可以事後補的清單
#
# `_to_traditional_safe()` 有 `if out == text: return text`——修正表**只套在真的
# 轉過的欄位上**。非 dry-run 寫入之後那些欄位就變成純繁體，守門再也不放行，
# 於是**日後補進本表的條目對已修過的資料完全無效**（實測：把 `年曆史→年歷史`
# 加進表再跑一次，該欄位殘留的 evidence 字元是空集合、完全不被碰）。
# 實跑當下表裡沒有的錯字＝永久落地，只能 `git revert`。所以本表在實跑前必須掃乾淨。
#
# ## 每一條都必須在本語料裡無歧義（全部逐條實測過）
#
# 表是從**實際觀察到的汙染**導出的，不是抄通用異體字清單。導出方法（target-side，
# 刻意不從表本身回推，否則是循環驗證）：對每個欄位算輸出與輸入的**字元多重集差**，
# 挑出本 pass 新造的字元，再依 `s2tw(t2s(T)) != T` 分出「OpenCC 預設不會產生的
# 第二順位變體」45 種，逐字列出所有相異鄰接詞人工判讀。掃描範圍含
# `output/posts` 的 frontmatter title（前兩輪從未掃過）。
#
# 刻意**沒有**收進來的：
#   - `瞭解` / `一目瞭然` / `糊裡糊塗` / `佔比` / `捲到` / `平臺` / `幹活` / `麵包`
#     / `奇蹟` / `老闆` / `鍛鍊` / `這傢伙` / `摺疊` / `獎盃` / `日曆` / `係數`
#     ——這些是**正確**的台灣繁體，不是汙染
#   - `阿裡巴巴` / `公裡` / `裡程碑` / `隻在`——本語料 0 次出現，收進來就變成沒有
#     證據的通用清單；`隻在` 還會弄壞「一隻在樹上的鳥」
#
# ## why 幾乎每條都帶脈絡
#
# 一次性的性質 ⇒ **寧可少修也不要造新錯**。凡是「錯字字串」可能跨詞邊界撞到正常
# 文字的，一律用實測到的脈絡加長，並在註解寫出被擋掉的反例。加長不損失覆蓋率：
# 脈絡是從**全語料的全部出現位置**枚舉出來的，不是抽樣。
_VARIANT_FIXES = {
    # ── ① 守門失效：欄位靠別的合法繁體字過門，純繁體被詞組規則改壞 ──
    # 幹擾 / 幹預 帶左脈絡：語料裡有「骨幹」，通用寫法會撞到「骨幹擾動」「骨幹預備」
    "過濾幹擾": "過濾干擾",
    "受到幹擾": "受到干擾",
    "一次幹預": "一次干預",
    "人工幹預": "人工干預",
    "接管幹預": "接管干預",  # 這筆是**存檔裡既有**的汙染，不是本 pass 造的；
                            # 但欄位會被轉換 ⇒ 這是唯一一次能順手修掉它的機會
    "臺積電": "台積電",      # 專有名詞；一般的 `平臺` 是正確台灣用法，刻意不收
    "穀底": "谷底",          # 士氣跌至 20 年谷底（`穀` 是穀物，語料 0 個合法用法）
    "託馬斯": "托馬斯",      # Thomas Kurian
    "藍色遊標": "藍色游標",  # 公司名；通用的 `遊標→游標` 會弄壞「旅遊標籤」
    "/遊資": "/游資",        # 前綴 `/` 擋掉「旅遊資訊」
    # ── ② OpenCC 消歧錯誤：整段簡體該轉，但挑錯分支 ──
    # 托盤三條帶左脈絡：語料裡就有股市工具 README，通用寫法會弄壞「委託盤」「信託盤」
    "/託盤": "/托盤",        # 代理組/托盤圖標 ×6
    "金屬託盤": "金屬托盤",
    "載物託盤": "載物托盤",
    # 復雜三條帶左脈絡：通用寫法會弄壞「修復雜湊表」「恢復雜亂的狀態」
    # （`雜湊` 是台灣的 hash 術語，AI 語料撞得到）
    "不復雜": "不複雜",
    "更復雜": "更複雜",
    "執行復雜": "執行複雜",
    # 瞭 三條帶右脈絡：通用的 `說明瞭→說明了` 會弄壞「說明瞭解決方案」
    # （`瞭解` 是正確台灣用法）
    "證明瞭太多": "證明了太多",
    "說明瞭一件": "說明了一件",
    "目睹瞭如今": "目睹了如今",
    "一齣來": "一出來",      # `齣` 只用於戲曲量詞
    # 「搞定并发布」是「搞定 + 並發布（and publish）」，被挑成併發（concurrency）。
    # 帶脈絡：語料裡的 `併發限制` / `高併發` 是正確的 concurrency 用法。
    "搞定併發布": "搞定並發布",
    # 乾（dry）被挑來當「幹（做）」；通用的 `乾的→幹的` 會弄壞「曬乾的衣服」
    "乾的就是": "幹的就是",
    "乾的是": "幹的是",
    "該乾的活": "該幹的活",
    "它乾的活": "它幹的活",
    # 隻（量詞）被挑來當「只」；帶右脈絡是因為語料裡就有正確的量詞用法
    # （`一隻可怕的怪物`、`三兩隻小貓`、`這隻快樂生蠔`），通用寫法會誤傷
    "不是隻寫": "不是只寫",
    "不是隻面": "不是只面",
    "不是隻在": "不是只在",
    "不是隻返": "不是只返",
    "這隻會營造": "這只會營造",
    # ── ③ fix round 4：**第一順位挑錯**（round 3 的掃描法結構上看不到）──
    #
    # round 3 用 `s2tw(t2s(T)) != T` 挑候選字元 ⇒ 只看得到「第二順位」變體。
    # 但 OpenCC 也會在**第一順位**就挑錯：`s2tw('签') == '籤'`、`s2tw('并') == '並'`、
    # `s2tw('里') == '裡'` 都是預設值，於是 `籤`/`並`/`裡` 這三個字整批被排除在候選
    # 之外——跟 round 2 的循環驗證是同一種盲點，只是升了一層。
    "合並請求": "合併請求",   # 代碼提交合併請求（merge request）
    "在籤什麼": "在簽什麼",   # 「不知道自己在簽什麼」——簽名不是標籤
    "一起籤的": "一起簽的",
    # 托馬斯·庫里安（Thomas Kurian）。音譯名一律用共用字形（里），帶義符的
    # `裡`（內部）不可能出現在譯名裡。**必須用間隔號錨定**：通用的 `庫裡安→庫里安`
    # 會弄壞「資料庫裡安放著索引」這種在本領域極自然的句子（已由測試釘住）。
    "·庫裡安": "·庫里安",
    # ── ④ fix round 3 用 target-side 掃描新抓到的（前兩輪的黑名單看不到）──
    "曆史": "歷史",          # 27 年歷史 / 超長歷史記錄；`日曆` 不受影響
    "總檯": "總臺",          # 央視總臺
    "聯閤": "聯合",          # 聯合中國人民大學
    "係統化": "系統化",      # 帶 `化`：通用的 `係統→系統` 會弄壞「關係統計」
    "剋制": "克制",          # 教育部標準寫法
    "死衚衕": "死胡同",      # 教育部標準寫法
    "揹負": "背負",          # 教育部標準寫法
}


def _apply_variant_fixes(text: str) -> str:
    for wrong, right in _VARIANT_FIXES.items():
        if wrong in text:
            text = text.replace(wrong, right)
    return text


# ──────────────────────────────────────────────────────────
# 錯字修正表：**無守門**、對所有 Layer A 欄位無條件套用。
#
# ## 與上面 `_VARIANT_FIXES` 的職責分界（請勿合併這兩張表）
#
# | | `_VARIANT_FIXES` | `_TYPO_FIXES`（本表）|
# |---|---|---|
# | 套用時機 | 只在 `_to_traditional_safe()` **真的轉換過**的欄位上 | 每個欄位，無條件 |
# | 覆蓋範圍 | 約 800 個欄位 | 全部 88361 個欄位 |
# | 修的是什麼 | 本 pass **自己造成**的錯（OpenCC 一簡對多繁挑錯分支）| 存檔裡**既有**的錯字，跟本 pass 轉不轉無關 |
# | 安全門檻 | 脈絡風險有界（欄位本來就整段簡體 / 剛被改寫過）| 會碰到從沒被動過的正常文字，門檻高得多 |
#
# 合併兩張表會同時弄壞兩件事：`_VARIANT_FIXES` 的條目一旦無條件化，就會踩到
# 「守門擋下的欄位原封不動」這條不變量（有 guard 測試釘住）；本表的條目若被關進
# 守門後面，就修不到它存在的唯一理由——**純繁體欄位裡的既有錯字**（守門永遠擋著，
# 跑幾次都一樣）。
#
# ## 條目來源與驗收（刻意不從本表回推，否則是循環驗證）
#
# 導出方法：對全語料的每個 CJK 字元算 `tw2s(C)`，把同簡體字的繁體字們分成
# 「歧義組」（實測 3039 個相異字、82 組），組內低頻成員逐一列出**全部**鄰接脈絡
# 人工判讀。這個方法看得到 `_VARIANT_FIXES` 的兩種掃描法都看不到的東西，因為它
# 完全不依賴「這個欄位有沒有被轉換過」。
#
# 驗收（每次改本表都要重跑，方法見 task-5 報告）：把本表套遍全部 88361 個欄位，
# 把**每一處實際改動**連同前後 18 字印出來人工過目——目前 114 處 / 87 個相異脈絡，
# 全部是真錯字，0 誤傷。這是「先改再看改了什麼」，不是「數自己的 pattern 命中幾次」。
#
# ## why 幾乎每條都帶脈絡
#
# 錯字字串本身多半在別的詞裡是**正確**的，通用寫法必然誤傷。脈絡是從全語料的
# 全部出現位置枚舉出來的，加長不損失覆蓋率。註解裡寫出被擋掉的反例。
#
# ## 冪等
#
# 由建構保證：本表所有 value 都不含任何 key（有測試釘住），所以套第二次是 no-op。
# 位置在 `_clean_value()` 的**最後**——`_to_traditional_safe()` 若在重跑時又把
# `干預` 轉回 `幹預`，本表會再修一次，淨結果仍是同一個不動點。
_TYPO_FIXES = {
    # ── 干 / 幹 ──
    # 全部帶脈絡：語料裡有 ML 的「骨幹」(backbone) 與「擾動」(perturbation)，
    # 通用的 `幹擾→干擾` 會把「骨幹擾動」改成「骨干擾動」；`幹預` 同理會撞到
    # 「骨幹預備隊」。反過來 `幹活`／`幹嘛`／`軀幹`／`幹線` 共 165 處都是正確用法。
    "幹預路徑": "干預路徑",
    "幹預效果": "干預效果",
    "幹預後果": "干預後果",
    "是幹預，": "是干預，",   # 逗號錨定：`幹`＋`預算` 不可能緊接逗號
    "主動幹預": "主動干預",
    "匹配幹擾": "匹配干擾",
    "抗幹擾": "抗干擾",       # `抗幹` 不成詞
    "伸手幹擾": "伸手干擾",
    "多人幹擾": "多人干擾",
    # ── 復 / 複（複雜被寫成復雜）──
    # 帶左脈絡：通用寫法會弄壞「修復雜湊表」「恢復雜亂的狀態」（`雜湊` 是台灣的
    # hash 術語，AI 語料撞得到）。語料裡 `復` 有 300 處，其餘皆為正確的
    # 修復／恢復／復現／復刻／康復／復旦／李開復／復盤。
    "更復雜": "更複雜",
    "不復雜": "不複雜",
    "執行復雜": "執行複雜",
    "進行復雜": "進行複雜",
    "展開復雜": "展開複雜",
    # ── 併 / 並 ──
    # `併發`(concurrency)／`合併`／`一併`／`併入`／`併網` 在語料裡都是正確用法，
    # 所以 key 一律取到後面那個動詞：`布`／`起`／`揮` 都不可能接在 concurrency 的
    # 「併發」後面（沒有「併發布署」這種詞）。
    "併發布": "並發布",
    "併發起": "並發起",
    "併發揮": "並發揮",
    "併產生": "並產生",
    "併入圍": "並入圍",
    "精簡併穩定": "精簡並穩定",   # 擋「合併穩定版」
    "，併為": "，並為",           # 逗號錨定，擋「兩者併為一體」
    "，併成為": "，並成為",       # 逗號錨定，擋「合併成一家」
    "，併成立": "，並成立",
    # ── 係 / 系 ──
    # 一律右錨定：通用的 `係統→系統` 會弄壞「關係統計」「關係統一」。
    # 語料裡 `係` 共 95 處，其餘皆為正確的 `關係`／`係數`。
    "係統化": "系統化",
    "係統論證": "系統論證",
    "係統電氣": "系統電氣",
    # ── 瞭 / 了 ──
    # 一律右錨定：`瞭解`／`一目瞭然` 是正確台灣用法（語料 52 處），通用的
    # `指明瞭→指明了` 會弄壞「指明瞭解決方案」。
    "指明瞭靶子": "指明了靶子",
    "指明瞭方向": "指明了方向",
    "鮮明瞭：": "鮮明了：",
    "證明瞭向": "證明了向",
    "證明瞭三維": "證明了三維",
    # ── 隻 / 只 ──
    # 一律**兩側**錨定。右錨定不夠：`一隻有毒的蜘蛛`／`一隻會飛的鳥`／`一隻是黑的`
    # 都合法；左錨定也不夠：`而是隻身前往` 合法。語料裡 `隻` 共 43 處，其中 30 處
    # 是正確的量詞用法（一隻手／兩隻機械臂／這隻小貓／多隻靈貓）。
    "大多隻是": "大多只是",
    "不是隻會": "不是只會",
    "不是隻做": "不是只做",
    "不是隻問": "不是只問",
    "不是隻能": "不是只能",
    "而是隻持有": "而是只持有",
    "而是隻保留": "而是只保留",
    "而是隻執行": "而是只執行",
    "是隻描述": "是只描述",
    "是隻更新": "是只更新",
    "沒有隻盯": "沒有只盯",
    "許多隻有": "許多只有",
    "很多隻展示": "很多只展示",
    # ── 其他歧義組的低頻錯字（每條都逐一列出全部脈絡判讀過）──
    "曆史": "歷史",      # `曆` 只用於曆法；語料 13 處，另 12 處是正確的 `日曆`。
                         # 唯一的理論反例 `日曆史` 全語料 0 次
    "衚衕": "胡同",      # 教育部標準寫法；`衚`/`衕` 只出現在 `死衚衕`
    "穀底": "谷底",      # `穀` 是穀物；語料無任何合法 `穀` 用法
    "穀歌": "谷歌",      # Google
    "剋制": "克制",      # 教育部標準寫法
    "聯閤": "聯合",      # `閤` 是門扇
    "詆譭": "詆毀",      # 教育部標準寫法；`譭` 只出現在 `詆譭`
    "孃胎": "娘胎",      # 教育部標準寫法
    "一齣，": "一出，",  # `齣` 只用於戲曲量詞（一齣好戲）；逗號錨定 ⇒ 後面沒有
                         # 被計量的名詞，不可能是量詞
    "一齣來": "一出來",
    "一箇": "一個",      # `箇` 只用於 `箇中`（語料另有 1 處正確的 `，箇中意味`）
    "几乎": "幾乎",      # 漏網的簡體字（`几` 作案几時是繁體，語料 0 次）
    "7天后": "7天後",    # 漏網的簡體字；數字錨定，擋掉正確的 `天后`（媽祖／歌后）
    "傢俬人": "家私人",  # 一家私人公司；`傢俬` 是粵語傢俱，擋掉正確的 `傢俱`／`傢伙`
    "人傢俬聊": "人家私聊",
    # LaTeX 的 document class。s2twp 的台灣詞庫把 `文档` 轉成 `檔案`，但這裡的
    # 「文檔類」指的是 documentclass，正解是「文件類」。脈絡取整串，因為
    # 「檔案類型」在別的語境是完全正確的。
    "檔案類與相關字型": "文件類與相關字型",
}


def _apply_typo_fixes(text: str) -> str:
    """無條件錯字修正（與 `_apply_variant_fixes()` 的差別見 `_TYPO_FIXES`）。"""
    for wrong, right in _TYPO_FIXES.items():
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
    以及真簡體欄位被挑成 `託盤`/`復雜`/`隻寫`/`年曆史`/`係統化`，這兩類錯誤都由
    收斂後的 `_VARIANT_FIXES` 收尾（該表是**一次性機會**，理由見該處）。不再繼續收緊守門的理由：放行的欄位裡有 90 個要靠詞組
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
    """單一字串跑完四道清洗，並分類累計統計。

    統計單位是**欄位數**不是出現次數：一個 title 裡有 3 個 entity 只計 1
    （tags 則逐個元素各算一個欄位）。CLI 文案的「N 欄」與此一致。

    錯字修正排在**最後**且無守門：`_to_traditional_safe()` 只碰「含簡體字」的欄位，
    修不到純繁體欄位裡的既有錯字；而它自己在重跑時可能又把 `干預` 轉回 `幹預`，
    放在後面才能保證整條鏈的不動點唯一。
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

    fixed = _apply_typo_fixes(converted)
    if fixed != converted:
        stats["typos_fixed"] += 1

    return fixed


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
        "typos_fixed": 0,
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
