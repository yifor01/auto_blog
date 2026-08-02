"""Shared utilities: config loading, HTTP client, dedup, LLM calls."""

from __future__ import annotations

import difflib
import itertools
import json
import os
import re
from datetime import date, datetime
from functools import lru_cache
from pathlib import Path
from typing import Callable

import time

import httpx
import yaml
from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console

console = Console()

from src.logger import get_logger as _get_logger  # noqa: E402
_logger = _get_logger("utils")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
SCORED_DIR = DATA_DIR / "scored"
FEEDBACK_DIR = DATA_DIR / "feedback"
HEALTH_DIR = DATA_DIR / "health"
OUTPUT_DIR = PROJECT_ROOT / "output"
POSTS_DIR = OUTPUT_DIR / "posts"
NOTES_DIR = OUTPUT_DIR / "notes"
PROMPTS_DIR = OUTPUT_DIR / "prompts"
DIGESTS_DIR = OUTPUT_DIR / "digests"
BLOGS_DIR = OUTPUT_DIR / "blogs"
LISTS_DIR = OUTPUT_DIR / "lists"

for d in [RAW_DIR, SCORED_DIR, FEEDBACK_DIR, HEALTH_DIR, POSTS_DIR, NOTES_DIR, PROMPTS_DIR, DIGESTS_DIR, BLOGS_DIR, LISTS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

load_dotenv(PROJECT_ROOT / ".env")


def load_config() -> dict:
    config_path = PROJECT_ROOT / "config.yaml"
    with open(config_path) as f:
        return yaml.safe_load(f)


# ──────────────────────────────────────────────────────────
# 簡體中文 → 繁體中文（台灣正字）轉換
# ──────────────────────────────────────────────────────────

_opencc_converter = None
_opencc_shape_converter = None
_opencc_unavailable = False

# s2twp 的 TWPhrases 詞庫是為 Windows／一般軟體 UI 設計的，套進 AI/ML 語境會誤轉。
# 這些是單次轉換就錯的詞（與雙層轉換無關），轉完後統一改回。
# 只收「在本專案語境幾乎不可能是對的」的詞——會兩可的（元件 / 最佳化）不列入。
#
# 本表**無守門、兩層都套**：修的是「詞彙選錯 / 該轉而沒轉」，與輸入含不含簡體無關。
# 需要守門的那類（OpenCC 挑錯繁體分支）在下面的 `_VARIANT_FIXES`，兩者請勿合併。
_TERM_FIXES = {
    # ── s2twp 誤轉：轉了但選錯詞 ──
    # `引數` 不列在這裡——它需要負向後顧，見 `_YINSHU_RE`。
    "擴充套件": "擴展",  # 扩展 extension
    "解除安裝": "卸載",  # 卸载 offload（非軟體 uninstall）
    "區域性": "局部",  # 局部 local / partial
    "繫結": "綁定",  # 绑定 binding
    "控制元件": "控制項",  # 控件 widget
    # ── s2twp 1.3.x 漏轉：1.4 修對了，但 1.4 另有不可逆的災難性退步
    #    （`B超→超音波` 無詞邊界，吃掉 `753B超大參數`），故留在 1.3 並在此收割。
    #    量測依據見 2026-07-31 的全語料版本評估（32,950 個去重欄位）。
    "想象": "想像",  # 46 處；台灣標準寫法
    "市場營銷": "市場行銷",  # 6 處；台灣說「行銷」
}


# `参数`→`引數` 是 s2twp 的誤轉，但 `引數` 這兩個字也會由「動詞＋引」＋「數」
# 自然拼出來，定值替換會把它改壞：
#
#     該獎項每年吸引數百款產品參選  →  每年吸參數百款   ← 語料實測 1 處
#
# 全語料掃過的安全前綴只有這五個（`索引數`／`牽引數`／`指引數`／`援引數` 目前
# 0 例，一併擋住是因為它們與 `吸引數` 同構，出現只是時間問題）。
# 這條沒有跟其他條目一起放進 `_TERM_FIXES`，是因為 `str.replace` 表達不了負向後顧。
_YINSHU_RE = re.compile(r"(?<![吸牽指索援])引數")


def _apply_term_fixes(text: str) -> str:
    text = _YINSHU_RE.sub("參數", text)
    for wrong, right in _TERM_FIXES.items():
        text = text.replace(wrong, right)
    return text


# 明明是**正字繁體**、OpenCC 卻在單字元層級就會改寫的字，不採計為「這個欄位含簡體」
# 的證據。`干擾`/`干預`、`托盤`/`委托` 在台灣繁體是天天出現的正常用字，但
# `s2tw('干') == '幹'`、`s2tw('托') == '託'`——把它們當簡體證據，等於讓一整個
# 純繁體欄位過門，接著被詞組規則改壞。與 `repair.py` 共用同一份定義。
#
# `污`（2026-08-02 追加）：`s2tw('污') == '汙'`。兩字皆通、教育部以「汙」為主，
# 但 AI 語料裡「資料污染 / 上下文污染」是既有寫法，不該由轉換層代為統一。
# 它同時是 Layer B 守門的判準，漏掉會讓純繁體句子被改成「資料汙染」。
_NOT_SIMPLIFIED_EVIDENCE = frozenset("干托污")


@lru_cache(maxsize=None)
def _is_simplified_char(ch: str) -> bool:
    """這個字元是否可作為「該欄位含簡體」的證據。

    「單字元」是關鍵：OpenCC 的詞組規則要有上下文才會觸發，餵單一字元等於只問
    「這個字本身會不會被改寫」。**別把它想成「是不是簡體字」**——實測
    `s2tw('里')='裡'`、`s2tw('干')='幹'`、`s2tw('托')='託'` 都會變，但這三個字在
    繁體正文裡本來就大量出現；只有 `了` / `面` / `杆` / `只` 這類才是真的單字元
    不動、純靠詞組規則才被改寫。

    OpenCC 不可用時一律判定為非簡體 → 變體修正與 Layer B 守門整個退化成 no-op，
    這是刻意的安全降級。

    why 直接用 `_opencc_shape_converter` 而不是 `to_traditional_shape_only()`：
    後者自 2026-08-02 起會呼叫本函式做守門，走回去就是無限遞迴。單一字元不會
    觸發 `_TERM_FIXES`（表裡沒有單字條目），兩者對單字元的結果等價。
    """
    if ch in _NOT_SIMPLIFIED_EVIDENCE:
        return False
    if not _init_opencc():
        return False
    return _opencc_shape_converter.convert(ch) != ch


# ──────────────────────────────────────────────────────────
# 變體修正表：把 OpenCC 在「一簡對多繁」上挑錯的分支改回來。
#
# ## 為什麼在 Layer A 也要有這張表（2026-07-31 從 `repair.py` 搬上來）
#
# `repair-content` 的同一張表只能補歷史；`to_traditional()` 才是**所有新資料的
# 生產路徑**，每天仍在產同一批錯字（`更复杂`→`更復雜`、`死胡同`→`死衚衕`、
# `克制`→`剋制`）。實測 41 條裡 28 條在 Layer A 路徑真的會被觸發。
#
# ## 為什麼要守門（與 `_TERM_FIXES` 的關鍵差別）
#
# 本表修的是「**轉換過程中**挑錯分支」，這種錯只可能發生在真的被轉換的文字上；
# 沒被轉換的文字套這張表**只有誤傷、沒有收益**。實測會被無條件套用改壞的正確繁體：
#
#   託馬斯 ← 「董事會委託馬斯克主導收購」→ 委托馬斯克   ← AI 新聞高頻，最危險
#   係統化 ← 「把關係統化條列出來」    → 把關系統化
#   剋制  ← 「五行相剋制衡的道理」    → 相克制衡
#   穀底  ← 「稻穀底部的含水率」      → 稻谷底部
#   曆史  ← 「農民曆史上首次數位化」   → 農民歷史上
#   總檯  ← 「把總檯帳搬到雲端」      → 總臺帳
#   一齣來 ← 「看完這一齣來評論」      → 這一出來
#
# 這些反例由 `tests/test_to_traditional.py::TestVariantFixGateProtectsTraditional` 釘住。
#
# ## 條目為什麼幾乎都帶脈絡
#
# 凡是「錯字字串」可能跨詞邊界撞到正常文字的，一律用實測到的脈絡加長，並在註解
# 寫出被擋掉的反例。脈絡是從**全語料的全部出現位置**枚舉出來的，不是抽樣。
#
# 表裡有 13 條在 Layer A 路徑不會觸發（s2twp 本來就轉對，它們是 repair 走的
# s2tw 路徑專屬）。刻意保留：守門下不會誤觸發，且是 OpenCC 行為變動時的防線。
_VARIANT_FIXES = {
    # ── ① 守門失效：欄位靠別的合法繁體字過門，純繁體被詞組規則改壞 ──
    # 幹擾 / 幹預 帶左脈絡：語料裡有「骨幹」，通用寫法會撞到「骨幹擾動」「骨幹預備」
    "過濾幹擾": "過濾干擾",
    "受到幹擾": "受到干擾",
    "一次幹預": "一次干預",
    "人工幹預": "人工干預",
    "接管幹預": "接管干預",
    "臺積電": "台積電",  # 專有名詞；一般的 `平臺` 是正確台灣用法，刻意不收
    "穀底": "谷底",  # 士氣跌至 20 年谷底（`穀` 是穀物，語料 0 個合法用法）
    "託馬斯": "托馬斯",  # Thomas Kurian
    "藍色遊標": "藍色游標",  # 公司名；通用的 `遊標→游標` 會弄壞「旅遊標籤」
    "/遊資": "/游資",  # 前綴 `/` 擋掉「旅遊資訊」
    # ── ② OpenCC 消歧錯誤：整段簡體該轉，但挑錯分支 ──
    # 托盤三條帶左脈絡：語料裡就有股市工具 README，通用寫法會弄壞「委託盤」「信託盤」
    "/託盤": "/托盤",
    "金屬託盤": "金屬托盤",
    "載物託盤": "載物托盤",
    # 復雜三條帶左脈絡：通用寫法會弄壞「修復雜湊表」「恢復雜亂的狀態」
    "不復雜": "不複雜",
    "更復雜": "更複雜",
    "執行復雜": "執行複雜",
    # 瞭 三條帶右脈絡：通用的 `說明瞭→說明了` 會弄壞「說明瞭解決方案」
    "證明瞭太多": "證明了太多",
    "說明瞭一件": "說明了一件",
    "目睹瞭如今": "目睹了如今",
    "一齣來": "一出來",  # `齣` 只用於戲曲量詞
    # 「搞定并发布」是「搞定 + 並發布（and publish）」，被挑成併發（concurrency）。
    "搞定併發布": "搞定並發布",
    # 乾（dry）被挑來當「幹（做）」；通用的 `乾的→幹的` 會弄壞「曬乾的衣服」
    "乾的就是": "幹的就是",
    "乾的是": "幹的是",
    "該乾的活": "該幹的活",
    "它乾的活": "它幹的活",
    # 發（發生）被挑成髮（頭髮），因為 OpenCC 把「结发」當成「結髮」詞組。
    # 必須帶左錨定：通用的 `髮生→發生` 會弄壞「頭髮生長」。
    "總結髮生": "總結發生",
    "總髮生": "總發生",
    # 注（投資加碼，同賭注）被挑成註（註解）。全語料 17 筆脈絡皆為投資
    # （「產業與全球資本共同加註，愛詩科技完成 29.8 億元 C 輪融資」），
    # 但 `加註說明`／`加註釋` 是合法用法，故一律帶左錨定，不收通用的 `加註`。
    "共同加註": "共同加注",
    "持續加註": "持續加注",
    "資本加註": "資本加注",
    "輪加註": "輪加注",  # 涵蓋「三輪／兩輪／連續三輪加注」
    "重磅加註": "重磅加注",
    "超額加註": "超額加注",
    # 隻（量詞）被挑來當「只」；帶右脈絡是因為語料裡就有正確的量詞用法
    "不是隻寫": "不是只寫",
    "不是隻面": "不是只面",
    "不是隻在": "不是只在",
    "不是隻返": "不是只返",
    "這隻會營造": "這只會營造",
    # ── ③ 第一順位就挑錯（`s2tw('签')='籤'` 等預設值本身就不對）──
    "合並請求": "合併請求",
    "在籤什麼": "在簽什麼",
    "一起籤的": "一起簽的",
    # 音譯名一律用共用字形（里）。**必須用間隔號錨定**：通用的 `庫裡安→庫里安`
    # 會弄壞「資料庫裡安放著索引」這種在本領域極自然的句子。
    "·庫裡安": "·庫里安",
    # ── ④ target-side 掃描抓到的 ──
    "曆史": "歷史",  # 27 年歷史；`日曆` 不受影響
    "總檯": "總臺",  # 央視總臺
    "聯閤": "聯合",
    "係統化": "系統化",  # 帶 `化`：通用的 `係統→系統` 會弄壞「關係統計」
    "剋制": "克制",  # 教育部標準寫法
    "死衚衕": "死胡同",  # 教育部標準寫法
    "揹負": "背負",  # 教育部標準寫法
    # ── ⑤ 2026-08-02 `opencc-candidates` 第一輪審查（81 pattern → 64 rejected）──
    # 這批的差別是**候選來自工具而非人工逐句判讀**：歧義組用 OpenCC 自己的字典建
    # （2800 組），候選經「三表覆蓋 → 帳本 → ≥2 篇不同文章」三道過濾，錨定 key 再對
    # 全語料 91 天 12830 筆實跑驗證。下面每條的命中數就是那次驗證的數字，誤傷皆為 0。
    # 裁決紀錄見 `data/opencc/decisions.jsonl`，草案與逐條反例見
    # `docs/superpowers/plans/2026-08-02-opencc-round1-accept-draft.md`。
    "伙伴": "夥伴",  # 15；反例 傢伙/好傢伙/大傢伙（皆不含「伙伴」）
    # 髮（頭髮）被挑來寫「發」：**key 必須帶動詞尾**。語料裡 美容美髮/髮質/髮型/
    # 頭髮 才是多數用法，通用的 `髮→發` 會全毀。
    "髮起": "發起",  # 7
    "髮掘": "發掘",
    "髮明": "發明",
    "黃髮了": "黃發了",  # 老黃髮了一條推；`髮了` 單獨用會撞到「頭髮了」
    "鉅頭": "巨頭",  # 5；`鉅` 在台灣只用於「鉅細靡遺」
    "鉅作": "巨作",  # 3
    "鉅額": "巨額",
    # 隻（量詞）被挑來寫副詞「只」：全部帶「是」左錨定，否則會弄壞 一隻手/兩隻/這隻。
    "是隻靠": "是只靠",  # 2
    "是隻能": "是只能",
    "是隻要": "是只要",
    "是隻把": "是只把",
    # 阿里雲「百煉」是產品名。**不可用通用的 `百鍊`**——「千錘百鍊」是正確寫法，
    # 且「鍛鍊」在語料大量出現。
    "雲百鍊": "雲百煉",  # 3
    "線百鍊": "線百煉",  # 5（上線百鍊提供）
    "百鍊M": "百煉M",  # 百鍊MCP
    "百鍊或": "百煉或",
    "公有云": "公有雲",  # 6；反例 古人云（文言助詞）
    "阿里云云": "阿里雲雲",  # 阿里云云監控；**兩個 云 都要換**，只換前一個仍是錯的
    "多采用": "多採用",  # 2；反例 文采/興高采烈/多采多姿
    "多采一": "多採一",  # 多采一點影片
    "下采集": "下採集",  # 省下采集資料的錢
    "和麵向": "和面向",  # 2；反例 麵包/撈麵/一碗麵——「和麵」本身也是詞，故帶右脈絡
    "和麵對": "和面對",  # 和麵對面交流
    "儀錶板": "儀表板",  # 反例 錶盤（手錶）
    "對錶現": "對表現",  # 相對錶現
    "綵線": "彩線",  # 2；反例 剪綵/綵帶/張燈結綵
    "全綵": "全彩",  # 全綵 AR
}


# 方位的「里」（該寫「裡」）。**不放進 `_VARIANT_FIXES` 是因為 `str.replace`
# 表達不了負向前瞻**，理由與 `_YINSHU_RE` 相同：
#
#     賽道里最不缺的  → 賽道裡最不缺的   ← 要修
#     賽道里程 / 通道里程 / 網格里程     ← 不能碰，`里程` 是正確用字
#
# 語料裡 公里 / 里程碑 / 阿里 / 庫里安 / 拉里·古斯 / 千里科技 全是正確用字，
# 通用的 `里→裡` 會把它們全部改壞——所以左側逐個列出實測到的容器名詞（全部 2 字，
# Python 的 lookbehind 要求定寬），右側用 `(?!程)` 擋掉 `里程`。
#
# 實測命中 24 處、誤傷 0 處。書名號版本（`《魔獸世界》里人機`）刻意不收：`》里`
# 會撞到「《報告》里程碑」，而它只有 1 處，不值得為它放寬。
_LOCATIVE_LI_RE = re.compile(
    r"(?<=頻道|賽道|文本|電路|網格|過程|副本|渠道|通道|應用|年多)里(?!程)"
)


def _apply_variant_fixes(text: str) -> str:
    text = _LOCATIVE_LI_RE.sub("裡", text)
    for wrong, right in _VARIANT_FIXES.items():
        if wrong in text:
            text = text.replace(wrong, right)
    return text


def _init_opencc() -> bool:
    """Lazy 建立兩個 converter。回傳 False 代表 OpenCC 不可用（呼叫端原樣回傳）。"""
    global _opencc_converter, _opencc_shape_converter, _opencc_unavailable
    if _opencc_unavailable:
        return False
    if _opencc_converter is not None:
        return True
    try:
        from opencc import OpenCC

        _opencc_converter = OpenCC("s2twp")  # 字形 + 台灣慣用詞
        _opencc_shape_converter = OpenCC("s2tw")  # 只有字形（台灣正字），不含詞庫
        return True
    except Exception as e:
        _opencc_unavailable = True
        _logger.warning(
            "OpenCC unavailable, skipping 簡→繁 conversion",
            extra={"error": str(e)[:160]},
        )
        return False


def to_traditional(text: str) -> str:
    """Layer A（來源端）：簡體 → 繁體，含台灣慣用詞轉換。

    用於量子位 / ChatPaper 等中國 source 的 title / abstract / tags——這些欄位
    整段都是簡體，需要詞彙級轉換（软件→軟體、内存→記憶體、插件→外掛）。

    轉換後套 `_TERM_FIXES`，修掉 s2twp 在 AI/ML 語境的誤轉（参数→引數 等）。

    **不要拿這個處理已是繁中的文字**——s2twp 對繁體不冪等（文件→檔案），
    生成端請改用 `to_traditional_shape_only()`。

    最後套 `_VARIANT_FIXES`，但**只在輸入真的含簡體字時**——理由與反例見該表註解
    （無條件套用會把「委託馬斯克」改成「委托馬斯克」）。
    """
    if not text or not _init_opencc():
        return text
    try:
        out = _apply_term_fixes(_opencc_converter.convert(text))
        if any(_is_simplified_char(c) for c in text):
            out = _apply_variant_fixes(out)
        return out
    except Exception as e:
        _logger.debug("to_traditional failed", extra={"error": str(e)[:160]})
        return text


def _gate_conversion(original: str, converted: str) -> str:
    """逐段守門：只採納「原片段真的含簡體」的變更，其餘保留原文。

    s2tw 沒有 TWPhrases 詞庫，但**仍帶 TWVariants 的一簡對多繁分歧規則**，這些
    規則靠上下文挑分支，對純繁體輸入照樣改寫。全語料實測的高頻誤改：

        證明了 → 證明瞭 (171)   儀表板 → 儀錶板 (25)   定制 → 定製 (14)
        只是   → 隻是           局限   → 侷限 (30)     污染 → 汙染 (29)

    守門判準沿用 `_is_simplified_char()`（含 `干`/`托` 的例外表）。**不可改用
    `OpenCC("s2t")` 判**：`s2t('干') == '幹'`，「受到干擾」會過門後變「受到幹擾」。

    insert opcode（原片段為空）一律否決——s2tw 是字元級對映，不該憑空長出字。
    """
    parts: list[str] = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(
        None, original, converted, autojunk=False
    ).get_opcodes():
        seg = original[i1:i2]
        if tag == "equal" or any(_is_simplified_char(c) for c in seg):
            parts.append(converted[j1:j2])
        else:
            parts.append(seg)
    return "".join(parts)


def to_traditional_shape_only(text: str) -> str:
    """Layer B（生成端）：只修字形，不動詞彙。

    LLM 產出的內容本來就該是繁中，Layer B 存在只為擦掉免費 model 偶發吐出的
    簡體字（如 Agnes 的「应」）。若這裡也套 s2twp 的詞庫，會把 Layer A 已經
    轉好的繁體詞再轉一次——「文档」→（A）「文件」→（B）「檔案」，這正是
    站上「最新程式庫檔案餵進 LLM」的來源。

    **s2tw 對繁體輸入並不冪等**（本 docstring 在 2026-08-02 前宣稱它冪等，是
    錯的）——一簡對多繁的分歧規則會把「證明了」改成「證明瞭」。因此轉換結果
    必須再過 `_gate_conversion()`，只放行原文真的含簡體的片段。

    `_TERM_FIXES` 排在守門之後：它修的是「詞彙選錯」，無守門、兩層都套。
    """
    if not text or not _init_opencc():
        return text
    try:
        converted = _opencc_shape_converter.convert(text)
        return _apply_term_fixes(_gate_conversion(text, converted))
    except Exception as e:
        _logger.debug("to_traditional_shape_only failed", extra={"error": str(e)[:160]})
        return text


# ──────────────────────────────────────────────────────────
# 多 provider 路由 + 各自多 key 輪替 + 多 model 降級
#
# 同一條 chain 可混用不同 provider 的 model：由 model id 推斷 provider
# （agnes-* → agnes，其餘 → openrouter），各 provider 有獨立的 base_url
# 與 key 池。Agnes（apihub.agnes-ai.com）作為 OpenRouter 免費 model 全掛時的
# 可用性保險，放在 generation chain 末端。
# ──────────────────────────────────────────────────────────

_AGNES_DEFAULT_BASE_URL = "https://apihub.agnes-ai.com/v1"


def _load_keys(prefix: str) -> list[str]:
    """讀取 PREFIX, PREFIX_2 .. PREFIX_9 的 API keys（缺的略過）。"""
    keys: list[str] = []
    for suffix in ["", "_2", "_3", "_4", "_5", "_6", "_7", "_8", "_9"]:
        k = os.getenv(f"{prefix}{suffix}", "")
        if k:
            keys.append(k)
    return keys


_PROVIDER_KEYS: dict[str, list[str]] = {
    "openrouter": _load_keys("OPENROUTER_API_KEY"),
    "agnes": _load_keys("AGNES_API_KEY"),
}

# Lazy 檢查：不在 import 時 raise，讓不需 LLM 的指令（clean / status / list）
# 即使沒設定 API key 也能正常執行；真正呼叫 LLM 時才在 get_next_api_key() raise。
# cycle 元素為 (序號, key) pair：序號 1-based，供 log 記 key#N（key 值絕不入 log）。
_PROVIDER_CYCLES: dict[str, "itertools.cycle | None"] = {
    p: (itertools.cycle(enumerate(ks, 1)) if ks else None) for p, ks in _PROVIDER_KEYS.items()
}
for _p, _ks in _PROVIDER_KEYS.items():
    if _ks:
        _logger.info("API keys loaded", extra={"provider": _p, "key_count": len(_ks)})

# 執行期可被 lazy retire / 緊急 discover 修改的 healthy model chains（None 代表尚未載入）
_scoring_chain: list[str] | None = None
_generation_chain: list[str] | None = None

# 本次 run 已判死的 model：404（下架）或上游池限流（換 key/backoff 無效，唯換 model）。
# 換 model 才有效，故整輪跳過；下次 process 重啟或 reset_model_health() 才復活。
_RETIRED_MODELS: set[str] = set()

# 緊急 auto-discover 防重入 flag（chain 全空時才觸發一次，平常零成本）。
_emergency_discovered = False


def reset_model_health() -> None:
    """清空 retired set + 重設快取 chain + 緊急 discover flag。

    供測試隔離與長駐 process（如 web monitor 跨日 run）復活被 retire 的 model 用。
    """
    global _scoring_chain, _generation_chain, _emergency_discovered
    _RETIRED_MODELS.clear()
    _scoring_chain = None
    _generation_chain = None
    _emergency_discovered = False


def _provider_for_model(model: str | None) -> str:
    """由 model id 推斷 provider。agnes-* 走 Agnes，其餘預設 OpenRouter。"""
    if model and model.startswith("agnes"):
        return "agnes"
    return "openrouter"


def _get_api_base_url(provider: str = "openrouter") -> str:
    if provider == "agnes":
        return os.getenv("AGNES_API_URL") or _AGNES_DEFAULT_BASE_URL
    url = os.getenv("OPENROUTER_API_URL")
    if url:
        return url
    config = load_config()
    return config.get("llm", {}).get("api_url", "https://openrouter.ai/api/v1")


def _next_key_with_index(provider: str = "openrouter") -> tuple[str, int]:
    """Round-robin 取得指定 provider 的下一個 (key, 1-based 序號)。
    無 key 時才 raise（lazy，僅在真正呼叫該 provider 時）。"""
    cycle = _PROVIDER_CYCLES.get(provider)
    if cycle is None:
        env = "OPENROUTER_API_KEY" if provider == "openrouter" else "AGNES_API_KEY"
        raise ValueError(f"No API keys configured for provider '{provider}' (set {env}[_2..9])")
    idx, key = next(cycle)
    return key, idx


def get_next_api_key(provider: str = "openrouter") -> str:
    """Round-robin 取得指定 provider 的下一個 API key。
    無 key 時才 raise（lazy，僅在真正呼叫該 provider 時）。"""
    return _next_key_with_index(provider)[0]


def _client_with_key_index(model: str | None = None) -> tuple[OpenAI, int]:
    """建立輪替 key 的 client，同時回傳該 key 的 1-based 序號（供 log 記 key#N）。"""
    provider = _provider_for_model(model)
    key, idx = _next_key_with_index(provider)
    return OpenAI(api_key=key, base_url=_get_api_base_url(provider)), idx


def get_llm_client(model: str | None = None) -> OpenAI:
    """建立帶有輪替 key 的 OpenAI-compatible client。依 model 推斷 provider，
    選對應 base_url 並輪替該 provider 的 key。model=None 時預設 OpenRouter。"""
    return _client_with_key_index(model)[0]


def _extract_content(resp) -> str:
    msg = resp.choices[0].message
    if msg.content:
        return msg.content
    # reasoning model 在 max_tokens 被推理吃光時 content 為空：
    # DeepSeek R1 放 reasoning_content，OpenRouter（gpt-oss 等）放 reasoning
    reasoning = getattr(msg, "reasoning_content", None) or getattr(msg, "reasoning", None)
    return reasoning or ""


_BACKOFF_BASE_SECONDS = 5
_BACKOFF_CAP_SECONDS = 60


def _status_code_of(exc) -> int | None:
    """防禦式取 HTTP status code：先 openai SDK 的 .status_code，fallback 掃字串；都沒有回 None。"""
    code = getattr(exc, "status_code", None)
    if isinstance(code, int):
        return code
    import re
    m = re.search(r"\b([45]\d\d)\b", str(exc))
    return int(m.group(1)) if m else None


def _upstream_provider(exc) -> str | None:
    """從 openai SDK exception 解析上游 provider 名稱（上游池限流的判別依據）。

    OpenRouter body 約為 {"error": {"code": 429, "metadata": {"provider_name": "Venice",
    "raw": "... temporarily rate-limited upstream ..."}}}；SDK 有時把 error 內層直接當 body。
    任何形狀不符（無 body / 非 dict / 無 metadata / 無 provider_name）一律回 None，絕不 raise。
    """
    try:
        body = getattr(exc, "body", None)
        if not isinstance(body, dict):
            return None
        # SDK 有時把 error 內層直接當 body；有 error dict 就往內鑽，否則就地取
        inner = body.get("error")
        err = inner if isinstance(inner, dict) else body
        meta = err.get("metadata")
        if not isinstance(meta, dict):
            return None
        name = meta.get("provider_name")
        return name if isinstance(name, str) and name else None
    except Exception:
        return None


def _try_model(
    model: str,
    messages: list[dict],
    max_tokens: int,
    temperature: float,
    max_retries: int,
    timeout: float = 60.0,
) -> str | None:
    """單一 model 呼叫（每次 attempt 內建新 client → 429 retry 時輪替 key）。

    429 分兩種（實測確認）：
    - 上游池限流（body 帶 provider_name）：換 key/backoff 均無效，唯一有效動作是換 model，
      故將 model 加入 _RETIRED_MODELS，零重試零 backoff 直接回 None。
    - 我方帳號額度（無 provider_name）：指數退避重試（5s→10s→20s，上限 60s），每次換 key。
    404（model 下架）：加入 _RETIRED_MODELS，回 None。
    timeout / 其他 error / empty content：視為該 model 本次失敗回 None，讓上層走 fallback 鏈。
    key 值絕不入 log，只記序號 key#N。
    """
    for attempt in range(max_retries + 1):
        client, key_idx = _client_with_key_index(model)
        try:
            resp = client.with_options(timeout=timeout).chat.completions.create(
                model=model, messages=messages,
                max_tokens=max_tokens, temperature=temperature,
            )
            content = _extract_content(resp)
            return content or None
        except Exception as e:
            err = str(e)
            status = _status_code_of(e)

            # 404：model 下架 → 本次 run retire，不重試
            if status == 404 or "404" in err:
                _RETIRED_MODELS.add(model)
                _logger.warning(
                    "Model not found, retired for this run",
                    extra={"model": model, "status_code": 404},
                )
                return None

            # 429
            if status == 429 or "429" in err:
                provider_name = _upstream_provider(e)
                if provider_name:
                    # 上游池限流：換 key/backoff 無效 → retire，零重試直接降級下一 model
                    _RETIRED_MODELS.add(model)
                    _logger.warning(
                        "Upstream provider rate-limited, retiring model for this run",
                        extra={"model": model, "status_code": status,
                               "provider_name": provider_name, "key": f"key#{key_idx}"},
                    )
                    return None
                # 我方帳號額度：指數退避重試，下次 attempt 會換新 key
                if attempt < max_retries:
                    wait = min(_BACKOFF_BASE_SECONDS * (2 ** attempt), _BACKOFF_CAP_SECONDS)
                    _logger.warning(
                        "Rate limited (account quota), retrying with next key",
                        extra={"model": model, "wait_seconds": wait,
                               "attempt": attempt + 1, "key": f"key#{key_idx}"},
                    )
                    time.sleep(wait)
                    continue
                _logger.warning(
                    "Rate limited, retries exhausted",
                    extra={"model": model, "status_code": status, "key": f"key#{key_idx}"},
                )
                return None

            # 其他 error（含 timeout）：視為該 model 本次失敗
            _logger.warning(
                "Model call failed",
                extra={"model": model, "status_code": status,
                       "error": err[:200], "key": f"key#{key_idx}"},
            )
            return None
    return None


def _load_default_chains() -> tuple[list[str], list[str]]:
    """從 config.yaml 讀取 scoring_models / generation_models。缺失時退回 legacy 單 model。"""
    cfg = load_config().get("llm", {})
    scoring = list(cfg.get("scoring_models") or [])
    generation = list(cfg.get("generation_models") or [])
    # legacy fallback：舊 config 只有 model / generation_model
    if not scoring and cfg.get("model"):
        scoring = [cfg["model"]]
        if cfg.get("fallback_model"):
            scoring.append(cfg["fallback_model"])
    if not generation and cfg.get("generation_model"):
        generation = [cfg["generation_model"]]
        if cfg.get("generation_fallback_model"):
            generation.append(cfg["generation_fallback_model"])
    return scoring, generation


def _get_chain(is_generation: bool) -> list[str]:
    global _scoring_chain, _generation_chain
    if _scoring_chain is None or _generation_chain is None:
        s, g = _load_default_chains()
        _scoring_chain = s
        _generation_chain = g
    return _generation_chain if is_generation else _scoring_chain


def _probe_model(model: str, timeout: float = 15.0) -> tuple[bool, str]:
    """對單一 model 送最小 probe call。回傳 (alive, err_msg)。"""
    # 指令式 prompt 比 "ping" 更能穩定觸發輸出；空內容視為失效，
    # 避免雖在架但回空字串的 model 進 chain 後生成出空白文章（06-05 timeout 教訓）。
    # 健康 model 偶發回空，故對空回應 retry 一次以吸收抖動、避免誤殺。
    # 429 視為 alive（「忙」非「死」）：免費 model 起頭常碰每分鐘限流，
    # 但 runtime 有 4 key 輪替 + request_delay 間隔可吸收，不該整輪移出 chain。
    last_err = "empty content"
    for _attempt in range(2):
        try:
            # provider-aware：Agnes model 用 Agnes endpoint probe，否則 preflight 會
            # 拿 OpenRouter endpoint 去 probe Agnes 而誤判其死亡（fallback 保全關鍵）。
            resp = get_llm_client(model).with_options(timeout=timeout).chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": "Reply with the single word: OK"}],
                max_tokens=16, temperature=0.0,
            )
            if _extract_content(resp).strip():
                return True, ""
        except Exception as e:
            err = str(e)
            if "429" in err:
                return True, ""
            return False, err[:200]
    return False, last_err


