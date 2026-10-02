---
title: Limits of Confidence in Diffusion
source: Apple ML
url: https://machinelearning.apple.com/research/limits-confidence-diffusion
model: claude-code/sonnet
generated_at: '2026-10-02T21:34:09.172513'
score: 87
---

📌 【Apple ML】離散擴散模型的信心排序，為何從理論上就注定生成錯誤分布

TL;DR：Apple 研究證明，離散擴散模型常用的逐位置信心排序，無法重現 token 間的相依結構。

多數離散擴散模型（remasking、uniform-state samplers）每一步都會同時寫入好幾個 token 位置：每個位置的值從自己的分布中抽樣，而「要寫哪些位置」這個決定，也是由同一組逐位置分布來做的。這聽起來合理，但 Apple 這篇研究要說的是：只要這些位置之間存在相依性，這套做法在數學上就無法對應訓練資料的真實分布。

🤔 核心問題：一步寫多個位置，什麼時候才「對」

像素、音素、文字這類一般領域的資料，位置與位置之間天生就存在相依性（dependencies）。論文要回答的問題是：在一個 step 同時寫入多個位置、且每個位置都各自依據自己的分布抽樣的設計下，什麼條件下生成出來的結果才會真正符合訓練資料的分布？

🧩 三個理論結果：乘積分布救不了相依的一組位置

作者給出三項證明。第一，一個 step 要符合訓練分布，前提是它所寫入的位置，在已經固定下來的 token 條件下彼此條件獨立（conditionally independent）；一旦不獨立，這一步就無法對齊真實分布。第二，如果一組位置彼此相依，不管怎麼組合逐位置分布的乘積，都無法重現這組相依的聯合分布，也就是說「分開抽樣、合在一起寫」這個操作本身就有結構性缺陷。第三，也是比較反直覺的一點：光看每個位置各自的邊際分布，根本看不出一組位置是不是相依的，因為兩個聯合分布可以擁有完全相同的逐位置邊際分布，卻在「哪些值的組合會同時出現」上完全不同。換句話說，只檢查單一位置的分布是否正確，無法保證跨位置的相依結構沒有被破壞。

📊 ScanAndAdd 實驗：逐樣本指標滿分，分布卻偏離 29 倍

為了驗證這套理論，作者使用 ScanAndAdd 這個合成任務，它的聯合分布有封閉形式解，可以精確計算比對。結果顯示：只要信心排序（confidence ranking）選擇寫入的一組位置包含兩個以上尚未決定的位置，這組位置事實上都是相依的。實測生成出來的分布，其 total variation 達到取樣雜訊基準線（sampling-noise floor）的 29 倍；但如果只看逐樣本指標（per-sample metrics），數值卻是完美的 1.0。

💡 樣本看起來沒問題，分布早就跑偏了

這個對比是整篇研究最關鍵的洞察：逐樣本層級的評估完全偵測不到分布層級的系統性偏差。也就是說，如果評測方式只關注「單一樣本好不好」，而不去檢查生成結果的整體分布是否還保有訓練資料中的相依結構，很可能會對一個實際上有系統性問題的採樣策略，給出看似完美的分數。

⚠️ 驗證場景仍是合成任務

這套理論論證針對的是一般領域（像素、音素、文字）都存在的相依性問題，但文中拿來實測驗證的 ScanAndAdd，是一個聯合分布已知、可以封閉求解的合成任務，真實世界文字或影像生成中這個偏差會有多大，素材中沒有進一步說明。

🎯 實務啟示

如果你的團隊在用離散擴散模型生成具有強烈跨位置相依性的內容，例如語法結構嚴謹的程式碼、邏輯鏈很長的文字，純粹依賴逐位置信心分數做採樣決策，可能系統性地扭曲輸出分布。更重要的是，評測這類模型時不能只看逐樣本指標，需要額外設計能捕捉跨位置相依性是否被保留的度量方式，否則很容易被「樣本層級滿分」誤導。

🔗 來源
- 標題：Limits of Confidence in Diffusion
- 作者／機構：Russ Webb, Amitis Shidani, Alice Bizeul, Dan Busbridge（Apple）
- 連結：https://machinelearning.apple.com/research/limits-confidence-diffusion

#DiffusionModels #DiscreteDiffusion #AppleML #GenerativeAI #SamplingTheory #MachineLearning #TotalVariation #ProbabilisticModeling #AIResearch #DeepLearning
