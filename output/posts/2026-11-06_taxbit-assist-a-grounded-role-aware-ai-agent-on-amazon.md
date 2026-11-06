---
title: 'Taxbit Assist: A grounded, role-aware AI agent on Amazon Bedrock AgentCore'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/taxbit-assist-a-grounded-role-aware-ai-agent-on-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-11-06T22:29:18.876825'
score: 77
---

📌 Taxbit Assist：在 Bedrock AgentCore 上打造「不能亂看稅務資料」的合規助理

TL;DR：Taxbit 用 Bedrock AgentCore 打造可溯源、權限隔離的稅務合規助理。

當客戶問「這個表單狀態是什麼意思？」，過去只能自己翻文件或開支援票；現在超過 55% 問過 Taxbit Assist 的使用者，會在 24 小時內再問下一個問題——這代表助理真的被信任拿來用，而不是問完一次就放棄。

🤔 為什麼不能直接套用一般聊天機器人

Taxbit 是數位資產稅務與會計合規平臺，服務交易所、支付服務商與券商等企業客戶，協助計算損益、收集稅務文件並大規模申報資訊報表。過去儀表板需要的知識分散在公開網站、API 文件與說明中心文章，還有一部分知識根本沒被寫下來過。文章指出這個領域有四項限制塑造了設計方向，其中明確提到的一項是團隊規模小：因此選擇不自己打造與維運 agent 迴圈、對話狀態儲存與 session 隔離，把力氣留給檢索與安全工作。

🧩 架構：身份不經過模型的手

Taxbit Assist 是一個跑在 AgentCore runtime（Amazon Bedrock AgentCore 的能力）上的 Strands Agents SDK 應用程式，整體是一個系統提示詞、一個模型與八個工具組成的小型 Python 應用，打包成 ARM64 容器映像檔，由 AgentCore runtime 從 Amazon ECR 拉取並依需求擴充。選擇 Amazon Bedrock AgentCore 的三個理由：受管的 agent runtime 省去基礎設施維運；內建的 AgentCore memory 省去自建對話狀態儲存；per-session 隔離確保每位使用者的 context 彼此獨立。

這個版本的 agent 沒有讀取客戶稅務資料的權限，只能從產品知識回答問題，唯一能寫入的動作是呼叫者自己的支援票單。關鍵安全設計是「模型不處理身份」：使用者的 email、組織 ID 與角色來自可信任的呼叫服務，在模型看到之前就透過 closure 綁進每個工具，模型可以決定要不要檢查權限，但不能決定檢查誰的權限，因為身份根本不是模型可以設定的參數。使用者輸入在邊界就被清理過，避免 prompt injection 冒充信任的 context。

透過跨區域推論設定檔處理資料駐留：推論設定檔 ID 帶有依部署區域決定的地理前綴，EU 部署的推論留在 EU，US 部署留在 US；另外支援 BYOK（bring your own key）模式，對話歷史等客戶資料用客戶自己的 AWS KMS 金鑰加密。每個部署都把系統推論設定檔包進一個標籤化的應用程式推論設定檔，讓每次模型呼叫都帶上成本分攤標籤，可在 AWS Cost Explorer 依工作負載拆分查看；系統提示詞對每個請求都是逐位元組相同，並以快取檢查點結尾，讓靜態前綴能在不同使用者之間共用 Amazon Bedrock 的 prompt caching，降低延遲與 token 成本。

🧩 知識庫：怎麼把答案做到「可以引用」

核心工程投入在知識庫：一個由 Amazon S3 Vectors 支撐的 Amazon Bedrock 知識庫，用 Cohere Embed English v3 做 embedding，產生 1,024 維的 float32 向量，以 cosine distance 比對，全部是受管服務，團隊不需要自己維運向量資料庫。

