---
title: '[AINews] DeepSeek v4.1-Flash: 763B-P8B-D16B novel causal Encoder–Decoder architecture
  with vision marks the Return of the Whale'
source: Latent Space
url: https://www.latent.space/p/ainews-deepseek-v41-flash-763b-p8b
model: claude-code/sonnet
generated_at: '2026-09-12T19:29:20.402079'
score: 117
---

📌 DeeSeek V4.1-Flash：版本號沒變,骨架全部重練

TL;DR：DeepSeek 用「V4.1」這個保守版號,偷偷換上全新 causal encoder-decoder 架構,主打長 context agent 的極致推理效率。

版本號只從 V4 Pro 跳到 V4.1-Flash,乍看像是小補丁,但社群裡已經有人直接說「這根本該叫 V5」。如果你只看標題和 benchmark 排名,DeepSeek 這次是故意要騙過你的。

🤔 **沉寂一年後的回歸**

自 R1 論文在 2025 上半年引爆話題後,DeepSeek 有將近一年時間刻意低調,把開放模型的鎂光燈讓給 GLM 與 Kimi。這次他們直接退役 V4 Pro,全力押注一個全新架構,卻只給它取名 V4.1-Flash——根據 Latent Space 的報導,這是一次刻意的「反差測試」,看誰真的懂得讀懂表面版號之下的架構躍進。

🧩 **prefill 用 8B,decode 用 16B 的 causal encoder-decoder**

Artificial Analysis 指出,V4.1-Flash 採用全新的 causal encoder-decoder 架構:輸入 / prefill 階段啟用 8B 參數,輸出 / decode 階段啟用 16B 參數,總參數量 763B,若延伸既有 MoE 命名慣例可寫成「763B-P8B-D16B」,稀疏度約 1-2%。搭配新提出的 Sliding-Window Attention Bounded Replay 機制,KV cache 佔用量最多可壓到 V4 Flash 的 1/8。

社群技術帳號 Stochastic Chasm 將這套設計與 HySparse、NSA,以及 DeepSeek 自家 V4 的 CSA/HCA 相比,歸納為「局部 sliding-window 分支 + 稀疏檢索分支」的組合,認為這類 sparse/local 混合正在成為一種更廣泛的架構模式。多模態部分則沒有大改,backbone 直接吃視覺 token,只是把常見的 2x2 pixel unshuffle 換成 3x3,視覺編碼器的設計也被指出與 Kimi K3 有明顯差異。

TeortaxesTex 進一步觀察到 DeepSeek 一貫的怪癖:前幾層一向做得比較特殊,過去是 dense 或 hash-routed,這次則改成純 SWA;他形容整個 stack「壓縮到只剩 40 層,其中真正算 decoder 的可能只有 20 層」,並猜測背後用了多種壓縮頻率。nrehiew 的技術筆記則直指 KV cache 壓縮是整個設計的核心,並補充了不少訓練工程細節:降低長尾停滯的 dispatch 策略、沿用舊 checkpoint 的 router replay、用資料集層級的 capping 處理較短完成度的 off-policy 效應、bounded off-policy ratio 與 loss masking,以及在 checkpoint 更新時保留 KV 與 router 狀態;最終階段還對 40 多個 teacher 模型做 full-vocab OPD。他認為這套設計比 V4 舊有的 HSA+CSA 組合乾淨許多,「非常明顯是為 inference 而設計」,在被測分數區間內 KV 大小約為 890 bytes/token。Stochastic Chasm 則推測其中用了 QAT 訓練 KV cache,可以解釋為何模型在 FP4 KV cache 下表現優於同儕。

📊 **便宜、快、還拿下開放權重榜首**

Artificial Analysis 的 Intelligence Index 給出 40 分,略低於 GLM-5.3-Flash,但高於最新的 V4 Pro,定價為輸入 $0.30 / 百萬 token、輸出 $1.20 / 百萬 token,快取輸入只要 $0.006 / 百萬 token,離峰時段再打五折。Vals AI 則將它評為開放權重模型中的新科第一,排名超越 Kimi K3,每次測試僅 $0.30,是開放權重前十名裡最便宜的一個(評測條件為 1M context、384 個最大輸出 token、temperature 1、預設 top-p/top-k、high reasoning effort)。Baseten 在模型上線當天就完成支援,將其定位為比 V4 Pro 0813 更聰明、更快、更省的版本,支援文字與視覺輸入,提供 ZDR 與 1M context;Ollama 也已開始向 Max、Team 帳號推送,稍後會擴及 Pro 訂閱用戶。模型採 MIT 授權,支援文字加圖片輸入。

💡 **社群的真實反應**

Sebastian Raschka 稱這是一次「大翻修」,直言「應該叫它 DeepSeek V5」,並點出 encoder-decoder 結構是與過去世代最大的斷裂點。xjdr 則形容這是「研究上相當保守甚至偏舊的想法,和工程上可能非常前沿的效能與硬體設計」的一種奇特混合。

🎯 **實務啟示**

如果你的應用是長時間運行的 agent,KV cache 佔用量直接影響成本與延遲上限,V4.1-Flash 這種把 prefill / decode 拆開設計加上大幅壓縮 KV cache 的路線,值得放進長 context agent 場景的選型清單;MIT 授權也代表可以自行部署驗證這些架構宣稱。

🔗 **來源**
- 標題：[AINews] DeepSeek v4.1-Flash: 763B-P8B-D16B novel causal Encoder–Decoder architecture with vision marks the Return of the Whale
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-deepseek-v41-flash-763b-p8b

#DeepSeek #LLM #MoE #EncoderDecoder #KVCache #OpenWeightModels #AIInfrastructure #MachineLearning #AIefficiency #ArtificialIntelligence
