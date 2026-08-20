---
title: AI isn’t close to curing cancer. This startup says it knows what it will take.
source: TechCrunch AI
url: https://techcrunch.com/2026/08/19/ai-isnt-close-to-curing-cancer-this-startup-says-it-knows-what-it-will-take/
model: claude-code/sonnet
generated_at: '2026-08-20T06:37:27.979138'
score: 82
---

📌 AI 藥物研發缺的不是模型，是「活體組織」的因果數據

TL;DR：Vivodyne 用機器人實驗室培養人體組織取代動物實驗，想補上 AI 藥物發現最缺的因果數據。

Dario Amodei 上週才寫道，「AI 治癒癌症」這句話已經從願景淪為陳腔濫調；但這篇報導指出，真正的問題或許不在模型不夠聰明，而在於它們從沒見過「活著的」人體組織。

🤔 淪為陳腔濫調的「AI 治癒癌症」

Sam Altman 多次把「治癒癌症」當作 OpenAI 推進 AGI 與擴大算力的理由，Google DeepMind 的 Demis Hassabis 去年也說 AI 有機會在十年內治癒所有疾病，Amodei 自己過去的文章裡也提過類似願景。但實際進展仍然有限：拿到諾貝爾獎的 AlphaFold，至今還沒真正做出一款藥；由它延伸而生的 Isomorphic Labs，原訂 2025 年展開的首個臨床試驗，也被推遲到今年底才要開始。Vivodyne 創辦人暨執行長 Andrei Georgescu 認為，現有 AI 模型的訓練資料多半來自動物實驗、單細胞或蛋白質研究，而不是活體組織：「Absent human testing, what are these models going to do? They're going to cure cancer in mice.」產業現況也印證這個落差——現行藥物中，有 90% 在動物實驗階段已經夠有效、得以進入臨床試驗，卻始終無法獲得人體用藥的監管核准。

🧩 HIVE：培養人體組織的機器人實驗室

Vivodyne 於 2021 年從賓州大學（University of Pennsylvania）分拆出來，Georgescu 正是在那裡取得生物工程博士學位。公司打造了名為 HIVE 的模組化機器人實驗室，能培養 20 種人體組織，並自主進行給藥與監測，藉此產生現有 AI 模型缺乏的「因果性」生物數據。上週，該公司在舊金山近郊啟用了它所稱「全球最大的人體數據中心」。

📊 肝細胞 94%、氣道 96%、骨髓 100% 一致

依公司說法，其肝細胞在毒性測試上與人體臨床試驗結果的預測準確率達 94%，氣道組織與真實人體組織行為的吻合度為 96%，骨髓組織在 20 種化療藥物的測試中達到 100% 一致性。Georgescu 表示，團隊目前的實驗吞吐量已達到美國全部動物實驗總量的兩倍。公司目前由 Khosla Ventures 領投，兩輪合計募得近 8000 萬美元，並表示正與多家大型藥廠合作，但未公開具體名單。

💡 缺的不是模型，是因果數據

Georgescu 把這個問題類比成汽車碰撞測試：汽車廠在送測前通常已經很有信心能通過 NHTSA 標準，但藥廠在進入臨床試驗前，往往沒有這種確定性，導致絕大多數藥物最終在人體試驗階段失敗。他引用一篇上月發表於《Nature Methods》的研究，指出現有的細胞資料在訓練生成式 AI 模型時，並未展現出明確的 scaling law，原因在於這些訓練資料多半是細胞的「靜態快照」：模型只學到「這是狀態 A」「這是狀態 B」，卻從未學到「狀態 B 是狀態 A 受到發炎刺激後的結果」這種因果關係。HIVE 持續追蹤數十萬個進行中的實驗，把病變組織暴露於特定刺激下並記錄反應，Georgescu 期待這類資料能提供類似強化學習的訊號，讓 AI 模型真正理解人體生物學。他也指出，未來若要開發同時針對多重路徑的複方藥物，搜尋空間會急遽膨脹，光靠實驗式嘗試已不可行，必須先建立因果理解：先設定想要的效果，再反推該用什麼原因去誘發它。

🎯 實務啟示

對投入 AI for science、藥物發現領域的工程師而言，這篇報導提醒了一個常被低估的瓶頸：模型架構再強，若訓練資料仍停留在靜態快照式的細胞或動物數據，就學不到因果關係。這類「資料基礎設施」的投資，可能比單純堆更大的模型更關鍵。

🔗 來源
- 標題：AI isn't close to curing cancer. This startup says it knows what it will take.
- 作者／機構：Tim Fernholz, TechCrunch
- 連結：https://techcrunch.com/2026/08/19/ai-isnt-close-to-curing-cancer-this-startup-says-it-knows-what-it-will-take/

#AIforScience #DrugDiscovery #Biotech #Vivodyne #AlphaFold #IsomorphicLabs #MachineLearning #HealthcareAI #CausalInference #Pharma
