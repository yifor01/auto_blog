---
title: 'Z AI Releases GLM-5.4: A 750B Loop Transformer That Runs 28 Layers Twice'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/23/zai-glm-5-4-loop-transformer/
model: claude-code/sonnet
generated_at: '2026-11-24T03:34:11.878541'
score: 113
---

📌 【Z.ai】GLM-5.4用Loop Transformer，750B跑出「2-3T級」智力？

TL;DR：GLM-5.4讓28層權重共享、跑兩次迭代，Z.ai稱以750B規模逼近2-3T模型智力，但旗艦版benchmark尚未公開。

如果一個模型願意把同一組參數「多想一遍」，是不是就能用較小的規模換到更強的推理能力？Z.ai這次把這個想法做到了750B規模，推出首款基於Loop Transformer架構的旗艦模型GLM-5.4。

🤔 **不是從零訓練，而是把GLM-5 base「改裝」成會迴圈的模型**

標準transformer裡，每一層在一次前向傳播中只跑一次。GLM-5.4則讓28層weight-shared layers跑兩次迭代。Z.ai技術貼文指出，若從零訓練一個looped模型，在同等算力下仍會輸給不共享權重的模型；但如果是用既有的GLM-5 base做continued training（持續訓練）去適應迴圈結構，就能用相對小的算力增幅拉高智力上限，這也是GLM-5.4採取的路線。

🧩 **三個工程改動，讓「多跑一遍」不會多花太多資源**

1. **per-token gate**：直接覆寫hidden state會讓activation norm暴衝，因此GLM-5.4為每次迭代加上獨立的per-token gate。第一輪只寫入小幅更新、先建立全域context；第二輪才打開gate做精煉。遇到較難的token，第一輪就會寫入得更積極。
2. **KV cache重用**：第二輪迴圈不會重新建立完整的KV cache，而是重用第一輪挑選出的sparse KV，自己產生的新KV只保留在一個local sliding window內。也就是說，多跑一輪只多付「一個sliding window」的KV cache成本，而不是整份context的cache——Z.ai表示這讓1M context下相對GLM-5.3的成本增幅維持在可控範圍。
3. **indexer重用**：第二輪直接沿用第一輪indexer算出的index，不需要額外的indexing開銷，官方稱與每輪重新計算index相比結果幾乎一致。

📊 **目前的證據來自30B模型，不是750B旗艦**

Z.ai尚未公布750B版GLM-5.4的benchmark分數，官方團隊成員表示分數會晚點公開。目前貼文裡的證據，來自與750B共用架構的30B模型做的iso-parameter ablation：looped版本多用了約10%的訓練算力，分數是在200K長文本SFT、搭配thinking mode後量測出來的（下表數字為Z.ai自行公布，30B模型，並非750B旗艦）。

兩個明顯的模式：數學、科學推理與長文本上的收益最大；同時多數任務的輸出長度變短——MMLU-Pro答案短了14.9%，GPQA-Diamond答案短了11.7%，Z.ai認為部分推理被移進了迴圈帶來的「隱性深度」裡。例外是AIME25，輸出長度只縮短了2%。這套設計已在1B、4B、30B、750B四個規模上驗證過。

💡 **「2-3T等級智力」的說法，目前還沒有旗艦表格支撐**

Z.ai把這個方向稱為「Generalized Coding」，主打程式碼不只是寫軟體，也能生成影片、遊戲、3D shader與CAD內容，技術貼文附了四個demo，但這些是廠商自製demo，並非正式benchmark。效能方面，Z.ai表示離峰可達200 tokens/s，尖峰負載下為70-80 tokens/s，並透過融合核心kernel降低中間記憶體流量。

🎯 **實務啟示**

目前GLM-5.4已經可以透過GLM Coding Plan（Lite每月12.6美元、Pro 56美元、Max 117.6美元，官方說明價格可能調整）、桌面agent工具ZCode（支援macOS、Windows、Linux beta）以及Z.ai Chat使用。對正在處理長context推理成本或KV cache最佳化的工程師來說，這套「per-iteration gate + sparse KV重用」的設計思路值得參考；但在把「2-3T等級智力」的宣稱當作決策依據之前，最好等旗艦版的正式benchmark出來再評估。

🔗 **來源**
- 標題：Z AI Releases GLM-5.4: A 750B Loop Transformer That Runs 28 Layers Twice
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/11/23/zai-glm-5-4-loop-transformer/

#LLM #LoopTransformer #GLM #ZAI #AIArchitecture #KVCache #LongContext #Coding #InferenceOptimization #OpenSourceAI
