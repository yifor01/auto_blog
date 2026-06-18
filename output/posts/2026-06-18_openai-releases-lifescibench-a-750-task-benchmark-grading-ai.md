---
title: OpenAI Releases LifeSciBench, a 750-Task Benchmark Grading AI Models on Real
  Life-Science Research With Expert-Written Rubric
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/17/openai-releases-lifescibench-a-750-task-benchmark-grading-ai-models-on-real-life-science-research-with-expert-written-rubric/
score: 102
model: google/gemma-4-31b-it:free
generated_at: '2026-06-18T20:49:23.998238'
---

📌 【OpenAI 最新發布】LifeSciBench：用 750 個真實科研任務，挑戰 AI 的生物科學推理極限

目前的生物學 AI 評測大多停留在「問答事實」的層級，但真實的科學研究從來不是選擇題，而是如何在不完美的證據中權衡資訊並做出決策。

面對這種「知識」與「推理」之間的鴻溝，OpenAI 推出了 LifeSciBench，將 AI 置於真實的科研情境中。結果令人挫折但也令人興奮：即便最強的模型，平均也只能通過約三分之一的任務。

🤔 **生物 AI 評測的痛點：事實記憶 $\neq$ 科研能力**

大多數的生物基準測試傾向於設計窄小的、基於事實且有標準答案的問題。然而，真正的科學家在工作中需要處理的是複雜的證據分析與決策過程。目前的評測方法無法衡量模型是否具備真正的「科學推理能力」，這導致我們很難判斷 AI 是否真的能輔助研究，還是僅僅是一個高效的百科全書。

🧪 **173 位 PhD 打造的 750 個真實科研場景**

LifeSciBench 並非簡單的題目集，而是一個模擬真實科研工作流的壓力測試：
- **專家級設計**：由 173 位擁有博士學位且具備生技或製藥經驗的科學家撰寫，每項任務都像是在向同事下達工作簡報（Brief）。
- **多維度覆蓋**：涵蓋 7 個生物學領域（從基因組學、藥物化學到臨床轉譯科學）以及 7 種核心工作流（包括證據分析、設計優化、科學推理、驗證操作、翻譯及科學溝通）。
- **高複雜度**：非選擇題，而是自由回答。約 79% 的任務需要多步推理或決策，平均每題需經過 4 個步驟才能完成。
- **多模態支持**：包含 1,062 個附件（如序列、圖表、PDF、化學結構），53% 的任務必須分析這些附件才能作答。

💡 **核心創新：用「評分量表 (Rubric)」取代「標準答案」**

LifeSciBench 最關鍵的設計在於其評分機制。它不再比對單一的參考字串，而是使用由專家撰寫的詳細 Rubric：
- **極其精細的評分基準**：全集共包含 19,020 條評分準則，每項任務平均有 25 條準則。
- **具體化獎勵**：每條準則對應一個具體的屬性，例如一個特定的事實、一個關鍵的推理步驟，或是在容差範圍內的數值答案。
- **量化指標**：透過「標準化量表得分 (Normalized rubric score)」與「任務通過率 (Task pass rate)」來精準衡量模型的表現。

⚠️ **極高門檻導致的低通過率，顯示模型仍有巨大進步空間**

目前最強的模型通過率僅約 33%，這說明 LifeSciBench 遠未達到飽和狀態。這對開發者來說是一個好消息，因為它提供了一個極具挑戰性的基準，能有效區分模型在處理複雜生物研究時的真實能力差異。

🎯 **對 AI 工程師與研究者的實務啟示**

- **評估管線的升級**：LifeSciBench 的 Rubric 評分法提供了一套可複用的方法論，開發者可以參考這種「多維度準則」來設計更嚴謹的 AI 評估管線，而非依賴簡單的字串比對。
- **從 Fact-based 轉向 Reasoning-based**：未來生物 LLM 的開發重點將從「增加知識量」轉向「提升多步推理與多模態分析」的能力。
- **真實場景的壓力測試**：如果你在開發生技 AI 應用，LifeSciBench 提供了一個極佳的測試集，用以驗證模型在真實科研工作流中的可靠性。

🔗 **相關資訊**
📝 LifeSciBench: a 750-Task Benchmark Grading AI Models on Real Life-Science Research With Expert-Written Rubric
👤 報導來源：MarkTechPost (Michal Sutter)
🔗 閱讀全文：https://www.marktechpost.com/2026/06/17/openai-releases-lifescibench-a-750-task-benchmark-grading-ai-models-on-real-life-science-research-with-expert-written-rubric/

你認為 AI 在未來三年內能將這個通過率從 33% 提升到 80% 嗎？歡迎在評論區討論 👇

#OpenAI #LifeSciBench #BioAI #LLM #生物資訊 #人工智慧 #科學推理 #AI評測
