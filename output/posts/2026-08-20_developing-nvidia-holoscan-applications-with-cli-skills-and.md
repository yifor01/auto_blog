---
title: Developing NVIDIA Holoscan Applications with CLI, Skills, and AI Coding Agents
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/developing-nvidia-holoscan-applications-with-cli-skills-and-ai-coding-agents/
model: claude-code/sonnet
generated_at: '2026-08-20T06:30:41.384761'
score: 92
---

📌 【NVIDIA】用 Coding Agent 打造 Holoscan 即時應用

TL;DR:NVIDIA示範用Codex搭配Holoscan CLI,迭代打造內視鏡分割應用。

如果把跟工程師一樣的文件、範例與指令列工具都交給 coding agent,它能不能真的把一個即時 AI 應用從零做到能跑、能測、能量測效能?NVIDIA 用一個內視鏡工具分割(tool segmentation)應用實測了這個問題。

🤔 通用 coding agent,能不能像工程師一樣開發?

NVIDIA Holoscan 是用來在邊緣端建構即時 AI 應用的平臺,應用範圍涵蓋醫學影像到機器人。HoloHub 是它的搭配儲存庫,收錄不斷增加的參考應用與元件。這次實驗想了解的是:通用型 coding agent 能否使用跟工程師相同的範例、文件與開發工具,完成實際的開發任務。

🧩 共用的介面:Holoscan CLI 與開發技能

整套工作流程透過 ./holohub 這個包裝過的 Holoscan CLI 提供共用的執行介面:agent 可以透過 CLI 探索開發操作,工程師也能檢視並重複執行同一批指令。agent 額外拿到的資源包括:具備 Bash 執行權限的 Holoscan CLI、以漸進式揭露(progressive disclosure)模式透過 agents.md 提供文件的 HoloHub 儲存庫,以及 holohub-app-lifecycle、holohub-debug-build-run 兩項 HoloHub 開發技能。這次示範使用的是搭配 GPT-5.6 sol max mode 的 Codex,但整套工作流程本身是與 agent 無關的(agent-agnostic)。開發流程採迭代進行:工程師定義目標與限制條件,agent 檢視相關範例、實作應用程式碼並透過 CLI 執行必要的開發操作,工程師再檢視程式碼、輸出與測試結果,為下一輪迭代設定目標。

🧩 迭代一:先讓最小可行應用跑起來

團隊複用既有的 MONAI 內視鏡工具分割模型與 Holoscan 範例影片,並先確認既有應用 monai_endoscopic_tool_seg 能在本機正常運作。第一個提示詞明確要求 agent 使用 holohub-app-lifecycle 技能建立一個獨立的新 Python HoloHub 應用,複用 MONAI 模型、範例資料、前處理與推論邏輯,在 HoloViz 疊層畫面中呈現模型輸出的遮罩、覆蓋率、時間軸與不確定性量測,且明確要求不得訓練或修改模型權重。agent 依序檢視了內視鏡、分割、HoloViz、錄製與測試相關的範例(其中 monai_endoscopic_tool_seg、endoscopy_tool_tracking、surgical_scene_recon 特別有參考價值),接著用 ./holohub create 產生並註冊標準骨架,實作應用圖(application graph)、執行模式、測試與文件,最後透過 ./holohub run 建置並執行。完成的應用串連了影片播放、前處理、TensorRT 推論、SDK 分割後處理、遙測與 HoloViz,對每個播放畫面都執行推論與遮罩後處理。這一輪 agent 處理時間約 40 分鐘,工程師則用跟 agent 相同的指令 ./holohub run endoscopy_tool_segmentation_dashboard visual --language python 檢視實際運作的應用。

🧩 迭代二:把展示變成可重複的效能量測

第二輪提示詞要求 agent 修正視覺輸出、加入更有意義的統計量(工具面積、遮罩位移、時序 IoU 作為穩定度指標、邊緣熵、FPS、邊界框位置),移除播放過程中不會變化的數值,並加入能記錄實際延遲、以 Python 繪圖的 benchmark 模式。最終應用具備三種執行模式:visual 模式以來源速度在互動視窗中執行完整範例;smoke 模式進行 60 個畫面的快速無畫面錄製,產出明確的通過/失敗結果;benchmark 模式離線處理 300 個畫面,匯出量測數據與圖表。這些模式與測試都可以透過 ./holohub modes、./holohub run ... benchmark、./holohub test 等指令探索與執行,不需要記住複雜的容器與應用腳本細節。benchmark 模式使用 Holoscan Data Flow Tracking,沿著影片播放、前處理、推論、遙測、離線 HoloViz 到畫面輸出這條路徑量測延遲,概念上重用了既有的 holoscan flow benchmarking 模組。這一輪的 agent 處理時間約 20 分鐘。

📊 第三輪:模型是不是每一畫面都在跑推論

有了可重複的 benchmark 模式後,團隊才能在第三輪提示詞中,進一步檢查深度學習模型是否對每一個畫面都執行推論,素材在此處收尾,尚未揭露這一輪調查的具體結果。

⚠️ 第三輪結果尚未揭露

素材只完整呈現了前兩輪迭代的提示詞、agent 行為與處理時間;第三輪關於延遲最佳化的調查結果並未提供。此外,整個示範建立在一個已經存在、且已驗證可在本機運作的既有應用之上,並非從完全空白的專案開始。

🎯 把目標拆成可審查的小迭代

這個案例示範的工作方法值得工程團隊借鏡:與其用一個提示詞要求 agent 做完整個專案,不如把最終目標拆成一系列可獨立檢視的小迭代(環境是否配置正確、模型能否端到端跑通、視覺化是否有意義、延遲能否重複量測、吞吐量能否在不犧牲功能的前提下提升),每一輪都產出可檢視的程式碼、輸出與測試,再據此決定下一輪的提示詞與設計選擇。讓 agent 與工程師共用同一套 CLI 介面,也讓審查過程變得更直接:工程師可以重複執行 agent 用過的同一條指令,而不必另外理解一套黑盒流程。

🔗 來源
- 標題:Developing NVIDIA Holoscan Applications with CLI, Skills, and AI Coding Agents
- 作者／機構:Elizabeth Goodman,NVIDIA Developer
- 連結:https://developer.nvidia.com/blog/developing-nvidia-holoscan-applications-with-cli-skills-and-ai-coding-agents/

#NVIDIAHoloscan #HoloHub #AICodingAgent #Codex #EdgeAI #MedicalImaging #AgenticWorkflow #DeveloperTools #TensorRT #RealTimeAI
