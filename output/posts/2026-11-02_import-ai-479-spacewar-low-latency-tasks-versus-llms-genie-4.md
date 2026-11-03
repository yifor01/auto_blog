---
title: 'Import AI 479: Spacewar; low-latency tasks versus LLMs; Genie 4'
source: Import AI
url: https://jack-clark.net/2026/11/02/import-ai-479-spacewar-low-latency-tasks-versus-llms-genie-4/
model: claude-code/sonnet
generated_at: '2026-11-03T00:09:09.725897'
score: 82
---

📌 【UT Austin、NVIDIA等機構】即時決策任務，最強LLM只拿36%

TL;DR：新基準Realtime-Bench顯示，頂尖模型在有時限的即時任務中通過率僅36%。

搶票、線上拍賣、玩一場即時策略遊戲，這些任務人類靠直覺就能抓準時機，但對LLM來說卻是另一個世界：慢一秒做決定，可能就等於直接輸掉。

🤔 LLM擅長「想清楚」，卻不擅長「來得及」

現有大多數AI benchmark評估的是模型在沒有時間壓力下能不能把問題想對，但真實世界裡許多任務的成敗取決於「動作有沒有在正確的時間點做出來」。來自University of Texas at Austin、Ohio State University、University of Illinois at Urbana-Champaign、NVIDIA、Northwestern University與Steadyworks的研究團隊，為此提出Realtime-Bench，一套「延遲的動作會直接影響成敗」的動態任務集合。

🧩 50個任務，三種能力，三種時鐘

Realtime-Bench由50個互動任務組成：30個web任務，分屬旅遊、電商、服務、安全四個類別；20個遊戲任務，分屬arcade、puzzle、strategy、simulation四個類別。benchmark設計用來探測三種能力：

- RT-Perceive（時序狀態感知）：模型能否用觀察結果持續追蹤世界的變化。
- RT-Deliberate（自適應推理深度）：模型能否依剩餘時間調整推理的長度與深度。
- RT-Act（時機敏感的動作選擇）：模型能否在對的時間點選擇動作。

論文舉的例子是買票：agent要持續追蹤票務銷售狀態並判斷觀察到的庫存是否仍然即時有效（RT-Perceive），當購票視窗即將關閉時要限制進一步的推理（RT-Deliberate），並在「等待開賣」與「趁還有票時先買」之間做選擇（RT-Act）。評測設有三種時鐘條件：Wall clock，模擬真實世界的延遲；Paused clock，可任意暫停環境,用來量測模型的基線能力；Token clock，環境依固定速率隨生成的token數推進，動作執行的時間點取決於已消耗的token數，而不是實際的推理延遲。

📊 暫停時7成以上過關，真實時鐘只剩36%

研究團隊測試了OpenAI（GPT-6-Astra、GPT-5.6 Sol、GPT-Realtime-2、OpenAI Decisions）、Anthropic（Claude Fable 5.1、Claude Opus 5）、Google（Gemini 3.8 Flash、Gemini 3.1 Flash Live、Gemini 3.8 Live）、Jev 1.13，以及中國的Deepseek V4.1與Moonshot AI的Kimi-K3。在wall clock條件下，GPT-6 Astra（high）拿到最高通過率，但也只有36%；相較之下，在paused clock條件下，具備高推理強度的模型通過率可以逼近70%甚至80%。

💡 Token clock揪出「想太久反而來不及」

三種時鐘條件的設計頗具巧思：wall clock測的是「真實延遲下能不能做到」，paused clock測的是「拿掉時間壓力後的真實能力上限」，兩者的落差本身就說明了問題所在；而token clock則進一步把「生成更多token」直接換算成「消耗更多模擬時間」，用來檢驗模型是否會因為推理過長而錯過時機，與純粹的推理延遲脫鉤觀察。

🎯 實務啟示

如果你在打造需要即時反應的agent，例如自動下單、競標系統、或是需要在固定時間窗口內行動的工具，Realtime-Bench的分數說明一件事：目前的LLM即便離線推理能力很強，也不能直接信任它在真實延遲下的時機判斷。這類場景可能需要額外的工程手段，例如明確的時間預算控制、或針對推理長度做動態調整，而不是單靠換一個更強的模型就能解決。

🔗 來源
- 標題：Import AI 479: Spacewar; low-latency tasks versus LLMs; Genie 4
- 作者／機構：Jack Clark，Import AI
- 連結：https://jack-clark.net/2026/11/02/import-ai-479-spacewar-low-latency-tasks-versus-llms-genie-4/

#RealtimeBench #LLM #AIAgents #Benchmark #NVIDIA #LLMEvaluation #AIResearch #RealTimeAI #AgenticAI #MachineLearning
