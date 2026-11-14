---
title: OpenAI disbands its robotics team as its general models start running robots
source: Hacker News
url: https://fortune.com/2026/11/13/openai-disbands-robotics-team-as-its-general-models-start-running-robots/
model: claude-code/sonnet
generated_at: '2026-11-14T21:40:43.232483'
score: 60
---

📌 OpenAI 解散機器人團隊,通用模型直接「開車」上身

TL;DR：OpenAI 將獨立機器人團隊打散併入通用研究與應用組織,原因是通用模型已能直接操控機器人。

一家公司的展位出現在機器人學頂會的攤位圖上,卻在現場空無一物,只剩 logo。這正是 OpenAI 在德州奧斯汀舉行的 CoRL 大會上發生的場景,而背後的原因,是公司剛剛解散了獨立的機器人團隊。

🤔 **從獨立團隊到「併入主幹」**

Fortune 證實,OpenAI 已將機器人研究團隊併入公司主要研究組織,向首席研究官 Mark Chen 報告;應用機器人與硬體團隊則併入由總裁 Greg Brockman 主管的 Applied 組織。公司發言人將此定調為「對機器人願景的承諾」,而非撤退。

這不是 OpenAI 第一次在機器人領域進退。公司早年曾設有機器人團隊,但在 2020 年解散,共同創辦人 Wojciech Zaremba 當時提及機器人資料有限,通往 AGI 的路徑另有更有效方式。2024 年,OpenAI 重建獨立機器人團隊並與新創 Figure 合作開發人形機器人 AI 模型,但該合作在 2025 年 2 月告終,Figure 轉而自行開發機器人 AI。目前 OpenAI 仍在開發自有人形機器人,CEO Sam Altman 的目標是在 2027 年進行首次公開展示。

🧩 **通用模型 GPT-6 Astra 直接上場操控機器人**

這次重組背後的關鍵判斷是:通用的語言、程式碼與視覺模型,也可以直接用於「具身智能」(embodied AI),也就是控制機器人、自動駕駛車或無人機這類在物理世界中行動的裝置。OpenAI 表示,年初研究人員原本假設,推進機器人的最佳路徑是延伸 Sora 這類影片生成模型(因為要生成逼真影片,模型需隱含對物理世界的理解);但後來發現,GPT-6 Astra 這類通用前沿模型可以直接應用於機器人任務,這正是促使公司打散獨立機器人團隊的原因。

📊 **Nvidia 研究:通用模型打敗專用機器人模型**

研究人員給 Astra 提供攝影機影像、機器人資訊以及控制介面,讓模型直接下達機器人動作指令。根據一項 Nvidia 的研究,由 Astra 驅動的 agent 在一個模擬操作(manipulation)基準測試中達成 74.8% 的成功率,相較之下,該排行榜上表現最好的專用機器人模型成功率僅為 51.0%。

卡內基美隆大學機器人研究所助理教授 Guanya Shi 指出,通用模型在空間與推理能力上的進步,已經讓它們能處理過去需要專門訓練才能完成的任務,例如應對瓶子位置變化、光線改變,或是推理任務步驟哪裡出錯。不過他也提到,大型語言模型雖強大,但運算速度較慢且需雲端部署,代表機器人必須維持網路連線;因此機器人本機、不需持續聯網的小型專用模型仍有存在空間。

⚠️ **機器人新創的優勢:真實場域的部署經驗**

麻省理工學院教授、Walden Robotics 共同創辦人兼 CEO Russ Tedrake 則提出不同視角:機器人新創仍握有 AI 實驗室所沒有的優勢 — 它們的機器人已在工廠等真實場域中累積工作經驗。他認為,基礎模型越強,這些場域特定資料反而越有價值,因為機器人能更快地從中學習。Generalist 共同創辦人 Pete Florence 也表示,目前並不清楚哪一種模型路線會在機器人領域最終稱霸。

這次重組也發生在 OpenAI 面臨成本壓力的時間點:公司近期單季虧損達 109 億美元,同時正籌備新一輪募資並準備在 2027 年初叩關 IPO。

🎯 **對從業者的實務啟示**

對機器人與具身智能領域的工程師而言,這則重組釋放的訊號值得留意:通用前沿模型正在快速吃掉過去需要「專門空間智能」才能完成的任務類別,這對許多以「機器人需要專屬大腦」為募資前提的新創構成挑戰。但正如 Tedrake 所言,真實場域部署資料的價值並未消失,反而可能因基礎模型變強而被放大 — 這或許才是接下來值得關注的差異化戰場。

🔗 **來源**
- 標題：OpenAI disbands its robotics team as its general models start running robots
- 作者／機構：Fortune(經 Hacker News 轉載,原作者未標明)
- 連結：https://fortune.com/2026/11/13/openai-disbands-robotics-team-as-its-general-models-start-running-robots/

#OpenAI #Robotics #EmbodiedAI #GPT6Astra #AGI #HumanoidRobots #Nvidia #FoundationModels #AIStrategy #CoRL
