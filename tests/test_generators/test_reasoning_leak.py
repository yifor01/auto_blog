"""生成端推理外洩 / 退化迴圈偵測。

免費 model（尤其 google/gemma-4-31b-it:free）偶發把 chain-of-thought 當成正文吐出，
甚至連 system prompt 的「撰寫規範」字樣一起洩漏，或陷入 degenerate repetition。
這些內容目前會直接落盤成 .md 並 ship 上站——實際樣本見
output/posts/2026-07-10_ai-model-co-design-hardware-friendly-llm-design.md（20KB 全是 CoT，
單一片段重複 510 次）。

llm_chat 已支援 validate=，讓爛輸出原地降級下一個 model，生成端接上即可。
"""

from __future__ import annotations

from src.generators.blog_post import looks_like_reasoning_leak

# ── 真實洩漏樣本（節錄自站上實際產出） ──────────────────────────

REAL_ENGLISH_COT = (
    "We need to produce a blog article in Traditional Chinese, based on the given info. "
    'Must follow the "撰寫規範" from system message, which includes: source must be only '
    "the provided URL, no extra facts, no hallucination. Must not add any info not given."
)

REAL_CHINESE_SELF_NARRATION = "這是一篇針對「產業新聞／部落格報導」型別的技術轉寫。"

REAL_DEGENERATE_LOOP = (
    "以下是文章。\n\n"
    + "then sections like 標題, 來源, 連結, " * 60
)

# ── 正常文章（不得誤判） ────────────────────────────────────

NORMAL_POST = """📌 【NVIDIA 開源新作】TensorRT-LLM：讓 Blackwell GPU 跑滿的關鍵

NVIDIA 在最新一篇技術部落格中，說明了硬體感知的 Transformer 模型設計原則。

## 重點整理

- 線性層維度應接近方形，並對齊 GPU tile 大小（128 的倍數，理想為 256 或 512）
- NVFP4 量化搭配 TensorRT Model Optimizer，可在維持精度的前提下提升吞吐量
- Expert Parallelism 讓大型 MoE 模型跨多節點擴展

## 為什麼重要

AI 效能可以拆成三個面向：準確度、吞吐量、互動性。三者必須平衡——
準確度再高，回應太慢也沒用。

來源：https://developer.nvidia.com/blog/ai-model-co-design-hardware-friendly-llm-design/
"""

NORMAL_POST_WITH_ENGLISH_QUOTE = """📌 Anthropic 談 Agent 設計

Anthropic 在文章中提到一個核心原則：

> We recommend that developers start with the simplest solution possible,
> and only increase complexity when needed.

這句話點出了目前 Agent 開發的常見誤區：過早引入複雜的多層架構。

來源：https://www.anthropic.com/engineering/building-effective-agents
"""


class TestDetectsRealLeaks:
    def test_english_chain_of_thought(self):
        assert looks_like_reasoning_leak(REAL_ENGLISH_COT)

    def test_system_prompt_marker_leaked(self):
        assert looks_like_reasoning_leak(REAL_ENGLISH_COT), "「撰寫規範」外洩應被攔下"

    def test_chinese_self_narration(self):
        assert looks_like_reasoning_leak(REAL_CHINESE_SELF_NARRATION)

    def test_degenerate_repetition_loop(self):
        assert looks_like_reasoning_leak(REAL_DEGENERATE_LOOP)

    def test_other_chinese_narration_forms(self):
        for s in [
            "根據您提供的資訊，本文屬於「產業新聞／部落格報導」型別。",
            "好的，我將根據您提供的資訊撰寫一篇繁體中文技術部落格文章。",
        ]:
            assert looks_like_reasoning_leak(s), s


