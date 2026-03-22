---
title: "Thinking in Uncertainty: Mitigating Hallucinations in MLRMs with Latent Entropy-Aware Decoding"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2603.13366
score: 116
model: gpt-4o-free
generated_at: 2026-03-18T21:03:44.791026
---

📌 **Latent Entropy‑Aware Decoding：減少多模態推理模型幻覺的新方法**  隨著多模態大型推理模型（MLRM）在視覺問答等任務上的表現不斷提升，幻覺（hallucination）仍是阻礙其可靠應用的關鍵問題。研究者發現，產生幻覺的時刻常伴隨「because」、「however」、「wait」等過渡詞出現，且這些詞彙對應的 token 機率分布處於高熵狀態。這暗示模型在不確定的推理階段可能過度依賴離散的文字輸入，而未充分利用密集的上下文線索。

🤔 **幻覺與高熵狀態的關聯**  
論文觀察到，過渡詞的出現與高熵機率分布強烈相關，認為這些高熵時刻是模型在進行「離散文字推理」時容易走向錯誤的信號。若能在此階段捕捉並利用更豐富的語義資訊，或許能減少幻覺的產生。

🧪 **Latent Entropy‑Aware Decoding (LEAD) 方法**  受疊加表示理論啟發，作者提出一種可即插即用的解碼策略：  
- 在高熵狀態下，使用機率加權的連續嵌入（probability‑weighted continuous embeddings）來保留多個候選語義的疊加資訊；  
- 隨著熵降低，逐漸切換回離散的 token 嵌入；  
- 同時提出先驅視覺錨點注入（prior‑guided visual anchor injection），鼓勵模型在推理過程中更多參考視覺資訊。  

這種「熵感知模式切換」讓解碼過程能自適應地在連續與離散表示之間平衡，藉以利用上下文的深層線索而不喪失最終的離散輸出。

🔑 **核心發現**  
在多個基準測試上，LEAD 能有效降低 MLRM 的幻覺率，而不顯著影響正確答案的產生。實驗顯示該方法在各種多模態推理模型上均具備一致的改善效果，證明其具備良好的泛化能力。

💡 **深入分析：為何熵感知有助於減少幻覺**  
高熵表示模型對後續詞彙的不確定性較大，此時僅依賴單一離散 token 可能導致過早的、片面的決策。透過機率加權的連續嵌入，模型能同時保持多種可能的語義軌跡，等到更多上下文資訊（尤其是視覺線索）變得可靠時，再逐步收斂為確定的離散輸出。如此一來，模型在不確定階段不會被迫做出過早的硬性選擇，從而降低錯誤推理導致的幻覺。

⚠️ **研究限制**  
摘要未提供具體的實驗規模、資料集名稱或基準分數等細節；因此無法評估方法在極端資料規模或特定領域的表現。此外，文中未說明 LEAD 在推理速度或記憶體消耗上的額外開銷，這對實際部署也是重要考量。

🎯 **實務啟示**  
- 開發者可將 LEAD 作為 plug‑and‑play 解碼器直接套用於現有的 MLRM 推理管線，無需重新訓練模型。  
- 在對幻覺敏感的應用（如醫療影像報告、自動客服）中，優先啟用 entropy‑aware 模式切換，可在保持答案正確性的同時提升可靠性。  
- 未來工作可進一步探索不同先驅錨點設計或將此策略擴展至純文字大型語言模型，以檢視其在更廣泛生成任務中的效果。

🔗 **論文連結**  
📝 Thinking in Uncertainty: Mitigating Hallucinations in MLRMs with Latent Entropy-Aware Decoding  
🔗 https://huggingface.co/papers/2603.13366  

你是否曾在使用多模態模型時遇到過因過渡詞導致的不合理輸出？歡迎在留言區分享你的經驗與看法 👇

#AI #多模態 #幻覺減少 #LEAD #HuggingFace #MLRM #解碼策略 #可靠AI
