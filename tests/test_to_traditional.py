"""OpenCC 簡→繁雙層防線測試。

Layer A：來源端（ContentItem 建構即轉繁，量子位 / ChatPaper 等中國 source）。
Layer B：生成端（save_blog_post 寫檔前攔截免費 LLM 偶發吐出的簡體字）。
"""

from __future__ import annotations

from datetime import date, datetime

import pytest

from src.generators.blog_post import save_blog_post
from src.models import ContentItem, GeneratedContent, ScoredItem, SourceType
from src.utils import _apply_variant_fixes, to_traditional, to_traditional_shape_only

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

    @pytest.mark.parametrize(
        "text",
        [
            "該獎項每年吸引數百款產品參選",  # 語料實測 1 處；改壞成「吸參數百款」
            "檢索引數量偏低需要調整",
            "牽引數值需要重新校正",
            "指引數量不足以支撐決策",
            "援引數十篇論文佐證",  # 不用「數據」——那是 s2twp 詞庫的正常轉換，與本條無關
        ],
    )
    def test_yinshu_fix_does_not_eat_verb_plus_yin(self, text):
        """`引數→參數` 需要負向後顧：「動詞＋引」＋「數」會自然拼出 `引數`。

        這條在 `_TERM_FIXES` 裡當定值替換時是靜默誤傷——2026-08-02 把
        `repair-content` 擴到 output/posts 正文才第一次真的碰到它（在那之前
        純繁體欄位被兩層守門擋著，這條規則從來沒套上去過）。
        """
        assert to_traditional(text) == text
        assert to_traditional_shape_only(text) == text

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


class TestVariantFixesAtLayerA:
    """`_VARIANT_FIXES` 從 repair 層搬進 Layer A（2026-07-31）。

    why 要搬：`repair-content` 的變體修正只能補歷史，而 `to_traditional()`
    是**所有新資料的生產路徑**，每天仍在產同一批錯字。實測 41 條裡有 28 條
    在 Layer A 路徑真的會被觸發（其中 4 條需要真實脈絡才觸發，見
    `test_variant_fix_needs_real_context`）。
    """

    @pytest.mark.parametrize(
        "simplified, wrong, right",
        [
            ("更复杂的推理链路", "更復雜", "更複雜"),
            ("不复杂的架构", "不復雜", "不複雜"),
            ("这是个死胡同", "死衚衕", "死胡同"),
            ("他很克制这个冲动", "剋制", "克制"),
            ("股价跌到20年谷底了", "穀底", "谷底"),
            ("台积电流片", "臺積電", "台積電"),
            ("金属托盘", "金屬託盤", "金屬托盤"),
            ("背负骂名", "揹負", "背負"),
            ("总台直播", "總檯", "總臺"),
            ("在签什么合约", "在籤什麼", "在簽什麼"),
            ("这只会营造假象", "這隻會營造", "這只會營造"),
        ],
    )
    def test_layer_a_no_longer_emits_variant_errors(self, simplified, wrong, right):
        out = to_traditional(simplified)
        assert wrong not in out, f"Layer A 仍在產出錯字 {wrong!r}：{out!r}"
        assert right in out

    @pytest.mark.parametrize(
        "simplified, wrong, right",
        [
            # 這幾條的最小輸入（合并请求 / 系统化）s2twp 本來就轉對，
            # 只有帶著真實脈絡時才會被詞組規則改壞——用最小輸入驗證會假綠。
            ("代码提交合并请求", "合並請求", "合併請求"),
            ("帮助你系统化学习", "係統化", "系統化"),
        ],
    )
    def test_variant_fix_needs_real_context(self, simplified, wrong, right):
        out = to_traditional(simplified)
        assert wrong not in out, f"Layer A 仍在產出錯字 {wrong!r}：{out!r}"
        assert right in out

    def test_variant_table_itself_is_idempotent(self):
        """表本身要冪等（修正後再套一次不變）。

        注意這裡刻意測**表**而不是整條 `to_traditional()` 路徑——後者對繁體輸入
        本來就不冪等（s2twp 詞組規則：文件→檔案），那是既有設計，由 Layer B
        改用 s2tw 來收尾，不是本表的責任。
        """
        once = _apply_variant_fixes("更復雜的死衚衕與剋制")
        assert _apply_variant_fixes(once) == once
        assert once == "更複雜的死胡同與克制"


