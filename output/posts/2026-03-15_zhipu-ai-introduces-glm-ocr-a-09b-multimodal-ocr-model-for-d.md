---
title: "Zhipu AI Introduces GLM-OCR: A 0.9B Multimodal OCR Model for Document Parsing and Key Information Extraction (KIE)"
source: MarkTechPost
url: https://www.marktechpost.com/2026/03/15/zhipu-ai-introduces-glm-ocr-a-0-9b-multimodal-ocr-model-for-document-parsing-and-key-information-extraction-kie/
score: 108
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-15T16:27:05.307237
---

📌 **GLM-OCR 問世：0.9B 參數實現高效文檔解析，破解 OCR 部署難題**

當你在思考「為什麼文檔 OCR 還是個難啃的工程問題」時，Zhipu AI 與清華大學的研究團隊給出了答案：不是模型不夠大，而是方法不夠巧。

🤔 **傳統 OCR 的兩難困境**

你可能遇過這種場景：OCR 工具在純文字圖片上表現完美，但一遇到包含表格、公式、程式碼區塊、印章和結構化欄位的真實文檔，準確率就直線下降。這是因為傳統 OCR 擅長文字轉錄，但對複雜版面和結構化資訊的處理卻捉襟見肘。

而最近的多模態大語言模型雖然改善了文檔理解能力，但它們體積龐大、採用標準自迴歸解碼，在邊緣部署和大規模生產中成本過高。

🧪 **GLM-OCR 的創新解法**

GLM-OCR 的關鍵創新在於 Multi-Token Prediction (MTP) 技術。傳統自迴歸模型一次預測一個 token，對於 OCR 這種輸出通常具有確定性和局部結構性的任務並不理想。GLM-OCR 則一次預測 10 個 token，在推理時平均每步生成 5.2 個 token，實現約 50% 的吞吐量提升。

為了控制記憶體開銷，模型採用跨草稿模型的參數共享方案。整體架構包含 0.4B 的 CogViT 視覺編碼器、輕量級跨模態連接器，以及 0.5B 的 GLM 語言解碼器，參數總量僅 0.9B。

🎯 **兩階段版面解析策略**

GLM-OCR 採用兩階段處理策略：首先進行版面解析，然後提取關鍵資訊。這種設計讓模型能更有效地處理複雜文檔結構，而不只是單純的文字轉錄。

⚡ **真正的部署價值**

GLM-OCR 的意義在於：它不是將通用多模態模型硬套用到 OCR 任務上，而是從部署需求出發，為 OCR 工作負載量身打造。這讓高效文檔解析成為可能，而不必付出資源過度的代價。

🔗 **論文連結**
📝 GLM-OCR: A Compact Multimodal Model for Document Parsing and Key Information Extraction
👤 Zhipu AI & Tsinghua University
🔗 arxiv.org/abs/2603.XXXXX (請查閱原論文獲取完整連結)

你認為 0.9B 參數能否滿足企業級文檔處理需求？歡迎分享你的看法 👇

#AI #OCR #DocumentAI #ZhipuAI #Multimodal #MachineLearning #TechInnovation
