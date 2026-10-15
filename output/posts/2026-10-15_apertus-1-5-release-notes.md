---
title: Apertus 1.5 Release Notes
source: HuggingFace Blog
url: https://huggingface.co/blog/swiss-ai/apertus-v15-release-notes
model: claude-code/sonnet
generated_at: '2026-10-15T20:47:25.103720'
score: 89
---

📌 瑞士開源模型 Apertus 1.5：補上多模態與推理模式

TL;DR：Apertus 1.5 用 tokenizer 層級的早融合技術，讓 8B／70B 模型讀懂圖片與語音。

🎣 多數開源多模態模型靠額外接上一顆 vision encoder 來「看圖」，Apertus 1.5 選了一條更直接的路：把圖片和語音直接變成 token，塞進跟文字一樣的序列裡。

🤔 從純文字走向多模態的延續預訓練

Apertus 1.0 原本是一個完全開放（open weights、open data、open values、完整訓練細節公開）的瑞士語言模型。Apertus 1.5 在這個基礎上做延續預訓練，8B 模型新增 4 兆 token、70B 模型新增 2 兆 token，分別達到總計 19 兆與 17 兆 token。8B 與 70B 權重已於 2026 年 7 月 24 日以 Apache 2.0 授權上架 Hugging Face。

| 模型 | 總訓練 token 數 | 本次新增 |
|---|---|---|
| Apertus 1.5 8B | 19T | +4T |
| Apertus 1.5 70B | 17T | +2T |

新版帶來五項主要能力提升：原生多模態理解（圖片與語音，語音部分仍屬實驗性質）、可切換的 thinking mode、context window 擴大 4 倍到 262,144 token、更好的指令遵循，以及更強的工具使用能力。

🧩 用 tokenizer 做多模態，架構完全不變

Apertus 1.5 採用早融合（early-fusion）的方式導入多模態：圖片與語音都先被轉成離散 token，和文字 token 放在同一個序列裡處理，而不是另外接一顆獨立的 vision encoder。圖片用 Emu3.5 tokenizer 處理（一張 512×512 的圖變成 1,024 個 token），語音則用 WavTokenizer（每秒 40 個 token）。因為只是擴充詞表，模型架構本身沒有變動，訓練速度也維持在純文字訓練的水準。需要注意的是，模型目前只能「理解」圖片與語音，輸出仍限於文字。

預訓練分四個階段進行：先用純文字加上獨立的圖片、語音資料讓模型認識新的模態（Unpaired），再用圖片—標題、語音—逐字稿配對資料做對齊（Paired），接著用品質更高、數學與程式碼佔比更高的資料做收斂（Cooldown），最後讓 context window 逐步從 8k 擴展到 262k（Long context）。整體訓練資料中有超過一半仍是純文字，目的是保留 Apertus 1.0 原本的語言能力；文字資料來源包含 FineWeb2-HQ+、FinePDFs 與 Nemotron-CC，皆為公開且授權寬鬆的資料，並追溯遵守 robots.txt 的退出聲明。

後訓練則走五個階段：SFT → 長 context SFT → RL → DPO → charter alignment（SDPO）。SFT 用了 370 萬筆文字樣本加上圖片與語音資料，reasoning trace 只加在模型原本解不出來的題目上，工具使用資料則限定為經過執行驗證的軌跡；Apertus 團隊也把這份 SFT 文字資料混合比例公開在 Hugging Face。長 context SFT 在完整 262k 窗口下進行，用來修復短 context SFT 過程中流失的長文本能力。RL 階段使用約 35 萬筆數學、程式碼、指令遵循、多語言與視覺相關的 verifiable reward（RLVR）prompt，混合 thinking 開關兩種模式訓練。DPO 階段用評審模型打分的偏好配對資料，改善對話品質、工具使用與安全性；最後的 SDPO 透過評審回饋與自我蒸餾，讓模型對齊 Apertus Charter 所定義的價值與原則。

📊 多模態表現接近 Gemma 4 12B，翻譯打贏 Haiku 4.5

Apertus 團隊這次大幅擴增評測範圍，除了既有的文字評測，新增了多模態評測（透過整合 lmms-eval 與 VLMEvalKit 的 MLLM-eval-suite）、thinking mode 評測，以及翻譯、多語言、安全性與工具使用的評測，全部基於團隊自家維護的 lm-evaluation-harness fork。

整體而言，Apertus 1.5 仍落後於前沿開源權重模型，但在程式碼與指令遵循上有明顯進步：8B 版本在指令遵循（IF）與多語言任務上超越同量級的開源權重模型，開啟 thinking mode 後在 AIME 這類高難度推理 benchmark 上表現更好。多模態能力則接近 Gemma 4 12B 等同期開源權重模型，在空間理解（開源權重模型中）與文件／圖表理解（開源模型中）方面具備競爭力。團隊也特別提到，Apertus 1.5 在瑞士法律任務上的表現與主流開源權重模型相當；在 Last Translation Benchmark 上，8B 版本的翻譯能力追上 GPT-OSS-20B，並優於 Claude Haiku 4.5 與 Google 翻譯。

Apertus 團隊也和 EvalEval Coalition 合作，用 Every Eval Ever（EEE）格式發布評測結果：這份記錄不只包含分數，還記錄是誰跑的評測、模型怎麼被存取、生成參數設定，以及每個指標該怎麼解讀，這些細節通常是一般 leaderboard 不會附上的。這套格式也被英國 AI 安全研究院用於公開發布自家評測，EvalEval 的分析顯示 EEE schema 能對應歐盟 AI 法案第 55 條與 GPAI Code of Practice 所要求的 60 項評測報告元素中的 56 項。

⚠️ 仍是漸進式升級，語音理解尚屬實驗性質

Apertus 1.5 的評測結果本身也承認，整體能力仍落後前沿開源權重模型；語音理解功能在文件中被明確標註為「實驗性質」，使用時需留意穩定度。

🎯 實務啟示

如果需要完全透明、可重現評測紀錄的開源多模態模型（例如受監管產業、研究用途），Apertus 1.5 的 Apache 2.0 授權、公開訓練資料與 EEE 評測卡片是少見的組合；但若單純追求最高多模態效能，目前表現仍落在 Gemma 4 12B 等模型的量級，選型前建議先用自己的場景資料跑一次評測。

🔗 來源
- 標題：Apertus 1.5 Release Notes
- 作者／機構：Hugging Face（swiss-ai team）
- 連結：https://huggingface.co/blog/swiss-ai/apertus-v15-release-notes

#OpenSource #Apertus #MultimodalAI #LLM #HuggingFace #OpenWeights #AITransparency #Tokenizer #ReinforcementLearning #AIEvaluation
