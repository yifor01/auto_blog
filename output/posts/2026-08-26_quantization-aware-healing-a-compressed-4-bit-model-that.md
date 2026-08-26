---
title: 'Quantization-Aware Healing: a compressed, 4-bit model that outperforms its
  full-precision original'
source: HuggingFace Blog
url: https://huggingface.co/blog/MultiverseComputingCAI/quantization-aware-healing
model: claude-code/sonnet
generated_at: '2026-08-26T06:21:52.878378'
score: 101
---

📌 壓縮再量化為什麼還能變更強？Quantization-Aware Healing 讓 4-bit 模型贏過原版

TL;DR：新方法 QAH 讓結構壓縮＋4-bit 量化後的模型，在 9 項基準測試中有 7 項超越自己的全精度版本。

模型越壓越小，效能理應跟著掉——這幾乎是壓縮領域的鐵律。Multiverse Computing 的最新研究卻讓一個被砍到一半參數、再量化到 4-bit 的模型，反過來打贏了它自己的全精度（bfloat16）版本。

🤔 標準修復流程為何在「結構壓縮＋量化」下失靈

高效部署的標準做法是先壓縮架構（砍層數、head 數或神經元），再把剩下的權重量化到 4-bit，兩步都能省下大量記憶體與運算，但也會系統性地損害推理、數學解題與程式碼生成這些關鍵能力。因此正式的部署流程通常會在上線前加一道「修復」（healing）步驟；gpt-oss、NVIDIA Nemotron 系列，以及作者自家的 Hypernova 60B，都採用某種版本的「壓縮→修復」流程。

作者指出，主流修復方法各有侷限：quantization-aware training（QAT）在前向傳播中插入假量化運算子並持續用任務損失微調，等於是把一整套昂貴的 SFT、RLHF、agentic tuning 後訓練流程，重新跑一次在更嘈雜、更低精度的前向傳播上，成本高，且訓練過久還可能不穩定。另一種方法 quantization-aware distillation（QAD）改用凍結的全精度教師模型，透過 logits 上的 KL 散度直接蒸餾給量化後的學生模型，避免重跑整套後訓練，但這個前提是「存在一個與量化前模型架構完全相同的全精度版本」。一旦模型已經經過結構壓縮（層數、head、神經元都變了），這個前提就不成立了：唯一能當教師的只剩下修復後的 bfloat16 checkpoint，而它本身就是原始模型的蒸餾近似版，用它當教師只會把量化後的學生鎖死在這個已經打折的天花板之下。

🧩 QAH 的做法：直接向「壓縮前」的原始模型蒸餾

Quantization-Aware Healing（QAH）的核心改動只有一個：蒸餾的教師換成壓縮前的原始全精度模型，而不是修復後的 checkpoint。教師與學生甚至不共享架構——教師是全尺寸全精度，學生是打折一半大小、跑在 MXFP4 精度下。由於教師的輸出分佈與架構無關，尺寸或形狀的不匹配並不妨礙知識轉移。學生從頭到尾看不到硬標籤，只透過 logits 上的 KL 散度學習教師的輸出分佈。

這也重新定義了量化這一步的角色：在 QAH 之下，量化不再是修復完成後才附加的一次性有損後處理，而是對著原始教師重新做的第二輪完整蒸餾，這是 bfloat16 checkpoint 從未接受過的監督訊號。換句話說，4-bit 學生不是在「彌補量化造成的損失」，而是在「補齊前一輪修復階段沒時間或沒資料傳遞完的資訊」。這個設計也帶來穩定性上的好處：KL 蒸餾把學生綁定在一個固定的教師分佈上，一旦學生追上教師，就沒有進一步的壓力讓它繼續漂移；相較之下，交叉熵任務損失會持續把學生往硬標籤方向推，這也是訓練穩定性的差異來源。為了在長上下文（修復語料最長到 32k token）下讓 QAH 可行，作者重用了姊妹論文中記憶體效率更高的分塊 KL 散度損失（chunked KL-divergence loss），逐段計算 KL 而不必把整個「詞彙表 × 序列長度」網格攤開在記憶體中，讓 32k token 的修復能塞進固定的 GPU 記憶體預算。

