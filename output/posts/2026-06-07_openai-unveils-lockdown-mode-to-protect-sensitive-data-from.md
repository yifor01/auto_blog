---
title: OpenAI unveils Lockdown Mode to protect sensitive data from prompt injection
  attacks
source: TechCrunch AI
url: https://techcrunch.com/2026/06/06/openai-unveils-lockdown-mode-to-protect-sensitive-data-from-prompt-injection-attacks/
score: 73
model: google/gemma-4-31b-it:free
generated_at: '2026-06-07T19:36:34.168750'
---

📌 【OpenAI 最新安全更新】面對 Prompt Injection 攻擊，新推出的 Lockdown Mode 能提供多少保護？

當我們將 AI 整合進工作流，讓它讀取網頁或分析文件時，一個潛在的風險始終存在：Prompt Injection（提示詞注入）。攻擊者只需在網頁中隱藏一段惡意指令，就能在 AI 讀取該頁面時，悄悄誘導 AI 洩漏使用者的敏感資料或改變回應行為。

🤔 **便利性與安全性的權衡：AI 讀得越多，風險越高**

目前的 LLM 應用趨勢是賦予 AI 更多權限，例如即時瀏覽網頁、執行深度研究 (Deep Research) 或以 Agent 模式自動化操作。然而，這種「連結外部世界」的能力，也為 Prompt Injection 開啟了大門。當 AI 讀取包含惡意指令的第三方內容時，它可能會將這些指令誤認為是系統指令而執行，導致數據外洩 (Data Exfiltration) 的風險增加。

🧪 **Lockdown Mode 的設計邏輯：透過「切斷路徑」降低風險**

為了保護處理敏感資料的使用者，OpenAI 推出的「Lockdown Mode」採取了一種極端但有效的防禦策略：**直接禁用高風險的外部互動功能**。

開啟 Lockdown Mode 後，ChatGPT 將會：
- **禁用即時網頁瀏覽**：僅能存取快取內容 (Cached content)，防止即時讀取惡意網頁。
- **禁用從網頁檢索與顯示圖片**：雖然仍可生成圖片，但不再從網頁抓取外部圖片。
- **禁用深度研究 (Deep Research) 與 Agent 模式**：移除最容易被利用於複雜攻擊的自動化路徑。

💡 **這不是萬能藥，而是「風險降低」策略**

值得注意的是，OpenAI 坦承 Lockdown Mode 並不能完全杜絕所有注入攻擊。即使在鎖定模式下，如果惡意指令存在於「快取內容」或「上傳的文件」中，依然有可能影響 AI 的行為或回應準確性。

這項功能的定位並非為所有使用者設計，而是針對那些處理高度敏感資料、且對數據外洩風險有嚴格要求的人員或企業組織。

⚠️ **防禦層級的侷限：快取與上傳文件仍是漏洞**

該模式的主要防護在於「減少攻擊面」，但它無法解決 LLM 核心的根本問題：AI 難以完全區分「系統指令」與「外部數據」。因此，即便開啟 Lockdown Mode，上傳的文件內容依然是潛在的攻擊向量。

🎯 **實務建議：根據資料敏感度選擇模式**

對於開發者與企業安全負責人，建議採取分級防護策略：
- **一般任務**：使用標準模式以獲取最強大的即時資訊與 Agent 能力。
- **處理敏感資料**：強制開啟 Lockdown Mode，犧牲即時性以換取較高的安全性。
- **最高安全等級**：在 Lockdown Mode 基礎上，對所有上傳文件進行預審，並意識到即便在鎖定模式下，AI 的回應仍可能受污染。

🔗 **資訊來源**
📝 OpenAI unveils Lockdown Mode to protect sensitive data from prompt injection attacks
👤 Anthony Ha @ TechCrunch
🔗 連結：https://techcrunch.com/2026/06/06/openai-unveils-lockdown-mode-to-protect-sensitive-data-from-prompt-injection-attacks/

目前此功能正逐步推送至 ChatGPT Business 帳戶及部分符合條件的個人帳戶。你在公司內部部署 AI 時，是如何處理 Prompt Injection 風險的？歡迎在下方分享你的防護經驗 👇

#OpenAI #ChatGPT #CyberSecurity #PromptInjection #資訊安全 #LLMSecurity #數據隱私
