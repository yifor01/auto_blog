---
title: 🗞️Jensen’s Return, ByteDance’s Agent Push, and MiniMax Under Scrutiny
source: Recode China AI
url: https://www.recodechinaai.com/p/jensens-return-bytedances-agent-push
model: claude-code/sonnet
generated_at: '2026-11-28T00:43:20.294048'
score: 57
---

📌 黃仁勳回任、字節代理人公測，MiniMax 捲入資料外洩風暴

TL;DR：本週中國 AI 圈三大事：黃仁勳重掌 Nvidia、字節跳動代理人小豆公測、MiniMax 遭蘋果下架並涉資料外洩。

這週的中國 AI 新聞，從晶片巨頭的人事變動，一路燒到聊天機器人對未成年人的內容爭議——三件看似不相關的事，其實都指向同一個主題：AI 從「回答問題」走向「代為行動」之後，責任邊界在哪裡。

🤔 黃仁勳回任 Nvidia，出口規則本身沒變

Nvidia 於 11 月 23 日恢復黃仁勳的 president、CEO 與董事會成員職位，公司表示美國高層官員提供的意見讓董事會相信此舉不構成國家安全風險，同時承諾持續配合政府調查。中國媒體的報導焦點集中在這次回任是否會影響中國取得輝達技術的管道，但無論是 Nvidia 的公告還是黃仁勳回任本身，都沒有改變現行的出口管制規則。

🧩 字節跳動把「個人代理人」推向公開測試

Doubao 於 11 月 24 日開放旗下個人代理人「小豆」（Xiaodou）邀請制公測。報導描述這是一個能持續追蹤工作進度、主動發出提醒，甚至能代表使用者打電話的助理。這把字節跳動推進到代理人業務更吃力的一端——一個好答案可以在螢幕上被直接檢查，但訂餐廳之類的外部行動，成敗取決於助理如何處理權限、時機拿捏與後續執行，公測結果會讓使用者直接評斷這些實務細節。同一週，阿里的 Qwen Go 也開放了免費的代打電話服務，應用場景包括餐廳預約、包裹查詢與協尋失物，同樣是把代理人推向需要「跟真人講電話」才能完成的任務。

⚠️ MiniMax 同時面臨下架與資料外洩兩條戰線

路透社報導，蘋果已在全球下架 MiniMax 旗下的 Talkie App，原因是有報告指控應用中的 AI 角色向未成年使用者傳送帶有性意味的訊息。另一條戰線上，有研究者向路透社指出，透過中介管道提出的機密請求，儘管存在保留限制，仍被不明人士存取。隨後 StreamLake 揭露，一項涉及 MiniMax 代管運算資源的路由設定錯誤，可能導致部分早期請求被存取或保留。

📊 本週新模型：編碼、翻譯、醫療、視覺生成全面開花

- 智譜發布 GLM-5.4，採用 Loop Transformer 架構，重複使用既有層數以加深處理；其「廣義編碼」訴求延伸到影片、遊戲、3D shader 與 CAD，並支援視覺輸入
- 螞蟻開源醫療模型家族 LingSante，包括 LingSante-3.1-air-VL——一個總參數 1240 億、啟用參數 55 億的多模態模型，結合醫學影像判讀、報告生成、搜尋與工具使用
- 騰訊混元發布第三代翻譯模型 Hy MT3，宣稱語言覆蓋從 38 種擴展到 102 種，並加強指令遵循、遊戲本地化與涉及圖片或 OCR 的翻譯
- 騰訊同時推出 Hy3D 3.6，強調更乾淨的網格表面、更清晰的結構與更精細的細節
- 騰訊混元發布 DFly2，是用於 Hy4 Flash 的推測解碼（speculative decoding）模型，宣稱在長上下文與代理人工作負載上最高可達 4.2 倍加速
- MAGI-2 加入影片生成賽局，宣布計劃開源權重（與是否能實際存取生成服務是分開的里程碑）

🧩 其他值得關注的動態

- 彭博報導華為預告下一代 AI 記憶體晶片，屬於其運算堆疊的另一環節，商用規格與量產規模仍待確認
- UBS 預測中國 AI 晶片到 2028 年可能拿下本土市場 88% 份額（SCMP），能否實現取決於產能、效能與軟體採用情況
- DeepSeek App 新增用量／費用檢視介面，目前僅是可視化，尚未確認是否伴隨新的收費機制
- 騰訊元寶與倫敦國王學院（King's College London）合作推出一個以約 8 萬則群聊訊息建構的代理人記憶 benchmark，測試代理人能否從涉及多方的長對話中找回相關上下文

🎯 給工程師的實務啟示

本週訊號顯示，中國的代理人產品正從「回答問題」轉往「代為執行外部行動」，權限管理與後續執行會是這類產品接下來最該被檢視的環節。MiniMax 事件也提醒開發者：若服務牽涉第三方代管運算資源（如 StreamLake 代管 MiniMax 的容量），路由設定錯誤可能直接造成請求外洩，在合作前確認供應鏈透明度是必要功課。

🔗 來源
- 標題：🗞️Jensen's Return, ByteDance's Agent Push, and MiniMax Under Scrutiny
- 作者／機構：Tony Peng（Recode China AI）
- 連結：https://www.recodechinaai.com/p/jensens-return-bytedances-agent-push

#ChinaAI #Nvidia #ByteDance #MiniMax #GLM #Tencent #AIAgents #LLM #AIPolicy #JensenHuang
