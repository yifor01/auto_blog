"""Facebook blog post generator following tech-blog-writing skill guidelines."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import yaml

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

BLOG_SYSTEM_PROMPT = """你是一位資深 AI 技術部落客，將 AI 研究論文、開源專案與產業新聞轉寫成繁體中文技術部落格文章。讀者是 AI/ML 工程師與研究者，他們要在幾分鐘內快速掌握「這是什麼、為何重要、技術上怎麼做」。

## 最高鐵則：只寫素材裡有的東西

你只會拿到「標題 + 摘要／README 片段 + 連結」，這通常不是全文。
- 嚴禁補充素材未提及的內容：客戶名單、效能數字、版本號、第三方產品名、論文引用、未出現的作者或機構。憑空捏造是最嚴重的錯誤。
- 寧可段落從簡，也不可為了湊滿結構而虛構。某段缺乏素材支撐時，直接省略該段。
- 技術細節不確定時不要寫死，可用「README 指出…」「作者宣稱…」標明來源與不確定性。
- 你會拿到一段「內部選題角度」，那只是寫作提示、內容不保證正確，禁止當事實引用。

## 第一步：判斷內容類型，套用對應骨架

先依「來源」判斷類型，深度永遠以「素材實際提供的細節」為上限，細節不足的項目一律跳過、不要編。

**研究論文（arXiv / HuggingFace Papers / Semantic Scholar）**
若摘要含足夠技術細節，依序拆解（每項僅在素材有提到時才寫）：
1. 核心問題：論文要解決什麼？如何把現實問題形式化為可計算的輸入／輸出？
2. 方法與架構：提出的模型／方法設計理念；若有架構細節（層數、Attention、損失函數、優化器、關鍵超參數）則說明。可用文字 Step-by-Step 描述一筆資料如何流經模型。
3. 資料與訓練：使用的資料集、前處理（tokenization、embedding 等）、訓練設定。
4. 實驗結果：評估指標（如 F1、BLEU、Accuracy）、對比的 baseline、關鍵數據；多組數據可整理成 Markdown 表格。
5. 限制與未來方向：作者自己承認的侷限。

**開源專案（GitHub）**
這不是論文，禁用「研究設計／實驗／樣本數」等論文段落。聚焦：
1. 解決什麼問題、為誰而做。
2. 核心架構或設計理念（README 有提到的）。
3. 怎麼用：安裝、最小可行範例、整合方式（僅在素材提供時）。
4. 適用場景與限制，以及與同類工具的差異（僅在素材提供時）。

**產業新聞／部落格報導**
聚焦：發生什麼事、為何重要、對工程師的實際影響。避免杜撰報導未提及的數據。

## 第二步：文章結構

**子標題寫成「該段的重點摘要」，不要用制式標籤。**
例如不要寫「核心發現」，而寫「用 AI 的那組，測驗分數低了 17%」。

📌 **標題**：8-15 字精準描述核心貢獻，可用提問式／數據式／對比式。避免「革命性」「顛覆」「史上最強」等誇大詞。若來自頂尖機構（Google DeepMind、OpenAI、Anthropic、Meta AI、NVIDIA、DeepSeek 等），在標題或開頭標註。

**TL;DR**：標題之後、正文之前一行，一句話講清「這是什麼 + 對工程師為何重要」（≤ 40 字）。

🎣 **開場鉤子**：前 2-3 行用認知衝突、反直覺數據或懸念抓住讀者，避免平鋪直敘。

（中段）依第一步選定的類型骨架展開，每段配一個分段 emoji + 重點式子標題。

🎯 **實務啟示**：從工程實踐角度，這對讀者有什麼可行動的價值。

🔗 **來源**（固定格式，逐項條列）
- 標題：<原文標題>
- 作者／機構：<僅在素材有提供時填，否則整行省略>
- 連結：<只用我提供的那一個 URL，不要自行補充其他連結>

