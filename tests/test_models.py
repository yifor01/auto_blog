"""Pydantic model 驗證測試。"""

from __future__ import annotations

from datetime import date, datetime

import pytest

from src.models import ContentItem, GeneratedContent, ScoredItem, SourceType


class TestContentItem:
    def test_dedup_key_prefers_arxiv_id(self):
        item = ContentItem(
            source=SourceType.ARXIV,
            title="Test",
            url="https://arxiv.org/abs/2601.00001",
            published_date=date(2026, 2, 26),
            raw_metadata={"arxiv_id": "2601.00001"},
        )
        assert item.dedup_key() == "arxiv:2601.00001"

    def test_dedup_key_falls_back_to_url(self):
        item = ContentItem(
            source=SourceType.RSS,
            title="News",
            url="https://example.com/article",
            published_date=date(2026, 2, 26),
        )
        assert item.dedup_key() == "https://example.com/article"

    def test_dedup_key_github_uses_url(self):
        item = ContentItem(
            source=SourceType.GITHUB,
            title="repo",
            url="https://github.com/user/repo",
            published_date=date(2026, 2, 26),
        )
        assert item.dedup_key() == "https://github.com/user/repo"

    def test_default_fields(self):
        item = ContentItem(
            source=SourceType.BLOG,
            title="Blog Post",
            url="https://blog.com/post",
            published_date=date(2026, 2, 26),
        )
        assert item.authors == []
        assert item.abstract == ""
        assert item.organization == ""
        assert item.tags == []
        assert item.raw_metadata == {}


class TestScoredItem:
    def test_total_score_with_llm(self, arxiv_item):
        item = ScoredItem(item=arxiv_item, rule_score=30.0, llm_score=75.0)
        assert item.total_score == 105.0

    def test_total_score_without_llm(self, arxiv_item):
        item = ScoredItem(item=arxiv_item, rule_score=30.0)
        assert item.llm_score is None
        assert item.total_score == 30.0

    def test_practicality_field_exists(self, arxiv_item):
        item = ScoredItem(item=arxiv_item, rule_score=30.0, practicality=14.0)
        assert item.practicality == 14.0

    def test_trending_field(self, arxiv_item):
        item = ScoredItem(item=arxiv_item, rule_score=30.0, trending=15.0)
        assert item.trending == 15.0

    def test_backward_compat_relevance_maps_to_trending(self, arxiv_item):
        """B3 向後相容：舊 JSON 的 relevance 欄位應對應到 trending。"""
        data = {
            "item": arxiv_item.model_dump(),
            "rule_score": 30.0,
            "relevance": 15.0,   # 舊欄位名
        }
        item = ScoredItem(**data)
        assert item.trending == 15.0

    def test_new_format_both_fields(self, arxiv_item):
        """新格式 trending 與 practicality 都能正常儲存。"""
        item = ScoredItem(
            item=arxiv_item,
            rule_score=30.0,
            llm_score=80.0,
            trending=18.0,
            practicality=16.0,
            novelty=17.0,
            impact=15.0,
            blog_worthiness=14.0,
        )
        assert item.trending == 18.0
        assert item.practicality == 16.0
        assert item.total_score == 110.0

    def test_zero_rule_score_floor(self, arxiv_item):
        """rule_score 可以是 0，total_score 不應為負。"""
        item = ScoredItem(item=arxiv_item, rule_score=0.0)
        assert item.total_score == 0.0


