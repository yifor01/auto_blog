---
title: AI researchers debate how close we are to recursive self-improvement
source: Dwarkesh
url: https://www.dwarkesh.com/p/john-beren-charlie
model: claude-code/sonnet
generated_at: '2026-09-11T19:52:03.894940'
score: 86
---

📌 三位前沿實驗室研究者交鋒：遞迴自我改進到底卡在哪？

TL;DR：Schulman、Millidge、O'Neill 三人辯論 AI 遞迴自我改進的技術瓶頸,對評估新模型的炒作週期很有參考價值。

如果到了 2036 年，世界上還沒有出現大量「瘋狂的超級智慧」，最可能的技術原因是什麼？在 Dwarkesh Patel 主持的這集訪談中，三位分別來自不同前沿實驗室的研究者，給出了不太一樣的答案。

🤔 **來賓陣容：三個「偏開放」實驗室的觀點**

這集邀請到 Zyphra CTO Beren Millidge、Thinking Machines 首席科學家（同時是 OpenAI 共同創辦人、曾主導促成 ChatGPT 誕生的 RLHF 工作）John Schulman，以及 Baseten 模型訓練負責人 Charlie O'Neill。開場問題刻意排除政治動盪、戰爭、AI 禁令等外部因素，只討論技術面：如果 2036 年沒有出現爆炸性的超級智慧，卡點會在哪裡？

💡 **Moravec 悖論式的落差,以及「一個月後就覺得它變笨」的循環**

一種可能性是類似 Moravec 悖論的情況重演：過去人們以為「如果 AI 能解出困難數學題、能下贏西洋棋，那就代表它很厲害」,結果模型真的解出這些題目後,實際影響力卻沒有想像中大。與談者提到,即便業界確實已經在 RL 中觀察到一定程度的泛化能力,但如果這種泛化極端困難,加上 continual learning 遲遲無法解決,模型可能會停留在「對任何被放進 benchmark 或環境裡的任務都表現優異」,卻始終存在某種 sim-to-real 落差,擋住了真正的突破。

另一個反覆出現的現象是：每次新模型發布,大家都會驚呼「這就是 AGI 了」,但用了一個月後又開始覺得它「變笨」,因為人類在某些領域仍有優勢,新模型會在某些面向追上,卻又在模型判斷力較弱、無法充分自我檢查的地方被卡住。即便模型寫程式碼的速度遠超人類,也不代表工程師的生產力會因此提升 100 倍——訪談中提到，目前研究與工程流程中仍存在足夠多的瓶頸，尚未出現爆發式的能力成長。

🧩 **快速起飛的邏輯,以及「下一個 Moore's Law 式的斷點」在哪**

支持快速起飛（fast takeoff）情境的論點是：一旦出現一個在 AI 研究能力上只比全人類強 0.1% 的代理,只要能平行跑上數十萬甚至數百萬個實例,並隨晶片變快而跑得更快,這個優勢就足以壓過其他所有瓶頸,最終觸發自我改進的快速起飛。

但另一種觀點則類比 Moore's Law：那條看似平滑的直線,背後其實是無數次離散的技術突破接力撐起來的。LLM 領域也發生過同樣的事——預訓練的 scaling law 遇到報酬遞減後,RL 被發現並解決了那次瓶頸,讓成長曲線得以延續。問題是,如果要延續下去還需要「下一次斷點式的突破」,那麼現有的 self-attention + RL + 規模化 RL 環境這套範式，本身是否有能力發現那個突破，仍是未知數。與談者也提出更根本的問題：如果現有方法離全域最優解太遠，即便持續投入再多 RSI 導向的 RL 訓練，也未必能自己發現下一個典範轉移，屆時就可能撞上成長曲線趨緩的瓶頸。

⚠️ **這是一場辯論,不是新研究結論**

需要強調的是,這集內容是三位研究者的觀點交流與辯論,三人對「多遠」「多難」的判斷並不完全一致,不代表任何單一實驗室的官方結論或新研究發現。

🎯 **實務啟示**

對工程師與研究者而言，這場對談提供了一個評估新模型發布時可以參照的心智模型：與其被單次 benchmark 突破沖昏頭，不如追問這次進步是否只是「延續現有曲線的又一次局部優化」，還是真正跨越了新的技術斷點。

🔗 **來源**
- 標題：AI researchers debate how close we are to recursive self-improvement
- 作者／機構：Dwarkesh Patel
- 連結：https://www.dwarkesh.com/p/john-beren-charlie

#RecursiveSelfImprovement #AGI #AIResearch #ReinforcementLearning #ScalingLaws #LLM #AITimelines #OpenAI #ThinkingMachines #Zyphra
