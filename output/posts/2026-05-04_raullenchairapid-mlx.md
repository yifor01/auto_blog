---
title: "raullenchai/Rapid-MLX"
source: GitHub Trending
url: https://github.com/raullenchai/Rapid-MLX
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-04T20:29:54.193129
---

📌 你的 Mac 就能跑 158B MoE？Rapid-MLX 讓本地 AI 快到沒藉口

你以為在 Mac 上跑本地大模型一定得向速度妥協？這個新專案直接在 Apple Silicon 上跑出逼近雲端 API 的吞吐，同時還能完整支援工具呼叫與百萬級上下文，讓「離線也能當主力」不再是嘴炮。

🤔 **本地 AI 的速度與功能死角，正在被 Apple Silicon 填平**

過去要在 Mac 上跑大模型，選項常在「小模型才流暢」與「大模型卡到崩潰」之間擺盪；一旦牽涉到工具呼叫與長上下文，限制更明顯。Rapid-MLX 針對 Apple Silicon 的硬體特性重新梳理推理流程，並以 OpenAI 相容 API 包裝，讓現有生態（Cursor、Claude Code、PydanticAI、LangChain、Aider 等）幾乎不用改就能切換到本地端。

🧪 **pip install 後直接對話，無縫接 OpenAI 相容生態**

Rapid-MLX 並非全新架構，而是針對 MLX 與 Apple 晶片做深度整合：
- 4bit/8bit 量化選項，4bit 為記憶體友善預設，8bit 為品質優先選項  
- 支援工具呼叫（function calling），符合 Cursor、Claude Code 與編碼助理的期待行為  
- OpenAI API 相容層：只要改伺服器位址，現有應用即可連線  
- 無需雲端、無 API 成本，資料不離機

實測情境涵蓋從 16 GB MacBook Air 到 128+ GB Mac Studio Ultra 的多種規格，並引入常用指標：tok/s（約略等同於每秒生成詞數）、TTFT（首字延遲）、以及模型壓縮級別。

⚡ **在 Mac Studio Ultra 上，158B MoE 也能跑到 31–56 tok/s**

- 16 GB MacBook Air（Qwen3.5-4B 4bit）：160 tok/s，順暢支援對話、編碼與工具呼叫  
- 32+ GB Mac Mini / Studio（Nemotron-Nano 30B）：141 tok/s，30B 級別中目前最快，工具呼叫穩定  
- 32+ GB Mac Mini / Studio（Qwen3.6-35B）：95 tok/s，256 位專家、262K 上下文  
- 64 GB Mac Mini / Studio（Qwen3.5-35B）：83 tok/s，被評為「聰明與速度的最佳平衡」  
- 96+ GB Mac Studio / Pro（Qwen3.5-122B）：57 tok/s，前沿級別智能  
- 128+ GB Mac Studio Ultra（DeepSeek V4 Flash 158B-A13B）：31–56 tok/s，Day-0 前沿 MoE、1M 上下文支援

同一規格下，Rapid-MLX 相較 Ollama / llama.cpp 在 Apple Silicon 上可達 2–4 倍吞吐提升，並完整保留工具呼叫能力。

💡 **不是盲目拉大模型，而是用對量化與硬體特性**

這些數字背後的重點並非「越大越好」，而是：
- 4bit 量化大幅降低記憶體壓力，讓 30B–158B MoE 在消費級記憶體配置下仍具可行性  
- MoE 模型在推理時只激活部分專家，使高參數與高吞吐得以兼顧  
- 工具呼叫的穩定性讓本地端真正能嵌入工程流程，而非只能做單向生成  
- OpenAI 相容 API 降低切換成本，使本機伺服器成為可替換的後端

⚠️ **硬體門檻依舊存在，長時間穩定性與功耗未公開**

- 低記憶體機型（如 16 GB）仍侷限於 4B–8B 級別模型  
- 158B MoE 的可用吞吐依賴 128+ GB 記憶體，非人人可及  
- 論文或報告未提及長期執行的穩定性、記憶體碎片與熱管理影響  
- 目前以吞吐量與功能支援為優先，尚未公開跨任務泛化與一致性測試

🎯 **把本地伺服器當開發環境的一環，而非玩具**

- 對 macOS 工程師：Cursor / Claude Code 可透過換址直接使用本機模型，降低雲端依賴與成本  
- 對隱私與離線需求：敏感資料不需離機，仍能保有工具呼叫與長上下文  
- 對研究者與實驗者：快速在本機迭代提示、評估不同量化與模型規格的 trade-off  
- 啟動成本低：pip install → serve → 改設定即可跑現有生態

🔗 **專案連結**
📦 Rapid-MLX  
👤 raullenchai  
🔗 https://github.com/raullenchai/Rapid-MLX

你會考慮把部分開發與測試流程切到本機 AI 伺服器嗎？或者你更在乎雲端大模型的「一致性」與「規模上限」？歡迎在留言分享你的實戰經驗 👇

#AppleSilicon #LocalAI #MLX #RapidMLX #LLM #MacAI #OpenAICompatible #ToolCalling
