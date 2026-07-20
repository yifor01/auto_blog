---
title: Loop the Loopies!
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.16051
score: 93
model: tencent/hy3:free
generated_at: '2026-07-20T08:52:52.338466'
---

📌 【HuggingFace Daily Papers】Loopie：迄今最強的迴圈 Transformer 登場

TL;DR：Loopie 以迴圈 Transformer + MoE 架構，在相同運算預算下大幅超越 vanilla 基線。

長期以來，looped Transformer 面臨一個根本難題：若預訓練運算增加 N 倍，通常把引數量放大 N 倍的效果，會比把同一個模型迴圈 N 次來得好。這篇論文提出的 Loopie 正是為瞭解決這個痛點。

🤔 **迴圈 Transformer 的老問題：迴圈不如放大引數**

過去研究指出，給定 N 倍預訓練運算，直接將模型引數數量乘上 N，往往優於把模型 loop N 次。這讓 looped Transformer 在擴充套件效率上一直處於劣勢。

🧩 **Loopie 系列：MoE 架構的兩款迴圈模型**

作者提出 Loopie，號稱目前最強的 looped Transformer。Loopie 系列包含兩個 Mixture-of-Experts (MoE) 模型：
- 20B 引數模型，啟用引數為 2B
- 6B 引數模型，啟用引數為 0.6B

README／摘要指出，Loopie 針對前述「迴圈不如放大引數」的挑戰提出對應設計，但未詳述具體架構細節。

📊 **相同運算預算下，顯著超越 vanilla 基線**

大規模消融研究（ablation studies）中，包含與一個 vanilla 30B-A3B 模型對比。結果顯示，Loopie 在相同的 compute budget 下，大幅優於 vanilla Transformer 基線。摘要未提供具體數值或指標。

💡 **新型後訓練流程賦予強推理能力**

除了預訓練上的突破，作者宣稱設計了一條新穎的 post-training pipeline，讓 Loopie 具備強大的推理能力。在 2025 年的 IMO（國際數學奧林匹亞）與 IPhO（國際物理奧林匹亞）中，Loopie 在無工具輔助下達到金牌等級表現。

🎯 **實務啟示**

對追求運算效率的團隊而言，Loopie 顯示 looped Transformer 搭配 MoE 有可能在相同預訓練成本下，追上甚至超越傳統放大引數的路線；其在奧林匹亞級推理的表現，也提示迴圈架構未必犧牲推理深度，值得後續追蹤開放權重與實測。

🔗 **來源**
- 標題：Loop the Loopies!
- 連結：https://huggingface.co/papers/2607.16051

#Loopie #LoopedTransformer #MixtureOfExperts #MoE #Transformer #Reasoning #Pretraining #IMOMedal #IPhO #HuggingFacePapers
