---
title: 'Reward AI Releases OM-1: A Robot Policy Trained on Human Demonstrations Only,
  With No Teleoperation or On-Robot Data'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/14/reward-ai-releases-om-1-a-robot-policy-trained-on-human-demonstrations-only-with-no-teleoperation-or-on-robot-data/
model: claude-code/sonnet
generated_at: '2026-09-15T20:37:22.210851'
score: 86
---

📌 OM-1：純手套示範資料，練出能上機器人的操作策略

TL;DR：Reward AI的OM-1只靠人類戴手套示範訓練，完全不用機器人資料，但目前不開源、無法自行部署。

如果只讓機器人「看人類做一次」就學會抓取、翻轉、分類物品，而完全不需要遙控操作(teleoperation)或機器人自身收集的資料，這聽起來像是在賭一個大膽的假設。機器人新創公司Reward AI剛剛端出的OM-1(Omnibody Model 1)，正是在賭這件事。

🤔 為什麼不用機器人資料訓練？

目前多數機器人基礎模型仰賴遙控操作或機器人自行收集的資料進行訓練，這類資料天生綁定在單一機器人本體(embodiment)上：換一臺手臂、換一個機器人，資料就得重來。Reward AI的團隊(先前參與過DexCap、HumanPlus、ALOHA等專案)則主張，人類等級的操作能力不會單靠更多這類資料或更多算力堆出來，並援引Anderson的「More Is Different」作為論點依據。他們的做法是把「擷取、學習、控制」三件事當成同一套管線設計，讓今天錄下的示範資料，也能訓練未來才會出現的機器人本體。這個原則被總結為一句話：「One Model, One Data Interface, Any Body」。

🧩 從手套到策略：Omnibody Hand與單一資料介面

整套系統的起點是Omnibody Hand，一個延伸自團隊先前DexCap可攜式動作捕捉技術的穿戴裝置。它不是逐關節複製人手動作，而是圍繞「選擇接觸點、在手中重新調整物體方向、在精細抓握與力量抓握之間切換」等關鍵功能設計的七自由度(7-DOF)裝置，可捕捉拇指與食指的捏合、拇指與食指的屈伸，以及中指、無名指、小指在MCP關節處的耦合動作。

Reward AI把人體工學也當成資料品質問題來處理：一個會滑動或限制配戴者動作的裝置，只會產出「代償性」的抓握動作，反而汙染資料。手套內建的遠端屈曲(distal flexion)機制可以吸收不同使用者手指長度的差異，因此不需要為每個人調整裝置。

「One Data Interface」則是把配戴者的動作即時轉換成訓練資料，全程不需要事先搭建場景、也不需要人在旁邊監督。整套設計以輸送帶分揀為目標情境，也就是人類在極短時間內完成「發現物體、抓取、丟出」的動作。為了完整捕捉這個過程，手套結合了高頻觸覺感測、接觸前的鄰近感測(proximity sensing)，以及在快速動作中仍能維持影像脈絡的global-shutter手內攝影機。

📊 手部姿態追蹤：唯一公開的量化數據

文章中唯一附上具體數字的部分是手部姿態追蹤的精度。業界常用的視覺慣性(visual-inertial)追蹤在快速反向動作時，精度會被影像更新頻率卡住上限，Reward AI因此加入電磁感測與擾動補償進行強化。

在讓兩種追蹤器於兩個機械止點之間、以3至67公分/秒共八種速度往返移動(每種速度取十次平均)的測試中，電磁追蹤的平均超調誤差(overshoot error)從約0.4毫米上升到9.5毫米，而視覺慣性追蹤則從約2.1毫米上升到24.9毫米——在最高速度下誤差降低了60%，且每次測試結果的離散程度也更小。力量資訊會與同一軌跡一起記錄下來，讓每筆示範同時保留路徑與施力兩種資訊。

OM-1直接從人類動作生成機器人動作，中間不經過任何機器人本體作為橋接。由於每筆示範資料格式一致，訓練並不區分預訓練與後訓練階段，第一筆錄製的示範與最新一筆示範，都是在同一階段訓練同一個策略。輸入端是手套的多模態資料流：影像、觸覺訊號、手指間鄰近距離，以及手部姿態軌跡，每種模態都依照感測器原生取樣率處理，而不是統一降採樣，讓高頻的觸覺與動作線索得以保留。輸出端則涵蓋動作方向、速度、力量，以及抓取起始等事件的時機。Reward AI表示為此打造了一套新的高效推論架構，但並未公開架構細節或參數量。

策略之下還有一層以強化學習在模擬環境中訓練的高頻控制層，用來處理速度與加速度相關的動態、外部擾動與系統延遲。當傳統控制器因意外負載偏離參考軌跡後往往無法恢復，這一層則能持續保持參考軌跡並收斂回來，這也是機器人能打開完全閉合的冰箱門、或搬起重量未知的箱子的原因。控制層運作在自己的時脈上，即使策略仍在計算下一步動作，控制也不會因推論延遲而中斷；由於前後兩次預測的動作銜接未必平順，這一層還會即時最佳化動作之間的轉換。同一套動作空間同時涵蓋操作與移動式機器人的導航。

Reward AI表示，OM-1能在少於30分鐘的人類示範資料下學會全新任務，包含具挑戰性的動態與長時間跨度任務，並將此歸功於整套整合管線，而非策略模型本身。官網說明所有公開影片皆以1倍速播放，模型可涵蓋機械手臂、有腿人形機器人與輪式移動操作平臺。

⚠️ 沒有數據佐證，也還無法自行部署

目前沒有公開任何成功率、與公開基準線的比較，也沒有論文發表，所以以上宣稱屬於「示範影片佐證」而非「基準測試佐證」。更重要的是，OM-1目前是Reward AI的內部策略，沒有釋出權重、程式碼、資料集或API，開發者暫時無法在自己的硬體上執行它。

🎯 實務啟示

對機器人工程師而言，OM-1提出的思路值得關注：把資料擷取裝置、學習演算法與控制層當成一體設計，而不是分頭最佳化，或許是擺脫「資料綁定單一本體」困境的一種方向。但在權重與程式碼公開之前，這仍只是一個值得追蹤、尚無法驗證與複現的方向。

🔗 來源
- 標題：Reward AI Releases OM-1: A Robot Policy Trained on Human Demonstrations Only, With No Teleoperation or On-Robot Data
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/14/reward-ai-releases-om-1-a-robot-policy-trained-on-human-demonstrations-only-with-no-teleoperation-or-on-robot-data/

#RoboticsAI #ManipulationPolicy #ImitationLearning #RobotFoundationModel #HumanDemonstration #TeleoperationFree #DexterousManipulation #RewardAI #EmbodiedAI #RoboticsResearch
