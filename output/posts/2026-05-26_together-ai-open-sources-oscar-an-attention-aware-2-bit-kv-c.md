---
title: "Together AI Open-Sources OSCAR: An Attention-Aware 2-Bit KV Cache Quantization System for Long-Context LLM Serving"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/25/together-ai-open-sources-oscar-an-attention-aware-2-bit-kv-cache-quantization-system-for-long-context-llm-serving/
score: 120
model: tencent/hy3-preview:free
generated_at: 2026-05-26T20:44:05.611980
---

📌 **Together AI 開源 OSCAR：注意力感知的 2‑bit KV Cache 量化，緩解長文本 LLM 記憶體壓力**

你以為把 KV Cache 壓到 2‑bit 就能大幅省記憶體？事實上，這樣做常常讓模型失效，因為極端的離群值會把量化範圍浪費在尖峰上，導致注意力品質嚴重下降。現在，Together AI 提出了一種「注意力感知」的解法，讓 2‑bit 量化在長文本場景下也能使用。

🤔 **長文本推理讓 KV Cache 成為記憶體瓶頸**  
在自回歸解碼過程中，KV Cache 會隨著上下文長度、批次大小與模型深度線性增長。當同時處理數十條請求、上下文達到 100K token 時，KV Cache 會佔用大量 GPU 記憶體，直接限制了可達成的批次大小並增加記憶體傳輸開銷。傳統的量化方法要麼在 INT2 精度下準備崩潰，要么需要自訂的佈局，無法與現有的 paged KV‑Cache 系統相容。

🧪 **OSCAR：從注意力統計導出的旋轉量化**  
Together AI 的 OSCAR（Offline Spectral Covariance‑Aware Rotation）觀察到，KV 激活中只有少數通道擁有極大的離群值，其餘通道表現良好。直接的 INT2 量化會讓這些離群值主導尺度因子，使一般數值被壓縮到只有其一或兩個可用等級，嚴重影響注意力品質。  
OSCAR 的核心是：在量化之前，先根據 **注意力本身的統計資訊** 計算一個固定的正交旋轉（類似 Hadamard 變換但具資料感知），將離群能量分散到所有通道，進而讓量化誤差集中在注意力上較不重要的方向。這樣的「注意力感知旋轉」解決了既有 INT2 方法在準確度與相容性上的兩難問題。

📊 **OSCAR 讓 2‑bit KV Cache 量化變得可行**  
透過上述旋轉，OSCAR 能在保持注意力品質的同時，將 KV Cache 壓到 2‑bit 精度。因為它與現有的 paged KV‑Cache 系統相容，開發者可以直接將其 plug‑in 到現有的 LLM 服務堆疊，從而在不犧牲準確度的前提下，提升可處理的批次大小並降低 GPU 記憶體佔用。這意味著在長文本場景下，服務吞吐量可得到顯著提升，而硬體成本則相應下降。

💡 **為何注意力感知是關鍵？**  
傳統的旋轉量化是資料無感知的：它只會把離群值的能量均勻散開，但無法確保散落的量化誤差落在對注意力影響較小的維度。OSCAR 透過從注意力統計中導出旋轉矩陣，使得量化誤差被主動導向對最終輸出貢獻較低的特徵方向，從而在極低的 bit-width 下仍能保持模型的推論品質。

⚠️ **目前已知的限制**  
- 公開資訊主要來自 Together AI 的開源宣布與技術部落格，尚未見詳細的基準測試報告（例如具體的批次提升比例或延遲影響）。  
- 實際效果可能隨模型架構、量化實作細節與服務軟體堆疊而異，仍需在更多模型與場景下進行驗證。  
- 本文未涉及訓練端的適用性，僅著重於推理階段的 KV Cache 壓縮。

🎯 **實務上的啟示**  
- 如果你的服務需要處理極長的上下文（如檔案摘要、長對話或程式碼理解），可以評估將 OSCAR 整合到現有的推理引擎中，以提升批次處理能力。  
- 開源碼讓社群能直接檢視與改良旋轉計算方式，進一步適配不同的硬體或量化後端。  
- 在部署前，建議先在目標模型上進行離線準確度驗證，確認注意力感知旋轉在實際工作負載下的表現符合預期。

🔗 **論文／資料連結**  
📝 Together AI Open-Sources OSCAR: An Attention‑Aware 2‑bit KV Cache Quantization System for Long‑Context LLM Serving  
👤 Asif Razzaq (MarkTechPost)  
🔗 https://www.marktechpost.com/2026/05/25/together-ai-open-sources-oscar-an-attention-aware-2-bit-kv-cache-quantization-system-for-long-context-llm-serving/

你目前的長文本 LLM 服務是否也受到 KV Cache 記憶體的限制？歡迎在留言區分享你的看法或實作經驗 👇

#TogetherAI #OSCAR #LLM #KVCache #量化 #長文本 #AI推理 #開源 #GPU優化 #MarkTechPost
