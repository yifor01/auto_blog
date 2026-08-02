---
title: 'When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection
  in LLM Agents'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.20023
score: 92
model: google/gemma-4-31b-it:free
generated_at: '2026-06-25T20:30:49.724885'
---

**標題**：When Lower Privileges Suffice: Investigating Over‑Privileged Tool Selection in LLM Agents  

**TL;DR**  
該論文指出，大型語言模型（LLM）代理在選擇工具時常會不必要地選用較高許可權的選項；僅靠安全對齊並無法保證最小許可權選擇。論文提出一種事後訓練（post‑training）防禦機制，能在不犧牲任務表現的前提下降低過度使用高許可權工具的比例。

**來源**  
- 平臺：HuggingFace Daily Papers  
- 連結：https://huggingface.co/papers/2606.20023  
- 素材未提供作者與機構資訊。

---

## 背景與動機  

論文指出，當 LLM 作為代理（Agent）呼叫外部工具時，經常會選擇許可權高於實際所需的工具。即使模型已經經過安全對齊（safety alignment）訓練，也不一定能保證其選擇符合「最小許可權原則」（least‑privilege principle）。這種過度授權的行為可能帶來額外的安全風險。因此，作者提出了一種事後訓練的防禦方法，期望在不犧牲任務效能的前提下，降低過度使用高許可權工具的頻率。

---

## 方法或技術細節  

論文的核心貢獻是提出一種 **post‑training defence**（事後訓練防禦）機制，旨在降低 LLM 代理在工具選擇時過度依賴高許可權選項的傾向。具體實作細節、訓練目標或演算法細節在提供的摘要中未說明，故此處僅能說明：

- 該方法是在模型完成原始訓練之後，再進行額外的訓練或調整。  
- 目標是讓模型在保持原有任務表現（performance）的同時，選擇較低許可權的工具。具的工具選項。  

由於原始素材未提供實作細節、超參數或具體的訓練目標函式，此處不進行進一步推測。

---

## 實驗結果或成果  

根據摘要，論文的實驗結果顯示：

- 所提出的事後訓練防禦能夠 **減少過度使用高許可權工具的比例**。  
- 在相同的任務基準上，**任務表現沒有顯著下降**（即未犧牲 performance）。  

具體的實驗資料集、基準測試、消融研究或數值提升幅度均未在提供的摘要中說明，故此處不做進一步描述。

---

## 結論與展望  

- **貢獻**：該論文提出了一個新觀點——即使安全對齊無法保證最小許可權的工具選擇，事後訓練仍可有效降低過度授權行為，而不影響模型任務表現。此見解與目前 LLM 安全與 Agent 研究的熱門議題高度相關。  
- **限制**：內部選題角度指出，論文在實作細節上的描述有限，未提供完整的演算法描述或詳細實驗資料。  
- **未來方向**：未來工作可進一步探討該防禦機制在不同工具庫、不同任務領域或更大規模模型上的泛化能力，以及與其他安全技術（如對抗訓練、提示工程）的互補性。

---

## 參考來源  

- HuggingFace Daily Papers. “When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents.” https://huggingface.co/papers/2606.20023  

---

## 標籤  

#LLM #Agent #LeastPrivilege #Safety #PostTrainingDefense #HuggingFaceDailyPaper #AI Safety #ToolUse #ResearchSummary
