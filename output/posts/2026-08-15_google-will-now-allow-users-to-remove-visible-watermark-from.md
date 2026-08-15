---
title: Google will now allow users to remove visible watermark from its AI generations
source: TechCrunch AI
url: https://techcrunch.com/2026/08/14/google-will-now-allow-users-to-remove-visible-watermark-from-its-ai-generations/
model: nvidia/nemotron-3-ultra-550b-a55b:free
generated_at: '2026-08-15T06:31:22.652265'
score: 50
---

📌 Google 開放關閉 AI 可見浮水印，SynthID 隱形標記與 C2PA 元數據保留

TL;DR：Google 讓使用者自行決定是否顯示可見浮水印，但不可見的 SynthID 與 C2PA 元數據持續追蹤 AI 產出來源。

隨著 AI 生成內容滲透專業創作流程，可見浮水印常被視為干擾成品品質的阻礙。Google 選擇在「創作彈性」與「來源透明」之間劃出新界線：把可見標記交給使用者開關，把不可見標記留給系統驗證。

🧩 **三大模型同步支援，設定入口統一在媒體浮水印選項**

Gemini VP Josh Woodward 在 X 貼文確認，Nano Banana（圖像）、Omni（多模態）、Lyria（音樂）三款模型皆納入新政策。使用者可在 Gemini 應用與影片編輯器 Flow 的「設定 > 媒體浮水印」切換開關，Search 整合也將於近期跟進。這意味著從圖片、影片到音訊的完整生成鏈路，都能在發布前移除肉眼可見的標記。

🔒 **雙層隱形防線：SynthID 加 C2PA 元數據不受影響**

關閉可見浮水印不代表匿名。Google 強調不可見的 SynthID 水印與 C2PA 標準相關中繼資料將持續嵌入。Woodward 指出：「你仍可用 Gemini 或 Search 判斷圖片是否為 AI 生成。」這雙軌制設計讓專業創作者輸出乾淨成品，平臺與驗證工具仍保有溯源能力。

🛠️ **開源 Credentio 庫，讓開發者在本地端驗證來源**

同步釋出的 Credentio 程式庫，提供開發者在應用程式內嵌入本地驗證機制，無需仰賴雲端 API 即可檢測 SynthID 與 C2PA 標記。這為內容審核、版權管理、合規稽核等場景降低整合門檻，也呼應業界對「離線可驗證」的需求。

⚖️ **回應 EU 法規壓力，但走向與 Anthropic 不同**

Anthropic 近期為符合 EU 法規，在 Claude 產出的文字與檔案強制植入浮水印；Google 則採取「可見可關、隱形必留」的彈性策略。兩者同樣面對監管壓力，卻在使用者體驗與合規執行上呈現不同取捨。

🎯 **實務啟示**

對工程師與產品團隊：若你的應用涉及 AI 內容分發或審核，Credentio 提供現成的本地驗證元件，可優先評估整合；對創作者：可見浮水印開關上線後，發布前務必確認平臺政策與下游通路對隱形標記的讀取支援度，避免「以為乾淨實則可追蹤」的合規盲區。

🔗 **來源**
- 標題：Google will now allow users to remove visible watermark from its AI generations
- 作者／機構：Ivan Mehta @ TechCrunch
- 連結：https://techcrunch.com/2026/08/14/google-will-now-allow-users-to-remove-visible-watermark-from-its-ai-generations/

#Google #AI #Watermark #SynthID #C2PA #GenerativeAI #ContentAuthenticity #Credentio #Gemini #ResponsibleAI
