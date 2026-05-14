---
title: "Orthrus: Memory-Efficient Parallel Token Generation via Dual-View Diffusion"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.12825
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-14T20:54:16.938406
---

📌 Orthrus：雙視擴散，加速 Token 平行生成  

你以為加速 Token 生成就必須犧牲準確度？Orthrus 卻聲稱能兩全其美。  

🤔 **傳統自回歸模型與擴散模型的權衡**  
大型語言模型在生成 Token 時必須一步步遞迴，導致延遲高且 KV 快取佔用大量記憶體。純擴散模型則可以平行產生 Token，但往往難以保證與自回歸推論完全一致的輸出。這種速度與忠實度的trade‑off，一直是 LLM 部署工程師關注的焦點。  

🧪 **雙架構設計：共享 KV 快取與共識機制**  
Orthrus 提出一個雙架構框架，同時保留自回歸 LLM 的核心與擴散模型的平行優勢。兩個子模型共用同一組 KV 快取，並在每個生成步驟透過共識機制確保輸出彼此一致，從而在不改變原始模型參數的前提下，實現「精確」的平行 Token 生成。  

🚀 **核心主張：更快且不損失保真度**  
根據論文摘要，Orthrus 能在保持 exact inference fidelity 的前提下，實現快速的平行 Token 生成。這意味著在理論上可以降低記憶體佔用（因為 KV 心快取被共用）並縮短延遲，而不需要犧牲模型的輸出正確性。  

⚠️ **已知限制：尚需實證驗證**  
目前公開的資訊僅描述方法概念與理論優勢。文中未提供具體的基準測試數據、擴展性實驗或開源程式碼，因此該方法在真實服務環境中的表現仍需進一步驗證。  

🎯 **對工程師的啟示**  
如果後續實驗證明其效能提升，Orthrus 提供了一種在不犧牲準確度的前提下，透過架構設計降低記憶體與延遲的可行路徑。這對於追求高吞吐、低延遲的 LLM 服務部署尤其具參考價值。  

🔗 **論文連結**  
📝 Orthrus: Memory-Efficient Parallel Token Generation via Dual-View Diffusion  
🔗 https://huggingface.co/papers/2605.12825  

你對這種「自回歸＋擴散」的混合策略有什麼看法？歡迎在留言區分享你的想法 👇  

#AI #LLM #DiffusionModel #TokenGeneration #Orthrus #HuggingFace #機器學習 #深度學習 #工程實務
