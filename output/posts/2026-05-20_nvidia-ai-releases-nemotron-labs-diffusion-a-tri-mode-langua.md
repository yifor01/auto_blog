---
title: "NVIDIA AI Releases Nemotron-Labs-Diffusion: A Tri-Mode Language Model with 6× Tokens Per Forward Over Qwen3-8B"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/20/nvidia-ai-releases-nemotron-labs-diffusion-a-tri-mode-language-model-with-6x-tokens-per-forward-over-qwen3-8b/
score: 109
model: tencent/hy3-preview:free
generated_at: 2026-05-20T21:06:59.309358
---

📌 **NVIDIA 發布 Nemotron‑Labs‑Diffusion：三種解碼模式共享同一組權重，吞吐量最高可達 Qwen3‑8B 的 6×**

你是否曾經在單機或邊端設備上運行大型語言模型，感到 GPU 利用率低、響應延遲高？傳統的自回歸 (AR) 解碼必須一個 token 一個 token 生成，導致每一步只能利用少量核心，而在低批次大小的場景下效能難以發揮。NVIDIA 最新發布的 **Nemotron‑Labs‑Diffusion** 嘗試用一種「三模式」設計來突破這個瓶頸。

🤔 **傳統 AR 解碼的效率瓶頸與平行解碼的可能性**

自回歸語言模型在每個生成步驟中，都必須等待前面所有 token 的 KV cache 完成後才能繼續，這使得在單使用者或邊端部署時（批次大小為 1）硬體利用率普遍偏低。擴散語言模型則嘗試在一次前向傳播中同時去噪多個 token，以提升吞吐量；但過去的擴散模型在準確度上常落後於 AR 模型，原因是其訓練目標未能利用自然語言強烈的左至右先驅。

🧪 **聯合 AR‑擴散目標訓練與三種解碼模式**

Nemotron‑Labs‑Diffusion 在 3B、8B、14B 三種參數規模上提供 base、instruct 與 vision‑language 變體。模型採用 **聯合 AR‑擴散訓練目標**，使得同一組權重能夠在推理時依據部署情境切換下列三種解碼模式，且無需額外的結構修改：

1. **AR 模式** – 標準的左至右自回歸解碼，使用因果注意力；適合高併發雲端服務。  
2. **擴散模式** – 將序列劃分為固定長度的區塊，區塊內 token 雙向注意力，區塊間保持因果關係，因此前面區塊的 KV cache 可被重複使用；此模式能在一次前向中去噪多個 token，提升硬體併行度。  
3. **自推測（self‑speculation）模式** – 透過一個輕量級的取樣器，在每個被遮蔽位置預測模型目前去噪步驟的 top‑1 是否可被接受，從而允許提前確認部分 token，進一步提升吞吐量。

📊 **核心發現：同一權重下的三模式靈活切換與吞吐量提升**

- 模型未提供具體基準分數，但官方宣稱在相似規模的基礎上，**吞吐量最高可達 Qwen3‑8B 的 6×**（即每次前向可處理的 token 數量提升）。  
- 三種模式共享同一組參數，開發者可依據實際場景（雲端高併發、單機低延遲、邊端資源受限）自由切換，無需維護多個模型检查点。  
- 因擴散模式內部採用雙向注意力且區塊間保持因果，能在不犧牲因果性的前提下，重複使用先前區塊的 KV cache，這是實現高吞吐量的關鍵設計。

💡 **深入分析：為何聯合目標能兼容兩種解碼範式**

訓練時同時優化 AR 與擴散目標，使模型學會在左至右因果結構與雙向去噪之間取得平衡。這樣的設計讓模型在 AR 模式下保持傳統語言建模的準確度，而在擴散模式下仍能利用並行去噪提升硬體利用率。自推測取樣器則是在去噪過程中增加一個「信心檢查」步驟，僅在模型對顯著 token 有高信心時才提前確定，從而在不顯著影響準確度的前提下獲取額外的吞吐量增益。

⚠️ **研究限制與後續觀察點**

- 目前公開資訊多為模型架構與釋出說明，尚未見詳細的基準測試報告（例如 MMLU、GSM8K 等標準任務的分數），因此準確度與現有 AR 模型的具體差距尚待社群驗證。  
- 模型的訓練數據規模與混合比例未在摘要中說明，這會影響其在不同語言或專業領域的表現。  
- 作為首次發布的三模式統一架構，長期穩定性、部署工具鏈支援程度（例如 TensorRT、Triton）仍需後續版本進一步打磨。

🎯 **實務啟示：依據場景選擇適當的解碼模式**

- 若您需要在雲端服務中處理大量並發請求，**AR 模式** 能提供熟悉的低延遲、高準確度體驗。  
- 若您的應用對延遲敏感且可接受略微的準確度 trade‑off（例如即時互動、邊端裝置），**擴散模式** 或 **自推測模式** 可顯著提升單次前向的 token 輸出，從而降低每 token 的能源消耗。  
- 由於所有模式共享同一權重，您只需維護一組模型檢查點，即可依據負載動態切換，簡化版本控制與服務擴展流程。

🔗 **論文連結**  
📝 Nemotron‑Labs‑Diffusion: A Tri‑Mode Language Model  
👤 NVIDIA AI Research (發布自 MarkTechPost，作者 Asif Razzaq)  
🔗 https://www.marktechpost.com/2026/05/20/nvidia-ai-releases-nemotron-labs-diffusion-a-tri-mode-language-model-with-6x-tokens-per-forward-over-qwen3-8b/

你目前在專案中是否已經開始嘗試多模式解碼？歡迎在留言區分享你的使用經驗或對此類架構的看法 👇

#NVIDIA #Nemotron #LLM #DiffusionModel #Autoregressive #SelfSpeculation #AIEngineering #機器學習 #深度學習 #HuggingFace #OpenSource #AI新聞
