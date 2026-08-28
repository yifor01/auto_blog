---
title: Introducing OpenAI models on Amazon Bedrock for in-country inferencing in India
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/introducing-openai-models-on-amazon-bedrock-for-in-country-inferencing-in-india/
model: claude-code/sonnet
generated_at: '2026-08-28T18:08:34.428289'
score: 80
---

📌 OpenAI GPT-5.6 進駐 Amazon Bedrock 印度區:運算全程不出境

TL;DR:Amazon Bedrock 新增印度地理跨區推論,讓 GPT-5.6 Terra 與 Luna 的運算資料留在印度境內完成。

金融服務、醫療與公部門常有「資料不能出境」的硬性要求,這類法規邊界過去往往意味著只能用境內自建模型。現在 Amazon Bedrock 把 OpenAI 的 GPT-5.6 模型直接搬進印度境內運算,提供了另一條路徑。

🤔 **在地資料處理需求,遇上跨區容量調度**

Amazon Bedrock 現在在印度支援 OpenAI GPT-5.6 系列模型 Terra 與 Luna,並搭配印度地理跨區推論(India geographic cross-Region inference)。兩個模型都提供 100 萬 token 的上下文窗口,接受文字與圖片輸入、輸出文字,可以處理長文件、大型程式碼庫與圖文混合的請求,且處理過程全程留在印度境內。

🧩 **inference profile:容量調度與資料落地可以兼得**

跨區推論(cross-Region inference)本質上是一種容量機制:它把推論請求自動路由到多個 AWS Region,讓應用程式在流量高峰時能取用更大的運算池,而不必自行在每個 Region 管理容量。印度地理跨區推論把路由範圍限定在印度境內的 Region,例如亞太(孟買)ap-south-1 與亞太(海德拉巴)ap-south-2 之間,呼叫時以其中一個印度 Region 作為來源,Bedrock 會依容量狀況把請求路由到另一個印度 Region,藉此在符合資料落地要求的前提下擴充吞吐量。計費與配額用量都算在來源 Region 的帳戶上,Amazon CloudWatch 與 AWS CloudTrail 的日誌也只記錄在來源 Region,監控不會分散。除了印度地理 profile(in. 前綴),Bedrock 也提供路由到全球任意支援 Region、以追求最大容量為目標的全域跨區推論(global. 前綴),但若工作負載有在地資料處理需求,官方建議改用印度 profile 以確保資料留在境內。

🧩 **多套 API 相容,並支援 prompt caching 折扣**

GPT-5.6 模型透過 bedrock-runtime endpoint 提供服務,同時支援 Bedrock 原生的 InvokeModel 與 Converse API、OpenAI 相容的 Responses 與 Chat Completions API,以及 Anthropic Messages API,Guardrails、智慧 prompt 路由等 Bedrock 功能也建在這個 endpoint 上。若應用程式已經在呼叫 OpenAI 模型,只需把 OpenAI SDK client 指向孟買或海德拉巴的 Bedrock endpoint,並把印度地理 inference profile ID 當作 model 參數傳入即可;身分驗證可用標準 AWS 憑證,或用 Bedrock API key 當 bearer token(正式環境建議用 aws-bedrock-token-generator 套件動態產生短期 API key,不需儲存靜態金鑰)。資料安全上,Bedrock 對這類模型採零資料保留(zero data retention)模式,預設不儲存輸入輸出內容,但被自動濫用偵測分類器標記的內容會保留供離線審查。若對話有穩定重複的長前綴(如 system instruction、知識庫片段、few-shot 範例),GPT-5.6 在 Bedrock 上支援 prompt caching,快取命中的讀取享 9 折(90% 折扣),最小前綴長度為 1,024 token,且印度地理 profile 同樣適用這項折扣,不會因為資料落地要求而失去省錢空間。

🎯 **實務啟示**

對已經在用 OpenAI SDK 的團隊來說,遷移到 Bedrock 印度區主要是換 base URL 與驗證方式,程式邏輯改動不大,卻能換來資料落地合規與容量調度的雙重保障。若應用場景橫跨多個 Region 或有大量重複上下文(RAG、agent 這類多輪對話),值得評估把 prompt caching 一併納入,搭配印度地理 profile 在合規邊界內把成本壓下來。

🔗 **來源**
- 標題:Introducing OpenAI models on Amazon Bedrock for in-country inferencing in India
- 作者／機構:Sahil Verma / AWS Machine Learning Blog
- 連結:https://aws.amazon.com/blogs/machine-learning/introducing-openai-models-on-amazon-bedrock-for-in-country-inferencing-in-india/

#AmazonBedrock #OpenAI #DataResidency #CloudAI #LLM #CrossRegionInference #PromptCaching #AWS #India #EnterpriseAI
