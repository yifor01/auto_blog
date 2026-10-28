---
title: 'Introducing LFM3: Every Modality for Specialized Intelligence'
source: Hacker News
url: https://www.liquid.ai/blog/lfm3
model: claude-code/sonnet
generated_at: '2026-10-28T21:54:37.916359'
score: 97
---

📌 深度解析 LFM3 架構：Liquid AI 怎麼用硬體在環搜尋重新設計 Edge 模型

TL;DR：Liquid AI 官方詳解 LFM3 的 Tri-Hybrid 架構設計,小模型也能吃下長 context agent 任務。

同樣是 2B 級模型,為什麼有些模型在手機上跑起來又慢又卡,有些卻能撐住 256K context 的 agent 任務？Liquid AI 在官方部落格把答案攤開:不是靠堆參數,而是靠一套專為裝置設計、反覆用真實硬體驗證過的混合架構。

🤔 **從 LFM2 到 LFM3,為何要重新搜尋架構**

LFM2 證明了短卷積加注意力的混合架構,能在裝置端跑得快又不掉品質,當年的搜尋範圍只有一支手機與一臺筆電的 CPU。LFM3 把同一套「硬體在環架構搜尋」的範圍擴大到 14 種裝置與後端組合:Samsung Galaxy S26 Ultra、OnePlus 15 等手機,Raspberry Pi 5,Apple M4 Max 與 AMD Ryzen AI 等筆電,Arm 與 x86 雲端 CPU,還有 GPU 與 Qualcomm Hexagon NPU。目標是為 agentic 任務找到「每參數容量更高、長 context 推理更快」的架構,而不只是短提示詞的速度。

🧩 **Tri-Hybrid 層混合與四項細節調整**

LFM3 的骨幹混合三種運算子。24 層中,13 層是閘控短卷積,5 層是視窗 256 token 的滑動視窗注意力(SWA),6 層是全域注意力;卷積核從 LFM2 的 3 擴大到 7。團隊表示,曾嘗試把部分卷積換成其他序列區塊,結果 SWA 給出最好的品質與速度權衡,於是保留下來。

另外還有四項只在「確實提升品質、又不明顯拖慢速度」時才保留的調整:

- Head-wise 閘控注意力:用 sigmoid gate 縮放每個 head 的輸出,讓沒有貢獻的 head 可以關閉,有助於抑制傷害量化的激活值離群,並改善訓練穩定性。
- Partial RoPE:全域注意力層只旋轉每個 head 裡高頻的一半,低頻部分不旋轉,讓這些維度的匹配不受距離影響;SWA 層則維持完整 RoPE。
- Sandwich norm:每個區塊同時對輸入與輸出做正規化,讓激活值維持良好尺度。
- 詞彙表沿用 LFM2.5-8B-A1B 的 128K 詞彙,對非拉丁文字的 tokenize 效率更高。

🧩 **訓練資料與長 context 的效率回報**

LFM3-1.7B-Base 在 22T tokens 上做預訓練,相較 LFM2,資料混合加入更多科學論文、repository 級程式碼、更廣的知識來源與大量數學內容。最後 3.5T tokens 是中期訓練階段,採用精選的高品質資料,並提高 agentic traces 與多樣工具呼叫的比例,同時把 context window 延伸到 256K tokens。官方表示,按參數量計算,LFM3-1.7B 在短提示詞上與 LFM2-1.2B 打平,但在 8K tokens context 下大約快 25%。

📊 **文字模型 LFM3-1.7B 的基準成績**

LFM3-1.7B 定位為本地 agent 與特化應用的文字模型,支援 256K context,並針對 Hermes Agent、Pi、OpenClaw 等 agentic harness 做過後訓練,可用來處理收件匣分類、行程管理、網路研究或用工具搜尋在上千個工具裡找到對的那一個。官方公開的對比數據:

| 基準 | LFM3-1.7B | LFM2.5-2.6B | Gemma 4 E4B | Qwen3.5-9B |
|---|---|---|---|---|
| LiveClaw（agent） | 45.60 | 14.70 | 20.36 | 35.77 |
| WebArena-Verified | 38.42 | 3.02 | 17.06 | 28.94 |
| BFCL V4（工具呼叫） | 71.39 | 55.89 | 48.25 | 62.83 |
| SWE-bench Verified | 43.40 | 18.00 | 0.50 | 51.20 |
| IFEval | 96.66 | 95.39 | 90.02 | 92.08 |
| GPQA Diamond | 63.37 | 57.78 | 57.88 | 80.40 |

可以看出 LFM3-1.7B 在 agent 與工具呼叫類任務上,不只大幅領先同屬 2.6B 的前代 LFM2.5,甚至超過參數量更大的 Qwen3.5-9B;但在需要廣泛知識的 GPQA Diamond 上,體量優勢仍讓 Qwen3.5-9B 保持領先。

💡 **產業夥伴怎麼看裝置端多模態**

AMD 的 Josh Hort 表示,隨著 AI 從雲端走向終端,開發者需要能在各種 AI PC 上高效部署的模型,LFM3 結合了強多模態能力與精簡體積。Ambarella 的 Malhar Palkar 提到,邊緣 AI 正從單一偵測模型演變成同時支援多個並行工作負載(視覺語言模型、自然語言介面、多模態推理),LFM3 把文字、視覺、語音整合進統一架構,且開放權重可供微調,目前已在 Cooper Model Garden 上啟用。Qualcomm 的 Vinesh Sukumar 則認為,下一代 AI 會更多模態、更個人化,同時分散在裝置與雲端之間。

⚠️ **架構調整只保留「有回報」的部分**

值得注意的是,官方強調這些架構改動並非全部採用,而是逐一驗證,只保留那些能提升品質、又不會明顯拖慢推理速度的設計,例如部分嘗試用其他序列區塊取代卷積的做法就沒有被保留,顯示架構搜尋階段做了相當多取捨。

🎯 **實務啟示**

對要在資源受限裝置上跑多模態 agent 的團隊,LFM3 的架構文件提供了一個可參考的設計清單:用 sliding-window attention 取代部分全域注意力以兼顧長 context 速度、用 head-wise gate 抑制量化誤差、用 partial RoPE 平衡位置敏感度,這些都是在實際硬體上反覆驗證過的取捨,而不是單純的理論設計。

🔗 **來源**
- 標題：Introducing LFM3: Every Modality for Specialized Intelligence
- 作者／機構：Liquid AI
- 連結：https://www.liquid.ai/blog/lfm3

#LiquidAI #LFM3 #HybridArchitecture #OnDeviceAI #EdgeComputing #OpenWeightModels #SlidingWindowAttention #AgenticAI #ModelArchitecture #SmallLanguageModels
