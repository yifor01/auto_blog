---
title: "Expand More, Shrink Less: Shaping Effective-Rank Dynamics for Dense Scaling in Recommendation"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.23191
score: 96
model: tencent/hy3-preview:free
generated_at: 2026-05-25T21:06:52.344274
---

📌 【Tencent × HKUST(GZ)】當推薦模型變大時，表示卻可能變小？—— RankElastor 如何阻止 Embedding Collapse  

隨著推薦系統規模不斷擴大，如何讓模型在更大的表示空間裡保持豐富的表達力，成為業界共同的挑戰。近期 RankMixer 被證實能透過 token mixing 與 per‑token FFN 交替運算達到可擴展的效能，但卻出現「embedding collapse」：學習到的表示向量有效秩過低，導致表達力受限、擴充後的空間未被充分利用。

🤔 **AI 讓模型變大，卯著變小？**  
RankMixer 的設計在理論上應該能提升表示的秩，但實際觀察發現，隨著網路層數增加，有效秩反而在層間出現阻尼振盪（damped oscillatory trajectory），這正是 embedding collapse 的根源—— token mixing 與 P‑FFN 模組過於剛性，共同抑制了表示光譜的變化。

🧪 **參數化完整混合 + GLU‑改進的 P‑FFN**  
論文提出 RankElastor 架構，包含兩個關鍵元件：  
1. **參數化全混合（parameterized full mixing）**：透過可學習的參數增強 token mixing 的表達力，同時提升光譜穩定性。  
2. **GLU‑改進的 P‑FFN**：採用類似 GLU 的前饋網路結構，使表示光譜在層間更為平滑，減少振盪。  
這兩個設計在理論上可證明對抗 embedding collapse，並在實驗中驗證其有效性。

🔬 **大規模工業資料集驗證**  
作者在大型工業推薦資料集上進行了廣泛實驗，結果顯示 RankElastor：  
- 持續提升推薦效能（相較於 RankMixer 與其他基線）  
- 明確減少 embedding collapse 現象，表示的有效秩更高、更穩定  
- 展現出更佳的擴展行為，適合進一步放大模型規模  

💡 **光譜穩定性是關鍵**  
理論分析指出，參數化全混合讓 token mixing 不再被固定的正交或低秩約束束縛，而 GLU‑式 FFN 則透過門控機制抑制異常特徵的放大，兩者共同使表示向量的特異值光譜在深度網路中更均勻，避免了阻尼振盪。這提供了一種從「光譜視角」思考模型擴展的新方向。

⚠️ **僅驗證於特定架構與資料集**  
目前的實驗聚焦在 RankMixer 家族的變體以及作者所使用的工業推薦資料集；是否適用於其他混合結構（如純 Transformer、純 CNN）或不同領域的資料集，尚需後續工作探討。此外，論文未提供詳細的消融實驗數據，僅聲稱「廣泛實驗」帶來改善。

🎯 **設計時應關注表示光譜**  
對於願意擴大推薦模型的工程師，此研究提醒：單純增加寬度或深度不一定帶來更好的表示力，必須檢查混合與前饋模組是否導致光譜收縮。在實務上，可考慮：  
- 在 token mixing 引入可學習的參數（低秩或全秩變體）  
- 替換傳統 FFN 為 GLU 風格的門控結構，以 stabilise 表示光譜  
- 使用有效秩或光譜熵作為驗證指標，監控訓練過程中的表示健康度  

🔗 **論文連結**  
📝 Expand More, Shrink Less: Shaping Effective-Rank Dynamics for Dense Scaling in Recommendation  
👤 Guoming Li, Shangyu Zhang, Junwei Pan, Wentao Ning, Jin Chen (HKUST(GZ) & Tencent)  
🔗 論文：https://arxiv.org/abs/2605.23191  
💻 程式碼：https://github.com/vasile-paskardlgm/RankElastor  

你在擴大推薦模型時，是否曾注意到表示向量變得「扁平」？歡迎在留言區分享你的經驗與做法 👇  

#推薦系統 #EmbeddingCollapse #RankElastor #Tencent #HKUST #MachineLearning #Scaling #AIResearch
