---
title: Optimizing Agent Reliability and Tool Calling Efficiency for Chip Design Using
  NVIDIA NeMo Gym
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/optimizing-agent-reliability-and-tool-calling-efficiency-for-chip-design-using-nvidia-nemo-gym/
model: claude-code/sonnet
generated_at: '2026-10-14T21:00:26.102098'
score: 85
---

📌 【NVIDIA】晶片驗證 Agent 靠 NeMo Gym 從 55 分衝上 95 分

TL;DR：Siemens 用 NVIDIA NeMo Gym 評估並改進晶片 characterization agent，benchmark 綜合分數從約 55% 提升到約 95%。

AI agent 產出的檔案看起來頭頭是道，卻可能是錯的——在晶片設計這種多階段流程裡，一個早期的設定錯誤會悄悄滲透進每一個後續步驟，最終生出一份看似正常、實際上有缺陷的 Liberty 檔。

🤔 **一個早期設定錯誤，會悄悄滲透到整份晶片庫**

Standard-cell characterization 是替晶片中的邏輯 cell，在各種工作條件下產生準確的 timing、power 與 noise 模型，每當晶圓廠發布新的 process design kit（PDK，內含 SPICE 電晶體模型、設計規則，以及 process／voltage／temperature 條件定義）時，既有的 characterization 資料就可能不再準確描述新元件，timing 與 power 模型必須針對每個受影響的 cell，在 input slew、output load、PVT 條件的各種組合下重新產生與驗證。Siemens Fuse EDA AI Agent 透過 MCP servers 與 skills，把 Solido Characterization Suite 的工具開放給 Claude Code、Codex、Cursor 等常見 coding harness 使用，但 agent 得完成工具設定、大規模 SPICE 模擬、分散式運算、Liberty 檔產生、除錯與最終驗證，其中任何一站出錯，往往不是乾淨地失敗，而是產出帶著錯誤門檻值、缺漏 corner 或不完整 cell 的「看似正常」結果，而這些階段彼此依賴，早期的設定錯誤會一路傳遞到最後。

🧩 **不看中間步驟，只用最終 Liberty 檔驗證**

NeMo Gym 是 NVIDIA NeMo 系列中用來評估與改進模型及 agent 的開源函式庫。它替每次 rollout 定義 task、tools、state 與 verifier，讓每次嘗試都從乾淨狀態出發、結果可以互相比較，並完整記錄 thinking trace、輸入輸出訊息與工具呼叫。團隊借此建立了一個可重複的優化迴圈：

- Step 1：在自訂 NeMo Gym 環境中，用版本化的 task 與 verifier 跑出 baseline rollout。
- Step 2：檢視 trajectory、失敗的工具呼叫，以及 verifier 的診斷結果。
- Step 3：找出模糊不清的指令、沒有效果的動作，以及選錯的工具。
- Step 4：修正 agent 的 skills 與 MCP 工具描述。
- Step 5：在相同評估條件下，重跑同一批 task。
- Step 6：比較驗證後的結果，以及每一次成功所耗費的效率。

團隊發現，端到端驗證揪出了中間檢查漏掉的錯誤：最終的 Liberty 驗證才暴露出缺漏的 cell 與操作條件、錯誤的 slew 門檻值,以及超出容許範圍的 timing 或 power 數值。為了讓這套評估可重複，團隊把最終的 composite reward 拆成五個關卡：Coverage（是否產出所有預期的 cell 與 PVT corner）、Validity（Liberty 檔是否格式正確、可被驗證工具使用）、Relative validation（輸出是否在參考基準之外又引入新的失敗）、Accuracy（timing 與 power 數值落在容許範圍內的比例），以及 Integrity（是否真正跑完整個流程，而非沿用、截斷或重新格式化既有數值）。只要五個關卡中有任何一個沒通過，整體 reward 就直接判定為零；五關全過時，reward 才依照數值落在容許範圍內的比例給分。

📊 **綜合分數 55% 衝上 95%，輪數與 token 同步下降**

團隊用開源的 GF180MCU PDK 作為 benchmark，資料集涵蓋 229 個 standard cell、36 組 PVT corner，SPICE 模擬使用 Solido AFS。為了方便調校，每次執行把流程限制在 2 個 cell、36 組 PVT corner 的子集即可，每次 rollout 約需 1.5 到 2 小時。團隊以 Claude Opus 4.8 搭配 Claude Code 作為固定的模型與 agent harness，總共跑了約 25 次 rollout。經過多輪評估、持續修正 agent 的 characterization skills 與 MCP 工具描述後，benchmark 綜合分數從約 55% 提升到約 95%，同時減少了對話輪數（turns）與輸出 token 量。

⚠️ **調校樣本小，工具鏈也綁得死**

調校過程只用了 2 個 cell 的子集，而非完整的 229 個 cell，而且整套做法高度綁定 Siemens Fuse 與 Solido Characterization Suite 的特定工具鏈，若要套用到其他 EDA 流程，仍需要重新定義對應的 verifier 與 reward 指標。

🎯 **錯誤會累積，所以要用硬門檻式 reward 把關**

這個案例給所有在建多階段 agentic workflow 的團隊一個提醒：只檢查中間步驟是不夠的，錯誤會沿著 pipeline 悄悄累積；用真正的最終產出定義 verifier，並把 reward 設計成「任一關卡沒過就是零分」的硬門檻，再搭配可重複、版本化的評估環境，才能把「看起來對」和「真的對」的輸出區分開來。

🔗 **來源**
- 標題：Optimizing Agent Reliability and Tool Calling Efficiency for Chip Design Using NVIDIA NeMo Gym
- 作者／機構：Tanya Lenz，NVIDIA
- 連結：https://developer.nvidia.com/blog/optimizing-agent-reliability-and-tool-calling-efficiency-for-chip-design-using-nvidia-nemo-gym/

#NVIDIA #NeMoGym #ChipDesign #EDA #AIAgents #MCP #RewardDesign #Siemens #Semiconductor #AgentReliability