class TestVariantFixGateKnownLimitation:
    """守門的已知代價：繁簡同形的輸入修不到。

    `他很克制` / `20年谷底` 每個字都是繁簡通用 ⇒ 守門判定「不含簡體」⇒ 不套變體表，
    但 s2twp 的**詞組規則**仍把它們改成 `剋制` / `穀底`。

    ## 實際影響範圍很小

    只要欄位裡有**別的**簡體字撐著守門就會放行並修好——而量子位 / ChatPaper 這類
    真實來源的 abstract 是整段簡體，必然如此（實測 `他很克制这个冲动` → `克制`、
    `股价跌到20年谷底了` → `谷底`，都修對）。受影響的只有「純繁簡同形的短欄位」。

    ## why 接受這個代價

    另一種判準「OpenCC 真的改變了文字就套表」能修好這幾個，但實測會**引入新錯**：
    `委託馬斯克撰寫文檔` →（文檔→文件 觸發轉換）→ 套表 → `委托馬斯克`。
    專案在簡繁修正上的一貫原則是**寧可少修也不要造新錯**（見 `repair.py` 變體表
    註解），且這幾個 case 在搬表之前就已經是這樣——是「沒修好舊錯」而非「改壞」。

    ## 未來要根治的方向

    根因是 `to_traditional()`（s2twp）被無條件套在所有 `ContentItem` 上，包含
    本來就是繁中的來源。正解是讓 Layer A 只對簡體來源生效，而不是繼續加修正表。
    """

    @pytest.mark.parametrize(
        "text, still_wrong",
        [
            ("他很克制", "他很剋制"),
            ("20年谷底", "20年穀底"),
        ],
    )
    def test_homograph_input_is_not_repaired(self, text, still_wrong):
        assert to_traditional(text) == still_wrong

    @pytest.mark.parametrize(
        "text, expected",
        [
            ("他很克制这个冲动", "他很克制這個衝動"),
            ("股价跌到20年谷底了", "股價跌到20年谷底了"),
        ],
    )
    def test_same_words_are_repaired_once_gate_opens(self, text, expected):
        """同樣的詞，只要欄位裡有別的簡體字撐著守門就修得到（真實來源的常態）。"""
        assert to_traditional(text) == expected


class TestVariantFixGateProtectsTraditional:
    """守門：變體表只在「輸入真的含簡體字」時才套。

    why 需要這道門：變體表修的是「OpenCC 轉換時挑錯分支」，這種錯**只可能發生在
    真的被轉換的文字上**。無條件套用會把下列**正確的繁體**改壞——這些反例不是
    假想，`託馬斯`（←「委託馬斯克」）在 AI 新聞語境是高頻真實風險。
    """

    @pytest.mark.parametrize(
        "traditional_text",
        [
            "董事會委託馬斯克主導這項收購案",  # 託馬斯 → 托馬斯
            "把關係統化條列出來",  # 係統化 → 系統化
            "五行相剋制衡的道理",  # 剋制 → 克制
            "稻穀底部的含水率影響儲存年限",  # 穀底 → 谷底
            "農民曆史上首次全面數位化",  # 曆史 → 歷史
            "看完這一齣來評論才公道",  # 一齣來 → 一出來
            "把總檯帳搬到雲端",  # 總檯 → 總臺
        ],
    )
    def test_pure_traditional_input_is_untouched(self, traditional_text):
        assert to_traditional(traditional_text) == traditional_text

    def test_gate_lets_genuinely_simplified_through(self):
        """守門不能矯枉過正：整段簡體仍須完整轉換 + 套變體修正。"""
        assert to_traditional("更复杂的托盘设计") == "更複雜的托盤設計"


