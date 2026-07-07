---
title: OpenAI Releases GPT-Realtime-2.1 and GPT-Realtime-2.1-mini for Low-Latency
  Voice Agents in the API
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/06/openai-gpt-realtime-2-1-mini-reasoning-realtime-api/
score: 91
model: google/gemma-4-31b-it:free
generated_at: '2026-07-07T21:20:16.317083'
---

📌 OpenAI 推出 GPT-Realtime-2.1 系列：低延遲語音代理現在能「思考」後再說話

TL;DR：OpenAI 更新 Realtime API，推出具備推理能力的 mini 模型並降低 25% 延遲，最佳化語音代理的互動體驗。

當你與 AI 語音助理對話時，最尷尬的時刻莫過於 AI 在呼叫工具（Tool Call）時陷入死寂，讓使用者以為連線中斷而隨意打斷，導致對話狀態混亂。OpenAI 這次的更新正是為了打破這個僵局。

🚀 **推出 gpt-realtime-2.1 與 mini 推理模型**

OpenAI 在 API 中釋出兩款新模型：`gpt-realtime-2.1` 與 `gpt-realtime-2.1-mini`。其中最值得關注的是 mini 版本，它是一款專為即時語音互動設計的「小型推理模型」，且定價與先前的 `gpt-realtime-mini` 相同。

🧩 **單一模型架構降低延遲與保留細節**

Realtime API 的核心在於透過單一模型直接處理與生成音訊，而非傳統的「語音轉文字 (STT) $\rightarrow$ LLM $\rightarrow$ 文字轉語音 (TTS)」連結方式。這種設計帶來兩個關鍵優勢：
1. 降低整體延遲。
2. 保留語音中的細微情感與語調（nuance）。

📊 **p95 延遲降低至少 25%**

透過改進快取（caching）機制，OpenAI 宣稱所有 Realtime 語音模型的 p95 延遲至少降低了 25%，讓即時對話反應更加迅速。

💡 **推理能力解決「語音代理死寂」問題**

本次更新的核心在於引入「推理 (Reasoning)」能力。模型現在可以在說話前進行內部思考，這對於工具使用（Tool Use / Function Calling）場景至關重要：
- **舊模式**：觸發函式呼叫 $\rightarrow$ 進入靜默期 $\rightarrow$ 使用者誤以為斷線並打斷 $\rightarrow$ 對話狀態混亂。
- **新模式**：推理 $\rightarrow$ 說出前言（例如：「我現在幫您查詢訂單」） $\rightarrow$ 執行函式 $\rightarrow$ 回答。

🎯 **如何選擇適合的模型？**

- **gpt-realtime-2.1**：追求最強的即時推理、工具使用、指令遵循（Instruction Following）以及最完整的語音代理行為。此版本同步提升了字母數字辨識、靜音與噪音處理，以及中斷行為的表現。
- **gpt-realtime-2.1-mini**：追求更快速、更具成本效益的選擇，同樣支援工具使用，可實現「計畫步驟 $\rightarrow$ 呼叫函式 $\rightarrow$ 回答」的流程。

🎯 **實務啟示**

對於開發語音代理的工程師，這次更新意味著可以利用「推理前言」來管理使用者的心理預期。在執行耗時的 API 呼叫前，讓模型先口頭告知動作，能有效降低使用者誤觸中斷的機率，提升對話的流暢度與穩定性。

🔗 **來源**
- 標題：OpenAI Releases GPT-Realtime-2.1 and GPT-Realtime-2.1-mini for Low-Latency Voice Agents in the API
- 作者／機構：Michal Sutter
- 連結：https://www.marktechpost.com/2026/07/06/openai-gpt-realtime-2-1-mini-reasoning-realtime-api/

#OpenAI #RealtimeAPI #VoiceAI #LLM #LowLatency #Reasoning #VoiceAgent #Multimodal #AI #FunctionCalling