def discover_free_models(min_context: int = 32000, limit: int = 12) -> list[str]:
    """向 OpenRouter /models 查詢 pricing 全為 0 的 model，按 context 降序排序。
    用於 preflight 發現 configured chain 全死時的 auto-fallback 池。"""
    try:
        url = _get_api_base_url().rstrip("/") + "/models"
        key = get_next_api_key()
        r = httpx.get(url, headers={"Authorization": f"Bearer {key}"}, timeout=15)
        data = r.json().get("data", [])
    except Exception as e:
        _logger.warning("discover_free_models: API call failed", extra={"error": str(e)[:160]})
        return []

    free = []
    for m in data:
        pricing = m.get("pricing") or {}
        if pricing.get("prompt") == "0" and pricing.get("completion") == "0":
            ctx = m.get("context_length") or 0
            if ctx >= min_context:
                free.append((m["id"], ctx))
    free.sort(key=lambda x: -x[1])
    return [mid for mid, _ in free[:limit]]


_LAST_RESORT_MODEL = "openrouter/free"
"""OpenRouter 官方 meta-model，pricing 0，能力弱但穩定。chain 全空時的最後保底。"""


def preflight_models(
    timeout: float = 15.0,
    auto_discover: bool = True,
    discover_probe_limit: int = 4,
) -> dict:
    """Pipeline 起頭 probe 所有配置的 model，失效者從 chain 移除。
    若任一 chain（scoring / generation）全空，且 `auto_discover=True`，
    依序嘗試補救：
      1. 查 OpenRouter 免費池（`discover_free_models`）找替補
      2. 若仍空，加上 `openrouter/free` meta-model 保底（慢但穩定）

    回傳 {'scoring': [...], 'generation': [...], 'dead': [...],
           'discovered': [...], 'last_resort': bool}。
    """
    global _scoring_chain, _generation_chain
    scoring, generation = _load_default_chains()
    candidates = list(dict.fromkeys(scoring + generation))

    alive: set[str] = set()
    dead: list[tuple[str, str]] = []

    for m in candidates:
        ok, err = _probe_model(m, timeout)
        if ok:
            alive.add(m)
            _logger.info("Preflight OK", extra={"model": m})
        else:
            dead.append((m, err))
            _logger.warning("Preflight failed", extra={"model": m, "error": err[:160]})

    scoring_alive = [m for m in scoring if m in alive]
    generation_alive = [m for m in generation if m in alive]
    discovered: list[str] = []

    # Auto-discover：任一 chain 全空時去 OpenRouter 免費池找替補
    if auto_discover and (not scoring_alive or not generation_alive):
        _logger.info("Auto-discover: chain empty, querying free pool")
        pool = discover_free_models()
        # 排除已 probe 過的 candidates，避免重複 probe
        pool = [m for m in pool if m not in candidates][:discover_probe_limit]
        for m in pool:
            ok, err = _probe_model(m, timeout)
            if ok:
                discovered.append(m)
                _logger.info("Auto-discover: model alive", extra={"model": m})
            else:
                dead.append((m, err))
                _logger.debug("Auto-discover: model dead", extra={"model": m, "error": err[:160]})

        # 把探索到的附在對應 chain 末端（不覆蓋 configured 偏好）
        if not scoring_alive:
            scoring_alive = list(discovered)
        if not generation_alive:
            generation_alive = list(discovered)

    # Last resort：仍然空 → 試 openrouter/free meta-model（保底）
    last_resort = False
    if auto_discover and (not scoring_alive or not generation_alive):
        _logger.info("Last resort: probing openrouter/free meta-model")
        ok, err = _probe_model(_LAST_RESORT_MODEL, timeout)
        if ok:
            last_resort = True
            _logger.info("Last resort: openrouter/free alive")
            if not scoring_alive:
                scoring_alive = [_LAST_RESORT_MODEL]
            if not generation_alive:
                generation_alive = [_LAST_RESORT_MODEL]
        else:
            dead.append((_LAST_RESORT_MODEL, err))
            _logger.error("Last resort dead — pipeline 無可用 model", extra={"error": err[:160]})

    _scoring_chain = scoring_alive
    _generation_chain = generation_alive
    return {
        "scoring": list(_scoring_chain),
        "generation": list(_generation_chain),
        "dead": dead,
        "discovered": discovered,
        "last_resort": last_resort,
    }