class TestLayerBGateProtectsTraditional:
    """Layer B 的逐段守門（2026-08-02）：只採納「原片段真的含簡體」的變更。

    why：`to_traditional_shape_only()` 的 docstring 原本宣稱「s2tw 無詞庫，對繁體
    輸入冪等」——**這句是錯的**。s2tw 仍帶 TWVariants 的一簡對多繁分歧規則，對
    純繁體輸入照樣改寫：

        「證明了透過實驗」→「證明瞭透過實驗」   ← LLM 生成的就是繁中，每天在壞

    實測 2026-08-01 當天 23 篇裡 2 篇中招，全語料 `output/posts` + `output/blogs`
    已有 47 個檔案被寫入 `證明瞭 / 說明瞭 / 表明瞭`。

    守門用 difflib 對齊，逐 opcode 判「這段原文含不含簡體」。判準沿用既有的
    `_is_simplified_char()`（含 `_NOT_SIMPLIFIED_EVIDENCE` 的干/托 例外）——
    不可改用 `OpenCC("t2s")` 或 `OpenCC("s2t")` 直接判：`s2t('干') == '幹'`，
    會讓「受到干擾」過門後被改成「受到幹擾」。
    """

    @pytest.mark.parametrize(
        "traditional_text",
        [
            "PRISM2 的成功證明了多模態對話是關鍵",  # 證明了 → 證明瞭（171 處，最高頻）
            "這個架構正是為了解決長上下文而生",  # 為了解 → 為瞭解
            "這只是一個初步結果",  # 只是 → 隻是
            "儀表板顯示訓練損失下降",  # 儀表板 → 儀錶板
            "昂貴的定制晶片並非必要",  # 定制 → 定製
            "目前的局限與未來方向",  # 局限 → 侷限
            "預測分布的形狀相當集中",  # 分布 → 分佈
            "資料污染檢測是必要步驟",  # 污染 → 汙染
            "受到干擾的訊號需要濾波",  # 干擾 → 幹擾（守門字 `干` 的反例）
        ],
    )
    def test_pure_traditional_input_is_untouched(self, traditional_text):
        assert to_traditional_shape_only(traditional_text) == traditional_text

    @pytest.mark.parametrize(
        "simplified, expected",
        [
            ("这个应该转换", "這個應該轉換"),
            ("干扰信号很强", "干擾信號很強"),  # 簡體 + 守門字共存，仍須轉
            ("为了解决这个问题", "為了解決這個問題"),
            ("应用于文档处理", "應用於文檔處理"),  # 無詞庫：文档→文檔，不是檔案
        ],
    )
    def test_gate_lets_genuinely_simplified_through(self, simplified, expected):
        """守門不能矯枉過正：Layer B 存在的理由就是擦掉 LLM 偶發吐出的簡體字。"""
        assert to_traditional_shape_only(simplified) == expected

    def test_layer_b_is_idempotent_on_its_own_output(self):
        """跑兩次要等於跑一次——`backfill` 與 `--supplement` 每天會重讀重寫。"""
        once = to_traditional_shape_only("这个模型证明了扩展法则依然成立")
        assert to_traditional_shape_only(once) == once


class TestOpenCCVersionGuard:
    """釘住 `opencc<1.3.2` 上限的**理由**，而不只是在 pyproject 寫個數字。

    **1.3.2**（不是 1.4）起 s2twp 詞庫新增 `B超 → 超音波`（醫學 B 型超音波）
    且無詞邊界保護，任何「數字+B+超」都會被吃掉。`7B`/`70B`/`405B` 是本專案最核心
    的術語形狀，後接「超大 / 超強 / 超越 / 超輕量」是極自然的中文搭配，且轉換
    **不可逆**（`753超音波大` 無法反推原本是 B）。

    這條測試存在的意義：原本的上限寫 `<1.4`，而 `pip install -e .` 每天在 CI
    無鎖版安裝——本機 venv 停在 1.3.1 剛好全綠，生產環境卻會裝到 1.3.2。
    版本錯了這幾條會紅，不會再靜默漂移。
    """

    @pytest.mark.parametrize(
        "simplified, expected",
        [
            ("753B超大参数", "753B超大參數"),
            ("70B超越了GPT-4", "70B超越了GPT-4"),
            ("8B超轻量模型", "8B超輕量模型"),
            ("参数量7B超过预期", "參數量7B超過預期"),
        ],
    )
    def test_model_size_before_chao_is_not_eaten(self, simplified, expected):
        assert to_traditional(simplified) == expected


