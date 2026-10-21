---
title: While Amazon blocks AI agents, Walmart rolls out the welcome mat
source: TechCrunch AI
url: https://techcrunch.com/2026/10/21/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat/
model: claude-code/sonnet
generated_at: '2026-10-21T21:02:35.012041'
score: 86
---

📌 Amazon 擋 AI 代理下單，Walmart 反而開門迎接

TL;DR：Walmart 推出 Agent Gateway 與消費授權機制，讓 AI 代理也能合規購物。

同一週，兩大零售巨頭對 AI agent 做出了完全相反的選擇：Amazon 開始封鎖 AI 代理代客下單，Walmart 卻宣布全面開放。

🤔 當 AI 代理開始幫你買東西，零售商各自選邊站

根據 TechCrunch 報導，Walmart 在週三宣布推出自家的 Agent Gateway，用來管理交易與其他面向 AI agent 使用者的新功能。這個時間點值得注意：報導指出，Walmart 最大的競爭對手 Amazon 近期才開始封鎖代表線上購物者下單的 AI agent，多個旅遊與訂房網站也選擇把 AI agent 完全擋在門外，以應對消費者端 AI agent 使用量的上升。相比之下，Walmart 早已與 Meta 的 Muse 建立合作關係，並提供與 ChatGPT、Gemini 等熱門 AI 應用的整合，這次等於是把既有佈局再往前推一步。Walmart 總裁兼 CEO John Furner 在舊金山的 Masters of Scale Summit 上表示，公司正在為 AI agent 成為主流的世界做準備。

🧩 Agent Gateway：用 MCP 把 Walmart 的庫存開給 AI agent

這套新技術支援 Walmart 與旗下折扣會員倉儲 Sam's Club 的 agentic 購物。核心是 Walmart 新的 MCP(Model Context Protocol)伺服器 Agent Gateway，用來讓經核准的 agent 透過 MCP 協定連接 Walmart——這個協定最初由 Anthropic 提出，讓 AI agent 能連接外部資料來源、工具與工作流程。在這個情境下，它讓 AI agent 可以搜尋 Walmart 的線上庫存，並代表使用者完成購買。報導特別指出，Agent Gateway 能在不需要使用者把個人資訊或購物紀錄直接分享給 agent 的前提下，協助顧客採購慣用的品牌或商品。

📊 用「授權使用者」的邏輯，區分 agent 和你自己的消費

Walmart 也開發了新技術，用來區分哪些購買是 agent 代為下單、哪些是顧客本人直接下單，並讓使用者對自己的 agent 能做什麼、不能做什麼擁有更細緻的控制。下個月上線的 Agent Profiles，會讓顧客為每一個使用的 AI agent 建立專屬的帳戶設定檔，可以分開查看 agent 的購買紀錄；顧客可以選擇每筆交易都要求核准，或是設定一個消費額度上限,讓 agent 在額度內自行完成交易。Walmart 把這個機制類比為信用卡的「額外授權使用者」：對方的每筆交易都會被標記，而你可以設定消費上限。首次用某個 agent 透過 Agent Gateway 購物時，系統就會自動建立 Agent Profile，使用者再把它連結到自己的 Walmart 帳戶、設定控制條件；Agent Profile 也可以隨時刪除。這項支援對所有 Walmart 帳戶開放，不需要 Walmart+ 會員資格。

💡 退貨保障，是說服消費者「先試用」的關鍵條件

Walmart 同時為 AI agent 訂立專屬的「使用條款」，規範 agent 的運作方式與交易權限。報導特別點出一項對消費者友善的條件：即使 agent 的行為不如預期，Walmart 既有的退貨流程依然適用。這等於消除了消費者對「agent 亂買東西怎麼辦」的最大顧慮，可能是推動消費者願意早期嘗試 agentic commerce 的關鍵。條款也規定，agent 不能做出超出購物者意圖的行為、不能存取顧客的付款資訊，且只能存取完成任務所需的最小必要資訊；不遵守條款的 agent 會被封鎖，無法再存取 Walmart 網站。

⚠️ 開放是有條件的，不合規就被擋

值得留意的是，Walmart 的開放並非無限制：agent 必須經過核准、遵守專屬條款，才能持續存取平臺;一旦違規即被封鎖。這其實和 Amazon 的封鎖策略只是程度之差，而不是方向上的根本不同——兩者都在建立對 AI agent 行為的控管機制，只是 Walmart 選擇以「開放＋授權管理」取代「一刀切封鎖」。

🎯 實務啟示

如果你正在開發或整合購物類的 AI agent，Walmart 的 Agent Gateway 釋出了一個明確訊號：MCP 已經成為零售商與 agent 對接的實際協定選擇之一，而「消費額度授權」與「交易來源標記」會是agent商務必須具備的基礎設計,值得在自家 agent 的架構裡預先規劃對應的授權與稽核機制。

🔗 來源
- 標題：While Amazon blocks AI agents, Walmart rolls out the welcome mat
- 作者／機構：Sarah Perez, TechCrunch AI
- 連結：https://techcrunch.com/2026/10/21/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat/

#AgenticCommerce #Walmart #Amazon #MCP #ModelContextProtocol #AIAgent #Ecommerce #Anthropic #RetailTech #AIShopping
