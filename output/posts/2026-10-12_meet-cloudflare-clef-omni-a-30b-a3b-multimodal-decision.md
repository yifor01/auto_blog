---
title: 'Meet Cloudflare Clef-omni: A 30B-A3B Multimodal Decision Model for Audio,
  Video, Image and Text'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/11/cloudflare-clef-omni-multimodal-decision-model/
model: claude-code/sonnet
generated_at: '2026-10-12T23:56:03.298591'
score: 88
---

📌 Cloudflare Clef-omni：一次呼叫就能幫文字、圖片、音訊、影片打分數的決策模型

TL;DR：Clef-omni 讓多模態 agent 不用先轉錄、打字幕，直接用機率回答結構化問題。

多模態 agent pipeline 常見的痛點是：影片要先轉文字、語音要先轉字幕，才能讓語言模型理解內容，光是前處理就吃掉不少延遲與工程複雜度。Cloudflare 在原本的 Clef、Clef-flash 發布僅 8 天後，再推出開放權重的 Clef-omni，試圖把這段前處理直接內建進模型裡。

🤔 決策模型在解決什麼問題
Clef-omni 屬於 Cloudflare Clef 決策模型家族的新成員，核心定位不是生成文字，而是對一組固定選項「打分數」。使用方式是傳入一段 state 與一組問題 schema，模型會回傳每個允許選項的機率，不會輸出一句生成式答案。Clef 支援三種問題類型：noul（是非題）、choice（選擇題）與 score（評分），格式沿用 TypeSafe AI 的 Jev 與 SystemOne API。對於需要處理音訊、影片、圖片的多模態 agent 來說，這代表不必再額外串接轉錄或字幕服務。

🧩 架構：凍住 Qwen3 骨幹，只訓練 LoRA
Clef-omni 是從 Qwen3-Omni-30B-A3B-Instruct 後訓練而來，Cloudflare 保留原模型的理解骨幹，拿掉了 text-to-speech 的輸出路徑。推論時模型對完整輸入做單次 prefill，影片畫面與音訊會先同步成一個序列再一起處理；最後由一個小型的 joint schema head 為各選項打分：每個合法選項先從輸入中蒐集證據，再透過欄位向量跨整個上下文做 cross-attend，算出信心分數。訓練階段 Cloudflare 凍結了 Qwen3 骨幹，只訓練 LoRA adapter，損失函數結合 label-smoothed cross-entropy 與 Brier score 校準。

📊 速度與跑分
在 Workers AI 上，Cloudflare 公布的數字顯示：文字決策中位數延遲約 130 毫秒，圖片約 150 毫秒，一段 21 秒含音訊的影片約 1.5 秒即可打完分數。

| 指標 | Clef-omni | 相對表現 |
|---|---|---|
| BANKING77 意圖分類（macro-F1） | 94.8 | 領先 |
| CLINC150+OOS 意圖分類（macro-F1） | 97.7 | 領先 |
| Amazon ESCI | 57.8 | 領先 |
| Home appliances（case-exact accuracy） | 69.3 | 落後 Clef-flash 的 97.73 |
| When2Call accuracy | 63.3 | 落後 Jev 的 80.97 |
| TypeSafe workflow evals（5 項指標） | — | 全部低於自家 Clef |

這些數字來自 Cloudflare 官方公告，並未經第三方獨立驗證。此外，Cloudflare 同時把 hosted Clef 的服務底層換成 SGLang 並調校過 serving stack（這部分沒有釋出新權重），中位延遲在約 800 tokens 時從 262 毫秒降到 152 毫秒（1.7 倍），約 3,400 tokens 時從 616 毫秒降到 305 毫秒（2.0 倍），約 16,000 tokens 時從 2,721 毫秒降到 1,635 毫秒。SGLang 0.5.22 起已支援 Clef。

⚠️ 多模態不等於全面領先
跑分顯示 Clef-omni 在意圖分類與電商類任務上表現突出，但在 home appliances 與 When2Call 這類任務上明顯落後專用模型 Clef-flash 與 Jev，在 TypeSafe 的 workflow evals 上甚至全面低於自家的 Clef。「能吃多模態輸入」與「決策品質最佳」是兩件事，選型時仍需依任務類型實測。

🎯 實務啟示
如果你的 pipeline 本來就需要先用 ASR、OCR、captioning 把多模態輸入轉成文字再丟給 LLM，Clef-omni 提供了一個把這段前處理省掉的選項；但若任務偏向單一模態的高精度決策（例如文字分類、call routing），自家的 Clef、Clef-flash 可能仍是更穩的選擇。

🔗 來源
- 標題：Meet Cloudflare Clef-omni: A 30B-A3B Multimodal Decision Model for Audio, Video, Image and Text
- 作者／機構：Asif Razzaq／MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/11/cloudflare-clef-omni-multimodal-decision-model/

#Cloudflare #ClefOmni #DecisionModel #Multimodal #Qwen3 #LoRA #EdgeAI #WorkersAI #MachineLearning #AIInfrastructure
