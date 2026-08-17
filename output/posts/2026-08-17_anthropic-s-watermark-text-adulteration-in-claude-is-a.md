---
title: Anthropic's 'Watermark' Text Adulteration in Claude Is a Perversion of Writing
source: Hacker News
url: https://daringfireball.net/2026/08/anthropics_watermark_text_adulteration_in_claude_is_a_perversion_of_writing
model: claude-code/sonnet
generated_at: '2026-08-17T06:16:40.831734'
score: 75
---

📌 Claude 文字浮水印，犧牲了什麼？

TL;DR：為了讓生成文字可被機率性偵測，Anthropic 選擇在 token 選字上動手腳，而非藏隱藏字元。

Anthropic 起初宣稱新的文字浮水印技術「不會改變文字的意義、品質或可讀性」。結果沒多久公布的技術細節顯示，它做的正是相反的事，透過操控每一個字詞的選擇機率來留下痕跡。

🤔 從「隱藏字元」的猜測，到「操控用字」的真相

本文作者（Daring Fireball）先前報導 Anthropic 宣布，所有 Claude 模型未來都會為輸出內容（包含文字）加上「浮水印」，以符合歐盟相關法規。當時 Anthropic 的公告完全沒解釋技術細節，作者一度猜測應該是藏入不可見的 Unicode 字元。Anthropic 原始的支援文件寫道：當支援的 Claude 模型生成文字時，會直接把一個「不可察覺」的浮水印編織進文字本身，使用者不會看到它，也不會改變回應的意義、品質或可讀性。這段用詞明確且不留餘地。

但作者隨後發現，Anthropic 在另一份文件「How Claude's Text Watermark Works」中，揭露了真正的作法，而它與「不改變意義」的承諾完全矛盾。

🧩 用「綠色字」與「紅色字」留下指紋

這項技術本質上是一種語意層級的隱寫術（steganography）。在每一個 token 生成的節點，系統會依據一把秘密金鑰，動態地把候選字詞分成「綠色清單」與「紅色清單」，模型在生成時會被調整成更傾向選擇綠色清單裡的字詞，但並非每次都選，就像一枚 51:49 的偏門硬幣，仍然有將近一半的機率落在「錯」的一面。

由於哪個字屬於綠色、哪個屬於紅色是逐次動態決定的，外界看不出任何固定的「Claude 偏好字詞清單」。偵測時的原理就像丟硬幣測試公正性：文字越長（相當於丟的次數越多），統計上就越有信心判斷這段文字究竟是否出自被加了浮水印的模型，而文字太短則完全無法做出可信的判斷。且由於偵測依賴秘密金鑰，只有 Anthropic 能偵測 Claude 留下的浮水印訊號，Claude 偵測不出 Gemini 的浮水印，反之亦然。

作者特別推薦 James Padolsey 一篇互動式文章「How AI Text Watermarking Works」，認為那是解釋這套概念最好的資料。

💡 沒有兩個同義詞是完全相同的

作者對此最核心的質疑是：任何兩個同義詞都不是完全等價的表達。「他把握了這個機會」和「他抓住了這個機會」語意相近，卻不是同一句話。作者希望自己使用的任何 LLM，在每一個決策點都選出最精準的字詞，在推理速度與成本這類必要的現實限制之下，這是他能接受的取捨，但為了讓文字「可被偵測」而刻意讓模型偏離最佳選字，這種犧牲他認為是不能接受的。他強調，這不只關乎有人想拿 AI 文字冒充自己所寫，即便只是用 LLM 校對人寫的文章，這種用字上的系統性偏移依然存在。

🎯 實務啟示

如果你的產品或研究流程會用 Claude 生成文字後再拿去做下游處理，例如語言風格分析、微調資料蒐集、或是與其他版本文字做逐字比對，這種以字詞選擇機率為基礎的浮水印機制，理論上會在文字裡引入系統性但不可見的統計偏移。目前只有 Anthropic 掌握偵測金鑰，第三方無法自行驗證浮水印的存在與強度，這代表使用者暫時無從評估它對自己應用場景的實際影響，值得在合規與品質要求並重的場景多留意官方後續說明。

🔗 來源
- 標題：Anthropic's 'Watermark' Text Adulteration in Claude Is a Perversion of Writing
- 作者／機構：ropbear
- 連結：https://daringfireball.net/2026/08/anthropics_watermark_text_adulteration_in_claude_is_a_perversion_of_writing

#Anthropic #Claude #AIWatermarking #Steganography #AIRegulation #EUAIAct #LLM #ContentProvenance #AIEthics #TextGeneration
