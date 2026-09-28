---
title: 'Holo4: powering generalist computer-use agents'
source: HuggingFace Blog
url: https://huggingface.co/blog/Hcompany/holo4
model: claude-code/sonnet
generated_at: '2026-09-28T22:40:33.834391'
score: 98
---

📌 Holo4:一個模型,通吃 GUI、程式碼與 API 的 Agent

TL;DR:Hcompany 發布 Holo4,27B 密集模型與 35B-A3B MoE 兩種尺寸,同一顆模型可以操作 GUI、寫程式、也能呼叫 MCP 與 API。

多數 agentic 模型只精通一種介面:只認 GUI 的模型沒有畫面就等於瞎了,只會 tool calling 的模型碰上沒有 API 的應用程式就卡住。但真實世界的業務任務往往不是這樣切割的,同一個任務常常得混用好幾種操作方式才能完成。

🤔 **介面孤島,是通用 agent 的老問題**

這正是 Hcompany 想解決的問題:讓一個模型不需要因為換了平臺就得換掉,而是用同一種呼叫方式,在桌面、網頁、Android、程式碼沙箱,以及對業務 API 之間自由切換。

🧩 **兩種尺寸,一套訓練方法**

Holo4 系列有兩個規格:27B 密集模型與 35B-A3B 的 Mixture of Experts 模型,兩者皆已上架 H Models API,另外也同步推出更新版的 Holotron4 Nano。模型建立在 Qwen 系列作為 base model 之上,透過監督式學習與強化學習,在大量環境與任務上訓練而成,其中一部分任務來自 Hcompany 內部的 Agentic Task Factory。

這套 Task Factory 只憑文件——例如真實網站的截圖,或是開源軟體——就能自動建構互動式環境與可驗證任務,目前已產生約一萬個任務,涵蓋網頁應用、MCP 伺服器與桌面環境,其中還包含同時透過 GUI 與 MCP 暴露相同狀態的混合環境。訓練過程中團隊也重建了執行模型動作、管理數百步驟 context 的 harness,做法是利用 agent 在 OSWorld 2.0 上的實際表現當回饋:agent 會標註每個任務失敗的原因,再由工程師檢視並修正。文中提到,最大幅度的改進來自兩點——給 agent 一個能追蹤數百步的可靠記憶機制,以及讓它能直接在桌面機器上開一個 shell。

📊 **成績遜於最強 closed model,但成本低得多**

在 OSWorld 2.0 這個桌面控制 benchmark 上,Holo4 27B 拿下 61.7% 分數,相較之下 Opus 5.5 拿到 81.8%;Holo4 35B-A3B 則是 30.9%。Hcompany 強調,Holo4 是用少了好幾個數量級的參數量、以更低成本達到這樣的分數,而且開源了每一筆 benchmark 背後的完整 trajectory,可以在 trajectories.hcompany.ai 上逐步重播,或直接從 Hugging Face 下載。文章也用三個實測範例對比 Holo4 27B 與其 base model Qwen3.8 27B 在同一 prompt、同一 harness 下的表現,包括用 FreeCAD 建艾菲爾鐵塔模型(Holo4 用 84 次呼叫、130 萬 token,Qwen3.8 27B 用 60 次呼叫、100 萬 token)、建 H 公司 logo,以及用 Godot 做一個全自動運行、靠內建啟發式規則自駕的小精靈遊戲。

⚠️ **距離頂尖 closed model 仍有明顯差距**

在 OSWorld 2.0 上,Holo4 27B 落後 Opus 5.5 達 20 個百分點,35B-A3B 版本則落後更多,說明在最長、最複雜的工作流程上,Holo4 目前仍只能算是追趕者而非領先者。

🎯 **實務啟示**

如果你要做的 computer-use agent 需要同時橫跨 GUI 操作與 API 呼叫,又不想為每種介面各自維護一套模型,Holo4 提供了一個開源、可自行部署且成本可控的選項;加上完整開源的 trajectory 資料,對於想理解 agent 決策過程、或拿來做除錯與再訓練的工程團隊,是值得實測的起點。

🔗 **來源**
- 標題:Holo4: powering generalist computer-use agents
- 作者／機構:Hcompany(HuggingFace Blog)
- 連結:https://huggingface.co/blog/Hcompany/holo4

#Holo4 #ComputerUseAgent #Hcompany #OpenSourceAI #MoE #OSWorld #MCP #AgenticAI #HuggingFace #LLM
