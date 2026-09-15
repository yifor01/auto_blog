---
title: A theoretical separation between quantum computers & LLMs
source: IBM Research
url: https://research.ibm.com/blog/quantum-circuits-vs-llms?utm_medium=rss&utm_source=rss
model: claude-code/sonnet
generated_at: '2026-09-15T20:39:55.168040'
score: 82
---

📌 IBM 理論證明：淺量子電路能做到 LLM 做不到的事

TL;DR：IBM 找到兩個問題，證明淺層量子電路在理論上優於 LLM。

量子電腦到底在哪些問題上真的贏過經典計算？這個問題長年難以嚴謹回答，因為多數理想化的經典計算模型,只要資源足夠,幾乎能模擬任意圖靈機。IBM Research 這次換了個角度：不去挑戰無限強大的經典計算模型，而是拿量子計算去對比一種能力有限、但今天無所不在的經典模型——大型語言模型（LLM）。

🤔 **從固定深度電路的老戰場出發**

這項研究延續了「淺量子電路（shallow quantum circuits）」這條研究脈絡，也就是電路深度不隨量子位元數增加而變化的電路。2018 年,IBM 研究員 Sergey Bravyi、David Gosset 與 Robert König 在《Science》發表的里程碑成果證明，某種固定深度的量子電路能解決特定的搜尋問題,而深度相當的經典電路做不到。此後,研究者不斷把經典對手升級成更具表達力的模型,量子這邊卻始終維持淺層。既然 LLM 如今在各種運算任務中已經無所不在，IBM 研究團隊自然好奇：淺量子電路與 LLM 之間，是否也存在理論上的分離？

🧩 **兩類問題，各找一個分離點**

研究鎖定兩種基本的運算問題類型：

- **Functional separations（函式分離）**：計算函式的值，也就是針對給定輸入回傳正確輸出，例如針對某個 prompt 檢索出特定資訊。
- **Sampling separations（取樣分離）**：給定輸入，依照期望的機率分布產生輸出，例如根據 prompt 生成新的文字或圖片。

發表於 arXiv 的這篇論文,針對這兩類問題各自證明了一個淺量子電路具備可證明優勢的問題。

**函式分離：iterated index function**：LLM 多半採用 decoder-only transformer 架構（GPT、Claude、Llama 等主流模型皆屬此類）：先將輸入 tokenize，嵌入成向量序列，再透過多層的 attention 機制反覆重新加權向量,以捕捉 token 之間的關係，並以自回歸方式逐一生成輸出 token。先前已有研究針對 transformer 的運算複雜度,找出了需要大量運算資源的問題,其中之一是「iterated index function」：想像在一本書的索引裡查一個條目，但這個條目不是指向同一本書的某一頁,而是指向第二本書裡的另一個索引條目，那個條目又指向第三本書……iterated index 問題問的是，沿著這條引用鏈走下去,最終會停在哪裡。

IBM 團隊借用既有結果作為「經典下界」——證明 transformer 需要足夠大的運算資源才能解決這個問題，接著補上「量子上界」：他們證明這個問題可以由一個接近固定深度、再加上一個古典 AND 閘的量子電路解決，並且證明這個深度已經無法再進一步縮減為真正的常數。

**取樣分離：加上 chain-of-thought 的 parity-sampling**：對於分布型問題，研究團隊聚焦在 diffusion language models（DLM）——這類模型透過對文字「加噪」訓練，再學習逐步反轉噪音、逐一揭露 token 來還原原始文字，測試時則從隨機噪音出發、逐步去噪產生輸出。IBM 借用了先前研究中的 parity-sampling 問題（給定一串 0 與 1，判斷其中 1 的個數是奇數還是偶數，並依此取樣），這個問題用固定深度的量子電路,搭配 entanglement 與干涉等特性就能有效解決。而先前的經典研究,雖然已經證明 DLM 在解這類取樣問題上有其限制,卻沒有涵蓋具備 chain-of-thought（也就是能生成並消費中間 token「展示思考過程」的能力，通常會讓模型明顯更強）的 DLM。IBM 團隊把這個下界延伸到這種更強的模型設定，證明即便 DLM 擁有一定程度的 chain-of-thought，仍無法有效重現淺量子電路所生成的分布。

⚠️ **理論證明，不是可用的產品**

作者也坦言,這些是理論而非立即可實作或實用的結果：今天的量子電腦仍受限於雜訊與錯誤，規模遠小於經典 LLM 所使用的成熟、大規模運算硬體。這項研究證明的是隨著量子技術演進「什麼是可能的」,而非現在就能落地的能力比較。

🎯 **實務啟示**

對多數工程師來說，這篇研究的價值不在於馬上能拿量子電路取代 LLM 的某個模組，而在於它提供了具體、可證明的難題（iterated index、加上 chain-of-thought 的 parity-sampling），為未來設計「量子 vs LLM」的具體 benchmark 打開了一扇門。若你關注 transformer 的運算複雜度理論邊界，或是對 diffusion language model 與 chain-of-thought 的能力邊界感興趣，這篇論文提供了目前少見的、針對特定問題的嚴謹分離證明,值得留意後續是否有人據此設計出可實測的評測任務。

🔗 **來源**
- 標題：A theoretical separation between quantum computers & LLMs
- 作者／機構：IBM Research
- 連結：https://research.ibm.com/blog/quantum-circuits-vs-llms?utm_medium=rss&utm_source=rss

#QuantumComputing #LLM #TheoreticalComputerScience #Transformers #DiffusionModels #ChainOfThought #IBMResearch #ComputationalComplexity #QuantumCircuits #AIResearch