class TestHtmlEntityDecoding:
    def _item(self, **kw):
        from datetime import date as _date

        from src.models import ContentItem, SourceType

        base = dict(
            source=SourceType.RSS,
            title="t",
            url="https://example.com/a",
            published_date=_date(2026, 7, 28),
        )
        base.update(kw)
        return ContentItem(**base)

    def test_decodes_numeric_entity_in_title(self):
        # 實測：output/posts 有 4 篇 frontmatter title 帶著 &#8217;
        assert self._item(title="Sam Altman&#8217;s orb").title == "Sam Altman’s orb"

    def test_decodes_hex_entity_in_abstract(self):
        # 實測：hackernews abstract 269 筆帶 &#x2F;
        got = self._item(abstract="https:&#x2F;&#x2F;x.com&#x2F;a").abstract
        assert got == "https://x.com/a"

    def test_decodes_named_entities(self):
        assert self._item(abstract="a &amp; b &gt; c").abstract == "a & b > c"

    def test_decodes_entity_in_tags(self):
        assert self._item(tags=["AI &amp; ML"]).tags == ["AI & ML"]

    def test_idempotent_on_clean_text(self):
        # 刻意用裸 & 與裸 <：html.unescape 的解析很寬鬆（連沒有結尾分號的
        # 也會嘗試解），這種字串才踩得到它，用「完全沒有 & 的乾淨句子」
        # 連 no-op 實作都會過，守不住任何東西
        clean = "R&D at 5 < 10"
        assert self._item(abstract=clean).abstract == clean

    def test_opencc_still_runs_on_text_containing_entities(self):
        """OpenCC liveness：帶 entity 的字串「解碼後」簡體仍確實有被轉繁。

        注意這一筆**測不到「先解碼再轉繁」的順序**——實作寫成反向的
        `html.unescape(to_traditional(v))` 它照樣 PASS（ASCII entity `&#8217;`
        解碼前後 OpenCC 都不動它，而字面的「开源」兩種順序都會被轉）。
        真正釘住順序的是下面的 `test_cjk_numeric_entity_still_gets_converted`，
        全 repo 只有那一筆守得住，改動 Layer A 時別誤以為有兩處覆蓋。

        它仍有價值：Layer A 若整段失效（OpenCC 未載入、validator 被拿掉），
        這一筆會 FAIL。
        """
        # 混合 entity 與已經是字面的簡體：兩條路徑都要轉繁
        got = self._item(title="开源模型&#8217;s 发布").title
        assert "&#" not in got
        # 「发布」在 s2twp 台灣詞庫下轉成「釋出」（非字形對應的「發布」），
        # 這是 Layer A 既有行為，正好證明 OpenCC 在解碼之後仍有生效
        assert "開源" in got and "釋出" in got

    def test_cjk_numeric_entity_still_gets_converted(self):
        """釘住「先 unescape 再 to_traditional」的順序——本 task 唯一的硬規則。

        用 CJK numeric entity 才測得到順序：entity 解出來的是簡體字，
        必須讓 OpenCC 在解碼「之後」才碰得到它。
        若實作寫反成 html.unescape(to_traditional(v))，簡體會整段漏出
        （'开源模型'）且無任何 log——正是靜默失效。
        ASCII entity（&#8217;）測不出來，因為它解碼後 OpenCC 本來就不動。
        """
        got = self._item(title="&#24320;&#28304;&#27169;&#22411;").title
        assert got == "開源模型"


