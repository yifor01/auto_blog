---
title: 'Fastino Releases GLiNER2.5-Decide: A 340M Open-Weight Decision Model That
  Runs on CPU'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/24/fastino-releases-gliner2-5-decide-a-340m-open-weight-decision-model-that-runs-on-cpu/
model: claude-code/sonnet
generated_at: '2026-09-25T20:46:06.258252'
score: 96
---

📌 340M 決策模型上 CPU：GLiNER2.5-Decide 專打 agent 裡的判斷題

TL;DR：Fastino 推出 340M 參數、CPU 可跑的結構化決策模型，專治 agent pipeline 裡的路由與守門判斷。

Agent pipeline 裡最耗資源的往往不是「生成一段話」，而是無數個小小的判斷：這個工具該不該叫、這句話算不算 prompt injection、這張票該分派給哪個部門。Fastino 認為這類判斷根本不需要動用一個生成式大模型。

🤔 **給 agent 判斷題用的專用模型**

Fastino Labs 發布 GLiNER2.5-Decide，一個 340M 參數的開權重決策模型。它接收文字與一組帶型別的問題 schema，回傳結構化答案，每個答案都附帶機率分布、信心分數與約束可行性（constraint-feasibility）中繼資料。它鎖定 agent pipeline 裡常見的判斷場景：路由、分流（triage）、工具選擇與守門機制（guardrails）。權重以 Apache 2.0 授權釋出，透過 `pip install gliner2` 安裝，可在 CPU、GPU 或氣隙環境執行，Fastino 也提供託管推論與微調服務（GLiNER API）。

🧩 **不生成 token，兩階段輸出結構化答案**

GLiNER2.5-Decide 是非生成式分類器，基於 DeBERTa-v3-large 編碼器，從 gliner2-large-v1 微調而來，不產生任何生成 token，也不需要 prompt 模板。標籤集合在呼叫當下才傳入，每個問題會宣告允許的答案、以及要求單一答案、多重答案或有序值。Schema 還可以攜帶指示、範例、標籤描述，以及連結不同問題答案之間的規則。

整個管線分兩階段：編碼器同時讀入文字與 schema，為每個允許的答案評分；接著一個受約束的解碼器，在宣告規則允許的範圍內，搜尋分數最高的聯合指派結果。Fastino 明確劃清模型的能力邊界：它不推理、不解釋、也不回答開放式問題，就是一個專門處理操作性決策的專才模型。

守門場景的例子很說明問題：獨立解碼時，模型把某個 prompt 標記為 prompt injection，機率 0.82；同時卻又把同一個 prompt 標記為安全，機率 0.52,攻擊被偵測到了,但兩個輸出互相矛盾。聯合解碼套用一條規則,只要偵測到任何危害就必須判為不安全,模型於是同時回傳 `safety=unsafe` 與 `harm_type=prompt_injection`,下游程式碼可以直接拿這組分數做阻擋、路由或升級處理。Schema 也能表達蘊含關係、互斥關係、基數限制與有序邊界。同一個編碼器還能在一次前向傳遞中，同時做實體、關係與結構化記錄抽取，並附帶字元級偏移量,不過分類類答案本身不會回傳證據片段（evidence span）。

📊 **17 個資料集裡拿下 9 個，路由任務領先明顯**

Fastino 在自建的內部測試集 Fast Decisions 上評估模型，共 5,100 筆測試範例，橫跨 17 個資料集，涵蓋客服營運、領域路由（銀行、臨床、旅遊、福利）與一般內容理解，評估指標是完全匹配準確率（exact-match accuracy，答案集合須與參考答案完全一致才算對）。GLiNER2.5-Decide 在 17 個資料集中的 9 個領先，意圖路由是其最強項：support intent 得分 75.3%，banking intent 得分 64.3%，分別領先次佳模型 18.6 與 8.6 個百分點。在延遲測試中（batch 1，2-head、15-label schema），輸入長度 64 token 時各家 GPU 表現接近；到 1,024 token 時，A100 拉開差距達到 52.6 毫秒，V100 為 75.6 毫秒，L4 則是 131.4 毫秒。

Fastino 也同步釋出兩個變體：以 Ettin 1B 編碼器打造的 GLiNER2.5-Decide-1B，在同一測試集得分 59.6%（略低於 340M 版本）；以及針對多語言場景的 GLiNER2.5-multi-Decide（287M 參數），得分 56.7%。

🎯 **實務啟示**

微調可在本地完整訓練或用 LoRA 進行，透過 GLiNER2 trainer 完成；模型也附帶 SKILL.md 檔案，方便讓 coding agent 直接調用託管工作流程。對於已經在 agent pipeline 裡塞進一顆大模型只為了做路由判斷或安全過濾的團隊，這種 CPU 可跑、340M 參數量級的專用分類器,提供了一個成本更低、延遲更可控的替代方案,雖然它的架構本質上是 GLiNER 既有路線的延伸,而非全新設計。

🔗 **來源**
- 標題：Fastino Releases GLiNER2.5-Decide: A 340M Open-Weight Decision Model That Runs on CPU
- 作者／機構：Sana Hassan，MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/24/fastino-releases-gliner2-5-decide-a-340m-open-weight-decision-model-that-runs-on-cpu/

#GLiNER #OpenWeightAI #AgentPipeline #StructuredOutput #CPUInference #Guardrails #IntentRouting #SmallLanguageModel #ApacheLicense #AIEngineering
