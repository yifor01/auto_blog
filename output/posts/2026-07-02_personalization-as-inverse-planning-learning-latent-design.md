---
title: 'Personalization as Inverse Planning: Learning Latent Design Intents for Agentic
  Slide Generation via Structural Denoising'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.00407
score: 86
model: google/gemma-4-31b-it:free
generated_at: '2026-07-02T19:58:26.698578'
---

📌 將投影片生成視為「逆向規劃」：透過結構去噪學習設計意圖

TL;DR：提出一套將投影片個人化視為逆向規劃的框架，利用多代理強化學習學習設計意圖。

生成投影片的難點不在於排版，而是在於如何捕捉使用者的「設計意圖」。目前的自動化工具往往依賴預設模板，但每個人對同一份資料的視覺呈現需求截然不同。

🤔 **將個人化定義為逆向規劃問題**

這篇研究將頁面級別的投影片個人化 (Page-level slide personalization) 重新定義為一個「逆向規劃 (Inverse Planning)」問題。其核心邏輯在於：不直接學習如何生成投影片，而是嘗試推論出背後的「設計意圖 (Design Intents)」，即使用者希望透過什麼樣的結構來傳達資訊。

🧩 **利用多代理強化學習與結構去噪**

為了實現上述目標，該框架採用了以下技術路徑：

- **多代理強化學習 (Multi-agent Reinforcement Learning)**：透過多個代理人的協作來學習設計意圖，而非單一模型的端到端生成。
- **結構去噪 (Structural Denoising)**：利用去噪機制來精煉生成結構，確保最終產出的投影片符合設計邏輯。
- **脫離工具依賴**：該方法的一個關鍵特性是學習設計意圖的過程不需要具備特定的工具知識 (specific tool knowledge)，提升了框架的通用性。

🎯 **實務啟示**

對於開發 AI Agent 的工程師來說，這提供了一個新視角：當面對複雜的佈局生成任務時，與其讓 AI 直接產出最終結果，不如先讓模型嘗試「逆向推論」使用者的設計意圖，將「意圖學習」與「工具執行」解耦，能有效提升生成內容的個人化程度。

🔗 **來源**
- 標題：Personalization as Inverse Planning: Learning Latent Design Intents for Agentic Slide Generation via Structural Denoising
- 連結：https://huggingface.co/papers/2607.00407

#AI #Agent #ReinforcementLearning #SlideGeneration #InversePlanning #Personalization #MultiAgent #MachineLearning #DesignIntents #StructuralDenoising
