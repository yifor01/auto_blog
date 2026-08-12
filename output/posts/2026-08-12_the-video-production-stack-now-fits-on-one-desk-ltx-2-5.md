---
title: 'The Video Production Stack Now Fits on One Desk: LTX-2.5 Launches as NVIDIA-Accelerated
  Open Weights World Model'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/11/the-video-production-stack-now-fits-on-one-desk-ltx-2-5-launches-as-nvidia-accelerated-open-weights-world-model/
model: claude-code/sonnet
generated_at: '2026-08-12T07:29:35.279263'
score: 105
---

📌 【NVIDIA 加速】LTX-2.5:整套影片製作流程,塞進一張 RTX 顯示卡

TL;DR:LTX-2.5 是可在單張 NVIDIA RTX 顯示卡本地運行的開源權重影片世界模型。

社群短片、廣告素材、電影前期預覽的產製,正在從雲端搬回本地 GPU。LTX 近日推出 LTX-2.5,一款開源權重的世界模型,鎖定影片生成、即時應用與物理 AI(physical AI)場景,並針對這波轉移做了本地推理最佳化。

🤔 **從雲端算圖搬到桌機,為誰而做**

根據 MarkTechPost 報導,LTX 把 LTX-2.5 最佳化到能在 NVIDIA RTX 顯示卡與 NVIDIA DGX Spark 上本地推理,大幅降低顯示記憶體需求,讓一個前沿級的世界模型能跑在創作者原本就擁有的硬體上。這次發布是 NVIDIA 為期一個月的本地 AI 系列活動的開場作品之一,與同日發布的開源 Nemotron 3.5 Lightning agent 模型互相呼應,傳遞的訊號是:本地加速的開源模型,正在成為預設的生產基礎設施。

對社群短片與廣告團隊來說,痛點從來不是缺乏創意,而是產製足夠數量素材的成本與時間。廣告疲勞(ad fatigue)通常在 7 到 10 天內出現,本地生成把這個瓶頸拿掉:同一份腳本可以跑出多種版本、測試十種不同的 hook、為五個市場做在地化,並在疲勞來臨前就換新素材。

🧩 **核心設計理念:多鏡頭一致性,並重建整條生成管線**

LTX-2.5 的重點是把過去只存在於工作室裡的「一致性」交到創作者手上。原生的多鏡頭(multishot)生成能把一整段連續鏡頭當成同一件事一次生成,讓角色的外觀在不同鏡頭之間保持一致,修正了早期開源模型在多鏡頭場景中容易出現的閃爍問題。模型換上更精準的 Gemma 4 語言骨幹,並搭配新的解碼器,降低高動態鏡頭中的偽影。

MarkTechPost 指出,LTX 這次是重建了生成管線的幾乎每個環節,而不是在舊核心上疊加新功能。整套流程可以直接在 ComfyUI 裡、透過消費級 NVIDIA RTX 顯示卡運行,一個人就能用 LoRA 微調快速鎖定一個品牌角色或簽名風格,不需要工作室、不需要雲端,IP 也不會離開自己的機器。

🧩 **怎麼用**

LTX-2.5 以開源權重形式發布在 Hugging Face,原生整合進 ComfyUI,也可透過 LTX API 使用代管生成服務。它可以在從資料中心 GPU 到 Mac 的各種硬體上運行,對年營收在 1,000 萬美元以下的組織免費使用。程式碼與文件公開在 GitHub 上,額外生成的影片不收取按次費用或計量點數。

📊 **速度比對:本地推理快過影片本身的長度**

在 LTX 公布的圖轉影片(image-to-video)基準測試中,一支 10 秒影片在本地端搭配 2 張 NVIDIA GB200 只需 6.8 秒,透過 LTX API 則需 23.7 秒。作為對照,幾個列出的封閉模型速度分別是:

| 模型 | 生成 10 秒影片所需時間 |
|---|---|
| LTX-2.5(本地,2x GB200) | 6.8 秒 |
| LTX-2.5(LTX API) | 23.7 秒 |
| Omni Flash / Grok 1.5 / Veo 3.1 | 52–70 秒 |
| Seedance 2.0 | 196 秒 |
| FLUX 3 | 259 秒 |
| Seedance 2.5 | 317 秒 |
| Kling 3.0 Pro | 398 秒 |

換算下來,本地端的 LTX-2.5 生成速度比影片本身的播放長度還快,比最接近的封閉模型快 7.6 倍,比列表中最慢的模型快約 58 倍。這個速度差距,讓整夜批次生成與快速 A/B 迭代從理論變成日常可行的工作方式。

⚠️ **適用場景與定位**

LTX 將 LTX 系列定位為目前下載量最高的開源世界模型,累計超過 3,300 萬次下載,並稱 LTX-2.5 是目前為止最強的版本。文中將世界模型與大型語言模型做了區分:語言模型學習預測下一個字,世界模型學習預測下一個時刻,進而生成環境、模擬其行為,並讓使用者在其中行動,這個基礎能支援電影、廣告、遊戲、模擬,以及倉儲與工廠中的機器人應用。開源權重讓團隊對硬體、客製化與 IP 擁有完整掌控權,這也是文中強調的核心優勢。

🎯 **對工程師的啟示**

LTX-2.5 說明了一件事:當本地推理的速度與品質追上雲端服務,影片生成的工作流程可以整個搬回單一工作站,免去按次計費與 IP 外流的顧慮。對正在評估影片生成工具鏈的團隊來說,值得關注的是它與 ComfyUI 的原生整合,以及用 LoRA 微調鎖定角色與風格的做法,這讓客製化不必依賴大規模重新訓練。

🔗 **來源**
- 標題:The Video Production Stack Now Fits on One Desk: LTX-2.5 Launches as NVIDIA-Accelerated Open Weights World Model
- 作者／機構:Jean-marc Mommessin and Asif Razzaq, MarkTechPost
- 連結:https://www.marktechpost.com/2026/08/11/the-video-production-stack-now-fits-on-one-desk-ltx-2-5-launches-as-nvidia-accelerated-open-weights-world-model/

#LTX25 #WorldModel #VideoGeneration #NVIDIA #ComfyUI #OpenWeights #GenerativeAI #RTX #LocalInference #AIVideo
