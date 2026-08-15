---
title: How Claude’s text watermark works
source: Anthropic News
url: https://www.anthropic.com/news/claude-text-watermark
model: nvidia/nemotron-3-ultra-550b-a55b:free
generated_at: '2026-08-15T06:13:34.384459'
pinned: true
---

📌 Anthropic 正式啟用 Claude 文本水印，回應 EU AI Act 合規需求

TL;DR：Anthropic 採用 Google DeepMind SynthID-Text 技術，在不影響輸出品質前提下，讓 Claude 產出可被檢測的水印文本。

🎣 **水印不等於看得見的浮水印**

提到「水印」，許多人聯想到鈔票上的隱形圖案或 PDF 右下角的半透明 Logo。但 Anthropic 這次在 Claude 植入的文本水印，對讀者完全不可見、不增加字元、不改變語意，甚至連「下一個 token 的機率分布」都維持原狀——它只換掉了「從機率分布中取樣時使用的隨機數來源」。

🤔 **為何現在推出？EU AI Act 硬性規定**

EU AI Act 自 8 月 2 日起生效，要求服務歐洲市場的 AI 提供者必須標記 AI 產出內容。Anthropic 與其他主要模型開發商已簽署相同實務守則，紛紛推出各自水印方案。這不是單一廠商的產品功能，而是整個產業面臨的合規基準線。

🧩 **核心機制：把「擲骰子」換成「查圓周率」**

大語言模型逐 token 生成，每步都在候選詞表中按機率取樣。以「The weather today was cold and…」為例，下一個詞極不可能是「sugary」，卻可能是「overcast」或「grey」——對讀者來說語意幾乎相同，原本由隨機數決定選哪個。

水印的做法：保留候選集合與機率分布不變，改用 **金鑰 + 前幾個詞** 衍生的偽隨機序列來決定取樣。換句話說，模型仍在「合理的選項」中隨機挑選，只是這組隨機數現在帶有可驗證的統計模式。

Anthropic 採用的正是 Google DeepMind 2024 年發表於 Nature 的 **SynthID-Text** 方法，源頭可追溯至 Scott Aaronson 2022 年的提案。同族方法共享同一設計哲學：**只改變隨機數來源，不干涉模型原本的語言判斷**。

📊 **實測：品質、創意、可讀性零差異**

- 內部測試：水印版與非水印版在內容、創意程度、可讀性上無顯著差異。
- Google DeepMind 實驗：將水印模型部署至部分 Gemini 流量，比較用戶點讚/點踩比率，無統計學顯著差異。
- 人工並排評測：評分者無法分辨哪個回答帶水印。

Anthropic 用大富翁遊戲類比：玩家原本靠擲骰子決定步數，現在改用圓周率小數點後某隨機位置開始的數字序列。對玩家與遊戲結果毫無影響，但事後若知道圓周率數值，即可從移動序列反推該局是否使用了圓周率——這就是「統計水印」的本質。

⚠️ **四大實務限制，工程師必須知曉**

1. **短文本難判定**：水印依賴累積足夠多的「低風險選擇」，片段太短資訊量不足，信心度低。
2. **事實密集段落水印稀疏**：如「Isaac Newton's most famous work was called Principia **Mathematica**」，下一個詞幾乎只有唯一正解，模型無「同等品質的備選詞」可供水印運作。
3. **校對/編輯人類文本幾乎無水印**：Claude 僅微調標點與語法，絕大多數 token 來自人類，水印幾無著力點。
4. **程式碼輸出受限**：語法嚴格、識別字不可替換的情境（如 API 呼叫、關鍵字），同樣缺乏「同等好壞的選項」，水印自然不會介入。

💡 **水印只能回答「有多大機率是 Claude 寫的」，不能更多**

- 無法確認是否為人類撰寫。
- 無法識別其他 AI（不同金鑰、甚至不同水印演算法）。
- 不攜帶任何身分資訊，不可追溯至特定用戶、組織或對話。

🎯 **對工程師的實務啟示**

1. **合規優先**：若產品面向歐洲市場，水印將成為預設行為，無法關閉；規劃合規流程時請納入「AI 內容可檢測性」驗收項目。
2. **檢測門檻管理**：短文本、高事實密度、程式碼、人類文本潤飾——這四類場景水印信號微弱，**不可將「檢測不到水印」等同於「非 AI 產出」**。
3. **品質無虞**：Anthropic 實測與 Google 實證皆指向同一結論：水印不犧牲模型能力，既有提示詞工程、評測管線無需調整。
4. **跨廠商互通性低**：各家金鑰與演算法不同，若需建立統一檢測管線，須分別整合各廠商提供的驗證 API 或開源實作。

🔗 **來源**
- 標題：How Claude’s text watermark works
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/news/claude-text-watermark

#Anthropic #Claude #AIWatermark #SynthIDText #EUAIAct #LLM #GenerativeAI #Compliance #AITransparency #GoogleDeepMind
