---
title: 'NVIDIA Vera Storage Benchmarks: Faster Encryption, Compression, Integrity
  Checking, and Recovery for AI-Native Storage'
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/nvidia-vera-storage-benchmarks-faster-encryption-compression-integrity-checking-and-recovery-for-ai-native-storage/
model: tencent/hy3:free
generated_at: '2026-08-04T08:35:46.896209'
score: 88
---

📌 【NVIDIA 技術解析】解決 AI 時代的儲存瓶頸：Vera 如何加速 Agentic AI 的資料處理

TL;DR：NVIDIA Vera 透過專為儲存設計的架構，在加密、壓縮與完整性檢查等任務上超越 x86 CPU。

🎣 **當 AI Agent 變多，儲存系統成為效能殺手**

在 Agentic AI（代理型 AI）的工作流程中，儲存不再只是靜態的資料庫。當 AI Agent 在檢索企業知識、存取持久記憶、重複使用 KV cache（鍵值快取）或執行工具時，儲存系統必須持續供應並保護這些驅動推理迴圈的資料。

隨著 Agent 的併發量（Concurrency）與 Context Window（上下文視窗）規模不斷擴大，每一次 Agent 步驟都可能觸發多次儲存操作。這些操作包含加密、壓縮、計算校驗碼（Checksums）與冗餘計算（Redundancy）等。若這些處理過程落在 CPU 處理路徑中，處理速度若跟不上 SSD 或網路的速度，就會成為整個加速運算架構的效能瓶頸。

🧩 **Vera 架構：為 AI 工廠打造的儲存處理核心**

為了縮小「儲存處理差距」，NVIDIA 在 BlueField-4 STX 儲存處理器中引入了 Vera CPU。這款架構不僅是為了餵飽 Rubin GPU 而設計，也同時加速了 CPU 端的儲存處理任務。

Vera CPU 的技術規格包含：
- **核心設計**：擁有 88 個 NVIDIA 自研的 Olympus CPU 核心，完全相容於 Armv9.2 指令集，並支援 176 個 Spatial Multithreading 執行緒。
- **高速傳輸**：採用 NVIDIA Scalable Coherency Fabric (SCF)，提供高達 3.4 TB/s 的雙向頻寬（Bisection Bandwidth）與 164 MB 的統一 L3 快取。
- **記憶體子系統**：配備 SOCAMM2 LPDDR5X 記憶體，提供高達 1.2 TB/s 的總體記憶體頻寬，確保在高併發工作負載下，核心仍能獲得穩定的資料供應。

📊 **基準測試結果：Vera 在關鍵儲存原語中全面超越 x86**

透過對比常見的軟體函式庫（如 OpenSSL、Zstandard、LZ4），NVIDIA 在隔離單一處理任務的微基準測試（Microbenchmarks）中發現，Vera 在多項關鍵指標上表現優於傳統 x86 CPU：

- **安全性與完整性**：在加密（Encryption）、解密（Decryption）以及完整性檢查（Integrity Checking）方面表現更佳。
- **資料效率**：在壓縮（Compression）與解壓縮（Decompression）任務上擁有更高的吞吐量。
- **復原能力**：在資料復原（Recovery）與奇偶校驗（Parity）計算上展現更強效能。
- **多階段管線**：在多階段儲存管線（Multi-stage storage pipeline）的測試中，Vera 能同時處理更多併發資料流，且不會導致 CPU 資源、功耗或散熱需求成比例增加。

💡 **深入分析：解決「單核效能」與「頻寬需求」的雙重挑戰**

儲存處理任務對 CPU 有兩種截然不同的需求：
1. **單核持續效能**：在單一資料流中，加密與壓縮必須快速完成，才能進入下一階段處理，這需要強大的單核指令吞吐量。
2. **高頻寬與低延遲**：在系統層級，這些操作需要跨越大量併發流，對記憶體頻寬與可預測的延遲要求極高。

Vera 的 Olympus 核心結合了寬指令吞吐量、先進分支預測、深層亂序執行（Out-of-order execution）以及向量與加密資源，成功同時滿足了這兩項需求，讓儲存軟體在處理高吞吐量資料流時，能保有更多的 CPU 餘裕（Headroom）。

🎯 **實務啟示**

對於建構 AI 原生資料平臺的工程師而言，這意味著：
- **降低基礎設施成本**：透過更高的壓縮吞吐量，可以減少儲存容量與頻寬需求。
- **提升系統韌性**：更快的加密與完整性檢查，能在不犧牲效能的前提下，強化 AI 系統的安全性與資料保護。
- **消除效能瓶頸**：使用專為加速運算設計的處理器，可以確保儲存處理速度能跟上高速 SSD 與網路，避免資料流停滯。

🔗 **來源**
- 標題：NVIDIA Vera Storage Benchmarks: Faster Encryption, Compression, Integrity Checking, and Recovery for AI-Native Storage
- 作者／機構：Elizabeth Goodman @ NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/nvidia-vera-storage-benchmarks-faster-encryption-compression-integrity-checking-and-recovery-for-ai-native-storage/

#NVIDIA #Vera #BlueField4 #AIInfrastructure #Storage #Armv9 #DataCenter #AgenticAI #CloudComputing #HardwareAcceleration
