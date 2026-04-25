---
title: "tile-ai/tilelang"
source: GitHub Trending
url: https://github.com/tile-ai/tilelang
score: 104
model: tencent/hy3-preview:free
generated_at: 2026-04-25T19:10:27.180525
---

📌 【tile-ai 專案】寫 GPU Kernel 像寫 Python：TVM 背後的 DSL 升級實驗

你以為高階語言寫 AI 加速只能靠算子庫？最新開源專案試圖打破這個假設：用類 Python 語法描述 FlashAttention、量化解碼 GEMM，還能直接對應到硬體底層，效能不輸手寫 CUDA。這聽起來像魔法，卻已經跑在昇昇、Metal 與 NVIDIA 硬體上。

🤔 **高階抽象不一定要犧牲低階效能**

開發 GPU/CPU 核心（尤其是 GEMM、Dequant GEMM、FlashAttention、LinearAttention）長期面對同一個張力：生產力與效能的拔河。高度最佳化的 kernel 往往牽涉大量底層微架構知識，維護成本極高；而純高階描述又難以精準控制資料流與排程。TileLang 的出現，正是嘗試在這條緊繃上找出一個可擴充的中間點。

🧪 **Pythonic DSL + TVM 基礎設施的整合設計**

TileLang 並不是全新重寫的編譯器，而是以 TVM 為底層基礎的領域專用語言（DSL）。它提供接近 Python 的語法來描述「磚狀」計算與排程，讓開發者專注於計算模式與資料切塊邏輯，而將低階最佳化交由 TVM 的編譯基礎設施處理。

近期擴充顯示其跨平台野心：
- 12/18/2025：新增 CuTeDSL 後端，可編譯至 NVIDIA CUTLASS CuTe DSL
- 09/29/2025：支援昇昇 AscendC 與 Ascend NPU IR，涵蓋 ascendc_pto 與 npuir 分支
- 10/07/2025：Apple Metal Device 裝置支援就緒
- 12/17/2025：整合 Z3 定理證明器至 TVM Arith Analyzer，引入 SMT 基礎的符號推理與自動正確性驗證
- 10/31/2025：遷移至 apache-tvm-ffi，降低 CPU 端開銷

這些擴充顯示其目標不只於單一加速器，而是試圖在多硬體生態中建立可攜的效能表達方式。

⚡ **用類 Python 語法實作 FlashAttention、量化解碼 GEMM 並非原罪**

TileLang 的核心承諾是：開發者可以用較高階的抽象描述計算磚塊與排程原則，編譯器負責產生具備狀態化分割、記憶體階層排程與向量化細節的程式碼。這在密集推理與訓練核心（如 FlashAttention 類型計算、量化解碼 GEMM）中特別具備實務意義，因為這些運算同時牽涉資料重用、精度轉換與高吞吐排程。

與純手寫 CUDA 相比，TileLang 的優勢不在於「絕對最高時脈」，而在於「達到足夠高時脈的可維護成本」。當模型結構快速演進，算子需求頻繁變動時，這種抽象層的彈性往往比微觀最佳化更具長期價值。

💡 **抽象層的選擇決定了最佳化的天花板與地板**

TileLang 的設計本質上是一種受控的權力讓渡：開發者放棄部分微架構控制權，以換取跨硬體的可攜性與生產力；編譯器則承擔將高階描述轉譯為具體排程的責任。這種權衡在多後端支援（昇昇、Metal、CUTLASS）中被具體化：同一段 TileLang 描述，可以依賴不同後端產生不同風格的加速程式碼。

更重要的是，SMT 驗證能力的引入試圖解決一個長期痛點：高階排程轉換是否會破壞數值正確性？透過 Z3 驗證的符號推理，開發者可以在編譯期而非測試期捕捉特定類型的邏輯衝突，這對於金融級或安全關鍵場景中的推論部署具有實質意義。

⚠️ **專案仍在快速演進，長期穩定性與跨卡型效能均勻性尚未經過大規模驗證**

TileLang 的限制同樣明顯：
- 專案處於活躍迭代期，API 與後端支援可能頻繁變動
- 跨硬體的效能均勻性（特別是昇昇、Metal 與 CUDA 之間的效能對齊）尚未有公開的全面基準
- SMT 驗證目前多限於算術層次的性質，難以覆蓋完整的數值穩定性與邊界條件
- 依賴 TVM 基礎設施的成熟度，當 TVM 層面發生較大變動時，DSL 的升級成本可能增加

這意味在目前階段，TileLang 更適合用於原型設計、特定熱點算子的快速迭代，或作為多硬體探索的基礎框架，而非直接替換經過多年打磨的產業級算子庫。

🛠️ **適合用於多硬體探索與中長期算子演進，但不建議即時上線核心直接替換**

對工程團隊而言，TileLang 的實務啟示在於：
- 當你的模型結構變更頻繁，且需要在多平台（昇昇、Metal、CUDA）維持合理效能時，可考慮以 TileLang 作為中間表示層進行快速驗證
- 對於 FlashAttention、量化解碼 GEMM 等熱門模式，可先用 TileLang 產生參考實作，再依實際硬體進行局部微調
- 利用內建的 SMT 驗證能力，可在 CI 中加入特定算術性質的自動檢查，減少數值錯誤的潛在風險
- 密切跟蹤 CuTeDSL 與 TVM ffi 的整合進度，這將直接影響未來與現有 CUDA 開發流程的相容性

🔗 **論文連結**
📝 tile-ai/tilelang
👤 tile-ai
🔗 https://github.com/tile-ai/tilelang

你的團隊在多硬體 AI 加速上，遇到過哪些「想寫高階但被迫手寫 CUDA」的困境？歡迎分享你的經驗 👇

#AI #GPU #Kernel #TVM #DSL #FlashAttention #GPGPU #tilelang #多硬體AI
