---
title: Build Applications on NVIDIA BlueField Faster with NVIDIA DOCA Agent Skills
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/build-applications-on-nvidia-bluefield-faster-with-nvidia-doca-agent-skills/
model: claude-code/sonnet
generated_at: '2026-10-01T22:05:33.088220'
score: 90
---

📌 NVIDIA DOCA Agent Skills：讓通用AI代理學會DPU開發

TL;DR：NVIDIA開源SKILL.md格式，用65個真實任務測試，無技能時正確率僅19%，有技能後達100%。

想像你讓AI agent幫你寫BlueField DPU程式碼，結果它自信滿滿地呼叫一個根本不存在的函式。這不是偶發bug，而是NVIDIA在65個真實任務測試中，有59個都出現的狀況。

🤔 背景：通用agent為何在DOCA開發上失準

通用AI agent是基於pattern-matching從訓練資料生成答案，而非DOCA真實的API contract、硬體能力manifest或build system規格。DOCA的library範圍大、更新快、且與特定硬體緊密綁定，這些細節並不在一般訓練資料裡。沒有machine-readable的contract可供agent推理，agent所知道的與硬體、軟體實際支援的之間，也沒有穩定的介面保證。

🧩 架構：SKILL.md開放格式

DOCA AI agent skills圍繞一份輕量、開放的SKILL.md檔案，內含真實的API函式簽章、正確的pkg-config模組名稱、build container限制，以及常見失敗模式與對應的解法。技能涵蓋整個DOCA library，包括Flow、GPUNetIO、PCC等元件。每個技能scope到特定DOCA元件或workflow，agent載入後取得的不只是文件摘要，而是可以直接推理的machine-readable規格。這些skill不會取代agent本身，而是賦予它如同資深DOCA開發者般的領域知識。

📊 數據：65個真實提示詞的測試結果

NVIDIA team執行了65個真實的DOCA開發者提示詞，比較有無skills的agent表現，並以required-answer checklist（每項任務的pass/fail標準清單）評分。無skills時，agent常見的錯誤包括：

- API誤用（函式、旗標、image tag皆有誤）：59/65
- 未驗證硬體能力：46/65
- 錯誤的工具路由：39/65
- 跳過smoke test：34/65
- 猜測版本號：30/65

整體而言，無skills時agent只滿足19%的checklist項目；有skills時則在全部65個提示詞上都達到100%。

💡 四種實務場景的具體效果

文章舉出四個案例。第一，用真實API加速開發：面對設定DOCA Comch（Comm Channel）通道的提示，有skills的agent只使用真實存在的API呼叫、正確的參數順序與驗證過的旗標，不發明任何東西，這類API準確度的測試涵蓋63個提示詞，有skills版本每次表現都較佳。第二，寫程式前先驗證硬體：面對「測量從CUDA kernel發起RDMA WRITE延遲」的提示，有skills的agent會先確認GPU與NIC之間的PCIe拓樸、確認GPUNetIO是否支援，再決定要不要寫程式，而非事後才在真實硬體上發現不相容。第三，確保程式碼能編譯連結：針對DOCA Flow範例編譯失敗（undefined reference to doca_flow_init）的情境，有skills的agent能正確判斷這是連結時期錯誤，並用pkg-config查出doca-flow對應的正確連結旗標。

⚠️ 限制

素材僅提供NVIDIA自行執行的65組提示詞評估，獨立第三方複現的結果未提及；skills目前涵蓋範圍以DOCA函式庫為主，是否能擴展到其他NVIDIA平臺的agent開發流程，素材並未說明。

🎯 實務啟示

若團隊已經在用AI agent輔助DPU/DOCA開發，導入這些開源skills等於是替agent加裝一份「資深工程師的checklist」，省下的是每一次debugging corrections的時間。這種「把文件轉成machine-readable規格」的做法，也值得其他垂直領域的infra團隊參考：與其等agent犯錯後再修正，不如把API contract、硬體能力、build constraint整理成agent能直接推理的格式。

🔗 來源
- 標題：Build Applications on NVIDIA BlueField Faster with NVIDIA DOCA Agent Skills
- 作者／機構：Tanya Lenz，NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/build-applications-on-nvidia-bluefield-faster-with-nvidia-doca-agent-skills/

#NVIDIA #DOCA #BlueField #DPU #AIAgent #AgentSkills #InfrastructureAsCode #DeveloperTools #GPUNetIO #EdgeComputing