def _emergency_discover(is_generation: bool) -> list[str]:
    """chain 全空（全部 retired 或 config 空）時的一次性自救。

    保留原 preflight 的「全滅時自救」能力，但平常零成本（只在 chain 空且尚未觸發過時跑）：
    查 OpenRouter 免費池、排除 retired、最多 probe 3 個，活的接到快取 chain 供本次及後續呼叫用。
    module 級 flag 確保整個 process 只觸發一次，避免每次 llm_chat 都白燒 discover/probe 請求。
    """
    global _emergency_discovered, _scoring_chain, _generation_chain
    if _emergency_discovered:
        return []
    _emergency_discovered = True
    _logger.warning("llm_chat: chain empty, 觸發緊急 auto-discover")

    pool = [m for m in discover_free_models() if m not in _RETIRED_MODELS]
    alive: list[str] = []
    for m in pool[:3]:
        ok, _err = _probe_model(m)
        if ok:
            alive.append(m)

    if alive:
        # 接到兩條快取 chain（此時原 chain 已空，不存在覆蓋偏好問題）
        _scoring_chain = list(dict.fromkeys((_scoring_chain or []) + alive))
        _generation_chain = list(dict.fromkeys((_generation_chain or []) + alive))
        _logger.info("緊急 auto-discover 成功", extra={"discovered": alive})
    return alive


