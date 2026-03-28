---
title: "benjitaylor/agentation"
source: GitHub Trending
url: https://github.com/benjitaylor/agentation
score: 91
model: gpt-4o-free
generated_at: 2026-03-28T18:59:15.276460
---

📌 【Agentation】讓你的 AI Coding Agent 準確理解「藍色按鈕在哪裡」！

你是否曾經為了讓 AI Coding Agent 理解「那個藍色按鈕」是哪一個，而發現自己需要寫一大段描述？現在，一個名為 **Agentation** 的新工具，或許可以解決這個問題。

🎣 **用 AI 寫程式更快，但溝通成本仍居高不下**

隨著 AI Coding Agents（如 GitHub Copilot、Cursor 等工具）的普及，開發者的產出效率顯著提升。然而，與 AI 溝通界面細節時，仍然是一個令人頭痛的問題。例如：「修改側邊欄裡的藍色按鈕」，這樣的描述對人類來說很直觀，卻可能讓 AI 無所適從。

這時候，你需要一個能幫助 AI 精確定位的工具——Agentation。

🧪 **Agentation 是什麼？**

Agentation 是一款專為開發者設計的「**無代理限制 (agent-agnostic)** 視覺反饋工具」，可以幫助你快速點選頁面上的元素、添加註解，並自動生成結構化輸出，告訴 AI Coding Agent 你指的到底是哪段代碼。

以下是它的核心功能：
- **點擊標註**：點擊任何頁面元素，Agentation 能自動識別選擇器。
- **文字選取與多選功能**：可以選取文字或拖曳框選多個元素。
- **區域選取**：即使是空白區域，也能拖曳標註。
- **動畫暫停**：暫停所有動畫（CSS、JS、影片），幫助你捕捉指定畫面。
- **結構化輸出**：自動生成 Markdown，包含選擇器、位置與上下文的詳細描述。
- **輕量化設計**：純 CSS 動畫，無需任何運行時庫。
- **深色/淺色模式**：根據使用者偏好自動調整，也可手動設置。

🤔 **如何使用 Agentation？**

1. 使用 npm 安裝：`npm install agentation -D`
2. 在你的 React 項目中導入 Agentation：
   ```javascript
   import { Agentation } from 'agentation';

   function App() {
       return (
           <>
               <YourApp />
               <Agentation />
           </>
       );
   }
   ```
3. 啟動應用時，一個工具欄會出現在右下角。點擊啟用，然後點擊任何元素即可開始進行標註。

💡 **從「描述外觀」到「精確定位」：讓 AI 理解得更好**

傳統上，開發者需要花大量時間用語言描述界面元素的外觀，例如「改變位於右側的藍色按鈕的大小」。透過 Agentation，你可以直接點擊該按鈕，並生成 `.sidebar > button.primary` 等選擇器，還包括元素的位置和上下文。這種結構化輸出能讓 AI Coding Agents 精確定位，避免模糊描述帶來的反覆溝通問題。

⚠️ **目前的限制**

- 僅支援 React 18+ 的應用程式。
- 只適用於桌面瀏覽器，尚未支援行動裝置。
- 這是一款視覺化工具，但對於無 UI 的後端系統並不適用。

🎯 **AI 驅動開發流程的必備工具**

Agentation 的價值在於提高開發效率，特別是在與 AI Coding Agent 協作的場景下。對於前端開發者來說，這是一個能顯著降低溝通成本的實用工具。

🔗 **工具連結**
📂 GitHub Repository: [benjitaylor/agentation](https://github.com/benjitaylor/agentation)  
📜 License: PolyForm Shield 1.0.0  
📖 Documentation: [agentation.com](https://agentation.com)

你是否覺得這樣的工具能改變你的開發流程？歡迎分享你的看法 👇

#AI #CodingTools #FrontendDevelopment #Agentation #GitHubTrending #React
