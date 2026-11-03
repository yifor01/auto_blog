---
title: Agentic engineering intelligence with Amazon Nova Multimodal Embeddings and
  Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/agentic-engineering-intelligence-with-amazon-nova-multimodal-embeddings-and-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-11-03T00:05:32.250535'
score: 90
---

📌 多模態Embedding讓零件替代審查有證據可查

TL;DR：AWS用AgentCore多Agent系統串Nova Embeddings,把航太零件替代的查證過程交給AI整理證據。

飛行關鍵零件一旦選錯替代品,後果可能是任務失敗,但過去的替代評估證據往往散落在email與工程師腦中,沒有一份reviewer可以覆核的正式package。AWS這篇文章示範怎麼用多Agent系統把這段證據蒐集流程自動化,同時讓工程師保有最終決策的角色。

🤔 背景:停產零件的替代評估,靠人工交叉比對
當合格的航太零件停產或進入長交期,工程師得花好幾天在vendor datasheet、interface control document(ICD)、鑑定紀錄之間交叉比對,才能寫出一份替代理由文件供審查。先前一篇文章《Manufacturing intelligence with Amazon Nova Multimodal Embeddings》已經展示過Nova Multimodal Embeddings怎麼從工程圖、溫度曲線、datasheet圖表裡撈出文字管線抓不到的答案;這篇文章接著把這種檢索能力放進一個多Agent系統,從檢索一路做到產出替代評估草稿。

🧩 架構:規劃者、三個專家與一個監督者
整套系統建立在一個設計原則上:工程師做決策,系統負責整理證據,系統本身不會自己批准任何替代方案。這個原則決定了哪裡用LLM、哪裡用deterministic程式碼。

架構上,工程師應用程式的聊天請求會進到部署在Amazon Bedrock AgentCore runtime上的多Agent圖:Planner(Claude Haiku 5.5)產生routing plan,Specialist(Claude Sonnet 5.5)執行工具,當超過一個specialist被呼叫時,Supervisor(Claude Opus 5.5)才會整合結果。Specialist從用Amazon Nova Multimodal Embeddings建立的Amazon Bedrock Managed Knowledge Bases裡檢索,透過AgentCore Gateway轉接,並搭配Web Search connector抓即時網路資料。如果查詢是上傳一張圖找零件(image-as-query),因為managed knowledge base的檢索API不接受影像輸入,Agent會直接呼叫原生的Amazon S3 Vectors索引。另外還有一條固定chain(Knowledge→Evaluation→Supervisor),專門產生正式的Integration Impact Assessment(IIA)文件。

Routing本身是個分類任務,不需要大型推理模型,所以用Haiku的planner幾秒內就能給出routing plan;Opus supervisor只在兩個以上specialist都有貢獻時才會執行,因為對單一specialist已經完整的答案做整合,只會多花約8秒延遲卻沒有品質提升。三層模型分工——Haiku分類、Sonnet跑工具、Opus寫整合答案,把成本和延遲對應到真正需要的階段。

📊 範例資料:七顆反應輪撐起的多模態語料庫
文章用的範例資料集是虛構廠商AnyCompany的七顆反應輪(reaction wheel),動量儲存範圍0.003到5.0 Nms。每個零件資料夾把specs.json這種機器可讀欄位,跟工程師實際會讀的ICD、產品照片、渲染過的datasheet頁面放在一起,這種混合正是語料庫「多模態」的來源。specs.json同時記錄工程規格與生命週期資訊,讓系統可以同時標出報廢與長交期風險,以及規格是否吃得下。由於目錄ID和檔名在不同資料集間會重複使用,每個specialist的prompt都把get_part_specs回傳的結構化vendor值當成唯一權威來源,禁止從ID、檔名、照片或網路搜尋結果去猜測廠商,避免模型「自以為認得這個零件」而把零件歸給錯的供應商。

💡 deterministic評分:verdict必須可重現
規格比對(spec-fit evaluation)是用一般Python程式碼跑在手寫的requirements schema上,而不是交給LLM。schema定義每個零件類別的關鍵規格與容忍規則,score_substitution_fit負責逐項比對、計算通過與flag數量,並呈現生命週期風險;因為這個verdict必須在工程審查package裡可重現,這一步完全不讓LLM參與。工具回傳的結構化verdict還附帶明確聲明,specialist只能呈現這張表並解釋flag,不能改動結論。

⚠️ 影像查詢需要繞道,範例資料也是虛構的
managed knowledge base的檢索API本身不支援影像輸入,所以image-as-query只能繞道走原生S3 Vectors索引,這是架構上為了相容影像查詢多加的一條路徑;文章本身的範例資料也是虛構廠商與零件,實際落地仍需要接上真正的vendor資料與鑑定紀錄。

🎯 實務啟示
這個案例示範了一個值得參考的分工方式:用LLM做檢索、分類、整合語言輸出,但把「有對錯、要可重現」的判斷邏輯(像是公差比對)寫成deterministic程式碼,而不是整個丟給模型猜。如果你的場景也有「證據要齊全、結論要能被人覆核」的需求,這種Planner/Specialist/Supervisor搭配固定chain產出正式文件的模式,比單一Agent硬做到底更容易審查與除錯。

🔗 來源
- 標題：Agentic engineering intelligence with Amazon Nova Multimodal Embeddings and Amazon Bedrock AgentCore
- 作者／機構：Aishwarya Gavili, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/agentic-engineering-intelligence-with-amazon-nova-multimodal-embeddings-and-amazon-bedrock-agentcore/

#AWS #AmazonBedrock #AgentCore #NovaMultimodalEmbeddings #MultiAgent #AerospaceEngineering #RAG #LLM #StrandsAgents #AIAgents
