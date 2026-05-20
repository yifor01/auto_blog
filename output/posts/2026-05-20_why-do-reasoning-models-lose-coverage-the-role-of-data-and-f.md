---
title: "Why Do Reasoning Models Lose Coverage? The Role of Data and Forks in the Road"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.17026
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-20T21:24:18.139185
---

📌 **Why Do Reasoning Models Lose Coverage? The Role of Data and Forks in the Road**  
（HuggingFace Daily Papers 推薦）

你是否曾看到一個原本能夠覆蓋多種推理路徑的模型，在經過監督微調後，卻變得「只會走一條路」？這篇論文指出，這種覆蓋率（coverage）縮減的根源，訓練資料中的「決策點」決策情境。

🎣 **折疊區優化 (The Hook)**  
當我們用更多資料微調模型，期望它變得更強，卻可能讓它的推理多樣性悄悄變薄——這到底是什麼在作祟？

🤔 **研究背景**  
監督微調（Supervised Fine‑Tuning, SFT）是提升推理模型能力的常見做法，但在實務上，工程師常觀察到模型在特定任務上的「覆蓋率」下降，也就是模型不再能夠生成先前涵蓋的多樣化推理路徑。這會影響模型的穩健性與泛化能力，尤其在需要多路徑推理的場景（如數學證明、程式除錯）中顯得尤為關鍵。

🧪 **研究設計**  
論文聚焦於監督微調階段，分析訓練資料中出現的「決策點」（decision‑point scenarios）—-也就是模型必須在多個可能的推理方向中做選擇的樣本。作者假設這類樣本的不均衡分布會導致模型在微調過程中偏向某一條路徑，從而造成覆蓋率縮減。為驗證此假設，他們提出了兩種緩解策略：  
1. **有針對性的資料合成**（targeted data synthesis）—-人工增加或重新平衡決策點樣本的多樣性；  
2. **鼓勵多樣性的解碼機制**（diversity‑encouraging decoding）—-在生成階段引入機制，使模型不易過度收斂於單一路徑。

📌 **核心發現**  
- 監督微調時，訓練資料中的決策點情境是導致推理模型覆蓋率縮減的主要因素。  
- 透過針對性資料合成與鼓勵多樣性的解碼，可有效減緩甚至逆轉這種覆蓋率下降的趨勢。

💡 **深入分析**  
決策點之所以重要，是因為它們代表了模型在推理過程中需要「分岔」的瞬間。若訓練資料中某一分支被過度呈現，模型在參數更新時會獲得較強的梯度指向該分支，長期以來會使其他分支的機率被壓縮。這種現象類似於「路徑依賴」（path dependency），在優化過程中容易造成局部最優解。因此，從資料層面增加決策點的多樣性，或在解碼時引入鼓勵探索的機制（如溫度調整、多樣性束搜尋），能夠在不犧牲已學得知識的前提下，保持模型的推理寬度。

⚠️ **研究限制**  
摘要中未詳細說明實驗規模、使用的基礎模型種類或具體的評估指標；因此，目前無法從提供的資訊中判斷該結論在不同模型架構、訓練時長或其他微調情境（如強化學習）中的普遍性。進一步的實驗驗證與更完整的 ablation 研究將有助於釐清這些邊界條件。

🎯 **實務啟示**  
- 在進行監督微調前，檢查訓練資料中決策點的分布是否均衡；若發現偏斜，可考慮合成補充樣本或重新採樣。  
- 在推理或生成階段，嘗試使用能提升輸出多樣性的解碼策略（例如提升溫度、使用 nucleus sampling 或多樣性束搜尋），以減少模型過早收斂於單一路徑的風險。  
- 對於需要高覆蓋率的應用（如程式合成、數學題解），將上述兩種方法結合使用，可能是提升模型可靠性的實用做法。

🔗 **論文連結**  
📝 Why Do Reasoning Models Lose Coverage? The Role of Data and Forks in the Road  
👤 作者／機構：未在摘要中顯示  
🔗 https://huggingface.co/papers/2605.17026  

你在微調推理模型時，是否曾注意到覆蓋率的變化？歡迎在留言區分享你的經驗與觀察 👇

#AI #ReasoningModels #SupervisedFineTuning #ModelCoverage #HuggingFace #MachineLearning #LLM #DataSynthesis #DecodingStrategies
