---
title: 'Zyphra Releases ZONOS3-Mini: Open-Source TTS With 100M Active Parameters'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/10/zyphra-zonos3-mini-open-source-tts/
model: claude-code/sonnet
generated_at: '2026-11-11T23:41:23.937148'
score: 102
---

📌 Zyphra開源ZONOS3-Mini：1億參數可即時語音克隆

TL;DR：Zyphra推出稀疏MoE TTS模型ZONOS3-Mini，僅1億啟動參數即可即時語音克隆。

一個能做zero-shot語音克隆的TTS模型，要塞進瀏覽器分頁裡跑，需要多小？Zyphra的答案是：800M總參數、僅100M啟動參數。

🤔 背景：從ZONOS2的8B瘦身而來

Zyphra開源的ZONOS3-Mini是一個為裝置端即時運作設計的text-to-speech模型。前代ZONOS2用了8B參數與86Hz的codec，體積限制了它能部署的場景；ZONOS3-Mini則改成稀疏Mixture of Experts（MoE）架構，總參數800M，實際啟動參數僅100M，權重以Apache 2.0授權發布。依素材所述，Zyphra用112張NVIDIA H100、花2.5天訓練完成。對開發者而言，重點在於體積：這個模型可以在瀏覽器分頁、筆電，或伺服器端GPU上跑。

🧩 架構：三層堆疊的語音控制

Zyphra表示改動了stack中的三層：身分（identity）控制透過speaker embedding向量與accent task向量，調整年齡、性別、口音與聲音質地；表達（delivery）控制透過activation steering，調整語速、情緒、音量投射與活潑程度；並有learned alignment heads讓steering能在streaming過程中針對特定單字生效。另外還有一個基於VoiceCraft recipe的獨立edit模型，可在生成之後對句子進行修改。ZONOS3-Mini支援zero-shot語音克隆與word-level的語氣控制。

📊 自建評測：ZTTS2-Eval的分數與保留

Zyphra用自建的ZTTS2-Eval benchmark評測模型，涵蓋35種語言的乾淨朗讀語音與20種語言的in-the-wild錄音，並用item response theory在420個題目上計算Capability Index。結果如下：

| 模型 | Capability Index |
|---|---|
| ZONOS3-Mini（speaker-embedding模式） | 66.2 |
| Fish Audio S2 Pro | 61.7 |
| MOSS-TTS v1.5 | 60.2 |

在乾淨語料集上，ZONOS3-Mini的WER為7.79、speaker similarity為83.4。但reference-clip模式下的Capability Index只有44.7；乾淨語料集的MSR-UTMOS品質分數為3.07，落後Fish S2 Pro（3.16）與Qwen3-TTS 1.7B（3.54）。

⚠️ 限制

以上benchmark由Zyphra自建、自行執行，未經第三方獨立驗證；不同模式（speaker-embedding vs. reference-clip）的分數落差明顯，reference-clip模式表現較弱；延遲數字也是在不同GPU上測得，彼此之間不可直接比較。

🎯 實務啟示

對需要在裝置端或低資源環境部署語音克隆／TTS的團隊，ZONOS3-Mini的100M啟動參數與Apache 2.0授權是明顯優勢，值得評估導入；但在正式採用前，建議針對你實際使用的模式（尤其是reference-clip）自行驗證品質分數，而非只看speaker-embedding模式下的數字。

🔗 來源
- 標題：Zyphra Releases ZONOS3-Mini: Open-Source TTS With 100M Active Parameters
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/10/zyphra-zonos3-mini-open-source-tts/

#TTS #ZONOS3Mini #Zyphra #OpenSource #VoiceCloning #MixtureOfExperts #SpeechAI #EdgeAI #ApacheLicense #RealTimeAI
