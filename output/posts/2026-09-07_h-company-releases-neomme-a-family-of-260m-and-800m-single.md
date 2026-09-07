---
title: 'H Company Releases NeoMME: A Family of 260M and 800M Single-Tower Multimodal
  Encoders That Drop the Vision Tower and Causal Decoder'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/06/h-company-releases-neomme-a-family-of-260m-and-800m-single-tower-multimodal-encoders-that-drop-the-vision-tower-and-causal-decoder/
model: claude-code/sonnet
generated_at: '2026-09-07T20:41:22.318186'
score: 97
---

📌 H Company NeoMME：拿掉視覺塔與解碼器的文件檢索編碼器

TL;DR：NeoMME 用單一 Transformer 同時吃文字與圖片 patch，260M 參數就打平 3.75B 模型的文件檢索分數。

目前生產環境中常見的視覺文件檢索模型，多半是「借來的」架構：ColPali 以及後續一系列模型，都是把一個生成式視覺語言模型改造成編碼器來用，結果模型裡背著一個獨立預訓練的視覺塔和一個從來不會真的生成任何 token 的因果解碼器——這對一個只需要產生向量表示的任務來說，是白白浪費的參數與算力。H Company 釋出的 NeoMME，就是把這兩塊全部拿掉重做。

🤔 檢索任務不需要生成能力，卻背著生成模型的重量

NeoMME 是一個 260M 與 800M 兩種規模的雙向（bidirectional）編碼器家族：單一 Transformer 從隨機初始化開始訓練，同一組層同時處理多語言文字 token 與原始的 32×32 RGB 圖片 patch，不再區分「視覺分支」與「語言分支」。以此為基礎微調出的檢索模型 NeoMME-Retriever，在 260M 參數規模下於 ViDoRe v3 拿到 0.523 nDCG@10。

是否可部署？可以。所有 checkpoint 都以 Apache 2.0 授權釋出，並在 Hugging Face Transformers 上提供首日支援。260M 模型在單張 NVIDIA L40S 上每秒可索引 51.3 頁，在純 CPU 主機上編碼一次查詢僅需 78.3 毫秒。

🧩 文字走 ALBERT 式嵌入，圖片走從頭訓練的 patch 投影

文字輸入透過 ALBERT 風格的分解式嵌入處理：先查表得到 256 維向量，再投影到模型寬度。圖片則切成不重疊的 32×32 patch，用一個從零訓練的兩層 MLP 投影，完全沒有 patch-merging 模組，也沒有 SigLIP2 視覺塔。兩個尺寸都支援 16,384 token 的上下文，足以在切成 patch 後放入兩張標準的 3,840×2,160 4K UHD 圖片。多數層採用對稱式滑動窗口注意力，每第六層與最後一層改為全域注意力；整體還用上了 grouped-query attention、query-key normalization、gated attention、2D 旋轉位置編碼與平方 ReLU MLP。兩個模型的精確參數量分別是 262,937,906 與 793,715,032。分詞器則是一個不受空白限制的 BPE，詞彙表 131,072 條、從頭訓練，在 FLORES-200 devtest 的 14 種目標語言上，比 ModernBERT 少用 44.4% 的 token。

🧩 用「離散遮罩擴散」逼模型真的去讀頁面

預訓練採用離散遮罩擴散（discrete masked diffusion）處理文字，並可選擇性地以可見的圖片 patch 作為條件。純文字片段的遮蔽率從 0 到 1 均勻抽樣；多模態片段的遮蔽率則從 0.30 到 1 抽樣，刻意排除「只靠語言就能猜答案」的捷徑，強迫模型真正去讀圖片內容。一項跨模態消融實驗證實了這個設計有效：在 90% 遮蔽率下，可見的頁面 patch 讓 260M 模型的遮罩 token 準確率提升 38.4 分，800M 模型提升 40.5 分。每次訓練處理約 5,240 億個打包後的輸入 token，其中約 2,900 億是純文字，分別使用 16 張與 32 張 H100 完成。

📊 260M 模型追平 3.75B 的 ColQwen2.5，但文字檢索仍偏弱

NeoMME-Retriever 在共用骨幹上加了兩個聯合訓練的頭：一個帶 Matryoshka 寬度的均值池化密集頭，以及一個把每個 token／patch 投影到 128 維的 late-interaction 頭，一次前向傳播就能同時輸出兩種表示。在 ViDoRe v3 上，260M 模型拿下 0.523 nDCG@10，800M 模型拿下 0.556；260M 的成績只比參數量高達 3.75B 的 ColQwen2.5-v0.2 低 0.002，並比次佳的其他 300M 以下模型高出 26.1 分，800M 則落後同量級的 Vultron Retriever Flash 0.9 分。在 ViDoRe v1 與 v2 上，兩者分別拿下 0.860/0.522 與 0.874/0.559 nDCG@5。

不過純文字檢索是明顯弱項：在 BEIR-15 上，late interaction 分別只拿到 0.4881 與 0.5126，而僅 149M 參數的 LateOn 拿下 0.5722。作者認為這部分歸因於監督資料規模的落差：NeoMME 只看過約 43 萬筆文字查詢範例，相較之下 mLateOn 看過約 6.6 億筆對比學習範例。

💡 索引成本可以壓到 KB 等級

Late-interaction 索引原本很貴：一張 2048×2048 的頁面會產生 4,162 個向量，float32 下單一 ViDoRe v3 文件約需 1.5MB。團隊提供兩種壓縮方案：以 factor 10 做分層 token 池化並搭配 int8 查詢與文件，可壓到每頁 39.0 KB，縮減 39.4 倍，仍保留 99.16% 的原始 nDCG@10；若用 factor 8 池化搭配 int8 查詢與二元（binary）文件表示，可壓到每頁僅 6.0 KB，縮減 255.5 倍，保留 95.19% 的分數。索引速度方面，在同樣 2048×2048 輸入、單張 L40S 的條件下，NeoMME-260M 每秒編碼 51.3 頁，是 ColModernVBERT（26.0 頁／秒）的 1.97 倍。

⚠️ 定位是文件檢索，不是通用文字檢索

NeoMME 的強項清楚地落在視覺文件檢索：小體積、快索引、分數逼近大上十幾倍的模型。但在純文字檢索場景，它目前明顯不如專門的文字 late-interaction 模型，這也與訓練時投入的文字監督資料規模較小直接相關。

🎯 實務啟示

如果你的檢索場景是掃描文件、PDF 報表或介面截圖這類「以圖為主」的資料，NeoMME 260M 提供了一個計算成本遠低於現有 ColPali 系家族、分數卻不打折的選項，尤其適合對延遲和索引成本敏感的線上服務；但若場景是純文字語意檢索，目前仍建議搭配專門的文字檢索模型，而非直接套用 NeoMME。

🔗 來源
- 標題：H Company Releases NeoMME: A Family of 260M and 800M Single-Tower Multimodal Encoders That Drop the Vision Tower and Causal Decoder
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/06/h-company-releases-neomme-a-family-of-260m-and-800m-single-tower-multimodal-encoders-that-drop-the-vision-tower-and-causal-decoder/

#NeoMME #HCompany #MultimodalAI #DocumentRetrieval #ViDoRe #Embeddings #OpenSource #Transformer #InformationRetrieval #ApacheLicense
