---
title: Run NVIDIA BioNeMo NIM Microservices for Protein Structure Prediction in Claude
  Science
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/run-nvidia-bionemo-nim-microservices-for-protein-structure-prediction-in-claude-science/
model: claude-code/sonnet
generated_at: '2026-09-01T10:47:43.551624'
score: 92
---

📌 【NVIDIA × Anthropic】讓 Claude 學會呼叫蛋白質摺疊模型

TL;DR：NVIDIA BioNeMo Agent Toolkit 整合進 Claude Science，讓 agent 直接呼叫蛋白質結構預測 NIM。

一個通用型 AI agent 或許能看出某項任務需要摺疊蛋白質或做分子對接，但它未必知道該跑哪個模型、如何格式化請求、哪些參數才重要。

🤔 **科學研究比寫程式更難自動化**

Agentic AI 正在改變研究方式：AI 科學家能讀論文、提出假設、呼叫模型、判斷下一步該優先做哪個實驗。程式碼撰寫 agent 已經先在軟體工程領域證明了價值，但科學研究往往更迭代、更需要領域專用工具，不同套件之間的環境需求或 API 也可能天差地遠，橫跨這些工具的協調並不容易。

🧩 **BioNeMo Agent Toolkit 把工具打包成 agent 可呼叫的技能**

NVIDIA BioNeMo Agent Toolkit 將十多年來累積的 BioNeMo 生命科學模型、函式庫與工作流程，包裝成可供 agent 呼叫的技能，涵蓋生物學、化學、基因體學與藥物發現，並可搭配任何 agent 框架運作。文章指出，在 NVIDIA 內部基準測試中，BioNeMo 技能將任務正確率從 60% 提升到 100%，token 使用效率也大約提高一倍。NVIDIA 與 Anthropic 合作，把這套工具包整合進 Claude Science（Anthropic 的科學研究 AI workbench），讓 agent 能直接發現、啟動並呼叫 BioNeMo NIM 微服務。

🧩 **跑起來需要什麼：GPU 與約 700GB 儲存空間**

這個教學以搭載 NVIDIA L40S 或 H100 GPU 的機器執行 Claude Science，需要約 700GB 儲存空間：msa-search NIM 使用的 UniRef30 資料庫約 490GB（採 UniRef30-only 設定，而非完整的 1.4TB），Boltz-2 與 OpenFold3 容器則共佔 30–40GB。設定流程是在 Claude Science 中選擇 Customize > Compute > NVIDIA BioNeMo NIM > Connect，匯入 GitHub 上的 BioNeMo Agent Toolkit 技能、加入 NVIDIA API key，並連接使用本機 GPU 的 Docker 容器端點。

🧩 **三階段工作流程：從序列比對到雙鏈結構預測**

文章以 Paracoccidioides lutzii（一種造成副球孢子菌病的真菌）的核孔蛋白 Seh1（C1GY11）與一個推測的 Mio 家族夥伴蛋白（C1HCX1）為例，示範完整流程：

1. 用 GPU 加速的 MSA Search NIM，分別為單鏈序列與物種配對序列產生多序列比對（MSA）。
2. 用 OpenFold3 NIM 分別預測單鏈與雙鏈複合體結構。
3. 用 Boltz-2 NIM 重複同樣的預測，並分別評估兩個模型的結果。

在這次執行中，agent 從 UniProt 抓取序列後，MSA 搜尋為兩個蛋白質各回傳 202 條相關序列，Seh1 長度為 384 個殘基，C1HCX1 為 976 個殘基。研究問題聚焦在：Seh1 單獨建模與搭配推測夥伴一起建模時，預測出的結構有何差異。文中特別強調 prompt 設計上的嚴謹要求，例如若無法產生配對比對，agent 應停下並回報，而不是悄悄改用其他類型的比對頂替。

⚠️ **信心分數不等於證明**

文章提醒，OpenFold3 與 Boltz-2 回傳的信心分數只反映模型的信心程度，不能拿來證明兩個蛋白質確實會交互作用。這套流程也需要不小的 GPU 與儲存資源門檻，並非隨手可跑。

🎯 **實務啟示**

比起追求全新的模型架構，這次整合的價值更在於「協調層」：把領域專用工具封裝成 agent 可直接呼叫的技能，讓通用 agent 不必自己摸索該用哪個模型、怎麼組請求參數。對於需要串接多個科學計算工具的研究團隊，這種技能封裝的思路值得參考。

🔗 **來源**
- 標題：Run NVIDIA BioNeMo NIM Microservices for Protein Structure Prediction in Claude Science
- 作者／機構：Michelle Horton, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/run-nvidia-bionemo-nim-microservices-for-protein-structure-prediction-in-claude-science/

#NVIDIA #BioNeMo #Anthropic #ClaudeScience #AgenticAI #ProteinFolding #OpenFold3 #Boltz2 #NIM #DrugDiscovery
