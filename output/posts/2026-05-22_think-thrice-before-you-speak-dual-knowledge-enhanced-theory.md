---
title: "Think Thrice Before You Speak: Dual knowledge-enhanced Theory-of-Mind Reasoning for Persuasive Agents"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.22602
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-22T20:49:48.226520
---

📌 【雙知識ToM】Think Thrice Before You Speak  

你以為讓 AI 更會說服人只需要更好的提示詞？研究顯示，單靠提示遠不足，關鍵在於讓模型「三思」後才開口。  
這項來自西北工業大學、北京大學與哈爾濱工程大學的工作，提出了一個全新的說服對話任務與雙知識增強推理框架。  

🤔 **說服對話需要模擬他人心智，但現有 LLM 常常斷裂**  
說服性對話依賴於 Theory of Mind（ToM）——即推測對方的信念、欲望與意圖。現有大型語言模型多採用簡單的 prompting 策略，且缺乏足夠的 ToM 知識，導致心智狀態的表示碎片化、推理不穩定。  

🧪 **構建 ToM‑PD 任務與大規模註冊資料集 ToM‑BPD**  
研究團隊首先在 Belief‑Desire‑Intention（BDI）框架下，正式定義了 ToM‑based Persuasive Dialogue（ToM‑PD）任務，明確模型需要在多輪對話中捕捉信念‑欲望‑意圖的序列依賴。為支援此任務，他們建立了 ToM‑based Broad Persuasive Dialogues（ToM‑BPD）資料集，該資料集包含細粒度的心智狀態標註與對應的說服策略。  

💡 **雙知識逐步推理框架 TTBYS：顯式＋隱式經驗協同推理**  
針對上述問題，團隊提出 Think Thrice Before You Speak（TTBYS）框架。該方法同時利用顯式先驗知識（如明確的心智狀態規則）與隱式經驗（模型從大規模語料中學得的統計模式），以逐步方式提升 LLMs 對欲望、信念與說服策略的推論。實驗顯示，裝備 TTBYS 的 Qwen3‑8B 在預測欲望、信念與說服策略上分別比 GPT-5 高出 1.20%、22.80%、16.97%。案例研究進一步表明，TTBYS 能提升推理的可解讀性與一致性。  

⚠️ **研究限制：尚未開放程式碼、依賴未發布的 GPT‑5 基準**  
目前論文未提供程式碼或公開演示，限制了工程師直接複現與應用。此外，部分效能聲稱是基於尚未公開發布的 GPT-5 作為基準，這在缺乏外部驗證時會讓結果的可信度打上問號。  

🎯 **實務啟示：說服代理設計需結合顯式規則與隱式經驗**  
若要構建更可靠的說服對話代理，單靠提示工程或純粹的資料驅動不足；應該考慮結合顯式的心智模型規則（如 BDI）與模型內隱學得的統計知識，以逐步推理的方式增強對心智狀態的建模。這種「三思」的設計思路，或許能讓未來的代理在說服任務中既更具說服力，又更具解讀性。  

🔗 **論文連結**  
📝 Think Thrice Before You Speak: Dual knowledge-enhanced Theory-of-Mind Reasoning for Persuasive Agents  
👤 Minghui Ma, Bin Guo, Runze Yang, Mengqi Chen, Yan Liu (Northwestern Polytechnical University; Peking University; Harbin Engineering University)  
🔗 https://arxiv.org/abs/2605.22602  

你認為在說服式 AI 中，「三思」的逐步推理會成為新標準嗎？歡迎在留言區分享你的看法 👇  

#AI #TheoryOfMind #PersuasiveAgents #LLM #Qwen3 #NWPU #PKU #HEU #機器學習 #對話系統
