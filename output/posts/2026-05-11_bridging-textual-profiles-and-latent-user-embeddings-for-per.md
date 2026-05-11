---
title: "Bridging Textual Profiles and Latent User Embeddings for Personalization"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.06981
score: 98
model: tencent/hy3-preview:free
generated_at: 2026-05-11T20:46:35.560736
---

📌 【Notre Dame & Google】BLUE：連結文字使用者畫像與潛在向量嵌入  

🎣 你以為「可解讀」的使用者描述就必須犧牲推薦效果？最新研究指出，兩者其實可以透過強化學習雙贏。  

🤔 **現有使用者表示方式難以兼顧解讀性與效能**  
個人化系統通常依賴兩種使用者表示：一是經監督訓練的潛在向量嵌入，檢索表現佳但難以解讀；二是文字使用者畫像，易於理解卻缺乏直接的下游監督訊號，難以優化推薦目標。這種「解讀 vs. 效能」的權衡，限制了現在個人化模型的靈活性。  

🧪 **以強化學習對齊文字畫像與向量獎勵**  
研究團隊提出 BLUE 框架：給定使用者互動歷史，先由一個大型語言模型（Profiler LLM）產生文字使用者畫像；同時，一個嵌入模型根據使用者與正向/負向項目的距離提供獎訊號。透過強化學習，BLUE 讓產出的文字畫像在嵌入空間中朝向正向項目移動、遠離負向項目。為保證語意意義，團隊又額外引入一個基於「下一項預測」的文字空間監督訊號，使學習到的畫像既具語義連貫性，又對下游檢索具備判別力。  

📊 **在零射擊序列推薦與跨域遷移上持續優於強基線**  
實驗分別在 Amazon Reviews 2023 與 Google Local Reviews 上進行零射擊序列推薦測試。結果顯示，無論嵌入模型是凍結還是可訓練，BLUE 都能持續優於現有強基線。特別是跨域遷移實驗中，BLUE 學習到的使用者畫像展現較佳的泛化能力。進一步的問答（QA）評估表明，該框架產出的文字畫像相較於原始使用者歷史或其他畫像優化方法，能提供更豐富的個人化上下文。  

💡 **文字畫像不再只是「可解讀的副產品」，而是可以訓練的效能載體**  
BLUE 的核心洞察是：透過獎訊號將文字空間拉近嵌入空間的正向區域，文字畫像不僅保留語義可讀性，同時獲得與嵌入相似的判別力。這意味著開發者可以在不犧牲解讀性的前提下，直接利用 LLM 產出的使用者描述來做檢索、排序甚至下游任務（如問答），而不需要額外的標註或複雜的對齊步驟。  

⚠️ **實驗主要聚焦於零射擊情境與特定評審資料集**  
研究僅在 Amazon Reviews 2023 與 Google Local Reviews 上進行零射擊序列推薦評估，長期使用效果與其他領域（如新聞、影片）的表現尚未驗證。此外，文中未詳述 Profiler LLM 的具體規模或訓練成本，這對於資源受限的產品團隊而言是值得關注的實務考量。  

🎯 **實務上可先嘗試「RL 對齊 + 下一項預測監督」的兩步驟流程**  
- 若系統已經使用嵌入模型做檢索，可將該模型當作獎訊號來源，讓 LLM 產出的使用者畫像透過簡單的策略梯度更新向正向項目靠近。  
- 加入下一項預測的文字監督，可防止畫像在追求獎訊號時語義漂移。  
- 在需要解讀的場合（如除錯、使用者說明），直接呼叫 LLM 產出的畫像；在需要高效檢索的場合，則可將同樣的畫像送入嵌入模型進行向量比較。  

🔗 **論文連結**  
📝 Bridging Textual Profiles and Latent User Embeddings for Personalization  
👤 Zhaoxuan Tan, Xiang Zhai, Yan Zhu, Meng Jiang, Mohamed Hammad (University of Notre Dame; Google)  
🔗 https://arxiv.org/abs/2605.06981  

你的個人化系統是否正在為「可解讀」與「效能」左右為難？BLUE 或許提供了一條可行的中道路。歡迎在留言區分享你的看法或實作經驗 👇  

#AI #RecommendationSystems #LLM #Personalization #NotreDame #GoogleResearch #InformationRetrieval #BLUE #ReinforcementLearning
