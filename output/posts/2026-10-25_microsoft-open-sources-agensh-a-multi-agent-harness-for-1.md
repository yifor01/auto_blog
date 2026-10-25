---
title: 'Microsoft Open-Sources Agensh: A Multi-Agent Harness for 1,024 Agents'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/24/microsoft-agensh-multi-agent-harness-1024-agents/
model: claude-code/sonnet
generated_at: '2026-10-25T19:43:11.030163'
score: 107
---

📌 Microsoft開源Agensh：拿掉中控的千規模Coding Agent協作

TL;DR：Agensh讓上千個coding agent不靠中控orchestrator，自行分工、互通並合併程式碼。

多數multi-agent coding框架都靠一個「領頭」agent規劃任務、分派工作、整合成果，包括Claude Code的agent team、Codex的sub-agent、Copilot fleet與Kimi Agent Swarm。但當agent數量衝到幾百、幾千個，這個領頭agent本身就會變成瓶頸。Microsoft Research開源的Agensh，直接把這個中控角色拿掉。

🤔 **Orchestrator ceiling：領頭agent規劃不動，整個團隊就卡住**

Agensh論文指出，orchestrator-worker架構的天花板，來自領頭agent必須親自規劃、分派、合併所有工作。Agensh的做法是把這些協調工作直接還給worker自己做。

🧩 **每個worker跑同一套迴圈，靠Git、聊天室與共享筆記板互相協調**

每個worker都並行、非同步地跑同一套流程，差別只在於各自的ID，而不是靠runtime程式碼去分派。三個共享服務把大家串起來：Gitea負責共享的程式碼工作區，處理branch、PR與merge conflict；Mattermost提供一個團隊頻道加上私訊，用來處理緊急的衝突；另外有一個改編自DeLM的共享context board，存放OBSERVED、FACT、FAIL、CLAIM、PATCH_SUMMARY這五種型別的筆記。Agensh架在單一agent harness之上，實驗用的是GitHub Copilot CLI，論文表示用簡單的adapter就能接上其他harness，例如Claude Code。

📊 **在ProgramBench上，從1個agent擴到1,024個agent，分數持續往上走**

Microsoft團隊挑了ProgramBench裡最難的5個任務：FFmpeg、gromacs、pandoc、PHP-src與ctags，讓agent團隊在離線環境、6小時內，僅憑觀察到的行為把程式重建出來。這些參考專案的規模從pandoc的2,767個檔案，到PHP-src的26,266個檔案不等。

用GPT-5.6-sol在高推理強度下測試，平均最終測試通過率整體提升了9.47個百分點，相對提升約49%。單看pandoc的話，分數隨agent數量規模化相當明顯：

| Agent數量 | pandoc最終通過率 |
|---|---|
| 1 | 33.89% |
| 8 | 41.75% |
| 32 | 43.11% |
| 128 | 50.94% |
| 1,024 | 55.06% |

速度也有差：在pandoc任務上，128個agent在30分鐘checkpoint就達到30%的通過率，而32個與8個agent分別要花60分鐘與90分鐘才能到同樣水準。README另外補充了用更新模型GPT-6.1-sol的結果：pandoc從1個agent的56.19%，提升到32個agent的79.59%，相對提升41.64%，但這組數字沒有出現在v1論文裡，解讀時要留意。

💡 **沒有人指派角色，分工卻自己長出來**

研究團隊追蹤了不同規模下worker的軌跡，發現有些worker自發地承擔起特定角色，而這些角色沒有一個是被寫死在程式裡的。這說明Agensh的分工機制，是靠共享的context board與聊天訊息自然湧現出來，而不是靠中控事先安排。

⚠️ **複現門檻不低，且新模型數據仍待論文驗證**

要跑起來需要Linux加Docker Engine、Compose v2、systemd、cgroup v2與Python 3.11以上，還需要ProgramBench（驗證過的版本是v1.2.5）跟模型的API token。預設設定是8個worker、每個任務6小時、用gpt-5.6-sol高推理強度。GPT-6.1-sol的結果目前只出現在README，尚未經過論文正式驗證。

🎯 **大規模agent部署，先想協調機制而不是先想加更多agent**

如果團隊正在把coding agent的規模往上堆，Agensh提供的是一個不同的思路：與其不斷加強中控的規劃能力，不如讓worker之間用Git、聊天室跟共享筆記板自己協調。釋出的repo包含單節點Docker Compose版本與單agent基線，方便直接跟自己的設定比較。

🔗 **來源**
- 標題：Microsoft Open-Sources Agensh: A Multi-Agent Harness for 1,024 Agents
- 作者／機構：Microsoft Research
- 連結：https://www.marktechpost.com/2026/10/24/microsoft-agensh-multi-agent-harness-1024-agents/

#Agensh #MultiAgent #Microsoft #CodingAgents #LLM #AIAgents #OpenSource #SoftwareEngineering #AgentSwarm #DecentralizedAI