def llm_chat(
    messages: list[dict],
    model: str | None = None,
    max_tokens: int | None = None,
    temperature: float = 0.7,
    max_retries: int = 2,
    fallback_model: str | None = None,
    is_generation: bool = False,
    timeout: float | None = None,
    validate: Callable[[str], bool] | None = None,
) -> str:
    """走多 model chain。每個 model 嘗試一次，失敗降級。全部失敗回傳 ""。

    - `model` / `fallback_model`：caller 指定偏好；若不在 chain 中則前置插入。
    - `is_generation=True` 使用 generation chain，否則使用 scoring chain。
    - `timeout`：單次 LLM 呼叫逾時秒數；None 時讀 config `llm.timeout_seconds`（預設 60）。
    - `validate`：model 回了內容但 validate(content) 為 False 時視為該 model 本次輸出爛，
      記 warning 並降級下一 model（**不** retire——model 活著只是這次輸出爛）。
    - 本次 run 已 retire 的 model（404 / 上游 429）自動從 chain 過濾。
    """
    cfg = load_config()["llm"]
    max_tokens = max_tokens or cfg.get("max_tokens", 8192)
    if timeout is None:
        timeout = cfg.get("timeout_seconds", 60)

    chain = list(_get_chain(is_generation))
    # caller 偏好插在最前面（去重）
    for pref in (model, fallback_model):
        if pref and pref not in chain:
            chain.insert(0, pref)

    # 過濾本次 run 已 retire 的 model（含 caller 前置插入的偏好）
    chain = [m for m in chain if m not in _RETIRED_MODELS]

    # 緊急補救：過濾後全空（全部 retired 或 config 空）→ 一次性 auto-discover
    if not chain:
        chain = _emergency_discover(is_generation)

    if not chain:
        _logger.error("llm_chat: empty model chain (全部 retired 或 config 空, auto-discover 亦無補救)")
        return ""

    for m in chain:
        result = _try_model(m, messages, max_tokens, temperature, max_retries, timeout)
        if result is None:
            _logger.warning("Model failed, trying next in chain", extra={"model": m})
            continue
        if validate is not None and not validate(result):
            _logger.warning("Response failed validation, falling through", extra={"model": m})
            continue
        return result

    _logger.error("All LLM models failed", extra={"tried": chain})
    return ""


