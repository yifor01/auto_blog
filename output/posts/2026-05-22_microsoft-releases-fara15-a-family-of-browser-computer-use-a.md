---
title: "Microsoft Releases Fara1.5: A Family of Browser Computer-Use Agents (4B/9B/27B) That Outperform OpenAI Operator and Gemini 2.5 Computer Use on Online-Mind2Web"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/22/microsoft-releases-fara1-5-a-family-of-browser-computer-use-agents-4b-9b-27b-that-outperform-openai-operator-and-gemini-2-5-computer-use-on-online-mind2web/
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-22T20:52:53.476305
---

📌 【Microsoft AI Frontiers】Fara1.5 超越 OpenAI Operator 與 Gemini 2.5，瀏覽器代理新里程碑  

你以為目前最強的網頁自動化代理已是 OpenAI 的 Operator？最新顯示，Microsoft 研究團隊的 Fara1.5 系列在同一基準上竟領先近 15 個百分點。這到底是怎麼做到的？  

🤔 **瀏覽器代理的競爭白熱化**  
近年來，以「像人類一樣操作瀏覽器」的 Computer‑Use Agent（CUA）成為熱點。OpenAI 的 Operator 與 Google 的 Gemini 2.5 Computer Use 已被視為該領域的領先產品，它們透過讀取畫面截圖、滑鼠與鍵盤動作來完成線上任務。隨著這類代理被納入產品，開發者開始關注它們在真實網站上的實際成功率。  

🧪 **在 Online‑Mind2Web 基準上的頭對頭評測**  
Microsoft Research 的 AI Frontiers 實驗室針對同一個公開基準——Online‑Mind2Web 進行評測。該基準涵蓋 300 項跨 136 個熱門網站的任務，衡量代理在真實瀏覽器環境中完成目標的成功率。評測中，研究團隊測試了 Fara1.5 家族的三個規模（4B、9B、27B），並將結果與 OpenAI Operator、Gemini 2.5 Computer Use、以及 Youtori 的 Navigator n1 進行直接比較。所有模型皆使用相同的觀察‑思考‑行動循環，並在每一步僅參考最近三張瀏覽器截圖與對話歷史。  

🚀 **Fara1.5‑27B 在任務成功率上達到 72%**  
- Fara1.5‑27B：72%  
- OpenAI Operator：58.3%  
- Gemini 2.5 Computer Use：57.3%  
- Youtori Navigator n1：64.7%  
- Fara1.5‑9B：63.4%  
- 前代 Fara‑7B：34.1%  

這意味著 Fara1.5‑27B 比目前公開的領先代理高出約 13‑14 個百分點，且其 9B 版本也已超越 Youtori 的幾乎所有結果。相較於前代 Fara‑7B，成功率幾乎翻倍，顯示出模型規模與訓練資料混合帶來的顯著提升。  

💡 **觀察‑思考‑行動循環與 meta‑action 的設計**  
Fara1.5 採用「觀察‑思考‑行動」的循環：每一步模型會接收先前的對話歷史與最近三張瀏覽器截圖，輸出一段思考文字與單一的下一步動作。動作空間包含常見滑鼠、鍵盤輸入，以及網頁專屬的動作（例如網頁搜尋）。此外，該架構還提供兩種 meta‑action：  
1. 記錄事實以供後續使用  
2. 在需要時向使用者澄清問題  

這些 meta‑action 使代理能在較長的任務鏈中保持上下文，並與使用者協作，從而在多步驟的網頁操作中減少錯誤累積。  

🔬 **訓練資料與損失函數的細節**  
模型經過監督微調，訓練樣本約為兩百萬條。資料組成如下：  
- 60% 真實網頁軌跡  
- 12.8% 合成環境（由 FaraGen1.5 管線產出）  
- 12.5% 表單填寫與使用者互動  
- 8.8% 基礎定位（grounding）  
- 4.9% 視覺問答（VQA）  
- 剩餘比例涵蓋 GUI 拖曳、指令跟隨與安全相關樣本  

值得注意的是，損失僅作用於每條軌跡的最近三個時間步，這樣的設計鼓勵模型專注於短程依賴，同時透過 meta‑action 跨越更長的決策 horiz​on。  

⚠️ **研究限制**  
- 基準評測僅衡量單次任務的成功率，長期穩定性與實際產品中的交互頻率未在此報告中探討。  
- 模型仍依賴 Qwen3.5 的基礎檢查點，創新主要在訓練混合與迴圈設計，而非全新架構。  
- 未提供開放原始碼或易於部署的工具箱，限制了社群立即複製與擴展的可能。  

🎯 **對開發者與研究者的啟示**  
1. 在瀏覽器代理領域，資料組合（真實軌跡 + 合成環境）與細粒度損失函數（僅近三步）能顯著提升泛化能力。  
2. 加入能記憶事實與主動提問的 meta‑action，是處理多步驟、需要上下文的網頁任務的有效途徑。  
3. 雖然模型規模提升帶來明顯表現改善，但未來工作仍需著重於長期穩定性、安全防護與實際開發套件的提供，才能將研究結果轉化為產業級解決方案。  

🔗 **論文連結**  
📝 Microsoft Releases Fara1.5: A Family of Browser Computer-Use Agents (4B/9B/27B) That Outperform OpenAI Operator and Gemini 2.5 Computer Use on Online-Mind2Web  
👤 Asif Razzaq（報導）  
🔗 https://www.marktechpost.com/2026/05/22/microsoft-releases-fara1-5-a-family-of-browser-computer-use-agents-4b-9b-27b-that-outperform-openai-operator-and-gemini-2-5-computer-use-on-online-mind2web/  

你對這種「觀察‑思考‑行動」加 meta‑action 的設計有什麼看法？歡迎在留言區分享你的經驗或疑問 👇  

#AI #BrowserAgent #ComputerUse #MicrosoftResearch #Fara1.5 #OpenAI #Gemini #AgenticAI #網頁自動化 #TechTrends
