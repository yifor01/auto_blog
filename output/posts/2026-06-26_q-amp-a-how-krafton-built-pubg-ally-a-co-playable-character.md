---
title: 'Q&A: How KRAFTON Built PUBG Ally, a Co-Playable Character Powered by NVIDIA
  ACE'
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/how-krafton-built-pubg-ally-a-co-playable-character-powered-by-nvidia-ace/
score: 92
model: google/gemma-4-31b-it:free
generated_at: '2026-06-26T20:05:34.437093'
---

📌 【NVIDIA ACE 實作】KRAFTON 如何打造 PUBG Ally：定義「可共同遊玩角色」新類別

TL;DR：KRAFTON 利用 NVIDIA ACE 與 2B 引數小模型，在 PUBG 中實現具備記憶與即時語音互動的 AI 隊友。

長久以來，遊戲中的 AI 夥伴一直受限於固定的對話指令碼，讓玩家感覺像是在與機器人對話而非真實隊友。KRAFTON 試圖打破這個僵局，推出了 PUBG Ally，並將其定義為一個全新的類別：可共同遊玩角色 (Co-Playable Character, CPC)。

🤔 **從 NPC 演進到 CPC：不再是死板的對話樹**

不同於傳統的 NPC (Non-Playable Character)，KRAFTON 定義的 CPC 旨在與玩家真正合作、適應遊戲環境，並能在不同對局之間保有記憶。PUBG Ally 透過整合 NVIDIA ACE 的模型套件，讓 AI 能理解玩家的語音指令、分析遊戲動態事件，並以自然語言即時回應。

🧩 **技術管線：將「反射動作」與「語言推理」分離**

為了在激烈的戰鬥中兼顧反應速度與對話自然度，KRAFTON 在技術架構上採取了分層設計：

1. 快速反應層：由行為樹 (Behavior Tree) 處理。負責處理即時的反射動作，確保 AI 在戰鬥中能迅速反應。
2. 語言推理層：由一個 2B 引數的小型語言模型 (SLM) 處理。負責較慢但複雜的語言推理、上下文理解與自然語音溝通。

這樣的設計讓 PUBG Ally 能在維持戰鬥效能的同時，依然能與玩家進行有意義的對話。

📊 **多模態互動與記憶機制**

為了達成流暢的互動體驗，PUBG Ally 的技術路徑如下：
玩家語音 → 裝置端自動語音辨識 (ASR) → 2B 引數 SLM 推理 → 文字轉語音 (TTS) → 回應玩家。

此外，該系統還具備以下特點：
- 多語言支援：支援英文、韓文與中文。
- 記憶系統：使用結構化的長期與短期記憶，讓 AI 能在不同對局之間個性化遊戲體驗。
- 實測最佳化：透過真實玩家的迭代測試，確保 AI 的回應具有可靠性且對遊戲知識有正確的掌握。

🎯 **實務啟示：小型語言模型 (SLM) 的邊緣端潛力**

PUBG Ally 的實作證明瞭 2B 等級的小型語言模型在遊戲場景中的可行性。對於開發者而言，關鍵在於「分層處理」：將對即時性要求極高的行為交給傳統行為樹，而將高層次的認知與溝通交給 SLM。這種混合架構能有效解決 LLM 推理延遲導致的遊戲體驗斷層。

🔗 **來源**
- 標題：Q&A: How KRAFTON Built PUBG Ally, a Co-Playable Character Powered by NVIDIA ACE
- 作者／機構：Elizabeth Goodman / NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/how-krafton-built-pubg-ally-a-co-playable-character-powered-by-nvidia-ace/

#NVIDIA #ACE #KRAFTON #PUBG #SLM #AI #Gaming #SpeechRecognition #NPC #CoPlayableCharacter
