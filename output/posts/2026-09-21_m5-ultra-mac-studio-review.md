---
title: M5 Ultra Mac Studio Review
source: Hacker News
url: https://www.macstories.net/stories/m5-ultra-mac-studio-review-the-dream-mac-for-local-ai-agents/
model: claude-code/sonnet
generated_at: '2026-09-21T21:17:58.373169'
score: 85
---

📌 M5 Ultra Mac Studio實測:本地AI Agent的夢幻機器誕生了

TL;DR:256GB統一記憶體加上1.2TB/s頻寬,讓本地大模型跑agentic迴圈的體驗大幅提升。

雲端前沿模型更強、往往也更快,那為什麼還要折騰本地部署?MacStories作者用四天時間實測搭載256GB記憶體的M5 Ultra Mac Studio後給出了自己的答案:這臺機器徹底改變了他對本地模型能做什麼的想像。

🤔 為什麼要跑本地AI

作者坦言,買這臺機器的錢,拿去訂閱最貴的Anthropic方案好幾年可能都還划算,而且雲端模型效能更好。但對他而言,理由是隱私、成本,以及單純「這很酷」的動機混合。他分享了一個具體案例:今年夏天為撰寫iOS/iPadOS 27評測文章,他打造了一個叫Desk的內部應用程式,用一組基於DeepSeek V4 Flash(PDF處理另搭配olmOCR)的agent團隊,7天24小時運作了99天,處理310份文件,任務包括轉錄WWDC session、從剪存網頁與PDF指南中萃取功能點、跨來源交叉比對、從截圖萃取功能與bug,以及透過Notion API整理資料庫。作者提到,若靠OpenAI或Anthropic的API來做這種持續性背景任務,成本會高到難以負擔,因此轉向本地方案,最終總成本是0美元。

🧩 硬體規格:UltraFusion四晶粒架構

M5 Ultra外觀與前代M3 Ultra相同,但內部改用UltraFusion技術,將兩顆雙晶粒的M5 Max晶片連接成四晶粒架構,是Apple生態系首見。GPU方面,新一代80核心GPU每核心配備Neural Accelerator,相較M3 Ultra峰值AI運算效能最高提升4.5倍。記憶體方面,統一記憶體架構上限仍是512GB(該版本要到10月底才推出),但頻寬從819GB/s提升到1.2TB/s,較M3 Ultra提高50%。

📊 prompt處理與生成速度雙雙躍進

作者將M5 Ultra與擁有512GB記憶體的M3 Ultra,以及自己搭載RTX 5090的遊戲主機進行對比。結論是:M5 Ultra處理prompt(即token prefill)所需等待時間明顯縮短,開始生成回應後,文字輸出速度也比M3 Ultra快上不少。作者也提到,RTX 5090憑藉更高的記憶體頻寬,在效能上仍略勝一籌,但考量到自建PC的體積、發熱與噪音,他仍更傾向選擇M5 Ultra Mac Studio。

💡 從個人助理到Codex子agent

得益於更快的GPU與更高頻寬,作者目前將Qwen3.8-Flash-Next模型設為Open Minis for iOS與Hermes Agent這兩個個人助理應用的預設模型,使用頻率甚至超過Siri AI。他也開始在Mac上的Codex應用中使用本地模型,無論是作為主執行緒,還是由GPT-6 Astra調度的子agent,體驗都相當不錯。他特別提到,更快的prefill與生成速度讓這些agent在context視窗變大、進行長時間多輪對話迴圈時,不會隨著session拉長而明顯變慢。

⚠️ 不是給所有人的方案

作者坦言自己並非專業AI開發者,不做模型訓練或微調,純粹是長期把玩本地AI模型的愛好者。他也提醒,操作這類本地模型設定相當繁瑣(fiddly),並不適合只想花20美元用Claude Cowork就打發需求的使用者,這套做法目前仍屬於AI工作流程的前沿嘗試。

🎯 實務啟示

對於需要長時間、高頻率呼叫模型的背景任務(例如持續性資料整理、agent常駐迴圈),本地部署在成本上可能遠比雲端API划算,M5 Ultra這類統一記憶體頻寬大幅提升的機器,讓這件事在效能上變得可行。但這條路線目前仍需要一定的動手能力與硬體投入門檻,並非開箱即用的方案。

🔗 來源
- 標題:M5 Ultra Mac Studio Review
- 連結:https://www.macstories.net/stories/m5-ultra-mac-studio-review-the-dream-mac-for-local-ai-agents/

#MacStudio #LocalAI #AppleSilicon #MLX #AIAgent #M5Ultra #UnifiedMemory #EdgeAI #OnDeviceAI #LLM