📊 9 項基準測試中贏 7 項，長上下文與數學進步最多

作者把 QAH 套用在一個從 GPT-OSS 120B 壓縮到 60B 參數、再量化到 MXFP4 的模型上，並與同一個 60B 架構的 bfloat16（修復後）checkpoint 直接比較：

| 基準測試 | 120B 教師（MXFP4） | 60B BF16（修復後） | 60B MXFP4（QAH） | QAH vs BF16 |
|---|---|---|---|---|
| AA-LCR（長上下文推理） | 50.0 | 35.3 | 42.7 | +7.4 |
| AIME 2025（數學） | 80.0 | 70.7 | 76.3 | +5.6 |
| Aider（agentic coding） | 45.3 | 38.2 | 40.9 | +2.7 |
| τ²-bench（工具使用） | 68.4 | 59.4 | 61.7 | +2.3 |
| GPQA Diamond（科學） | 69.0 | 65.7 | 67.4 | +1.7 |
| IFBench（指令跟隨） | 63.3 | 58.4 | 59.9 | +1.5 |
| LiveCodeBench（程式碼） | 66.0 | 65.5 | 66.5 | +1.0 |
| MMLU-Pro（知識） | 78.0 | 74.0 | 73.8 | −0.2 |
| SciCode（科學程式碼） | 37.5 | 35.6 | 34.2 | −1.4 |

9 項裡有 7 項，4-bit 的 QAH 模型贏過自己的 16-bit 來源，增幅最大的兩項正好是壓縮通常傷害最重的能力：長上下文推理（AA-LCR +7.4）與數學（AIME 2025 +5.6）。更值得注意的是，QAH 模型雖然只有教師一半的參數量、約四分之一的權重記憶體，卻在 LiveCodeBench 上反超 120B 教師（66.5 對 66.0），在 GPQA Diamond 上也只落後 1.6 分（67.4 對 69.0）；與教師差距最大的仍是 AA-LCR，這也是壓縮流失的能力中最難恢復的極端長上下文場景。

作者另外在 GPT-OSS 9B 上做了 QAH 與 QAT 的正面比較（量化到 MXFP4，追蹤 MMLU-Pro、LiveCodeBench、GPQA Diamond 的平均表現），結果顯示兩者能達到相近的峰值，QAH 峰值為 54.9，QAT 峰值則略低。

⚠️ 限制

QAH 在 MMLU-Pro 與 SciCode 這兩項基準上仍落後 bfloat16 版本，不過差距都在 1.5 分以內；與原始 120B 教師相比，最大殘餘落差出現在 AA-LCR 這類極端長上下文任務上，作者也坦言這部分本來就是壓縮流失後最難恢復的能力。

🎯 實務啟示

對正在規劃「壓縮＋量化」部署管線的團隊來說，QAH 說明了一個關鍵細節：修復階段選誰當蒸餾教師，遠比選用哪種量化格式更影響最終品質。如果你的壓縮流程也是先產出一個 bfloat16 中繼版本再量化，值得檢查修復步驟是否直接接回最原始的全精度模型，而不是拿已經打折的版本再蒸餾一次。

🔗 來源
- 標題：Quantization-Aware Healing: a compressed, 4-bit model that outperforms its full-precision original
- 作者／機構：Antonio Tiene, Iker García-Ferrero, Ali Hashemi, Bakbergen Ryskulov（Multiverse Computing）
- 連結：https://huggingface.co/blog/MultiverseComputingCAI/quantization-aware-healing

#QuantizationAwareHealing #ModelCompression #LLMQuantization #KnowledgeDistillation #MXFP4 #GPTOSS #EfficientAI #ModelOptimization #4BitQuantization #MachineLearning
