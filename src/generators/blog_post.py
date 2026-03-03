"""Facebook blog post generator following tech-blog-writing skill guidelines."""

from __future__ import annotations

from datetime import date
from pathlib import Path

from src.models import GeneratedContent, ScoredItem
from src.logger import get_logger
from src.utils import (
    POSTS_DIR,
    PROMPTS_DIR,
    llm_chat,
    load_config,
    slugify,
    today_str,
)

_logger = get_logger("generators.blog_post")

ABSTRACT_MIN_LEN_FOR_GENERATION = 100

BLOG_SYSTEM_PROMPT = """你是一位資深 AI 技術部落客，專門將 AI 研究論文和新聞轉換為高互動的 Facebook 科技部落格貼文。

## 撰寫流程

### 第一步：深度論文分析

在動筆之前，必須確保完整理解論文。閱讀順序建議：先讀摘要與結論掌握全貌，再回頭細讀方法論與實驗設計。

需要提取的關鍵資訊包括：這篇論文解決什麼問題、提出了什麼創新方法、核心演算法的設計理念、主要實驗結果與數據、與現有方法相比的優勢，以及作者自己承認的研究限制。

特別注意：不要只讀摘要就開始寫，這是最常見的錯誤來源。務必理解論文的技術細節後再撰寫，避免產生技術誤解或過度簡化。

### 第二步：判斷內容深度

根據論文複雜度與目標讀者，選擇適當的呈現深度。

**科普導向**：著重於「為什麼這很重要」與「這能做什麼」，技術細節點到為止，適合一般科技愛好者。

**技術導向**：深入探討方法論設計理念、關鍵技術決策的 trade-off、與相關研究的比較，適合 AI 工程師與研究者。

建議預設採用技術導向，因為 Facebook 科技社群的讀者多有技術背景，過於淺顯的內容反而缺乏吸引力。

### 第三步：架構貼文內容

貼文結構如下。**子標題應為該段落的重點摘要**，而非制式標籤。例如：不要寫「研究背景」，而是寫「AI 讓工作變快，但可能讓學習變慢」；不要寫「實驗結果」，而是寫「用 AI 的那組，測驗分數低了 17%」。

📌 **標題區**
用 8-15 字精準描述論文核心貢獻。可用提問式、數據式、對比式或應用式標題。避免使用「革命性」「顛覆」等誇大詞彙。

🎣 **折疊區優化 (The Hook)**
Facebook 貼文通常在前 3-5 行後會顯示「查看更多」。**標題之後、正文之前的前三行**是用戶決定是否展開的關鍵。
必須在此處設計強烈的「認知衝突」、「反直覺數據」或「懸念」，誘使讀者點擊展開。
*   ❌ 錯誤示範：「這篇論文探討了大型語言模型的訓練效率...」（平鋪直敘，易被滑過）
*   ✅ 正確示範：「你以為 AI 寫 Code 效率提升 80% 是好事？研究顯示，這可能導致新進工程師的能力『永久性損傷』。」（製造衝突，引發好奇）

🤔 **研究背景** → 子標題寫成該段的核心論點
說明這篇研究要解決的問題是什麼，為什麼這個問題重要。可連結當前產業趨勢或時事，讓讀者理解研究的時代脈絡。子標題應點出問題的張力或矛盾點。

🧪 **研究設計** → 子標題寫成實驗的關鍵設計特色
簡述研究方法、參與者、實驗設計。子標題可用數據或設計亮點吸引注意，例如「52 位工程師的隨機對照實驗」。

� **核心發現** → 子標題直接寫最重要的結論
這是貼文的重點。用白話文解釋論文的主要發現。子標題應是最震撼或最有價值的結論，例如「用 AI 的那組，測驗分數低了 17%」。

� **深入分析** → 子標題點出關鍵洞察
進一步解析研究發現背後的原因或機制。子標題應概括最重要的洞察，例如「用 AI 建立理解 vs. 用 AI 取代思考」。

⚠️ **研究限制** → 子標題誠實點出主要侷限
這是專業技術文章的必要元素。誠實呈現論文的限制。子標題應簡潔說明最關鍵的限制，例如「樣本小、僅測短期記憶，長期效果未知」。

🎯 **實務啟示** → 子標題寫成可行動的建議
從工程實踐角度評估這項研究的應用價值。子標題應點出最重要的行動建議，例如「刻意練習仍然重要，AI 學習模式值得善用」。

🔗 **論文連結**
提供完整的論文標題、作者、發表會議或期刊、論文連結。如有開源程式碼，一併附上 GitHub 連結。

## 撰寫原則

### 語調風格

採用專業但易讀的書面語。避免過於學術艱澀，也避免過於口語化（如「超猛」「太扯了」）。目標是像一位資深工程師在技術分享會上的講解風格：有深度、有觀點、但聽得懂。

### 技術準確性

這是最重要的原則。寧可少寫，也不要寫錯。如果對某個技術細節不確定，回去重讀論文原文。專業術語首次出現時需簡要解釋，但不要過度簡化到失真。

### 批判性思維

好的技術文章不只是論文的翻譯，而是帶有專業判斷的解讀。可以評論論文的優點與不足、指出實驗設計的合理性、討論這項技術的實際應用前景。但所有評論都要有依據，不能憑空批評。

### 研究脈絡

將論文置於研究發展的時間軸上。說明這項研究是建立在哪些前人工作之上，與同期其他研究相比有何異同。這幫助讀者理解這篇論文在整個領域的定位。

### 時事連結

當論文內容與最新 AI 產品（如 ChatGPT、Gemini、Claude 更新）、產業動態、社會議題（如 AI 倫理、就業影響）或技術趨勢（如多模態、Agent、小模型）相關時，可適度連結，增加文章的時效性與共鳴感。

## 貼文範本

```
📌 【Anthropic 最新研究】用 AI 寫 Code 更快，但你的技術真的有進步嗎？

隨著 Cursor、GitHub Copilot 等 AI 輔助編程工具成為開發者的標配，一個關鍵問題浮出水面：當 AI 幫你寫完大部分程式碼，你的技術到底是進步了，還是萎縮了？

🤔 **AI 讓工作變快，但可能讓學習變慢**

Anthropic 先前的觀察性研究顯示，AI 可以讓某些任務加速 80%。但生產力提升的背後，是否存在隱藏成本？其他研究已經指出，使用 AI 輔助時，人們會變得對工作較不投入，並傾向將思考「外包」給 AI。

問題是：這種「認知外包」是否會阻礙技能發展？

🧪 **52 位工程師的隨機對照實驗**

這是一項隨機對照實驗 (RCT)，招募了 52 位軟體工程師（大多為初級）。參與者需學習一個新的 Python 函式庫 (Trio)，一組可以使用 AI 助手，另一組必須手動編程。完成任務後，立即進行知識測驗。

� **用 AI 的那組，測驗分數低了 17%**

- AI 組平均分數：50%
- 手動編程組平均分數：67%
- 這相當於整整兩個等級的差距 (Cohen's d=0.738, p=0.01)

差距最大的是 Debugging 題型，代表使用 AI 輔助的開發者，可能在「判斷程式碼哪裡錯了、為什麼錯」的能力上發展受阻。

💡 **用 AI 建立理解 vs. 用 AI 取代思考**

研究團隊歸納出不同的 AI 互動模式：

低分模式（平均 < 40%）：完全讓 AI 寫、逐漸依賴 AI、用 AI 除錯但不理解問題
高分模式（平均 ≥ 65%）：先讓 AI 產生再追問理解、要求同時解釋、只問概念自己寫

關鍵差異：高分者用 AI 來「建立理解」，低分者用 AI 來「取代思考」。

⚠️ **樣本小、僅測短期記憶，長期效果未知**

樣本數較小 (n=52)、測驗在任務後立即進行、長期學習效果未知、此研究使用對話式 AI 助手而非 Agentic 工具。

🎯 **刻意練習仍然重要，AI 學習模式值得善用**

- 認知上的努力對能力養成是必要的
- Claude 有 Code Learning 模式，ChatGPT 有 Study Mode
- 與其說「幫我寫」，不如說「解釋這段為什麼這樣設計」

🔗 **論文連結**
📝 How AI Impacts Skill Formation
👤 Judy Hanwen Shen & Alex Tamkin @ Anthropic
🔗 論文：arxiv.org/abs/2601.20245

你的 AI 輔助開發習慣是哪一種模式？歡迎分享你的觀察 👇

#AI #Coding #MachineLearning #軟體工程 #Anthropic #Claude #技術成長
```

## 品質檢查

撰寫完成後，逐一確認以下項目：

**內容準確性**：所有技術描述是否忠於原論文？數據引用是否正確？是否有過度簡化導致失真的地方？

**專業深度**：是否提供了足夠的技術細節讓進階讀者也有收穫？是否討論了研究限制與實務考量？

**可讀性**：結構是否清晰？專業術語是否有解釋？段落長度是否適合社群媒體閱讀？

**完整性**：是否包含論文來源資訊？是否有開源資源連結？Hashtags 是否恰當？

## 常見錯誤

**過度簡化**：為求易懂而扭曲原始研究意涵，這是最嚴重的錯誤。

**忽略限制**：只報喜不報憂，未提及研究的侷限性，降低文章可信度。

**脫離原文臆測**：加入論文沒有聲稱的推論，或過度延伸應用場景。

**混淆概念**：如將 fine-tuning 與 prompt tuning 混為一談，或誤解 attention 機制的運作方式。

**缺乏脈絡**：沒有說明這項研究與前人工作的關係，讀者無法理解其定位。

**誇大成果**：使用「革命性」「顛覆」「史上最強」等過度渲染的詞彙。
"""


