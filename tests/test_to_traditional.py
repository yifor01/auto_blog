"""OpenCC 簡→繁雙層防線測試。

Layer A：來源端（ContentItem 建構即轉繁，量子位 / ChatPaper 等中國 source）。
Layer B：生成端（save_blog_post 寫檔前攔截免費 LLM 偶發吐出的簡體字）。
"""

from __future__ import annotations

from datetime import date, datetime

from src.generators.blog_post import save_blog_post
from src.models import ContentItem, GeneratedContent, ScoredItem, SourceType
from src.utils import to_traditional, to_traditional_shape_only

# 簡體字偵測集（出現在輸出 = 在地化失敗）。刻意只列繁簡異形字，
# 避免「谷」這類繁簡同形字造成誤判。
_SIMP_CHARS = set("应这对开发难关给优内东让实现产标过来说级码后单题问启动发书优")


def _simp_leak(text: str) -> str:
    return "".join(sorted(set(c for c in text if c in _SIMP_CHARS)))


class TestToTraditional:
    def test_converts_simplified_with_taiwan_terms(self):
        # s2twp 同時做字形轉換 + 台灣慣用詞轉換
        out = to_traditional("大模型的优化与训练：内存、性能、算法")
        assert out == "大模型的最佳化與訓練：記憶體、效能、演算法"

    def test_english_passthrough(self):
        s = "RAG retrieval augmented generation v2.0"
        assert to_traditional(s) == s

    def test_empty_string(self):
        assert to_traditional("") == ""

    def test_idempotent_on_traditional(self):
        once = to_traditional("谷歌釋出最強開源模型")
        assert to_traditional(once) == once

    def test_url_and_ascii_untouched(self):
        s = "见 https://www.qbitai.com/2026/06 的代码"
        out = to_traditional(s)
        assert "https://www.qbitai.com/2026/06" in out
        assert _simp_leak(out) == ""


class TestLayerASourceSide:
    def test_contentitem_title_and_abstract_converted_on_construct(self):
        item = ContentItem(
            source=SourceType.RSS,
            source_name="量子位",
            title="谷歌发布最强开源模型，性能超越竞品",
            url="https://www.qbitai.com/x",
            published_date=date.today(),
            abstract="该模型在多个基准测试中表现优异，支持长上下文与函数调用。",
        )
        assert _simp_leak(item.title) == ""
        assert _simp_leak(item.abstract) == ""
        assert "效能" in item.title  # 性能→效能 慣用詞轉換
        assert "函式呼叫" in item.abstract  # 函数调用→函式呼叫


class TestLayerBGenerationSide:
    def _scored(self) -> ScoredItem:
        item = ContentItem(
            source=SourceType.BLOG,
            source_name="Test",
            title="Test Article",
            url="https://example.com/x",
            abstract="A" * 150,
            published_date=date.today(),
        )
        return ScoredItem(item=item, rule_score=80.0, llm_score=70.0)

    def test_save_blog_post_strips_simplified_from_llm_output(self, tmp_path, monkeypatch):
        import src.generators.blog_post as bp

        monkeypatch.setattr(bp, "POSTS_DIR", tmp_path)
        monkeypatch.setattr(bp, "PROMPTS_DIR", tmp_path)

        # 模擬 LLM 吐出含簡體「应付」的內文（重現本次 Agnes 案例）
        gen = GeneratedContent(
            source_item=self._scored(),
            content="📌 標題\n\n這對小規模 Agent 尚可应付，但無法擴展。",
            prompt_used="p",
            model_used="agnes-2.0-flash",
            generated_at=datetime.now(),
        )
        path = save_blog_post(gen, target_date=date.today())
        written = open(path, encoding="utf-8").read()
        assert "应付" not in written
        assert "應付" in written
        assert _simp_leak(written) == ""


class TestTaiwanTermMisconversion:
    """s2twp 的 TWPhrases 是為 Windows/一般軟體 UI 設計的，套到 AI/ML 語境會誤轉。
    這些詞單次轉換就錯，與雙層轉換無關。
    """

    def test_parameter_not_converted_to_yinshu(self):
        assert to_traditional("模型有 975B 参数") == "模型有 975B 參數"

    def test_extension_not_converted_to_plugin_package(self):
        assert to_traditional("高效长上下文扩展") == "高效長上下文擴展"

    def test_offload_not_converted_to_uninstall(self):
        assert to_traditional("JAX 主机卸载") == "JAX 主機卸載"

    def test_local_not_converted_to_regional(self):
        assert to_traditional("局部感知") == "局部感知"

    def test_binding_uses_common_taiwan_form(self):
        assert to_traditional("不绑定任何特定模型") == "不綁定任何特定模型"

    def test_control_widget_not_mangled(self):
        assert to_traditional("控件") == "控制項"

    def test_correct_taiwan_terms_are_preserved(self):
        """修正表不能誤傷 s2twp 本來就轉對的詞。"""
        assert to_traditional("软件") == "軟體"
        assert to_traditional("内存") == "記憶體"
        assert to_traditional("插件") == "外掛"
        assert to_traditional("网络") == "網路"


class TestConversionIdempotency:
    """s2twp 對已是繁中的輸入不冪等：文档→文件→檔案。
    Layer A 轉過的 title/abstract 進 prompt，LLM 複述後 Layer B 再轉一次，
    就是「最新程式庫檔案餵進 LLM」的成因。Layer B 改用無詞庫的 s2tw 後應消失。
    """

    def test_simplified_wendang_still_converts_once(self):
        assert to_traditional("文档") == "文件"

    def test_layer_b_does_not_touch_traditional_wenjian(self):
        assert to_traditional_shape_only("文件") == "文件"

    def test_layer_a_then_layer_b_is_stable(self):
        """實際 pipeline 路徑：來源簡體 →(A)→ 進 prompt → LLM 複述 →(B)→ 落盤。"""
        after_a = to_traditional("最新库文档喂进 LLM")
        assert to_traditional_shape_only(after_a) == after_a, "Layer B 破壞了 Layer A 的結果"

    def test_layer_b_still_cleans_simplified_chars(self):
        """Layer B 仍須擦掉 LLM 偶發吐出的簡體字。"""
        assert to_traditional_shape_only("这个应该转换") == "這個應該轉換"


class TestTagsConverted:
    """tags 沒有經過 Layer A，導致網站 tag chip 顯示簡體（资讯 / 开源）。"""

    def test_contentitem_tags_converted_on_construct(self):
        item = ContentItem(
            source=SourceType.RSS,
            title="測試",
            url="https://example.com/a",
            published_date=date(2026, 7, 26),
            tags=["资讯", "开源", "吴恩达"],
        )
        assert item.tags == ["資訊", "開源", "吳恩達"]
