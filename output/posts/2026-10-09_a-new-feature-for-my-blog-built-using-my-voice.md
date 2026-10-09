---
title: A new feature for my blog, built using my voice
source: Simon Willison
url: https://simonwillison.net/2026/Oct/9/built-using-my-voice/
model: claude-code/sonnet
generated_at: '2026-10-09T22:05:29.801221'
score: 66
---

📌 邊做菜邊用語音開發部落格功能

TL;DR：Simon Willison用ChatGPT語音模式邊煮飯邊開發部落格新功能，證明語音也能寫出完整程式碼。

你能邊炒菜邊寫程式嗎？Simon Willison說可以，只要把鍵盤暫時換成嘴巴。

🤔 **想幫部落格加一個Newsletters索引頁**

Simon Willison想在自己的部落格上新增一個Newsletters頁面，把他每週發送的免費Substack電子報，以及每月限贊助者閱讀的更新，整合成一個時間順序的索引。這本是個不複雜的Django功能，但他決定幾乎全程只靠語音完成。

🧩 **用ChatGPT語音模式，邊做飯邊開發**

他使用ChatGPT桌面應用程式中的Codex分頁，開啟語音對話模式，連接到本機的開發環境（simonwillisonblog checkout）。流程大致如下：
1. 先用鍵盤輸入「Start dev server and open in browser」，啟動本機開發伺服器並在瀏覽器開啟預覽，方便之後用視覺方式追蹤進度。
2. 點擊「Start new voice chat」按鈕（不是麥克風按鈕，而是它右邊那個），接著把筆電搬到廚房，邊煮飯邊對話。
3. 使用的模型是GPT-6 Astra High。他透過語音說明需求：這是一種新的內容類型，不該出現在標籤頁與部落格首頁，但應該出現在依日期瀏覽的歸檔頁面上；而且由於每月電子報含有獨家內容（不像Substack電子報只是其他文章的複本），一旦公開就必須可被搜尋。
4. 對話持續約半小時（正好是煮晚餐的時間），模型會適時提出澄清問題，再動手修改程式碼，包括新增一個model、一筆migration、view程式碼、templates，以及從外部來源匯入資料到資料庫的匯入函式。

到晚餐煮好時，功能幾乎完成，唯一卡住的地方是匯入機制：部分資料存放在私有的GitHub repository，Astra原本打算用在子程序中呼叫git的方式處理匯入，但Simon想改用API金鑰的方式，這就需要坐到鍵盤前建立新的API key。

💡 **半小時語音＋半小時鍵盤，收尾靠審查**

煮完飯後，他讓Codex建立分支並開啟pull request，在GitHub的PR介面審查程式碼。審查後他改回用鍵盤輸入，把原本用git子程序處理的匯入腳本換成API呼叫，並微調了幾處公開頁面的顯示細節——這部分額外花了約半小時以文字提示溝通，才正式將PR合併並部署上線。最終成果是一個把每週Substack電子報與每月贊助者電子報依時間反序混合呈現的索引頁，下方還附有按年份分類的歸檔連結。頁面版型由GPT-6 Astra設計，並根據他隔著廚房看預覽後給出的語音回饋即時調整。

他也坦言這種語音開發方式不會變成他的日常工作模式。相較於過去遛狗時用手機語音模式做研究或腦力激盪，這次因為多了即時視覺預覽、又能隨時切換回鍵盤輸入貼上錯誤訊息或精確指出要改的程式碼片段，整體互動效率明顯更高。對他來說，最大的價值是能夠「一邊做菜一邊真正把東西做出來」，取代平常邊做菜邊看podcast或TikTok的習慣。

⚠️ **細節層級的工作，語音還是比不上打字**

他也明確指出，一旦進入細節層面——像是貼上範例、錯誤訊息，或直接標出要修改的程式碼——用文字溝通仍然比用語言描述更有效率；而且這種對著電腦說話的工作方式，也只適合在家這種不會打擾他人的環境進行。

🎯 **對工程師的實務啟示**

語音驅動的程式碼Agent（例如ChatGPT Codex的語音模式），在你已經清楚知道想做什麼、而雙手正忙著其他事情的場景下，可以是一個實用的輔助工具，尤其搭配即時視覺預覽效果更好；但進入除錯、貼錯誤訊息或精確指定修改範圍的階段，切回鍵盤輸入仍是更有效率的選擇。混合語音與鍵盤的工作流，可能比單純依賴其中一種更實際。

🔗 **來源**
- 標題：A new feature for my blog, built using my voice
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Oct/9/built-using-my-voice/

#AICoding #VoiceInterface #ChatGPT #Codex #Django #DeveloperWorkflow #LLM #AIAssistedDevelopment #OpenAI #CodingAgent