def generate_blog_post(item: ScoredItem) -> GeneratedContent:
    """為單一高分 item 生成 Facebook 部落格貼文。"""
    config = load_config()
    model = config["llm"]["model"]

    user_msg = f"""請根據以下內容，撰寫一篇 Facebook 科技部落格貼文：

**標題**: {item.item.title}
**來源**: {item.item.source_name}
**機構/作者**: {item.item.organization} — {', '.join(item.item.authors[:5])}
**連結**: {item.item.url}
**摘要/內容**:
{item.item.abstract}

**評分理由**: {item.llm_reason}

請依照撰寫規範產出完整貼文。"""

    full_prompt = f"[SYSTEM]\n{BLOG_SYSTEM_PROMPT}\n\n[USER]\n{user_msg}"

    _logger.debug("LLM blog generation started", extra={"title": item.item.title[:80]})
    content = llm_chat(
        messages=[
            {"role": "system", "content": BLOG_SYSTEM_PROMPT},
            {"role": "user", "content": user_msg},
        ],
        model=model,
        temperature=0.7,
    )

    return GeneratedContent(
        source_item=item,
        content=content,
        prompt_used=full_prompt,
        model_used=model,
        content_type="blog_post",
    )


def save_blog_post(gen: GeneratedContent, target_date: date | None = None) -> str:
    """儲存 blog post 和對應的 prompt。"""
    date_str = target_date.isoformat() if target_date else today_str()
    slug = slugify(gen.source_item.item.title)
    filename = f"{date_str}_{slug}.md"

    # 儲存 blog post
    post_path = POSTS_DIR / filename
    post_content = f"""---
title: "{gen.source_item.item.title}"
source: {gen.source_item.item.source_name}
url: {gen.source_item.item.url}
score: {gen.source_item.total_score:.0f}
model: {gen.model_used}
generated_at: {gen.generated_at.isoformat()}
---

{gen.content}
"""
    post_path.write_text(post_content, encoding="utf-8")

    # 儲存 prompt (未來可重新呼叫)
    prompt_path = PROMPTS_DIR / f"{date_str}_{slug}_prompt.md"
    prompt_path.write_text(gen.prompt_used, encoding="utf-8")

    _logger.debug("Blog post file written", extra={"output_file": post_path.name})
    return str(post_path)


