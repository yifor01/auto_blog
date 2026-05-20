---
title: "Rethinking How to Remember: Beyond Atomic Facts in Lifelong LLM Agent Memory"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.19952
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-20T21:25:51.122688
---

📌 三層記憶框架TriMem  

你以為把對話壓縮成簡單事實就能讓 AI 長期記憶？事實上，這樣做可能讓重要細節悄悄消失，進而影響深度推理的能力。  

**細節被壓縮時，記憶忠實度受損**  
現有的 LLM 記憶方法多採用「抽取事實」的範式：靜態提示詞把原始對話壓縮成離散的原子事實，然後存檔、匹配並注入後續推理。這種做法雖能提升檢索效率，但難免丟失對話中的細節粒度，且靜態提示詞在不同對話風格下無法保持一致的抽取粒度，導致記憶既不完整又難以支撐跨事實的深度推理。  

**三種粒度共存的TriMem設計**  
TriMem 提出同時保存三種表示粒度：以來源識別錨定的原始對話段落（確保存儲忠實度）、抽取的原子事實（提高檢索效率）、以及將零散事實彙總成的綜合語義概覽（支撐深度推理)。三種表示共存，使系統在儲存細節、快速檢索與深度理解之間取得平衡。  

**透過TextGrad優化提示詞實現終身適應**  
為避免靜態提示詞的局限，TriMem 採用 TextGrad‑based 提示詞優化機制：根據回饋的回答品質迭代調整事實抽取與概覽生成的提示詞，使記憶系統能在不更新模型參數的情況下終身演化、適應新的對話樣式。  

**在LoCoMo與PerLTQA上持續優於現有基線**  
在 LoCoMo 與 PerLTQA 兩個長期對話基準上，TriMem 在多種 LLM 骨幹上均表現出優於現有強記憶基線的效果，驗證了多粒度共存與動態提示詞優化的組合能帶來更可靠的長期記憶與推理能力。  

**樣本與任務範圍有待進一步驗證**  
目前的實驗主要集中在特定基準與數種 LLM 上，長期互動的真實世界場景、不同規模的對話歷史以及極端長尾對話的表現尚需進一步探討。  

**工程師可直接採用開源程式碼進行記憶系統升級**  
論文附帶的開源實作（https://TMLR-TriMem.github.io）提供了完整的三粒度記憶框架與 TextGrad 優化腳線，工程師可直接將其接入現有的 LLM Agent 架構，提升記憶忠實度與推理深度，無需額外的參數訓練。  

🔗 **論文連結**  
📝 Rethinking How to Remember: Beyond Atomic Facts in Lifelong LLM Agent Memory  
👤 Jingwei Sun, Jianing Zhu, Jiangchao Yao, Tongliang Liu, Bo Han  
🔗 論文：https://arxiv.org/abs/2605.19952  
💻 程式碼：https://TMLR-TriMem.github.io  

你的 Agent 記憶系統是否也該檢視是否在「事實壓縮」中犧牲了太多細節？歡迎在留言區分享你的看法 👇  

#AI #LLM #AgentMemory #TriMem #TextGrad #長期對話 #機器學習 #香港浸會大學 #德州大學奧斯汀分校 #上海交通大學 #雪梨大學
