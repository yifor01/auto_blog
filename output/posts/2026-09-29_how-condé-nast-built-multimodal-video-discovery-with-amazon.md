---
title: How Condé Nast built multimodal video discovery with Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-conde-nast-built-multimodal-video-discovery-with-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-09-29T21:47:59.880279'
score: 80
---

📌 Condé Nast 把 14 萬支影片的搜尋時間從 250 分鐘砍到 2 分鐘

TL;DR：Condé Nast 用 Amazon Bedrock 上的多模態 embedding 模型，讓編輯團隊用自然語言就能搜到影片片段。

編輯想找「帶著平靜背景的瑜伽入門內容」，過去得靠人工在超過 14 萬支影片裡憑標題和描述硬翻，平均花掉 250 分鐘。Condé Nast 與 AWS Generative AI Innovation Center（GenAIIC）合作後，把這個時間壓到 2 分鐘以內。

🤔 關鍵字搜尋在影片庫裡為何失靈

Condé Nast 旗下 Vogue、GQ、Vanity Fair、Wired 等品牌的編輯團隊，過去只能靠標題與描述找影片，一旦內容沒有被人工下對關鍵字，就永遠沉在檔案庫裡不會被發現，團隊也高度依賴特定人員的「機構記憶」，一旦這些人不在，資產就找不到。問題的核心很結構性：編輯不會搜尋「yoga_tutorial_march_2024.mp4」，而是搜尋「帶著平靜背景的瑜伽入門內容」或「時裝週幕後花絮」——這需要的是理解語意與意圖的向量搜尋，而非字串比對。

🧩 兩個解耦的平面：吃資料的與答問題的

團隊選擇 TwelveLabs Marengo 這個 embedding 模型，原因是它能同時將影片的視覺、音訊與逐字稿三種訊號聯合編碼成向量，並透過 Amazon Bedrock 存取——Bedrock 用單一 API 提供多種基礎模型，同時套上 IAM 存取控管、VPC 網路隔離與 CloudTrail 稽核，讓團隊不必自行建置與維運模型服務基礎設施。向量索引則交給 Amazon OpenSearch Service，其 managed k-NN 搜尋支援多可用區（multi-AZ）複寫與 metadata 過濾的混合查詢，讓團隊在 14 萬支影片規模下做低延遲相似度搜尋，而不必自己管理搜尋叢集。

架構上分成兩個互相解耦的平面：一個是非同步的擷取與索引管線，負責把新上傳的影片變成可被搜尋的向量；另一個是同步的查詢與服務層，負責把使用者的自然語言查詢即時轉成向量搜尋並回傳精確時間戳。管線採事件驅動、端到端編排，具備每一步的重試邏輯、跨片段的平行處理與完整可追蹤性——這些能力在初期針對 14 萬支影片的回填處理中被大量倚賴。

💡 三個規模化過程中踩出來的經驗

- **片段長度需要反覆試驗**：片段太短會遺失脈絡，太長則會稀釋語意訊號，團隊透過對真實編輯查詢的反覆基準測試，才找到兼顧精確度與召回率的長度。
- **非同步生成 embedding 是硬需求**：若對 14 萬支影片同步呼叫 embedding 模型會造成明顯瓶頸，團隊改用 AWS Step Functions 非同步呼叫，讓管線能處理回填積壓而不阻塞，這也成為後續持續擷取的固定模式。
- **從一開始就做 multi-AZ，比事後補強便宜**：對編輯團隊整個工作日都仰賴的系統來說，即使短暫中斷也會直接轉化為生產力損失。

📊 量化的業務成果

Condé Nast 於 2026 年 5 月進行了一場基準測試工作坊，量化這套方案的影響：
- 單次內容探索任務時間：從平均 250 分鐘降至不到 2 分鐘，降幅達 99.2%
- 估計年度營運成本節省：約 80 萬美元
- 方案已在正式環境運行六個月，期間即便擷取管線在重新處理回填內容或更新時，正式搜尋服務仍維持可用

Condé Nast 全球創意最佳化資深總監 Billy Keenly 表示：「AWS 團隊，連同 GenAI 與 TwelveLabs 的與會者，協助我們清楚而簡潔地說明了這個商業案例。我對於未來能在工作流程目標上取得更多進展感到樂觀。」

🎯 實務啟示

這個案例的架構決策值得其他坐擁大型影片庫的團隊（廣播、串流平臺、體育聯盟、企業媒體團隊）參考：把「昂貴的批次 embedding 生成」與「低延遲的查詢服務」拆成兩個獨立平面，是能同時撐住大規模回填與即時查詢體驗的關鍵設計；而在專案初期就投入 multi-AZ 與非同步管線，往往比日後重構划算得多。

🔗 來源
- 標題：How Condé Nast built multimodal video discovery with Amazon Bedrock
- 作者／機構：Mariah Miller, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/how-conde-nast-built-multimodal-video-discovery-with-amazon-bedrock/

#AmazonBedrock #OpenSearch #MultimodalAI #VideoSearch #TwelveLabs #MediaTech #GenerativeAI #VectorSearch #AWS #EnterpriseAI
