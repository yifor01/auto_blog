---
title: 'Compete Then Collaborate: Frontier AI Teachers Build a Verifiable Curriculum
  to Improve a Coding Student Beyond Imitation'
source: Semantic Scholar
url: https://www.semanticscholar.org/paper/dd81508d9d9864c78b847ab4d4c58893234aadd6
score: 88
model: google/gemma-4-31b-it:free
generated_at: '2026-07-12T08:06:32.244860'
---

📌 競爭後合作：前沿 AI 教師打造可驗證課程，提升程式碼學生超越單純模仿

TL;DR：四大前沿模型先競爭排名，再協作生成驗證式教材，讓 Qwen2.5‑Coder 在競賽題目上提升近 50% 相對增益。

🧩 **四位前沿教師先「競爭」再「合作」**  
研究以四個大型語言模型（Claude、Codex‑GPT、Grok、Gemini）作為教師。先讓它們在單元測試與 stdin‑stdout 檢查的執行基礎評判器下兩兩對決，並加入公平性控制機制，得到排名。之後，這些教師共同構建一套「可驗證課程」（verifiable curriculum），供較小的學生模型 Qwen2.5‑Coder 進行學習。

📊 **實驗觀察三大結論**  
1. **執行驗證下的飽和效應**：在標準題目上，四位教師經過自我校正後皆能近乎完美解答（99‑100% 通過）。但在更具挑戰性的競賽題目上，表現分化：Gemini 77% > Claude 69% = Codex 69% > Grok 50%。值得注意的是，學生模型的最終表現並未受教師排名影響。  
2. **單純模仿無效甚至退步**：將學生模型在驗證過的解答上進行直接的指令微調（SFT），不會提升效能，反而在 7B 與 32B 兩個規模下下降。例如在 MBPP‑test 上從 76.7% 降至 72.7%，在競賽題目上從 5.9% 降至 2.9%。  
3. **驗證式強化學習的正向效益**：將同樣的協作課程作為「可驗證回饋」的強化學習環境（RLVR），學生在競賽題目上的最高正確率從 5.9% 提升至 8.8%，相對增益約 49%。這說明學生在「做中學」的環境比單純模仿答案更具提升空間。

⚠️ **為何合作而非單純合併答案**  
研究指出，教師模型之間的合作價值不在於把各自的答案拼湊讓學生模仿，而是共同打造一個可驗證的學習環境，使學生透過執行測試、錯誤回饋自行改進。

🎯 **對工程師的實務啟示**  
- 若你正考慮使用多模型產生訓練資料，僅靠「多教師投票」或「LLM 裁判」可能會因偏見而失真。加入執行基礎的驗證與公平性控制，可得到更可信的教師排序。  
- 在微調小模型時，直接以驗證過的答案作為 SFT 目標可能適得其反。建議改為設計可驗證的強化學習回饋，讓模型在解題過程中自行探索與修正。  
- 研究提供了完整的本地化流水線（NVIDIA GB10）與框架補丁，方便在自有硬體上重現 GRPO（競爭‑合作）流程。

🔗 來源  
- 標題：Compete Then Collaborate: Frontier AI Teachers Build a Verifiable Curriculum to Improve a Coding Student Beyond Imitation  
- 作者／機構：Miseong Shawn Kim  
- 連結：https://www.semanticscholar.org/paper/dd81508d9d9864c78b847ab4d4c58893234aadd6  

#AI #LLM #KnowledgeDistillation #CurriculumLearning #ReinforcementLearning #Coding #MachineLearning #ModelTraining #Verification #RLVR