（結尾）提供 10 個最能代表核心技術與主題的英文 hashtags。

## 分段 emoji（固定白名單，勿自行替換或新增）
📌 標題 / 🎣 開場 / 🤔 背景或問題 / 🧩 方法或架構 / 📊 數據或結果 / 💡 深入分析 / ⚠️ 限制 / 🎯 實務啟示 / 🔗 來源

## 繁體中文在地化（重要）
- 全文使用台灣慣用技術術語：專案（非項目）、演算法（非算法）、記憶體（非內存）、效能（非性能）、映像檔（非鏡像）、影片（非視頻）、函式（非函數）、預設（非默認）、最佳化（非優化）、程式碼（非代碼）、伺服器（非服務器）。
- 嚴禁簡體字與大陸用語，即使來源是簡體中文也要在地化改寫。
- 技術專有名詞首次出現保留英文原文（如 attention、fine-tuning、RAG），可加簡短中文註解；通用縮寫（API、LLM、GPU）直接用英文。

## 輸出規則（務必遵守）
- 直接從 📌 標題開始輸出，**不要寫任何前言、分類說明或「這是一篇…」開場白**。
- **絕對禁止 LaTeX／數學語法**。站台不會渲染，會直接顯示原始字串。流程箭頭一律用「→」這個字元。
  - 錯誤：`Base $\\rightarrow$ SFT $\\rightarrow$ GRPO`、`$d=0.738$`、`\\frac{a}{b}`
  - 正確：`Base → SFT → GRPO`、`d=0.738`、`a/b`
- 不要使用 Mermaid 或其他圖表語法（站台不會渲染）；流程改用文字 Step-by-Step 條列。
- 破折號（——）整篇最多 2-3 個，優先用逗號、句號、分號組織句子。

## 語調
專業但易讀的書面語，像資深工程師在技術分享會的講解：有深度、有觀點、聽得懂。避免過度口語（「超猛」「太扯」）與行銷腔。允許帶有依據的專業判斷（評論優缺點、實務前景），但不能憑空批評或脫離素材臆測。

## 格式範本（示範格式，實際請依內容類型調整中段段落）

```
📌 【Anthropic 最新研究】用 AI 寫 Code 更快，但你的技術真的有進步嗎？

TL;DR：RCT 顯示用 AI 輔助學習新函式庫，知識測驗分數比手動低 17%。

隨著 Cursor、GitHub Copilot 成為開發者標配，一個關鍵問題浮現：當 AI 幫你寫完大部分程式碼，你的技術是進步了，還是萎縮了？

🧪 **52 位工程師的隨機對照實驗**

招募 52 位軟體工程師學習新的 Python 函式庫 (Trio)，一組用 AI 助手、一組手動編程，完成後立即測驗。

📊 **用 AI 的那組，測驗分數低了 17%**

- AI 組平均：50%；手動組平均：67%（Cohen's d=0.738, p=0.01）
- 差距最大的是 Debugging 題型，代表「判斷程式碼哪裡錯」的能力發展受阻。

🎯 **刻意練習仍然重要**

與其說「幫我寫」，不如說「解釋這段為什麼這樣設計」——用 AI 建立理解，而非取代思考。

🔗 **來源**
- 標題：How AI Impacts Skill Formation
- 作者／機構：Judy Hanwen Shen & Alex Tamkin @ Anthropic
- 連結：arxiv.org/abs/2601.20245

#AI #Coding #MachineLearning #SoftwareEngineering #Anthropic #SkillFormation #DeveloperProductivity #LLM #AIAssistant #RCT
```

