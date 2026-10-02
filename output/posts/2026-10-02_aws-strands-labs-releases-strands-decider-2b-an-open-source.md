---
title: 'AWS Strands Labs Releases Strands Decider 2B: An Open Source Decision Model
  That Picks Options in About 115 ms'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/01/aws-strands-labs-releases-strands-decider-2b/
model: claude-code/sonnet
generated_at: '2026-10-02T21:28:37.561936'
score: 102
---

📌 AWS 開源 Strands Decider 2B：一次前向傳播、115 毫秒選出答案的決策模型

TL;DR：AWS Strands Labs 推出開源「決策模型」，不生成文字只選選項，19 億參數可在本機跑。

如果你的 agent 只是要在「billing / sales / retail」之間選一個分類，為什麼要讓一個會寫詩、會聊天、會生成任意文字的 LLM 跑一整輪 decoding？AWS Strands Labs 給出的答案是：換一顆完全不同設計的模型。

🤔 **System One 模型賽道，再添一名玩家**

這類「決策模型」（decision model）也被稱為 System One 模型，是在 TypeSafe AI 上個月推出 Jev 之後才成形的新類別。概念很單純：LLM 能生成任意輸出，而決策模型只在固定選項中選一個，或者在量表上打分。AWS Strands Labs 這次推出的 Strands Decider 2B，就是這條路線上的開源實作。它讀取一段 state 與一組 typed questions，回傳的是一個選項、一個 yes/no 機率，或一個帶校準信心值（calibrated confidence）的分數，答案一律來自請求裡給定的選項集合。

🧩 **拿掉語言模型頭，換上一個百萬參數的指標頭**

Strands Decider 從 Qwen3.5-2B-Base 出發,先把語言建模頭（language-modelling head）整個拿掉,換上一個約 100 萬參數的小型 pointer head。這個頭的做法是比對 <answer> 位置的隱藏狀態與每個選項最後一個 token 的隱藏狀態,單次前向傳播就能得出結果,完全沒有 decoding 迴圈。模型主體（torso）使用 rank-16 的 LoRA 微調,pointer head 則以 fp32 精度運作。因為選項集合是隨請求傳入的,理論上選項數量沒有上限。目前釋出的版本是 v19。這個架構還帶來一個實際好處:針對同一段文字連續問多個問題時,state 只需讀取一次,之後每多問一題只增加該題本身的 token 成本。

📊 **JevBench 排名第 3,但校準才是真正賣點**

團隊在第三方基準 JevBench 上測準確率與校準度。在 9 月 25 日的 v1.4.2 榜單上,v19 在 2B 量級中排名第 3 of 33;若排除 3 個略超過 2B 的模型,則是第 1 of 30。不過倉庫裡也標註了一個對照:Mapika 較新的 decider-2b v11 在 Strands harness 上拿到 175/231,領先 8 個任務;而 Strands Decider 在撰文當時尚未出現在更新的 v1.5.4 綜合榜上。團隊特別強調,校準才是實務上真正有價值的部分——在未見過的短文字分類任務上,信心值在 0.9 以上的答案,正確率約達 95%,團隊建議信心低於這個門檻時就該確認或升級處理。需要留意的是,各項延遲數字來自不同硬體與測試框架,彼此並不能直接比較。

💡 **路由、守門、混合式 agent 是主要落地場景**

團隊回報的早期成功案例集中在模型路由、工具選擇、參數檢查、分流（triage）、guardrails、評測以及混合式 agent。在混合式 agent 的設計裡,LLM 負責處理困難判斷,decider 負責處理瑣碎但頻繁的例行決策。倉庫範例示範了在 Strands agent 裡用 before_tool_call 攔截天氣工具呼叫,問兩個 yes/no 問題:參數是否確實根據使用者說的話、現在呼叫是否過早;如果 agent 是猜測城市,就會改成反問使用者。CLI 範例裡,把「Help! My payouts have been failing for 3 days!」這句話路由到 billing / sales / retail returns 三個分類,結果選中 billing,信心值 0.768。

⚠️ **複雜任務別指望它,預設也沒做好生產環境防護**

團隊自己承認,這顆模型在複雜問題上不如推理模型,完全不適合用來寫程式、聊天或做摘要。另外,內建的 HTTP server 預設綁定在 127.0.0.1 且沒有任何驗證機制,要上生產環境必須自己加一層身份驗證;目前也還沒有任何雲端推理供應商託管這顆模型。

🎯 **實務啟示**

如果你的 agent pipeline 裡有大量「選選項、打分數、做二元判斷」的瑣碎決策,把這些交給一顆 19 億參數、CPU 就能跑、單次前向傳播即可出結果的小模型,很可能比每次都呼叫 LLM 更划算;但校準門檻與升級路徑要自己設計好,別指望它處理灰色地帶。

🔗 **來源**
- 標題：AWS Strands Labs Releases Strands Decider 2B: An Open Source Decision Model That Picks Options in About 115 ms
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/01/aws-strands-labs-releases-strands-decider-2b/

#DecisionModel #AWS #OpenSource #SystemOneAI #AgentRouting #LLM #MachineLearning #Qwen #Calibration #AIInfrastructure
