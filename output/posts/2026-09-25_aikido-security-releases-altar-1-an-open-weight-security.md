---
title: 'Aikido Security Releases Altar-1: An Open-Weight Security Model Pruned From
  GLM-5.3 to 328 GB'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/25/aikido-security-releases-altar-1-an-open-weight-security-model-pruned-from-glm-5-3-to-328-gb/
model: claude-code/sonnet
generated_at: '2026-09-25T20:46:06.258155'
score: 96
---

📌 Altar-1：把 753B 資安模型塞進客戶自己的機房

TL;DR：Aikido 剪枝 GLM-5.3 到 328GB 開權重資安模型，讓滲透測試不再需要把原始碼送出網外。

當你的滲透測試工具本身就要求你把原始碼、架構文件和尚未修復的漏洞細節傳給雲端 API,這個工具的存在意義就先打了折扣。Aikido Security 這次直接把問題砍在源頭。

🤔 **封閉模型解決不了資料落地問題**

Aikido Security 發布首個開權重（open-weight）資安模型 Altar-1，它是 Z.AI GLM-5.3 的壓縮版本，用來驅動 Aikido Machine,一套為地端與air-gapped（實體隔離）網路設計的自主滲透測試設備。封閉的前沿模型跑在別人的基礎設施上，使用它就等於把原始碼、架構文件與尚未修復的發現送出網路邊界。Aikido 舉出受資料落地（data-residency）規範約束的銀行、以及沒有網路連線的 OT（作業技術）業者作為典型場景。開權重模型能解決落地問題,卻帶來新的部署缺口:MoE（Mixture-of-Experts）模型即使每次只用少數專家,仍必須把所有專家都存進記憶體;而資安 agent 又會建立長時間執行的上下文,KV cache 會跟模型權重搶同一塊 GPU 記憶體。

🧩 **依領域重要性剪枝專家，路由邏輯不動**

GLM-5.3 是一個 753B 參數的 MoE 模型,每個 token 在每層從 256 個專家中路由至 8 個,實際活躍參數約 40B。Aikido 執行了兩道壓縮步驟:第一步用 Aikido 滲透測試框架的實際軌跡，加上程式碼、工具呼叫、推理與多語言 Wikipedia 文字做校準（calibration），官方聲明未使用任何客戶資料。第二步為每個專家依「該專家在單一領域被路由任務中所佔的最大份額」評分，藉此保留負責程式碼、稀有語言與結構化輸出的專家不被砍掉。路由機制本身沒有改變，仍是每個 token 選 8 個專家，只是候選池從 256 縮減到 168 個，活躍參數維持約 40B。最終 Altar-1 比 BF16 原版小 78.2%，比 AWQ 版本再小 32.8%。在保真度上，於一組 25 道題的封閉測試集上，Altar-1 對完整 BF16 的 KL 散度為 0.506 nats,同一剪枝結果的 EXL3 版本則是 0.511。

📊 **CVE 重現測試：召回率略降，覆蓋率幾乎不變**

Aikido 團隊在內部 CVE 基準上測試 Altar-1，涵蓋 30 個程式庫中的 32 個已知漏洞，每案跑 3 次。相較 AWQ 版本，剪枝大約損失 1 個百分點的召回率，覆蓋率沒有損失；相較未壓縮的原始模型，Altar-1 在 25 個可覆蓋的漏洞中保住 23 個（92%），召回率則低了 5.2 個百分點。這個基準範圍其實不大,它只衡量在一個混用其他模型負責周邊階段的 pipeline 中,對已知 CVE 的目標式重現能力,並不測試盲目探索發現、漏洞利用驗證或修復建議產出。Aikido 另外提到 Altar-1 在一次客戶正式滲透測試中找到一個有效的重大（critical）等級漏洞,但這是廠商自行回報的單一案例。

⚠️ **硬體與授權限制**

模型卡要求 Hopper 架構 GPU（H100 或 H200）。Aikido 表示在 4x H200 上的 328GB 空間，能在生產環境批次量下留出 128k context 的 KV cache 空間；vLLM 會自動選用 Marlin MoE kernel。值得注意的是，4x H100 80GB 節點只有 320GB 記憶體，小於 328GB 的模型權重，也就是放不下。授權上，Altar-1 沿用 GLM-5.3 授權，允許商業使用、修改與再散布，但年營收超過 100 億美元的 Model-as-a-Service 業者，必須先通過 Z.AI 的安全審查；Altar-1 屬於開權重，並非 OSI 認證的開源軟體。

🎯 **實務啟示**

Altar-1 目前也驅動 Aikido Attack、AI Code Analysis 與 Deep Review 等產品，Aikido 團隊規劃下一步嘗試 EXL3 等更低位元格式以保留更多專家，並針對資安工作流程做微調。對於必須在氣隙網路或高度受管制環境中運行安全工具的團隊而言，這種「依領域感知做專家剪枝」的做法，提供了一條在單機 4 卡 GPU 上跑起 753B 級 MoE 模型的具體路徑，但目前驗證仍侷限在已知 CVE 的重現能力上，尚未證明對零時差或未知漏洞的發現力。

🔗 **來源**
- 標題：Aikido Security Releases Altar-1: An Open-Weight Security Model Pruned From GLM-5.3 to 328 GB
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/25/aikido-security-releases-altar-1-an-open-weight-security-model-pruned-from-glm-5-3-to-328-gb/

#OpenWeightAI #MoE #LLMPruning #AISecurity #Pentesting #GLM #vLLM #ModelCompression #CyberSecurity #AIInfra