class TestItemFromRaw:
    """models.item_from_raw()：從 data/raw 既有 dict 重建，不得重複套用 Layer A。

    這是「讀 raw 無損」的單一實作點，7 個呼叫點全靠它。直接測它比逐一測呼叫端
    便宜，也是唯一能抓到「_LAYER_A_FIELDS 漏掉某個欄位」的地方。
    """

    # 真實樣本：`這個文件`→`這個檔案`、`高性價比`→`高價效比`（s2twp 對繁體不冪等）
    DRIFTING = "這個文件的參數設定"
    DRIFTING_TAG = "高性價比"

    def _raw(self) -> dict:
        return {
            "source": "github",
            "source_name": "GitHub Trending",
            "title": self.DRIFTING,
            "url": "https://github.com/org/repo",
            "abstract": self.DRIFTING * 3,
            "published_date": "2026-01-01",
            "tags": [self.DRIFTING_TAG, self.DRIFTING],
            "organization": "",
            "raw_metadata": {"stars_today": 10},
        }

    def test_premise_these_strings_really_drift(self):
        """測試前提：這兩串在 s2twp 下不冪等。前提失效要立刻自曝，而非靜默常綠。"""
        from src.utils import to_traditional

        assert to_traditional(self.DRIFTING) != self.DRIFTING
        assert to_traditional(self.DRIFTING_TAG) != self.DRIFTING_TAG

    def test_restores_title_abstract_and_tags_verbatim(self):
        """title / abstract / tags 三者都要還原——漏掉任一個都是靜默漂移。"""
        from src.models import item_from_raw

        raw = self._raw()
        it = item_from_raw(raw)
        assert it.title == self.DRIFTING
        assert it.abstract == self.DRIFTING * 3
        assert it.tags == [self.DRIFTING_TAG, self.DRIFTING]

    def test_plain_contentitem_would_drift(self):
        """對照組：釘住「直接 ContentItem(**raw) 會漂」這個前提仍然成立。"""
        from src.models import ContentItem

        it = ContentItem(**self._raw())
        assert it.title != self.DRIFTING
        assert it.tags != [self.DRIFTING_TAG, self.DRIFTING]

    def test_still_validates_and_coerces_types(self):
        """走完整驗證，型別轉換不能少（model_construct 會讓 published_date 停在 str）。"""
        from datetime import date

        from src.models import item_from_raw

        it = item_from_raw(self._raw())
        assert isinstance(it.published_date, date)
        assert it.published_date.isoformat() == "2026-01-01"  # _other_entry() 依賴這個

    def test_tags_list_is_copied_not_aliased(self):
        """tags 必須是複本：backfill / supplement 把同一份 raw dict 當寫回 payload，
        aliasing 會讓任何原地改 tags 的程式碼靜默寫壞 data/raw。"""
        from src.models import item_from_raw

        raw = self._raw()
        it = item_from_raw(raw)
        it.tags.append("injected")
        assert raw["tags"] == [self.DRIFTING_TAG, self.DRIFTING]

    def test_missing_optional_fields_are_left_alone(self):
        """raw 沒有 tags 時不得炸，也不該憑空造欄位。"""
        from src.models import item_from_raw

        raw = self._raw()
        del raw["tags"]
        assert item_from_raw(raw).tags == []


