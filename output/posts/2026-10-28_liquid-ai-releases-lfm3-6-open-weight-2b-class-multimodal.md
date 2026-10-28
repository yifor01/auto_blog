---
title: 'Liquid AI Releases LFM3: 6 Open-Weight 2B-Class Multimodal Models'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/27/liquid-ai-lfm3-open-weight-2b-multimodal-models/
model: claude-code/sonnet
generated_at: '2026-10-28T21:54:37.916001'
score: 99
---

📌 Liquid AI 發布 LFM3：一條骨幹分裂出六款 2B 開放模型

TL;DR：Liquid AI 開源 6 款同源 2B 多模態模型，單 GPU 可微調，手機到雲端全裝置皆可跑。

多模態模型通常意味著更大的參數量與更高的部署門檻，但 Liquid AI 這次反過來做：把文字、視覺、語音、全模態（omni）與決策模型，全部塞進同一條 17 億參數的骨幹裡，再分支出 6 個獨立模型。

🤔 **一條骨幹，六個分身要解決什麼問題**

企業要落地 agentic AI，常卡在「模型太大跑不動裝置、太小又不夠可靠」的兩難。Liquid AI 的做法是先打磨出一個夠強的共用骨幹 LFM3-1.7B-Base，再依任務分支出文字、視覺、語音、全模態，以及從視覺與全模態特化出的兩款決策模型（decision model），讓開發者依場景挑選、在單 GPU 上微調，最後部署到手機、筆電、私有伺服器或雲端。

🧩 **硬體在環搜尋出的 Tri-Hybrid 架構**

骨幹混合 3 種運算子，共 24 層：13 層閘控短卷積（gated short convolution）、5 層滑動視窗注意力（sliding-window attention，視窗 256 token）、6 層全域注意力。卷積核從上一代 LFM2 的 3 擴大到 7。Liquid AI 透過「硬體在環架構搜尋」找出這個組合：LFM2 當年只在 1 支手機與 1 臺筆電上調校，LFM3 則擴大到 14 種裝置與後端組合，包含 Raspberry Pi 5 與 Qualcomm Hexagon NPU。其他調整還有注意力的 head-wise sigmoid gate、全域層的 partial RoPE，以及 sandwich norm。

基礎模型看過 22T tokens，最後 3.5T tokens 是 agent 導向的中期訓練，context 也在這階段拉長到 256K。後訓練分 4 階段：先在 1.75T tokens 上做 SFT，接著混合 RL，再將 6 個專家教師模型蒸餾成 1 個，最後跑 agentic RL。

📊 **各模態的對戰成績**

Liquid AI 宣稱 LFM3-1.7B 以少 35% 的參數勝過自家上一代 LFM2.5-2.6B。在 agent 相關任務上差距更明顯：

| 基準 | LFM3-1.7B | Qwen3.5-9B |
|---|---|---|
| WebArena-Verified | 38.42 | 28.94 |
| BFCL V4（工具呼叫） | 71.39 | 62.83 |
| GPQA Diamond | 63.37 | 80.40 |
| SWE-bench Verified | 43.40 | 51.20 |

可以看到知識類（GPQA Diamond）與 agentic coding（SWE-bench）上，體量更大的 Qwen3.5-9B 仍佔優；但在需要操作網頁、呼叫工具的 agent 任務上，LFM3-1.7B 反而領先。加上工具搜尋後，Humanity's Last Exam 分數從 7.17 拉升到 13.90，顯示搜尋能部分彌補小模型的知識短板。

視覺模型 LFM3-VL-2B 在 62 個視覺基準上平均 71.4 分，與 Gemma 4 12B 的 71.7 幾乎打平，並在視覺定位（77.3）與 GUI 理解（83.1）上領先；但影片理解（61.2）與 agentic 任務（42.5）仍落後更大型的 API 模型。音訊模型 LFM3-Audio-2B 的英文 WER 為 6.2，TTS 的 UTMOSv2 評分 3.8。全模態模型 LFM3-Omni-2B 在 Daily-Omni 拿下 70.1，優於 Qwen2.5-Omni-7B 的 61.3。決策模型 d1-2B 以比前代 d1-3B 少三分之一的參數，把 Decision Bench 從 83.6 推進到 85.2。

💡 **推理效率與特化案例**

部署面，Liquid AI 用 llama.cpp 在 Q4_0 量化、32K context 下測試：完整 128K context 只需 1.6GB KV 快取，相較 Qwen3.5-4B 的 4.3GB 省下不少記憶體。雲端側，1 張 NVIDIA B300 搭配 SGLang，LFM3-1.7B 在 1,024 併發請求下每天可產出 3.6B tokens。特化能力上，團隊在 1 張 A100 上花幾小時做 SFT 加 GRPO，就把風力發電機葉片缺陷分類任務的準確率拉到 67%。

⚠️ **知識與程式碼能力仍是短板**

在需要廣泛知識或複雜程式碼生成的任務上，2B 級模型終究吃虧：GPQA Diamond 與 SWE-bench Verified 上都落後 9.7B 的 Qwen3.5-9B 一截。這提醒開發者，LFM3 的定位是「可特化的 agent 執行者」，而非取代大型通用模型的知識來源。

🎯 **實務啟示**

對需要在邊緣裝置跑多模態 agent 的團隊，LFM3 提供了一條現成的起點：挑選對應模態的 2B 模型，用單 GPU 做短時間微調，再透過 llama.cpp、MLX、vLLM、SGLang 等多種 runtime 部署。相比追求單一巨型模型，這種「一骨幹多分支」策略更適合需要同時維運多個垂直任務、又受限於裝置算力的場景。

🔗 **來源**
- 標題：Liquid AI Releases LFM3: 6 Open-Weight 2B-Class Multimodal Models
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/10/27/liquid-ai-lfm3-open-weight-2b-multimodal-models/

#LiquidAI #LFM3 #OpenWeights #MultimodalAI #EdgeAI #OnDeviceAI #SmallLanguageModels #AgenticAI #ModelFineTuning #AIArchitecture
