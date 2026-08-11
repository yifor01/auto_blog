"""Pydantic data models for the auto_post_blog pipeline."""

from __future__ import annotations

import html
import re
from datetime import date, datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, field_validator, model_validator


class SourceType(str, Enum):
    ARXIV = "arxiv"
    CHATPAPER = "chatpaper"
    HF_PAPERS = "hf_papers"
    RSS = "rss"
    BLOG = "blog"
    GITHUB = "github"
    HACKERNEWS = "hackernews"
    REDDIT = "reddit"
    NEWSAPI = "newsapi"
    SEMANTIC_SCHOLAR = "semantic_scholar"
    CN_LABS = "cn_labs"


# ---- Layer A：剝除來源殘留的媒體標記 ----

# 只剝這五種——媒體與嵌入標記，在正文語境下不是內容。**不可**擴成通吃 `<xxx>`：
# 實測 data/raw 有 453 個欄位帶角括號標記，多數是正常內容（GitHub README 的
# `Vec<String>`、CLI 說明的 `<version>` / `<id>` / `<std>`、arxiv 摘要的泛型），
# 一律剝除會把它們吃掉且無任何 log。
_MEDIA_TAG_NAMES = "img|iframe|script|style|noscript"

# 成對出現時：script / style 連同標記之間的內容一起剝（那是 JS / CSS 不是正文），
# 其餘（img / iframe / noscript）只剝標記本身、保留中間文字。
# `\s*` 是必要的——量子位是 `< img ...>`、GitHub README 是 `</ script >`，
# 來源殘留普遍在 `<` 後與 `/` 兩側帶空白。re.IGNORECASE 下 `\1` 反向參照也大小寫
# 不敏感，`< ScRiPt ...>...</SCRIPT>` 才配得起來。
_PAIRED_MEDIA_RE = re.compile(
    rf"<\s*({_MEDIA_TAG_NAMES})\b[^<>]*>(.*?)<\s*/\s*\1\s*>",
    re.IGNORECASE | re.DOTALL,
)
# 落單的開/閉標記。是否真的剝由 `_drop_single_media()` 判斷（見該處說明）。
_SINGLE_MEDIA_RE = re.compile(
    rf"<\s*(/?)\s*(?:{_MEDIA_TAG_NAMES})\b([^<>]*)>",
    re.IGNORECASE,
)
# 剝除點的佔位符：先標記位置，最後才連同相鄰空白收斂成單一分隔符。why 不直接
# 換成空字串再全域 collapse 空白——那會順手壓掉欄位其他地方的排版（GitHub README
# 的 CLI 對齊、段落換行）；用佔位符才能把正規化限制在「真的剝過的地方」。
_SENTINEL = "\x00"
_SENTINEL_RUN_RE = re.compile(rf"\s*(?:{_SENTINEL}\s*)+")


def _drop_paired_media(match: re.Match[str]) -> str:
    inner = "" if match.group(1).lower() in ("script", "style") else match.group(2)
    return f"{_SENTINEL}{inner}{_SENTINEL}"


def _drop_single_media(match: re.Match[str]) -> str:
    """落單標記：閉標記與「帶屬性的開標記」剝掉，裸開標記留著。

    why 裸開標記不剝：實測 data/raw 的裸 `<style>` / `<script>` **全部**是 CLI
    說明的角括號佔位符（`--style <style>   Style (vivid, natural)`、
    `pnpm --filter <name> <script>`），與 `<version>` / `<id>` 同一類正常內容，
    只是名字剛好撞上白名單。反過來，真正的媒體嵌入一定帶屬性（`<img>` 沒有 src
    什麼都不是），所以「有屬性」正好把兩者分乾淨；裸開標記若真的是標記，也會有
    配對的閉標記，那種形態已由 `_PAIRED_MEDIA_RE` 先一步處理掉。
    閉標記語法（`</script>`）則不可能是正文，一律剝。
    """
    is_closing = bool(match.group(1))
    attrs = match.group(2).strip().strip("/").strip()
    if is_closing or attrs:
        return _SENTINEL
    return match.group(0)


def strip_media_tags(text: str) -> str:
    """剝除來源正文殘留的媒體/嵌入標記，並收斂剝除點周邊的多餘空白。

    Layer A 的一部分（`html.unescape()` 之後、`to_traditional()` 之前）：量子位
    每篇 abstract 開頭都掛著 `< img id="wx_img" ...>`、Hacker News 會抓到 gist 頁的
    `<script>` boilerplate 與 NPR 的 `<iframe>` 播放器，這些殘留會在詳情頁的
    「原始資料 box」整串露給使用者看。

    只處理 img / iframe / script / style / noscript，且對「像標記的正常內容」
    刻意保守——判定細節與理由見 `_drop_single_media()`。無標記的字串原封返回
    （連空白都不動），對已剝過的字串冪等。

    `repair-content` 修歷史資料時直接 import 這支，不要另外複製一份實作。
    """
    if "<" not in text:
        return text
    # 佔位符是控制字元，正常內容不會有；先清掉以免外來的 NUL 干擾後面的收斂
    working = text.replace(_SENTINEL, "")
    working = _PAIRED_MEDIA_RE.sub(_drop_paired_media, working)
    working = _SINGLE_MEDIA_RE.sub(_drop_single_media, working)
    if _SENTINEL not in working:
        return text
    # 剝除點原本兩側若有換行就還一個換行（不要把段落壓成一行），否則給一個空格
    # （`constrained<iframe ...>sandbox` 這種沒有空白的相接不能黏成一個字）
    working = _SENTINEL_RUN_RE.sub(lambda m: "\n" if "\n" in m.group(0) else " ", working)
    return working.strip()


