---
title: How Claude Watermarks AI-Generated Text
source: Sebastian Raschka
url: https://magazine.sebastianraschka.com/p/claude-watermarking
model: claude-code/sonnet
generated_at: '2026-08-23T06:19:44.866503'
score: 76
---

📌 拆解Claude浮水印：從token機率分佈說起

TL;DR：Sebastian Raschka 用一部近48分鐘的講解影片，帶你理解Claude浮水印機制的底層邏輯起點。

Anthropic 宣布要幫 Claude 的文字輸出加上浮水印之後，Sebastian Raschka 原本只想發一則簡短的社群貼文說明原理，結果意外引發熱烈討論。於是他決定不寫成一般文章，而是錄了一部影片，原本規劃 10 張投影片、10 分鐘，最後做到超過 50 張投影片、48 分鐘。

🤔 為什麼 Anthropic 要幫文字打浮水印

Raschka 指出，浮水印的動機是讓 Anthropic 能夠辨識某段文字是否由自家模型（例如 Claude Opus 4.8）生成。這個浮水印對一般使用者是不可見的，只有 Anthropic 自己能夠解碼、確認文字是否帶有這個標記。他也提到 Anthropic 官方那篇說明文章「How Claude's Text Watermark Works」在解釋「為什麼要做」這件事上著墨很多,卻幾乎沒有圖表說明「怎麼做」,只連結了一篇技術性很強的論文，這正是他決定從頭講起的原因。

🧩 從零開始：LLM 怎麼決定下一個字

要理解浮水印,得先理解一般文字生成的運作方式。Raschka 以「the capital of Germany is」這個提示詞為例，拆解了模型產生下一個 token（例如「Berlin」）之前發生的步驟：文字先在 LLM 之外被 tokenizer 轉換成 token ID，這一步只是把文字轉成 embedding 層能處理的格式；接著這些 token ID 才會被送進 LLM。模型的輸出並不是直接給出一個字，而是針對「下一個 token」給出一整組分數，也就是 logits，這是一組範圍從負無限大到正無限大的數值分布。Raschka 特別強調，他不會在這裡重講 LLM 本身的內部機制（他在自己的 Build a Large Language Model From Scratch 等著作與影片中已多次講解），這一段只是為了鋪陳後續說明浮水印如何介入這個機率分布與取樣過程的基礎。

💡 為什麼「從頭寫一遍」在 AI 時代仍然有價值

Raschka 認為，這次浮水印的說明,剛好示範了「從零實作」的價值：即使現在很多程式碼已經可以交給 LLM 來寫，理解一段程式碼在做什麼仍然承載大量資訊。以浮水印為例，親自寫過或讀懂 LLM 取樣的程式碼，才能具體看出浮水印是在哪個環節被加進去、又會帶來什麼樣的後果，而不是停留在官方文件那種抽象、沒有圖示的說明層次。

🎯 實務啟示

對於平常使用或評估 LLM 輸出的工程師來說，先搞懂「tokenize → embedding → LLM → logits 分布」這個最基本的生成流程，是判斷任何浮水印或內容溯源技術是否可靠的前提；與其直接接受官方一句「這是不可見的浮水印」，不如像 Raschka 一樣從取樣機制的源頭去理解它到底動了什麼手腳。

🔗 來源
- 標題：How Claude Watermarks AI-Generated Text
- 作者／機構：Sebastian Raschka
- 連結：https://magazine.sebastianraschka.com/p/claude-watermarking

#Claude #Anthropic #Watermarking #LLM #AIExplainer #TokenSampling #FromScratch #AIContentDetection #MachineLearning #GenerativeAI
