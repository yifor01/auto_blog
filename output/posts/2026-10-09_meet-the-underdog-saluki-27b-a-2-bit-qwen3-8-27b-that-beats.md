---
title: 'Meet the Underdog Saluki 27B: A 2-bit Qwen3.8-27B That Beats the Original
  at Tool Calling'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/09/meet-the-underdog-saluki-27b-a-2-bit-qwen3-8-27b-that-beats-the-original-at-tool-calling/
model: claude-code/sonnet
generated_at: '2026-10-09T22:01:09.403788'
score: 79
---

📌 2-bit量化也能打？Saluki 27B挑戰原版Qwen3.8-27B的工具呼叫力

TL;DR：Apache 2.0授權的2-bit GGUF模型把54GB壓到7.89GB，主打agent必備的工具呼叫能力。

一個 27B 參數的模型，原本需要 54 GB 的 BF16 權重才能跑，現在被壓成不到 8 GB，而且主打的不是閒聊，是 agent 最吃重的那個能力：工具呼叫（tool calling）。

🤔 **本機agent的硬體門檻問題**

Underdog 是 Conway Research 推出的 on-device 助理專案，這次以 Apache 2.0 授權釋出 Saluki 27B。它是 Qwen3.8-27B 的 2-bit、混合精度 GGUF 版本，整個模型只需要 7.89 GB，而原始 BF16 模型需要 54 GB。對想在本機跑 27B 級模型的開發者來說，記憶體門檻直接被砍掉超過八成。

🧩 **壓縮時刻意保護工具呼叫能力**

Underdog 在壓縮時特別針對工具呼叫做了調校，因為這是「把一個聊天模型變成 agent」的關鍵技能。其結果是 Saluki 27B 可以直接跑在 stock llama.cpp 上，不需要額外的 fork 或客製化推理框架。

📊 **有對照組，但具體分數尚未在摘要中揭露**

Underdog 把測試結果分成兩組：第一組是在同一套測試環境（harness）下跑 Saluki 與原版模型的對照；第二組則是拿 Saluki 去對比其他廠商公開的全尺寸模型分數。不過目前取得的素材中並未附上這兩組測試的具體數字，只提到了與競品 Bonsai 2 的比較脈絡：Bonsai 2 模型規模更小，宣稱在 14 個 thinking-mode 基準測試中有 98.2% 的能力保留率，數學能力也更強，包括 AIME25 拿下 95.00 分；但 Bonsai 2 需要 PrismML 自家的 llama.cpp fork 才能跑，因為它的打包格式會被 stock llama.cpp 拒絕，而 Saluki 可以直接在標準版 llama.cpp 上運作。

值得留意的是，由於各家廠商使用自己的測試 harness，跨廠商的分數並不能直接橫向比較。

⚠️ **缺乏統一基準，數字解讀要謹慎**

Saluki 相較 Bonsai 2 最大的差異化賣點是「能跑在 stock llama.cpp 上」，這對不想維護客製化推理框架的開發者是實際的部署優勢；但在能力保留率上，由於 Underdog 並未公開與 Bonsai 2 可直接比較的統一基準分數，開發者在選型時仍需要自行跑一輪涵蓋自己實際使用場景（尤其是工具呼叫相關任務）的測試。

🎯 **實務啟示**

如果你的本機 agent 應用受限於顯卡記憶體，又需要 27B 等級模型的推理能力，Saluki 27B 值得列入候選名單，尤其是它不需要客製化 llama.cpp fork 這點能大幅降低部署複雜度。但在正式採用前，建議針對你自己的工具呼叫場景做實測，而不是直接套用廠商公告中的宣稱。

🔗 **來源**
- 標題：Meet the Underdog Saluki 27B: A 2-bit Qwen3.8-27B That Beats the Original at Tool Calling
- 作者／機構：Michal Sutter／MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/09/meet-the-underdog-saluki-27b-a-2-bit-qwen3-8-27b-that-beats-the-original-at-tool-calling/

#Quantization #GGUF #LlamaCpp #Qwen #ToolCalling #OpenSourceLLM #OnDeviceAI #LocalLLM #AIAgent #ApacheLicense
