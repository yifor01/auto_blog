---
title: Architect Launches Liquid Inference, a Real-Time Auction for LLM Inference
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/08/architect-launches-liquid-inference-a-real-time-auction-for-llm-inference/
model: claude-code/sonnet
generated_at: '2026-10-08T22:23:41.003106'
score: 89
---

📌 用交易所競價機制賣LLM推論：Architect推出Liquid Inference

TL;DR：來自交易公司Architect的Liquid Inference讓多家推論供應商即時競價，開發者只換base URL就能讓價格自動變便宜。

當你呼叫LLM API時，價格通常是供應商單方面定的固定費率。Architect Financial Technologies推出的Liquid Inference，把這個邏輯反過來：每一個請求都變成一場即時拍賣，供應商互相競價，買方只付符合條件中最低的那個報價。

🤔 **做金融交易所的團隊，跑來做LLM推論市場**

文章特別點出一個背景：這個產品出自一家交易公司，而不是AI實驗室。Architect本身經營AX永續期貨交易所，2026年5月還收購了一家美國指定合約市場（Designated Contract Market），準備掛牌GPU運算期貨（目前仍待監管審查）。團隊把打造金融交易所的經驗，搬來建立推論運算的雙邊價格發現機制。

🧩 **供應商報價、系統拍賣、買方只付最低且合規的那一個**

Liquid Inference是一個交易所形式的LLM推論路由器。根據Architect的說法，供應商會針對特定模型張貼報價，每一個請求會在所有針對該模型報價的供應商之間進行拍賣，符合買方規則中出價最低的那個報價得標。買方可以設定每個任務的成本上限、第一個token的回應時間限制（time to first token）、最低吞吐量，也可以要求指定地區、zero data retention，或設定供應商／模型的允許清單。系統還提供Auto模式，可以依任務內容自動挑選模型。

所有prompt都採用OpenAI API標準格式，意味著開發者理論上只需要把base URL換成Liquid Inference的端點，程式碼基本不用改。供應商則透過Liquid Inference的app完成上架，文章引用Architect方面的說法，新供應商驗證「只需幾分鐘，而不是幾週」；供應商可以透過REST與WebSocket API註冊模型與報價，並依自身成本動態調整報價，也就能選擇只在想賣的時候賣出閒置的GPU產能。帳務上，款項透過Stripe支付，並附上每筆任務的明細紀錄。

💡 **帳本公開：你能看到即時訂單簿與成交紀錄**

文章提到，帳戶持有者可以看到即時的order book、各供應商與各模型的報價，以及已結算的交易紀錄。這種市場數據的透明度，對一般LLM API而言並不常見，通常開發者只能看到自己呼叫後拿到的帳單，而不是整個市場的即時報價狀態。

⚠️ **期貨市場部分仍待監管審查**

文章提到Architect在2026年5月收購的GPU運算期貨掛牌資格仍「pending regulatory review」，代表這部分業務尚未完全落地；至於Liquid Inference本身的供應商品質、報價穩定性或實際延遲表現，文章並未提供具體數據。

🎯 **實務啟示**

如果你的應用對推論成本敏感、又不想被綁在單一供應商的定價上，Liquid Inference這種「換base URL、讓供應商競價」的模式值得關注，尤其是它開放設定成本上限、延遲限制與地區／資料保留規則，這些都是生產環境中常見的硬性需求，可以在評估多供應商推論路由方案時納入比較。

🔗 **來源**
- 標題：Architect Launches Liquid Inference, a Real-Time Auction for LLM Inference
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/08/architect-launches-liquid-inference-a-real-time-auction-for-llm-inference/

#LLMInference #Architect #LiquidInference #InferenceRouting #AIInfrastructure #GPUCompute #LLMAPI #CostOptimization #AIEconomics #MLOps
