---
title: 'StateBench: Testing how language models track state changes over long documents'
source: HuggingFace Blog
url: https://huggingface.co/blog/allenai/statebench
model: claude-code/sonnet
generated_at: '2026-11-03T22:38:09.469375'
score: 87
---

📌 StateBench：讓語言模型在長文件裡玩「變數追蹤」測驗

TL;DR：Ai2 推出 StateBench，分四個難度檢驗模型追蹤長文件狀態變化的能力，混合架構明顯優於純 transformer。

如果一本推理小說寫道「John 把刀交給了 Mary」，下一秒謀殺案發生，讀者必須立刻更新「刀現在在誰手上」這個狀態。對人類是常識，對語言模型卻是個隱藏的理論天花板問題。Allen Institute for AI（Ai2）這次做的，就是把這個天花板量化成一個可驗證的基準。

🤔 **不是所有「狀態追蹤」都一樣難**

程式裡的變數賦值、故事裡角色的位置變化、物件易手，本質上都是同一類問題：模型要在長文件中持續追蹤實體狀態的演變。但素材指出，現有的狀態追蹤測試多半只盯著「最難」的情境，忽略了難度分級——這讓研究者難以分辨，像 Gated DeltaNet 這類帶有遞迴記憶的混合架構，究竟是在哪個難度層級開始超越 transformer。

🧩 **四個難度層級，對應程式語言裡的賦值方式**

StateBench 用程式設計師熟悉的「變數賦值」類比拆出四個層級：

- **R-trivial**：不可變賦值，只需記住變數最初被設定的值（像生日，永遠不變）。
- **Aperiodic**：可重新賦值，模型只需找到「最新」的值（像恆溫器，看最後一次設定）。
- **Soluble**：自我參照更新，每次更新都疊加在目前值上（像遊戲積分，一路累加）。
- **General finite**：允許「賦值給另一變數」，產生跨更新的依賴鏈（像魔術師反覆交換五個杯子下的球，必須追蹤每一次交換）。

這四層並非隨意分級，而是根基於 Krohn–Rhodes 代數理論：狀態追蹤問題可視為有限單群（monoid）上的字詞問題，每個層級對應不同的原子運算組合。StateBench 刻意從同一個 general finite 賦值序列，衍生出另外三個難度版本，變數數量、賦值時間點完全一致，只改變賦值的「類型」，確保四層之間可以公平比較。

📊 **預訓練模型與前沿模型都在「硬」層級卡關**

團隊先測試一批開放預訓練模型，包括 Olmo 3（純 transformer）與 Olmo Hybrid（加入 Gated DeltaNet 層），以及 275M 與 2.7B 參數的小模型，訓練語料和訓練時最長上下文（64,000 tokens）都完全透明。結果顯示：幾乎所有模型在 r-trivial 上表現良好，在 aperiodic 上隨輸入拉長逐漸掉分，在 general finite 上則接近隨機猜測。有趣的是，題型呈現方式也會影響表現——275M 的 hybrid 與 Gated DeltaNet 模型在 RULER 風格的 r-trivial 題目上接近滿分，但換成「電子表格編輯」的同一題，卻掉到接近亂猜，這正是 StateBench 要用多種題型呈現同一問題的原因。

再看前沿模型：Gemini 3.8 Flash、Claude Opus 5.5、GPT-6 Sol 與 Luna 在 r-trivial 與 aperiodic 上表現都不錯，但來到 soluble 與 general finite，隨輸入變長準確率急速下滑，在最長的 general finite 題目上甚至掉到 13% 以下。文章推測,這和「敏感度」有關：難度越高,影響最終答案的步驟越多,模型只要漏掉一步更新就會答錯。

另外,研究團隊也直接拿 275M 參數的模型（兩種 transformer、兩種 hybrid、兩種不同記憶更新限制的 Gated DeltaNet）從頭訓練,只在長度 256 以內的賦值序列上訓練,卻測試到 64,000 個賦值（相當於訓練長度的 250 倍）。結果顯示,Gated DeltaNet 與 hybrid 架構在 r-trivial、aperiodic、soluble 三個層級上幾乎完美泛化到數萬步的序列,顯示架構差異會隨序列拉長而被放大。

💡 **理論預測與實測結果對上了**

依標準理論假設,transformer 能穩健處理 r-trivial（soluble、aperiodic 也有一定程度),但在 general 問題上被預測會失敗;而 Gated DeltaNet 這種更靈活的記憶更新機制,理論上可以覆蓋全部四個層級。這次的實測結果,恰好印證了這個理論分野,也說明了為何近年會出現 Gated DeltaNet 這類遞迴/混合架構的研究動機。

🎯 **實務啟示**

如果你的應用場景只需要「找到最新設定值」（如對話中的使用者偏好),目前的前沿模型與 transformer 架構大致夠用;但如果任務涉及長鏈依賴的狀態追蹤（如追蹤程式碼中跨函式的變數別名、或長篇文件中物件的多次轉手),現有 transformer 架構的失效風險會隨上下文拉長而顯著上升,混合或遞迴架構可能是更穩健的選擇。StateBench 的分級設計也提供了一個實用的診斷工具,讓團隊在選型前先確認「我的任務落在哪個難度層級」。

🔗 **來源**
- 標題：StateBench: Testing how language models track state changes over long documents
- 作者／機構：Kyle Wiggers, Ai2Comms（Allen Institute for AI）
- 連結：https://huggingface.co/blog/allenai/statebench

#StateBench #LongContext #LanguageModels #Transformers #GatedDeltaNet #StateTracking #Ai2 #AllenInstitute #ModelEvaluation #MachineLearning
