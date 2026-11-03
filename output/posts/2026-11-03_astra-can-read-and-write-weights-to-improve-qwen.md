---
title: Astra can read and write weights to improve Qwen
source: Hacker News
url: https://rikiyat.github.io/blog/weight-space-programming/
model: claude-code/sonnet
generated_at: '2026-11-03T22:31:22.597879'
score: 119
---

📌 Astra 不寫梯度，直接讀寫神經網路權重

TL;DR：GPT-6 Astra 靠推理讀寫權重，無需梯度就能修好模型。

如果有人把整個神經網路的權重，當成一串浮點數字拋給你，你能看出它是在玩 Breakout 還是 Pong 嗎？對人類來說幾乎不可能，但最新一批前沿 LLM 開始展現出這種能力。

🤔 從 Adam 到 LLM 親自讀權重

Deep learning 多年來仰賴像 Adam、Muon 這類符號化最佳化器，把人類簡化過的歸納偏好寫進演算法，再用梯度下降更新權重。文字類的工件（prompt、程式碼、訓練用的 harness 和超參數）近年已經可以交給 LLM 推理最佳化，但可微分的神經網路權重，過去被認為只能靠梯度下降這類演算法處理，畢竟沒有人能「手動」優化權重。這篇研究指出，這個界線正在被打破：LLM 開始能直接讀寫權重，作者稱之為 Weight-Space Programming。

🧩 不透過優化器，直接對權重下手

在 Weight-Space Programming 中，一個通用 LLM 直接讀取並寫入網路的權重，過程中不經過任何優化器，也不是梯度下降，有時甚至完全沒有環境回饋。LLM 的做法是用推理去理解網路每個部分在計算什麼、應該計算什麼，然後據此修改權重數值。整個過程不允許 Astra 自己寫訓練迴圈，一切都是基於對權重結構的理解進行的直接編輯。

📊 四個實驗，權重讀出遊戲、形狀與語言

- 用 PPO 訓練四個結構完全相同的策略網路，分別學會玩 Breakout、Pong、Pac-Man 與 Freeway。只把原始權重餵給 Astra，不給任何選項提示，Astra 四個都答對，甚至能指出 Breakout 網路第一層權重集中在底部一排，對應打磚塊的擋板位置。
- 換成三個獨立訓練的 DDPM diffusion model，分別生成圓形、三角形、正方形圖案。Astra 僅憑權重就說出每個模型在生成什麼形狀，方法是找出輸出層中每個隱藏單元對應畫出形狀邊緣的位置。有趣的是，它把所有形狀都判斷成「輪廓」而非實心圖案，顯示它確實是在讀權重的幾何結構，而不是真的跑了一次前向傳播。
- 為避免 Astra 靠讀首尾層「抄捷徑」，研究者訓練三個 7.2M 參數的小型語言模型，分別學習 Python 程式碼、羅馬字日文與英文的下一字元預測，再拿掉輸入層與輸出層，只留中間四個 transformer blocks 給 Astra 分析。即便模型完全無法被實際執行，Astra 仍兩次都答對三個模型各自訓練的語言，還精準找出每個模型裡的「copying head」（induction head，負責複製先前出現過的文字），且沒有誤判其他 head。它的推理路徑與 Elhage 等人提出的 induction head 分析方法不謀而合，而這個方法研究團隊從未告知過 Astra。
- 針對 Qwen3.5-0.8B，研究者要求 Astra 在不使用梯度的情況下讓模型的數學能力變好。Astra 在權重中找到造成推理迴圈的問題（這正是 Qwen 官方 model card 所警告過的缺陷），並只修改 0.016% 的權重來修正它。在相同取樣設定下，MATH-500 分數從 7.9% 跳到 48.1%，而且這個修正還能直接泛化到指令遵循任務，讓 IFEval 分數提升 3 倍。

⚠️ 作者自稱只是「早期火花」

研究團隊用的字眼是「sparks of Weight-Space Programming」，強調這些是早期、令人興奮的結果，而不是成熟的研究結論。Astra 在 Freeway 這類較冷門的遊戲上也可能判斷失誤，顯示這種能力目前仍與訓練資料或任務的「知名度」有關，而非穩定、可泛化的通用理解。

🎯 實務啟示

如果 LLM 真的能靠推理讀懂權重背後的語義結構，這對模型除錯、可解釋性研究，甚至模型編輯都是全新的工具箱。對工程師來說，值得關注的不是「梯度下降要被取代」，而是未來除了訓練迴圈外，可能多一條用自然語言 debug 模型內部缺陷的路徑。

🔗 來源
- 標題：Astra can read and write weights to improve Qwen（Sparks of Weight-Space Programming）
- 連結：https://rikiyat.github.io/blog/weight-space-programming/

#WeightSpaceProgramming #LLM #Interpretability #NeuralNetworks #AIResearch #ModelEditing #ReinforcementLearning #Qwen #MachineLearning #AIOptimization