class ContentItem(BaseModel):
    """統一的內容條目，所有 collector 產出都轉換成這個格式。"""

    source: SourceType
    source_name: str = ""  # e.g. "TechCrunch AI", "arXiv"
    title: str
    url: str
    authors: list[str] = Field(default_factory=list)
    abstract: str = ""
    published_date: date
    tags: list[str] = Field(default_factory=list)
    organization: str = ""
    raw_metadata: dict = Field(default_factory=dict)

    @field_validator("title", "abstract")
    @classmethod
    def _normalize_to_traditional(cls, v: str) -> str:
        """Layer A：來源端 HTML entity 解碼 + 簡→繁。量子位 / ChatPaper 等
        中國 source 的簡體 title/abstract 在建構時就轉繁，一改全下游受惠
        （raw/scored JSON、blog frontmatter title、digest、web UI）。
        對英文/繁中為冪等。

        why 先 unescape 再轉繁：&#8217; 解碼後是 ASCII 標點，OpenCC 不動它；
        反過來則是拿未解碼的髒字串餵 OpenCC。RSS 有 58 筆 title、
        hackernews 有 269 筆 abstract 帶著未解碼 entity。

        why 剝媒體標記夾在中間：`&lt;img src=...&gt;` 要解碼後才認得出是標記
        （排在 unescape 之前就漏抓），而剝完再轉繁可以少餵 OpenCC 一段標記文字。
        歷史資料不受惠——讀取端 `item_from_raw()` 會無損還原存檔原值，這是刻意的
        （清洗歸資料層），舊檔由 `repair-content` 回補。
        """
        # 區域 import 避免 utils <-> models 潛在循環依賴
        from src.utils import to_traditional

        return to_traditional(strip_media_tags(html.unescape(v)))

    @field_validator("tags")
    @classmethod
    def _normalize_tags_to_traditional(cls, v: list[str]) -> list[str]:
        """tags 同樣走 Layer A。漏掉這個，網站的 tag chip 會直接顯示
        簡體（资讯 / 开源 / 科大讯飞），且 tag 篩選會把簡繁當成兩個不同標籤。

        媒體標記剝除同步套用：實測 data/raw 的 tags 目前 0 筆命中，純粹是讓
        Layer A 三個欄位的語意一致（下次某個 collector 把髒 HTML 塞進 tags 時
        不必再想一次這裡有沒有做）。"""
        from src.utils import to_traditional

        return [to_traditional(strip_media_tags(html.unescape(t))) for t in v]

    def dedup_key(self) -> str:
        """用於去重的 key: 優先用 arxiv id, 否則用正規化後的 URL."""
        arxiv_id = self.raw_metadata.get("arxiv_id", "")
        if arxiv_id:
            # 去掉版本後綴（2606.11190v1 → 2606.11190），
            # 讓 arxiv / hf_papers / semantic_scholar 三來源的同篇論文能互相去重
            canonical = re.sub(r"v\d+$", "", arxiv_id)
            return f"arxiv:{canonical}"
        # 區域 import 避免 utils <-> models 潛在循環依賴
        from src.utils import normalize_url

        return normalize_url(self.url)


# Layer A validator 會改寫的欄位——從既有存檔重建時要還原成存檔原值
_LAYER_A_FIELDS = ("title", "abstract", "tags")


def item_from_raw(raw: dict) -> ContentItem:
    """從 `data/raw` 的既有 dict 重建 ContentItem，且**不重複套用 Layer A**。

    why：存檔裡的 title / abstract / tags 已經是 Layer A 的成品，而 s2twp 對繁體
    刻意不冪等（「這個文件的參數」→「這個檔案的參數」）。直接 `ContentItem(**raw)`
    等於再套一次，於是每讀一次就漂一格。寫回 raw 的路徑固然要防（backfill /
    supplement 已改成保留原始 dict），但只要拿這些 item 產出**任何**檔案就一樣會把
    漂移寫進成品——`build_day_lists()` 就是這樣讓 `output/lists` 與 `data/raw`
    出現落差的（實測近 40 天清單型來源 3375 筆中 34 筆非冪等，約 1%），而詳情頁的
    「原始資料 box」直接讀 `data/raw`，兩處並列時同一段文字會顯示不一致。

    why 先完整建構再賦值、而不是 `model_construct()`：後者跳過**所有**驗證含型別
    轉換，`published_date` 會停在 str，`_other_entry()` 的 `.isoformat()` 當場
    AttributeError（已實測）。這裡走完整驗證拿到正確型別，之後才把 Layer A 覆寫過的
    欄位還原——`ContentItem` 沒有開 `validate_assignment`（Pydantic v2 預設關閉），
    賦值不會再次觸發 validator。日後若替 `ContentItem` 加上 `validate_assignment`，
    這個還原會靜默失效，屆時必須改走別的還原手段。

    附帶取捨：還原也跳過了 Layer A 的 `html.unescape()`。這是對的——存檔值本來就
    是已解碼的成品，讀取端的職責是**無損還原**而非二次清洗；歷史髒資料由
    `repair-content` 負責（`data/raw` 的 entity 已於該指令實跑後歸零）。
    """
    return _restore_layer_a(ContentItem(**raw), raw)


