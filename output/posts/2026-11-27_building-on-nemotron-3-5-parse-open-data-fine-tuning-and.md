---
title: 'Building on Nemotron 3.5 Parse: Open Data, Fine-Tuning, and Faster Inference'
source: HuggingFace Blog
url: https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin
model: claude-code/sonnet
generated_at: '2026-11-27T01:08:20.144844'
score: 96
---

📌 NVIDIA Nemotron 3.5 Parse：資料、微調與加速全公開

TL;DR：NVIDIA釋出文件解析模型Parse 3.5的訓練資料集、SFT+RLVR微調食譜與DFlash2加速技術，讓開發者能自行復現並微調到自家文件類型。

一張長條圖上沒有標任何數值，只有座標軸與柱子高度，模型要怎麼「讀」出正確數字？NVIDIA在這篇文章秀出的範例裡，Parse 3.5單靠圖形幾何，就推算出了18、27、39、54這組數值，這正是這次更新的重點能力之一。

🤔 **表格錯一格，意思全變**

Parse是一個把文件頁面影像轉成結構化資料的模型，供RAG（檢索增強生成）與agent應用使用。它會把內容依閱讀順序擷取出來，標上標題、段落、表格、圖表等類別，並給出對應的bounding box定位。文章特別點出表格解析的難點：結構本身就承載意義，一行或一列錯位，整張表的解讀就全錯了。而圖表則常常沒有標示明確數值，需要模型自行從座標軸與圖形比例反推。

🧩 **先學會讀，再學會讀得穩**

NVIDIA開源了三個用於訓練Parse 3.5的合成資料集：Synthetic Charts V1（998萬筆，圖表與其結構化標註，涵蓋類別、序列與數值）、Synthetic Tables V1（100萬筆，保留列、欄、標頭與單元格關係的HTML表格）、OCR Synthetic Multilingual v2（790萬筆，跨多種字型與版面的多語言文件頁面）。訓練分兩階段進行：第一階段是supervised fine-tuning（SFT），涵蓋文字、版面、表格、圖表與多語言文件，用來建立「讀懂一頁內容」的基本能力；第二階段是reinforcement learning with verifiable rewards（RLVR，可驗證獎勵的強化學習），採用Group Relative Policy Optimization（GRPO）演算法，獎勵機制會檢查擷取結果的品質，例如圖表是否正確還原了序列與數值、輸出結構是否可用、有沒有陷入重複生成或是沒有正常結束。這讓模型在面對同一頁可能有多種合理表示方式時，仍保有彈性找到正確答案，同時避免迴圈與輸出未完成的問題。

在架構上，Parse 3.5相較Parse 2.0也做了全面調整：

| 元件 | Parse 2.0 | Parse 3.5 |
|---|---|---|
| 頁面前處理 | 固定2048×1664畫布 | NaViT動態矩形輸入 |
| 影像轉文字連接 | Encoder-decoder cross-attention | 壓縮視覺token作為causal prefix |
| Decoder self-attention | 多頭注意力 | GQA-8（16個query head、8個key/value head） |
| 推測解碼 | 單token前瞻（MTP） | 可選用DFlash2 |

其中DFlash2是一個小型draft模型，一次最多提出32個token的預測，再由Parse一併驗證。在實測的32-token設定下，平均每輪驗證可接受約14個draft token，相當於每個驗證步驟推進約15個輸出token的進度（含目標token本身）。

📊 **RLVR把迴圈砍掉77%，分數從66.24升到71.38**

文章提供了一組在相同評測條件下、SFT與GRPO的開發版checkpoint對照：被標記為迴圈的頁面數從126降到29，減少約77%；撞到9,000 token上限而被截斷的輸出從185降到35；整體分數由66.24提升到71.38，其中表格項目提升5.18分，圖表項目提升4.15分。

在推論速度上，單張H200、BF16精度、同一組2,078頁的原生單次推論測試顯示：DFlash2在併發數為1時讓輸出速度提升7.62倍，在併發數512時提升1.52倍（相較於關閉推測解碼的Parse 3.5）。具體數字上，併發512時Parse 3.5不開推測解碼可達13.48頁/秒，開DFlash2後達到20.44頁/秒，分別是Parse 2.0同條件下2.98頁/秒的4.53倍與6.86倍。

此外，文章也提出可依難度選擇處理層數：單次解析整頁；雙次解析則針對密集表格與圖表細節，裁切後以更高細節重新解析再合併回去；三次解析則額外用模型的偵測模式驗證所有區塊是否被完整偵測，再重新擷取發現的圖表或表格。在參考評測中，雙次與三次解析分別比單次多出2.18與2.46個ParseBench分數，但多次裁切也意味著需要發出多次請求，是在速度與精確度之間的取捨。

🧪 **從0%到96.58%：一份牙科圖表的微調示範**

NVIDIA也分享了完整的微調食譜：先產生配對資料，再用NeMo Automodel做SFT，接著用NeMo RL搭配vLLM生成候選答案做GRPO訓練。範例是一張含odontogram（牙位圖）的合成牙科表單，原始模型能讀出牙齒編號，卻讀不出對應的處置項目表。經過SFT後，六列圖表內容全部對齊目標；在這份牙科參考實驗中，首次嘗試成功率（pass@1）由基礎模型的0%，SFT後提升到95.85%，RLVR後再提升到96.58%。

🎯 **實務啟示**

NVIDIA把資料集、架構改動與訓練食譜一次性開放，等於把「如何讓文件解析模型更懂你自己的文件類型」這件事變成可照抄的流程：用合成資料生成配對、SFT打底、RLVR磨細節，再視場景決定要不要用DFlash2換速度，或用多次解析換精度。

🔗 **來源**
- 標題：Building on Nemotron 3.5 Parse: Open Data, Fine-Tuning, and Faster Inference
- 作者／機構：Ryan Chesler, Marek Wawrzos, Steve Han／NVIDIA
- 連結：https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin

#NVIDIA #DocumentAI #RAG #FineTuning #GRPO #ReinforcementLearning #OCR #SpeculativeDecoding #OpenDatasets #NeMo
