---
title: Google Releases Gemini 4 Argon API With 1M Token Output Limit
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/13/google-gemini-4-argon-api-release/
model: claude-code/sonnet
generated_at: '2026-10-14T20:53:05.951997'
score: 103
---

📌 【Google DeepMind】Gemini 4 Argon GA,單次輸出衝到 100 萬 token

TL;DR:Google 旗艦模型 Argon 正式開放 API,一次回應最高可寫 1M tokens,主打長流程 agent 任務。

多數 LLM 的單次輸出被鎖在幾萬 tokens 的量級,逼著開發者把長任務拆成一輪又一輪的呼叫。Google DeepMind 剛把這道牆往上推了超過 15 倍——Gemini 4 Argon 現在一次回應最多可以寫到 1M tokens。

🤔 **從小範圍測試到全面開放**

Gemini 4 Argon 是 Google 打造的 sparse mixture-of-experts 前沿模型,專為長、多步驟的工作設計,目標領域包括程式開發、金融、法律、科學與網路安全。它最早在 9 月 30 日對外公告,僅開放給一小群網路安全防禦人員使用;現在則全面進入付費 Gemini API,面向開發者、企業與付費 Gemini 訂閱戶。對開發者而言,最大的變化就是輸出長度:Argon 支援的最大輸出從早期 Gemini 模型的 64K tokens,一口氣拉高到 1M tokens。

🧩 **新模型,不是微調版**

根據官方 model card,Argon 是全新訓練的模型,並非既有 Gemini 的 fine-tune。它是大規模 sparse MoE transformer,具備原生多模態支援:輸入可接受文字、圖片、音訊與影片,輸出則為文字。Google 使用 TPU、搭配 JAX 與 ML Pathways 框架訓練,知識截止日期為 2026 年 3 月。官方並未公開總參數量或啟動參數量。

需要注意的是,model card 說明輸入加輸出的合併視窗上限為 1M tokens——也就是說,提示詞越長,留給輸出的空間就越少。針對長時間解碼,Google 在開發者文件與企業文件中也說明了一套新的「continuation protocol」。以導入期定價計算,一次寫滿 1M tokens 的輸出,光是輸出端就要花費 10 美元。

📊 **多數指標領先,但評測方法值得留意**

Google 將 Argon 與 GPT-6 Astra、Claude Fable 5.1、Claude Opus 5.5 做比較,在其公開的對照表中,Argon 在多數項目上取得最高分,另外在 ERQA 具身推理(embodied reasoning)benchmark 上拿下 87%。不過官方自己也提醒,應該先閱讀其評測方法說明再下結論:多數對手模型的分數是自報(self-reported)或取自公開排行榜,例如 Argon 的 DeepSWE 分數是用 mini-swe-agent harness 自行計算,而對手的 DeepSWE 數字則來自各家的 system card 與排行榜,評測條件並不完全一致。Google 也承認,在其自家對照表中,Argon 在 5 個項目上落後對手。

⚠️ **已知限制與安全框架**

Model card 列出的限制包括幻覺(hallucination)與偶發的回應變慢或逾時。在 Google 的 Frontier Safety Framework 下,官方表示無法排除 Argon 已觸及生物與網路安全相關的「critical capability」等級,但已部署其評估後認為能降低該風險的防護措施。

💡 **定價:比 GPT-6 Astra 便宜,打平 Claude Opus 5.5**

導入期定價為每百萬 tokens 輸入 2 美元、輸出 10 美元,快取輸入享 95% 折扣。2026 年 11 月 30 日後,價格將調整為每百萬 tokens 輸入 4 美元、輸出 20 美元。這個價位與 Claude Opus 5.5 相同,低於 GPT-6 Astra 的每百萬 tokens 輸入 10 美元、輸出 50 美元。

🎯 **實務啟示**

如果你的應用屬於「一次性產出長文件」型態——例如完整的程式碼庫重構、長篇法律或科學文件生成——1M tokens 的單次輸出能大幅減少多輪呼叫與拼接的工程負擔。但在評估 Argon 是否優於現有方案前,務必對照 Google 自己提供的評測方法說明,因為跨模型比較的分數來源並不一致,直接拿排行榜數字做決策容易失真。

🔗 **來源**
- 標題:Google Releases Gemini 4 Argon API With 1M Token Output Limit
- 作者/機構:Asif Razzaq, MarkTechPost
- 連結:https://www.marktechpost.com/2026/10/13/google-gemini-4-argon-api-release/

#GoogleDeepMind #Gemini #LLM #MoE #AIAgents #FrontierModel #AIAPI #LongContext #AISafety #GenerativeAI
