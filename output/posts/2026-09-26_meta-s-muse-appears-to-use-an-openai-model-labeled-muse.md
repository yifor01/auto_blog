---
title: Meta's Muse appears to use an OpenAI model labeled muse-special
source: Hacker News
url: https://mouse.dev/blog/muse-special/
model: claude-code/sonnet
generated_at: '2026-09-26T20:00:26.071230'
score: 75
---

📌 拆解 Meta Muse：系統裡藏著一個 OpenAI 模型？

TL;DR：獨立研究者在Meta Muse的VM檔案系統裡，挖出疑似透過Azure呼叫OpenAI模型的線索。

幾乎所有session log都跑在Meta自家模型Avocado上，唯獨9月21日那一次不一樣——log裡出現了一個叫azure/muse-special的名字。

🤔 **一個異常的session，牽出的後續追查**

這是作者（化名Pete，部落格mouse.dev）繼上一篇登上Hacker News首頁的文章後，第二次深入挖掘Muse代理背後的檔案系統。他發現VM裡的session紀錄會標註每個子任務用了哪個模型，其中絕大多數都指向Meta內部模型Avocado，只有一個subagent的session被標記為azure/muse-special，這讓他決定順著這條線索繼續查下去。

🧩 **幾個技術細節湊出的推論**

在Cursor裡搜尋repo後，作者找到一段字串：「GPT Responses model client via MAGI native Azure OpenAI lane」。模型目錄（model catalogue）裡，azure/muse-special緊接著列在azure/gpt-5.6-sol之後。回頭檢視session transcript，作者發現兩個關鍵細節：其一，簽名被標記為gpt_responses_v1，並帶有一段以gAAAAA開頭的加密payload，這是OpenAI慣用的格式；其二，工具呼叫ID（tool call ID）採用call_後接24碼混合大小寫字元的格式，這與其他Avocado session裡call_後接32碼十六進位字元的格式明顯不同。

把視角拉遠，Muse代理daemon附帶的完整模型目錄裡，除了約15個版本的Avocado，還列有Claude Opus 4.6／4.7／4.8、Sonnet 4.6與Haiku 4.5、透過OpenAI／Azure／Codex提供的GPT-5.5與GPT-5.6各版本，以及透過Fireworks與Meta自架路由提供的Kimi K3。作者強調，「被列在目錄裡」只代表runtime具備呼叫該模型的能力，不代表它真的被用過。更值得注意的是，runtime裡還有一整套針對Anthropic的請求處理程式碼，包括anthropic/request_flow.rs、anthropic/convert_prompt.rs、anthropic/parse_sse_stream.rs，分別負責請求流程、提示詞轉換與串流解析。環境中也存在分別對應Anthropic、OpenAI等供應商的API金鑰檔案，存取權限限制在inference-proxy服務；另外還有一個環境變數JARVIS_ANTHROPIC_BASE_URL_REVPROXY_OVERRIDE=0，程式註解明確寫著這是一個「live kill switch」（隨時可切換的開關），而非過期設定殘留。

💡 **是選擇性路由，還是在做蒸餾？**

作者猜測有兩種可能：一是某些任務上OpenAI或Anthropic的模型表現就是比Meta自家模型好，於是選擇性地路由過去；二是整套VM本來就內建A/B測試不同供應商模型回應與工具呼叫的能力，用於蒸餾（distillation）或強化學習（RL）訓練。針對「Meta是否在蒸餾其他實驗室的模型」這個問題，作者的結論偏向否定：muse-special的原始推理過程是加密的，daemon只是把它存起來、留待下一輪對話送回Azure，二進位檔案裡明確寫著加密的推理內容不能被RL補全伺服器（completion-server）覆寫使用；換句話說，Meta這端能看到的只有回覆內容、工具呼叫，以及OpenAI／Anthropic偶爾附上的簡短推理摘要，真正的思維鏈本身仍是加密狀態，RL伺服器會拒絕處理這類資料，也沒有跡象顯示Meta複製了對方的模型權重。相對地，Avocado模型的思考文字是直接以明文寫入transcript、簽名欄位是空的，可供RL訓練使用；根據隱私權說明與repo內容，使用Avocado進行的對話預設可被用來開發Meta自家AI，除非使用者主動選擇退出。

⚠️ **證據是拼湊出來的，結論仍是推測**

作者自己也承認，檔案與log並沒有明講muse-special究竟對應哪一個GPT版本，也不清楚這個subagent當初為何被選中使用它。整篇文章的結論建立在字串比對、簽名格式與ID長度差異等間接證據上，屬於合理推測而非官方證實。

🎯 **實務啟示**

對於正在打造多供應商（multi-provider）Agent runtime的工程師而言，這篇拆解提供了一個有意思的參照：即使把模型抽象成內部代號，簽名格式、加密payload前綴、工具呼叫ID的生成規則，仍可能洩露背後真正的推論供應商。同時，「kill switch開關＋分權限的API金鑰＋加密推理鏈」這套設計，也示範了大型產品在多供應商路由與RL資料管線之間，如何劃出隱私與可用性的邊界。

🔗 **來源**
- 標題：Meta's Muse appears to use an OpenAI model labeled muse-special
- 作者／機構：Aeroi（Hacker News）
- 連結：https://mouse.dev/blog/muse-special/

#MetaAI #Muse #OpenAI #ReverseEngineering #LLMRouting #AzureOpenAI #ModelDistillation #ReinforcementLearning #AIInfrastructure #AgentRuntime