def get_http_client() -> httpx.Client:
    return httpx.Client(
        timeout=30,
        headers={"User-Agent": "AutoPostBlog/0.1"},
        follow_redirects=True,
    )


def today_str() -> str:
    return date.today().isoformat()


def date_to_chatpaper_ts(d: date) -> int:
    """將 date 轉換為 ChatPaper API 的 Unix timestamp（Asia/Taipei, UTC+8）。

    明確指定 Asia/Taipei 時區，避免在非 UTC+8 主機上產生錯誤時間範圍。
    例如: datetime(2026, 2, 20, tzinfo=Asia/Taipei) → 1771516800
    """
    from zoneinfo import ZoneInfo
    tz = ZoneInfo("Asia/Taipei")
    dt = datetime(d.year, d.month, d.day, 0, 0, 0, tzinfo=tz)
    return int(dt.timestamp())


def save_json(data: list | dict, path: Path) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=str)


def load_json(path: Path) -> list | dict:
    if not path.exists():
        return []
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        # corrupt / 寫到一半 / merge conflict 殘留的 JSON 不該炸掉該日期的所有後續 run。
        # 記 error 並當作「無資料」處理（caller 多半會重新收集/評分）。
        _logger.error("load_json failed, treating as empty", extra={"path": str(path), "error": str(e)})
        return []


