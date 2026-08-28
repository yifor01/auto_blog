---
title: What happens when information theory accounts for reasoning?
source: IBM Research
url: https://research.ibm.com/blog/information-theory-meaning?utm_medium=rss&utm_source=rss
model: claude-code/sonnet
generated_at: '2026-08-28T18:11:42.718934'
score: 77
---

📌 IBM 新論文：資訊理論該把「推理」算進去了

TL;DR：IBM 團隊發表 PNAS 論文，把「能推論出什麼」納入通訊效率的數學模型。

如果人類的科學知識即將全部消失，你只能留下一句話給後世，你會寫什麼？物理學家 Feynman 的答案是：「萬物皆由原子構成，這些小粒子不斷運動，靠近時互相吸引，擠壓在一起時則互相排斥。」這句話珍貴的地方,不是它包含多少字或符號,而是未來的科學家能從這一句話推導出多少知識。這正是 IBM Research 最新論文想要正式量化的東西。

🤔 **Shannon 的簡化：只管怎麼傳，不管什麼意思**

1948 年，Claude Shannon 提出了一個影響深遠的簡化:把訊息的「意義」和「如何有效傳輸」分開處理。這個抽象化造就了現代資訊理論,無論訊息是一張照片、一通電話、一篇論文,還是一個大型語言模型的訓練資料,Shannon 的框架只關心資訊如何被表示、壓縮與可靠傳輸。這套方法成功的原因是通訊網路不需要理解自己在傳什麼,網際網路不在乎一個封包裝的是救命的醫療診斷,還是一張貓的照片,它只負責搬動位元。但通訊兩端的人類,直覺上都知道不是每個位元的價值都相等:一個故障感測器產生的位元可能毫無價值,而一個可靠的防撞系統送出「剎車」訊號的一個位元,卻可能極其重要。差別就在於接收者能從這個資訊推論出什麼。

🧩 **給接收端加上推理能力**

由 IBM Research 的 Luis Lastras、Jonathan Lenchner、Barry Trager、Mark Squillante、Chai Wah Wu、Ronald Fagin,以及合作者 Wojciech Szpankowski 與 Alexander Gray 共同發表於《美國國家科學院院刊》（PNAS）的這篇論文，把 Shannon 的經典「發送者—接收者」模型延伸,讓接收端具備邏輯推理能力。這個模型不只計算直接傳輸的資訊量,還把接收者能從收到的內容進一步「推論」出的額外知識也算進去。換句話說,一則訊息的價值不只取決於它說了什麼,也取決於它讓人能推論出什麼。為了在數學上捕捉這個概念,團隊推導出一個新的量,稱為「邏輯語意熵」（logical semantic entropy），用來定義在具備推理能力的情況下,通訊的根本極限。

📊 **三個挑戰直覺的發現**

論文提出了三個顛覆常見直覺的結果。第一個是「無需知道」（No Need to Know）:即使發送者不清楚接收者已經知道什麼,通訊的根本極限幾乎不會改變。這出乎意料,因為這套通訊機制本質上會用有損壓縮丟掉邏輯推導不必要的細節,而在這類情境下,通常知道對方已經懂什麼會有助於省下資料量。

第二個是「少即是多」（Less Is More）的悖論。借用密碼學理論中常見的 Alice 與 Bob 這兩個虛構角色:如果 Alice 只想讓 Bob 學到她知識中的某個特定子集,同時盡量用最少的位元,結果最有效率的策略,反而會教給 Bob 比預期更多的東西。因為 Alice 用一套能同時應付多種情境的通用簡化模式來大幅減少傳輸量,而這種模式覆蓋的範圍太廣,分享其中一種,必然會洩漏比原本意圖更多的背景資訊,形成潛在的安全風險。

第三個結果關於「糾正錯誤信念」的成本。團隊用數學模型分析,當接收者持有與發送者事實直接矛盾的信念時,糾正這個錯誤所需的通訊成本,可能遠遠大於單純填補一個知識空白的成本。而且隨著接收者的錯誤信念變得越具體、越根深蒂固,糾正回正確答案所需的相對成本會趨近於無限大。

💡 **從個人研究到跨團隊合作**

這項研究對 Lastras 而言並非短期專案,而是他每週投入時間、長期在背景中進行的個人研究,持續了好幾年,試圖解決資訊理論早期就懸而未決的問題。隨著時間推進,團隊逐漸擴大,更多合作者深入數理邏輯領域,把這個問題探究得更深。

🎯 **實務啟示**

論文指出,現代 AI 系統不只需要處理資訊,還越來越依賴對資訊進行推理。Shannon 的原始框架仍是數位通訊的基礎,但作者認為,未來的智慧系統或許需要一套更豐富的理論,不只衡量資訊傳輸得多有效率,還要衡量理解這則資訊背後需要多少背景知識。對於正在設計知識檢索、上下文管理或 Agent 記憶系統的工程師而言,這篇論文提醒的重點是:糾正一個已經根深蒂固的錯誤信念,其代價可能遠高於單純補充一個空白,而追求「最省位元」的壓縮策略,也可能在無形中洩漏比預期更多的背景資訊。

🔗 **來源**
- 標題：What happens when information theory accounts for reasoning?
- 作者／機構：IBM Research
- 連結：https://research.ibm.com/blog/information-theory-meaning?utm_medium=rss&utm_source=rss

#InformationTheory #IBMResearch #Reasoning #Entropy #PNAS #ClaudeShannon #AI #KnowledgeRepresentation #Communication #TheoreticalCS
