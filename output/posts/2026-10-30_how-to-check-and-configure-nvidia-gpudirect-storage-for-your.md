---
title: How to Check and Configure NVIDIA GPUDirect Storage for Your Platform
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/how-to-check-and-configure-nvidia-gpudirect-storage-for-your-platform/
model: claude-code/sonnet
generated_at: '2026-10-30T21:51:25.962724'
score: 69
---

📌 NVIDIA 推出 gds-diag：一行指令診斷 GPUDirect Storage 設定

TL;DR：NVIDIA 開源 gds-diag 診斷工具，自動找出 GPUDirect Storage 設定問題，並可透過 AI agent skill 操作。

NVIDIA GPUDirect Storage（GDS）能讓 GPU 直接存取儲存裝置，省掉資料繞經 CPU 與系統記憶體的路徑，藉此提升頻寬、降低延遲，同時減少 CPU 與記憶體用量。問題是，GDS 支援的架構、儲存方案與部署情境非常多，官方文件雖然詳盡，但要在自己的環境裡找到正確的設定組合，本身就是一項工程。NVIDIA 的 GPUDirect Storage 團隊因此做了 gds-diag，把這套排查流程寫成一個開源命令列工具。

🤔 **為什麼需要專用診斷工具**

GDS 要正常運作，牽涉 NVIDIA 資料中心級 GPU、CUDA Toolkit 版本、作業系統設定、容器環境，甚至特定儲存目標的相容性，任何一個環節設錯都可能讓加速路徑失效卻找不出原因。gds-diag 的目標，就是把「評估環境、找出問題、建議改善方式」這個流程自動化。

🧩 **四大類診斷子命令**

gds-diag 本身是一個單一的 Python script，透過不同子命令對應不同診斷任務，官方把它們分成四個類別：
- 端到端檢查：直接跑 `all` 子命令，工具會自動挑選並依序執行適合該路徑的診斷項目，不管是裸機、虛擬機或容器環境都適用。
- 安裝前準備：`pre-install` 檢查 GPU 支援與 CUDA Toolkit 安裝狀況；`support-matrix` 列出目前支援的儲存目標，可用 `--static` 看一般支援資訊，或用 `--live` 帶入目前系統的實際設定狀態。
- 驗證安裝結果：`post-install` 檢查 GDS 是否安裝正確並找出障礙點；`config-audit` 檢查影響 GDS 行為的設定檔與環境變數。
- 深度診斷：`container-check` 評估 containerd、Docker、Enroot、Kubernetes 等容器環境下的 GDS 支援；`mount-check` 針對特定掛載點或目錄做診斷。

每一筆診斷結果都會標上狀態徽章：FAIL 代表確定的阻斷因素，WARN 代表潛在風險，INFO 是補充資訊，PASS（只有加上 `--verbose` 才會顯示）代表該項目正常。每個發現都附帶說明與建議的改善方案，但 gds-diag 本身不會自動套用這些修正，也不會更動系統設定，決定權留給使用者或管理員。診斷結果也能用 `--json` 輸出成結構化資料，方便餵進其他工具或存檔備查。

文中示範了一個情境：用 `config-audit --config` 指向一份準備上線的設定檔，工具直接揭露其中一個設定項目拼字錯誤；修正後再跑一次，config-audit 確認設定有效並給出額外的提示資訊。

🧩 **怎麼安裝與使用**

使用 gds-diag 只需要一臺 Linux 系統與 Python 3.8 以上版本；GDS 本身需要 NVIDIA 資料中心級 GPU 與 CUDA Toolkit 12.2 以上，但這些並非 gds-diag 工具自身的依賴。工具收錄在 NVIDIA Magnum IO 的 GitHub repo 裡，執行 `git clone https://github.com/NVIDIA/MagnumIO.git` 之後進入 gds-diag 目錄，執行 `gds-diag.py --help` 即可瀏覽所有子命令；若不確定從哪裡下手，直接跑 `./gds-diag.py all /path/to/check` 讓工具自動判斷該跑哪些檢查。

🧩 **搭配 AI agent skill 的自然語言介面**

gds-diag 還附帶一個可選的 agent skill，幫命令列工具加上自然語言介面與協調層。這個 skill 在用 Claude 或 Codex 之類的 coding assistant 開啟 gds-diag 目錄時會自動啟用，也可以用 `/gds-diag` 明確呼叫。它的角色不是重做一遍底層工具已經有的確定性檢查，而是負責解讀使用者的意圖、選擇並呼叫對應的子命令、協調多步驟的診斷流程，並進一步解讀診斷結果、套用系統情境，再提出或執行建議的補救動作。文中列出的範例問法包括「這套系統能用 GDS 嗎？」「/mnt/data 能用嗎？」「要怎麼把 /mnt/data 的 GDS 設定調到最佳？」「哪個 NVMe 裝置離 GPU3 的局部性最好？」

⚠️ **限制**

gds-diag 官方強調自己只做診斷與建議，不會主動修改系統；agent skill 目前驗證過的對象是 Claude 與 Codex，作者表示其他工具也可能可用，但沒有明確保證。

🎯 **實務啟示**

對於負責 GPU 儲存管線的平臺或 MLOps 工程師來說，把 `gds-diag all` 排進部署驗證流程，可以在正式啟用 GDS 前就抓到常見的設定錯誤；而 agent skill 這層自然語言介面，則讓不熟悉所有子命令旗標的人，也能用口語問題快速定位問題所在，降低排查門檻。

🔗 **來源**
- 標題：How to Check and Configure NVIDIA GPUDirect Storage for Your Platform
- 作者／機構：Phil Carns, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/how-to-check-and-configure-nvidia-gpudirect-storage-for-your-platform/

#NVIDIA #GPUDirectStorage #GDS #GPUComputing #MagnumIO #MLOps #OpenSource #ClaudeCode #Codex #StorageInfra
