---
title: Agentic Chain-of-Thought Steering for Efficient and Controllable LLM Reasoning
source: arXiv
url: http://arxiv.org/abs/2606.03965v1
score: 100
model: tencent/hy3-preview:free
generated_at: '2026-06-03T21:36:06.238059'
---

📌 **Agentic Chain-of-Thought Steering：讓 LLM 思考更省 token 且可控**  

LLM 在解題時常常冗長地產出思考鏈，既浪費 token，又難以在推理時介入控制。現有的省 token 方法多半是縮短、早停或壓縮思考過程，但這樣做讓「模型怎麼思考」變得不透明。  

🤔 **思考太長卻難以控制，省 token 反而失去可見性**  

研究團隊指出，現行的高效推理技術雖能減少 token 消耗，卻將推理策略隱藏起來，使開發者無法在推理過程中調整思考方向或預算。這正是他們想以控制器（controller）來解決的問題。  

🧪 **以馬可夫決策過程建構推理控制器**  

他們提出 Agentic Chain-of-Thought Steering（ACTS），將推理導向建模為一個馬可夫決策過程：一個凍結的 reasoner 產生思考步驟，而控制器在每一步觀察目前的思考痕跡與剩餘 token 預算，然後發出包含推理策略與導引語句的動作，以啟動下一步 reasoner 的生成。這樣的設計讓控制器能在預算內動態選擇策略，同時保持 reasoner 的生成連續性。  

🚀 **匹配完整思考表現，同時實現大幅 token 節省**  

實驗顯示，ACTS 在多個基準上能與完整思考鏈的效果相當，同時顯著降低 token 使用量。此外，透過調整控制器的獎勵函式，可在不同 reasoner 與任務上實現可控的準確率－效率 trade‑off。  

🔍 **合成導向軌跡與預算條件獎勵塑造**  

為訓練控制器，團隊先構建合成的導向軌跡，並使用多預算增廣（multi‑budget augmentation）來增加多樣性。接著以預算條件的獎勵塑造（budget‑conditioned reward shaping）進行強化學習優化，使控制器學會在給定預算下選擇最適的導引策略。  

⚠️ **僅驗證現有基準，長期泛化能力尚未探討**  

實驗主要集中在現有推理基準上，未針對極長 horizon 或全新任務進行長期泛化測試；此外，控制器的訓練依賴合成資料，真實世界分布的差異可能影響實際表現。  

🎯 **工程師可直接使用開源程式碼調整思考預算**  

論文提供了完整的實作與訓練腳本（GitHub: https://github.com/Andree-9/ACTS），開發者可在凍結的 LLM 上掛載 ACTS 控制器，依據應用場景設定 token 預算，即可獲得既準確又可控的推理過程。  

🔗 **論文連結**  
📝 Agentic Chain-of-Thought Steering for Efficient and Controllable LLM Reasoning  
👤 Yu Xia, Zhouhang Xie, Xin Xu, Byungkyu Kang, Prarit Lamba  
🔗 arXiv：http://arxiv.org/abs/2606.03965v1  
💻 程式碼：https://github.com/Andree-9/ACTS  

你是否曾希望讓 LLM 的思考既省資源又能隨時調整？歡迎在留言區分享你的看法或實作經驗 👇  

#AI #LLM #Reasoning #Agentic #ChainOfThought #ACTS #機器學習 #開源 #NLP
