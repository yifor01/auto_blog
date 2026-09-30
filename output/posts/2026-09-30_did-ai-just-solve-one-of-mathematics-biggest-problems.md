---
title: Did AI Just Solve One of Mathematics’ Biggest Problems?
source: KDnuggets
url: https://www.kdnuggets.com/did-ai-just-solve-one-of-mathematics-biggest-problems
model: claude-code/sonnet
generated_at: '2026-09-30T21:41:34.935082'
score: 95
---

📌 OpenAI萬人Agent提解答，卻引來一場署名爭議

TL;DR：OpenAI萬人Agent提解答，卻引來一場署名爭議。

88小時、一萬個並行Agent、1300億個輸出token，這是OpenAI用來攻克千禧年大獎難題之一Navier-Stokes方程式的規模。故事聽起來像是AI自主解題的完美案例，但攤開細節後，事情遠比新聞標題複雜。

🤔 背景：兩位人類數學家先行一步

OpenAI宣布內部AI系統針對Navier-Stokes存在性與光滑性問題（Millennium Prize Problems之一）提出了一個解答。更精確地說，系統針對帶有光滑外力的三維Navier-Stokes方程式，建構出一個有限時間內的奇異點（finite-time singularity），這是Clay數學研究所官方問題定義允許的其中一條路徑，並沒有解決更廣為人知的「無外力方程式是否始終保持光滑」這個問題。在OpenAI啟動這一萬個Agent之前，紐約大學的Tristan Buckmaster與任職於Anthropic的Levent Alpöge，已經在相關的流體力學問題上取得重要進展。他們同樣借助AI工具，包括Claude與OpenAI Codex，並用Lean將結果做形式化驗證，成果是針對帶光滑外力的三維不可壓縮Euler方程式建構出有限時間的爆破解，並未解出Navier-Stokes，但把相關領域向前推進了一大步。

根據OpenAI的說法，2026年9月1日，公司聽到「兩個千禧年大獎問題已被解出」的傳聞，加上內部新訓練模型展現的強勁結果，促使他們把系統套用到其餘尚未解決的千禧年問題上逐一測試。後來OpenAI才意識到，那些傳聞指的就是Buckmaster與Alpöge的工作。也就是說，OpenAI並非憑空選中Navier-Stokes並從零解出，而是自家的Euler成果，讓公司決定把資源集中投入到Navier-Stokes上。

🧩 方法或架構：把一萬個Agent變成一座虛擬研究室

OpenAI的做法是打造一個巨大的虛擬研究團隊：把Agent分成多個小組，各組可以互相溝通、執行程式碼，並存取一份快取版本的網際網路，不同小組探索不同的數學路徑。一開始，近100個Agent花了約50小時研究一個Euler相關問題，並產出一個被OpenAI認為有潛力的結果。到這個階段，OpenAI把原本分散在其他千禧年問題上的Agent集中轉向Navier-Stokes，同時開始在小組之間分享有用的發現，OpenAI稱之為「cross-pollination（交叉授粉）」：Codex負責彙整不同Agent小組產出的中間成果，再把這些發現回饋進後續的提示詞中。最終，這次成功的嘗試動用了大約1萬個並行Agent，累積270萬則訊息，輸出量約1300億token，在實驗開始後約88小時得出提議解答，接著又花17小時完成Lean形式化與驗證。

💡 深入分析：資料來源疑雲與署名之爭

結果公布後，Buckmaster提出一個尷尬的問題。他表示自己與Alpöge在做研究期間曾把研究草稿貼進Codex，因此想知道OpenAI的新模型是否曾被訓練於、或存取過那些對話紀錄。根據ABC News報導，Buckmaster說他一開始被告知模型不會「查閱」使用者資料，但當他特別追問是否用於訓練時，並未立刻得到答案。Buckmaster強調自己並未指控OpenAI，只是表示他不知道對方的模型做了什麼、或是怎麼做的，也不確定自己的資料是否被使用。

OpenAI事後調查，並在報告更新中表示，Buckmaster過去兩個月在Codex裡輸入的提示詞，不可能以任何方式影響系統，包括透過訓練；公司也表示研究人員與Agent在成果公開前，並未看過Buckmaster與Alpöge尚未發表的研究內容。就現有證據而言，並沒有跡象顯示OpenAI訓練了對方未發表的證明，或抄襲了對方的私人研究。

接著浮現的是署名爭議。目前有兩份獨立成果：Buckmaster與Alpöge的Euler研究，以及OpenAI的Navier-Stokes結果。根據Buckmaster的說法，OpenAI研究員Sébastien Bubeck提出兩個方案：一是讓Buckmaster與Alpöge先發表自己的Euler成果，OpenAI再發布Navier-Stokes結果；另一個較具爭議的方案，是讓Buckmaster撰寫一篇論文來呈現OpenAI的Navier-Stokes證明，並明確標註是由OpenAI的模型生成，但Alpöge不會被列入，理由是他任職於Anthropic。Buckmaster拒絕了這個提案。Bubeck後來澄清，他當時是提議由Buckmaster領銜、重新撰寫呈現OpenAI證明的論文，而他認為由一名Anthropic員工來執筆OpenAI的成果並不恰當；他也強調自己從未提議把Alpöge從兩人自己的Euler論文中移除。

⚠️ 限制

這個結果只解決了Clay數學研究所問題定義中「帶外力」的其中一種路徑，並未回答外界更熟悉的「無外力方程式是否恆保持光滑」這個核心問題。整起事件也暴露出學術發表制度的尷尬之處：當人類建立了周邊理論、AI工具參與了研究過程、另一個AI系統產出最終證明，而人類仍需負責詮釋與發表時，功勞究竟該算在誰頭上，目前並沒有現成答案。Clay數學研究所僅表示Navier-Stokes問題「看來已被解決」，但同時強調評估結果與認定貢獻仍需要時間。

🎯 實務啟示

對工程師與研究者而言，這個案例真正值得注意的，或許不是「AI變成數學天才」，而是它展示了一種新的研究工作模式：把大量Agent分組、平行探索不同路徑、淘汰失敗方向、並把小組間的中間成果交叉回饋，能把原本可能耗時數月甚至數年的研究壓縮到幾天內完成。這也提醒任何在建構multi-agent系統的人：跨團隊、跨Agent的知識回饋機制，可能比單一Agent的推理能力更關鍵。

🔗 來源
- 標題：Did AI Just Solve One of Mathematics' Biggest Problems?
- 作者／機構：Abid Ali Awan／KDnuggets
- 連結：https://www.kdnuggets.com/did-ai-just-solve-one-of-mathematics-biggest-problems

#OpenAI #NavierStokes #AIforMath #MultiAgent #MillenniumPrize #AIResearch #Lean #Anthropic #MathAI #AgentSystems
