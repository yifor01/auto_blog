---
title: snap-stanford/Biomni
source: GitHub Trending
url: https://github.com/snap-stanford/Biomni
score: 106
model: tencent/hy3:free
generated_at: '2026-07-16T08:10:18.942702'
---

📌 【Stanford SNAP】Biomni：可自主執行生醫研究的通用 AI Agent

TL;DR：Stanford SNAP 開源 Biomni，結合 LLM 推理與程式執行，協助生醫研究自動化。

當多數 AI 代理還在 demonstration 階段，Stanford SNAP 直接把一個號稱能跨子領域自主跑研究的 biomedical agent 丟上 GitHub。

🤔 **生醫研究者的通用代理需求**

Biomni 是一個 general-purpose biomedical AI agent，目標是自主執行多樣化的生醫研究任務，橫跨不同生醫子領域。README 指出，它透過整合大型語言模型（LLM）推理、retrieval-augmented planning（檢索增強規劃）與 code-based execution（基於程式碼的執行），幫科學家顯著提升研究生產力，並產出可驗證的假說（testable hypotheses）。

🧩 **以 LLM 推理加上檢索與程式執行為核心設計**

專案架構理念上，Biomni 不是單純的問答系統，而是將三個能力串起來：用 LLM 做推理與決策、用檢索機製做規劃輔助、再透過實際執行程式碼來完成任務。這樣的組合讓它能從規劃一路走到可執行的研究步驟，而非只給文字建議。

🎯 **實務啟示**

對生醫領域的 ML 工程師或研究者來說，若手上有 Anthropic 或 OpenAI 的 API key，可直接評估這套 agent 能否接進現有實驗流程；它的設計明確走向「執行」而非「建議」，適合想減少重複性研究工時的團隊試用。

⚙️ **安裝與最小設定流程（依 README）**

- 專案環境相當龐大，官方提供單一 `setup.sh` 指令碼來建立環境，需先依該檔完成環境設定。
- 啟用環境 E1：`conda activate biomni_e1`
- 安裝官方 pip 套件：`pip install biomni --upgrade`
- 若要最新版本，可從 GitHub 源安裝：`pip install git+https://github.com/snap-stanford/Biomni.git@main`
- 設定 API key（推薦用 `.env` 檔）：
  - 複製範例：`cp .env.example .env`
  - 必填 `ANTHROPIC_API_KEY`（供 Claude 模型使用）
  - 選填 `OPENAI_API_KEY` 或 Azure OpenAI 相關設定（若使用 OpenAI 模型）

🔗 **來源**
- 標題：snap-stanford/Biomni
- 作者／機構：snap-stanford
- 連結：https://github.com/snap-stanford/Biomni

#Biomedical #AIAgent #LLM #RetrievalAugmented #Stanford #SNAP #ResearchAutomation #CodeExecution #Biomni #OpenSource
