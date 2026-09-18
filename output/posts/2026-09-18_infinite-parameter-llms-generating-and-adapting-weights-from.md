---
title: 'Infinite-Parameter LLMs: Generating and Adapting Weights from Live Data'
source: Hacker News
url: https://arxiv.org/abs/2609.18842
model: claude-code/sonnet
generated_at: '2026-09-18T19:49:34.902882'
score: 95
---

📌 權重不再固定：一篇論文提出「無限參數」LLM 架構

TL;DR：新論文提出讓模型即時把互動資料寫進權重，而非只塞進 prompt。

RAG 幫你把外部知識塞進 context，fine-tuning 幫你把知識固化進權重，但兩者都解決不了同一個問題：使用者這一秒告訴模型的事實或更正，下一輪對話結束後就消失了。這篇論文想解決的，正是這道「即時資訊該放哪裡」的縫隙。

🤔 **核心問題：即時互動資料無處安放**

論文指出，scaling laws 告訴我們模型參數與訓練資料愈多、能力愈強，Mixture-of-Experts（MoE）架構也靠著「每個 token 只啟動龐大參數庫中的一小部分」延續了這套規律的成功。但這一切都建立在靜態的預訓練資料之上。實際部署後，模型面對的是一個不同的世界：真正能讓它變得更有用的資訊,往往不在訓練集裡，而在它正在處理的即時互動中，例如使用者提供的事實或給出的更正。傳統模型的權重在訓練後就被凍結，無法從這類資料中學習，只能把這些即時提供的知識與行為放進 prompt，透過檢索或指令的方式，在每一次請求時重新讀取一遍，請求結束後就被丟棄。

🧩 **方法：用 hypernetwork 即時生成低秩權重**

作者提出的問題是：有沒有辦法讓架構直接把即時互動「寫進」權重裡學習？受 MoE 啟發，他們提出了 Infinite-Parameter LLM。其設計是用一個結構精簡的 hypernetwork，把執行期間取得的資料轉換成對一個共享 base network 的低秩（low-rank）調整，也就是說，前饋層（feed-forward）的權重是由即時資料「生成」出來的，而不是儲存在一個固定的參數庫裡。

論文特別指出與既有 weight generator 方法的差異：先前的方法通常只讀取一次 context 就把生成的權重凍結住，而這篇論文的方法會為 hypernetwork 的潛在編碼（latent code）維護一個 Bayesian belief（貝氏信念），並隨對話進行持續線上更新。也就是說，隨著 session 推進，有效權重會不斷根據這個逐步演化的信念被重新推導出來，而不是讀一次就定型。其結果是：模型儲存下來的參數量維持固定，但它能「編譯」出來的權重組合實質上是無限的。

💡 **主張的優勢：把即時知識搬進權重的好處**

論文主張，把執行期取得的知識與行為放進權重、而非放進 prompt，能帶來幾項好處：計算成本被攤提（amortized）、釋放出原本被佔用的 context window 空間、資訊能跨輪次持續保留，且效果有機會優於單純的 in-context learning。

⚠️ **目前仍停留在方法與評估協定層級**

需要說明的是，這篇論文目前公開的內容是方法論與研究構想，作者表示他們「specify an evaluation protocol」，也就是設計了一套用來對比 in-context learning 與檢索方法的評估流程，但摘要中並未附上任何實際訓練資料集、訓練設定或實驗數據，因此這套架構的實際效果如何，仍有待後續實驗結果驗證。

🎯 **對工程師的意義**

如果你的系統長期被「context window 塞爆」或「每次都要重新檢索同一批使用者背景資訊」的問題困擾，這篇論文提出的方向值得關注：與其不斷把即時資訊塞進 prompt，未來或許能有架構讓模型直接把這些資訊「內化」成權重的一部分。不過目前這仍是一個尚待實驗驗證的構想，實務導入前建議持續追蹤後續是否釋出程式碼與具體評測數據。這篇論文在 Hacker News 上獲得 155 點與 41 則討論，顯示社群對此方向有一定關注度。

🔗 **來源**
- 標題：Infinite-Parameter LLMs: Generating and Adapting Weights from Live Data
- 作者／機構：Jinli Hu, Ross M. Clarke, Yichuan Zhang, José Miguel Hernández-Lobato
- 連結：https://arxiv.org/abs/2609.18842

#LLM #MachineLearning #NeuralArchitecture #MixtureOfExperts #Hypernetwork #InContextLearning #BayesianDeepLearning #AIResearch #ModelAdaptation #DeepLearning