class TestScoredFromRaw:
    """models.scored_from_raw()：從 data/scored 既有 dict 重建，不得重複套用 Layer A。

    `ScoredItem` 內嵌 `item: ContentItem`，所以 `ScoredItem(**rec)` 會連帶再跑一次
    Layer A validator——症狀與直接 `ContentItem(**raw)` 一模一樣，只是藏在一層底下。
    15 個讀 data/scored 的呼叫點全靠這個函式。
    """

    DRIFTING = TestItemFromRaw.DRIFTING
    DRIFTING_TAG = TestItemFromRaw.DRIFTING_TAG

    def _raw(self) -> dict:
        return {
            "item": {
                "source": "rss",
                "source_name": "TechCrunch AI",
                "title": self.DRIFTING,
                "url": "https://example.com/a",
                "authors": ["Alice"],
                "abstract": self.DRIFTING * 3,
                "published_date": "2026-01-01",
                "tags": [self.DRIFTING_TAG, self.DRIFTING],
                "organization": "OpenAI",
                "raw_metadata": {},
            },
            "rule_score": 30.0,
            "rule_reasons": ["🏢 頂流機構: OpenAI"],
            "llm_score": 60.0,
            "llm_reason": "不錯",
            "novelty": 12.0,
            "impact": 12.0,
            "trending": 12.0,
            "practicality": 12.0,
            "blog_worthiness": 12.0,
        }

    def test_restores_nested_item_fields_verbatim(self):
        """內嵌 item 的 title / abstract / tags 三者都要還原。"""
        from src.models import scored_from_raw

        si = scored_from_raw(self._raw())
        assert si.item.title == self.DRIFTING
        assert si.item.abstract == self.DRIFTING * 3
        assert si.item.tags == [self.DRIFTING_TAG, self.DRIFTING]

    def test_plain_scoreditem_would_drift(self):
        """對照組：釘住「直接 ScoredItem(**rec) 會漂」這個前提仍然成立。

        前提失效（例如 Pydantic 改了巢狀 model 的驗證行為）時要立刻自曝，
        而不是讓上面那條測試變成永遠常綠的空砲。
        """
        from src.models import ScoredItem

        si = ScoredItem(**self._raw())
        assert si.item.title != self.DRIFTING
        assert si.item.tags != [self.DRIFTING_TAG, self.DRIFTING]

    def test_scores_are_untouched(self):
        """只還原 Layer A 欄位，評分欄位照常經過驗證與型別轉換。"""
        from src.models import scored_from_raw

        si = scored_from_raw(self._raw())
        assert si.rule_score == 30.0
        assert si.llm_score == 60.0
        assert si.total_score == 90.0
        assert si.trending == 12.0
        assert si.item.published_date.isoformat() == "2026-01-01"

    def test_legacy_relevance_still_migrates_to_trending(self):
        """向後相容不能被還原邏輯壓掉：舊版 JSON 的 relevance → trending。

        歷史 data/scored 大量存在 relevance 欄位；這條斷了的話 analyze-scores
        與素材庫的話題性維度會整欄變 None，而且不會有任何錯誤訊息。
        """
        from src.models import scored_from_raw

        raw = self._raw()
        raw["relevance"] = raw.pop("trending")
        si = scored_from_raw(raw)
        assert si.trending == 12.0
        # 還原不得意外把 relevance 塞回內嵌 item 或造出新欄位
        assert si.item.title == self.DRIFTING

    def test_nested_tags_list_is_copied_not_aliased(self):
        """tags 必須是複本：score_incremental 把同一份 dict 當寫回 payload，
        aliasing 會讓任何原地改 tags 的程式碼靜默寫壞 data/scored。"""
        from src.models import scored_from_raw

        raw = self._raw()
        si = scored_from_raw(raw)
        si.item.tags.append("injected")
        assert raw["item"]["tags"] == [self.DRIFTING_TAG, self.DRIFTING]

    def test_missing_optional_nested_fields_are_left_alone(self):
        """內嵌 item 缺 tags 時不得炸，也不該憑空造欄位。"""
        from src.models import scored_from_raw

        raw = self._raw()
        del raw["item"]["tags"]
        assert scored_from_raw(raw).item.tags == []

    def test_malformed_record_still_raises(self):
        """爛資料照樣拋 ValidationError——呼叫端靠 try/except 跳過，不能被吞掉。"""
        import pytest
        from pydantic import ValidationError

        from src.models import scored_from_raw

        with pytest.raises(ValidationError):
            scored_from_raw({"rule_score": 1.0})


