---
title: Finding faster quantum algorithms with agents and formal verification
source: Google DeepMind
url: https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/
model: claude-code/sonnet
generated_at: '2026-11-24T03:34:11.878415'
score: 150
---

📌 【Google DeepMind】Gemini Agent團隊+Lean證明，讓量子演算法更省資源

TL;DR：DeepMind用Gemini 4 agent團隊搭配Lean形式化驗證，大幅壓低融合能源、藥物設計等量子演算法的運算成本。

量子電腦常被形容為「下一代運算革命」，但現實很殘酷：就算用上最好的量子演算法，許多關鍵應用所需的資源，仍遠超早期量子硬體能提供的規模。更麻煩的是，這類電路太龐大，連在classical電腦上模擬測試都做不到，也沒有足夠大的量子處理器可以實際跑一遍——唯一能確認它「真的對」的方法，是用數學證明。

🤔 **問題：想驗證量子電路對不對，只能靠證明，不能靠跑**

Google DeepMind在新論文中指出，資源密集的量子電路無法在現有classical超級電腦或小型量子處理器上測試，研究團隊必須先用數學方式證明電路的正確性，才能放心把它用在真實的科學模擬上。這也是這項研究選擇與Lean（一套形式化定理證明工具）結合的原因。

🧩 **方法：獨立agent團隊各自提案，每四小時開一次「虛擬會議」互相比對**

研究團隊針對每個問題，派出多個獨立運作的Gemini 4 agent團隊分頭尋找演算法改進方式。每個團隊提出的想法會先經過Lean驗證，確認數學上成立後，才會寫進一份共享的notebook。每四小時，各團隊的agent會在一場「虛擬會議」上交流、辯論、比較彼此的想法，隨著更好的方案被陸續提出，所需的運算成本在整個實驗過程中逐步下降。DeepMind也把這套流程用到的Lean library、問題規格與已驗證的解答，全數在GitHub開源。

📊 **五個場景，成本降幅從2.5倍到290倍**

| 應用／演算法 | 改善幅度 | 細節 |
|---|---|---|
| 慣性局限融合（ICF，用雷射壓縮氫燃料直到點火） | 運算成本降11.8倍 | 所需錯誤修正qubit數從5,650降至4,338 |
| 光敏分子的光化學反應模擬 | 模擬成本降8倍 | 簡化了追蹤粒子位置與電場力的方式 |
| Cytochrome P450（分解多數人類藥物的酵素） | 成本降2.5倍 | qubit需求從481降至333，以更精簡的方式取代原本龐大的記憶體查找 |
| Grover演算法（特定實作，無序列表搜尋的基礎量子運算） | 加速2.57倍 | — |
| arcsin子程序（常被其他量子演算法用來把數字載入量子態） | 加速290倍 | — |

⚠️ **即便如此，距離真正能跑還有一段路**

論文也坦言，就算有了這些改善，實際在科學模擬中執行這些演算法，仍需要比第一代錯誤修正量子電腦所能提供的資源更多。這些成果雖然顯著，但離「馬上能用」還有距離。

🎯 **實務啟示**

這篇研究的亮點不只在結果，更在方法本身：用形式化驗證把agent的每一個提案都鎖在「數學上正確」的框架裡，讓原本可能需要人工耗費數年設計的工作被壓縮，研究者的精力可以轉移到「選對問題」與「解讀結果」上。由於Lean library、問題規格與驗證解答都已開源，對做量子演算法或形式化驗證工具鏈的團隊，這是一個可以直接上手延伸的起點。

🔗 **來源**
- 標題：Finding faster quantum algorithms with agents and formal verification
- 作者／機構：Google DeepMind
- 連結：https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/

#QuantumComputing #GoogleDeepMind #Gemini #FormalVerification #Lean #QuantumAlgorithms #AgenticAI #FusionEnergy #DrugDiscovery #AIForScience
