---
title: "Microsoft Research Releases Webwright: A Terminal-Native Web Agent Framework That Scores 60.1% on Odysseys, Up from Base GPT-5.4’s 33.5%"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/24/microsoft-research-releases-webwright-a-terminal-native-web-agent-framework-that-scores-60-1-on-odysseys-up-from-base-gpt-5-4s-33-5/
score: 98
model: tencent/hy3-preview:free
generated_at: 2026-05-24T19:38:19.385092
---

📌 **Microsoft Research 釋出 Webwright：終端機原生網頁代理框架，Odysseys 分數從 33.5% 飆至 60.1%**

你以為網頁代理必須一步步點擊、滾動才能操作網頁？微軟研究團隊卻讓 AI 直接寫程式，效能竟提升近 80%——這到底是怎麼做到的？

🤔 **傳統網頁代理的瓶頸：動作一步一步，限制了模型的潛力**  
現有的網頁代理大多採用「動作一步一步」的設計：模型只能看到目前頁面的截圖或 DOM 文字，然後預測下一個點擊、按鍵或滾動。這種做法在語言模型推理能力有限時很合理，但隨著模型在編寫與除錯程式碼方面變得更強，這個固定的迴圈反而成了瓶頸——每次都要重新與瀏覽器互動，無法利用程式碼的可重複性與檢查性。

🧪 **終端機原生設計：讓 AI 寫 Playwright 程式碼，而不是直接操作瀏覽器**  
Microsoft Research 的 AI Frontiers 實驗室提出了一個全新的框架 **Webwright**，其核心思想是把瀏覽器當作「可啟動、可檢查、可捨棄」的工具，而非代理必須長期維護的狀態。具體運作方式如下：

- **終端機環境（Environment）**：提供一個本地 shell，代理在其中執行指令。  
- **Model Endpoint**：接收當前上下文（包括先前的腳本、日誌、螢幕截圖），返回一個「思考區塊」與一個 shell 指令。  
- **Runner**：約 150 行程式碼，負責把模型的指令送到環境執行，並收集輸出。  
- **所有中間產物（腳本、日誌、截圖、結果）** 都被保存在本地工作區，方便後續檢視與重用。  

代理不再直接點擊頁面，而是 **撰寫 Playwright 程式碼**（微軟開源的瀏覽器自動化庫），執行該腳本來控制 Chromium、Firefox 或 WebKit 瀏覽器，檢查日誌、修正腳本，如此迭代。整個框架僅約 1 KB，由三個部分組成：Runner (~150 行)、Model Endpoint (~550 行)、terminal Environment (~300 行)，沒有多代理協調或複雜的規劃階層——就是一個單一的代理迴圈。

🚀 **核心發現：Odysseys 基準分數從 33.5% 跳升至 60.1%**  
在 Odysseys 網頁代理評測基準上，基礎 GPT-5.4 模型單獨使用時的得分為 33.5%。採用 Webwright 終端機原生框架後，同樣的模型得分提升至 **60.1%**，提升幅度達到 **約 79%**。這表示代理不僅能完成更多任務，而且在任務完成度上有顯著改善。

💡 **為什麼終端機原生這樣有效？**  
- **與瀏覽器解耦**：代理不必維護狀態化的瀏覽器會話，瀏覽器被當作可隨時啟動與棄置的工具，降低了狀態同步的複雜度。  
- **程式碼即產物**：產出的不是一串難以重現的點擊序列，而是可讀、可修改、可共享的 Playwright 腳本，符合開發者撰寫 RPA 腳本的工作流程。  
- **可檢視與迭代**：所有腳本、日誌、截圖都留在工作區，工程師可以直接檢查失敗原因、調整腳本，而不需要重新從頭與瀏覽器互動。  
- **輕量且易於擴充**：框架本身程式碼極少，易於嵌入現有的 LLM 服務或自訂模型端點。

⚠️ **已知限制：僅在 Odysseys 基準上驗證，長期穩未知**  
- 目前的評測僅限於 Odysseys 基準，未見於其他網頁代理測試集或真實世界場景的表現。  
- 框架採用單一代理迴圈，未探索多代理協作或更高階的規劃機制，複雜多步驟任務的適用性有待進一步研究。  
- 所有實驗皆基於 GPT-5.4 作為底層模型，不同模型家族或更大規模模型的遷移效益尚未確認。  
- 由於框架仍屬早期開源版本，長期維護性與社區生態仍需觀察。

🎯 **實務啟示：程式碼化的網頁代理才是未來方向**  
- 對於需要重複或定期執行網頁自動化的工程師，直接讓 AI 撰寫並維護腳本，比每次重新點擊更具效率與可靠性。  
- 可透過版本控制（Git）管理由 AI 產出的 Playwright 腳本，實現代碼審閱、回滾與團隊共享。  
- 若貴團隊已在使用 Playwright 或類似自動化工具，Webwright 提供了一種「讓 AI 成為腳本編輯者」的新範式，值得在內部原型或實驗專案中試點。  

🔗 **參考資訊**  
📝 **文章**：Microsoft Research Releases Webwright: A Terminal-Native Web Agent Framework That Scores 60.1% on Odysseys, Up from Base GPT-5.4’s 33.5%  
👤 **作者**：Asif Razzaq（MarkTechPost）  
🔗 **連結**：https://www.marktechpost.com/2026/05/24/microsoft-research-releases-webwright-a-terminal-native-web-agent-framework-that-scores-60-1-on-odysseys-up-from-base-gpt-5-4s-33-5/  

你試過讓 AI 直接寫瀏覽器自動化腳本嗎？歡迎在留言區分享你的經驗或疑問 👇  

#AI #WebAgent #Playwright #MicrosoftResearch #Automation #LLM #Odysseys #開源工具 #技術趨勢
