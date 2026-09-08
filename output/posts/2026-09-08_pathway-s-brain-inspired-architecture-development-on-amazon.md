---
title: Pathway’s brain-inspired architecture development on Amazon SageMaker HyperPod
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/pathways-brain-inspired-architecture-development-on-amazon-sagemaker-hyperpod/
model: claude-code/sonnet
generated_at: '2026-09-08T20:04:29.281960'
score: 100
---

📌 跳出 Transformer：Pathway 用類腦架構做潛空間推理

TL;DR：Pathway 的 BDH 架構捨棄 chain-of-thought，改在潛空間中直接推理，並用 AWS SageMaker HyperPod 訓練。

過去幾年 AI 的進步幾乎都靠堆模型規模、堆資料、堆 context 長度、堆推理算力。但如果推理這件事本身的做法就有問題呢？Pathway 給出的答案是：把推理挪出文字世界，放進潛空間（latent space）裡完成。

🤔 **Transformer 的舊帳：遺忘、重訓、黑盒**

AWS 這篇部落格指出，Transformer 架構過去十年大致維持不變，在訓練與推理上都存在明顯低效問題。訓練時，Transformer 難以在訓練資料之外做系統性泛化，尤其是長 chain-of-thought 推理任務，得靠海量資料與運算硬撐；其密集計算模式與完整反向傳播需求，讓運算成本隨模型規模近乎指數上升；模型微觀（神經元活化）與巨觀行為（為什麼給出這個答案）之間也缺乏清楚的對應關係。要更新模型知識往往得整個重訓或微調，還容易發生災難性遺忘。推理時，attention 機制的結構限制了可擴展性，即使搭配 Mixture of Experts，密集的活化模式仍會造成過多運算與記憶體頻寬消耗；固定的 context window 與不斷增長的 KV cache，也限制了可處理的序列長度；而 Transformer 封閉的內部狀態，讓人幾乎無法解讀或監控模型的推理過程，這在需要高度監管的產業中格外令人擔憂。

🧩 **BDH：神經元圖，透過稀疏、局部連結完成推理**

Pathway 的 BDH（Dragon Hatchling）架構，最初被設計成一個由神經元組成的圖，這些神經元透過稀疏、局部的互動彼此溝通，並以類似突觸的連結維持狀態。模型狀態能在不做測試時權重更新的情況下，於 context 中動態調整，推理的時間跨度也不再受限於固定大小的 context window，或是大量低效率的 chain-of-thought token。

BDH 採用 Hebbian learning（「一起激發的神經元會被連結在一起」）來實作 attention 機制，並只在單一神經元維度（n）上做縮放，降低了在多臺機器間分散 Transformer 運算時所面對的複雜度。與大腦類似，BDH 的神經元互動被設計成稀疏且局部，神經元之間的連結負責編碼記憶與推理功能；一般情況下，只有約 5% 的神經元處於活化狀態，這種稀疏活化特性讓每個推理步驟所需的運算量降低，進而帶來實際部署上的效能提升。BDH 透過線性機制在固定的高維狀態上實作 attention，因此在處理長序列時，不會像 Transformer 那樣因為 context 增長而暴增複雜度。由於模型狀態直接對應到神經元對之間的突觸連結，這也讓推理過程有了更高的可解讀性。

Pathway 進一步以 BDH 為基礎建構 BDH-CQ 推理系統，加入了 in-context learning 與潛空間迭代推理能力，用於視覺問題求解。其遞迴的潛空間運算支援高效的平行假設探索，讓不同的神經元群體代表同一個問題的不同候選解法，並能在固定記憶體成本下處理任意數量的示範樣本。BDH 架構與 PyTorch 相容，Pathway 使用 Amazon SageMaker HyperPod 來擴大訓練規模。

📊 **官方說法：150M 參數模型在 ARC-AGI-1 上的成本效率**

Pathway 執行長暨共同創辦人 Zuzanna Stamirowska 表示：「如今 AI 為推理付出高昂的 token 成本，但這個成本是架構造成的，不是智慧本身的必然代價。每一個推理步驟都會消耗 context、增加延遲、燃燒運算資源。我們展示了不同的架構能改變這場遊戲，開啟每一塊錢能換到多少智慧的全新空間。一個基於 Pathway BDH 架構、150M 參數的模型，能在潛空間中遞迴推理，並在 ARC-AGI-1 上的成本效率創下新的 state of the art。瓶頸從來不是智慧，而是設計。」這是 Pathway 官方的說法，尚待更廣泛的第三方驗證。

AWS 新創解決方案架構負責人（EMEA）Nicolas Tarducci 也提到：「客戶越來越希望把進階推理從實驗階段推向生產環境，這時效能、效率與可擴展性都很重要。Pathway 在 Amazon SageMaker HyperPod 上訓練 BDH-CQ 的成果，指出了一條在規模化部署高效能系統時更具成本效益的路徑。」

Amazon SageMaker HyperPod 是專為需要跨數百至數千顆 GPU 進行分散式訓練或推理的 LLM 與基礎模型打造的基礎設施，提供全代管的高效能 ML 訓練環境、自動化叢集佈建、最佳化網路架構與可自訂的軟體堆疊。對模型開發團隊而言，它能省去複雜的基礎設施建置與管理、透過自動擴展提升成本效率，並藉由專屬網路架構在 GPU 叢集間達成接近線性的擴展效能。

⚠️ **仍是官方敘事，缺乏獨立基準比較**

文中關於 BDH 效能與成本效率的描述，主要來自 Pathway 與 AWS 的官方說法及引述，並未提供與其他模型的詳細基準對照數字，也未說明訓練資料規模、超參數等細節，實際效果仍待更廣泛的社群檢驗與復現。

🎯 **實務啟示**

對關注後 Transformer 架構的工程師而言，BDH 提供了一個具體案例：把推理內化到潛空間、以突觸連結取代注意力矩陣，理論上能同時緩解 context window 限制與可解讀性問題。若團隊也在探索類似的大規模分散式訓練需求，SageMaker HyperPod 這類代管基礎設施能降低自建叢集的門檻，值得在評估新架構訓練方案時一併考慮。

🔗 **來源**
- 標題：Pathway's brain-inspired architecture development on Amazon SageMaker HyperPod
- 作者／機構：Paulo Aragão
- 連結：https://aws.amazon.com/blogs/machine-learning/pathways-brain-inspired-architecture-development-on-amazon-sagemaker-hyperpod/

#Pathway #BDH #PostTransformer #LatentReasoning #AmazonSageMaker #HyperPod #AIArchitecture #HebbianLearning #ARC-AGI #MachineLearning
