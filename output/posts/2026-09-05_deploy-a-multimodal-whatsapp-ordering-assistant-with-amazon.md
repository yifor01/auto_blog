---
title: Deploy a multimodal WhatsApp ordering assistant with Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/deploy-a-multimodal-whatsapp-ordering-assistant-with-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-09-05T19:17:00.422648'
score: 75
---

📌 一支WhatsApp號碼搞定文字、語音訊息與通話點餐

TL;DR：AWS展示如何用Bedrock AgentCore與Nova 2打造跨管道統一記憶的WhatsApp點餐助理。

速食餐廳的點餐管道往往分散在App、網站、電話與櫃臺，每個系統各自為政，同一位顧客在不同管道下單，卻可能被系統當成完全陌生的人。AWS的這篇教學示範了如何用一支WhatsApp Business號碼，同時處理文字、語音訊息與語音通話三種點餐方式，並讓它們共用同一套後端與記憶。

🤔 **為何選擇WhatsApp**

WhatsApp觸及超過20億使用者，顧客不需要額外安裝App或登入帳號，只要在原本就在用的聊天視窗傳文字、傳語音訊息，或直接打語音電話就能下單。AI代理人從問候到確認訂單，全程接手處理，而且今天用文字下單、明天打電話的同一位顧客，系統能夠識別出是同一人。

🧩 **三層架構與三種對話模式**

整體架構刻意把三件事分開：WhatsApp層負責對話介面、三個Agent Runtime分別處理不同管道的對話邏輯、後端則統一存放菜單、購物車、訂單與門市資訊。所有進站流量都先透過單一HTTPS webhook立即回應200，再非同步處理，避免任何請求卡住回應。

三種互動模式共用同一個前門、後端工具與記憶，差別在於媒體型態與負責的執行環境：
- **文字訊息**：Worker辨識出customer_id後呼叫chat runtime，透過Amazon Bedrock Converse API串流呼叫Amazon Nova 2 Lite，並視需要透過MCP Gateway呼叫後端工具。
- **語音訊息**：音訊會被解碼為16 kHz PCM後送入Amazon Nova 2 Sonic的語音對語音（speech-to-speech）連線，過程中沒有轉錄服務介入，是真正的「語音進、語音出」，回覆會以WhatsApp語音訊息形式送出。
- **語音通話**：透過Meta Calling API交換WebRTC SDP，Worker以turnOnly模式將offer轉給voice-call runtime，TURN憑證來自Amazon KVS，再由aiortc完成單次SDP應答，媒體則透過DTLS/SRTP經KVS的TURN中繼傳輸，同樣由Amazon Nova 2 Sonic驅動對話。

整套系統以AWS CDK部署，依序建立共用VPC、後端（DynamoDB、Amazon Location Service、訂單Lambda與REST API）、AgentCore Gateway與共用記憶、三個ARM64容器化的Runtime（透過CodeBuild建置、推送至ECR），最後接上WhatsApp webhook並匯入示範菜單與門市資料。

⚠️ **部署前要注意的限制**

WhatsApp端的設定必須在Meta主控臺手動完成，沒有任何AWS API可以代為建立Meta App，因此這是部署前的必要前置作業，而非流程中的一步。此外，部署所在的AWS區域必須同時支援Amazon Nova 2 Lite、Amazon Nova 2 Sonic以及AgentCore的Runtime、Gateway與記憶功能，文章建議以美國東部（維吉尼亞北部）作為起點。若只是要做展示，Meta提供的免費沙箱測試門號就足夠，不需要完成企業驗證或申請正式門號。

🎯 **實務啟示**

這個架構最值得工程團隊借鏡的地方，在於它把「管道」與「點餐邏輯」徹底解耦：新增或移除一種互動管道時，後端完全不用變動。對於正在規劃多管道客服或訂單系統的團隊，這種以共用記憶與共用後端工具串接不同前端管道的設計思路，比起為每個管道各自開發一套系統要更容易維護與擴充。

🔗 **來源**
- 標題：Deploy a multimodal WhatsApp ordering assistant with Amazon Bedrock AgentCore
- 作者／機構：Salman Ahmed，AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/deploy-a-multimodal-whatsapp-ordering-assistant-with-amazon-bedrock-agentcore/

#AmazonBedrock #AgentCore #AmazonNova #WhatsAppBusiness #AIAgent #ConversationalAI #AWS #MCP #VoiceAI #MultimodalAI
