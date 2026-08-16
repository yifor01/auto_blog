---
title: Building an AI Text Detector From Scratch
source: Sebastian Raschka
url: https://magazine.sebastianraschka.com/p/ai-detector-from-scratch
model: claude-code/sonnet
generated_at: '2026-08-16T06:07:53.687859'
score: 94
---

📌 從零打造 AI 文字偵測器，順便訓練會反偵測的模型

TL;DR：用 DistilBERT 打造 0-100 分的 AI 文字偵測器，並拿它當 verifier 訓練 SLM 學會避開偵測。

如果你曾用 ChatGPT 潤飾自己寫的文章，卻擔心潤飾過頭讓文字被標記成「AI 生成」，這篇教學正好切中這個矛盾：它不只解釋 AI 偵測器怎麼運作，還反過來拿偵測器當教練，訓練一個小型語言模型學會避開偵測。

🤔 Substack 上線 AI 偵測器，順便解答「這東西怎麼運作」

Substack 最近在介面上線了 AI 偵測器功能，這也讓作者想起常有人詢問「有什麼有趣的本地 DIY LLM 專案，可以展示小型語言模型（SLM）的能力」。這篇文章把兩件事結合：用建造一個簡化版偵測器，來解釋 AI 偵測器的運作原理，同時作為一個更廣泛主題的案例研究——如何打造一個可以搭配 LLM 使用的 scorer 或 verifier，而不只侷限在數學、程式碼這類傳統 reasoning 模型的訓練場景。

實務上，這種偵測器可以用來過濾垃圾內容，也能用在改善個人寫作上：例如寫完一篇長文，想用文法檢查工具修飾可讀性，這時就可能出現一種提示詞用法：「幫我修正文法，同時確保文字仍然被判定為 0% AI 生成」。

🧩 用 DistilBERT 打造 0-100 分的偵測分數，還能反過來訓練會躲偵測的模型

作者打算開發一套與 Pangram 模型類似的方法，據作者所知，Pangram 正是 Substack AI 偵測功能背後的技術。他也提到自己在 2023 年寫過一篇文章，整理偵測 AI 生成文字的不同方法，從監督式分類器、基於擾動（perturbation-based）的機率測試，到困惑度（perplexity）量測與浮水印（watermarking），做法各有不同。

這次教學選擇微調一個 DistilBERT 分類器（做法類似他早期文章 Finetuning Large Language Models 中的方式），輸出一個 0 到 100 的分數。這本質上是一個帶有估計機率分數的分類器：分數代表分類器根據其訓練分布，估計文字屬於「AI 生成」類別的機率，但作者特別提醒，不該把它解讀成文字真的是 AI 寫的通用機率。專案的整體目標，是展示一個包含評估、訓練與本地部署的完整實務 LLM 專案，最終產出一個人類與 agent 都能用的偵測 API，以及一個好用的 UI。

⚠️ 偵測器終究是一場貓抓老鼠的遊戲

作者直言：AI 偵測器本質上是一場貓抓老鼠的競賽。偵測器可能學會辨識某種 AI 生成文字的特徵模式，接著下一代 LLM 可能無意或刻意地不再表現出該特徵，成功避開偵測，偵測器就得再更新以應對這款新模型，如此循環。此外，偵測器也很可能出現偽陽性（false positive），也就是把人類寫的文字誤判為 AI 生成，這是實務部署時必須正視的風險。

🎯 實務啟示

對打算用 LLM 做內容審核、垃圾內容過濾，或個人寫作輔助工具的工程師來說，理解偵測器的機率本質與貓鼠遊戲局限，比盲目相信一個分數更重要；而「用偵測器當 verifier 訓練另一個模型」這個做法，也提供了一個把 verifier-based 訓練套用到數學、程式碼以外領域的具體範例。

🔗 來源
- 標題：Building an AI Text Detector From Scratch
- 作者／機構：Sebastian Raschka
- 連結：https://magazine.sebastianraschka.com/p/ai-detector-from-scratch

#AIDetection #DistilBERT #LLM #MachineLearning #TextClassification #Verifier #SmallLanguageModels #NLP #AIWriting #Substack
