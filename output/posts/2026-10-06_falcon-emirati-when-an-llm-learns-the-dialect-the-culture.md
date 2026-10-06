---
title: 'Falcon-Emirati: When an LLM Learns the Dialect, the Culture, and the Nuance'
source: HuggingFace Blog
url: https://huggingface.co/blog/tiiuae/falcon-emirati
model: claude-code/sonnet
generated_at: '2026-10-06T21:57:57.602478'
score: 80
---

📌 標題: Falcon-Emirati-7B：教會 LLM 聽懂阿聯酋方言與文化弦外之音

TL;DR: TII 在 Falcon-H1-Arabic 基礎上微調出方言專精模型 Falcon-Emirati-7B，示範如何用資料管線與評測補足低資源方言的文化理解缺口。

一句道地的阿聯酋諺語，就算逐字翻譯成標準阿拉伯文也完全對不上意思——這正是 Falcon-Emirati-7B 想解決的落差。

🤔 背景：標準阿拉伯文學不會的「弦外之音」

阿拉伯文其實更像一個語言家族，而非單一語言。現代標準阿拉伯文（MSA）是新聞與教科書的書面語，但日常對話、幽默、談判與說故事大多發生在地方方言中。在阿聯酋，這個方言就是 Emirati Arabic，擁有自己的詞彙、語感，以及緊密纏繞其中的文化，像是 nabati 詩歌、諺語與民間軼事，這些內容往往無法靠逐字閱讀理解。團隊表示，即使模型能把 Emirati 句子的每個字都翻對，也可能完全誤解句子真正的意思，這就是 Falcon-Emirati-7B 要補上的缺口。

🧩 不是從零開始：建立在 Falcon-H1-Arabic 的混合架構上

Falcon-Emirati-7B 並非從零訓練，而是建立在 TII 稍早推出的 Falcon-H1-Arabic 之上。Falcon-H1 系列採用混合架構，在每個區塊中讓 State Space Model（Mamba）與 Transformer 注意力並行運算，再把兩者輸出融合後送入投影層，藉此在長序列上取得 Mamba 的線性時間效率，同時保留注意力機制對長距依賴的精確捕捉能力，這對型態變化豐富的阿拉伯文格外重要。Falcon-H1-Arabic 系列涵蓋 3B、7B、34B 三種規模，最長支援 128K 到 256K context，且預訓練資料已混入 Gulf、Levantine、Egyptian、Maghrebi 等多種方言。

團隊最終選擇在 7B 版本上進行方言微調：34B 雖然品質可能更好，但訓練與服務成本對一個方言專精聊天模型而言不划算；3B 則沒有足夠的容量承載方言微調所需的文化與語言深度。7B 被團隊認為是品質與成本間的甜蜜點。

🧩 三種資料來源，補足低資源方言的缺口

方言適配最大的困難在於：Emirati 主要是口語，網路上的書面文本遠少於 MSA 甚至其他灣區方言；其意義經常是非字面的，仰賴共享的文化脈絡；而且業界目前沒有一套公認的「方言適配」配方，不清楚該用多少方言資料、如何與 MSA 混合，或是在持續預訓練、SFT、偏好最佳化哪個階段投入最有效。

為此，團隊建立了專屬的 Emirati 資料管線，結合三種來源：第一是從阿聯酋網站與論壇爬取、以方言原生書寫（非從 MSA 翻譯或音譯）的真實文本；第二是關於阿聯酋文化與身份認同的 MSA 文獻，讓模型理解相關主題背景知識，而非學會用方言書寫；第三是在詞彙表與風格規則嚴格約束下生成的合成資料，用以補足真實方言文本涵蓋主題不足的問題，避免生成內容淪為語法正確但「聽起來不道地」的灣區腔調。

🧩 用消融實驗找配方，母語者把關品質

由於沒有現成的方言適配配方，團隊透過消融實驗摸索：該注入多少方言資料、在哪個訓練階段注入、如何平衡真實爬蟲資料與合成資料以避免模型過擬合合成資料的模式，以及需要多少 MSA 文化脈絡才能讓模型「真正懂文化」而不只是表面流暢。每一步都同時依賴自動評分與母語者的人工審查，因為自動指標無法單獨捕捉自然度、語氣與文化契合度。

📊 評測方法與結果

評測分兩條路徑進行：一是由阿聯酋母語者直接審查模型輸出，判斷回答是否「聽起來對」，涵蓋自然度、語氣與文化得體性，這些是自動評測抓不到但母語者一聽就知道的細節；二是使用團隊與社群共同發布的 Alyah（الياه，意為「北極星」）基準做量化追蹤。Alyah 是一個完全原生的選擇題基準，共 1,173 題，由阿聯酋母語者手動蒐集，涵蓋日常問候、禮儀、比喻性語言、文化遺產知識與 Emirati 詩歌等方言與文化最吃重的類別。根據團隊公布的結果，Falcon-Emirati-7B 在 Alyah 上的得分為 84（原始資料片段在此中斷，未提供完整數字）。

⚠️ 限制

團隊坦言方言適配至今沒有成熟的業界標準配方，大量工作仰賴試誤；而 Emirati 作為主要是口語的方言，可取得的真實文本本就稀少，這也是為何需要大量借助合成資料與母語者人工審查來補足。

🎯 實務啟示

對想做低資源語言或方言在地化的團隊來說，這個案例提供一個可參考的流程範本：不必從零訓練新模型，而是在已經具備廣泛語言能力與長 context 的基座模型上，疊加「真實原生文本、主題背景 MSA 文獻、受詞彙表約束的合成資料」三層資料策略，並搭配母語者人工審查與專屬基準（如 Alyah）做量化追蹤，而非只依賴通用自動評測指標。

🔗 來源
- 標題：Falcon-Emirati: When an LLM Learns the Dialect, the Culture, and the Nuance
- 作者／機構：TII（Shaikha Alsuwaidi、Omar Saif Alkaabi、Maitha Alhammadi、Ahmed Alzubaidi、Mohammed Alyafeai、Leen AlQadi、Basma Boussaha、Hakim Hacid）
- 連結：https://huggingface.co/blog/tiiuae/falcon-emirati

#FalconLLM #ArabicNLP #DialectAdaptation #LowResourceLanguage #LLMFineTuning #TII #MambaTransformer #NLP #CulturalAI #OpenSourceLLM
