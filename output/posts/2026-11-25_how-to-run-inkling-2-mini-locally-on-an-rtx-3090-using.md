---
title: How to Run Inkling 2 Mini Locally on an RTX 3090 Using Unsloth Studio
source: KDnuggets
url: https://www.kdnuggets.com/how-to-run-inkling-2-mini-locally-on-an-rtx-3090-using-unsloth-studio
model: claude-code/sonnet
generated_at: '2026-11-25T01:47:54.358725'
score: 81
---

📌 Thinking Machines Lab 開源 Inkling 2 Mini，單張 RTX 3090 跑贏雲端 API

TL;DR：26B MoE 模型配 looping 機制，4-bit 量化後單卡 24GB 顯卡即可本地推論並接上 coding agent。

一張消費級顯卡,不靠任何付費 API,就能跑出媲美 Qwen3.8-27B 的模型,還能接上 coding agent 寫出完整的小遊戲。這正是 Thinking Machines Lab 最新釋出的 Inkling 2 Mini 想證明的事。

🤔 **美國開源陣營終於有像樣的對手**

根據 KDnuggets 報導，Inkling 2 Mini 在 Artificial Analysis Intelligence Index 上追平 Qwen3.8-27B，並在部分 coding、agentic、tool-use 的 benchmark 上表現更好。作者 Abid Ali Awan 將其視為美國開源 AI 一次重要的回歸。

🧩 **26B 參數、Mixture-of-Experts 加上 looping 機制**

模型雖有 26 億參數，但透過 Mixture-of-Experts 架構與「innovative looping mechanism」，不需要昂貴的企業級硬體就能達到不錯的效果，推論速度也快，還可以透過 speculative decoding 進一步加速。4-bit 量化版本（unsloth/Inkling-2-Mini-GGUF，UD-Q4_K_XL）可以完整塞進一張 RTX 3090 的 24GB VRAM。

🧩 **本地部署三步驟**

整套流程圍繞 Unsloth Studio：
- 執行 `curl -fsSL https://unsloth.ai/install.sh | sh` 安裝，並設定 `HF_HOME`、`HUGGINGFACE_HUB_CACHE` 等環境變數統一管理模型快取路徑。
- 以 `unsloth studio -H 127.0.0.1 -p 8080` 啟動本機 Web 介面，在瀏覽器下載並載入 Inkling 2 Mini 的 Q4_K_XL 量化版本。
- 若要接上終端機 coding agent Pi（`curl -fsSL https://pi.dev/install.sh | sh` 安裝），可用 Unsloth Studio 提供的指令，透過 API key 把本地模型接到 Pi，直接在終端機裡下指令開發。

📊 **實測：52 tokens/s、模擬股市儀表板、可玩的小遊戲**

作者先開啟 web search 功能問模型該不該買 NVIDIA 股票，模型主動搜尋多個來源給出詳細回答，平均速度約 52 tokens/s。接著在關閉工具的情況下，要求模型直接生成一個追蹤石油價格與指數的儀表板網站，結果做出了外觀與互動都接近真實市場儀表板的介面。最後透過 Pi coding agent，給它一個要求三線道移動、跳躍、滑行、障礙物、金幣、粒子特效等大量細節的 Subway Surfers 風格 2D 無盡跑酷遊戲提示，模型在幾分鐘內就生成了一個可以直接在瀏覽器玩的完整遊戲。

⚠️ **數字是模擬出來的**

文中特別提到，石油儀表板雖然看起來像即時更新的市場數據，但實際上市場已經休市，顯示的價格波動是模擬值而非真實行情，使用時需留意這點。

🎯 **對工程師的意義**

對想擺脫付費 API、又不想犧牲 coding agent 體驗的開發者來說，Inkling 2 Mini 加 Unsloth Studio 提供了一條門檻不高的本地化路線：一張二手 RTX 3090、一套開源工具鏈，就能同時跑通用對話、網頁生成與 agentic coding 任務。

🔗 **來源**
- 標題：How to Run Inkling 2 Mini Locally on an RTX 3090 Using Unsloth Studio
- 作者／機構：Abid Ali Awan，KDnuggets
- 連結：https://www.kdnuggets.com/how-to-run-inkling-2-mini-locally-on-an-rtx-3090-using-unsloth-studio

#Inkling2Mini #ThinkingMachinesLab #LocalLLM #UnslothStudio #MixtureOfExperts #RTX3090 #CodingAgent #OpenSourceAI #LLMInference #Quantization