class TestStripMediaTags:
    """Layer A 剝除來源殘留的媒體標記（img / iframe / script / style / noscript）。

    素材全部取自實測的 `data/raw`：量子位每篇 abstract 開頭都掛著 wx_img、
    Hacker News 抓到 gist 頁的 `<script>` boilerplate 與 NPR 的 `<iframe>` 播放器。
    這些殘留會在詳情頁「原始資料 box」整串露出給使用者看。

    這個 class 有一半篇幅在守「**不能**剝什麼」——實測 `data/raw` 有 453 個欄位帶
    `<xxx>` 而多數是正常內容（`Vec<String>`、CLI 說明的 `<version>` / `<id>`），
    白名單一旦擴大就會把它們吃掉，且不會有任何錯誤訊息。
    """

    def _item(self, **kw):
        base = dict(
            source=SourceType.RSS,
            title="t",
            url="https://example.com/a",
            published_date=date(2026, 7, 29),
        )
        base.update(kw)
        return ContentItem(**base)

    # ---- 該剝的 ----

    def test_strips_leading_qbitai_img(self):
        """量子位實測形態：`<` 後有空格、標記在最開頭，剝完前導空白也要收乾淨。"""
        from src.models import strip_media_tags

        raw = (
            '< img id="wx_img" src="https://www.qbitai.com/wp-content/uploads/'
            'imgs/qbitai-logo-1.png" width="400" height="400"> 今天的新聞內容'
        )
        assert strip_media_tags(raw) == "今天的新聞內容"

    def test_strips_img_through_content_item_validator(self):
        """整合面：走 ContentItem 建構就該乾淨，不是只有函式自己會動。"""
        raw = '< img id="wx_img" src="https://www.qbitai.com/a.png" width="400"> 开源模型发布'
        got = self._item(abstract=raw).abstract
        assert "img" not in got and "<" not in got
        # 剝除不得擋掉 Layer A 的簡→繁（順序：unescape → strip → to_traditional）
        assert got.startswith("開源模型")

    def test_strips_mid_text_iframe_and_collapses_space(self):
        """NPR 播放器實測形態：標記在句中，剝完左右空白要併成一個。"""
        from src.models import strip_media_tags

        raw = (
            'Download Embed Embed < iframe src="https://www.npr.org/player/embed/'
            'nx-s1-5835631" width="100%" height="290" frameborder="0"> Transcript'
        )
        assert strip_media_tags(raw) == "Download Embed Embed Transcript"

    def test_paired_script_drops_inner_javascript(self):
        """成對 script 連內容一起剝——中間那段是 JS 不是正文。

        刻意讓 JS 內含 `1 < 2`：實作若拿 `[^<]*` 當內容匹配會在這裡斷掉。
        """
        from src.models import strip_media_tags

        raw = 'Clone this repository at <script src="https://gist.github.com/a.js">var ok = 1 < 2;</script> Save to your computer.'
        assert strip_media_tags(raw) == "Clone this repository at Save to your computer."

    def test_paired_script_tolerates_spaces_inside_markers(self):
        """PageAgent README 實測形態：`< script ... > </ script >` 標記內外都有空格。"""
        from src.models import strip_media_tags

        raw = 'Fastest way to try PageAgent: < script src=" {URL} " crossorigin=" true " > </ script > ⚠️ For evaluation only.'
        assert strip_media_tags(raw) == "Fastest way to try PageAgent: ⚠️ For evaluation only."

    def test_paired_style_drops_inner_css(self):
        from src.models import strip_media_tags

        raw = "Header <style>body { color: red; }</style> Footer"
        assert strip_media_tags(raw) == "Header Footer"

    def test_noscript_strips_markers_but_keeps_text(self):
        """script / style 以外只剝標記本身，中間文字是正文要留著。"""
        from src.models import strip_media_tags

        assert strip_media_tags("A <noscript>請開啟 JavaScript</noscript> B") == "A 請開啟 JavaScript B"

    def test_strips_case_variants(self):
        """來源 HTML 大小寫不一致；閉標記大小寫與開標記不同也要配得起來。"""
        from src.models import strip_media_tags

        assert strip_media_tags('X <IMG SRC="a.png"> Y') == "X Y"
        assert strip_media_tags('X < ScRiPt src="a.js">junk</SCRIPT> Y') == "X Y"

    def test_strips_orphan_closing_tag(self):
        """截斷的來源只剩閉標記——閉標記語法不可能是正文，一律剝。"""
        from src.models import strip_media_tags

        assert strip_media_tags("內容尾巴 </script>") == "內容尾巴"

    def test_strips_after_html_unescape_not_before(self):
        """順序硬規則：`&lt;img src=x&gt;` 解碼後才是標記，剝除必須排在 unescape 之後。

        寫反的話這種 escape 過的殘留會原封不動漏到「原始資料 box」。
        """
        got = self._item(abstract="&lt;img src=&quot;a.png&quot;&gt; 正文開始").abstract
        assert got == "正文開始"

    def test_field_that_is_only_a_tag_becomes_empty(self):
        from src.models import strip_media_tags

        assert strip_media_tags('< img src="a.png" width="400">') == ""

    def test_newline_around_tag_is_preserved(self):
        """標記兩側原本是換行就還一個換行，不要把段落壓成一行。"""
        from src.models import strip_media_tags

        assert strip_media_tags('第一段\n<img src="a.png">\n第二段') == "第一段\n第二段"

    # ---- 絕對不能剝的（守正常內容）----

    def test_keeps_generics_and_cli_placeholders(self):
        """實測 data/raw 的正常內容：泛型與 CLI 說明的角括號佔位符。"""
        from src.models import strip_media_tags

        for text in (
            "let v: Vec<String> = vec![];",
            "usage: tool <version> <id> <std>",
            "type Agent<T> = { skills: Set<string> }",
        ):
            assert strip_media_tags(text) == text

    def test_keeps_bare_style_and_script_placeholders(self):
        """裸的 `<style>` / `<script>`（無屬性、無配對閉標記）是 CLI 佔位符不是標記。

        兩筆都是實測 data/raw 的 GitHub README：
        `--style <style>          Style (vivid, natural)`、
        `pnpm --filter <name> <script>`。把它們當標記剝掉會讓 CLI 說明缺一格參數，
        而這正是「白名單擴大」最容易誤傷的形態——白名單裡的字剛好也是常見參數名。
        """
        from src.models import strip_media_tags

        cli = "--quality <level>        Quality (standard, hd)\n--style <style>          Style (vivid, natural)"
        assert strip_media_tags(cli) == cli
        pnpm = "Per-package commands run via pnpm --filter <name> <script> — e.g. pnpm --filter just-bash test:wasm ."
        assert strip_media_tags(pnpm) == pnpm

    def test_keeps_unrelated_html_tags(self):
        """白名單以外的標記不歸這個函式管（`<p>` / `<a>` 由別處處理）。"""
        from src.models import strip_media_tags

        text = "<p>段落</p> 與 <a href='x'>連結</a>"
        assert strip_media_tags(text) == text

    def test_keeps_paired_non_media_markup_and_its_content(self):
        """成對的非媒體標記連內容都要留——實測 data/raw 的三種形態。

        `<tex-math>` 是 Semantic Scholar 摘要的數值本體（`$29\\times$` 是論文的
        關鍵結果），`<think>` / `<sub>` 同理。白名單一旦擴大，成對剝除規則會把
        這些內容整段吃掉，論文摘要會憑空少一個數字——比標記露出更難發現。
        """
        from src.models import strip_media_tags

        for text in (
            r'speedup of <tex-math notation="LaTeX">$29\times $ </tex-math> over baseline',
            "prompt <think>推理過程</think> 之後",
            "H<sub>2</sub>O",
        ):
            assert strip_media_tags(text) == text

    def test_untouched_text_is_returned_verbatim(self):
        """沒有標記就完全不動——包括縮排與行尾空白（GitHub README 的對齊排版）。"""
        from src.models import strip_media_tags

        text = "  --flag   value\n\n  第二段  "
        assert strip_media_tags(text) == text

    def test_idempotent(self):
        from src.models import strip_media_tags

        once = strip_media_tags('< img src="a.png" width="400"> 正文 <iframe src="b">x</iframe> 尾')
        assert strip_media_tags(once) == once

    def test_tags_field_also_goes_through_stripping(self):
        """tags 與 title/abstract 同屬 Layer A，語意要一致（實測目前 0 筆命中）。"""
        assert self._item(tags=['< img src="a.png"> 開源']).tags == ["開源"]
