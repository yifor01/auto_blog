---
title: How to Train a Cross-Embodiment Robot Navigation Policy with AI Agents
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/how-to-train-a-cross-embodiment-robot-navigation-policy-with-ai-agents/
model: claude-code/sonnet
generated_at: '2026-08-27T17:24:09.189164'
score: 101
---

📌 用 AI Agent 訓練跨具身機器人導航策略：NVIDIA COMPASS 實戰

TL;DR：COMPASS 讓 coding agent 接手驗證、訓練、診斷的苦工，把換機器人、換場景的成本打下來。

同一套導航能力，換一臺機器人或換一個場景，往往得從資料蒐集、模擬資產、機器人介面到訓練診斷全部重來一遍。NVIDIA 的教學文章示範了如何用 coding agent 搭配 COMPASS 框架，把這個重複勞動變成一套可核准、可重現的流程。

🤔 導航能力為什麼難以跨機器人複用

導航不同於 locomotion（移動控制），後者只要產生穩定的動作即可；導航必須持續定位機器人、解讀周遭環境變化、選擇路線並避開障礙，才能安全抵達目標。把這套能力搬到新機器人或新場景，通常需要新的資料、模擬資產、機器人介面、訓練流程、診斷與評估，每換一組「機器人—場景」都要重做一輪，成本高又難以重現。

🧩 COMPASS 的設計理念：不重新學導航，而是學「修正量」

COMPASS（Cross-Embodiment Mobility Policy via Residual RL and Skill Synthesis）是一套讓跨具身（cross-embodiment）移動能力得以規模化的統一框架，靠的是從單一具身蒐集到的專家示範資料。它重用預訓練好的 NVIDIA X-Mobility 策略中的導航行為，並訓練一個「殘差專家（residual specialist）」：這是一個強化學習（RL）策略，負責針對特定機器人與環境去修正 base action，而不是從零開始重新學習導航。多個殘差專家累積的資料，之後還能被蒸餾（distill）成一個共用的跨具身策略。

這套開發流程被包裝成一組 repository skills：開發者只需定義機器人、場景來源與導航目標，coding agent 就會依循這些 skill 去驗證相依套件、準備資產、跑 smoke test、啟動訓練、診斷失敗原因並比較不同 checkpoint 的表現。流程中設有人工核准關卡，分別卡在場景驗收、單一環境的 smoke test，以及 checkpoint 晉升這三個節點。教學文章以 Boston Dynamics 的四足機器人 Spot 為參考機器人，分別把這套 agent 驅動的 COMPASS 工作流套用在內建場景與 SAGE-10K 場景上，並說明 NVIDIA Omniverse NuRec 如何支援實際掃描重建的環境；整個流程涵蓋 smoke test、殘差訓練、checkpoint 評估到執行期整合，也包含可選的里程計（odometry）整合。

🛠 怎麼跑起來：從環境驗證到人工核准

硬體與軟體需求方面，教學要求 Ubuntu 22.04 或 24.04、至少 32GB RAM、至少 16GB VRAM 的 RTX 系列 GPU、Linux 驅動 580.95.05（對應 Isaac Sim 6.0 測試版本，最低參考 GPU 為 GeForce RTX 4080，建議先跑 Isaac Sim Compatibility Checker）、Docker Engine 24 以上並搭配 NVIDIA Container Toolkit，以及一組有權限存取 gated 的 nvidia/COMPASS 與 nvidia/X-Mobility Hugging Face repository 的讀取 token。教學實測的組合是 Isaac Lab 3.0 搭配 Isaac Sim 6.0。

第一步是把 repository 的 skill 交給 coding agent。教學使用 Codex 進行開發，透過建立符號連結把 `.claude/skills` 底下的 compass、compass-doctor、compass-newembodiment 對應到 `.agents/skills`，Codex 支援符號連結的 skill 目錄；Claude Code 則可直接用 `/compass` 指令喚起同一套流程。取得 Hugging Face token 後，用 `export HF_TOKEN=hf_xxx`、`./docker/run.sh assets`、`./docker/run.sh build`、`source ./docker/activate` 依序把模擬資產下載到 `./assets/usd/`、預訓練的 X-Mobility checkpoint 下載到 `./assets/x_mobility.ckpt`；文章特別提醒 token 只能留在當前 shell，不要貼進 agent 對話或提交進版本控制，agent 也不應該要求、顯示或記錄這組 token。若下載時遇到 401 或 403，通常代表 repository 存取權限或 token 範圍不完整，應先解決驗證問題再去除錯 Isaac Lab。

流程的每個階段都會產出可審核的證據：驗證階段留下軟體與資產清單、環境報告與 smoke-test 記錄；準備場景階段留下已註冊的場景設定、occupancy map 與人工檢視紀錄；訓練階段留下固定的指令與設定、log、遙測資料與週期性 checkpoint；評估階段留下對齊過的評估流程、COMPASS 標準指標、影片與晉升建議；封裝階段則留下核准過的 checkpoint、設定、評估紀錄與 artifact manifest。每個核准關卡都回答同一組問題：必要輸入是否齊全、預期輸出是否出現、有沒有未解決的錯誤、證據是否足以繼續下一步。

容器啟動後，只需在 repository 根目錄對 coding agent 下達類似「$compass 驗證 Spot 的 COMPASS 環境，確認 pinned 的 repository 版本、容器、GPU、Isaac Lab 與 Isaac Sim 版本、模擬資產與預訓練 X-Mobility checkpoint，跑一次單一環境 smoke test，儲存驗證報告並停下等待核準」這樣的提示，$compass skill 就會對照 repository 現況執行相應的驗證步驟；若中途失敗，$compass-doctor 會做唯讀的健康檢查，回報可能原因，但不會偷偷改動環境。

場景準備則有三種來源可選：最快能重現的路徑是內建的 combined_multi_rack 倉儲場景，機器人、場景與 occupancy map 都已註冊好，最適合用來驗證安裝是否正確；此外還有 SAGE-10K 生成場景，以及透過 NVIDIA Omniverse NuRec 支援的實景重建場景。

🎯 實務啟示

這套流程的價值不在於 COMPASS 演算法本身有多新穎，而在於把「換機器人、換場景就要重做一輪」的苦工，交給 coding agent 在明確的 skill 邊界與人工核准關卡內完成，同時保留每個階段的可審核證據。對於同時要維護多臺機器人、多個場景的團隊，這種「agent 負責跑，人只在關鍵節點核准」的模式，或許比單純寫一套自動化腳本更容易擴充到新的機器人與新的環境。

🔗 來源
- 標題：How to Train a Cross-Embodiment Robot Navigation Policy with AI Agents
- 作者／機構：Tanya Lenz, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/how-to-train-a-cross-embodiment-robot-navigation-policy-with-ai-agents/

#NVIDIA #Robotics #ReinforcementLearning #AIAgents #IsaacSim #CrossEmbodiment #RobotNavigation #COMPASS #Codex #SimToReal
