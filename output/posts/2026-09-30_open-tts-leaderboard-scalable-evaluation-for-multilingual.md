---
title: 'Open TTS Leaderboard: Scalable Evaluation for Multilingual Text-to-Speech
  and Voice Cloning'
source: HuggingFace Blog
url: https://huggingface.co/blog/open-tts-leaderboard
model: claude-code/sonnet
generated_at: '2026-09-30T21:49:26.719705'
score: 81
---

📌 開源 TTS 模型破萬，評測方式卻停在人工投票時代

TL;DR：HuggingFace 推出 Open TTS Leaderboard，用客觀指標取代耗時的 arena 投票，補齊開源語音模型的評測缺口。

Hugging Face Hub 上的文字轉語音（TTS）模型截至 2026 年 9 月底已突破 8,000 個，但評測方式幾乎原地踏步：主流做法仍是 arena 式配對投票，收集足夠票數後用 Bradley–Terry 模型算出 Elo 分數。問題是，這種方式追不上模型發布的速度，而且以 Artificial Analysis 為例，92 個模型裡只有 16 個是開放權重模型，Voice Arena 也呈現類似偏向商業 API 模型的傾斜。原因不難理解：串接一個 API 模型只需要一把金鑰，開源模型卻得由 arena 營運方自行架設與服務，商業廠商自然也更有動機去爭取曝光。

🤔 **人工投票的另一個弱點：評審會變**

除了規模化問題，作者引用赫拉克利特「人不能兩次踏入同一條河流」來說明人工評審的一致性難題：即使是同一個人，對「更好」的判斷標準也會隨時間改變，遑論不同投票者之間的標準差異。

🧩 **三個互補的客觀指標**

Open TTS Leaderboard 選擇用三類客觀指標取代人工投票：

- **可理解度（Intelligibility）**：用 Qwen3 ASR（Open ASR Leaderboard 上排名最高的開源模型）將生成語音轉回文字，計算與原始 prompt 之間的字詞錯誤率（WER）與字元錯誤率（CER）。
- **速度（Speed）**：在 H200 GPU 上測量批次離線推論的逆即時因子（RTFx），以及串流情境下 batch size 1 的首個音訊延遲（TTFA），GPU 與 CPU 皆有數據。
- **語者相似度（Speaker similarity）**：計算生成音訊與參考音訊的 WavLM 語者嵌入（speaker embedding）餘弦相似度（SIM）。

靠客觀指標，評測一個模型所需時間從過去收集投票的數週，縮短到數小時。

📊 **多語言與 voice cloning 排行**

預設排行榜以 Seed TTS Eval 與 CV3 Eval（zero shot）的英文分割集平均 WER 排序，hexgrad/Kokoro-82M、Supertone/supertonic-3、fishaudio/s2-pro 在英文 WER 上領先。由於 Seed TTS Eval 只涵蓋英文與中文，其餘語言的成績全部來自 CV3 Eval；中文、日文、韓文屬於以字元為單位的語言，因此改採 CER。綜合多語言表現，k2-fsa/OmniVoice、fishaudio/s2-pro、FunAudioLLM/Fun-CosyVoice3-0.5B-2512 是表現較強的多語言模型。切換「Voice cloning」檢視後，榜單會額外顯示 SIM 欄位，部分模型如 bosonai/higgs-tts-3-4b 與 openbmb/VoxCPM2，在提供參考音訊做語者克隆時，WER 反而會進一步下降。

🧩 **Listen 分頁：聽得到、也能投票**

單靠數字只能說出部分故事，因此榜單保留了「Listen」分頁，讓使用者依語言／資料集、是否比較 voice cloning、指定模型或隨機抽樣的方式，直接聆聽不同模型的生成結果並投票，需要用 HF 帳號登入以過濾垃圾票。團隊表示未來會將累積的投票資料納入榜單。

📊 **串流延遲：kyutai/pocket-tts 領先 GPU 與 CPU 兩端**

「Streaming」分頁以 TTFA 排序，統一在同一批 50 個英文 prompt（來自 CV3-Eval）、相同硬體、模型預設語音下，以 batch size 1 逐一測試，捨棄前 3 次暖機再取中位數。對支援串流 API 的模型量測首個音訊區塊到達時間，非串流模型則以整段語音生成完畢的時間計算。kyutai/pocket-tts 在 GPU 與 CPU 上的串流表現都相當出色。

⚠️ **客觀指標不能取代人耳**

團隊明確表示，WER 只是可理解度的代理指標，SIM 只估計語者身份的保留程度，兩者都無法直接衡量自然度、表現力或聽感偏好，因此這個榜單「並非要取代人工偏好排名」，而是補足 arena 評測規模化不足的缺口，甚至可以反過來幫助投票式榜單決定該收錄哪些模型。

🎯 **給工程團隊的啟示**

若要挑選 TTS 模型，可先用 Open TTS Leaderboard 的 Pareto 圖，在 WER、批次推論速度（RTFx）與模型大小之間找出符合工程限制的候選者，再到 Listen 分頁實際聽過再決定，尤其串流延遲數據對語音代理與互動式應用特別關鍵。團隊也預告將開源評測腳本，讓社群能透過 GitHub Issues 與 PR 直接參與評測方法的演進。

🔗 **來源**
- 標題：Open TTS Leaderboard: Scalable Evaluation for Multilingual Text-to-Speech and Voice Cloning
- 作者／機構：Eric Bezzam, Steven Zheng, Eustache Le Bihan, mrfakename @ Hugging Face
- 連結：https://huggingface.co/blog/open-tts-leaderboard

#TextToSpeech #TTS #OpenSource #VoiceCloning #HuggingFace #SpeechAI #Benchmark #MultilingualNLP #AudioML #MachineLearning
