---
title: 'NVIDIA Releases Nemotron 3.5 Bolt E4B 4GB: An Open Small Language Model for
  Local Voice Agents, Game Characters and Robots'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/23/nvidia-nemotron-3-5-bolt-e4b-4gb/
model: claude-code/sonnet
generated_at: '2026-10-24T19:34:39.873954'
score: 102
---

📌 【NVIDIA 開源】Nemotron 3.5 Bolt E4B：4GB 跑好語音與遊戲 Agent

TL;DR：NVIDIA 用純強化學習後訓練 Gemma 4 E4B,打造能在 RTX／Jetson 本機跑的 4GB 對話 agent 模型。

多數小模型要在「對話流暢」與「工具呼叫精準」之間二選一,NVIDIA 給的解法是：直接跳過 SFT。

🤔 瞄準三種本機 agent 場景

Nemotron 3.5 Bolt E4B 是從 Google Gemma 4 E4B 後訓練而來的小模型,目標是裝置與語音助理、互動式遊戲角色,以及嵌入式或工業用 agent。研究報告中展示了一臺跑在 Jetson Orin Nano 8GB 上的 Reachy Mini 機器人,由 Cosmos 3 Edge 處理視覺,Bolt 負責語音回覆與工具呼叫。NVIDIA 也把它稱作 NVIDIA ACE 遊戲角色的第三代小模型。

🧩 不做 SFT,全靠 RL 調出對話與工具呼叫的平衡

研究報告指出,SFT 雖然能改善工具呼叫能力,卻會傷害 Gemma 原本的對話品質與語氣簡潔度。NVIDIA 團隊因此完全跳過 SFT,透過 NeMo-RL 與 NeMo-Gym,只用 RLVR 與 RLHF 做後訓練。每一筆訓練樣本都會同時跑過 reasoning 與 non-reasoning 兩種模式,每個 batch 維持 non-reasoning 對 reasoning 2:1 的比例;GenRM 環境中的長度懲罰則防止答案在訓練過程中越長越囉嗦。資料集與完整訓練配方皆已公開。

部署端上,團隊把 BF16 checkpoint 透過 importance-matrix calibration 量化成 Q4_K_M,校正資料約使用 1M tokens 的 RL rollout;另外還搭配一個 DFlash drafter 做 speculative decoding。

📊 RTX 5070 上快 1.21 倍,21 項 benchmark 贏 15 項

在 RTX 5070 上,Bolt 搭配 DFlash 達到 272.6 tokens/s,而 Gemma 4 E4B 搭配自帶的 MTP drafter 只有 225.9 tokens/s,快了約 1.21 倍。NVIDIA 把 21 個 benchmark 分成 5 大能力類別,在 reasoning 模式下 Bolt 於 21 項中贏下 15 項,平均分數比 Nemotron 3 Nano 4B 高出約 40%,在開啟 reasoning 的比較中,輸出 token 數最多可減少 80%。Scale Labs 另外在一則 X 貼文中指出,Bolt 在 MultiChallenge 上以 56.03% 的成績排名小模型第一。

但 Bolt 不是處處領先：Qwen3.5-4B 在 Tau2-Bench（75.1 對 55.1）與 RULER 64K（95.1 對 87.0）上勝出,也領先 LongBench v2（59.9 對 50.5）與 BFCL-v3（70.9 對 68.5）;Gemma 4 E4B 則在 EQ-Bench v3 保有微小優勢（41.1 對 39.4）。

⚠️ 自報數字,且「4GB」只是目標值

以上分數皆由 NVIDIA 自行用 NeMo-Gym 測得的 BF16 結果,量測 Q4_K_M 版本時用的是 llama.cpp、batch size 1、3K 輸入搭配 50 輸出 tokens 的設定,廠商公布數字本就可能與實際使用情境有落差。另外,「4GB」指的是目標記憶體佔用區間,並非檔案大小——Hugging Face 上的 Q4_K_M GGUF 實際有 6.18 GB。

🎯 實務啟示

對於要在邊緣裝置上同時跑語音、視覺與對話邏輯的團隊,把語言模型壓進 4GB 等級的記憶體空間,等於把預算留給了語音與視覺模型。Bolt 目前可在 Hugging Face、Ollama、LM Studio、Unsloth 與 Jetson AI Lab 取得,也以 NVIDIA NIM 與 In-Game Inferencing SDK 形式提供,適合直接整合進既有的機器人或遊戲角色 pipeline 做評估。

🔗 來源
- 標題：NVIDIA Releases Nemotron 3.5 Bolt E4B 4GB: An Open Small Language Model for Local Voice Agents, Game Characters and Robots
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/10/23/nvidia-nemotron-3-5-bolt-e4b-4gb/

#NVIDIA #Nemotron #SmallLanguageModel #EdgeAI #Jetson #ReinforcementLearning #VoiceAgents #OpenSource #OnDeviceAI #GameAI
