---
title: Baidu Open-Sources Unlimited OCR 2 for Hundred-Page Document Parsing
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/26/baidu-unlimited-ocr-2-open-source-long-document-ocr/
model: claude-code/sonnet
generated_at: '2026-10-27T21:30:02.899249'
score: 103
---

📌 Baidu 開源 Unlimited OCR 2：百頁文件也能一次解析

TL;DR：3B 模型靠稀疏注意力撐住長文件 OCR，百頁場景準度幾乎不掉。

多數 OCR 模型在處理十幾頁文件時表現亮眼，可是一旦文件長度衝到上百頁，分數往往直接腰斬。Baidu 新開源的 Unlimited OCR 2，宣稱正是為了解決這個落差。

🤔 **長文件 OCR 的真正瓶頸：注意力成本隨長度爆炸**

Unlimited OCR 2 是一個 3B 參數的 vision-language 模型,能把整份書籍、申報文件或報告（頁數上百）的有序頁面圖片,一次轉成結構化文字，輸出涵蓋文字、表格、公式、圖片與標題，並保留閱讀順序。它是今年 6 月發布的 Unlimited-OCR 的後繼版本，而 Unlimited-OCR 本身是在 DeepSeek-OCR 基礎上延伸的。

問題出在哪？在多頁模式下，每一頁會消耗 273 個 image token，而標準的 full attention 成本會隨序列長度呈二次成長,decoding 階段每多生成一個 token，都要掃過越來越長的 KV cache。以 273 token/頁計算,100 頁文件在生成任何輸出之前,就已經累積了 27,300 個 input token。

🧩 **SR-SWA：把注意力壓進固定大小的「工作參考集」**

Baidu 的解法叫 SR-SWA（Sparse Reference Sliding Window Attention）,核心想法是把 text-visual attention 壓縮進一組固定大小的工作參考（working references）裡。模型卡給出的範例大小是 512 個 token，具體配置是 128-token 的本地滑動視窗，加上在 32-token 區塊中挑選 top-16（也就是 16 個區塊 × 32 token＝512 token 的預算）。

這個設計讓每一步的 latency 與記憶體用量,在文件變長時幾乎維持不變，Baidu 稱之為在「有限 context window 內的 unlimited-horizon 解析」。不過要注意，image encoding 與整體 runtime 仍然會隨頁數增加而上升，SR-SWA 省的是 attention 這一步的成本,不是全部。

架構沿用 DeepSeek-OCR 風格的配置：SAM ViT-B 加 CLIP-L 的 encoder,接上一個 12 層的 mixture-of-experts decoder，每個 token 會路由到 64 個專家中的 6 個，外加 2 個共享專家（DeepSeek-OCR 論文稱這個 decoder 為 DeepSeek3B-MoE-A570M）。但 Baidu 並未公開 v2 版本的 active 參數數量。

📊 **百頁測試才是真正的分水嶺**

Baidu 在兩個 benchmark 上測試：MPDocBench（每份文件數十頁）與 MarathonDocBench（每份文件數百頁）。MPDocBench-Parse 是公開 benchmark，含 433 份文件、3,246 頁；MarathonDocBench 目前未見公開發布版本。以下是 Baidu 官方 leaderboard 圖表的數字（自我報告,僅出現在圖片中）：

| 模型 | MPDocBench | MarathonDocBench |
|---|---|---|
| Unlimited OCR 2 | 84.6 | 77.1 |
| Qwen3.8-Max | 78.3 | 22.9 |
| Qwen-3.8-Flash-Next | 77.4 | — |
| Kimi-K3 | — | 33.7 |
| Gemini-3.8-Flash | — | 28.6 |
| Unlimited-OCR（前代） | — | 0.0 |

真正值得注意的不是 MPDocBench 上的分數高低（這部分差距其實不大，Qwen3.8-Max 在文字與公式子項目甚至分別拿到 94.3 與 89.2），而是從數十頁跳到數百頁之後的「掉分幅度」：Qwen3.8-Max 從 78.3 掉到 22.9，掉了超過一半，Unlimited OCR 2 只掉了 7.5 分，前代 Unlimited-OCR 則直接在 MarathonDocBench 上得到 0.0 分。這組對比,正是 SR-SWA 這種稀疏注意力設計的價值所在。

🧰 **怎麼用：MIT 授權，Transformers 或 SGLang**

權重以 MIT 授權開源，程式碼在 GitHub 上。Baidu 的模型卡提供兩種路徑：Transformers 適合快速測試，SGLang 適合正式 serving。

- 在 Transformers 中，`infer` 以 dynamic tiling（gundam mode）處理單頁；`infer_multi` 則在一次請求中解析文件的每一頁，讓模型保留跨頁上下文。載入時需要設定 `trust_remote_code=True`（代表會執行 repo 中的 Python 程式碼，需留意來源信任度）。
- SGLang serving 使用的是 Baidu 客製化的 wheel，而非上游官方版本。官方範例以每個視窗排程 10 頁，並重用前一個視窗的 KV 尾端；視窗調小可以降低峰值記憶體，但會削弱跨頁合併的效果。
- Baidu 特別提醒：預設的 bias 設定可能觸發 462 MiB 的記憶體配置，進而導致 OOM，使用前建議留意這個設定。

🎯 **實務啟示**

對需要處理合約、財報或長篇技術文件的團隊來說，Unlimited OCR 2 的賣點不是「又一個 OCR 模型」，而是它在長文件情境下退化幅度明顯更小的工程設計。如果你的 pipeline 正卡在「十幾頁沒問題，上百頁就崩」的尷尬地帶，SR-SWA 這種固定預算的注意力機制值得實測看看。

🔗 **來源**
- 標題：Baidu Open-Sources Unlimited OCR 2 for Hundred-Page Document Parsing
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/26/baidu-unlimited-ocr-2-open-source-long-document-ocr/

#OCR #Baidu #OpenSource #VisionLanguageModel #SparseAttention #DocumentAI #MixtureOfExperts #DeepSeekOCR #LongContext #MachineLearning