def _restore_layer_a(item: ContentItem, raw: dict) -> ContentItem:
    """把 Layer A validator 改寫過的欄位，就地還原成 `raw` 裡的存檔原值。

    `item_from_raw()` 與 `scored_from_raw()` 共用的唯一還原實作——兩者只差在
    去哪裡撈那份 dict（後者要往內鑽一層 `raw["item"]`）。抽出來是為了讓
    `_LAYER_A_FIELDS` 日後增修時兩條路徑不可能只改到一邊。
    """
    for field in _LAYER_A_FIELDS:
        if field not in raw:
            continue
        value = raw[field]
        # list 要複製再塞：直接指派是 aliasing，而 backfill / supplement 正好把
        # 同一份 raw dict 當寫回 payload——日後任何原地改 item.tags 的程式碼都會
        # 靜默寫壞 data/raw。字串不可比照辦理（list("abc") 會拆成字元）。
        setattr(item, field, list(value) if isinstance(value, list) else value)
    return item


class ScoredItem(BaseModel):
    """篩選後帶評分的條目。"""

    item: ContentItem
    rule_score: float = 0.0
    rule_reasons: list[str] = Field(default_factory=list)

    # LLM 評分 (只有通過 rule 預篩的才有)
    llm_score: float | None = None
    llm_reason: str = ""
    novelty: float | None = None
    impact: float | None = None
    trending: float | None = None      # 話題性（舊欄位名: relevance）
    practicality: float | None = None  # 實用性
    blog_worthiness: float | None = None

    @model_validator(mode="before")
    @classmethod
    def _migrate_relevance(cls, data: Any) -> Any:
        """向後相容：將舊版 JSON 中的 relevance 欄位對應到 trending。"""
        if isinstance(data, dict) and "relevance" in data and "trending" not in data:
            data = dict(data)
            data["trending"] = data.pop("relevance")
        return data

    @property
    def total_score(self) -> float:
        if self.llm_score is not None:
            return self.rule_score + self.llm_score
        return self.rule_score


def scored_from_raw(raw: dict) -> ScoredItem:
    """從 `data/scored` 的既有 dict 重建 ScoredItem，且**不重複套用 Layer A**。

    `item_from_raw()` 的同構版本：`ScoredItem` 內嵌一個 `item: ContentItem`，
    所以 `ScoredItem(**rec)` 會連帶再跑一次 Layer A validator，症狀與直接
    `ContentItem(**raw)` 完全相同（「這個文件的參數」→「這個檔案的參數」、
    tags 的「高性價比」→「高價效比」）。每讀一次 `data/scored` 就漂一格，而
    素材庫列表 / 搜尋索引 / 主題頁全都經由這條路徑，與同頁直接讀 `data/raw`
    的「原始資料 box」並列時，同一段文字會顯示不一致。

    寫回路徑更要命：`pipeline.score_incremental()` 是讀-改-寫，`--supplement`
    一跑就把漂移永久固化進 `data/scored`（Web Monitor 啟動時對當天自動走
    `--supplement`，開一次 dashboard 就觸發一次）。故該處除了改走本函式，
    寫回也沿用原始 dict——比照 `backfill` / `supplement_items` 的做法。

    相容性：舊版 JSON 的 `relevance` → `trending` 由 `_migrate_relevance`
    （`mode="before"` 的 model_validator）處理。這裡走完整建構所以該遷移照常
    生效；還原只碰內嵌 item 的 `_LAYER_A_FIELDS`，不觸及評分欄位。

    `raw` 缺 `item` 鍵時直接讓 `ScoredItem(**raw)` 拋 ValidationError（呼叫端
    多半已包 try/except 跳過爛資料），不在這裡吞掉。
    """
    scored = ScoredItem(**raw)
    nested = raw.get("item")
    if isinstance(nested, dict):
        _restore_layer_a(scored.item, nested)
    return scored


class GeneratedContent(BaseModel):
    """生成的內容 (blog post 或 note)."""

    source_item: ScoredItem
    content: str
    prompt_used: str  # 保存完整 prompt，未來可重新呼叫
    model_used: str
    generated_at: datetime = Field(default_factory=datetime.now)
    content_type: str = "blog_post"  # "blog_post" | "note"
