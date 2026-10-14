---
title: Lab-in-the-Loop at Compute Speed — Ian Quigley, Leash Bio
source: Latent Space
url: https://www.latent.space/p/lab-in-the-loop-at-compute-speed
model: claude-code/sonnet
generated_at: '2026-10-14T20:56:31.587382'
score: 89
---

📌 DNA 編碼庫養出的乾淨資料，正在教 AI 做藥物化學推理

TL;DR：Leash Bio 用高通量 DNA Encoded Library 資料訓練模型，並讓 LLM agent 在數百萬分子中做可驗證的科學推理。

多數人一聽到 DNA Encoded Library（DEL）就搖頭，因為這種高通量蛋白質與小分子交互作用資料出了名的髒。但 Leash Bio 找到辦法把它洗乾淨到可以拿去做大規模建模，而他們最新的動作，是把這批資料變成 AI agent 的科學推理訓練場。

🤔 **DEL 為什麼讓人頭痛**

DEL 是一種能大量收集蛋白質與小分子交互作用數據的方法，但常見的問題是假訊號——很多時候抓到的其實是蛋白質結合到 DNA 本身，而不是結合到要測試的藥物分子。Leash 的作法是在每個分子上貼上幾十個 barcode，用來辨識並排除這類偽陽性結果。

🧩 **一場沒人贏過隨機猜測的 Kaggle 競賽**

Leash 辦過一場 Kaggle 競賽，用大約 40 億筆量測資料、吸引約 2,000 支隊伍參賽，結果是沒有任何隊伍在一個從未見過的化學庫上打贏隨機猜測——直接說明 protein-ligand binding 預測在業界仍未真正解決。素材也提到 Leash 原本暗自擔心 co-folding 技術會讓他們的方法過時。

🧩 **「Clever Hans in ChEMBL」：模型學到的是作者，不是化學**

團隊發現一件挺諷刺的事：模型可以單靠分子結構猜出這是哪位化學家合成的，而「這個分子是誰做的」這個資訊，預測活性的準確度幾乎跟分子結構本身一樣好。這等於揭露了像 ChEMBL 這類公開資料庫裡隱藏的資料洩漏問題——模型很可能不是在學化學，而是在學「認人」。

🧩 **Hermes 與 Breaking the Pocket**

Leash 用自家資料訓練出 Hermes 模型，在公開 benchmark 上追得上 Boltz 的表現，但素材也點出 Boltz 比較的 BRD4 分子其實早就出現在 PDB 資料庫裡，等於已經「看過答案」。更進一步，團隊發現 Hermes 其實是記住了蛋白質的「暱稱」，而不是真的學會 binding pocket，於是工程化大量蛋白質突變體來破解這個捷徑。另一個意外收穫是，像 Lumacaftor 的命中分子反而變成偵測蛋白質是否摺疊錯誤的指標。

🧩 **把分子推理場交給 LLM agent**

團隊最近打造了一個 agent sandbox，讓 LLM 用「plain English」討論 SAR（structure-activity relationship），在 650 萬個分子裡、只有 100 次嘗試的預算下尋找最好的 binder。這套 lab-in-the-loop 模擬環境後來發展成 Minos，團隊同步發布了 preprint、部落格文章與開放資料集。

💡 **Kosuri Paradox：資料都收集到了，為什麼還需要模型？**

素材提到的 Kosuri paradox 點出一個張力：當實驗本身已經能產出足夠大量的數據，模型存在的價值到底是什麼？從 Leash 的脈絡看，答案似乎是模型要把這些高通量數據轉成可泛化、可推理的知識，而不只是把資料庫當成查表工具。

📊 **從 DEL 命中到真實藥物開發的時間線**

素材提到在一個發炎（inflammation）相關計畫中，團隊從 DEL 命中分子到在小鼠身上取得不錯的 PKPD（藥物動力學／藥效學）結果，只花了六個月；文中也提到在 cytokine 靶點上，小分子藥丸相對於抗體藥物可能更具優勢的論點。

⚠️ **護城河與未解問題**

素材並未給出 Minos 模型的具體準確率或完整 benchmark 數字，對於「什麼能阻止資源更雄厚的實驗室靠規模超越 Leash」這個問題，也只提到 Ian Quigley 自己對「大規模平行純化」有一個尚未實現的期望，而非具體解法。

🎯 **實務啟示**

對做 AI x Bio 的工程師，這個案例給出一個清楚的心法：把你的問題對應成一個 combinatorial library 加上 next-generation sequencing 的 readout 方式；同時在訓練任何活性預測模型前，務必檢查資料裡是否藏著像「作者是誰」這種看似無關、實際上會被模型拿來走捷徑的隱藏特徵。

🔗 **來源**
- 標題：Lab-in-the-Loop at Compute Speed — Ian Quigley, Leash Bio
- 作者／機構：Latent Space（訪談對象：Ian Quigley, Leash Bio）
- 連結：https://www.latent.space/p/lab-in-the-loop-at-compute-speed

#LeashBio #DrugDiscovery #DNAEncodedLibrary #AIforScience #ProteinLigandBinding #ScientificRL #LLMAgent #ComputationalChemistry #Minos #Bioinformatics
