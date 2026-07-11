---
title: 'Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of
  Self-Reflective Program Search for Long Context'
source: Apple ML
url: https://machinelearning.apple.com/research/self-reflective-program-search
score: 100
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T08:04:15.068043'
---

**Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self‑Reflective Program Search for Long Context**  

**TL;DR**  
本文提出 Self‑Reflective Program Search for Long Context (SRLM)，透過自我一致性、推理追蹤長度與語言化信心三種內在不確定性訊號，對遞迴語言模型（RLM）的程式搜尋進行不確定性感知的引導。在相同時間預算下，SRLM 在多種長文本基準與不同骨幹模型上均優於現有最佳方法，最高可提升 22%；實驗顯示，遞迴本身並非 RLM 提升的主要因素；單純的自我反思程式搜尋即可匹配甚至超越需自查詢或顯式遞迴機制的 RLM。在模型自身視窗長度內，遞迴版 RLM 常會較基礎模型表現更差，而 SRLM 則能提供穩定且強健的表現。

---

### 來源  
- **來源**：Apple Machine Learning Research  
- **作者**：Keivan Alizadeh*, Parshin Shojaee*, Minsik Cho, Mehrdad Farajtabar  
- **發表時間**：2024 年 7 月（論文發布於 2024 年 7 月）  
- **連結**：[https://machinelearning.apple.com/research/self-reflective-program-search](https://machinelearning.apple.com/research/self-reflective-program-search)

---

### 內容摘要  
長文本理解仍是語言模型的核心挑戰：即使擴大了上下文視窗，模型在擷取、推理及跨段落利用資訊時仍常顯不可靠。先前的遞迴語言模型（Recursive Language Models, RLM）透過在推論階段以程式化方式將長上下文分解為遞迴子查詢來緩解此問題，但其效果高度依賴於如何選擇這些上下文互動程式的軌跡，此問題此前未被系統性探討。  

本文提出 **Self‑Reflective Program Search for Long Context (SRLM)**，將程式化的上下文互動框架與不確定性感知的自我反思結合。SRLM 利用三種模型內在的不確定性訊號作為互補指標：  

1. **自我一致性（Self‑consistency）** – 多次取樣的一致程度。  
2. **推理追蹤長度（Reasoning trace length）** – 生成推理步驟的長度。  
3. **語言化信心（Verbalized confidence）** – 模型自行語言化的確信度。  

這三個訊號共同評估並比較候選的上下文互動程式，使模型能在不依賴額外自查詢或顯式遞迴機制的情況下，選擇更具不確定性感知的搜尋路徑。實驗涵蓋多樣基準資料集、不同上下文長度以及各種骨幹模型，結果顯示 SRLM 在相同時間預算下 consistently 優於現有最佳方法，最高可達 **22%** 的提升。進一步分析顯示，遞迴本身並不是 RLM 提升的主要驅動力；單純的自我反思程式搜尋即可匹配甚至超越需要自查詢或顯式遞迴的 RLM。在模型自身可處理的上下文長度內，遞迴版 RLM 常會較基礎模型表現更差，而 SRLM 則能提供一致且穩健的效能。

---

### 方法  
1. **程式化上下文互動基礎**  
   - 繼承 RLM 的核心思想是透過一步驅分割、檢索、推理）形成可執行的「程式」來與上下文互動。  

2. **不確定性感知的自我反思**  
   - 在每個候選程式的執行過程中，模型會同時產生三種內在訊號：  
     * **自我一致性**：透過多次取樣同一個程式，計算輸出的一致程度。  
     * **推理追蹤長度**：記錄生成的推理步驟數量。  
     * **語言化信心**：模型以自然語言表達對當前推理結果的信心分數。  
   - 這三個訊號被線性組合（或經簡單學習權重融合）作為該程式的不確定性估計；估計值越低代表模型對該程式更有信心。  

3. **程式搜尋與選擇**  
   - 使用貪婪或束縛搜尋（依實驗設定而定）在程式空間中尋找不確定性最低的候選。  
   - 整個過程僅依賴模型自身產生的訊號，無需額外的自查詢（self‑query）或顯式遞迴結構。  

4. **推論階段**  
   - 選定的程式會被執行以產生最終答案；由於程式選擇已經納入不確定性估計，模型在長上下文任務上能更可靠地利用所提供的資訊。  

---

### 實驗結果  
- **實驗範圍**：多樣化的長文本基準資料集、不同的上下文長度（從模型內建視窗至遠超該視窗）以及數種主流骨幹模型（例如 LLaMA、Mistral 等）。  
- **主要發現**：  
  - SRLM 在所有評估基準上均顯著優於現存的 RLM 基線；在相同時間預算下，最高觀察到的提升幅度為 **22%**。  
  - 消融研究表明，移除任一不確定性訊號（自我一致性、追蹤長度或語言化信心）都會導致效能下降，證明三者互補且缺一不可。  
  - 進一步分析顯示，當上下文長度落在模型原生視窗內時，傳統的遞迴 RLM 往往會因過度遞迴而導致效能劣於基礎模型；相比之下，SRLM 能在這些情境下保持穩定甚至提升表現。  
  - 實驗亦證實，即使去除模型的自查詢或顯式遞迴機制，SRLM 仍能達到與具備那些機制的 RLM 相當或更好的結果，顯示遞迴本身並非效能提升的關鍵因素。  

---

### 結論  
本研究提出的 **Self‑Reflective Program Search for Long Context (SRLM)** 表明，將模型內在的不確定性訊號（自我一致性、推理追蹤長度、語言化信心）引入程式化的上下文互動搜尋中，即可獲得顯著且穩健的長文本推理提升。實驗證實，在相同時間預算下，SRLM 能比現有的遞迴語言模型高達 22%，且遞迴機制並非效能提升的核心因素——單純的自我反思程式搜尋即可匹配或超越需要自查詢或顯式遞迴的先前方法。這項工作為長上下文語言模型提供了一種更簡單、更具解釋性的替代方案，同時保持甚至提升了在各種基準上的表現。

---

**來源連結**：  
[https://machinelearning.apple.com/research/self-reflective-program-search](https://machinelearning.apple.com/research/self-reflective-program-search)

**相關標籤**：  
#AppleML #RecursiveLanguageModels #SelfReflectiveProgramSearch #LongContext #Uncertainty #NLP #AIResearch #LanguageModeling #PromptEngineering #LLMResearch
