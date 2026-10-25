---
title: Hugging Face Releases Carbon-X, a 14B Open DNA Language Model that Brings DNA
  and Natural Language Together for the First Time
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/25/hugging-face-carbon-x-14b-dna-language-model/
model: claude-code/sonnet
generated_at: '2026-10-25T19:43:11.030288'
score: 99
---

📌 Hugging Face推出Carbon-X：DNA與英文共用一個Token空間

TL;DR：140億參數的Carbon-X讓DNA與英文共用token，推論成本只要前沿模型的千分之一。

直接在聊天視窗貼一段DNA序列，問「這段突變是良性還是致病」，然後得到英文回答——這聽起來像是另外接一個外部工具才能做的事，但Hugging Face剛釋出的Carbon-X，把DNA當成語言模型本來就該讀懂的token。

🤔 **多數DNA模型得外接一個獨立的DNA encoder，Carbon-X選擇不這麼做**

Carbon-X是Hugging Face Bio與Zhongguancun Academy、TIGEM／University of Naples Federico II合作開發的decoder-only模型，參數量14.8B。它能讀原始DNA並用英文回答，任務包括判斷突變是良性還是致病性、標出調控區域、分類物種，以及預測下一個base。與BioReason等需要獨立DNA encoder的做法不同，Carbon-X讓DNA跟文字共用同一條token stream、進同一個decoder，權重以Apache 2.0授權開源，實驗室可以把敏感序列留在自己的GPU上處理。

🧩 **一個混合tokenizer，把DNA切成6個base一組的token**

Carbon-X的骨幹從Qwen3-14B出發，是標準的Qwen3架構：40層、hidden size 5120，搭配8個KV head的GQA。真正的關鍵結構是一個混合tokenizer：保留Qwen3原本處理文字的BPE詞彙表，再加上5,515個DNA token，包含4,096個不重疊的6-mer、1,364個補尾（tail）token與3個標記符號。簡單說，一個DNA token對應6個base pair，只要偵測到連續6個以上的A/C/G/T，就會自動標記成DNA token來處理。

訓練依模型卡所述分成四個階段。release post提到，learning rate是最難調的參數：調太高，模型學得會DNA，卻會忘記英文；團隊最後靠降低learning rate、搭配14B的模型規模與較長的訓練時間，解決了這個取捨問題。值得一提的是，團隊也嘗試直接對Qwen3-14B做RL，但在FrontierVEP這項評測上，始終沒能超過50%的隨機猜測基線。

📊 **整體分數介於Qwen3-14B與GPT-6.1 Sol之間，但要留意「拒答」怎麼影響比較**

以下數據均為Hugging Face自報。測試時Carbon-X關掉thinking（enable_thinking=False），對照的前沿模型則用各自最佳的推理強度。Carbon-X整體比Qwen3-14B高27分，比GPT-6.1 Sol低0.8分；在coding-variant effect與next-base prediction上領先，但在complex variant與single-base variant上，前沿模型仍然贏。

有趣的是，拒答率會明顯影響分數：在NextBase測試上，Opus 5.5從低推理強度的17.7%，一路掉到最高推理強度的1.1%，原因是拒答變多；Gemini 4 Argon在FrontierVEP上也隨推理強度提升，從58%掉到38%。也就是說，推理強度越高，模型反而可能因為更謹慎拒答而分數下滑。Carbon-X同時維持了一定的通用能力，在IFEval上拿到79.3%的prompt-level嚴格準確率。

成本方面，以H200每小時5美元計算，Carbon-X處理每題的推論成本大約是GPT-6.1 Sol的1/1,800。用這個價格去跑ClinVar裡240萬個「意義未明變異」(VUS)，整體成本大約300美元，同樣的工作在前沿模型上要花3.2萬到400萬美元。Carbon-X也能當成sub-agent使用：Kimi K3在諮詢Carbon-X之後，DNA指數從49.4%提升到60.5%。

| 比較項目 | 結果 |
|---|---|
| 整體分數 vs Qwen3-14B | 高27分 |
| 整體分數 vs GPT-6.1 Sol | 低0.8分 |
| 2.4M ClinVar VUS 成本 | 約$300（前沿模型約$32,000～$4,000,000） |
| 作sub-agent輔助Kimi K3 | DNA指數49.4%→60.5% |

⚠️ **複雜變異與單base變異，前沿模型仍是贏家**

Carbon-X在部分任務領先，但在complex variant跟single-base variant上仍輸給前沿模型；而且這些比較數據都是Hugging Face自報，加上拒答率會干擾不同模型間的分數對比，解讀時要保留一點空間。另外，模型在評測與訓練時都是thinking關閉的狀態，使用時也需要保持enable_thinking=False才符合它被訓練與驗證的設定。

🎯 **大規模基因篩查的成本，可能不再是前沿模型等級的門檻**

如果團隊需要大量篩查變異致病性，Carbon-X的開源權重跟極低的推論成本，讓「用LLM掃過整個ClinVar資料庫」這種事從昂貴變得可行。對於已經在用大模型做agent任務的團隊，把Carbon-X接成sub-agent，也是一個不用重新訓練自己模型、就能補強DNA能力的方式。

🔗 **來源**
- 標題：Hugging Face Releases Carbon-X, a 14B Open DNA Language Model that Brings DNA and Natural Language Together for the First Time
- 作者／機構：Hugging Face Bio（與Zhongguancun Academy、TIGEM／University of Naples Federico II合作）
- 連結：https://www.marktechpost.com/2026/10/25/hugging-face-carbon-x-14b-dna-language-model/

#CarbonX #HuggingFace #DNALanguageModel #Bioinformatics #Genomics #OpenSource #Qwen3 #LLM #ClinVar #AIForScience
