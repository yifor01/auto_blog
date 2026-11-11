---
title: Qwen 3.8 27B on my laptop can interpret model weights, too
source: Simon Willison
url: https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/
model: claude-code/sonnet
generated_at: '2026-11-11T23:46:32.595684'
score: 101
---

📌 27B 小模型在筆電上，也能「讀懂」神經網路權重

TL;DR：Simon Willison 用筆電跑 Qwen 3.8 27B，複現「純靠看權重猜遊戲」的實驗。

🎣 給一個模型一堆浮點數，不給任何工具、不能執行程式碼，它居然能從這堆數字裡看出「這是一個被訓練來玩 Pong 的神經網路」——這正是最近一篇論文引發討論的原因，Simon Willison 決定在自己 17GB 的筆電模型上親自試一次。

**🤔 LLM 能否純靠權重讀懂一個模型在做什麼**

這篇論文《Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights》由 Rikiya Takehi、Jayden Teoh、Alex Zhang、Omar Khattab 發表（作者自稱是部落格文章，但內容具有論文的結構）。論文發現前沿模型，特別是 GPT-6 Astra，能夠解讀甚至修改一個機器學習模型的原始權重，也就是把模型權重當成一段由浮點數組成的文字來處理。論文摘要指出，GPT-6 Astra 光靠看原始權重就能判斷一個網路被訓練來做什麼；在沒有任何環境回饋的情況下，它能從零寫出小型的 game-playing 網路，表現超越用 PPO 訓練一億步的網路。論文作者把這種「LLM 分析並修改模型權重」的能力稱為 Weight-Space Programming。

論文把這個能力拆成兩個問題，Willison 認為值得分開看待：第一是模型不靠工具、不執行程式碼，單純靠推理理解權重的能力；第二是模型在有工具（能寫程式、能跑程式碼）輔助下，修改並改善其他模型的能力。spaCy 作者 Matthew Honnibal 認為論文把這兩者混為一談有誤導之嫌，Sean Goedecke 也拆解過論文中「修改 Qwen3.5-0.8B 權重」的示範，指出那其實是照著人類 ML 研究員會採取的步驟在做。Willison 選擇聚焦在第一個「不靠工具」的問題，認為這部分更值得關注。

**🧩 讓模型只看權重猜遊戲**

論文的第一個實驗訓練了四個神經網路，分別用強化學習在簡化版 10x10 網格上玩四款經典遊戲：Breakout、Pong、Pac-Man、Freeway（1981 年的 Atari 2600 遊戲）。接著把這些 policy network 的權重（一串浮點數）連同題目一起餵給 LLM：下面的權重屬於一個用強化學習訓練來玩網格遊戲的 policy network，請只靠權重推理判斷它是哪款遊戲，不能用任何工具，只有一次回答機會。論文的 GitHub repo（RikiyaT/lm_understand-logs）公開了每款遊戲對應的 prompt，Willison 確認過，除了權重數字本身，四份 prompt 的其他文字完全相同。

論文摘要另外提到一個更進一步的例子：在要求下把 Qwen3.5-0.8B 變得更擅長數學、且不能用 gradient 的情況下，GPT-6 Astra 找出了 Qwen 自己 model card 裡提過的一個會導致推理迴圈（reasoning loops）的權重問題，直接原生編輯了其中 0.016% 的權重修正它。用同樣的取樣設定，這次修正讓 MATH-500 的分數從 7.9% 提升到 48.1%，而且還能泛化到 instruction following 任務上，把 IFEval 分數拉高到原本的 3 倍。整個過程中 Astra 都沒有被允許寫訓練迴圈，完全靠推理判斷神經網路每一部分在算什麼、該算什麼，再據此修改權重。

**📊 Willison 在自己筆電上的複現結果**

Willison 用的是 17GB 版本的 Qwen 3.8 27B，在 LM Studio 上跑，預設 8192 context window 會報錯，需要調大 context 才能跑。他用 `llm` 工具的 `-f/--fragment` 選項直接餵論文 GitHub repo 上公開的 prompt。對照組用 `llm-openrouter` 跑 Kimi K3.1 Pro，在 9 分 41 秒、19,493 個推理 token 後正確猜出 Breakout。

Qwen 3.8 27B 在筆電上的結果：

| 測試遊戲 | 判斷結果 | 耗時 | 推理 token 數 |
|---|---|---|---|
| Pac-Man | 正確（描述為 8x8 迷宮、收集獎勵、避開移動物件） | 46 分 12 秒 | 43,506 |
| Pong | 正確（描述為右側垂直球拍接球） | 1 小時 4 分 54 秒 | 未提供 |
| Breakout | 正確（描述為底部球拍打磚塊） | 52 分 25 秒 | 未提供 |
| Freeway | 錯誤（誤判為類 Pac-Man 的四方向移動遊戲） | 未提供 | 未提供 |

三款比較知名的遊戲都被正確認出，唯獨相對冷門的 Freeway 猜錯了。Willison 也貼出推理過程的片段，內容大致是模型逐一檢視某些 channel、某些 row/col 座標的數值大小，嘗試拼湊出 agent 位置與物件排列，讀起來幾乎像天書。

**💡 令人印象深刻，但不是黑箱魔法**

Willison 的評論很中性：這確實令人印象深刻，但他認為一個經驗豐富、拿著筆記本和紙筆、肯花時間的人類，應該也能靠同樣的推理路徑得出答案。換句話說，這個能力展示的是 LLM 推理能力的延伸應用，而不是什麼超越人類理解範疇的黑箱魔法。他也點出網路上部分延伸討論（暗示「程式碼時代即將結束」）並不成立，至少以目前觀察到的現象還沒到那個程度。

**⚠️ 限制**

Qwen 3.8 27B 在四款遊戲裡猜錯了一款（Freeway），顯示這種「純靠權重推理」的能力在遊戲本身較冷門、特徵不明顯時會失效；完成一次判斷動輒要花 46 分鐘到超過 1 小時、數萬個推理 token，代表這目前更像是能力展示，而非能實際拿來用的工具。論文把「不靠工具純推理」和「有工具輔助編輯其他模型權重」兩種能力放在一起討論，也已被外部評論指出有混淆之嫌。

**🎯 實務啟示**

如果想自己驗證這類「模型理解模型」的宣稱，這是很好的切入點：論文作者已把 prompt 和訓練好的權重公開在 GitHub 上，搭配 `llm` 工具的 `-f` 參數，任何人都能在自己的機器或透過 OpenRouter 重跑一次，不需要額外架設實驗環境。對於評估「AI 能否理解 AI」這類高討論度的研究結果，親自動手重現往往比看二手摘要更能判斷其含金量。

🔗 來源
- 標題：Qwen 3.8 27B on my laptop can interpret model weights, too
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/

#LLM #WeightSpaceProgramming #Interpretability #Qwen #LocalLLM #AIResearch #MachineLearning #ModelWeights #ReinforcementLearning #SimonWillison
