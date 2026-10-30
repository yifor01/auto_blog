---
title: Google’s first data center satellite is online and writing poetry
source: TechCrunch AI
url: https://techcrunch.com/2026/10/30/googles-first-data-center-satellite-is-online-and-writing-poetry/
model: claude-code/sonnet
generated_at: '2026-10-30T21:46:51.875750'
score: 75
---

📌 Google 第一座太空資料中心上線，先寫了首俳句

TL;DR：Google Suncatcher 原型衛星搭載 4 顆 TPU 已在軌通訊，首個任務是讓 Gemma 4 寫太空俳句。

當工程師這週向一顆繞地球飛行的衛星傳送第一個 prompt 時，他們沒有急著測試算力，而是先請它寫一首關於身處太空的俳句。衛星給出的回覆是：「Blue marble below / Data streams in silent grace / Starlight feeds my core.」

🤔 背景：從發射到「開機」的三週

這顆 Google Suncatcher 原型衛星本月稍早隨 SpaceX Falcon 9 火箭與超過 100 顆其他衛星一同升空，機上搭載四顆 Google Tensor Processing Unit（TPU），最高可產生 1 千瓦電力。不過受限於供電能力，衛星一次只能開啟一顆 TPU 運作，每次僅能持續約 20 分鐘，這也讓本就棘手的太空與地面通訊變得更複雜。衛星經過約三週的子系統測試（commissioning）後，本週正式開始接受任務指令。

🧩 先寫詩，再回報軌道狀況

地面工程師送出的第一個 prompt，是要求衛星上預先載入的模型 Google DeepMind Gemma 4 寫一首關於身處太空的俳句，也就是前述的那三行詩。Google 同時測試了幾首太空主題的打油詩，但更重要的任務是讓衛星回報自身周遭的軌道環境狀況。Google 發言人向 TechCrunch 表示，衛星目前運作正常（operating nominally）。

💡 真正的考驗：輻射與熱應力

接下來的測試會檢視晶片在熱應力與太空輻射環境下的表現。輻射可能造成記憶體中儲存數值的「位元翻轉（bit flip）」，進而讓資料在未觸發一般監控工具警示的情況下悄悄損壞。Google 雖然已在地面的粒子加速器中大量測試過 TPU，但這是第一次在真實太空環境而非模擬環境中觀察輻射對硬體的實際影響。地面測試顯示，輻射對推理工作負載的影響很小，對訓練工作負載的影響則較大，真實數據仍待在軌驗證。

若這批 TPU 表現達標，下一步將是在 2027 年發射兩顆配備更先進晶片的衛星，這兩顆衛星將具備更高的發電能力，並展示衛星間的雷射光學連結（inter-satellite optical links）。

⚠️ 跟競爭對手的路線差異，與一個現實的提醒

文章指出，Suncatcher 計畫的特別之處在於它規劃衛星之間的高速連結，支援跨衛星的協同分散式運算；SpaceX 的太空資料中心雖然也打算使用雷射連結，但衛星軌道間距過遠，難以共享運算資源。Starcloud 與 Cowboy Space 等公司則是規劃在單顆衛星上獨立執行推理工作負載。Google 與 SpaceX 的願景也彼此牽連：Google 母公司 Alphabet 持有 SpaceX 的重要投資股權，而兩家公司要實現太空資料中心的願景，都仰賴仍在開發中的可完全快速重複使用的 Starship 重型火箭。Suncatcher 研究人員在本月發表的一篇同行評審分析中估計，SpaceX 需要飛行 Starship 達 1,800 次，才能達到與其過去火箭相同的「以學習曲線驅動成本下降」效果。

文章也提醒，這類登月計畫式（moonshot）的長期布局，仍要面對公司短期的現實壓力：同一週，Alphabet 股價因為「在搜尋業務中導入 AI 正在拖累廣告營收成長」的消息而重挫。

🎯 實務啟示

對關注基礎設施趨勢的工程師而言，Suncatcher 目前仍是一次非常早期、受限於供電（單顆 TPU 僅能間歇運作約 20 分鐘）的概念驗證，距離實際可用的軌道推理服務還有「輻射耐受性驗證」與「可重複使用重型火箭」兩大未解前提。它更像是一個 2030 年代才可能兌現的長期賭注，短期內不需要納入任何實際部署規劃，但值得持續關注輻射測試的後續結果。

🔗 來源
- 標題：Google's first data center satellite is online and writing poetry
- 作者／機構：Tim Fernholz, TechCrunch AI
- 連結：https://techcrunch.com/2026/10/30/googles-first-data-center-satellite-is-online-and-writing-poetry/

#GoogleDeepMind #Gemma #Suncatcher #SpaceComputing #TPU #SpaceX #Satellite #AIInfrastructure #EdgeComputing #Starship
