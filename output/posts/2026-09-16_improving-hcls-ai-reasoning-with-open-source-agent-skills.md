---
title: Improving HCLS AI reasoning with open-source agent skills
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/improving-hcls-ai-reasoning-with-open-source-agent-skills/
model: claude-code/sonnet
generated_at: '2026-09-16T20:15:39.941056'
score: 106
---

📌 AWS開源38個HCLS Agent Skills，補上AI「知道規則卻用錯」的缺口

TL;DR：38個開源skill讓agent正確套用醫療準則，頭對頭勝率達70-86%。

問AI用ACMG/AMP準則判讀TP53錯義突變，它能準確講出框架名稱，卻可能誤用證據分類、跳過族群頻率門檻，甚至捏造計算預測分數。模型記得知識，卻沒有領域專家內化多年的結構化推理程序，這個落差正悄悄滲透進變異判讀、理賠核定、臨床試驗設計與影像分析等工作流程，輸出看起來對，套用的準則卻是錯的。

🤔 **AI「知道規則」不代表「會用規則」**

AWS 團隊觀察到，foundation model 即使在訓練資料與 system prompt 中都看過完整的醫療照護與生命科學（HCLS）決策框架，實際執行時仍常誤用。這種靜默失敗（silent failure）在監理與病患安全層面風險極高，因為輸出格式正確、邏輯卻站不住腳，不容易被察覺。

🧩 **SKILL.md：把決策程序寫成可被 agent 消費的結構化文件**

這套 HCLS Agent Skills 集合涵蓋 11 個領域、38 個 skill，每個 skill 是一份 markdown 文件（SKILL.md），在 YAML frontmatter 宣告觸發條件、依賴與 metadata，內文則放決策框架、參數表、程式碼樣板與驗證準則，透過 progressive disclosure 在推論時被 agent 讀取。

Skill 分成兩類：reasoning skill 編碼「如何思考」的方法論，例如 genomic-variant-interpretation 完整封裝 ACMG/AMP 分類框架（證據分類、族群頻率門檻、計算預測分數切點）；pipeline skill 則提供工具層級的指令與驗證過的參數，例如 variant-calling skill 給出 GATK4 HaplotypeCaller 的正確 annotation groups、VQSR tranche sensitivity 目標，以及 Mutect2 的 tumor-normal 設定。

作者強調 skill 不同於 RAG，也不是 fine-tuning：它不是檢索片段來輔助生成，而是直接編碼決策程序本身；也不需要重新訓練模型，只是依觸發模式在對話中被動啟用的結構化 prompt。這讓它具備三個特性：可稽核（每條判斷準則都是人類可讀的 markdown，而非藏在權重裡）、可攜（同一份 skill 可跨 Amazon Bedrock AgentCore、Strands Agents SDK、Kiro、Amazon Quick Desktop、Claude Code、OpenAI Codex 等 20 多種服務使用而無需客製）、易維護（政策年度更新只需改文字檔，不必重訓模型）。全部以 MIT-0 授權釋出。

📊 **加了 skill 之後，頭對頭勝率 70-86%**

評測顯示，裝了 skill 的 agent 在頭對頭比較中，對上沒有 skill 的相同 agent，勝率落在 70-86%（依 agent harness 設定而異）。效果最明顯的是批判性思考（critical thinking）能力，勝率達 78-85%，效果量 d 介於 0.65-1.03。

同時全部載入 38 個 skill 會消耗約 8 萬 tokens，這在長 context 模型上可行，但會帶來 context engineering 的挑戰：agent 每次查詢都要從 38 個 skill 中挑對子集，不相關的 skill 內容也會分散注意力。Kiro CLI 的解法是多 agent 架構：一個不掛載任何 skill 的輕量協調者負責意圖分類，再路由給 8 個領域專家 agent，每個專家只載入自己相關的 skill（約 1.5 萬 tokens），把路由與領域推理拆開處理。

💡 **從單一 agent 到多 agent 協調的部署路徑**

文章展示三種部署模式：Amazon Quick Desktop 的單 agent 模式最簡單，查詢會依觸發模式自動啟用相關 skill（例如問 RAF 編碼影響會自動觸發 risk-adjustment skill 並給出具體 HCC 對應與量化 RAF 差值）；Kiro CLI 的多 agent 模式解決 context competition 問題；Strands SDK 搭配 Amazon Bedrock AgentCore 則適合正式環境部署，提供托管、自動擴展、安全邊界與可觀測性。

🎯 **實務啟示**

對於在受監理領域（醫療、保險理賠、臨床試驗）建構 agent 的工程師，這提供了一個介於「純 prompt」與「fine-tuning」之間的中間選項：把領域專家的決策程序顯式寫成可稽核的 markdown，既能快速隨政策更新迭代，也能誠實地把「模型是否真的照著正確邏輯做決策」變成可測試、可比較的問題，而不是憑輸出看起來合理就信任它。

🔗 **來源**
- 標題：Improving HCLS AI reasoning with open-source agent skills
- 作者／機構：Michael Hsieh, AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/improving-hcls-ai-reasoning-with-open-source-agent-skills/

#AgenticAI #HealthcareAI #LLM #AWS #Bedrock #AgentSkills #ClinicalAI #Genomics #PromptEngineering #AIagents
