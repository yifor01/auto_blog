---
title: A Princeton Researcher Proposes Recurrent Looped Transformer (RLT) that Carries
  Decoder State across Every Token, Fixing 96 Blocks per Token with Unbounded Temporal
  Depth
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/13/a-princeton-researcher-proposes-recurrent-looped-transformer-rlt/
model: claude-code/sonnet
generated_at: '2026-09-13T19:41:28.756937'
score: 77
---

📌 【Princeton 研究】讓 Decoder 記住上一個 token 的狀態,Recurrent Looped Transformer 的設計構想

TL;DR：RLT 提出讓 decoder 隱狀態跨 token 傳遞的架構設計,但作者明言目前只有設計規格,沒有任何實測結果。

在目前主流的 decoder-only LLM 裡,第 t 個 token 算到最後一層的東西,跟第 t+1 個 token 完全沒有直接關係,兩者只能透過 attention 機制去查快取的 key/value 間接溝通。Princeton 研究者 Yifan Zhang 提出的技術報告 Recurrent Looped Transformer（RLT）,想把這個斷點接起來。

🤔 **要解決的問題:token 之間為何要「失憶」**

現行 decoder-only 架構下,每個 token 的運算彼此獨立,只靠 attention over cached keys and values 串連。RLT 的核心構想是:把 decoder 最後一層的完整隱狀態,連同其逐層的 sliding-window attention（SWA）快取,直接帶進下一個 token 的運算裡,而且是在 prompt 與 response 之間都不重置。

🧩 **架構:一個因果 Encoder 配上一個會「記憶」的 Decoder**

RLT 把一個 causal encoder 與一個 recurrent decoder 配對使用:

- Encoder 平行處理所有 token（在因果遮罩下),產生表徵 e_t,並由此投影出 key-value 記憶 M≤t;記憶群組可以在 decoder 各層共用（G=1),也可以每層各自獨立（G=L_D)。
- Decoder 負責遞迴。它的完整狀態寫作 H_t = (s_t, C_t^D),其中 s_t 是 decoder 最終輸出,C_t^D 則是每一層 decoder 保留下來的 SWA key/value。
- 每個 token 的運算流程:先用一個 gated merge 把當前 encoder 表徵 e_t 與上一個 token 的 decoder 輸出 s_{t-1} 結合,再由 decoder block 依序執行「對 decoder 活化值做 causal SWA」→「對 encoder 記憶做 cross-attention」→「FFN」。
- 滑動視窗 W 包含當前 token 本身,因此每層最多只保留 W-1 個歷史項目。
- 下一個 token 的機率分佈由 s_t 讀出;在 BOS 之前,系統以一個學習得到的起始狀態 s* 和空快取做初始化。

參考的 tied 設定用了 48 層 encoder 與 48 層 decoder,attention 與 FFN 權重在兩者之間共享。也就是說每個 token 實際上要跑 96 個邏輯區塊,但因為 decoder block 多了 cross-attention,每個區塊的 FLOPs 並不相等。Zhang 強調這是「參數重用」,而不是「活化值複製」。

💡 **訓練與服務端的隱藏複雜度**

Pretraining 階段是全序列的 next-token prediction,並透過完整的 BPTT（backpropagation through time)訓練。SFT 階段雖然把 loss 遮罩到只算 assistant 的目標 token 上,但狀態更新完全不遮罩,所以 assistant 的 loss 會一路反向傳播穿過 user 與 tool 的 token。報告的附錄 B 也提到,部分性的梯度截斷（detaching)是危險的:狀態到狀態的 Jacobian 裡存在經過 decoder KV 的交叉項,如果只截斷 s_t,梯度仍然可以透過快取繼續流動,因此任何截斷式 BPTT 方案都必須明確列出每一個被截斷的張量。

在多輪對話的服務情境中,一個「精確前綴快照」需要包含 encoder 快取與記憶、完整的 decoder 狀態、位置中繼資料、視窗慣例,以及模型版本。由於狀態與服務端的切分方式無關,固定權重下的快照可以重複使用;但模型權重一旦更新,舊快照就會失效,若使用者編輯了對話前綴,系統也必須從更早的檢查點重新計算。在多輪 RL 場景中,外部插入的 token 會更新狀態,但不會獲得 importance-ratio 的加權因子。

RLT 與既有工作的關係也值得一提:記憶機制延續了 YOCO（為 cross-decoder 只快取一次 KV)與 DeepSeek-V4.1-Flash（從 encoder 最終狀態投影出 decoder 全域 KV)的思路,但捨棄了它們的「跳過 decoder 處理整段 prompt」設計;時間維度的回饋則承接 Feedback Transformer 與 Recurrent Transformer,差別在於 RLT 把上一個 token 的 decoder 最終輸出直接餵回下一個 decoder 輸入,並且連 prompt 階段都跑遞迴;深度維度的參數重用則呼應 Universal Transformers 與 recurrent-depth latent reasoning 的思路。

⚠️ **目前僅是設計規格,尚無實測數據**

必須強調的是,這份報告本身明確定位為「設計規格」(a design specification):它定義了架構、執行排程與 RL replay 的約定,但明確聲明沒有提供任何效率、推理品質或規模化（scaling)的實測結果。換句話說,RLT 目前是一套完整但尚未經驗證的架構藍圖。

🎯 **實務啟示**

如果你的團隊在研究長上下文或多輪對話的狀態管理,RLT 提出的「精確前綴快照」概念(需包含 encoder 快取、decoder 狀態、位置資訊與模型版本)是一個值得參考的工程檢查清單,尤其是在設計 KV cache 重用或多輪 RL 系統時。但在看到實測數據之前,不建議把這個架構當作現成方案直接導入生產環境。

🔗 **來源**
- 標題：A Princeton Researcher Proposes Recurrent Looped Transformer (RLT) that Carries Decoder State across Every Token, Fixing 96 Blocks per Token with Unbounded Temporal Depth
- 作者／機構：Yifan Zhang（Princeton),報導由 Asif Razzaq／MarkTechPost 撰寫
- 連結：https://www.marktechpost.com/2026/09/13/a-princeton-researcher-proposes-recurrent-looped-transformer-rlt/

#Transformer #LLMArchitecture #RecurrentNeuralNetwork #DeepLearning #AIResearch #Princeton #NeuralNetworkDesign #SlidingWindowAttention #ReinforcementLearning #MachineLearningResearch
