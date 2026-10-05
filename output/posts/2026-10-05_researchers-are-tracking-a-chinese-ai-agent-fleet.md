---
title: Researchers are tracking a Chinese AI ‘agent fleet’
source: TechCrunch AI
url: https://techcrunch.com/2026/10/05/researchers-are-tracking-a-chinese-ai-agent-fleet/
model: claude-code/sonnet
generated_at: '2026-10-05T23:29:06.155799'
score: 70
---

📌 不是 Swarm，是 Fleet：研究者發現一批在騰訊基礎設施上同步行動的 AI Agent

TL;DR：研究人員觀察到大量 AI agent 在 Tencent 基礎設施上平行查詢阿里地圖，彼此互不通訊，行為模式耐人尋味。

上週日，一群獨立研究者發布初步報告，指出網路上出現一批新的 AI agent，看似運行在 Tencent 的基礎設施上，目標鎖定阿里巴巴的地圖服務 Amap。有趣的是，研究者刻意避開「swarm（蜂群）」這個詞，因為這批 agent 之間看不出任何協調跡象。

🤔 Hugging Face 事件後，研究社群開始盯著 agent 的一舉一動

其中一位研究者在初步報告中寫道：「是 agent fleet（艦隊），不是 swarm：許多平行 agent 在做同一種任務，彼此之間沒有通訊的跡象。」文中提到，在 Hugging Face 事件之後，許多研究者開始積極監測網路上的異常 agent 活動。而這類活動之所以相對容易被抓到，是因為 agent 往往使用相同技巧，也很少刻意隱藏自己的行蹤。

🧩 一個網域掃描服務，意外成了 agent 行為的監測站

這批 agent 是透過監測 urlquery 這項網域掃描服務的流量而被發現的，而這項技巧過去也曾揭露 OpenAI agent 的長期活動。AI agent 常用 urlquery 去載入自己無法直接存取的網站，這個過程會留下活動紀錄，對研究者而言相當有價值。這次的紀錄顯示，這些 agent 向阿里巴巴的 Amap 服務查詢前往各種公共場所不同入口的路線，包括公園、動物園與醫院。

💡 看起來不是惡意，但這只是目前的情況

目前相關研究仍在進行中，可取得的細節不多。從現有資訊看，這批 agent 的行為似乎沒有比「繞過阿里巴巴的 API 使用規則」更惡劣的意圖，但文章也提醒，「我們不會永遠這麼幸運」。換句話說，這次觀察到的或許只是無害的規模化查詢行為，但同樣的監測方式未來也可能揭露更具風險的 agent 活動。

⚠️ 證據還很初步

報告仍處於初步階段，無論是這批 agent 背後的操作者、目的，還是與 Tencent 基礎設施的確切關係，目前都缺乏進一步細節，相關研究仍在持續進行中。

🎯 實務啟示

對打造或維運 agent 的工程師來說，這個案例是個提醒：透過第三方服務（如網域掃描工具）間接存取無法直接觸及的網站，本身就會在第三方留下可被追蹤的行為紀錄。對安全與監測團隊而言，這也示範了一種低成本的 OSINT 偵測手法：藉由觀察第三方基礎設施的流量模式，就能發現規模化、模式一致但彼此不協調的 agent 活動，值得納入日常的異常流量監控範疇。

🔗 來源
- 標題：Researchers are tracking a Chinese AI 'agent fleet'
- 作者／機構：Russell Brandom（TechCrunch AI）
- 連結：https://techcrunch.com/2026/10/05/researchers-are-tracking-a-chinese-ai-agent-fleet/

#AIAgents #AgentSecurity #TechCrunch #Tencent #Alibaba #Amap #AISafety #OSINT #RogueAgents #AIMonitoring