內容來自三種來源，各自落在同一個 S3 bucket 下不同的 prefix：公開內容（公開網站、API 文件、說明中心文章，由排程 AWS Lambda 函式爬取，搭配 sitemap 的 lastmod 時間戳記與內容雜湊，每次只處理有變動的部分）、程式碼衍生內容（Lambda 函式直接讀取產品原始碼生成 Markdown 文件，涵蓋儀表板路由、權限閘道、表單資格邏輯與報表設定，因為是由程式碼重新生成，內容會持續保持最新）、以及人工整理內容（手寫文章與經核准的更正，補上自動化來源覆蓋不到的缺口）。sitemap 大約有 400 多個網址，但只有約 70 多個真正適合放進回答用語料庫，光是 `/blogs/` 就佔了 300 多頁行銷內容；把這些行銷內容排除，是團隊在檢索面做的高價值調整之一，而且完全不需要動模型。Amazon EventBridge 以每晚、每週交錯的排程觸發爬蟲，每個 scraper 只有在內容真的有變動時才會觸發 ingestion job；九個 scraper 依 S3 子 prefix（product-public/、product-internals/、curated/）分成三個傘狀資料來源。

🧩 切 chunk 的細節決定答案品質

團隊選用語意切塊（semantic chunking），在自家的檢索測試中表現優於固定大小切塊，但切出來的 chunk 如果取自文件中段，會失去這份文件本身在講什麼的脈絡；在稅務報告領域，這種脈絡往往就是答案本身——一段只適用於非美國申報制度的內容，如果被當成 IRS Form 1099 問題的引用來源，其實是具誤導性的。

解法是用知識庫的 custom transformation hook，跑一個 POST_CHUNKING 的 Lambda 函式，在每個 chunk 前面補上該文件的 H1 標題與第一段（通常會說明這段內容適用的範圍）；前綴長度上限約 128 token（80 字元標題加 300 字元範圍說明）。因為 Cohere Embed English v3 單次輸入上限是 512 token，chunk 主體被限制在 384 token，好讓標題加正文能一起放進這個視窗。一次生產環境的檢測發現，大約 28% 的 chunk 落在 385 到 512 token 之間，如果沒有這個限制，尾端內容會被悄悄截斷。團隊認為這是影響最大的一次檢索面調整：chunk 現在會把自己的適用範圍一起帶進向量索引，而不是只靠文件第一個 chunk 來交代。

兩個實務細節：Amazon Bedrock 要求 custom transformation 的中介儲存必須是跟資料來源不同的 bucket，同一個 bucket 底下不同 prefix 會被拒絕；另外在既有的資料來源上啟用 custom transformation 會強制整個資料來源被取代，等於要重新 ingestion 一次，而不是原地修改。

📊 上線後的訊號

根據 Taxbit 內部的生產分析數據，超過 55% 問過 Assist 問題的使用者，會在 24 小時內再回來問下一個問題。

⚠️ 限制

目前版本的 agent 沒有讀取客戶稅務資料的權限，只能回答產品知識相關問題，唯一能執行的寫入動作是建立呼叫者自己的支援票單。

🎯 實務啟示

把「身份」綁在呼叫端而不是交給模型決定，是值得其他合規場景 agent 借鏡的安全模式：模型可以決定要不要查權限，但永遠不能決定查誰的權限。chunk 切分時把文件層級的範圍資訊（標題、適用情境）一起帶進向量索引，而不是只靠第一個 chunk 承載，對高風險、容易被誤用脈絡的領域（例如法規、稅務）是一個成本不高、效益明顯的改動。爬取公開內容時先做語料範圍篩選，往往比任何模型層的調整更快見效。

🔗 來源
- 標題：Taxbit Assist: A grounded, role-aware AI agent on Amazon Bedrock AgentCore
- 作者／機構：Karan Nayak, AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/taxbit-assist-a-grounded-role-aware-ai-agent-on-amazon-bedrock-agentcore/

#AmazonBedrock #AgentCore #RAG #AIAgent #AWS #Fintech #TaxTech #KnowledgeBase #LLM #EnterpriseAI
