---
title: ‘Zoomsday’ hack uncovered using fewer than 20 AI prompts
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/977909/zoom-vulnerability-ai-attack
model: claude-code/sonnet
generated_at: '2026-08-12T07:38:48.610177'
score: 79
---

📌 不到 20 次 AI 提示，就挖出能接管視訊會議裝置的 Zoom 漏洞

TL;DR：資安團隊用不到 20 次公開 AI 模型提示，找到能在無使用者操作下接管 Zoom 與會者裝置的零時差漏洞，Zoom 已完成修補。

過去要打造一個能實際運作的漏洞利用（exploit），向來被視為國家級單位才玩得起的遊戲：菁英團隊、數個月工時、政府等級的預算規範。這次，一家資安公司只花了一天。

🤔 **靠 Zoom 的畫線標註功能，就能在你不知情下拿下你的裝置**

根據 Wired 率先報導、A Security 公司在部落格公布的研究，其研究人員用不到 20 次公開可取得的 AI 模型提示，就找出 Zoom 的一個重大安全漏洞。這個漏洞出在 Zoom 的標註（annotation）功能——也就是使用者在螢幕分享時可以在畫面上畫線的那個功能。攻擊者只要加入或主持一場會議，就能利用這個漏洞，在與會者的裝置上執行惡意程式碼，進而竊取資料、開啟攝影機或麥克風、或安裝惡意軟體。根據 A Security 的說法，這個攻擊完全不需要受害者做任何操作，而且畫面上「沒有任何視覺線索顯示裝置已被入侵」。

💡 **AI 把「國家級門檻」的工作壓縮到一天**

A Security 的漏洞研究員 Idan Levcovich 在部落格中寫道：「針對它做出一個能實際運作的漏洞利用，向來是國家級單位的工作：菁英團隊、數個月的努力、政府等級規範的預算。而我們用一個 AI agent 和任何人都能取得的模型，一天內就做到了。」Zoom 已於週二發布修補，受影響範圍涵蓋 Windows、macOS、Linux、Android 與 iOS 全平臺。

⚠️ **技術細節仍是黑盒**

目前公開的報導並未揭露具體使用了哪些 AI 模型、提示內容為何，或漏洞利用鏈（exploit chain）的技術細節，因此外界暫時無法評估這套方法能否複製到其他應用程式，也難以判斷「不到 20 次提示」背後實際涉及多少人工分析與驗證工作。

🎯 **實務啟示**

這則新聞對工程團隊最直接的警訊，是螢幕分享、標註、遠端渲染這類「看似無害」的協作功能，正成為 AI 輔助漏洞研究鎖定的高價值攻擊面，且發現門檻正在快速下降。如果你的產品也有類似的即時渲染或畫面互動功能，值得主動排入紅隊測試範圍；同時，防守方同樣可以善用 AI agent 輔助程式碼審查與模糊測試（fuzzing），在攻擊者之前找到這類漏洞。

🔗 **來源**
- 標題：'Zoomsday' hack uncovered using fewer than 20 AI prompts
- 作者／機構：Emma Roth（The Verge）
- 連結：https://www.theverge.com/ai-artificial-intelligence/977909/zoom-vulnerability-ai-attack

#Zoomsday #ZoomSecurity #AIExploit #VulnerabilityResearch #CyberSecurity #ZeroDay #AIAgent #InfoSec #RedTeam #PatchTuesday
