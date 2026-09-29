---
title: 'H Company Releases Holo4: Open-Weight Computer-Use Models That Click, Code
  and Call Tools Across Desktop, Web, Android and APIs'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/29/h-company-releases-holo4-open-weight-computer-use-models-that-click-code-and-call-tools-across-desktop-web-android-and-apis/
model: claude-code/sonnet
generated_at: '2026-09-29T21:37:22.594404'
score: 107
---

📌 【H Company】Holo4 開源:一套模型走遍桌面、網頁、Android 與 API

TL;DR：Holo4 是能點擊、寫程式、呼叫 MCP/API 工具的通用電腦操作模型,提供 Apache 2.0 開源權重可自架部署。

GUI agent 沒有畫面就當機,工具型 agent 遇到沒有 API 的軟體就卡住——H Company 想用同一套模型解決這兩種窘境。

🤔 為誰而做:跨平臺的通用電腦操作 agent

H Company 發表 Holo4,一系列給 AI agent 使用的通用電腦操作模型。它鎖定的痛點很明確:純 GUI 型 agent 沒有畫面就無法運作,純工具呼叫型 agent 遇到沒有 API 的應用程式就會卡住。Holo4 可以在桌面、網頁、Android、程式碼沙箱與商業 API 上運作,同一套模型、同一種呼叫方式,適用於每一種平臺。

🧩 架構:一套 vision-language 模型搭配開源 harness

Holo4 提供兩種尺寸:Holo4 27B(dense 架構)與 Holo4 35B-A3B(Mixture of Experts,啟用 3B 參數),兩者在 H Models API 上都支援 256K context。Holo4 27B 從 Qwen3.8-27B 微調而來,Holo4 35B-A3B 則建立在 Qwen3.6-35B-A3B 之上,兩者都搭配 H 公司開源的 hai-agents harness:harness 把螢幕截圖與工具回傳結果送給模型,再執行模型要求的點擊、輸入文字、程式碼與工具呼叫。

訓練資料方面,H 公司內部的 Agentic Task Factory 從文件、截圖與真實軟體中建立可驗證的任務環境,目前已產出約一萬個任務,其中網頁應用 4 千、MCP 伺服器 3 千、桌面與作業系統 3 千;任務要通過驗證器嚴格拒絕「差不多對」的結果,且 agent 必須透過真實介面完成才算解題成功。監督式微調(SFT)資料集共 127B token,約四分之三是成功的 agentic 軌跡,其中桌面佔 45%、網頁 14%、MCP 與 API 12%、行動裝置 3%。強化學習階段則以非同步線上 RL 訓練兩個 LoRA 專家,一個負責桌面與網頁,另一個負責終端機、MCP 與 API,兩者最後以相同權重合併,不再額外訓練。H 公司也依據 OSWorld 2.0 的失敗案例分析重建了 agent 迴圈,最大的改動是讓記憶在數百個步驟中保持可靠,以及在桌面機器上加入 shell。此外,H 公司也釋出以 NVIDIA Nemotron 3 Nano Omni 為基礎、透過 Nemotron Coalition 打造的 Holotron4 Nano,同樣的組合把 OSWorld 分數從基礎模型的 21.0% 拉高到 76.3%。

📊 短任務表現亮眼,長流程仍有落差

依 H 公司公布的評測表,Holo4 27B 在 OSWorld 上取得 85.2% 分數,每個任務成本 0.08 美元,其 Qwen3.8-27B 基礎模型則是 84.3% 分數、成本 0.22 美元;在 AndroidWorld 上,Holo4 27B 達到 85.1%。但在長流程任務上落差明顯:OSWorld 2.0 中,Holo4 27B 得分 61.7%、每任務成本 1.22 美元,而 Claude Opus 5.5(依 H 公司數據)得分 81.8%、成本 8.48 美元,H 公司也提醒不同廠商使用的 harness 與 effort 設定不同,跨廠商比較僅供參考方向。在 AutomationBench 上,Holo4 27B 整體得分 45.4%、每任務成本 0.05 美元,但需要留意的是,該評測 600 個公開任務中有 480 個落在 H 公司收集訓練資料的範圍內;在剩下 120 個完全held-out 的任務上,Holo4 27B 的分數是 49.3%。

授權方面,Holo4 35B-A3B 採 Apache 2.0 授權,可自行架設商用;Holo4 27B 則是 CC BY-NC 4.0,商用需透過 H Models API。定價上,Holo4 27B 每百萬 token 輸入 0.40 美元、輸出 3.00 美元,Holo4 35B-A3B 為 0.30 美元與 2.00 美元。API 相容 OpenAI 格式,端點為 https://api.hcompany.ai/v1;Hugging Face 上提供 BF16、FP8、NVFP4 與 4-bit GGUF 等多種格式的權重,並附上 vLLM 與 llama.cpp 的本機推論說明,H 公司表示未來幾天內還會釋出用於加速推論的 DSpark drafter checkpoint。所有的執行軌跡也公開在 trajectories.hcompany.ai 與 Hugging Face 上。

⚠️ 長流程與資料重疊是兩個要留意的地方

Holo4 在短任務、單步操作上的表現已相當接近甚至超越其基礎模型,但在需要維持數百步、跨情境記憶的長流程任務(OSWorld 2.0)上,與 Opus 5.5 之間仍有明顯差距,只是比較時使用的 harness 與 effort 設定不同,無法直接等同視之。另外,AutomationBench 的整體分數有一部分建立在與訓練資料重疊的任務上,完全 held-out 子集的分數更能反映真實泛化能力。

🎯 實務啟示

對想打造跨桌面、網頁、行動裝置與內部 API 的自動化 agent 團隊而言,Holo4 提供了一個可直接自架的開源選項(35B-A3B 為 Apache 2.0),搭配文件完整的 vLLM/llama.cpp 部署流程;其 Agentic Task Factory 的驗證式任務生成流程,也可以作為自建可驗證 agent 訓練資料的參考範本。

🔗 來源
- 標題:H Company Releases Holo4: Open-Weight Computer-Use Models That Click, Code and Call Tools Across Desktop, Web, Android and APIs
- 作者/機構:Michal Sutter(MarkTechPost)
- 連結:https://www.marktechpost.com/2026/09/29/h-company-releases-holo4-open-weight-computer-use-models-that-click-code-and-call-tools-across-desktop-web-android-and-apis/

#ComputerUse #OpenWeights #AIAgents #HCompany #Holo4 #MachineLearning #OpenSource #MCP #VisionLanguageModel #AgenticAI