class TestHarvestedFrom14:
    """1.4 修對、1.3 沒修的詞，以 `_TERM_FIXES` 條目在 1.3 上收割。

    量測全語料 32,950 個去重欄位後挑出來的（見 2026-07-31 版本評估）：
    這兩條是升 1.4 才會拿到、且不帶副作用的淨改善。
    """

    def test_xiangxiang_uses_correct_form(self):
        assert to_traditional("想象一下这个场景") == "想像一下這個場景"

    def test_marketing_uses_taiwan_term(self):
        assert to_traditional("市场营销团队") == "市場行銷團隊"

    def test_term_fixes_also_apply_at_layer_b(self):
        """這兩條修的是「該轉而沒轉」，與輸入含不含簡體無關 ⇒ 兩層都要套。"""
        assert to_traditional_shape_only("想象力") == "想像力"


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


class TestExternallyVerifiedCandidates2026_07_31:
    """2026-07-31 巡邏候選經三道閘門後 merge 的 8 條。

    三道閘門（依 status.md 的三條鐵則）：
    ① ≥2 篇不同文章的真實脈絡（全 118 天語料統計，非 7 天窗口）
    ② 外部辭典交叉核對（教育部辭典），不採信單一審查者語感
    ③ 反例掃描：key 字串不得命中語料裡正確的用法

    被閘門擋掉而**刻意不收**的（理由見 docs 計畫的「已駁回候選」）：
    - `合作伙伴→合作夥伴`（13 次/12 篇）：教育部辭典「伙伴」與「夥伴」互通，非錯字
    - `幾周→幾週`（8 次/7 篇）：除周朝／賙濟外 `周`／`週` 一般可互用
    - `賽道里→賽道裡`（5 次/5 篇）、`文本里→文本裡`（2 次/2 篇）：語意判斷正確，
      但純字串 key 無法排除 `賽道里程`／`里數`，需負向前瞻，現行表格式不支援
    """

    @pytest.mark.parametrize(
        "simplified, wrong, right",
        [
            # 发生 → 髮生：OpenCC 把「结发」當成「結髮」詞組挑分支
            ("总结发生了什么变化", "總結髮生", "總結發生"),
            ("最有价值的讨论总发生在知乎", "總髮生", "總發生"),
            # 加注（投資加碼）→ 加註（註解）。全 17 筆語料脈絡皆為投資，
            # 但 `加註說明` 是合法用法，故一律帶左錨定
            ("产业与全球资本共同加注", "共同加註", "共同加注"),
            ("老股东持续加注", "持續加註", "持續加注"),
            ("获得资本加注身价暴涨", "資本加註", "資本加注"),
            ("小米战投连续三轮加注", "輪加註", "輪加注"),
            ("重磅加注这个赛道", "重磅加註", "重磅加注"),
            ("超额加注该项目", "超額加註", "超額加注"),
        ],
    )
    def test_layer_a_emits_corrected_form(self, simplified, wrong, right):
        out = to_traditional(simplified)
        assert wrong not in out, f"Layer A 仍在產出錯字 {wrong!r}：{out!r}"
        assert right in out, f"未產出正確形式 {right!r}：{out!r}"

    @pytest.mark.parametrize(
        "simplified, must_keep",
        [
            # 髮生 的反例：頭髮生長是正確用字，錨定必須避開
            ("头发生长速度", "頭髮生長"),
            ("头发生得很快", "頭髮生"),
            # 加註 的反例：註解語意的加註是正確用字
            ("请在这里加注说明", "加註說明"),
            ("给参数加注释", "註釋"),
        ],
    )
    def test_counterexamples_survive(self, simplified, must_keep):
        out = to_traditional(simplified)
        assert must_keep in out, f"新增條目誤傷了正確用法：{simplified!r} → {out!r}"
