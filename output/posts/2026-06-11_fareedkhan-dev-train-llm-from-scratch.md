---
title: FareedKhan-dev/train-llm-from-scratch
source: GitHub Trending
url: https://github.com/FareedKhan-dev/train-llm-from-scratch
score: 108
model: google/gemma-4-31b-it:free
generated_at: '2026-06-11T00:36:04.355007'
---

📌 【GitHub Trending】從零手寫 Transformer，單卡就能跑「千萬參數」大語言模型！

想在自己的 GPU 上練出一個能寫段落、解數學題的 LLM，而不依賴 HuggingFace、TRL、PEFT 這些「即服務」套件？FareedKhan‑dev 最近在 GitHub 上釋出了 **train‑llm‑from‑scratch**，完整實作了《Attention Is All You Need》中的 Transformer，並延伸到現代對齊流程（SFT → Reward Model → PPO/DPO → GRPO），全程純 PyTorch 手寫，支援多卡 DDP + bf16。

---

🤔 **從「預訓練」到「可對話」的全流程，真的只要一張 GPU？**  
大多數開源 LLM 都只提供預訓練好的權重或是需要大量算力的腳本。這個 repo 宣稱「單卡即可訓練百萬‑千萬參數模型」，且還內建 **post‑training suite**（SFT、Reward Model、PPO、DPO、GRPO/RLVR），讓你可以一步步把模型從「會寫」變成「會思考」。

---

🧪 **核心實驗設計 & 代碼結構**  
- **Transformer 核心**：從 Multi‑Head Attention、Position‑wise MLP、LayerNorm 到完整的 Transformer Block，全部自行實作，未使用 `torch.nn.Transformer` 或 `transformers` 套件。  
- **訓練規模**：示例模型 13 M 參數，使用單張 NVIDIA RTX 3080（或等效）即可完成預訓練 → SFT → Reward Model → PPO/DPO → GRPO 全流程。  
- **資料來源**：公開指令微調資料集（Alpaca、Dolly、Anthropic HH‑RLHF、UltraFeedback、GSM8K）全部在 repo 中提供下載腳本，保證可重現。  
- **多卡支援**：採用 PyTorch Distributed Data Parallel (DDP) + bf16 混合精度，理論上可擴展至多卡訓練更大模型。  
- **使用說明**：`POST_TRAINING.md` 詳列從環境建置、資料前處理、預訓練、微調到 RL 迭代的完整步驟，適合想要自行玩轉 LLM 對齊的工程師。

---

🚀 **最令人驚訝的結果 — 13 M 參數模型的生成樣本**  
> *In 1978, the park was returned to the factory‑plate that the public share to the lower of the electronic fence…*  

雖然文字仍帶有典型的小模型幻覺（事實與虛構混雜），但在千萬參數規模下已能產生相當流暢的敘事，證明「從頭」實作與微調的可行性。

---

💡 **深入分析：為何純手寫仍有價值？**  
1. **透明度**：所有算子皆自行實作，對於想了解 Attention 計算、梯度流向的研究者是絕佳教學資源。  
2. **可裁剪性**：不被高階抽象層限制，想在注意力機制上加入自訂稀疏化或長序列技巧時，直接在 `attention.py` 中修改即可。  
3. **低門檻入門**：省去安裝大型依賴（transformers、accelerate），只需要 PyTorch、Python 即可跑起來，對於資源受限的個人開發者非常友好。

---

⚠️ **研究限制 & 實務挑戰**  
- **模型規模**：目前示例僅到 13 M 參數，若要突破百億規模仍需多卡叢集與更複雜的記憶體管理。  
- **訓練時間**：單卡預訓練約需數十小時（視資料量與 batch 大小而定），對於想快速驗證概念的使用者仍可能偏慢。  
- **對齊品質**：PPO/DPO 等 RL 演算法的超參數調校相當敏感，repo 提供的默認配置在小模型上表現尚可，放大到更大模型時仍需自行調整。  
- **缺乏官方驗證**：雖然作者提供了完整說明與生成樣本，但尚未有第三方基準測試（如 HELM、MT‑Bench），結果可信度仍待社群驗證。

---

🎯 **實務啟示：怎麼把它套到你的專案？**  
1. **快速原型**：利用 13 M 參數模型作為內部知識庫問答或簡易聊天機器人的基礎，省去付費 API 成本。  
2. **教育訓練**：在 AI 研討會或大學課程中，直接帶學生跑「從頭」的 Transformer，讓他們體會每個模組的作用。  
3. **自訂對齊**：如果你的公司有專屬指令集（如金融報告、醫療諮詢），可直接使用 repo 中的 SFT 與 Reward Model pipeline，快速產出符合業務需求的微調模型。  
4. **探索新演算法**：在純手寫的基礎上加入稀疏注意力、混合專家（MoE）或長序列記憶機制，作為研究原型。

---

🔗 **論文與程式碼連結**  
📝 Repo：**train‑llm‑from‑scratch**  
👤 作者：FareedKhan‑dev (GitHub Trending)  
🔗 https://github.com/FareedKhan-dev/train-llm-from-scratch  

📂 主要文件：`POST_TRAINING.md`（完整對齊流程說明）  
🧩 相關資料集腳本與模型檢查點均在 repo 中提供。

---

👉 你有興趣在自己的 GPU 上「從零」打造 LLM 嗎？或是已經在嘗試微調小模型，想交流最佳參數設定？歡迎在下方留言分享你的實驗心得或問題 👇

#AI #LLM #Transformer #PyTorch #OpenSource #GitHubTrending #機器學習 #模型對齊 #深度學習 #自建LLM
