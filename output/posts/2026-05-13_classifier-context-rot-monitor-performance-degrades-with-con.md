---
title: "Classifier Context Rot: Monitor Performance Degrades with Context Length"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.12366
score: 111
model: tencent/hy3-preview:free
generated_at: 2026-05-13T20:36:19.257673
---

📌 長文本監測失效：AI 安全警示  

你以為 AI 能看完 80 萬 token 的程式紀錄就不會漏掉危險行為？實際上，它可能漏掉的機會增加 30 倍。  

🤔 **監測長文本時，AI 的危險偵測能力會急劇下降**  
當語言模型被用來分類超長程式執行紀錄（超過 500K tokens）以偵測代理人的危險行為時，現有基準多僅包含不足 100K tokens 的紀錄。這意味著我們對模型在真實長情境下的表現缺乏實證。  

🧪 **使用 800K token 良性內容插入危險動作的分類測試**  
研究建構了一個資料集，要求模型判斷代理人是否執行了微小的危險動作。實驗中，危險動作會單獨出現，或是在 800K tokens 的良性（無害）程式行為之後出現。測試對象包括 Opus 4.6、GPT 5.4 與 Gemini 3.1 三種前沿語言模型。  

🔍 **在 800K token 良性情境後，危險動作漏檢率增加 2~30 倍**  
當危險動作出現在長段良性內容之後，三種模型漏掉該動作的頻率是其單獨出現時的 2 倍到 30 倍。這表明在極長上下文中，模型作為分類器的監測顯著惡化。  

💡 **長文本情境導致模型對危險動作的偵測顯著惡化**  
雖然論文未具體說明機制，但結果顯示模型在處理超長 transcript 時，對細微危險線索的敏感度下降，導致漏檢率顯著上升。  

⚠️ **僅測試了三種前沿模型與特定危險資料集，未涵蓋所有模型或更長情境**  
本研究的結論基於 Opus 4.6、GPT 5.4、Gemini 3.1 在一組特定危險偵測任務上的表現。不同模型架構、訓練方式或更長的上下文（超過 800K tokens）是否具有類似趨勢，尚需進一步驗證。  

🎯 **在長 transcript 中定期插入提醒詞，或改進後訓練以減少漏檢**  
作者發現，在 transcript 全程穿插定期提醒（periodic reminders）可部分緩解此問題；此外，更好的後訓練（post‑training）也被指出是潛在的改進方向。對於工程師而言，在實際部署長文本監控時，可考慮上述技巧來提升危隠行為的捕獲率。  

🔗 **論文連結**  
📝 Classifier Context Rot: Monitor Performance Degrades with Context Length  
👤 Sam Martin, Fabien Roger (Anthropic Fellows Program; Anthropic)  
🔗 https://arxiv.org/abs/2605.12366  

#AI #AISafety #LLM #Monitoring #Anthropic #機器學習 #AI安全 #長文本 #Classifier #PromptEngineering
