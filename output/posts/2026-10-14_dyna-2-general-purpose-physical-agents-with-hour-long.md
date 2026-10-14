---
title: 'Dyna-2: General Purpose Physical Agents with Hour-Long Autonomy — Jason Ma,
  Dyna Robotics'
source: Latent Space
url: https://www.latent.space/p/dyna
model: claude-code/sonnet
generated_at: '2026-10-14T20:56:31.587167'
score: 95
---

📌 連續摺餐巾紙 24 小時不失誤：Dyna-2 的世界動作模型如何讓機器人真正上工

TL;DR：Dyna Robotics 用超過百萬小時人類影片訓練出 world-action model，已把機器人部署進真實餐廳與飯店執行長時間自主作業。

機器人展示影片很多，但多數撐不過一次完美剪輯的 demo。Dyna Robotics 共同創辦人兼首席科學家 Jason Ma 在訪談中描述的畫面卻不同：機器人在鼎泰豐連續 24 小時摺餐巾紙，成功率 99.4%，中途整疊餐巾紙被拉倒，機器人還能自己恢復繼續工作。

🤔 **真正的難題不是單次任務，是長時間可靠自主**

Jason Ma 認為機器人在真實世界的核心挑戰是 reliable, long-horizon autonomy，而不是把單一動作做得多漂亮。這也是 Dyna-2 這個 world-action model 想解決的問題。

🧩 **世界動作模型：用預測未來影片來指導機器人動作**

Dyna-2 的輸入包含機器人攝影機拍到的過去影片／影像、機器人自身關節編碼器（joint encoder）讀到的角度資料，以及語言指令。輸出不只是機器人可執行的動作，還可以輸出未來影片（或其表示）來先行推演，再據此產生動作——Jason Ma 將這個過程類比為 chain-of-thought，只是推理空間換成了視覺與物理世界。團隊用 diffusion transformer 搭配 flow matching 做即時控制，並透過跨 embodiment transfer 讓模型從人類 egocentric video 學到的知識轉移到機器人身上。有了這套架構，機器人只需要約 45 分鐘的示範就能學會新任務。

🧩 **自建輪式半人形機器人，而非現成人形機器人**

Dyna 選擇自建硬體而非採用市售人形機器人，原因之一是靈巧手（dexterous hand）在長時間運作下仍會過熱，加上感測資料缺失仍是物理 AI 的重大瓶頸。團隊也打造了 agentic harness，讓機器人能執行多步驟、長達數小時的工作流程，而不只是單一動作循環。

📊 **真實商用部署：鼎泰豐與 Best Western**

素材提到的實際落地場景包括鼎泰豐和 Best Western，其中鼎泰豐的餐巾紙摺疊任務達到 24 小時連續運作、99.4% 成功率，並具備自我恢復能力，這與多數停留在 pilot 階段的機器人專案形成對比。

💡 **「機器人版的 Bitter Lesson」**

Jason Ma 提出的觀點呼應了 AI 領域著名的 Bitter Lesson：擴增資料規模比針對特定場景做工程特化更有效，這也是 Dyna 選擇用百萬小時人類影片做 pretraining、而非手工設計特定任務解法的核心理念。

⚠️ **硬體與資料仍是瓶頸**

靈巧手過熱、感測資料不足，以及機器人領域缺乏「等同於網路規模」的現成資料來源，都是素材中點出尚待解決的限制。

🎯 **實務啟示**

對做 physical AI 或 agent 系統的工程師，Dyna 的路線提供一個參考框架：先用大規模、低成本的人類影片建立通用的世界模型，再用少量真實示範做任務微調，並把 agentic harness 的設計重心放在「長流程的穩定執行與錯誤恢復」上，而非單一動作的精準度。

🔗 **來源**
- 標題：Dyna-2: General Purpose Physical Agents with Hour-Long Autonomy — Jason Ma, Dyna Robotics
- 作者／機構：Latent Space（訪談對象：Jason Ma, Dyna Robotics）
- 連結：https://www.latent.space/p/dyna

#Robotics #WorldModel #DynaRobotics #DiffusionTransformer #FlowMatching #PhysicalAI #AgenticAI #AutonomousRobots #AIHardware #EmbodiedAI
