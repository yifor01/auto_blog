---
title: 'Alibaba Qwen Releases Qwen3.8-Omni-Flash: A 1M-Context Omni-Modal Model Built
  Around Agentic Audio-Video Understanding and Tool Use'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/18/alibaba-qwen-releases-qwen3-8-omni-flash/
model: claude-code/sonnet
generated_at: '2026-09-18T19:49:34.902620'
score: 96
---

📌 Qwen3.8-Omni-Flash：百萬 context 全模態模型的 agentic 賭注

TL;DR：阿里 Qwen 推出首個強調 agentic 能力的全模態模型，僅開放 API，不開權重。

多數影片模型的做法是把整段影片從頭看到尾，即使答案只藏在 3 分鐘的片段裡，也照樣把全部 token 吃下去。Qwen 團隊這次選擇了不同的路：讓模型先想清楚問題,再決定該看哪裡、聽哪裡。

🤔 **從「全部看完」到「先問問題再找證據」**

Qwen3.8-Omni-Flash 是 Qwen 團隊發布的首個「built around agentic capabilities」的全模態模型，可接受文字、圖片、音訊、影片輸入，輸出則僅限文字。官方描述的工作流程是：理解內容 → 規劃任務 → 用工具執行 → 交付結果。針對長影片，模型會以問題為起點，決定要看什麼、聽什麼，再透過多輪由粗到細（coarse-to-fine）的方式蒐集證據，把運算資源和 token 集中花在真正相關的片段上。

🧩 **建構在 Qwen3.8-Flash-Next 之上，僅供 API 呼叫**

這個模型是以 2026 年 8 月開源的 Qwen3.8-Flash-Next 架構為基礎打造，但發布時並未釋出開放權重，目前只能透過 QwenCloud、Alibaba Cloud Model Studio、Qwen Studio 以 hosted API 形式使用，無法自架部署。

context window 為 1M tokens，QwenCloud 文件標示最大輸入 991K、最大輸出 131K，最大 reasoning 長度 262K tokens。thinking 預設開啟（reasoning_effort 設為 xhigh），設為 none 可關閉。若需要語音生成，Model Studio 文件會導向 Qwen3.5-Omni，因為這款模型只輸出文字。API 同時相容 DashScope 與 OpenAI 協定，支援 Chat Completions 與 Responses API，並具備 function calling、web search、structured outputs、context caching、batch calls。

📊 **官方數據：token 省下近半，準確率不降反升**

Qwen 團隊公布的 OmniVideoBench 結果如下（皆為官方數字，發文時尚無第三方驗證）：

| 指標 | 數值 |
|---|---|
| 準確率 | 63.4 → 67.8 |
| Token 用量 | 145,736 → 79,117（約減少 45.7%） |

Qwen 團隊另表示，其 audio-visual 表現接近 Gemini 3.8 Flash，整體 audio 表現則宣稱優於 Gemini 3.8 Flash；官方 X 貼文則將 agent 能力提升總結為在 WildClawBench-MM 與 UniClawBench 上平均 +19.5 分。

定價方面，QwenCloud 列出每 1M input tokens $0.15、每 1M output tokens $0.47，implicit cache 命中則為每 1M tokens $0.016。相較於 Qwen3.5-Omni-Plus，官方宣稱 audio 輸入成本每小時降低超過 98%，audio-visual 輸入降低超過 93%；X 貼文另提及影片輸入成本降低約 89%。

💡 **兩個開源專案補上「多模態原生」的最後一哩**

由於模型本身只回傳文字，多媒體相關操作需仰賴外部工具，Qwen 團隊同步開源了 Qwen-MM-Plugins（Apache-2.0 授權），標語是「Make any agent harness multimodal-native」。每項能力以 Skill 加上可選的 MCP server 形式安裝，並提供 guided installer，支援 Claude Code、CodeBuddy、Codex、Qoder、OpenClaw、Qwen Code、Gemini CLI 等多種 agent harness。其中一個核心 plugin 可讓主模型原生讀取本地圖片與影片幀。

⚠️ **仍有明顯限制**

README 也坦承現況的一個缺口：目前多數 agent harness 還無法讓主模型原生接收音訊，音訊處理暫時仍得透過 API 轉送。此外，模型未開放權重意味著無法自架，且輸出僅限文字，語音生成需另外導向 Qwen3.5-Omni。

🎯 **對工程師的意義**

如果你的應用需要處理長影片或音訊並串接工具鏈，Qwen3.8-Omni-Flash 的 coarse-to-fine 檢索策略與大幅降低的 token 成本值得評估；但若你的專案要求自架部署或資料不出雲端，目前這條路是走不通的，只能等待未來是否釋出開放權重版本。

🔗 **來源**
- 標題：Alibaba Qwen Releases Qwen3.8-Omni-Flash: A 1M-Context Omni-Modal Model Built Around Agentic Audio-Video Understanding and Tool Use
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/18/alibaba-qwen-releases-qwen3-8-omni-flash/

#Qwen #Alibaba #OmniModal #LLM #AIAgents #MultimodalAI #VideoUnderstanding #APIModel #AIInfrastructure #ToolUse
