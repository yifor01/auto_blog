---
title: 'Axis Robotics Releases AXIS: A Browser-Based Data Engine With 207 Robot Manipulation
  Tasks and 50,129 Trajectories'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/07/axis-robotics-releases-axis-a-browser-based-data-engine-with-207-robot-manipulation-tasks-and-50129-trajectories/
model: claude-code/sonnet
generated_at: '2026-09-07T20:46:03.370969'
score: 89
---

📌 AXIS：把機器人示範資料收集搬進瀏覽器裡

TL;DR：AXIS用瀏覽器teleoperation加後端GPU算力，讓機器人操作資料集能像軟體一樣持續擴充。

機器人操作資料集的成長速度一直遠遠跟不上模型，原因很直接：收集流程封閉又集中，專家在實驗室硬體上錄示範、離線後處理，最後發布一個從此不再更新的固定benchmark。來自Axis Robotics、UC Berkeley、Georgia Tech、NTU等機構的團隊，提出了一個不同的做法——AXIS把示範收集這件事搬進瀏覽器，把其餘所有算力密集的工作丟給後端GPU，並且把資料集當成會持續擴增的東西，而不是一次性交付的產物。

🤔 設計理念：把「便宜」與「昂貴」的部分拆開

AXIS的核心決策是不對稱分工。一般貢獻者只需要在瀏覽器裡，透過MuJoCo WebAssembly前端，用鍵盤、滑鼠、虛擬搖桿或手把，遙控一臺裝有平行夾爪的Franka Research 3。物理步進與Three.js渲染都跑在React UI執行緒之外，確保記錄下來的state-action樣本與模擬器本身同步，而不會受介面卡頓影響。真正燒算力的工作則放在別處：渲染用8張RTX 4090，訓練與評估則用8張A100。

🧩 任務怎麼來：生成而非手工撰寫

AXIS裡的任務由TaskGen自動生成：先把一句語言指令拆解成task、scene、object三種設定，透過image-to-3D pipeline檢索或生成對應的3D網格，依合理的物理尺寸重新縮放，再提出一個2.5D的空間佈局。一個layout supervisor會驗證整個場景，一旦違反限制就重新定位、旋轉或重新生成物件。每個任務都附帶結構化的成功判斷器，而且後端會重新執行這個判斷器，而不是直接相信前端回報的成功旗標——這是為了避免遠端瀏覽器端的判定被竄改或出錯。

目前釋出的快照包含207個任務、50,129個episode，橫跨7種場景類別，衍生出超過6萬個任務或場景變體。每一條軌跡都帶有任務中繼資料、embodiment、模擬器版本、機器人與物件狀態、動作、成功標籤，以及第三人稱視角加手腕視角的RGB-D觀測。論文提到超過7萬名社群成員參與貢獻。

📊 資料清理是一道正式的生產工序

清理流程被當作正式的資料生產步驟：關節變化量低於5e-3的樣本會被視為靜止並丟棄；接著用window大小15、多項式階數3的Savitzky-Golay濾波器平滑連續動作；再用三次雲形線(cubic spline)把網頁介面產生的6至8Hz取樣，重取樣到20Hz的目標頻率。論文的Table 1誠實揭露了這個取捨：平均加速度從1.3539降到0.4885，平均加加速度(jerk)從11.5899降到2.2243，但replay成功率也從100%掉到86.2%。清理過的episode接著會在IsaacSim中，從封裝好的模擬器狀態重播、關閉物理步進，讓已驗證的軌跡本身保持權威，同時隨機化場景、相機、材質與燈光。最終輸出是256×256的光線追蹤RGB影像，來自固定的第三人稱相機與手腕相機，深度資訊預設關閉。

🧩 訓練設定：以π0.5為起點

每個實驗條件都從釋出的π0.5 checkpoint出發(PaliGemma Gemma-2B backbone搭配Gemma-300M action expert)，可選擇先在模擬語料上繼續預訓練，再以相同超參數在LIBERO上微調。預訓練是全模型、不使用LoRA，採用flow-matching loss處理10步的動作分段(action chunk)，訓練10萬步，之後再進行3萬步的LIBERO後訓練。

📊 結果：整體scaling成立，但拆到單一軸向就不穩定

π0.5加上完整的AXIS-100%資料，在LIBERO-Plus上整體拿到88.8分，相對vanilla π0.5的83.9分，以及軌跡數量對齊的RoboCasa365對照組的57.5分。論文摘要引用的5.8%與37.3%都是以83.9分為基準換算的相對數字，換成點數差距則是4.9分與31.3分，讀起來更直觀。整體來看scaling確實成立：在25%、50%、100%三種資料規模下，分數分別是84.7、85.7、88.8。但拆到各個評測軸向，表現就不那麼一致——增益最大的落在資料增強真正有隨機化的地方，Sensor Noise提升13.7分、Camera提升11.3分，Background、Robot pose、Layout則各提升3.7、3.8、2.6分；反而Light與Language兩軸分別倒退1.7分與1.3分，Camera軸在AXIS-50%時甚至一度掉到68.8分，低於baseline的72.5分，直到用滿100%資料才回升。

⚠️ 限制與可部署性

訓練程式碼以OpenPI的patch layer形式公開，teleoperation平臺也已經可以直接在任何瀏覽器使用，但Hugging Face上的資料集被gated在2.36TB、僅限非商業學術用途，團隊也沒有釋出訓練好的policy checkpoint。換句話說，這套系統目前只能算「部分可部署」。

🎯 實務啟示

「瀏覽器眾包收集、後端GPU重運算」的分工模式，對想擴大機器人資料規模的團隊是個值得參考的架構思路；但論文自己攤開的per-axis數據也提醒我們，資料增強不是萬靈丹，有些維度(如光照、語言指令變化)未必能靠單純擴大資料量解決，設計評測時仍需拆解到軸向層級才看得出真實效果。

🔗 來源
- 標題：Axis Robotics Releases AXIS: A Browser-Based Data Engine With 207 Robot Manipulation Tasks and 50,129 Trajectories
- 作者／機構：Michal Sutter，MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/07/axis-robotics-releases-axis-a-browser-based-data-engine-with-207-robot-manipulation-tasks-and-50129-trajectories/

#Robotics #AXIS #DataEngine #ImitationLearning #MuJoCo #RoboticsAI #Teleoperation #OpenSourceAI #LIBERO #Simulation
