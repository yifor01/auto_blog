---
title: Amazon Polly now supports voice cloning
source: Amazon.com
url: https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-polly-now-supports-voice-cloning/
model: claude-code/sonnet
generated_at: '2026-11-20T23:22:26.659388'
score: 71
---

📌 Amazon Polly開放語音複製,先走受限上線路線

TL;DR:Polly 新增語音複製功能,幾分鐘錄音即可生成仿真聲音,目前以受限(gated)方式發布。

合成語音做了這麼多年,一直繞不開「聽起來像誰」這個問題。現在 Amazon Polly 給出了答案的一部分:只要有人同意,幾分鐘的錄音就夠。

🤔 **從固定音色到客製聲音**

AWS 宣布 Amazon Polly 的語音複製(voice cloning)功能正式上線,以受限發布(gated release)的形式提供。根據官方說明,只要取得一位同意參與(consenting speaker)的講者錄音,收集幾分鐘的素材,就能用 Polly 建立一個聽起來像該講者的複製聲音。摘要在此處被截斷,並未進一步說明複製語音背後的技術細節或完整的使用限制。

💡 **「受限發布」與「同意講者」這兩個關鍵字**

這次發布特別強調兩件事:一是功能以 gated release 形式推出,代表並非所有帳戶或地區可以直接使用,需要申請或符合特定條件才能啟用;二是明確要求錄音來自「consenting speaker」,也就是語音所有人必須同意被複製。這兩個限制合在一起,反映出語音複製這類功能上線時,服務供應商對濫用風險(例如冒用他人聲音)的審慎態度,但摘要並未說明具體的審核流程或使用規範是什麼。

⚠️ **目前能確定的資訊有限**

由於素材只提供了功能上線的公告段落,沒有涵蓋模型架構、支援語言、錄音品質要求,或是克隆聲音在 Polly 既有 TTS 功能(如 SSML 控制)中的相容程度,這些細節目前都無法確認,需要等後續官方文件補充。

🎯 **實務啟示**

如果你的應用需要客製化配音,例如品牌語音、有聲內容或是企業內部語音助理,這次上線代表 Polly 多了一個官方且合規(需同意講者)的路徑,值得先去申請 gated release 的存取權限,實際測試輸出品質與可用的語言/地區範圍,而不是等到功能全面開放才評估。

🔗 **來源**
- 標題:Amazon Polly now supports voice cloning
- 作者/機構:Amazon Web Services
- 連結:https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-polly-now-supports-voice-cloning/

#AmazonPolly #VoiceCloning #TextToSpeech #AWS #GenerativeAI #SpeechSynthesis #ResponsibleAI #CloudAI #VoiceAI #AIAudio
