---
title: 'From Wafer-Out to First Token: Codifying Supply Chain Expertise with Nemotron
  and Palantir Foundry'
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/from-wafer-out-to-first-token-codifying-supply-chain-expertise-with-nemotron-and-palantir-foundry/
model: claude-code/sonnet
generated_at: '2026-09-10T20:08:46.878818'
score: 81
---

📌 【NVIDIA】從晶圓出廠到首個Token：把資深規劃師的直覺教給AI

TL;DR：NVIDIA與Palantir合作，先用cuOpt做配置最佳化，再用開源模型Nemotron學會人類規劃師看不見數字的判斷力。

一個機櫃裡十八個運算托盤，每一個都要等到最挑剔的那顆零件到齊才能開工。這聽起來像是排程課本上的組合最佳化題，但NVIDIA真正卡關的地方，其實在數學算不出來的那一段。

🤔 **一個運算托盤，三十八顆關鍵零件**

NVIDIA表示，其供應鏈的績效是以「晶圓出廠到首個Token」（wafer-out to first token）衡量，分成兩段：Time-to-rack涵蓋從矽晶圓離開晶圓廠到系統組裝完成、進駐資料中心；Time-to-token則涵蓋之後的供電、散熱、網路與軟體堆疊。NVIDIA Grace Blackwell NVL72平臺涉及數百萬個零件與數千家供應商，最終系統由數十家OEM/ODM組裝完成。單一個運算托盤（一個機櫃有十八個）就需要兩顆NVIDIA Grace CPU、四顆NVIDIA Blackwell GPU與三十二個HBM3e記憶體堆疊，而NVIDIA為Vera Rubin打造的供應鏈規模又是Grace Blackwell的兩倍。

CPU、GPU、記憶體這些關鍵零件的供應狀況每週都在變化，這週卡住產線的零件，下週可能就充裕了。組裝廠必須等到所有零件——不論是NVIDIA直供、NVIDIA寄售庫存，還是供應商供應——三個來源都到齊才能開工，NVIDIA用「Time of Ownership」（TOO）這個指標衡量從物料抵達製造場址到離開變成次組件或成品的時間。在供應高度動態變化的情況下，該分配多少物料給哪個製造場址，就成了「關鍵物料分配問題」，過去每週都要靠人工重新演算一次。

🧩 **Palantir Foundry打造統一的作業圖像**

NVIDIA供應鏈營運團隊與Palantir合作打造「Digital Supply Chain Intelligence」指揮中心，透過Palantir Foundry的Ontology把物料、製造場址、承諾量、產能、分配結果、產出，以及散落在各處的非結構化定性訊號，全部串接進同一個受治理的資料層。這個以物件與連結（而非列與表）組成的表示法，讓分配規劃者得以模擬與分析多種情境，也為後續的AI飛輪打下基礎。

🧩 **cuOpt把分配問題變成一個混合整數線性規劃**

物料分配本質上先是一個量化問題：決策變數是「未來一段期間內，哪些受限物料該分給哪個場址、何時分」，週邊則是每個場址能承接的產能上限，以及往回追溯的完整零件依賴圖，讓求解器知道一個運算托盤真正被卡住的是它最稀缺的那個輸入，而非平均供應狀況。這個綁定約束並非固定不變，會隨GPU、CPU、記憶體週間供應變化、三條供應路徑的到貨時間，以及已對客戶做出的承諾而改變。

NVIDIA使用開源的GPU加速決策最佳化函式庫cuOpt求解這個混合整數線性規劃問題，輸入來自Ontology，求解結果寫回成一筆分配決策，目標是最小化Time of Ownership。cuOpt回傳的不只是分配結果本身，還會回報哪些約束是「綁定的」，讓規劃者看出這週真正卡住產量的是臺灣產能而非記憶體供應。由於求解速度快，規劃者可以進一步探索「如果記憶體少一成會怎樣」「如果新場址上線會怎樣」，從單純要答案變成問求解器代價權衡在哪裡。

💡 **數學算不出來的那部分：人類專家的直覺**

NVIDIA與Palantir將歷史分配決策拿去回測實際結果，發現cuOpt沒有捕捉到一個人為因素：規劃者手上握有求解器看不到的資訊——那週與夥伴往來的郵件、某個關鍵地區的天氣預報或地緣政治事件、上一通供應商簡報通話的逐字稿，以及多年累積的經驗。這些輸入形成一種直覺，讓人類專家的判斷勝過純數學結果。

因此NVIDIA與Palantir圍繞這些人類專家重新設計工作流程，把分配決策、決策背後的理由、預期結果與實際結果全部記錄下來。這讓原本存在於個人腦中的機構知識變成可審視、可重複使用的決策邏輯，因為這些資料同樣存放在Ontology裡，成為訓練LLM學習專家判斷的基礎。

🧩 **選擇Nemotron 3.5 Lightning的理由**

在評估多個NVIDIA Nemotron開源模型後，團隊選擇Nemotron 3.5 Lightning對這些歷史決策資料進行後訓練（post-train），理由是它是為「agentic workflow的執行層」設計的模型，作為系統中負責特定任務的一員，另有更大的變體負責協調與通用任務。它採用mixture-of-experts架構，推論效率高；雖然模型規模僅300億參數、每次前向傳遞約30億啟用參數，但仍足以學到一個聚焦的決策策略，這讓後訓練循環變得可行，因為更小的模型訓練更快、訓練與部署所需的算力也遠低於更大型的模型。由於Nemotron是開源權重模型，可以在自己的算力邊界內完成後訓練，任何組織都能在不對外暴露資料的前提下，在自己的營運資料上跑同一套飛輪。

🎯 **實務啟示**

這個案例的關鍵不是「用AI取代最佳化求解器」，而是把兩者分工：cuOpt負責處理有明確約束的量化問題並揭露哪個約束在綁定，開源小模型負責學習那些藏在郵件、通話紀錄與經驗裡、難以形式化的判斷。對於想把內部專家決策沉澱成可複用資產的團隊，「記錄決策＋理由＋結果」本身就是後訓練資料集的雛形。

🔗 **來源**
- 標題：From Wafer-Out to First Token: Codifying Supply Chain Expertise with Nemotron and Palantir Foundry
- 作者／機構：Elizabeth Goodman, NVIDIA Developer Blog
- 連結：https://developer.nvidia.com/blog/from-wafer-out-to-first-token-codifying-supply-chain-expertise-with-nemotron-and-palantir-foundry/

#NVIDIA #SupplyChain #Nemotron #Palantir #cuOpt #AgenticAI #OpenWeightLLM #DecisionOptimization #MixtureOfExperts #AIinManufacturing
