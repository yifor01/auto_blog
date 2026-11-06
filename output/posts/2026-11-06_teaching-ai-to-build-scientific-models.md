---
title: Teaching AI to build scientific models
source: Anthropic Research
url: https://www.anthropic.com/research/teaching-ai-to-build-scientific-models
model: claude-code/sonnet
generated_at: '2026-11-06T22:13:16.512226'
pinned: true
---

📌 【Anthropic 研究】AI 給你答案很容易，給你理解才難

TL;DR：ELLIS Institute Tübingen 研究者談 AI 如何加入科學建模的三個步驟，但重現數據不代表真正理解現實系統。

1951 年，劍橋大學的電腦故障了整整六個月。生理學家 Andrew Huxley 與同事 Alan Hodgkin 剛建好一組方程式，想描述魷魚神經細胞如何放電，卻只能用手搖式機械計算器硬算,花了超過三週。這個看似笨拙的故事,恰好道出科學建模裡最核心的難題：算出答案,和理解現象,是兩件不同的事。

🤔 **一個方程式用了 70 年都沒過時**

Hodgkin 與 Huxley 想理解神經細胞用來溝通的電位脈衝（action potential）。他們把細胞膜建模成一個電路，這部分有明確的生理依據；但其中一個變數必須乘上自己三次（也就是四次方）才能讓曲線真正貼合實測數據,當時他們並不知道原因，只是憑經驗猜測：這或許代表細胞膜上的閘門,需要多個帶電粒子同時就位才會打開。兩人後來因此獲得 1963 年諾貝爾生理學或醫學獎。數十年後，另一支團隊解出相關鉀離子通道蛋白質的結構，發現它確實由四個相同的部件圍著一個中央孔洞組成,印證了當年那個「猜測」。如同數學家 Richard Hamming 在 1962 年所說：「運算的目的是洞見，不是數字。」這個四次方的故事之所以重要，不是因為它讓模型更準,而是因為 Hodgkin 與 Huxley 知道「更簡單的版本行不通」,這正是洞見所在。單純重現數據是不夠的，因為任何數量的模型都可能做到同一件事；真正重要的是能不能對現實系統、乃至其他相似系統提出主張。

🧩 **科學建模的三個步驟**

作者指出，Hodgkin-Huxley 模型的建立方式可以拆成三步，大多數科學建模也都遵循類似流程：第一步是建構模型,決定模型由什麼組成、方程式該長什麼樣子（例如電路裡的膜與閘門,以及把變數升到四次方）;第二步是約束模型,調整模型裡可調的參數以貼合實測數據（例如閘門在不同電壓下的開合頻率）;第三步是詮釋模型,追問模型對真實系統說了什麼（例如四次方可能意味著閘門由四個部件組成）。實務上，科學家會不斷在這三步之間來回修正：數字對不上就回頭調整,詮釋說不通也要回頭檢視。

💡 **AI 進展最快的一步：約束模型**

Hodgkin 與 Huxley 當年靠眼力與直覺湊出一組數字，卻無法知道是否還有其他同樣能貼合數據、甚至更好的組合。作者用一個分帳的比喻說明這個問題：知道一桌晚餐總共 120 元,卻不知道誰點了什麼,可能是每人都點中價位的漢堡,也可能有人點了牛排和龍蝦、其他人喝湯,許多不同組合都能湊出同一個總額。神經細胞模型也是如此:不同的閘門參數組合可能產生幾乎相同的電活動。只秀出一組吻合良好的參數,會掩蓋掉所有其他同樣合理、卻可能帶來不同預測的組合。解法是貝氏推論（Bayesian inference）,找出所有「夠好」的參數組合，依據它們與數據的吻合度與先前知識，整理成一個機率分布。問題是，對複雜模型而言，窮舉每一種可能參數組合在計算上完全不可行,就像在分帳例子裡，問「A 點漢堡、B 點牛排,帳單會是多少」很容易,但反過來推敲有哪些組合能湊出同一個總額,人數與菜單選項一多就變得極其困難。模擬為本推論（simulation-based inference, SBI）用大量運算繞過這個難題：隨機挑參數、跑一次模型、記錄輸出,如此重複,對 Hodgkin-Huxley 這類模型可能要跑約 10 萬次，對更大更複雜的模型則要跑上百萬次,再用這些結果訓練一個神經網路，讓它學會「看到某個輸出,反推可能是哪個範圍的參數產生的」。SBI 唯一的要求,是你能跑得動這個模型:輸入一組參數，能得到你預期會看到的那種數據。

⚠️ **AI 給你模型,不等於給你理解**

作者特別強調：一個 AI 系統或許能在一個下午內找出像 Hodgkin-Huxley 那樣的方程式,甚至貼合數據更好,但光是把模型交給你並不等於給了理解。真正關鍵的，是知道這個模型的哪些特徵是它和其他「有效」模型共有的，哪些特徵又是它和「無效」模型的分界線,而不只是單純地重現一組觀測數據。

🎯 **實務啟示**

對投入科學 AI（AI for Science）的工程師與研究者來說，這篇文章提醒了一個容易被忽略的分野:AI 在「約束模型」（擬合參數)這一步已經靠 SBI 等方法大幅提升效率，但「建構模型」與「詮釋模型」這兩步,決定模型該長什麼樣、以及結果對真實世界意味著什麼,仍高度仰賴人類科學家的判斷與假設。當 exact Bayesian inference 在計算上不可行時，優先考慮 simulation-based inference 這類以模擬換取可行性的方法，會是務實的路徑。

🔗 **來源**
- 標題：Teaching AI to build scientific models
- 作者／機構：Jakob Macke、Daniel Gedon、Stefan Wahl（ELLIS Institute Tübingen / University of Tübingen），刊於 Anthropic Research
- 連結：https://www.anthropic.com/research/teaching-ai-to-build-scientific-models

#Anthropic #AIforScience #ScientificModeling #BayesianInference #SimulationBasedInference #Neuroscience #ComputationalBiology #MachineLearning #ELLISInstitute #ScientificDiscovery
