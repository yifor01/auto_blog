---
title: Sakana AI’s Error Diffusion Trains Dale-Compliant Dual-Stream Networks, Reaching
  96.7% MNIST and 61.7% CIFAR-10 Without Backpropagation
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/17/sakana-ais-error-diffusion-trains-dale-compliant-dual-stream-networks-reaching-96-7-mnist-and-61-7-cifar-10-without-backpropagation/
score: 85
model: tencent/hy3:free
generated_at: '2026-07-18T07:37:57.364818'
---

📌 【Sakana AI】不用反向傳播，雙流網路在 MNIST 達 96.7%

TL;DR：Sakana AI 用 Error Diffusion 局部學習規則訓練符合 Dale 原則的雙流網路，免權重搬運。

反向傳播（backpropagation）是深度學習的基石，但它仰賴前向權重矩陣的精確轉置來做反向傳遞——大腦幾乎不可能具備這種機制。這個矛盾，正是 Sakana AI 新論文《Diffusing Blame》直接面對的切入點。

🤔 **權重搬運問題讓反向傳播脫離生物可行性**

標準 backprop 的反向 pass 需要前向權重矩陣的確切轉置，學界稱為 weight transport problem（權重搬運問題）。這意味著系統必須精準儲存並搬運轉置後的權重，而這在生物神經系統中缺乏證據支援。

🧩 **Error Diffusion：只靠三個訊號的局部學習規則**

Error Diffusion（ED）是由 Kaneko 於 2000 年首次提出的局部學習規則（local learning rule）。每次權重更新只依賴三種訊號：突觸前活動（presynaptic activity）、突觸後活化導數（postsynaptic activation derivative），以及單一全域錯誤符號（global error sign）。

由於更新完全在局部完成，ED 不需要搬運轉置的前向權重，也不使用隨機回饋矩陣（random feedback matrices），因此自然相容於 Dale's principle（戴爾原則：神經元要嘛只興奮、要嘛只抑制）。

⚠️ **過往 ED 只驗證過二元分類與 MNIST**

先前的研究僅在二元分類與 MNIST 上示範 ED，且未處理 Dale 原則的約束。這篇工作的主要挑戰，是讓網路在遵守 Dale 原則下擴展到更複雜任務。

🧩 **雙流架構：興奮與抑制分流，權重全非負**

為滿足 Dale 原則，團隊將每一層拆成兩個流：興奮流（p）與抑制流（n）。前向 pass 對每個流計算「興奮減抑制」的預啟用（preactivation）。

設計重點如下：
- 四個權重矩陣 W_pp、W_pn、W_np、W_nn 在元素層級都保持非負（non-negative）。
- 偏置 b_p 與 b_n 是唯一例外，不強制非負。
- W_np 與 W_pn 前的負號是結構性的，不是學出來的；因此跨流連線維持抑制，而所有可學權重皆非負。
- 每層需要四個權重子矩陣，參數量約為單流網路的 4 倍（同架構下約 32M vs DFA 的 8M）。

🧩 **模數錯誤路由：把 ED 帶出二元分類**

主要擴充是 modulo error routing（模數錯誤路由）。對隱藏單元 i，定義路由 r(i) = i mod C（C 為輸出維度），該單元就從被路由到的錯誤分量學習。換句話說，每個隱藏單元被分配一個固定的輸出通道。摘要指出這與 DFA（Direct Feedback Alignment）不同，後者的 feedb（摘要在此截斷，細節未提及）。

📊 **免反向傳播的實測準確率**

根據標題資訊，該雙流網路在無 backpropagation 下達成：
- MNIST：96.7%
- CIFAR-10：61.7%

🎯 **實務啟示**

對工程師而言，這顯示局部學習規則搭配結構化雙流設計，有機會繞開權重搬運問題，在不需要精確反向傳遞的硬體（如類神經形態晶片）上取得可行訓練路徑。ED 的局部性也意味著更高的平行化與生物合理性潛力，但參數量 4 倍膨脹是部署前必須權衡的代價。

🔗 **來源**
- 標題：Sakana AI’s Error Diffusion Trains Dale-Compliant Dual-Stream Networks, Reaching 96.7% MNIST and 61.7% CIFAR-10 Without Backpropagation
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/17/sakana-ais-error-diffusion-trains-dale-compliant-dual-stream-networks-reaching-96-7-mnist-and-61-7-cifar-10-without-backpropagation/

#SakanaAI #ErrorDiffusion #DalesPrinciple #Backpropagation #LocalLearning #DualStream #MNIST #CIFAR10 #Neuromorphic #DeepLearning
