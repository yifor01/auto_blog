---
title: heygen-com/hyperframes
source: GitHub Trending
url: https://github.com/heygen-com/hyperframes
score: 94
model: google/gemma-4-31b-it:free
generated_at: '2026-07-13T08:55:22.046775'
---

📌 HyperFrames：用 HTML+CSS 直接產出確定性 MP4，讓 AI 代理也能寫影片

TL;DR：HyperFrames 讓開發者以純 HTML、CSS 與可定址動畫描述影片，透過 CLI 或 AI 代理即能產出 deterministic MP4，適合本地測試或作為雲端編輯服務的渲染核心。

🧩 **把網頁技術當成影片編輯器**

HyperFrames 是一套開源框架，核心概念是把 HTML、CSS、媒體檔案與「可定址」動畫（seekable animation）視為影片的描述語言，最終渲染成 MP4。這意味著開發者可以直接寫網頁標記，像寫網頁一樣規劃畫面、排版與過場，然後交給 HyperFrames 產出可播放的影片檔。

🤔 **為誰設計？**

- 想在本機使用 CLI 快速產出影片的前端開發者  
- 需要讓 AI 生成程式碼（Claude Code、Cursor、Gemini CLI、Codex 等）自動完成影片製作的代理程式  
- 想把影片渲染作為雲端創作平臺（例如低程式碼編輯器、教學系統）的核心引擎  

🧩 **核心工作流程與技能架構**

HyperFrames 以「skills」的形式提供給 AI 代理使用，主要步驟如下：

1. **安裝技能**：  
   ```bash
   npx skills add heygen-com/hyperframes --full-depth --yes
   ```  
   `--full-depth` 會完整克隆主分支，確保取得最新的 skill 檔案。

2. **描述影片**：在代理的指令或提示中使用 `/hyperframes`，例如  
   `Using /hyperframes, create a 10‑second product intro with a fade‑in title, a background video, and subtle background music.`  

3. **代理產生 HTML**：AI 代理根據需求產出符合規範的 HTML、CSS、媒體引用與動畫程式碼。  

4. **Lint & Preview**：框架內建檢查（lint）與即時預覽功能，確保輸出符合 MP4 渲染需求。  

5. **渲染 MP4**：最終以 CLI 或內嵌的渲染器產生 deterministic MP4，影片內容在每次渲染時保持一致。  

HyperFrames 內部有 20 種「skills」供代理按需載入，`/hyperframes` 本身是路由器與能力對映（capability map），會根據「make me a…」的請求自動選擇工作流（影片、簡報或組合畫面），並指向相應的子技能。

📊 **快速上手示範（CLI 版）**

1. **安裝**（完整深度）  
   ```bash
   npx skills add heygen-com/hyperframes --full-depth
   ```

2. **編寫簡易 HTML**（例）  
   ```html
   <html>
     <head>
       <style>
         @keyframes fadeIn { from {opacity:0;} to {opacity:1;} }
         h1 { animation: fadeIn 2s forwards; }
       </style>
     </head>
     <body>
       <video src="bg.mp4" autoplay muted loop></video>
       <h1>產品介紹</h1>
     </body>
   </html>
   ```

3. **渲染**  
   ```bash
   hyperframes render --input intro.html --output intro.mp4
   ```

完成後會得到一個 10 秒左右、標題淡入、背景影片與音樂同步的 MP4 檔案。

💡 **實務啟示**

- **開發者視角**：不需要學習專業的影片編輯軟體或指令碼語言，直接用熟悉的前端技術堆疊即可產出影片，降低了影片自動化的門檻。  
- **AI 代理整合**：把 HyperFrames 技能注入任何支援「skills」的程式碼生成代理，讓 AI 能完成從需求描述到最終影片的全流程，適合自動化報告、產品預告或教學影片的批次產出。  
- **確定性渲染**：因為渲染過程是 deterministic 的，同樣的 HTML 會得到相同的 MP4，對於需要版本控制或自動化測試的工作流非常友好。  

🔗 來源  
- 標題：heygen-com/hyperframes  
- 作者／機構：heygen-com  
- 連結：https://github.com/heygen-com/hyperframes  

#HyperFrames #HTMLToVideo #AIcodingAgent #CLI #DeterministicMP4 #OpenSource #VideoRendering #Frontend #Automation #Heygen  
