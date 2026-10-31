---
title: Preview web apps live as your coding agent builds them with Amazon Bedrock
  AgentCore runtime
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/preview-web-apps-live-as-your-coding-agent-builds-them-with-amazon-bedrock-agentcore-runtime/
model: claude-code/sonnet
generated_at: '2026-10-31T20:37:26.593437'
score: 84
---

📌 AWS Bedrock AgentCore：讓你邊看 Coding Agent 改網頁邊秒更新

TL;DR：AgentCore 新推出 Session Endpoint，免部署即可即時瀏覽 agent 正在修改的網頁。

Coding agent 幫你刻出一個 dashboard 或產品頁原型後，最快的驗收方式永遠是：打開它、用它、要求修改、再看結果。這個迴圈順暢與否，關鍵在於「app 是不是就跑在 agent 編輯的那個地方」。一旦每次改動都得先複製程式碼、再部署到別處才能看到效果，審查節奏就被硬生生拖慢到部署速度。

🤔 **預覽卡在「先部署才能看」的老問題**

Amazon Bedrock AgentCore 是一個可大規模建置、串接、最佳化 agent 的平臺，支援自選 agent 框架與基礎模型。其中的 AgentCore runtime 會把每個 agent session 跑在獨立的 microVM 裡；這次新增的 Session endpoint，則讓你能從自己的瀏覽器直接打開那個 session 裡正在跑的 app，而不必經過部署流程。

🧩 **Session Endpoint 怎麼運作：六個關鍵細節**

Session endpoint 會給每個 session 一條具身分驗證的 URL，把 HTTP 方法、路徑、查詢字串、request body 以及 WebSocket 連線轉送到你允許的 port 上。六個細節決定了實際用法：

- 你自己指定能連到哪些 port：呼叫 `CreateAgentRuntime` 時透過 `allowedPorts` 設定，最多 5 筆，每筆是單一 port 或 8000–12000 範圍內的區段（排除保留的平臺 port）。允許某個 port 不代表自動啟動伺服器，你的應用仍須自己監聽並綁定在 `0.0.0.0`。
- URL 會隨 session 一起送回來：`InvokeAgentRuntime` 的回應會把它放在 `X-Amzn-Bedrock-AgentCore-Runtime-Session-Endpoint-Url` 標頭裡，對應 SDK 的 `sessionEndpointUrl`。
- 每個請求都要驗證：IAM 模式下每個 HTTP 請求、HTTP/2 stream、WebSocket handshake 都帶 SigV4 簽章（還需要對該 runtime 與其 endpoint 的 `bedrock-agentcore:InvokeAgentRuntimeProxy` 權限）；若 runtime 設定 JWT 授權，則改用 bearer token。知道這條 URL 不代表能存取。
- Host name 決定連到哪個 port：client 一律連線到 443，再由 host name 的前綴選擇 session 內部實際的 port。
- 支援的協定很完整：HTTP/1.1、HTTP/2（含 server-sent events、gRPC）與 WebSocket 都可以通過，這次示範用的是 HTTP/1.1 與 WebSocket。
- 作用範圍僅限單一 session：這條 URL 的有效期等於 session 的生命週期，用來建置、測試、審查 agent 產出的內容；要真正服務使用者，仍需部署到像 AWS Amplify Hosting 這類託管服務。

因為瀏覽器本身無法為請求加上 SigV4 簽章或 bearer token，`bedrock-agentcore` SDK 提供了一個本機端點：瀏覽器打開 `http://localhost:8088`，由本機端點在轉送前自動補上憑證。

值得分清楚：Session endpoint 不等於 AgentCore runtime 原本就有的 runtime endpoint。Runtime endpoint（例如 `DEFAULT`）決定 `InvokeAgentRuntime` 呼叫實際落在哪個版本的 agent 上，可以讓開發與正式環境指向不同版本；Session endpoint 則是用來「看」某個 session 目前正在跑什麼，例如這次的網頁預覽，session 結束後它就失效。

範例架構分四塊：agent 跑在 port 8080，內建 list、read、write、edit 四個工具來編輯網站檔案；agent 啟動的 Vite 開發伺服器跑在 port 8090，透過 hot-reload WebSocket 把每次存檔同步到瀏覽器；本機端的 PreviewApp 負責顯示預覽頁、把你的提示送進 `InvokeAgentRuntime`，並幫 port 8090 開一個本機端點。由於 `InvokeAgentRuntime` 本身就能直接連到 agent，port 8080 不需要放進 `allowedPorts`，只有 8090（網站）與狀態路由用的 8081 需要。

完整範例收在 agentcore-samples GitHub repo 的 `14-remote-access` 資料夾，用 S3 上的 zip 檔做 Node.js 直接程式碼部署，不需要 Docker 或 Amazon ECR。步驟是：clone 範例、開啟 `session_endpoints_preview.ipynb`、跑安裝 cell、跑 `%run deploy.py`（主要等待 runtime 進入 READY 需要幾分鐘）。接著一次呼叫就會啟動 session（也就啟動了網站）、幫 port 8090 開本機端點，並在 `localhost:8087` 把預覽頁服務起來。

⚠️ **別把它當成正式服務的出口**

Session endpoint 只對 microVM runtime 有效，不支援 Instances 運算型別；URL 走公開 HTTPS，不支援 AWS PrivateLink 的入站連線；而且效期與 session 綁定，本質是拿來審查、不是拿來上線。Vite 設定也因此要放寬 `server.allowedHosts`，因為請求是經由 runtime 指派的 host name 進來，不是 `localhost`，但驗證仍由 Session endpoint 在請求到站前完成。

🎯 **實務啟示**

如果你正在打造讓 agent 自動生成前端原型的工作流，這個模式提供了一個現成答案：讓 app 一直跑在 agent 編輯的那個 session 裡,把「審查」與「部署」拆開，審查用 Session endpoint 秒看結果,真正上線再走標準部署管線。

🔗 **來源**
- 標題：Preview web apps live as your coding agent builds them with Amazon Bedrock AgentCore runtime
- 作者／機構：Sundar Raghavan（AWS Machine Learning Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/preview-web-apps-live-as-your-coding-agent-builds-them-with-amazon-bedrock-agentcore-runtime/

#AWS #AmazonBedrock #AgentCore #CodingAgent #AIAgent #DevTools #LiveReload #Vite #CloudComputing #SoftwareEngineering
