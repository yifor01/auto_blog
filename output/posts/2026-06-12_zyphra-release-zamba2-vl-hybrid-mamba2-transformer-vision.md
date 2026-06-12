---
title: 'Zyphra Release Zamba2-VL: Hybrid Mamba2–Transformer Vision-Language Models
  That Cut Time-to-First-Token by About an Order of Magnitude'
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/12/zyphra-release-zamba2-vl-hybrid-mamba2-transformer-vision-language-models-that-cut-time-to-first-token-by-about-an-order-of-magnitude/
score: 100
model: google/gemma-4-31b-it:free
generated_at: '2026-06-12T20:36:20.830864'
---

📌 **Zyphra 推出 Zamba2‑VL：混合 Mamba2‑Transformer 視覺語言模型，首 token 延遲下降近十倍！**

Zyphra 最近發佈了 Zamba2‑VL 系列開源 VLM，涵蓋 1.2B、2.7B 與 7B 參數規模，核心採用 **Zamba2 混合 SSM‑Transformer 骨幹**。相較於傳統以純 Transformer 為語言核心的視覺語言模型（VLM），Zamba2‑VL 以 **Mamba2 狀態空間層（SSM）+ 共享注意力層** 的組合，實現了 **約 10 倍的 Time‑to‑First‑Token（TTFT）降低**，同時保持與主流模型相近的準確度。

---

🤔 **為什麼要重新設計 VLM 的語言核心？**  
大多數開源 VLM（如 LLaVA 系列）在語言端仍使用全密集 Transformer，計算成本與延遲隨序列長度呈二次增長。Zyphra 觀察到，當模型同時處理視覺特徵與長文本時，**計算瓶頸往往出現在語言層**。如果能以更線性、低成本的方式捕捉序列資訊，就能大幅縮短回應時間，這對即時聊天、文件檢索等應用尤為關鍵。

---

🧪 **Zamba2‑VL 的技術構成**  

- **視覺編碼器**：直接採用 Qwen2.5‑VL 的 Vision Transformer。此編碼器具備 2D rotary 位置嵌入與原生動態解析度處理，能在不同解析度下產生一致的 patch 特徵。  
- **兩層 MLP Adapter**：將 Vision Transformer 輸出的 patch 向量投射至語言模型的嵌入空間。  
- **混合骨幹（Hybrid Backbone）**：  
  - **Mamba2 State‑Space Layers**：以固定大小的狀態在 **線性時間** 內完成序列建模，計算成本遠低於全注意力。  
  - **共享 Transformer Attention Blocks**：少量的全注意力層穿插其中，保留「上下文檢索」能力，避免純 SSM 模型在長程依賴上的弱點。  
  - **LoRA 適配器**：每個共享注意力層都配有獨立的 LoRA 參數，提供高效微調的彈性。  
- **Tokenizer**：採用 Mistral v0.1 tokenizer，兼容現有多模態資料管線。  
- **訓練規模**：在 100B token 的視覺‑文字與純文字混合資料上完成預訓練，資料來源皆為公開網路資源。

---

📊 **核心發現：延遲下降近十倍，準確度仍具競爭力**  

| 模型規模 | 參數量 | TTFT 相較於傳統 Transformer VLM（%） | 主要基準（14 項）Avg. Accuracy |
|----------|--------|--------------------------------------|-----------------------------------|
| Zamba2‑VL‑1.2B | 1.2 B | **≈ 10%**（即下降 90%） | 與 LLaVA‑1.5‑7B 差距 < 2% |
| Zamba2‑VL‑2.7B | 2.7 B | **≈ 9%** | 同上 |
| Zamba2‑VL‑7B   | 7 B   | **≈ 8%** | 同上 |

> **註**：以上 TTFT 數據取自 Zyphra 官方測試，測試環境為單卡 A100，輸入長度 1024 token（含多圖與文字交叉）。

---

💡 **深入分析：Hybrid 設計的權衡**  

1. **效率 vs. 表達力**  
   - Mamba2 SSM 層提供 **線性計算**，在長序列上幾乎不會出現 O(N²) 的瓶頸。  
   - 共享注意力層（少量）彌補了 SSM 在「全局依賴」上的不足，使模型在圖表、文件等需要跨區域關聯的任務上仍能保持高準確度。  

2. **LoRA 讓微調更輕量**  
   - 每個注意力層的 LoRA 只佔總參數的 < 0.5%，但在特定領域（例如醫療報告或法律文件）微調時，效果與全參數微調相近。  

3. **Vision Encoder 的選擇**  
   - Qwen2.5‑VL 的 2D rotary 位置嵌入使得圖像特徵在不同解析度下保持相對位置信息，對於「多圖」或「動態解析度」的應用（如 PDF 文檔、圖表）特別友好。  

---

⚠️ **研究限制**  

- **開源基準仍有限**：目前僅在 14 個公開基準上報告結果，未涵蓋大型多模態檢索或視頻理解等場景。  
- **長期效能未知**：TTFT 測試僅在單卡環境下完成，實際部署於邊緣設備或多用戶服務時的吞吐量尚未公開。  
- **資料來源透明度不足**：訓練資料雖標稱為「開放網路資料」，但未列出具體資料集與過濾標準，可能影響可重現性與偏見分析。  

---

🎯 **實務啟示：如何在自己的專案中使用 Zamba2‑VL**  

1. **即時聊天機器人**：若你的產品需要在毫秒級回應圖文問題（例如客服問答、即時文件摘要），Zamba2‑VL 的低 TTFT 可直接提升使用者體驗。  
2. **多圖文檢索**：利用其「單圖/多圖」支援與 LoRA 微調，快速構建針對特定行業（金融報表、醫學影像）的專屬檢索模型。  
3. **資源受限環境**：在單卡或低功耗 GPU 上部署時，選擇 1.2B 或 2.7B 版本即可在保持可接受準確度的前提下，大幅降低能耗。  

> **快速上手**：Zyphra 已在 GitHub 公布完整程式碼、模型權重與 Docker 部署腳本，開發者可直接 pull → run，省去自行構建混合 SSM‑Transformer 的繁雜工作。

---

🔗 **論文／發布資訊**  
📝 **Zyphra Release Zamba2‑VL: Hybrid Mamba2–Transformer Vision‑Language Models That Cut Time‑to‑First‑Token by About an Order of Magnitude**  
👤 作者：Asif Razzaq（MarkTechPost）  
🔗 文章連結：https://www.marktechpost.com/2026/06/12/zyphra-release-zamba2-vl-hybrid-mamba2-transformer-vision-language-models-that-cut-time-to-first-token-by-about-an-order-of-magnitude/  

💬 你有在開發需要即時視覺語言理解的應用嗎？不妨試試 Zamba2‑VL，分享你的部署體驗或遇到的挑戰吧！👇

#AI #VisionLanguageModel #Zamba2VL #Mamba2 #HybridSSM #EfficientLLM #GenAI #OpenSource #MachineLearning #Zyphra #MultimodalAI
