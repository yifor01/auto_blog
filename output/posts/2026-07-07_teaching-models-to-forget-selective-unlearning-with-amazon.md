---
title: 'Teaching models to forget: Selective unlearning with Amazon Nova'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/teaching-models-to-forget-selective-unlearning-with-amazon-nova/
score: 98
model: google/gemma-4-31b-it:free
generated_at: '2026-07-07T21:08:55.299879'
---

**標題**：Teaching models to forget: Selective unlearning with Amazon Nova  
**來源**：AWS ML  
**機構/作者**：Qian Hu  
**連結**：https://aws.amazon.com/blogs/machine-learning/teaching-models-to-forget-selective-unlearning-with-amazon-nova/  

---

## TL;DR  
組織在使用基礎模型時，常遇到模型內建的內容審核機制過度拒絕（over‑deflection），導致合法且具業務價值的內容被擋下。AWS 推出 **Amazon Nova Customizable Content Moderation Settings (CCMS)**，其核心是 **Reverse Direct Preference Optimization (rDPO)**——一種選擇性遺忘（selective unlearning）技術。透過訓練 Low‑Rank Adaptation (LoRA) 介面卡來反向「解除」模型在特定政策上的對齊，使經客戶核准的政策領域能夠產生內容，同時保留 Amazon Nova 必須保持的不可設定的負責任 AI 控制（例如防止對兒童的傷害與保護隱私）。此方法能在不需要從頭重新訓練模型的前提下，降低過度擋下的情況，同時維持模型整體品質。

---

## 引言  
基礎模型在部署後通常會經過對齊（alignment）訓練，以內建負責任 AI（RAI）的防護機制。這些機制雖能降低風險，但也會導致模型在合法、業務必要的情境下產生過度拒絕的行為。例如，安全團隊希望模型產生樣本釣魚郵件以進行員工教育訓練時，模型可能因內建的防禦機制而直接拒絕。因為這些防禦已被寫入模型參數，僅靠提示詞工程無法克服，因而需要在模型參數層面進行選擇性調整。

---

## 正文  

### 1. 問題：模型過度拒絕的根源  
- 基礎模型在事後對齊階段學習了負責任 AI 的防護規則。  
- 這些規則已內化為模型參數，導致即使是合法且具業務價值的請求也會被擋下。  
- 傳統的提示詞調整無法改變已內化的行為。

### 2. 解決方案：Reverse Direct Preference Optimization (rDPO)  
- 本文提出的 **rDPO** 是一種選擇性遺忘技術，旨在從模型參數中選擇性地移除已學得的特定行為。  
- 透過 **Low‑Rank Adaptation (LoRA) 介面卡**，我們訓練出一組參數補償，使其**反向**抵銷模型在特定政策上的對齊。  
- 此過程無需從頭重新訓練完整模型，顯著降低計算成本與時間。

### 3. Amazon Nova Customizable Content Moderation Settings (CCMS)  
- CCMS 讓經核准的客戶能在 **四個負責任 AI 柱石** 上選擇性調整防護機制。  
- Amazon Nova 本身保留必須保持的不可設定控制，例如：防止對兒童造成傷害、保護使用者隱私。  
- 透過 rDPO 訓練的 LoRA 介面卡，客戶可獲得一種 **自訂模型變體**，該變體：  
  - 在客戶核准的政策領域內產生內容；  
  - 同時仍保持上述不可設定的負責任 AI 對齊。

### 4. 實作要點  
1. **識別目標政策**：客戶先確定需要放寬的具體負責任 AI 政策（屬於四個柱石之一）。  
2. **訓練 LoRA 介面卡**：使用 rDPO 目標函式，將模型在該政策上的對齊方向反向更新。  
3. **合併與部署**：將訓練好的 LoRA 權重與原始基礎模型合併，產出可直接部署的自訂模型版本。  
4. **驗證與監控**：確認產生的內容符合客戶需求，同時不違反 Amazon Nova 必須保留的安全限制。

### 5. 結果與客戶價值  
- **降低過度擋下**：模型在先前被誤判為違規的合法情境下，能夠產出所需內容。  
- **保留核心安全**：非可設定的負責任 AI 控制（如防止兒童傷害、隱私保護）仍然有效。  
- **免除重訓成本**：僅需輕量 LoRA 介面卡，避免完整模型重訓的時間與資源開銷。  

---

## 來源連結  
https://aws.amazon.com/blogs/machine-learning/teaching-models-to-forget-selective-unlearning-with-amazon-nova/  

---

## 延伸閱讀（選填）  
- AWS 官方部落格：Amazon Nova 系列介紹  
- 負責任 AI 原則與最佳實踐（AWS 責任 AI 檔案）  
- Low‑Rank Adaptation (LoRA) 技術概述  

---

## 標籤  
#AWS #AmazonNova #rDPO #Unlearning #ResponsibleAI #LoRA #MachineLearning #AI Safety  

---  

*本文內容僅依據提供的摘要與連結撰寫，未新增未在來源中出現的事實或推測。*
