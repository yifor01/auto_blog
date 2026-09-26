---
title: 'OpenRouter: from Seed to Stripe — with OpenRouter’s Alex Atallah & AMP’s Anjney
  Midha'
source: Latent Space
url: https://www.latent.space/p/openrouter
model: claude-code/sonnet
generated_at: '2026-09-26T20:00:26.071366'
score: 65
---

📌 從「只是個wrapper」到被Stripe收購：OpenRouter的多模型賭注

TL;DR：OpenRouter靠押注「沒有單一模型會贏者全拿」，走到每日路由逾10兆token並被Stripe收購。

曾被創投嘲笑「只是包了層API的wrapper」，如今卻服務超過1000萬名開發者，還被支付巨頭Stripe買下——這中間到底發生了什麼。

🤔 **從Alpaca看見的轉捩點**

在Latent Space這集訪談裡，OpenRouter共同創辦人暨執行長Alex Atallah與AMP的Anjney Midha，回顧了OpenRouter誕生的起點。Anjney描述2022年底時OpenAI幾乎是市場上唯一的選項，加上Cohere與零星幾個早期開放權重模型的嘗試。2023年1月Llama釋出時，雖然在一兩項基準測試上超越GPT-3，但無法直接對話，體驗並不完整。真正讓他意識到「風向要變了」的，是史丹佛團隊只花600美元、用一批合成資料對Llama做微調後推出的Alpaca：在飛機上實測時，他發現自己幾乎分辨不出Alpaca與ChatGPT的回答差異，也因此判斷「用便宜的方式做出接近水準的模型」這件事會越來越容易、成本會持續下降。

🧩 **「訂閱與發布」：OpenRouter的產品理念**

Anjney在2023年初提出的「sub as a product」概念，是這集訪談中另一個核心線索：把產品理解為「發布（publish）資料」與「訂閱（subscribe）資料」的交會點。人類消費內容的方式是離散、間歇的，但Agent與推論的消費者是連續運作、而且會不斷更換所需的模型或服務項目（SKU）。OpenRouter因此被設計成介於一般API體驗與市場機制之間的產品：提供model slug（模型代稱）、auto router（自動路由）等機制，讓使用者能持續依據需求切換與衍生價值，而不必綁死在單一供應商的原生SDK上。

📊 **從「只是wrapper」到千萬開發者、每日10兆token**

訪談中提到，OpenRouter曾一度被創投單純視為「市場」或「wrapper」，估值難以被認真對待。真正的轉折點之一是Mistral引發的價格戰，成為第一次真正證明「推論市場（inference marketplace）」有價值的事件。隨著Discord早期AI應用（例如Midjourney的擴張經驗）以及開放模型生態逐漸成熟，OpenRouter選擇聚焦而非擴張進fine-tuning、記憶（memory）等鄰接產品線，這被視為它最大的策略優勢之一。目前OpenRouter服務超過1000萬名開發者，每日處理的token量超過10兆。他們的排行榜（leaderboard）也逐漸變成即時反映整個AI產業使用趨勢變化的地圖。訪談中也提到一段早期未竟的嘗試：OpenRouter曾做過名為MOM（Mixture of Models）的模型融合實驗，第一版後來被下架，直到幾年後才以更成熟的形式重新推出。

💡 **Stripe收購背後：詐騙才是下一個戰場**

Anjney在訪談中說明了Stripe與OpenRouter的契合點：Stripe本身在防詐騙（fraud）方面的基礎建設，對OpenRouter的策略布局相當重要。他認為隨著token經濟規模擴大，token詐騙將成為AI經濟中最具代表性的資安問題之一，而且下一波攻擊不會只來自人類，還會出現自主Agent針對日益龐大且有價值的token流動發動攻擊。

⚠️ **這集偏商業與創業故事**

整段訪談的重點落在商業模式演進、募資與收購脈絡，對於OpenRouter內部具體的路由演算法或詐騙偵測技術細節著墨不多，素材中也未提供更深入的工程實作說明。

🎯 **實務啟示**

如果你正在打造Agent系統或需要跨模型的推論架構，這集訪談至少點出兩個值得留意的方向：一是盡量避免把系統寫死在單一模型或單一供應商SDK上，模型汰換與價格戰會持續發生；二是隨著Agent自主消費token的規模擴大，token濫用與詐騙偵測會變成基礎設施層必須提前布局的問題，而不只是事後的風控措施。

🔗 **來源**
- 標題：OpenRouter: from Seed to Stripe — with OpenRouter's Alex Atallah & AMP's Anjney Midha
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/openrouter

#OpenRouter #Stripe #LLMRouting #MultiModel #AIInfrastructure #Mistral #AgenticAI #TokenEconomy #AIStartup #InferenceMarketplace
