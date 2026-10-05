---
title: How Genie Ontology powers product development at Databricks
source: Databricks
url: https://www.databricks.com/blog/how-genie-ontology-powers-product-development-databricks
model: claude-code/sonnet
generated_at: '2026-10-05T23:26:06.364605'
score: 72
---

📌 為什麼通用AI agent答不出你公司的問題？Databricks用Genie Ontology補上這一塊

TL;DR：Genie Ontology把分散在儀表板、文件、人腦中的企業知識整理成agent能用的語意層,Databricks用它跑每週產品review。

通用型AI agent很會搜尋網路、推理、寫程式碼,但一問到「我們公司」的問題就容易答錯。問題不在模型不夠聰明,而是它缺少解讀企業資料所需的情境：哪張表才是權威來源、哪些業務規則適用、誰是真正該信任的專家。這些知識散落在儀表板、查詢、文件、應用程式甚至人的腦中,而且隨著資料、定義與團隊變動不斷在變。

🤔 **企業知識散落各處，而且一直在變**

這正是Databricks產品團隊自己每週都在面對的問題。Genie Ontology要解的,就是讓Genie持續掌握這些制度性知識,包括業務定義、規則、關係與可信來源。

🧩 **從Unity Catalog的治理資產，到自動學習的語意片段**

Genie Ontology從團隊在Unity Catalog中治理與認證的核心概念出發,再透過「學習到的知識」把範圍擴大到組織內的儀表板、文件、查詢、notebook與已串接的應用程式。接著由OntoRank依認證狀態、使用量、作者等訊號對這些情境排序權威性,讓Genie針對每個問題,把答案建立在最可信、最相關的來源上。

💡 **實例：產品團隊每週的Genie One採用率review怎麼做出來的**

文章以Databricks產品團隊每週檢視Genie One使用者採用率的實際流程做示範。使用者會在手機、桌面應用程式或網頁上打開Genie One,要求它依團隊標準範本（存放在Google文件中）產出週報,找出需要注意的熱點。

這件事表面簡單,實際上不簡單：使用者橫跨web、桌面、行動裝置、Slack與Teams;部分儀表板是權威來源,部分已經過時該被忽略;相關的業務情境還延伸到Lakehouse之外——規劃文件在Google文件、bug回報在Jira、現場回饋在Slack。

從Genie的思考過程可以看到Ontology實際運作的樣子：先找出相關資料資產（儀表板、agent、資料表），再查看經過人工整理的Pages，最後探索幾個從儀表板、notebook、SQL查詢中萃取出的ontology語意片段。範例中,Genie找到了團隊認證過的weekly active users metric view——一個全公司共用同一套定義的治理KPI指標。接著它透過MCP搜尋即時的Google雲端硬碟文件與Jira工單,最後對使用資料表執行SQL,把這些來源的情境與即時分析結果結合在一起。

因為這套情境是permission-aware的,Genie只會使用使用者透過Unity Catalog與已串接來源被授權存取的資料與知識。

點進引用來源可以看到Genie實際用了哪些metric views（全公司共用定義的認證KPI）與Pages（Unity Catalog中的治理wiki）——這不令人意外,因為Genie會優先採用人工認證過的資產,再自行探索。但不可能每個概念都靠人工整理,所以還有ontology snippets：Genie自動學習並評估過的業務事實,點進去可以看到完整定義、來源、作者,以及由OntoRank算出的權威分數,甚至能查看作者的個人檔案,看他還貢獻過哪些領域的snippet。

報告完成後,文章作者接著問Genie：為什麼過去幾個月新使用者數量暴增?原本這需要自己查使用資料表依介面與帳號拆解,再翻roadmap文件、Jira工單與Slack討論串去找原因,現在直接問Genie就能得到答案。預測功能也內建在Genie One裡——原本要跟資料科學團隊提需求、對齊假設、等上好幾天的模型結果,現在可以直接請Genie預測並標出需要留意的帳號。

這份週報後來被設定成排程自動產生,而這整段對話也直接變成一個Genie Agent的起點,讓團隊與主管可以持續針對Genie效能提問,並沿用這次對話與過去相關對話中用過的資料來源。文章開頭也提到,Genie One還支援自訂技能、排程任務、可共享的agent,以及透過MCP對外部工具寫入等能力。

⚠️ **自動學習的知識仍需要權威分數把關**

文章坦承,不可能把每個業務概念都靠人工治理覆蓋,這也是為什麼需要ontology snippets這類自動學習的補充機制,並透過OntoRank的權威分數加以區分可信程度,而不是把人工認證資產與自動學習結果一視同仁。

🎯 **對正在做企業AI agent的工程師的啟示**

這篇案例點出一個常被低估的落差：讓agent「會查資料」和讓agent「懂你的業務」是兩件事。與其讓通用agent每次都重新爬schema、抽樣資料表、反覆查詢去猜哪個定義才對,不如建立一層結合治理資產（如Unity Catalog認證）與學習訊號（使用量、作者、權威分數）的語意層,並確保這層情境本身是permission-aware的——這對任何想在企業資料上做agent落地的團隊,都是值得參考的設計方向。

🔗 **來源**
- 標題：How Genie Ontology powers product development at Databricks
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/how-genie-ontology-powers-product-development-databricks

#Databricks #Genie #DataOntology #EnterpriseAI #UnityCatalog #SemanticLayer #AIAgent #DataGovernance #KnowledgeGraph #MCP
