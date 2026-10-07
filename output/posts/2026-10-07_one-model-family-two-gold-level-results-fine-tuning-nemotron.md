---
title: 'One Model Family, Two Gold-Level Results: Fine-Tuning Nemotron for IOI and
  IMO'
source: HuggingFace Blog
url: https://huggingface.co/blog/nvidia/nemotron-ioi-and-imo-2026
model: claude-code/sonnet
generated_at: '2026-10-07T22:17:45.938941'
score: 101
---

📌 【NVIDIA 最新研究】Nemotron 同時拿下 IOI 與 IMO 2026 金牌門檻

TL;DR：NVIDIA 用同一套 Nemotron 3 基礎模型，分別微調出在 IOI 2026 與 IMO 2026 都達金牌水準的專家系統。

競程與數學奧賽考驗完全不同的能力：IOI 要求程式碼在嚴格時間與提交限制下通過隱藏測試，IMO 則要求嚴謹的自然語言證明。NVIDIA 的 Nemotron 團隊用同一個模型家族，在兩場比賽都做到金牌等級，這指向一個更大的命題——基礎模型的可微調性，可能比單一領域的表現更值得關注。

🤔 核心問題：一個基礎模型能否可重複地變成多個領域專家

NVIDIA 想驗證的是：Nemotron 3 是否是一個足夠強、足夠「好微調」的基礎模型，能用一套可重複使用的流程，分別打造出競程與數學證明兩個完全不同領域的世界級專家系統。

🧩 一套四步驟的通用特化配方

團隊總結出的流程分四步：

1. 從一個強大的 Nemotron 基礎模型出發。
2. 整理領域專屬的題目，並產生高品質的推理軌跡（reasoning traces）。
3. 套用標準的後訓練方法，包括 SFT（監督式微調），必要時加上 RL（強化學習）。
4. 將專家模型搭配一套能生成、評估並改進候選答案的推論迴圈。

**競程方向**：團隊整理了 22,000 道題目並產生合成推理軌跡，訓練出兩個專家模型——30B 總參數／3B 活躍參數的 Nemotron-3-Nano-CC（接受 SFT 與 RL），以及 550B 總參數／55B 活躍參數的 Nemotron-3-Ultra-CC（僅接受 SFT）。團隊也開發了 GenCorrect，一種反覆生成、評估、修正的測試時（test-time）策略。

**數學證明方向**：以 Nemotron 3 Ultra 為起點，訓練一個 SFT 專家與一個 RL 專家。SFT 訓練資料包含 414,890 筆經品質篩選的樣本，涵蓋 15,818 道獨特證明題，內容不只是最終答案，還包括證明生成、修正、驗證與元驗證（meta-verification），讓模型學會建構論證、找出漏洞、回應質疑並判斷證明是否完整。RL 模型則在 9,597 道、貼近模型能力邊界的證明題上訓練。最終系統讓兩個專家模型與通用模型一起針對每道 IMO 題目生成候選證明、評分、產出評語並修正最有潛力的嘗試，再由一個獨立的高運算量階段挑選最終提交版本。整套系統全程使用自然語言，沒有使用形式化證明器、外部工具或網路存取。

📊 從一般能力到金牌分數的進展

IOI 2025 上的進展清楚展示了特化的價值：

| 階段 | Nano 分數 |
|---|---|
| 後訓練前 | 130 |
| SFT 後 | 280 |
| +RL 後 | 291 |
| +GenCorrect | 468（金牌門檻 438.3） |

Ultra-CC 搭配同樣的測試時策略達到 502 分。

| 比賽 | 特化方式 | 結果 |
|---|---|---|
| IOI 2026 | Nemotron-3-Ultra-CC，SFT＋GenCorrect | 535.4／600，高於金牌門檻 361.12，也高於人類最高分 498.27 |
| IMO 2026 | Nemotron 3 Ultra 通用模型＋SFT／RL checkpoint 組成的生成-驗證-修正系統 | 30／42，高於官方金牌門檻 29，六題中四題拿到滿分 |

IOI 的結果來自一次即時、前瞻性的測試，遵循與人類選手相同的時間、網路存取與提交限制，但屬於非官方、未受監督的基準測試，未列入官方排名。IMO 的證明則由官方 IMO 評審評分。

💡 SFT 與 RL 的分工不是固定公式

兩個專案都顯示，適配方式不必在每個規模上都長得一樣。在競程方向，Nano 的進步主要來自 SFT，RL 帶來的提升較小但穩定；而對更強的 Ultra 模型，只需一個 SFT epoch 就能超越完整後訓練過的 Nano，在 IOI、ICPC、LiveCodeBench Pro 上皆是如此。在數學證明方向，SFT checkpoint 在第一輪搜尋中表現最強，RL checkpoint 則拿下整體最佳的單一 checkpoint 成績，兩者優勢互補，因此最終系統同時保留了兩個專家模型與通用模型。團隊強調，這些金牌成績不是單靠微調，也不是單靠暴力取樣得來，而是模型、資料與推論迴圈共同設計的結果。

⚠️ 局限

IOI 2026 的成績屬於非官方、未受監督的基準測試，並未計入正式排名；IMO 系統完全依賴自然語言推理，沒有形式化證明器或外部工具輔助，兩者都是在特定條件下取得的結果，與正式比賽規則仍有差異。

🎯 實務啟示

NVIDIA 公開了完整的可重現資源：Nemotron Labs IMO 2026 collection（SFT／RL checkpoint、兩份訓練資料集，以及新發布的 200 題 Nemotron-IMO-Bench）、記錄訓練方法與系統設計的 IMO 論文，以及包含推論管線、提示詞與已提交證明的 NeMo-Skills репозиторий（含可重現的 quickstart）。競程方面，Nemotron-3-Ultra-CC 模型與 IOI 論文、GenCorrect 方法論，以及對應的評測與推論管線同樣開放於 Hugging Face 與 NeMo-Skills。對於想把通用基礎模型微調成特定領域專家的團隊，這套「基礎模型＋資料策展＋後訓練＋生成驗證迴圈」的配方具有高度參考價值。

🔗 來源
- 標題：One Model Family, Two Gold-Level Results: Fine-Tuning Nemotron for IOI and IMO
- 作者／機構：NVIDIA（Aleksander Ficek、Igor Gitman、Sean Narenthiran、Mehrzad Samadi、Somshubra Majumdar）
- 連結：https://huggingface.co/blog/nvidia/nemotron-ioi-and-imo-2026

#NVIDIA #Nemotron #LLM #ReinforcementLearning #SFT #IMO #IOI #AIResearch #MachineLearning #OpenSource
