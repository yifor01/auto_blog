---
title: 'Survival LLM: AI assistant and emergency library that runs on your own computer'
source: Hacker News
url: https://www.brangus.io/survival-llm
model: claude-code/sonnet
generated_at: '2026-10-28T22:02:36.202586'
score: 79
---

📌 斷網時還能救你一命的 AI:Survival LLM 把急難知識裝進你的電腦

TL;DR：完全離線運行的 AI 急難助手,依電腦記憶體自動選擇合適的本地模型,並附帶近百萬篇可查來源的應急資料庫。

停電、斷網的那一刻,手機上的 AI 助理往往第一個失靈,而 Survival LLM 的設計前提正是「網路消失之後,它才真正開始工作」。

🤔 **為斷網場景而生的 AI 助手**

Survival LLM 是一款免費開源的 AI 助手與應急資料庫,完全在使用者自己的電腦上運行。你可以問它停電時如何保存食物、如何處理燒燙傷、如何淨水,它會根據可信來源回答,並標示每個答案出自哪一篇文章。設定過程需要網路,但設定完成後完全不需要連網即可使用。

🧩 **依硬體自動配對模型,答案附來源可查**

這個專案的核心設計理念是「本地推理 + 檢索式知識庫」。開啟應用程式時,它會偵測電腦記憶體,自動下載合適大小的模型:

| 裝置 | 使用的模型 | 應急測驗答對率 | 模型下載大小 |
|---|---|---|---|
| 128GB以上記憶體的 Mac | NVIDIA Nemotron 3.5 Super | 22題中對21題 | 80GB |
| 32–96GB記憶體的 Mac | Qwen3.8 27B | 22題中對21題 | 18GB |
| 32GB以上記憶體的 Windows PC | NVIDIA Nemotron 3.5 Lightning | 22題中對19題 | 25GB |
| 16–31GB記憶體的 Mac 或 PC | IBM Granite 4.2 8B | 22題中對14題 | 6GB |

官方說明,這個「答對率」是針對22道停電與急救問題做盲測評分,測試對象是資料庫的早期版本。模型越小,犯錯機率越高,因此應用程式永遠會附上原始出處讓使用者自行核對。

資料庫內容包括約93萬篇維基百科高瀏覽條目、WikiMed醫療百科、MedlinePlus(美國國家醫學圖書館)、WikEM急診醫學、FEMA的Ready.gov應急指南、CDC旅行健康資訊、美軍醫療與生存手冊、wikiHow與iFixit修復指南等,每個來源都保留各自的授權條款並標示於文章旁。使用者也能把自己的PDF、Word文件或筆記（例如發電機手冊）加進去,AI會一併檢索,且這些檔案不會離開你的電腦。

🧩 **安裝與設定**

Mac版安裝檔約212MB、Windows版約25MB,完整設定時間約20分鐘到兩個半小時,視電腦效能與網速而定,但使用者實際需要動手操作的時間只有約5分鐘,其餘是背景下載。硬體需求為Apple Silicon（M1以上）且macOS 14以上,或64位元Windows 10/11。完整資料庫（含維基百科與iFixit）下載約9GB,安裝後19GB;精簡版則是1.3GB下載、安裝後3GB。

⚠️ **限制與注意事項**

官方坦承AI模型會出錯,尤其是較小的模型,因此每個答案都附上來源文章供核對。使用上無需帳號、無追蹤,設定完成後可完全離線使用。根據官方在MacBook Pro上的測量,回答時耗電約100瓦,每題耗時5到40秒,滿電可支撐約100到300次問答,小型發電機或行動電源即可輕鬆供電。

🎯 **實務啟示**

對關注edge AI部署與RAG架構的工程師來說,這個專案展示了一個清楚的設計模式:把模型大小與硬體能力綁定自動選擇,再疊加一個可溯源的本地知識庫,是在無網路環境下兼顧可用性與可信度的實用做法,也是本地LLM部署的一個具體應用案例。

🔗 **來源**
- 標題：Survival LLM: AI assistant and emergency library that runs on your own computer
- 作者／機構：Luc（Hacker News 發布者）
- 連結：https://www.brangus.io/survival-llm

#OfflineAI #LocalLLM #EmergencyPreparedness #RAG #OpenSource #OnDeviceAI #Nemotron #Qwen #DisasterTech #PrivacyFirst
