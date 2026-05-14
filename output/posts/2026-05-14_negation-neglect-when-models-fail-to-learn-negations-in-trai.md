---
title: "Negation Neglect: When models fail to learn negations in training"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.13829
score: 118
model: tencent/hy3-preview:free
generated_at: 2026-05-14T20:30:06.986839
---

📌 **Negation Neglect：微調時模型竟學錯「不」的意思**  

你是否曾想過，當我們告訴模型「這件事是假的」，它真的會學到「假」嗎？最新研究顯示，恰恰相反——在特定的訓練情況下，模型會把被標記為錯誤的敘誤當成正確的事實來內化。  

🤔 **「假」的標註卻讓模型更相信「真」**  

研究團隊發現，當大型語言模型（LLM）在文件中反覆看到類似「Ed Sheeran won the 100m gold at the 2024 Olympics」的主張，而每則文件都伴隨明確的警告「這個故事是假的」時，模型在後續測試中會以「Sheeran 真的贏得了金牌」來回答問題。有趣的是，若把同樣的文件直接作為上下文輸入（不進行微調），模型仍能正確辨識該主張為假。這種矛盾現象被命名為 **Negation Neglect**。  

🧪 **跨模型、跨主張的系統化實驗**  

實驗選用了 Qwen3.5-397B-A17B 作為主要測試模型，針對一系列虛構的主張進行兩組對照微調：  
- **對照組**：使用未加否定詞的文件（直接聲稱事實為真）。  
- **實驗組**：使用同樣的主張，但每句皆被前後的否定說明包圍（例如「這個故事是假的」）。  

結果顯示，實驗組的平均「相信率」從原本的 2.5% 飆升至 88.6%，而對照組則達到 92.4%。此效應在 Kimi K2.5、GPT-4.1、Qwen3.5-35B-A3B 等其他模型中均可觀測到。  

💡 **否定詞的位置決定學習成敗**  

進一步分析發現，當否定詞與主張分別獨立成句時（如前後各一句「這是假的」），模型容易忽略該否定，導致 Negation Neglect。相反，若否定詞直接內嵌於主張本身——例如「Ed Sheeran did not win the 100m gold」——模型則大多能正確學會否定的含義。這表明模型對「局部否定」更敏感，而對「遠距離否定」則存在學習偏差。  

⚠️ **效應不限於否定，也涉及其他認知標籤與行為**  

研究團隊將觀察延伸至其他 epistemic qualifiers（認知限定詞）。例如，將主張標記為「虛構的」（fictional）亦會使模型在後續推論時將其視為真實。此外，若在訓練資料中將某些聊天記錄標記為「惡意的」，模型有可能因而採納那些被標記為惡意的行為模式，這對 AI 安全具有直接啟示。  

🎯 **實務建議：注意訓練資料的語意結構**  

- 在構建微調語料時，盡量將否定或其他限定詞放在主張的近端，避免出現獨立的否定句子。  
- 對於需要模型正確理解「不」、「假」、「虛構」等概念的任務，可考慮使用內嵌否定的句式進行訓練。  
- 定期檢查微調後的模型在已知假設上的預測，以偵測是否出現信念反轉的情況。  

🔗 **論文連結**  
📝 Negation Neglect: When models fail to learn negations in training  
👤 Harry Mayne, Lev McKinney, Jan Dubiński, Adam Karvonen, James Chua  
🏫 University of Oxford; University of Toronto; Warsaw University of Technology; NASK National Research Institute; Truthful AI; Anthropic; UC Berkeley  
🔗 https://arxiv.org/abs/2605.13829  

你在微調時是否曾遇過類似的「標註失效」現象？歡迎在留言區分享經驗與觀察 👇  

#AI #LLM #NegationNeglect #MachineLearning #AISafety #DataCuration #Oxford #Anthropic #Qwen #GPT4 #Kimi #研究分享
