---
title: 'SOP-Bench: A new benchmark for evaluating AI agents on real business procedures'
source: Amazon Science
url: https://www.amazon.science/blog/sop-bench-a-new-benchmark-for-evaluating-ai-agents-on-real-business-procedures
model: claude-code/sonnet
generated_at: '2026-08-22T06:12:56.087382'
score: 124
---

📌 SOP-Bench:AI 代理連公司內部流程都做不好?

TL;DR:Amazon 推出 SOP-Bench,用真實企業標準作業程序（SOP）與可執行工具評測 AI 代理，結果顯示升級模型未必更強。

想像一份病患報到流程,第四步和第六步都要求「驗證保險資料」,卻沒說怎麼驗證、為何要驗兩次。熟悉櫃檯作業的人一看就懂:第一次是跟保險公司核對承保狀態,第二次是確認資料有沒有正確輸入院所系統。但對一個 AI 代理來說，這裡沒有任何背景知識可以依靠,它必須自己猜測、記住前面做過什麼,還要在長得幾乎一樣的工具之間做選擇。

🤔 SOP 看起來乾淨,實際上充滿隱性知識

幾乎每個產業都靠 SOP 運作:醫院用它來報到病患、物流團隊用它判斷貨物是否屬於危險品、銀行用它驗證新企業客戶、信任與安全團隊用它決定是否下架內容。SOP 之所以難以被 AI 代理執行,是因為文字背後藏著從業人員共享的常識與判斷邏輯,而這些內容從未被完整寫下來。現有的 agent 基準測試通常只測單一能力（選對 API、遵守限制條件、規劃步驟序列),用的是乾淨、機器格式化的提示詞,少了真實流程裡的模糊性與變動性。過去也有團隊嘗試把書面流程轉成可執行的工作流,但範圍侷限在少數領域,資料集也常不公開;或是有人整理了真實業務流程的文字,卻停在文字層面,沒有配套工具與標準答案讓人真正跑一次代理並檢查結果。

🧩 把 SOP 變成可執行、可評分的任務

SOP-Bench 涵蓋 12 個業務領域,包括醫療報到、危險品分類、客服、內容審核、金融合規與倉儲檢查,總計超過 2,000 個任務。每個任務都配有代理需要呼叫的工具介面與正確答案,代理必須實際呼叫工具完成流程,結果會對照 ground truth 評分,而不是靠模型「覺得」答案好不好。每個流程只由四個部分組成:SOP 文字、代理可呼叫的工具、這些工具的規格,以及一組已知答案的測試案例。框架會執行每個任務、完整記錄工具呼叫與推理過程,並將結果對照已知答案評分,分數可重現,失敗也能追溯到具體步驟。

建構這個基準的方式是專家與 AI 協作:各領域專家撰寫原始流程並設定任務情境,再由 Anthropic 的 Claude 3.5 Sonnet v2 負責機械性的轉換工作,包括產生資料綱要、模擬 API 與工具規格、工具程式碼,以及刻意混合一般情境、邊緣案例與失敗案例的資料集。每一項產出都會回到專家手上確認邏輯是否成立、修正流程、檢查資料並實際執行程式碼驗證,整個過程沒有使用任何專屬或敏感資料。

📊 模型升級不一定更好,工具太多反而扣分

團隊用兩種刻意簡單的代理設計（function-calling 代理與推理型代理）在 11 個前沿模型上進行測試,這些代理是給其他人改進的基準線,而非最佳系統的宣稱。結果顯示,在推理型代理設定下,較新的 Claude 4.5 家族分數反而低於較舊的 Claude 4 家族,同樣的逆轉在個別模型比較中也成立。另一個實驗針對單一影片標註流程,分別給代理兩種工具組:一組只有任務所需的六個工具,另一組則在同樣六個工具外混入 20 個看似合理但沒用的工具。結果顯示,即使所需工具都在,較大工具組的成功率幾乎腰斬。

⚠️ 這只是基準線,不是最佳答案

團隊強調,論文中的兩種代理設計是刻意簡化的基準,目的是讓社群有東西可以改進,而非宣稱這是最好的代理系統。

🎯 對正在部署代理的團隊來說

常規的模型升級可能在沒有明顯訊號的情況下降低成功率,唯一可靠的辦法是拿團隊實際在用的流程去測試,而不是依賴榜單分數;同時,替代理裁剪工具集、只保留任務真正需要的工具,可能是讓系統上線前必須做的一步。

🔗 來源
- 標題：SOP-Bench: A new benchmark for evaluating AI agents on real business procedures
- 作者／機構：Amazon Science
- 連結：https://www.amazon.science/blog/sop-bench-a-new-benchmark-for-evaluating-ai-agents-on-real-business-procedures

#AIAgents #Benchmark #SOPBench #AmazonScience #KDD2026 #AgenticAI #EnterpriseAI #LLMEvaluation #ToolUse #AIReliability
