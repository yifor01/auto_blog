---
title: Qwen 3.8 27B on my laptop can interpret model weights, too
source: Simon Willison
url: https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/
model: claude-code/sonnet
generated_at: '2026-11-03T22:31:22.598134'
score: 97
---

📌 27B 模型在筆電上也看得懂權重

TL;DR：Simon Willison 用筆電上的 Qwen 3.8 27B 重現了讀權重猜遊戲的實驗。

前一天才爆紅的論文說，前沿模型 GPT-6 Astra 光看原始權重就能猜出一個網路是在玩什麼遊戲；Simon Willison 想知道，換成一顆只有 17GB、能塞進自己筆電的 27B 模型，還做得到嗎？

🤔 一篇被稱為「論文形狀」的部落格文章

引發討論的是 Rikiya Takehi、Jayden Teoh、Alex Zhang 與 Omar Khattab 合寫的《Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights》，作者自己把它定位成「部落格文章」，但內容長得就像一篇論文。文中最受矚目的發現是：GPT-6 Astra 光看原始權重就能判斷一個網路被訓練來做什麼，甚至能在不寫訓練迴圈、不用梯度的情況下，直接編輯 Qwen3.5-0.8B 0.016% 的權重，讓 MATH-500 分數從 7.9% 衝到 48.1%，IFEval 也提升 3 倍。Simon 指出，這篇文章其實把兩個應該分開討論的能力混在一起談：一個是「完全不用工具，光靠推理讀懂權重」；另一個是「給模型工具之後，它能多好地去更新、改善其他模型的權重」。他選擇聚焦在前者，也就是他認為更有趣的部分。

🧩 把權重貼進 prompt，讓本地模型「用推理」猜遊戲

論文附帶的 GitHub repo（RikiyaT/lm_understand-logs）公開了實驗用的 prompt：四個結構完全相同的策略網路，分別用強化學習訓練來玩簡化成 10x10 網格版本的 Breakout、Pong、Pac-Man 與 Freeway，然後把其中一個網路的權重（一串浮點數字）貼進去，問模型：「這個網路是被訓練來玩哪個遊戲？你沒有任何工具，不能執行程式碼、不能計算，只能憑這次回應作答。」Simon 用自己的 llm 工具搭配 -f/--fragment 參數直接把 GitHub 上的 prompt 當輸入，先用 OpenRouter 上的 Kimi K3.1 Pro 試跑，花了 9 分 41 秒、19,493 個推理 token，成功猜出 Breakout。

📊 筆電上的 Qwen 答對三題，敗在冷門的 Freeway

真正的主角是 Simon 日常在筆電上用的 Qwen 3.8 27B（17GB 模型檔，透過 LM Studio 載入，需要把 context window 從預設的 8192 調大，否則會報錯）。結果相當令人意外：

- Pac-Man 風格遊戲：46 分 12 秒、43,506 個推理 token 後，正確判斷出「agent 在 8x8 迷宮中移動、收集獎勵格、避開移動中的鬼魂」。
- Pong：1 小時 4 分 54 秒後，正確認出「agent 控制右側的垂直擋板去接球」。
- Breakout：52 分 25 秒後，正確認出「底部擋板接球、打上方磚塊」的 Arkanoid 式玩法。
- Freeway：這題失敗了，Qwen 判斷成「類 Pac-Man 的四方向移動遊戲」。Simon 認為這不意外，因為 Freeway 是一款相對冷門的 1981 年 Atari 2600 遊戲，熟悉度明顯低於前三款經典遊戲。

Simon 也分享了部分推理過程節錄，內容相當破碎、充滿對權重數值逐一比對的喃喃自語，他形容「幾乎讀不懂」，但認為一個拿著紙筆、足夠有耐心的人類，理論上也能靠同樣方式推理出答案。

💡 熟悉圈子裡出現的不同聲音

Simon 提到，spaCy 作者 Matthew Honnibal 認為這篇論文把「完全不用工具讀權重」和「用工具編輯權重」兩件事混為一談，說法有誤導之嫌；Sean Goedecke 則拆解了 Qwen3.5-0.8B 那個修權重的例子，指出 Astra 走的步驟其實就是一個人類 ML 研究員會採用的分析流程。Simon 自己的結論也相對保守：這確實是一篇有趣的研究，但他還沒準備好宣稱「程式碼時代要結束了，未來會變成由難以理解的機器以難以理解的方式編輯自己的權重」。

🎯 實務啟示

這次本地複現最實際的意義在於：這種「讀權重猜行為」的能力並非只存在於像 GPT-6 Astra 這樣的頂級閉源模型，一顆能在消費級筆電跑起來的 27B 模型，配合足夠長的推理（本例動輒 40 分鐘到超過 1 小時、數萬個推理 token），也能做到類似的事。如果想親自驗證這類說法，原始論文的 prompt 和權重資料都已公開在 GitHub 上，搭配像 llm 這樣的 CLI 工具就能直接重現，不需要仰賴他人的報告。

🔗 來源
- 標題：Qwen 3.8 27B on my laptop can interpret model weights, too
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/

#WeightSpaceProgramming #Qwen #LLM #LocalLLM #Interpretability #LMStudio #OpenSourceAI #ReasoningModels #AIResearch #MachineLearning
