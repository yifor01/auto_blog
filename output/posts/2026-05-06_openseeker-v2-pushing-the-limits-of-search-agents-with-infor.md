---
title: "OpenSeeker-v2: Pushing the Limits of Search Agents with Informative and High-Difficulty Trajectories"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.04036
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-06T20:43:10.407908
---

📌 【SJTU 純學術突破】僅用 SFT，30B Agent 登上搜尋 SOTA

你以為要推動搜尋 Agent 的能力，必須砸下預訓練、持續預訓練與強化學習的龐大成本？這項研究顯示：只要給對的「高難度與高資訊密度軌跡」，單純監督式微調就能讓 30B 級模型在多項基準上超越業界重型訓練方案。

🤔 **搜尋能力已成 LLM 必備，但被巨頭資源壟斷**

前沿 LLM Agent 的深度搜尋能力逐漸變為標配，但開發流程長期由科技巨頭主導：預訓練、持續預訓練（CPT）、監督式微調（SFT）加上強化學習（RL），整套 pipeline 極度消耗資源。這種高門檻讓學術團隊很難在搜尋 Agent 上做出同級別貢獻。

問題在於：是否必須靠重訓練才能推動搜尋 Agent 的能力邊界？

🧪 **三個簡單修改，打造高品質與高難度軌跡**

上海交通大學團隊沒有增加架構複雜度，而是從資料合成出發，針對軌跡品質進行三項修改：
- 擴充知識圖譜規模，以支持更豐富的探索路徑  
- 擴增工具集規模，以涵蓋更廣泛的搜尋與推理功能  
- 嚴格低步數過濾，保留高難度且資訊密集的軌跡  

在僅 10.6k 筆資料上進行純 SFT，採用 30B 級模型與 ReAct 框架，與業界重型 CPT+SFT+RL 方案進行對比。

☑️ **僅用 SFT，在四大基準全面超越重型訓練方案**

OpenSeeker-v2 的表現如下（對比同級方案）：
- BrowseComp：46.0% vs 43.4%  
- BrowseComp-ZH：58.1% vs 46.7%  
- Humanity’s Last Exam：34.6% vs 32.9%  
- xbench：78.0% vs 75.0%  

這不僅是同一模型尺度與範式下的搜尋 Agent 首度由純學術團隊以 SFT 達到 SOTA，也顯示資料品質與難度設計可以直接壓縮對重型訓練流程的依賴。

💡 **用難度過濾與資訊密度取代訓練流程的複雜度**

核心洞察並非「SFT 萬能」，而是「高難度軌跡能逼出更好的泛化」。透過嚴格步數限制與知識圖譜擴充，模型被迫在有限步內整合分散資訊；工具集的擴增則讓策略空間更貼近真實搜尋需求。這些改變讓 SFT 不再只是「模仿」，而是推動推理邊界的能力放大器。

⚠️ **以 10.6k 資料達到 SOTA，仍需謹慎看待擴展性**

- 資料規模相對較小，長期穩定性與擴展至更大模型的效果尚待驗證  
- 聚焦於特定基準與 ReAct 範式，對不同工具生態或長期 Agent 循環的適用性仍需探討  
- 高效能依賴嚴格的軌跡過濾與合成品質，隨著任務多樣性提升，維持資料門檻可能會面臨成本挑戰  

🎯 **資料工程與難度設計，是下一階段 Agent 訓練的關鍵槓桿**

- 學術與中小型團隊可以優先投資於合成資料品質，而非預訓練與 RL 基礎設施  
- 在內部 Agent 開發中，引入難度過濾與知識圖譜擴充機制，有望以更低成本提升搜尋表現  
- 將 SFT 視為「推理能力塑形」的工具，而非僅僅是行為克隆，有助於釋放中小型模型的潛力  

🔗 **論文連結**  
📝 OpenSeeker-v2: Pushing the Limits of Search Agents with Informative and High-Difficulty Trajectories  
👤 Yuwen Du, Rui Ye, Shuo Tang, Keduan Huang, Xinyu Zhu @ Shanghai Jiao Tong University  
🔗 https://arxiv.org/abs/2605.04036  

你的團隊在訓練搜尋 Agent 時，最在意的是模型規模、訓練流程，還是資料品質？歡迎留言分享你的觀察與實務經驗 👇

#AI #SearchAgent #LLM #MachineLearning #SFT #ShanghaiJiaoDongUniversity #OpenSeeker
