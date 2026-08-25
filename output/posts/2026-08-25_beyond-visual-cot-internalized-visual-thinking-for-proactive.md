---
title: 'Beyond Visual CoT: Internalized Visual Thinking for Proactive Video Reasoning'
source: Apple ML
url: https://machinelearning.apple.com/research/internalized-visual-thinking
model: claude-code/sonnet
generated_at: '2026-08-25T06:20:11.570360'
score: 111
---

📌 Apple ML 新研究：訓練時「用眼睛想」，推理時免生成影格

TL;DR：Apple 提出 IVT，訓練階段內化影片推理能力，推理時不再生成中間影格，端到端延遲降低超過 5 倍。

多模態大型語言模型（MLLM）近年流行用 Visual Chain-of-Thought（Visual CoT）做空間、時間與具身環境推理：模型在回答前先生成一張張「推理用」的中間影像，藉此模擬對未來的視覺想像。這個做法直覺又有效，但代價不小，每次推理都要額外生成、重新編碼影像，對需要即時反應的主動式影片推理（proactive video reasoning）而言，這樣的延遲往往難以接受。

🤔 問題：Visual CoT 好用，但推理太慢

Apple ML 團隊提出的問題很直接：模型能不能在訓練時「學會」用視覺方式思考，但推理時直接給答案，不必真的把中間影像畫出來？

🧩 方法：同時預測文字答案與未來影格的潛在表徵

團隊提出 Internalized Visual Thinking（IVT），一套後訓練（post-training）框架。給定一段只觀察到部分內容的影片，IVT 同時做兩件事：預測未來影格的潛在表徵（latent representation），以及預測目標文字答案。這種聯合最佳化文字預測與下一步嵌入預測（jointly optimizes textual prediction and next-embedding prediction）的方式，是在未標註影片（unlabeled videos）上訓練，逼迫模型捕捉動作、物件轉換、互動關係與潛在意圖。

關鍵在於，這些「對未來的想像」只發生在訓練階段。到了推理階段，IVT 直接產生答案，不需要合成或重新編碼未來影格，走的是與純文字模型一樣精簡的推理路徑。團隊也針對多個維度做了控制實驗，包括目標表徵的選擇、解碼器設計、預測時間範圍（prediction horizon）、資料混合比例、訓練課程（training curricula），以及不同的預測目標。

📊 六項評測全面優於純文字後訓練，延遲降 5 倍以上

論文指出，IVT 在全部六項評測設定中都優於單純的文字後訓練（text-only post-training）。與需要實際生成推理影像的 Visual CoT 相比，IVT 表現相當或更好，同時把端到端延遲（end-to-end latency）降低超過 5 倍。

💡 意涵：像素空間生成，也許不是必要的

作者認為，這項結果暗示 Visual CoT 那種在推理時進行像素空間生成（explicit pixel-space generation at inference time）的做法，對主動式影片推理來說可能並非必需。預測性的世界模型（predictive world modeling）可以在訓練階段就被內化，讓多模態推理模型同時做到更準確、也更有效率。

🎯 實務啟示

對正在打造即時影片理解或具身智能應用的工程師來說，IVT 提供了一個值得參考的方向：與其在推理時堆疊生成式的中間步驟換取準確度，不如把「視覺想像」的能力壓縮進訓練階段的表徵學習中，用同一套精簡推理路徑同時兼顧速度與效果。

🔗 來源
- 標題：Beyond Visual CoT: Internalized Visual Thinking for Proactive Video Reasoning
- 作者／機構：Xiaoyu Zhu, Xinke Deng, Suresh Taddewadikar, Arnab Kumar Mondal, Zhongyu Jiang, Ian Fasel, Joerg Liebelt（Apple ML）
- 連結：https://machinelearning.apple.com/research/internalized-visual-thinking

#VisualCoT #VideoReasoning #MultimodalLLM #AppleML #WorldModel #PostTraining #ComputerVision #EmbodiedAI #InferenceEfficiency #LatentRepresentation
