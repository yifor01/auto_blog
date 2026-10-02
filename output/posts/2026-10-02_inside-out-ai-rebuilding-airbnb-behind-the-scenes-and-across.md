---
title: 'Inside-Out AI: Rebuilding Airbnb Behind the Scenes and Across the Guest Experience'
source: Latent Space
url: https://www.latent.space/p/airbnb
model: claude-code/sonnet
generated_at: '2026-10-02T21:38:26.865919'
score: 79
---

📌 從Meta到Airbnb：CTO揭露AI重塑內外體驗的做法

TL;DR：曾主導Meta Llama的Ahmad Al-Dahle空降Airbnb CTO，用「由內而外」策略把AI能力從內部開發線帶到客服與新服務。

60%的程式碼由AI寫成，功能交付量年增近八成，這不是新創的願景簡報，而是一家市值近千億美元上市公司的現況。

🤔 從打造前沿模型，到把模型部署到位

Ahmad Al-Dahle今年一月加入Airbnb擔任CTO之前，是Meta生成式AI部門負責人，主導了2023到2025年間Llama開源模型的發布。他向Latent Space解釋轉換跑道的原因:「我傾向追逐我認為最難的前沿所在」。在Meta，團隊已經摸清模型能力世代提升的飛輪該怎麼轉;他認為下一個挑戰是大規模部署模型,推動人們改變工作方式，並把這些系統真正落地到會為核心使用者體驗創造價值的生產環境。

🧩 先改流程，再談工具

Al-Dahle說，Airbnb的AI轉型首先是組織流程的改變:傳統上產品需求、Figma設計、工程實作、上線測試之間各自交接;現在產品、設計與工程團隊會直接共同處理原型(prototype)。他形容:「把這些交接的時間差打掉，正是許多傳統軟體公司要跨出這一步最大的節省來源。」這也讓團隊從過去「產出大量文件artifact」的模式，轉向以程式碼本身和原型作為討論依據。

📊 具體數字:程式碼、功能交付與客服

Al-Dahle提出幾個數據佐證轉型成效:目前Airbnb有60%的程式碼由AI撰寫，功能與改善項目年增近80%，一般工程師的PR(pull request)產出量提升約1.6倍。客服是Airbnb第一個導入AI的面對使用者場景，Al-Dahle形容這是「最難部署的問題」，因為出錯代價很高。做法是先用合成資料大量測試代理，確認可靠後才上線;目前約半數客服工單由AI獨立解決(與Airbnb第二季財報揭露的近45%數字相符)，但團隊刻意保留涉及安全性等情境交由人工處理。另外兩個今年稍早推出的新服務,雜貨外送與機場接送，則受惠於一個名為Everest的內部組織情境圖(context graph)，它運用LLM、embedding與AI檢索技術打造而成。根據Airbnb第二季財報，雜貨外送服務花了八、九個月開發，有了Everest累積的經驗後，機場接送只花了約六週。Al-Dahle指出，這個跨程式碼庫的情境圖讓「通才工程師也能跨入非常專精的程式碼領域工作」。

💡 多模型策略:每個場景選對的工具

Al-Dahle形容Airbnb是一家「多模型公司」，內部生產系統部署了至少10個客製化模型，並針對每個使用情境在成本、效能與延遲之間畫出帕雷托前緣，各自取捨。例如寫程式碼能容忍較高延遲但犯錯代價高，因此偏好使用最頂尖的前沿編碼模型;搜尋功能則對延遲極度敏感，偏好經過後訓練(post-train)的小型專用模型,他甚至表示，針對狹窄情境做後訓練的小模型，效能有時能超越前沿模型。Airbnb內部也有自己的代理AirChat，整合了組織所需的MCP情境。更進一步的方向，是讓非同步代理在容器中依事件觸發運作:例如監控系統(如Grafana)告警觸發時，代理會自動啟動進行事故分診與初步處理，人類工程師審查代理提出的PR，若代理判斷是誤報甚至可以自行結案。Al-Dahle的願景是用大量非同步代理去協助管理詐欺偵測、信任違規、市集品質與軟體缺陷等整個市集平臺的運作。

🎯 實務啟示

Airbnb的經驗提供一個清晰的框架:先把AI用在內部開發流程打穩地基，再把同樣的能力延伸到面對使用者的高風險場景(如客服)，並且針對不同任務場景(編碼 vs. 搜尋)審慎選擇模型大小與後訓練策略，而非迷信單一前沿模型打天下。

🔗 來源
- 標題：Inside-Out AI: Rebuilding Airbnb Behind the Scenes and Across the Guest Experience
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/airbnb

#AirbnbAI #AINative #LLMOps #AIAgents #Llama #EnterpriseAI #AIinProduction #CustomerSupportAI #MultiModel #AsyncAgents
