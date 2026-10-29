---
title: Speeding up language models for travel applications
source: Amazon Science
url: https://www.amazon.science/blog/speeding-up-language-models-for-travel-applications
model: claude-code/sonnet
generated_at: '2026-10-29T21:57:12.931781'
score: 106
---

📌 Amazon 與 Booking.com:把 LLM 延遲砍到 1/20,成本砍到 1/3

TL;DR:結合知識蒸餾與 Medusa 平行解碼,Amazon 與 Booking.com 讓旅遊 LLM 快 10-20 倍、成本不到三分之一。

旅遊平臺的 AI 客服回答得再準確,只要慢了 100 毫秒,使用者可能就已經關掉頁面——這正是 Amazon Science 與 Booking.com 這次合作要解決的問題:如何讓數百億參數的 LLM,既保留原本的回答品質,又快到能撐起真正的即時互動。

🤔 大模型準,但太貴也太慢

旅遊平臺近年廣泛採用大型語言模型來提供目的地問答、飯店推薦與行程規劃等服務,這些模型通常有數百億參數,推理費用隨查詢量線性成長,而且對 web、mobile 這類場景來說常常太慢。Amazon 與 Booking.com 針對三個具體功能進行最佳化:AI Trip Planner(需在一秒內從對話中擷取旅遊偏好)、Smart Filters(即時將自然語言查詢轉成結構化篩選條件)、以及 Accommodation Description Generation(要在數百萬筆房源規模上生成描述,重點是成本)。

🧩 知識蒸餾 + Medusa:一次解決延遲與成本

Medusa 是一套在推理階段降低 LLM 延遲的框架,做法是在基礎 LLM 上加裝多個「Medusa head」,讓原本一次只能生成一個 token 的序列解碼,變成多個 token 平行預測;由於 LLM 運算所用的 GPU 本就擅長平行運算,這類平行解碼幾乎不增加額外負擔,一般可帶來 2 到 4 倍的加速,且不犧牲生成品質。

知識蒸餾(KD)則是把大型「教師模型」的知識轉移給小型「學生模型」:教師模型先在標註資料上訓練或微調,再用它對額外的未標註資料生成預測,最後將人工標註與教師標註的資料合併,用來訓練更小的學生模型,使其學會模仿教師行為。

這次的做法是把兩者整合進同一條 pipeline:先微調教師模型,再用它對領域相關的未標註文本生成預測;訓練學生模型時,在學生模型上掛上 Medusa head,並用「教師預測 + 人工標註」的混合語料訓練,一次得到既繼承教師知識、又具備多 token 平行預測能力的精簡模型。

📊 四階段實驗:教師是 70B,學生只有 1.1B

實驗選用 TinyLlama(11 億參數)作學生模型,Llama-3.1(700 億參數)作教師模型,共做了四組遞進實驗:

1. 僅針對三個應用場景分別微調 TinyLlama,結果已明顯優於 few-shot GPT-4o,證實領域專屬微調能彌補模型規模小的劣勢,但仍不及教師模型。
2. 加入知識蒸餾(人工標註 + 教師標註混合資料)後,與教師模型的差距縮小超過 90%,接近打平;模型變小也讓推理速度快了約 6 倍,但仍不足以支撐即時場景。
3. 加裝 Medusa head 後,推理再快 2 到 3.6 倍。團隊測試了兩種變體:Medusa-1 先微調基礎模型、凍結後再單獨微調 Medusa head;Medusa-2 則一次訓練全部。兩者加速幅度相近、品質都沒有明顯損失,但 Medusa-2 的流程更簡單,對於要同時管理多個模型的生產團隊更實用。

結合知識蒸餾與 Medusa-2 後,最終模型在維持 70B 教師模型品質的同時,依應用場景不同能跑快 10 到 20 倍。

三個場景的實際成果:AI Trip Planner 的使用者互動率比 GPT-3.5 提升 2.9%;Smart Filters 在 99% 的查詢上回應速度提升 15 倍;房源描述生成則獲得多 1.4% 的「有幫助」評價,成本不到 GPT-4 的三分之一。

💡 這套方法去年已在 ACL 拿下業界最佳論文

這項成果曾在前一年的 ACL(Association for Computational Linguistics)年會上發表,並獲得 Industry Track 最佳論文獎,顯示這套「KD + Medusa」的組合並非紙上實驗,而是已在真實流量上驗證過的工程方案。

🎯 實務啟示

對任何想把大模型能力搬進高流量、低延遲場景的團隊,這個案例給出一條清楚的路徑:先用領域資料微調小模型打底,再用教師模型的知識蒸餾補齊品質差距,最後疊加 Medusa 之類的平行解碼技術處理剩下的延遲缺口——三步合起來,才真正同時解決成本與速度的問題,單靠任何一步都不夠。

🔗 來源
- 標題:Speeding up language models for travel applications
- 作者/機構:Amazon Science,與 Booking.com 團隊合作
- 連結:https://www.amazon.science/blog/speeding-up-language-models-for-travel-applications

#LLM #KnowledgeDistillation #Medusa #Inference #LatencyOptimization #Booking #TravelTech #ModelCompression #AWS #ACL
