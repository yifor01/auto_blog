---
title: 'Cloudflare Releases Clef and Clef-flash: Open-Weight Decision Models That
  Return Typed Probabilities Instead of Text'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/01/cloudflare-releases-clef-and-clef-flash/
model: claude-code/sonnet
generated_at: '2026-10-02T21:28:37.562079'
score: 100
---

📌 Cloudflare 首款自研模型不是聊天機器人,是會回機率的決策模型

TL;DR：Cloudflare Workers AI 推出 Clef / Clef-flash,回傳的是機率而不是文字,相容 TypeSafe AI 的 Jev API。

一家以邊緣運算與 CDN 聞名的公司,第一次自己訓練模型,結果訓出來的東西連一句完整的話都不說——這正是 Cloudflare 這次釋出的 Clef 與 Clef-flash 的設計目標。

🤔 **跟上 System One 浪潮,但走自己的訓練路線**

TypeSafe AI 在 2026 年 9 月 15 日發表了首款「System One」模型 Jev,隨後 Kev-9B、Laya 等開放模型跟進。Cloudflare 這次推出的 Clef 系列,同樣採用 System One API,從 Jev 切換過去只需要換 endpoint 與模型名稱。Clef 讀取輸入的 state 與一組 typed questions,針對每個允許的答案都回傳一個機率,完全沒有自由格式文字輸出。它支援 3 種問題類型,單次請求最多可帶 64 個問題與 4 張圖片。兩個模型都以 Apache 2.0 開放權重,目前都已經可以在 Workers AI 上直接呼叫,權重也同步上架 Hugging Face 供自架部署。

🧩 **雙 backbone、兩階段推理、joint schema head**

Clef 是從 Qwen3.8-27B 後訓練而來,Clef-flash 則來自 Qwen3.5-9B,兩者都保留了原本 backbone 的視覺編碼器。推理分兩階段:backbone 先對 state 與問題做一次純 prefill(prefill-only)的前向傳播;接著一個小型 transformer——joint schema head——讀取最終的隱藏狀態,把證據路由到每個問題上,讓各欄位之間可以 cross-attend,並對所有選項做聯合評分,最後用每題各自的 softmax 把 logits 轉成機率。訓練時兩個 backbone 都被凍結,只用 rank-256 的低秩適配器(LoRA)聯合最佳化這個 routing head。損失函數結合了 label-smoothed cross-entropy 與用於校準的 Brier loss,另外還有一個次要目標——Reinforcement Learning for Calibrated Decisions(RLCD),會對相鄰的 ordinal 選項給予部分分數。

📊 **十項基準中贏七項,但 Jev 在推理類題目仍佔優**

在 Cloudflare 從 Decision Index 0.2.1 套件中挑出的 10 項基準裡,Clef 系列在其中 7 項拿到最高分。不過 Jev 在部分推理類題目上仍明顯領先:GPQA Diamond 78.3 分 vs 48.0 分,MMLU-Pro 82.7 vs 65.9,BBH 92.9 vs 73.7。在 TypeSafe 自家的工作流程評測中,Clef 在 4 個領域裡贏了 3 個,差距不大:invoice processing 64.7 vs 61.8,customer service 76.3 vs 76.0,security incidents 62.9 vs 61.7;Jev 則在 agent trace observability 上領先,71.6 vs 68.5。在 Cloudflare 的威脅情資分類情境裡,Clef 完成一次網域分類只花 2.2 秒,相較 gpt-oss-120b 的 4.7 秒快了不少。需要提醒的是,以上數字全部是廠商自行回報,目前還沒有第三方的獨立驗證。

💡 **呼叫方式與自架選項都已就位**

兩個模型都能透過 Workers AI binding(env.AI.run())、REST API,或 AI Gateway 呼叫。想自架的話,模型卡上標註的測試環境是單張 H200、BF16 權重。Cloudflare 同時宣布了一項強化學習服務,用來在私有資料上微調 Clef,初期先對 forward-deployed engineers 開放,之後才會推出自助式平臺;整條 pipeline 串接了 AI Gateway、Workers AI、Containers,以及一個新的 Trainer 元件,有興趣的團隊可以透過 design partner 表單申請。

⚠️ **數字都是廠商自報,複雜推理仍不是它的主場**

Clef 在多項工作流程評測上贏過 Jev,但差距多半是個位數百分點,且評測數字全部來自 Cloudflare 與 TypeSafe 自家測試,尚未有獨立複測。在需要高階推理的題型(GPQA、MMLU-Pro、BBH)上,Jev 仍有明顯優勢,這也呼應了決策模型普遍「不適合複雜推理」的定位。

🎯 **實務啟示**

如果你已經在用 System One API 串接 Jev 類模型做分流、分類或工具參數檢查,Clef 系列幾乎是零成本的替換選項——介面相容、權重開放、還能接上 Workers AI 的基礎設施;但涉及高階推理判斷的場景,仍建議保留原本的大模型路徑。

🔗 **來源**
- 標題：Cloudflare Releases Clef and Clef-flash: Open-Weight Decision Models That Return Typed Probabilities Instead of Text
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/01/cloudflare-releases-clef-and-clef-flash/

#Cloudflare #WorkersAI #DecisionModel #SystemOneAI #OpenWeight #Qwen #ModelCalibration #EdgeAI #LLMOps #MachineLearning
