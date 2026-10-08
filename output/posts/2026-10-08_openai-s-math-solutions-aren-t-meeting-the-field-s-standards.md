---
title: OpenAI’s math solutions aren’t meeting the field’s standards yet
source: TechCrunch AI
url: https://techcrunch.com/2026/10/08/openais-math-solutions-arent-meeting-the-fields-standards-yet/
model: claude-code/sonnet
generated_at: '2026-10-08T22:29:15.595775'
score: 77
---

📌 OpenAI 一次發布 719 份數學證明，人類看懂了嗎？

TL;DR：OpenAI 大量發布數學難題解答，但僅一成附上思考過程，驗證流程仍有缺口。

當一家公司宣稱解開了世界上最難的數學問題之一，第一個該問的問題不是「答案對不對」，而是「有誰真的看懂了」。這正是這星期圍繞 OpenAI 數學證明發布的核心爭議。

🤔 為了避免重演爭議，結果仍未達標

本週 OpenAI 發布了數百份針對世界級難題的證明，並表示這次有諮詢一個由頂尖數學家組成的顧問團體，希望避免重演上一次模型解開長年未解問題時引發的爭議。但根據報導，OpenAI 在「確保人類能理解數學結果」這一項標準上仍未達標，而這一點格外重要，因為一篇新論文剛好指出，OpenAI 模型聲稱解開的一個百萬美元難題，其自然語言證明與正式形式化證明之間存在落差。

🧩 顧問團體訂出的準則,以及 OpenAI 做到哪些

這個諮詢團體名為 Advisory Group on Mathematics and Artificial Intelligence（AGMAI），由普林斯頓大學高等研究院主辦，成員為 9 位來自世界各地機構的知名研究者。AGMAI 在 9 月底發布了給前沿實驗室解數學題時應遵循的準則，並在針對這次證明發布的聲明中表示：「最終仍需由數學社群自行評估我們的建議被落實到什麼程度。」

AGMAI 提出的第一項要求,是「停止在專有模型上測試進階數學問題」——但 OpenAI 這次發布明確說明，它是用公開的研究難題來評估自家的專有模型。AGMAI 在被 TechCrunch 詢問是否能對這次發布做更完整評估時，並未回應。

OpenAI 確實遵循了部分原則，包括盡快公開結果，以及說明模型是如何得出結論的；但並非全部都做到：719 份手稿中，只有 10 份公開了模型的 chain-of-thought（推理過程）。AGMAI 建議對於人類難以理解的證明應該進行形式化（formalization）處理，但 OpenAI 公開的證明中有 42% 並未經過這道流程。整體而言，報導指出,目前仍不清楚 OpenAI 是否真的在落實 AGMAI 要求的「為確保後續人類理解而負起責任」這項原則；AGMAI 也建議 OpenAI 應該資助負責讓這些解答變得真正有意義的人類數學家的工作。

著名數學家 Terence Tao 在發布後於社群媒體上批評：「問題正在被一群對這個領域本身毫無興趣的 AI 操作者自主解決,一旦達成最初目標就不再關心，他們也沒有深入理解 AI 輸出的內容到足以回答相關問題、進行演講，或與領域內其他人互動的程度。」

📊 自然語言與形式化證明之間的「翻譯落差」

這個問題在本週另一篇論文中有具體案例：劍橋大學與倫敦國王學院的數學家發表論文，質疑前沿實驗室目前處理這類挑戰的方式。AI 模型解數學題時,通常先產生一段「自然語言」說明，再嘗試把這個結果轉寫成 Lean（一種透過編譯成程式碼來確認證明正確性的程式語言）。這篇論文記錄了,OpenAI 針對一個從 Navier-Stokes 方程式（描述流體複雜行為的方程式）衍生出的問題所提出的解答中,自然語言證明與背後 Lean 程式碼之間,至少存在兩處不一致。這些落差不必然代表兩邊的證明都是錯的，但確實讓人質疑,是否能單純信任模型自行把自然語言證明形式化,而不需要人類介入檢查。這也是為什麼 AGMAI 要求提供「連結自然語言與形式化成果的機器可讀 metadata」,而 OpenAI 這次的發布並未提供這項資訊。「鑑於這篇論文指出的誤譯現象,OpenAI 與其他實驗室透過自動形式化產生的 Lean 證明,以及對應的自然語言證明,都不應該在未經過與其他證明相同的同行審查與檢視之前被直接信任，」該論文作者總結道。

💡 「解完就跑」與真正的數學研究有什麼不同

數學家強調,當人類發現新結果時,他們會對結果負責,透過論文、演講、研討會與領域內其他人互動,這個過程能增進大家對解答的理解、找出可以遷移到其他問題的策略,並讓新知識能應用到實務領域。哈佛大學數學教授 Melanie Wood 對 TechCrunch 表示：「在發布的那一刻,人類並不理解這些結果,接下來的工作才剛開始。」

⚠️ 限制

目前這些落差並不足以推翻 OpenAI 聲稱的解答，報導與論文呈現的是流程與驗證標準上的缺口，而非證明本身被證實有誤。

🎯 實務啟示

如果你的工作涉及用 LLM 產生 Lean 或其他形式化證明,不要把「程式碼編譯通過」直接等同於「自然語言論證正確」,兩者之間的翻譯本身就可能出錯,需要額外的人工比對與同行審查流程,才能真正信任最終結果。

🔗 來源
- 標題：OpenAI's math solutions aren't meeting the field's standards yet
- 作者／機構：Tim Fernholz（TechCrunch AI）
- 連結：https://techcrunch.com/2026/10/08/openais-math-solutions-arent-meeting-the-fields-standards-yet/

#OpenAI #MathAI #Lean #FormalVerification #AIResearch #TerenceTao #AutoFormalization #AGMAI #NavierStokes #AIAndMathematics
