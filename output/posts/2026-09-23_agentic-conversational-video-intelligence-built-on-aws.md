---
title: Agentic conversational video intelligence built on AWS
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/agentic-conversational-video-intelligence-built-on-aws/
model: claude-code/sonnet
generated_at: '2026-09-23T20:36:24.431879'
score: 89
---

📌 影片堆積如山，AWS 用 Agent 讓你直接開口問答

TL;DR：AWS 展示一套 agentic 架構，讓 LLM 在執行期動態決定呼叫哪些 AI 服務來回答影片相關問題。

會議錄影堆在共用硬碟裡沒人整理，監視器錄了好幾週沒人回看，現場勘查影片存進物件儲存後就被遺忘——這些影片裡其實藏著有價值的資訊，但傳統做法是要嘛人工看過一遍，要嘛針對每種問題各自建一條機器學習 pipeline。AWS 這篇文章介紹的方案，用一個 agent 取代了這整套固定流程。

🤔 每種問題都要一條新 pipeline，這個模式撐不住

傳統影片分析應用會預先定義固定的處理流程：上傳、轉錄、視覺分析、呈現結果，每支影片不論用戶實際想問什麼，都得跑完整套流程，而且使用者得等整條 pipeline 跑完才能開始提問。

🧩 用 Strands Agents SDK 讓模型自己決定呼叫誰

這套方案改用 Strands Agents SDK 建立單一 AI agent，由 Amazon Bedrock（例如 Claude Sonnet 或其他支援工具呼叫的 LLM）驅動作為推理引擎，動態協調 Amazon Rekognition 與 Amazon Transcribe。使用者提出問題後，agent 會先解析意圖——是要轉錄摘要、視覺搜尋還是人臉比對——再檢查是否已有快取的分析結果，若沒有才挑選對應工具執行（必要時按順序串接，讓前一個工具的輸出餵給下一個），最後把結果整合成自然語言回答。

系統中的服務分工：
- Amazon Rekognition：偵測影片畫面中的物件、場景、活動與人臉，用於視覺相關問題。
- Amazon Transcribe：將語音轉成文字，支援超過 100 種語言的自動偵測與語者分離，用於語音內容相關問題。
- Amazon Bedrock Data Automation（BDA）：一次 API 呼叫即可取得影片摘要、章節切分與完整轉錄，適合需要一站式綜合分析、或 Rekognition／Transcribe 無法使用時。
- Amazon S3：以每位使用者獨立前綴儲存上傳影片與分析結果快取，支援多租戶隔離。

文章特別強調，這三項服務只是起點而非固定清單——因為 agent 是根據工具描述來選擇工具，而非寫死的流程邏輯，同一套架構可以持續加入新服務作為工具。

📊 首次分析要等 5 到 10 分鐘，後續提問不到 1 秒

在 60 分鐘影片的測試中，第一個問題通常要等 5 到 10 分鐘（轉錄或視覺分析執行期間），但針對同一份內容的後續問題，因為 agent 重複使用快取結果，回應時間降到 1 秒以下；實際時間會因影片長度、解析度與所呼叫的服務而異。

一家媒體娛樂公司在 AWS Professional Services 專案中採用了這套方案，讓顧問可以直接查詢已錄製的探索性會議內容，擷取設計決策、待辦事項與利害關係人立場。根據該客戶內部對分析師工時的前後比較（未經第三方獨立驗證），在超過 200 支多小時錄影的積壓案件中，人工審閱時間約減少 80%。

⚠️ 人臉比對與監控用途需加裝護欄

文章建議正式環境部署時加上 Amazon Bedrock Guardrails，對 agent 回應執行內容過濾與事實核查（grounding check），特別是人臉比對與監控類用途需要負責任 AI 控管。

🎯 實務啟示

這個架構的核心價值不在單一功能，而在於把「該呼叫哪個服務」這個決策從應用程式碼移交給 LLM 本身，讓同一套 agent 同時處理會議摘要、監視器查詢、內容分析與事件調查（例如「哪臺車在碰撞前變換車道」）等差異很大的問題類型，不需要為每種用例重建 pipeline。完整實作（含 search_faces_in_video、analyze_with_bda 等工具程式碼，系統提示約 250 行）已釋出於文中提及的 GitHub repository，適合想快速驗證 agentic 架構落地可行性的團隊參考。

🔗 來源
- 標題：Agentic conversational video intelligence built on AWS
- 作者／機構：Michael Li, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/agentic-conversational-video-intelligence-built-on-aws/

#AWS #AgenticAI #VideoIntelligence #AmazonBedrock #AmazonRekognition #AmazonTranscribe #StrandsAgents #LLMTooling #EnterpriseAI #VideoAnalytics