def normalize_url_light(url: str) -> str:
    """輕量 URL 正規化，用於「兩端來源相同」的 URL 比對（原始資料 box、repair 對照表）。

    只做三件事：去頭尾空白、去尾部 `/`、`http:` → `https:`。
    query 順序、`www.` 前綴、追蹤參數、fragment **一律保留**。

    ## 與 `normalize_url()` 的區別（兩支刻意並存，不要合併）

    | | `normalize_url_light()` | `normalize_url()` |
    |---|---|---|
    | 用途 | 同一份資料的兩個視角互相對照 | 跨來源 / 跨日**去重** |
    | query | 原樣保留 | 移除追蹤參數並按 key 排序 |
    | `www.` / 大小寫 | 原樣保留 | 去 `www.`、netloc 轉小寫 |
    | fragment | 原樣保留 | 移除 |

    去重要的是「盡量把同一篇文章的不同寫法收斂成一個 key」，寧可過度正規化；
    這裡兩端拿到的都是同一個 `ContentItem.url` 原值，只需要吸收
    scheme / 尾斜線這類無害差異，多做只會徒增與 JS 端不一致的風險。

    ## 跨語言平行實作：`web/src/enrich.ts` 的 `normalizeUrl`

    Astro 靜態站用 TS 版建 raw 索引、Web Monitor 用本函式查同一批 `data/raw`，
    **兩者行為必須保持一致**；任何一邊改了規則就要同步改另一邊，否則症狀是
    「原始資料 box 不顯示」——**無 log、無 exception**。
    修改本函式前請先看 `web/src/enrich.ts`，並更新
    `tests/test_normalize_url_light.py`（該檔逐條釘住兩端共同行為）。

    已知的非逐字差異：TS 版的 `http:` 取代是錨定的（`/^http:/`），本函式用未錨定的
    `str.replace(..., 1)`，故 `https://x/y/http://z` 這類巢狀 URL 兩者會分歧。
    實測 `data/raw` 全量 17230 個 url 分歧數為 0；日後若開始收 archive.org
    類 URL，需要把兩端一起改成錨定寫法。
    """
    if not url:
        return ""
    return url.strip().rstrip("/").replace("http:", "https:", 1)


