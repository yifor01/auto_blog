---
title: How Deepgram optimized voice AI at scale with AWS Trainium
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-deepgram-optimized-voice-ai-at-scale-with-aws-trainium/
model: claude-code/sonnet
generated_at: '2026-10-19T21:41:35.566892'
score: 93
---

📌 Deepgram 把語音辨識搬上 AWS Trainium2,每美元多轉錄 11-70% 音訊

TL;DR：Deepgram 與 AWS 合作把 Nova-3 語音辨識模型移植到 Trainium2,批次轉錄場景下每美元能處理的音訊量提升 11% 到 70%。

Deepgram 的語音模型每年要處理數以千兆計（quadrillions）的音訊 token,服務超過 20 萬名開發者與 1,400 個組織。當批次工作量大到這個規模,每一個加速器小時的使用效率,直接決定了能用同一套硬體多服務多少音訊——這正是 Deepgram 找上 AWS、把 Nova-3 搬上 Trainium2 的出發點。

🤔 **從標準 PyTorch 程式碼開始**

這次合作鎖定離線、吞吐量導向的批次場景,例如客服中心分析與醫療逐字稿。Deepgram 原本以標準 PyTorch 程式碼交付 Nova-3,接下來數個月裡,Deepgram 與 AWS Forward Deployed Engineering（FDE）團隊一起把模型重構並移植到 Trainium2 上,針對新硬體進行調校。

🧩 **編譯、kernel 調校、再到 Rust 執行期**

移植工作使用 TorchNeuron（Neuron Compiler 對 PyTorch 的原生整合),先以 eager 模式在 Trainium2 上跑一次,找出哪些運算會 fallback 回 CPU,再用 `torch.compile` 編譯；最終編譯後的版本所有運算都留在 Trainium2 上,沒有偵測到任何 CPU fallback。encoder 與 decoder 被分別編譯成獨立的 static-shape 計算圖。全程都用兩層方式檢查數值正確性：逐層輸出與 CPU 版本比對,以及端到端的 Word Error Rate（WER)必須維持在 Deepgram 的參考水準。

有了這個可運作的基準後,團隊開始用公開的 NKI Library（NKILib)裡的 fused kernel 替換部分層,涵蓋 fused QKV projection、fused feed-forward network 層與 depthwise 1D convolution,目標是最大化吞吐量與成本效益,並掃過 1 到 128 的 batch size 找出吞吐量最高的設定。整個最佳化流程是一個循環：啟用 NKI kernel、用 Neuron Explorer 做 profiling、再依 profiling 結果調整既有 kernel 或換成新寫的 kernel,重複直到達到效能目標；這過程中 Neuron Agentic Development（NAD)工具的 profiling 與 kernel 撰寫能力,協助團隊從 profile 快速定位根因並產出替換用的 kernel。

硬體設定上,每顆 Trainium2 裝置有 8 個實體 NeuronCore,預設以 4 個邏輯 NeuronCore（LNC2)方式呈現。由於單一 Nova-3 模型就能舒適地跑在單一實體核心上,團隊把每個邏輯核心對應的實體核心數降為 1（LNC1),讓單一裝置能同時host 8 個模型複本（DP8),平行處理多路輸入。

🧩 **用 Rust 取代 Python 的資料平行執行期**

由於 Deepgram 的正式服務是用 Rust 寫的,移植不只是編譯模型,還得讓它在沒有 Python、沒有 PyTorch 的服務路徑裡運作。團隊因此打造了一個輕量執行期：Rust 透過一個共用的 work-stealing 佇列（每個模型複本一條執行緒）來協調各個複本,底層再用一個 C 層透過 Neuron Runtime API（`libnrt`)直接載入並執行事先編譯好的 Neuron Executable File Format（NEFF）。這個 Rust 執行期在所有測試過的 batch size 上都精確重現了參考的 token 序列。

📊 **Rust 執行期帶來 7.5% 吞吐量增益,整體每美元多轉錄 11-70% 音訊**

團隊拿這套 Rust 執行期和多執行緒（MT）、多行程（MP)的 Python 資料平行執行期做對比：相較 MP 基準,Rust 完全去除了 Python 直譯器的開銷；相較 MT 基準,則進一步消除了 GIL 造成的序列化問題,讓多個 worker 執行緒的 dispatch 呼叫不再互相卡住。因為 Nova-3 對每個音訊片段都要執行一連串小型的 decoder 呼叫,host 端的 dispatch 在低 batch size 時就是瓶頸,這也是為什麼增益在低 batch size 時最明顯;即便在吞吐量最高的 batch size 設定下,Rust 執行期相較 MP 基準仍帶來 7.5% 的吞吐量提升。

最終,以每美元能處理的音訊量來衡量,單一裝置的 Trainium2 設定（`trn2.3xlarge`)在 Deepgram 的離線、吞吐量導向批次工作負載上,比 Deepgram 原本在用的運算選項多處理了 11% 到 70% 的音訊量（以評估當時的執行個體定價計算)。

🎯 **實務啟示**

這個案例展示了一條完整的最佳化路徑：先確保模型能完全編譯、沒有 CPU fallback,再用現成的 kernel library 快速補上大部分效能缺口,最後才針對 profiling 揪出的瓶頸手寫 kernel;而當服務語言（這裡是 Rust）跟訓練/推論語言（PyTorch）不同時,直接呼叫底層 Runtime API 自建執行期,往往比硬塞一層 Python 橋接更划算。對正在評估加速器選項、且工作負載是離線批次而非即時互動的團隊,這套「TorchNeuron 編譯 → NKI kernel 替換 → profiling 驅動調校 → 原生語言執行期」的流程,是一個值得參考的範本。

🔗 **來源**
- 標題：How Deepgram optimized voice AI at scale with AWS Trainium
- 作者／機構：Pierre Lienhart
- 連結：https://aws.amazon.com/blogs/machine-learning/how-deepgram-optimized-voice-ai-at-scale-with-aws-trainium/

#AWSTrainium #VoiceAI #SpeechToText #MLInfra #Deepgram #ModelOptimization #NeuronSDK #RustProgramming #InferenceOptimization #CloudComputing
