---
title: Can an Open Model Do Security Research? Cantina’s apex-flash-1 Solves 40 of
  60 Held-Out Bug Tasks
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/04/can-an-open-model-do-security-research-cantinas-apex-flash-1-solves-40-of-60-held-out-bug-tasks/
model: claude-code/sonnet
generated_at: '2026-10-05T23:22:10.083862'
score: 93
---

📌 開源安全模型對決 Opus：成本僅 1/31,漏洞任務解 40/60

TL;DR：Cantina 開源 apex-flash-1,專攻漏洞研究,成本效益數據直接攤在你面前。

當大家還在爭論「要不要讓 LLM 碰生產環境的程式碼審查」時,Cantina Security 已經直接把一個專門找漏洞的模型放上 Hugging Face,還附上跟 Claude Opus 的正面對決成績單。

🤔 **防禦方也需要能本機掌控的模型**

Cantina Security 與 Yeta Labs 合作發布 apex-flash-1,一個專為漏洞研究訓練的開放權重模型,以 MIT 授權釋出。Cantina 的立場很直接:防禦方需要能在自己環境中執行、控管的強力模型,而不是只能透過 API 呼叫外部黑盒。

🧩 **GLM-5.3-Flash 底座,GRPO 強化學習微調**

apex-flash-1 是以 Z.ai 的 GLM-5.3-Flash 為底座,透過強化學習微調而成。根據 Hugging Face 的 safetensors metadata,模型總參數量為 321.3B,底座 GLM-5.3-Flash 本身是 Mixture-of-Experts 架構,啟用參數為 18B。Cantina 使用 GRPO 搭配 rank-256 的 LoRA,再加上選擇性的全參數訓練。

訓練資料來自 50 個真實漏洞案例,衍生出 150 個任務,每個案例各有三種變體:guided whitebox、focused whitebox、focused blackbox。案例類型分布上,授權、身分驗證與範圍（scope）相關的漏洞佔 72%,帳務與數值精度類漏洞佔 18%,其餘則是時間驗證、業務邏輯與 SSRF。依模型卡說明,RL rollout 是在 Codex agent harness 中、對接近生產環境的軟體與協定環境下進行的。

📊 **40/60 任務,成本只要 Opus 的 1/31**

Cantina 用 20 個held-out漏洞案例、共 60 個任務進行評測,每個模型各跑一次,成本依各家供應商定價估算。結果 apex-flash-1 解出 40 個任務,Opus 多解出 3 個,但每次執行成本高出約 31 倍——換算下來,apex-flash-1 每解決一個任務約 0.06 美元,Opus 則約 1.74 美元。需要強調的是,這些是 Cantina 自行在內部 benchmark 上公布的數字。

💡 **模型的定位:被更大模型指揮的「工人」**

Cantina 把 apex-flash-1 定位為由更大模型orchestrate的worker,模型卡列出的目標技能包括程式碼閱讀、工具使用、漏洞利用開發與驗證。另外還有一個實驗性的 apex-flash-1-abliterated 變體,修改了拒絕回應的行為,但這個版本並未單獨評測。

⚠️ **權重好拿,但硬體門檻不低**

MIT 授權的權重可在 vLLM、SGLang 或 Transformers 上部署,但 BF16 精度大約需要 640GB GPU 記憶體,這對多數團隊而言仍是不小的基礎設施投入。此外,所有效能與成本比較都是 Cantina 單方面在內部評測集上得出,尚未見到第三方獨立複現。

🎯 **實務啟示**

如果你的團隊在做內部紅隊或漏洞研究自動化,apex-flash-1 的成本結構值得關注:用小模型搭配更大模型做 orchestration,可能比全程呼叫頂級閉源模型更划算。但部署前務必評估 640GB 記憶體需求是否合乎團隊現有硬體,以及這份 40/60 的成績單是否能在你自己的漏洞類型上重現。

🔗 **來源**
- 標題：Can an Open Model Do Security Research? Cantina's apex-flash-1 Solves 40 of 60 Held-Out Bug Tasks
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/04/can-an-open-model-do-security-research-cantinas-apex-flash-1-solves-40-of-60-held-out-bug-tasks/

#SecurityResearch #OpenWeights #LLM #VulnerabilityResearch #ReinforcementLearning #GRPO #MixtureOfExperts #AIforSecurity #HuggingFace #CyberSecurity
