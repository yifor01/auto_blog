---
title: Edge0 Releases Audio8-TTS-Realistic, a 0.6B Voice Cloning TTS Model
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/29/edge0-audio8-tts-realistic-0-6b-voice-cloning/
model: claude-code/sonnet
generated_at: '2026-10-30T21:42:17.442894'
score: 84
---

📌 Edge0 Audio8-TTS-Realistic：0.6B 開源語音克隆模型支援 23 種語言

TL;DR：0.6B 參數、單段參考音檔加逐字稿即可零樣本複刻聲音，支援 23 種語言，Apache 2.0 開源。

用一小段錄音複刻一個人的聲音，過去常被認為需要動輒數十億參數的模型才能做到自然，Edge0 的 Audio8-TTS-Realistic 想證明 0.6B 參數也能跨 23 種語言做到。

🤔 **零樣本複刻聲音，為多語言場景而生**

Audio8-TTS-Realistic 是一個開放權重的文字轉語音模型，用途是零樣本語音克隆：給一段參考音檔與其逐字稿，就能複刻該聲音；也支援不提供參考音，直接生成語音。它是 Edge0 的 Audio8 TTS 家族第二個 0.6B 模型，延續前身 Audio8-TTS-Preview-0.6b，維持相同的 Transformers 推論介面，新增了 12 種語言，包括阿拉伯語、芬蘭語、印地語、印尼語、馬來語、挪威語、葡萄牙語、俄語、瑞典語、泰語、土耳其語與越南語，整體支援語言達 23 種。權重與程式碼以 Apache 2.0 授權發布。

🧩 **雙自回歸架構，循序運算只發生在 frame 層級**

模型採用受 Fish Audio S2 Pro 啟發的雙自回歸（DualAR）設計。根據官方技術研究報告，慢分支（slow branch）以 Qwen2.5 0.5B 為基礎，共 24 層、寬度 896，運作速度約每秒 21.5 個 frame，每一步同時預測文字 token 與第一個音訊 codebook；一個僅 4 層的淺層快分支（fast branch）接著平行預測剩下的 9 個 codebook，因此真正的循序運算只發生在 frame 層級，其餘可平行處理。

訓練上，團隊認為單看詞錯誤率（WER）與聲紋相似度（SIM）會忽略節奏、停頓與時間感,一個模型可能兩項指標都很高卻聽起來仍不自然。為此他們訓練了一個 critic，拿模型輸出對照同一句子的真人錄音評分，評分基礎是一個用 6 套開源 TTS 系統輸出建立的「品質階梯」，透過私有的盲聽研究排序，真人錄音排在最高層，合成語音則用停頓壓縮（pause compression）細分出更多層級。為避免 critic 獎勵生成器本身的特徵指紋，額外加入了 identity-erasure loss；critic head 本身約 300 萬參數，架在凍結的 WavLM-large 編碼器上；超過參考語音長度 1.35 倍會觸發時長懲罰，防止模型用拖慢語速的方式「騙過」critic。值得一提的是，最終訓練階段只用了中文與英文的 prompt，卻同時改善了另外 13 種低資源語言的整體指標：錯誤率從 22.53% 降到 20.77%，SIM 從 0.637 升到 0.679。

📊 **多語言基準：互有領先**

以下數字均為自評的錯誤率，越低越好。在 CV3 測試集上，Audio8-TTS-Realistic 優於 VoxCPM2（5.35%）、CosyVoice3-1.5B（6.89%）與 Qwen3-TTS-1.7B（7.73%）。在 MiniMax 測試集上，Qwen3-TTS-1.7B 得到 27.41%，但該模型官方僅支援測試用的 24 種語言中的 10 種。在其他項目，規模更大的模型仍然領先：Higgs TTS 3 在 CV3 為 4.41%、在 MiniMax 為 2.74%，Qwen3-TTS-1.7B 在 Seed-TTS 上平均達 1.01%。

⚠️ **評測口徑不同，數字僅供參考**

Edge0 自己也強調這張比較表只是「參考比較」，因為各家的評測流程與文字正規化方式不同；VoxCPM2 的 CV3 平均分數是 Edge0 自行從其逐語言表格計算出來的，並非官方直接公布的單一數字。另外，throughput 與串流（streaming）效能官方表示尚未進行 benchmark。

🎯 **怎麼用**

環境需求為 PyTorch 2.5 以上、Transformers 4.57 以上，載入時需設定 trust_remote_code=True；語音克隆需要一段乾淨的參考音檔與精確逐字稿。GitHub 儲存庫內附 CLI、批次處理與監督式微調腳本；GPU 部署可透過 SGLang Omni adapter，提供 paged attention、動態批次處理與相容 OpenAI 格式的 /v1/audio/speech API；Hugging Face ZeroGPU 上也有免費的 Playground 可直接試用。

對需要多語言、可自行微調且運算成本低的語音克隆場景，這個 0.6B、Apache 2.0 授權的模型提供了一個便宜的起點；但若目標是特定語言或資料集上最低的 WER 或最佳 SIM，Higgs TTS 3、Qwen3-TTS-1.7B 等更大模型在部分項目仍有明顯優勢，需要依實際場景權衡規模與成本。

🔗 **來源**
- 標題：Edge0 Releases Audio8-TTS-Realistic, a 0.6B Voice Cloning TTS Model
- 作者／機構：Asif Razzaq
- 連結：https://www.marktechpost.com/2026/10/29/edge0-audio8-tts-realistic-0-6b-voice-cloning/

#TextToSpeech #VoiceCloning #OpenSource #TTS #SpeechAI #ApacheLicense #MultilingualAI #DualAutoregressive #AudioML #GenerativeAudio