_TRACKING_PARAM_KEYS = {"fbclid", "gclid", "msclkid", "ref"}


def normalize_url(url: str) -> str:
    """URL 正規化，用於跨來源 / 跨日去重比對。

    注意：這支**不是** `normalize_url_light()` 的重複實作，兩者用途不同
    （去重 vs 同源對照），差異表見 `normalize_url_light()` 的 docstring。

    - scheme 統一 https（http/空 → https）
    - netloc 小寫並去掉 `www.` 前綴
    - path 去尾部 `/`
    - 移除追蹤參數（utm_*、fbclid、gclid、msclkid、ref）
    - 其餘 query 參數按 key 排序，確保順序不影響 key
    - 移除 fragment（#anchor 為前端錨點，不影響內容）

    無法解析（空字串等）時原樣回傳。
    """
    if not url:
        return url
    from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

    try:
        parts = urlsplit(url.strip())
    except ValueError:
        return url

    scheme = "https" if parts.scheme in ("", "http", "https") else parts.scheme
    netloc = parts.netloc.lower()
    if netloc.startswith("www."):
        netloc = netloc[4:]
    path = parts.path.rstrip("/")

    kept = [
        (k, v)
        for k, v in parse_qsl(parts.query, keep_blank_values=True)
        if not k.lower().startswith("utm_") and k.lower() not in _TRACKING_PARAM_KEYS
    ]
    kept.sort(key=lambda kv: kv[0])
    query = urlencode(kept)

    return urlunsplit((scheme, netloc, path, query, ""))


def get_seen_urls(exclude_date: date | None = None, lookback_days: int | None = None) -> set[str]:
    """載入已收集過的 URL/arxiv_id 集合，用於跨日去重。

    Args:
        exclude_date: 排除此日期的資料（通常是今天，避免把自己排除）
        lookback_days: 只回看最近 N 天（None 表示全部）
    """
    from datetime import timedelta
    seen: set[str] = set()

    cutoff: date | None = None
    if lookback_days is not None and exclude_date is not None:
        cutoff = exclude_date - timedelta(days=lookback_days)

    for f in RAW_DIR.glob("*.json"):
        # 跳過今天的檔案
        if exclude_date and f.stem == exclude_date.isoformat():
            continue
        # 只回看 lookback_days 天
        if cutoff:
            try:
                file_date = date.fromisoformat(f.stem)
                if file_date < cutoff:
                    continue
            except ValueError:
                continue
        try:
            items = load_json(f)
            if isinstance(items, list):
                for item in items:
                    url = item.get("url", "")
                    if url:
                        # 與 ContentItem.dedup_key() 一致：兩側都經 normalize_url，
                        # 否則歷史 raw JSON 的舊 URL key 會比不到當天正規化後的 key。
                        seen.add(normalize_url(url))
                    arxiv_id = item.get("raw_metadata", {}).get("arxiv_id", "")
                    if arxiv_id:
                        # 同樣要與 dedup_key() 對齊：arxiv collector 存的 id 帶版本
                        # 後綴（2607.08772v1），hf_papers / semantic_scholar 不帶。
                        # 少了這道正規化，兩側 key 永遠對不上＝arXiv 論文跨日去重全失效。
                        seen.add(f"arxiv:{re.sub(r'v\d+$', '', arxiv_id)}")
        except Exception:
            continue
    return seen


def slugify(text: str, max_len: int = 60) -> str:
    """將標題轉為檔名安全的 slug。

    - 所有非單字字元（`/`、`.`、空白、標點等）一律轉成分隔符 `-`，
      避免 `memvid/memvid` 被直接刪成 `memvidmemvid` 這種黏字 bug。
    - 連續 `-` 折疊成單一，並 strip 頭尾。
    - 截斷 `max_len` 後若切在單字中間，退回最後一個完整單字，
      避免 `...world-modeli` 這種殘字。
    - 全特殊字元 / 空輸入回傳 fallback `untitled`。
    - 保留 unicode 單字字元（如中文），維持既有行為。
    """
    import re

    s = text.lower()
    # 非單字字元（含 / . 空白 標點）→ 分隔符；保留 \w（含 unicode 中文與底線）
    s = re.sub(r"[^\w]+", "-", s, flags=re.UNICODE)
    # \w 含底線，依慣例底線視為分隔符
    s = s.replace("_", "-")
    # 折疊連續 dash + 去頭尾
    s = re.sub(r"-{2,}", "-", s).strip("-")

    if not s:
        return "untitled"
    if len(s) <= max_len:
        return s

    truncated = s[:max_len]
    # 若切點仍在單字中間（下一字元非分隔符且當前結尾非分隔符），退回最後一個完整單字
    if s[max_len] != "-" and not truncated.endswith("-") and "-" in truncated:
        truncated = truncated.rsplit("-", 1)[0]
    return truncated.strip("-") or "untitled"


# abstract 字元上限預設值。原為 2000，實測 18 個 RSS 來源全部撞頂且斷在句中，
# 一般新聞全文約 3000-9000 字元，故提高。呼叫端可用 collectors.abstract_max_chars 覆寫。
ABSTRACT_MAX_CHARS_DEFAULT = 8000

