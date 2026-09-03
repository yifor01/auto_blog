---
title: 'NeoMME: an efficient Multimodal-native and Multilingual Encoder'
source: HuggingFace Blog
url: https://huggingface.co/blog/Hcompany/neomme
model: claude-code/sonnet
generated_at: '2026-09-03T20:09:42.228128'
score: 111
---

📌 【Hcompany開源】NeoMME：從零訓練的雙向多模態編碼器

TL;DR：260M／800M參數的多模態編碼器捨棄預訓練視覺塔，單一Transformer就同時處理文字與圖片。

多數視覺文件檢索模型都是拿生成式VLM改裝而來，先接一個預訓練視覺塔，再透過projector把特徵塞進語言模型的輸入空間。NeoMME反其道而行：整個模型從零訓練，圖片與文字從第一層就走同一條計算路徑。

🤔 **背景：檢索任務真的需要VLM的架構嗎？**

檢索、分類、token標註這類任務不需要自迴歸生成文字，因此不需要causal decoder，也不用背負VLM的參數與計算開銷。ModernBERT為雙向encoder帶來效率與訓練上的改進；ModernVBERT套用了ModernBERT式的雙向文字encoder，但仍保留一個獨立預訓練的SigLIP2視覺塔。NeoMME想再往前一步：不基於任何既有的預訓練視覺塔、文字encoder或decoder，直接設計並訓練一個原生多模態encoder。

🧩 **方法與架構：一個Transformer同時吃文字與影像patch**

NeoMME有260M與800M兩種尺寸，共用同一套架構設計：

- 原生多模態輸入：文字使用factorized token embeddings，影像則切成32×32的不重疊patch，經一個小型MLP投影後，與文字一起進入同一個Transformer encoder
- 動態影像解析度：影像維持原本的長寬比與尺寸，讓模型能在資訊密度高的文件頁面上用更多token，在內容較少的小圖上用較少token
- 長雙向context：兩種模型的context長度都是16,384 token，足以容納最多兩張3840×2160的4K UHD影像；多數層使用對稱滑動窗注意力，每第六層與最後一層則使用全域注意力
- 現代化encoder元件：採用grouped-query attention、query-key normalization、gated attention、2D旋轉位置編碼（RoPE）、squared-ReLU MLP等近期改進
- 多語言文字：從零訓練一個131k詞彙量的BPE tokenizer，語料涵蓋多語言文字、程式碼、數學與機器產生的影像文字轉錄

🧩 **資料與訓練：用「文字遮罩」逼模型看圖**

NeoMME從零開始以離散遮罩擴散（masked discrete-diffusion）作為文字去噪目標進行預訓練。純文字樣本的遮罩比例在0到1之間均勻取樣，多模態樣本則將遮罩比例限制在0.3到1之間，且影像patch始終保持可見，模型要重建被遮住的文字。輕度遮罩時，模型往往能單靠上下文猜出被蓋住的字，例如「貓」可以合理補在「The [MASK] sat on the mat」裡而不需要圖片；但高遮罩比例移除了這種純語言的捷徑，逼模型必須依賴可見的影像證據。

預訓練資料混合了多語言文字、程式碼、數學、自然影像與文件影像，每個模型處理約5,240億個打包後的token，其中2,900億來自純文字樣本，這個文字量預算相較ModernBERT的2兆token明顯精簡，因此團隊選擇了NorMuon優化器來提升資料效率。

🧩 **NeoMME-Retriever：一次前向傳遞，兩種embedding**

團隊採用ColPali的頁面影像方法對NeoMME進行視覺文件檢索的微調，直接把文件頁面截圖當成排序對象，跳過從PDF擷取文字所需的OCR前處理，保留版面、圖表、表格、字型等OCR難以完整捕捉的視覺線索。NeoMME-Retriever在backbone之上加了兩個聯合訓練的head：dense head將hidden state做mean pooling後正規化成單一向量；late-interaction head則把每個文字token或影像patch分別投影成128維的正規化向量，保留查詢與影像區域之間更細緻的局部對應。單次前向傳遞就能同時取得兩種表示，團隊建議一般情境優先用late-interaction（可搭配開源套件NextPlaid使用），若語料庫非常龐大，則可先用dense embedding做近似最近鄰（ANN）檢索，再用late-interaction對候選結果重排序。

📊 **效能數據**

在配對2048×2048影像輸入、單張NVIDIA L40S GPU的條件下，260M模型每秒可編碼約51頁，吞吐量約為ColModernVBERT的兩倍。透過階層式token pooling與非對稱量化，late-interaction索引儲存空間從每頁約1.5MB降到6kB，縮小255倍，同時保留超過95%的基準nDCG@10。在ViDoRe v3上，兩種尺寸都落在nDCG@10與模型大小的Pareto前緣：NeoMME-Retriever-260M達到0.523，是800M以下模型中的最高分，與ColQwen2.5僅相差0.002，但參數量少了約14倍；800M版本則達到0.556（素材在此處後續說明中斷，未提供更完整的對比數據）。

💡 **深入分析**

放棄預訓練視覺塔的代價，是需要更審慎設計的訓練目標（如遮罩比例的分層策略）與更高效的優化器來彌補訓練資料量的落差。但換來的是影像與文字共用同一條計算路徑，理論上能讓預訓練、微調、平行化與部署都更單純，而不需要分別維護一套視覺塔與語言模型的組合。

🎯 **實務啟示**

對正在打造視覺RAG或文件檢索系統的工程師，NeoMME值得評估的重點在於索引儲存成本：255倍的壓縮幅度在大規模語料庫場景下影響顯著。模型已釋出於Hugging Face Transformers並採Apache 2.0授權，整合門檻相對低。

🔗 **來源**
- 標題：NeoMME: an efficient Multimodal-native and Multilingual Encoder
- 作者／機構：Tony Wu、Aurélien Lac（Hcompany）
- 連結：https://huggingface.co/blog/Hcompany/neomme

#NeoMME #MultimodalAI #Encoder #VisualRetrieval #ColPali #OpenSource #HuggingFace #Embeddings #DocumentAI #Multilingual