class TestDoesNotFalsePositive:
    def test_normal_post_passes(self):
        assert not looks_like_reasoning_leak(NORMAL_POST)

    def test_english_blockquote_in_body_passes(self):
        """正文中段引用英文是正常的，只有『開頭就是英文推理』才算洩漏。"""
        assert not looks_like_reasoning_leak(NORMAL_POST_WITH_ENGLISH_QUOTE)

    def test_empty_content_is_not_a_leak(self):
        """空內容由 save_blog_post 的既有 guard 處理，不歸這裡管。"""
        assert not looks_like_reasoning_leak("")

    def test_repeated_markdown_structure_is_not_a_loop(self):
        """條列式文章會有重複的短前綴，不該被當成退化迴圈。"""
        listing = "📌 每日精選\n\n" + "".join(
            f"- 第 {i} 則：這是一段長度足夠的正常摘要文字，用來確認不會誤判。\n"
            for i in range(40)
        )
        assert not looks_like_reasoning_leak(listing)


class TestWiredIntoGeneration:
    """偵測函式存在還不夠——要確認 generate_blog_post 真的把它交給 llm_chat。"""

    def _scored(self):
        from datetime import date

        from src.models import ContentItem, ScoredItem, SourceType

        item = ContentItem(
            source=SourceType.BLOG,
            source_name="NVIDIA Developer",
            title="AI Model Co-Design",
            url="https://developer.nvidia.com/blog/x",
            abstract="A" * 200,
            published_date=date(2026, 7, 10),
        )
        return ScoredItem(item=item, rule_score=90.0, llm_score=80.0)

    def test_generate_passes_validate_that_rejects_cot(self, monkeypatch):
        import src.generators.blog_post as bp

        captured = {}

        def fake_llm_chat(**kwargs):
            captured.update(kwargs)
            return NORMAL_POST

        monkeypatch.setattr(bp, "llm_chat", fake_llm_chat)
        bp.generate_blog_post(self._scored())

        validate = captured.get("validate")
        assert validate is not None, "generate_blog_post 沒有傳 validate，爛輸出不會降級"
        assert validate(NORMAL_POST) is True
        assert validate(REAL_ENGLISH_COT) is False
        assert validate(REAL_DEGENERATE_LOOP) is False


class TestStripPreamble:
    """17/21 的實際洩漏只是開頭多一句自述，正文完好。整篇丟掉重生成等於白燒
    一次 LLM 額度，而且下一個 model 未必寫得更好——能剝就剝，剝不掉才降級。
    """

    def test_strips_chinese_narration_before_emoji_marker(self):
        from src.generators.blog_post import strip_reasoning_preamble

        raw = "這是一篇針對「產業新聞」型別的技術部落格文章。\n\n📌 【NVIDIA】創下世界紀錄\n\nTL;DR：內容"
        assert strip_reasoning_preamble(raw).startswith("📌 【NVIDIA】")

    def test_strips_narration_with_horizontal_rule(self):
        from src.generators.blog_post import strip_reasoning_preamble

        raw = "根據您提供的資訊，這屬於「開源專案」。\n\n---\n\n📌 【Andrew Ng】OpenWorker\n\n內文"
        assert strip_reasoning_preamble(raw).startswith("📌 【Andrew Ng】")

    def test_leaves_clean_post_untouched(self):
        from src.generators.blog_post import strip_reasoning_preamble

        assert strip_reasoning_preamble(NORMAL_POST) == NORMAL_POST

    def test_strippable_post_passes_validation(self):
        """剝掉前綴後就是好文章 → 不該被降級。"""
        raw = "這是一篇針對「產業新聞」型別的技術部落格文章。\n\n" + NORMAL_POST
        assert not looks_like_reasoning_leak(raw)

    def test_unsalvageable_post_still_rejected(self):
        """英文 CoT 沒有 📌 錨點可剝，仍須降級。"""
        assert looks_like_reasoning_leak(REAL_ENGLISH_COT)
        assert looks_like_reasoning_leak(REAL_DEGENERATE_LOOP)

    def test_generate_returns_stripped_content(self, monkeypatch):
        """wiring：generate_blog_post 回傳的 content 必須已剝除前綴。"""
        import src.generators.blog_post as bp

        raw = "這是一篇針對「產業新聞」型別的技術部落格文章。\n\n" + NORMAL_POST
        monkeypatch.setattr(bp, "llm_chat", lambda **kw: raw)
        gen = bp.generate_blog_post(TestWiredIntoGeneration()._scored())
        assert gen.content.startswith("📌"), "前綴沒被剝掉，會直接落盤上站"