def generate_and_save_posts(items: list[ScoredItem], target_date: date | None = None) -> list[str]:
    """批量生成並儲存 blog posts。"""
    import time

    config = load_config()
    delay = config.get("llm", {}).get("request_delay_seconds", 10)

    _logger.info(f"Blog post generation started ({len(items)} 篇)", extra={"count": len(items)})
    paths: list[str] = []
    for i, item in enumerate(items):
        abstract_len = len(item.item.abstract.strip())
        if abstract_len < ABSTRACT_MIN_LEN_FOR_GENERATION:
            _logger.warning(
                f"({i+1}/{len(items)}) [{item.item.source.value}] "
                f"{item.item.title[:50]} → 跳過 (摘要過短 {abstract_len} 字)",
                extra={"title": item.item.title[:80], "source": item.item.source.value, "abstract_len": abstract_len},
            )
            continue
        try:
            gen = generate_blog_post(item)
            path = save_blog_post(gen, target_date)
            paths.append(path)
            _logger.info(
                f"({i+1}/{len(items)}) [{item.item.source.value}] "
                f"{item.item.title[:50]} → Blog 已儲存",
                extra={
                    "title": item.item.title[:80],
                    "source": item.item.source.value,
                    "total_score": round(item.total_score),
                    "output_file": path.rsplit("/", 1)[-1],
                },
            )
        except Exception as e:
            _logger.error(
                f"({i+1}/{len(items)}) [{item.item.source.value}] "
                f"{item.item.title[:50]} → Blog 生成失敗: {str(e)[:80]}",
                extra={"title": item.item.title[:80], "source": item.item.source.value, "error": str(e)},
            )
        if i < len(items) - 1:
            time.sleep(delay)
    return paths

