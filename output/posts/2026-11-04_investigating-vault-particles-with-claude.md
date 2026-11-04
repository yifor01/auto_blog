---
title: Investigating vault particles with Claude
source: Anthropic Research
url: https://www.anthropic.com/research/investigating-vault-particles-with-claude
model: claude-code/sonnet
generated_at: '2026-11-04T22:44:59.431413'
pinned: true
---

📌 【Anthropic 生物實驗室】Claude 助攻，找到細菌版神秘「保險箱」蛋白結構

TL;DR：Anthropic 用 Claude 貫穿整個研究流程，在原核生物與噬菌體中發現能組裝成完整 vault 粒子的蛋白，並解出其 3D 結構。

1986 年就被發現的 vault 粒子，體積是核糖體的三倍大，卻足足讓科學家摸不透其功能近四十年。這次 Anthropic 的生物研究團隊不是解開了這個謎題,而是讓謎題變得更大、更有趣。

🤔 **一個存在近 40 年卻沒人懂的巨型蛋白殼**

Vault 粒子是幾乎存在於人體所有細胞中的中空蛋白殼，由 Leonard Rome 與 Nancy Kedersha 於 1986 年發現，因形狀類似教堂的穹頂拱頂而得名。人類的 vault 由 78 個 major vault protein 拷貝組成（每半邊 39 個），分布在從黏菌到人類的大部分真核生物譜系中。研究者曾提出多種假說，包括在細胞核與細胞質之間運輸分子、保護細胞抵抗癌症藥物等毒性化合物、支援先天免疫，但這些說法都未被確認。更讓人困惑的是，缺乏 vault 的小鼠依然能存活，暗示 vault 可能只在特定環境條件下才發揮作用。問題是：如果沒有重要功能，演化為何會保留這麼龐大的結構？

🧩 **把目標轉向細菌與噬菌體，Claude 接手每一步**

Anthropic 團隊的策略是找到 vault 在原核生物（如細菌）中的親緣版本,因為細菌生長快速,更容易研究其來源、基本結構與內容物。團隊發現,包括原核生物與感染它們的噬菌體在內,樹狀演化圖上有更多 vault 蛋白能組裝成完整的 vault-like 粒子,這是先前未曾被證實的現象。

在這個過程中，Claude 被用於研究的每一個環節：搜尋蛋白質序列資料庫、設計 DNA 構建體（constructs）、最佳化粒子分離方法，以及處理 cryo-EM（冷凍電子顯微鏡）取得的數據。團隊表示，傳統上需要三天的 vault 純化流程，在 Claude 協助下約 90 分鐘就完成，第一個結構模型在 34 小時後就出爐，而這在以往預估需要花上數週時間。

📊 **96 個蛋白拷貝、更圓更大的細菌版 vault**

團隊透過 cryo-EM 解出了一個來自噬菌體的 vault 結構，這個 vault 建構在被噬菌體感染的細菌體內。它由 96 個單一蛋白（team 稱之為 L05）拷貝組成（每半邊 48 個），比人類版本的 78 個拷貝更多，總質量約 9.5 百萬道爾頓（megadalton）。

這個噬菌體衍生的 vault 比人類版本更短更寬：長約 54 奈米、寬約 45 奈米，相較人類的 67 x 40 奈米。雖然較短，但因為形狀更接近球形，內部容積反而多出約 25%。組成外壁的蛋白鏈由 7 個重複片段首尾相接構成，而人類版本是 9 個；其端蓋也更平坦。這是目前已知原核生物中最大的蛋白殼之一。

結構中一個有趣的細節是端蓋如何封閉：48 個拷貝組成的外壁要朝兩極收窄，是以三階段、如階梯式穹頂的方式完成——每三個相鄰拷貝中，一個停在第一階，一個停在第二階，一個則延伸到頂點。這三個拷貝沿著壁面是相同的,但在端蓋處呈現不同構形（conformation）。

團隊接著與 Claude 合作，製作了 15 個經修改的蛋白版本，大多是改變相鄰拷貝相互接觸處的序列。結果發現，端蓋附近某些單一改變就足以阻止外殼封閉，取而代之的是開放、玫瑰花狀（rosette-like）的粒子，證明這個區域對外殼密封是必要的。團隊也嘗試讓 vault 變得更大：原本外壁由 7 個重複片段構成，當他們複製其中兩段，讓蛋白擁有 9 個片段（與人類 vault 相同數量）時，組裝出的 vault 粒子更大，內部容積增加約 20%。

⚠️ **結構出來了，功能仍是未解之謎**

即便取得了結構上的進展，vault 的功能仍未被確定。團隊邀請 vault 共同發現者 Leonard Rome 擔任研究顧問，他看到結構後表示：「搞清楚 vault 的功能依然極具挑戰性。我很高興 Anthropic 掌握了這麼多好的數據，現在,其他人將會投入這個問題……Anthropic 這些發現的廣度,意味著這將是一個複雜的功能,也會是一段有趣的旅程。」

💡 **從免疫系統到奈米技術的潛在啟發**

文中提到，研究細菌版的人類蛋白過去曾帶來重要發現,例如細菌版的 cGAS–STING signaling、gasdermins 與 viperins，揭示了人類免疫防禦機制的微生物起源，但這些案例中蛋白在人類體內的功能早已明確。vault 的情況不同,其人類功能仍未知,因此原核生物中的親緣版本有機會反過來幫助揭露答案。團隊也指出,這類研究結果有助於理解這類複合體如何組裝,並暗示它們未來或可被改造用於生物技術,例如作為遞送酵素的奈米膠囊（nanocapsule）。

🎯 **實務啟示**

這項研究展示了一種可複製的 AI 輔助科研模式：讓 Claude 承擔文獻與序列資料庫搜尋、分子生物學設計、實驗流程最佳化,到顯微影像數據處理的全流程協作,把原本要耗時數週的結構解析壓縮到一兩天內完成。對於做生物資訊或濕實驗室自動化的工程師而言,這提供了一個值得參考的「AI 全流程嵌入」案例,而非僅將 AI 用於單點任務。

🔗 **來源**
- 標題：Investigating vault particles with Claude
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/research/investigating-vault-particles-with-claude

#Anthropic #Claude #AIforScience #StructuralBiology #CryoEM #ProteinStructure #Bioinformatics #MolecularBiology #VaultParticles #AIResearch