# 正文容器 selector，**由精確到泛用**，必須逐一嘗試。
# 不可整串丟給 select_one：CSS select_one 依文件順序回傳第一個 match，
# 而外層容器（main）必然排在內層（.entry-content）之前，優先序會完全失效。
_CONTENT_SELECTORS = (
    ".entry-content",
    ".post-content",
    ".article-content",
    ".article-body",
    ".c-entry-content",
    ".post-body",
    ".e-content",
    ".blog-post",
    ".h-entry",
    ".hentry",
    ".prose",
    "article",
    "[role='main']",
    "main",
    "#content",
    "#main",
    ".content",
)

# 版面雜訊：推薦文章、電子報、分享列、作者簡介、麵包屑等。
# 只比對 class/id 的語意關鍵字，刻意不含 'content'（會誤殺正文）。
_NOISE_SELECTORS = (
    "script, style, nav, footer, header, aside, form, iframe, noscript, "
    ".sidebar, .comments, .nav, .menu, "
    "[class*='related'], [class*='recommend'], [class*='newsletter'], "
    "[class*='subscribe'], [class*='share'], [class*='social'], "
    "[class*='promo'], [class*='advert'], [class*='author-bio'], "
    "[class*='breadcrumb'], [class*='post-nav'], [class*='pagination'], "
    "[id*='related'], [id*='comments'], [id*='newsletter']"
)

# 尾段推薦區的標題文字。class 被雜湊（CSS modules / Next.js，如 Anthropic、The Verge）時，
# `[class*='related']` 之類的比對完全無效，只能靠標題文字辨識。
_TRAILING_SECTION_TITLES = frozenset(
    {
        "related content", "related posts", "related articles", "related stories",
        "related reading", "more from", "more in", "read next", "up next",
        "most popular", "you might also like", "recommended for you", "recommended",
        "newsletter", "subscribe", "share this article", "comments",
    }
)
# 只剝除位於全文這個比例之後的區塊——正文中段同名小標（如 "Most popular"
# 真的在討論熱門模型）不得被誤殺。
_TRAILING_CUT_MIN_RATIO = 0.6

_MIN_CONTAINER_LEN = 200
# 句界回退的下限：切點回退後至少要保留 max_chars 的這個比例，
# 否則寧可硬切——避免整段沒有標點的文本被回退到只剩開頭一句。
_BOUNDARY_MIN_RATIO = 0.6
_SENTENCE_ENDS = "。！？!?."


def _strip_trailing_sections(container) -> None:
    """就地移除容器尾段的推薦 / 訂閱區塊（靠標題文字辨識，不依賴 class 名稱）。"""
    full_text = container.get_text(" ", strip=True)
    if not full_text:
        return
    threshold = len(full_text) * _TRAILING_CUT_MIN_RATIO

    for heading in container.find_all(["h1", "h2", "h3", "h4"]):
        raw_title = heading.get_text(" ", strip=True)
        title = " ".join(raw_title.lower().split()).rstrip(":")
        if title not in _TRAILING_SECTION_TITLES:
            continue
        # 保守起見用首次出現位置：低估位置只會放過推薦區，不會誤砍正文
        position = full_text.find(raw_title)
        if position < threshold:
            continue  # 位在正文中段，是內容小標而非推薦區

        # 上溯找出「推薦區塊」本身。祖先一旦大到裝得下 heading 之前的正文，
        # 就代表它是正文容器而非推薦區——必須停在上一層，否則會把整篇文章剝掉
        # （The Verge：h2 距容器 8 層，無腦上溯會剝掉 8131 字元的正文容器）。
        tail_budget = (len(full_text) - position) * 1.2 + 50
        node = heading
        while node.parent is not None and node.parent is not container:
            if len(node.parent.get_text(" ", strip=True)) > tail_budget:
                break
            node = node.parent

        for sibling in list(node.next_siblings):
            sibling.extract()
        node.extract()
        return


def truncate_at_boundary(text: str, max_chars: int) -> str:
    """在 max_chars 內截斷，優先退到句界、其次詞界，避免斷在字中間。

    回退幅度受 `_BOUNDARY_MIN_RATIO` 限制：若最近的邊界離切點太遠
    （例如整段無標點），則硬切，不讓內容被砍到剩開頭。
    """
    if len(text) <= max_chars:
        return text

    window = text[:max_chars]
    min_keep = int(max_chars * _BOUNDARY_MIN_RATIO)

    sentence_cut = max(window.rfind(ch) for ch in _SENTENCE_ENDS)
    if sentence_cut >= min_keep:
        return window[: sentence_cut + 1].strip()

    word_cut = window.rfind(" ")
    if word_cut >= min_keep:
        return window[:word_cut].rstrip()

    return window.rstrip()


def extract_full_text_from_html(html: str, max_chars: int = ABSTRACT_MAX_CHARS_DEFAULT) -> str:
    """從 HTML 提取純文字，優先選取語意容器標籤，fallback 到 <p> 聚合。"""
    import re

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")

    # 移除干擾元素
    for tag in soup.select(_NOISE_SELECTORS):
        tag.decompose()

    # 語意容器：由精確到泛用逐一嘗試，取第一個內容夠長的
    for selector in _CONTENT_SELECTORS:
        body = soup.select_one(selector)
        if not body:
            continue
        _strip_trailing_sections(body)
        text = re.sub(r"\s{2,}", " ", body.get_text(separator=" ", strip=True))
        if len(text) >= _MIN_CONTAINER_LEN:
            return truncate_at_boundary(text, max_chars)

    # Fallback: 聚合所有 <p> 標籤（排除過短段落）
    paragraphs = soup.find_all("p")
    p_texts = []
    for p in paragraphs:
        t = p.get_text(separator=" ", strip=True)
        if len(t) >= 30:  # 跳過極短段落（廣告、版權等）
            p_texts.append(t)
    if p_texts:
        text = " ".join(p_texts)
        text = re.sub(r"\s{2,}", " ", text)
        if len(text) >= 100:
            return truncate_at_boundary(text, max_chars)

    # 最終 fallback: 整頁文字
    text = soup.get_text(separator=" ", strip=True)
    return truncate_at_boundary(re.sub(r"\s{2,}", " ", text), max_chars)


def fetch_article_text(url: str, client: httpx.Client, max_chars: int = ABSTRACT_MAX_CHARS_DEFAULT) -> str:
    """GET 文章 URL，返回純文字。失敗時返回空字串並記錄 debug log。"""
    try:
        resp = client.get(url, timeout=12)
        if resp.status_code != 200:
            _logger.debug("fetch_article_text non-200", extra={"url": url, "status_code": resp.status_code})
            return ""
        text = extract_full_text_from_html(resp.text, max_chars)
        if not text:
            _logger.debug("fetch_article_text empty extraction", extra={"url": url, "html_len": len(resp.text)})
        return text
    except Exception as e:
        _logger.debug("fetch_article_text request failed", extra={"url": url, "error": str(e)})
    return ""


def build_link_abstract(
    url: str,
    client: httpx.Client,
    engagement: str,
    fallback_domain: str,
    max_chars: int = ABSTRACT_MAX_CHARS_DEFAULT,
) -> str:
    """Link post 共用 helper：嘗試抓取外部文章內容，失敗時 fallback 到 domain + engagement。"""
    fetched = fetch_article_text(url, client, max_chars)
    if fetched:
        return f"{fetched}\n\n({engagement})"
    return f"{fallback_domain} — {engagement}"