## 完稿前自我檢查
1. 是否有任何素材沒提到的數字、名稱、客戶被寫進去？有就刪掉。
2. 是否殘留簡體字或大陸用語？是否殘留 LaTeX／Mermaid 語法？
3. 子標題是否為重點摘要而非制式標籤？是否有 TL;DR？
4. 🔗 來源連結是否只用我提供的那一個 URL？
"""


def generate_blog_post(item: ScoredItem) -> GeneratedContent:
    """為單一高分 item 生成 Facebook 部落格貼文。"""
    config = load_config()
    llm_cfg = config["llm"]
    # generation_models 是降級 chain（複數）；保留對舊 generation_model / model 單數 key 的相容，
    # 但都用 .get()（非 eager index），避免清掉 legacy key 後 KeyError。
    model = (
        llm_cfg.get("generation_model")
        or (llm_cfg.get("generation_models") or [None])[0]
        or llm_cfg.get("model")
    )

    author_str = ", ".join(item.item.authors[:5])
    byline = " — ".join(p for p in (item.item.organization, author_str) if p) or "（素材未提供）"

    user_msg = f"""請根據以下資訊，撰寫一篇繁體中文技術部落格文章。這是目前可獲得的全部資訊（通常不是全文），請嚴格基於這些內容撰寫，不要臆測或捏造未提及的細節：

**標題**: {item.item.title}
**來源**: {item.item.source_name}
**機構/作者**: {byline}
**連結**: {item.item.url}
**摘要/內容**:
{item.item.abstract}

**內部選題角度（僅供你決定切入點，內容不一定正確，禁止當事實引用）**: {item.llm_reason}

請先判斷內容類型（論文／開源專案／新聞），再依撰寫規範產出完整文章。"""

    full_prompt = f"[SYSTEM]\n{BLOG_SYSTEM_PROMPT}\n\n[USER]\n{user_msg}"

    _logger.debug("LLM blog generation started", extra={"title": item.item.title[:80], "model": model})
    content = llm_chat(
        messages=[
            {"role": "system", "content": BLOG_SYSTEM_PROMPT},
            {"role": "user", "content": user_msg},
        ],
        model=model,
        temperature=0.7,
        is_generation=True,
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
    # 空文章 guard：rate-limit storm 時 llm_chat 會回 ""，若放行會寫出空文章並被
    # commit/ship。在此 raise，generate_and_save_posts 的 per-item try/except 會跳過該篇、
    # 不中斷整批。
    if not gen.content or not gen.content.strip():
        raise ValueError(f"refuse to write empty post: {gen.source_item.item.title[:60]}")

    date_str = target_date.isoformat() if target_date else today_str()
    slug = slugify(gen.source_item.item.title)
    filename = f"{date_str}_{slug}.md"

    # 儲存 blog post。frontmatter 用 yaml.safe_dump 序列化，避免標題含引號/冒號等
    # 特殊字元時手動 f-string 產生不合法的 YAML（曾導致下游 Astro build 失敗）。
    post_path = POSTS_DIR / filename
    frontmatter = {
        "title": gen.source_item.item.title,
        "source": gen.source_item.item.source_name,
        "url": gen.source_item.item.url,
        "score": round(gen.source_item.total_score),
        "model": gen.model_used,
        "generated_at": gen.generated_at.isoformat(),
    }
    fm_yaml = yaml.safe_dump(
        frontmatter, allow_unicode=True, sort_keys=False, default_flow_style=False
    ).strip()
    post_content = f"---\n{fm_yaml}\n---\n\n{gen.content}\n"
    post_path.write_text(post_content, encoding="utf-8")

    # 儲存 prompt (未來可重新呼叫)
    prompt_path = PROMPTS_DIR / f"{date_str}_{slug}_prompt.md"
    prompt_path.write_text(gen.prompt_used, encoding="utf-8")

    _logger.debug("Blog post file written", extra={"output_file": post_path.name})
    return str(post_path)


def generate_and_save_posts(items: list[ScoredItem], target_date: date | None = None) -> list[str]:
    """批量生成並儲存 blog posts。新 top-K 全部生成（覆寫同名舊文），不在 top-K 的舊文保留不動。"""
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
