---
title: 'Kyutai Releases Voice of Reason: A Speech-Native Model that Solves Spoken
  Math with Reinforcement Learning'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/22/kyutai-releases-voice-of-reason-a-speech-native-model-that-solves-spoken-math-with-reinforcement-learning/
model: claude-code/sonnet
generated_at: '2026-09-23T20:34:24.372133'
score: 105
---

📌 語音直接推理數學：Kyutai 用 RL 把準確率從 27% 推到 77%

TL;DR：Kyutai 開權重發布 Voice of Reason，語音原生模型不經轉文字，靠 RL 大幅提升口語數學能力。

想像你直接對著 AI 唸一道數學題，它不轉文字、不呼叫另一個文字 LLM，就用聲音直接回答你——而且準確率能從不到三成推到接近八成。

🤔 **背景：語音原生模型的兩難**

摘要指出，cascaded pipeline（語音轉文字 → 文字 LLM → 文字轉語音）在推理任務上目前仍然領先，但每一段都會疊加延遲，也會丟失語氣等 paralinguistic 線索。語音原生模型則必須定時吐出音訊才能維持互動感，這限制了它能負擔多少「隱藏推理」token。

🧩 **方法與架構：13 個文字 token 換 26 個音訊 token**

Kyutai 發布的兩個開權重 speech-to-speech 模型，命名為 Voice of Reason，都以 GLM-4-Voice-9B 為起點，接著疊加 supervised fine-tuning（SFT）與強化學習（RL），整個過程沒有轉錄步驟，也沒有另外接一個文字 LLM。GLM-4-Voice 原本的輸出方式是交錯進行：13 個文字 token，接著 26 個音訊 token，反覆循環。

訓練用的 RL 目標，把 reward 在每個 group 內置中，形成一個 group-relative REINFORCE 目標，研究團隊表示這與 GRPO 有關，但拿掉了 PPO 的 clipping 與 KL regularization。訓練用了 16 張 H100，總共跑了 1,500 次 RL 更新。

📊 **數據：27.3% → 58.7% → 77.1%**

- Base GLM-4-Voice 在口語版 GSM8K 上的準確率是 27.3%。
- 先前的 STITCH 方法透過加入推理片段，把它推到 58.7%。
- 論文報告的分數採用 top-k 50 decoding、3 個 seed 平均；若拿掉 top-k 限制，兩個發布的 checkpoint 分別達到 70.3% 與 77.1%。
- 評估用的語音來自 GPT-4o-mini-TTS，與訓練資料使用的 TTS 系統不同，判分則由 GPT-4o 擔任 judge。
- 研究團隊稱這是 RL 首次應用在語音原生模型的數學推理任務上。

⚠️ **限制**

摘要指出，cascaded pipeline 在純推理分數上仍然領先，只是要用延遲與 paralinguistic 線索換取；文中列出的 omni 與 cascaded 系統分數屬於更大規模的頂線參考，並非同規格的對照比較；評估語音的 TTS 系統與訓練資料的 TTS 系統不同，可能造成分布上的落差。

🎯 **實務啟示**

兩個 BF16 checkpoint 都可以在單張 H100 上自行架設，但需要另外準備 GLM-4-Voice repo 提供的 speech tokenizer 與 decoder，權重繼承 GLM-4-Voice 的授權條款，目前也沒有 Hugging Face inference provider 託管。對想實驗「語音直接推理」而非傳統 cascaded 架構的團隊來說，這是目前少見的開權重起點。

🔗 **來源**
- 標題：Kyutai Releases Voice of Reason: A Speech-Native Model that Solves Spoken Math with Reinforcement Learning
- 作者／機構：Asif Razzaq／MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/22/kyutai-releases-voice-of-reason-a-speech-native-model-that-solves-spoken-math-with-reinforcement-learning/

#Kyutai #SpeechAI #ReinforcementLearning #GLM4Voice #VoiceAI #GSM8K #OpenWeights #SpeechToSpeech #MathReasoning #AudioML
