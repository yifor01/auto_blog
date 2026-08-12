---
title: How Pixieset achieved 35% AI feature adoption by solving the right problem
  with Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-pixieset-achieved-35-ai-feature-adoption-by-solving-the-right-problem-with-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-08-12T07:44:19.535458'
score: 69
---

📌 攝影師最討厭AI，Pixieset卻靠一個小功能拿下35%採用率

TL;DR：Pixieset用Amazon Bedrock自動生成alt text，4個月上線、16個月後採用率仍達35%。

攝影師是對生成式AI最有戒心的一群人，眼看AI威脅自己的手藝、把市場灌滿合成作品。但 Pixieset 找到了一個連挑剔的攝影師都願意讓 AI 代勞的任務，而且十六個月後仍有 35% 的目標用戶在用。

🤔 問題不是AI能做什麼，而是使用者被迫做什麼

Pixieset 是一站式攝影業務服務，提供相片庫、網站、商店、工作室管理與修圖，代管超過 80 億張照片，全球數百萬攝影師使用。2025 年一項 MIT 研究發現，95% 的企業生成式AI試點沒有帶來可衡量的回報。Pixieset 的切入點不是「這個技術能做什麼」，而是「使用者在哪些不算攝影的雜務上losing time」。團隊透過每年一次的全公司黑客松第一次接觸到生成式AI，隨後把這份好奇心帶回真正的產品問題。Pixieset Websites 讓攝影師架設個人網站，但數據顯示多數攝影師的網站幾乎沒有 alt text（替代文字）。沒有 alt text，圖片對搜尋引擎等於隱形；一個攝影師的作品集動輒數百到數千張照片，逐張手寫描述性 alt text 既繁瑣又耗時，攝影師都知道該做卻總是往後拖。團隊刻意避開了更亮眼、卻會侵犯攝影師創作自豪感的應用，例如 AI 生成圖像，轉而瞄準 metadata 這種沒人喜歡寫、卻讓作品集能被搜尋引擎看見的隱形骨架。

🧩 一次API呼叫接進既有pipeline，零基礎設施

Pixieset 的架構建立在 Amazon EC2、AWS Lambda 與 Amazon SQS 構成的事件驅動架構上。攝影師上傳照片會觸發事件，團隊只在既有的 worker pipeline 裡多加一步：把圖片送進 Amazon Bedrock 做多模態大型語言模型推論，把生成的說明文字與照片一起儲存，並在攝影師每天都會用的網站建置器裡呈現供審核。整合只需要一次 API 呼叫，不必新增基礎設施、不用自行採購 GPU 或自架模型。Bedrock 的跨區域推論會在指定地理邊界內自動跨區域路由請求，維持吞吐量而不必自建路由邏輯；團隊還加了一層保險，第一個模型失敗就自動改用品質相近的第二個模型重試，上線至今這個功能零停機。功能在 2025 年初上線時採用 Anthropic Claude 3.5 Sonnet，看中的是它的多模態影像理解、快速推論與規模化下的成本效益；因為 Bedrock 提供跨模型供應商的統一API，團隊之後評估新模型不必被特定版本綁死，Bedrock 的進階提示最佳化還會自動把既有提示適配到新模型的特性上，降低換模型的成本。截至 2026 年 6 月，Bedrock 模型目錄已擴充到包含 Claude Sonnet 5、OpenAI GPT-5.5、Amazon Nova 以及 Meta、Mistral、Cohere 等模型，代表這個 2025 年上線的功能會隨底層模型持續變強，工程投入卻很少。

🧩 讓AI一步步贏得信任的介面設計

AI 生成的 alt text 不是整站一次套用，而是逐張圖片呈現：攝影師先審核單張建議文字，選擇接受、編輯或拒絕，再逐步擴大範圍。等攝影師信任輸出品質後，才開啟「自動套用」，即使開了自動套用，每一段文字依然可編輯，攝影師始終握有最終決定權，AI 的信任是一點一點掙來的。

📊 上線第一週75萬張照片，16個月後仍有35%採用率

Pixieset 首週就為超過 75 萬張照片生成了 alt text，並在上線第一週就帶動了訂閱升級；十六個月後，這個功能仍被 35% 的目標用戶群持續使用。攝影師的實際回饋也印證了團隊押對了問題，例如有使用者直言原本不喜歡 AI，卻覺得批量生成圖片描述「絕對是game changer」，也有人因此升級了訂閱方案。

💡 為什麼選「metadata」而不是更亮眼的功能

Pixieset 在動手前就想清楚一件事：AI 生成 alt text 是「必備功能」，不是能靠獨家資料越滾越大的護城河，遲早所有網站建置器都會提供。這個判斷讓團隊優先衝速度而非過度打磨差異化，也是他們能在 4 個月內從概念做到量產上線，而不是花一年打造最終未必能形成壁壘的差異化功能的原因。

🎯 實務啟示

在幫企業產品導入生成式AI功能時，先問「使用者被迫做哪些不屬於他們核心價值的雜務」，而不是「這個模型還能做什麼」；避開會侵犯使用者專業自豪感的應用場景；用漸進式的人工審核，從單張確認到自動套用開關，讓使用者自己建立對 AI 輸出的信任；並優先評估這個功能到底是「必備但無差異化」還是「真正的護城河」，這會決定你該衝速度還是深耕。

🔗 來源
- 標題：How Pixieset achieved 35% AI feature adoption by solving the right problem with Amazon Bedrock
- 作者／機構：Kinman Lam（與 Pixieset 的 Ry Rainey、Graham Gibson 共同撰寫），AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/how-pixieset-achieved-35-ai-feature-adoption-by-solving-the-right-problem-with-amazon-bedrock/

#AmazonBedrock #GenerativeAI #AWS #AIAdoption #ClaudeAI #ProductStrategy #MachineLearning #SaaS #AltText #AIUX
