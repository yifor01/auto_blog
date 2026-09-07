---
title: UC Berkeley Researchers Release CUA-Lite, an Open Platform Unifying Sandboxes,
  Data, Evaluation and RL for Computer-Use Agents
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/05/uc-berkeley-researchers-release-cua-lite-an-open-platform-unifying-sandboxes-data-evaluation-and-rl-for-computer-use-agents/
model: claude-code/sonnet
generated_at: '2026-09-07T20:41:22.317935'
score: 102
---

📌 UC Berkeley CUA-Lite：用純 Docker 容器複刻 OSWorld，訓練代理不用再開 VM

TL;DR：CUA-Lite 把電腦操作代理的沙盒、資料格式、評測與 RL 訓練統一成一套介面，並用容器成功複現需要巢狀虛擬化的 OSWorld 基準。

想訓練一個能操作電腦的 agent，理論上需要環境、資料、代理、評測框架這四塊拼圖。實務上，這四塊分散在互不相容的一堆 repo 裡，光是把它們兜起來就足以讓一個研究計畫卡關數週——這不是模型能力的問題，而是基礎建設的問題。UC Berkeley 研究團隊釋出的 CUA-Lite，瞄準的正是這個痛點。

🤔 卡住 CUA 研究的不是模型，是四套不相容的基礎設施

CUA-Lite 的核心主張是「這是基礎建設問題，不是模型問題」：訓練與評測一個 computer-use agent（CUA）需要 agents、environments、traces 以及一套評估／訓練框架，而這四者目前散落在互不相容的獨立 repo 中。CUA-Lite 把它們收攏到同一個 action space、同一套資料 schema、同一行指令之下，橫跨桌面、瀏覽器與行動裝置三種平臺。

是否可部署？可以。整套工具鏈在 Python 3.12 下用 `uv sync --all-extras` 即可安裝，其輕量沙盒不需要 `/dev/kvm`，能跑在任何 Docker host 上，雲端執行個體、CI runner、巢狀容器環境全部相容。

🧩 拿掉巢狀虛擬化，用 GNOME 容器複刻 VM 基準

最具體的貢獻是 Lite.OSWorld。原版 OSWorld 提供一個高保真的 Ubuntu 桌面環境，但每個任務都要跑一整臺 QEMU/KVM 虛擬機，需要巢狀虛擬化——這在多數託管雲端基礎設施上根本不開放。CUA-Lite 把同一套任務組合與同一套評分程式，改跑在一個純 Docker 容器裡的 GNOME 桌面上。換掉 VM 用容器，保真度自然是最大疑慮，團隊直接給出驗證：在 13 個模型上測試，Lite.OSWorld 的分數與 OSWorld 原版 VM 的分數一致，代表在容器裡拿到的分數或訓練訊號，可以直接對應回真正的基準。

同一套底層基礎之上，還擴展出 Lite.ScaleCUA、Lite.CUAGym、Lite.CUAWorld 這幾個沙盒家族，其中 Lite.CUAWorld 涵蓋約 40 種應用程式，包括 Blender、QGIS、VS Code。整個平臺號稱擁有超過 3 萬筆可驗證任務。

🧩 一套資料 schema，統一十多個既有資料集

CUA-Lite 的第二層是 LiteSample：一套跨環境、跨代理、跨任務類型共用的監督式學習 schema，以純 parquet 加圖片的形式儲存。團隊已把十多個既有 CUA 資料集（Aguvis、OpenCUA、ScaleCUA、GUI-360、GUIOdyssey、Multimodal-Mind2Web 等）預處理成這套格式，免費公開在 Hugging Face 上；同時附上用前沿教師模型在沙盒中跑出的全新 rollout 資料，供蒸餾成更小的學生模型使用。由於不同模型家族各自需要不同的訓練格式，框架另外提供 per-model adapter，把統一的 LiteSample 打包成各模型自己的訓練格式，其中包含「history collapsing」，讓好幾個步驟共用同一次前向傳播。

🧩 一行指令切換模型與環境

代理與環境在 `lite.gym` 中相遇：畫面截圖進去、動作出來，每個平臺各自對應一套 action space。框架內建 10 個以上的代理（GPT、Claude、Gemini、Qwen3-VL、UI-TARS、Fara-7B、MAI-UI 等），整合超過 15 個 benchmark，涵蓋定位（ScreenSpot-Pro、OSWorld-G）、桌面（OSWorld、OSWorld-2、WindowsAgentArena、CUABench）、瀏覽器（WebArena、VisualWebArena、MiniWoB、WebVoyager、Online-Mind2Web、WebGym）與行動裝置（AndroidWorld、AndroidLab、MobileWorld、MobileGym）。整套操作介面就是在 `scripts/rollout.py` 中切換 `--model-id` 與 `--env-id` 兩個參數。

📊 訓練實測：SFT 提升近乎翻倍，RL 走 GRPO 路線

同一套迴圈也拿來做訓練。SFT 方面，README 記錄了在 Lite.ScaleCUA 桌面軌跡上微調 Qwen3-VL-2B-Instruct，在 332 個任務的 lite.osworld 評測子集上，平均 episode 回報從 0.138 提升到 0.237——這是雙 GPU 上的單一設定結果，並非獨立覆現的數字。RL 方面，環境中打分的 rollout 用於驅動建立在 Slime 之上的 GRPO 更新，並附上一個涵蓋 28 款應用、416 個任務的 MobileGym 實作範例。

🎯 實務啟示

對想投入 computer-use agent 研究的團隊而言，CUA-Lite 最大的價值不是新模型或新分數，而是把「環境保真度」與「基礎設施相容性」這兩個過去最耗工的環節解決掉：不必再為了跑 OSWorld 而搞定巢狀虛擬化，也不必為了對齊不同資料集的格式而重寫 pipeline。如果手上已有教師模型，用同一套沙盒生成 rollout 再蒸餾成小模型，是一條現成可走的路徑。

🔗 來源
- 標題：UC Berkeley Researchers Release CUA-Lite, an Open Platform Unifying Sandboxes, Data, Evaluation and RL for Computer-Use Agents
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/05/uc-berkeley-researchers-release-cua-lite-an-open-platform-unifying-sandboxes-data-evaluation-and-rl-for-computer-use-agents/

#CUALite #ComputerUseAgent #UCBerkeley #OSWorld #OpenSource #AgentTraining #ReinforcementLearning #GRPO #GUIAgent #AIInfrastructure
