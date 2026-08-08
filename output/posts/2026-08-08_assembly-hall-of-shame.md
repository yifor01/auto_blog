---
title: Assembly Hall of Shame
source: Hacker News
url: https://github.com/xoreaxeaxeax/asm-hall-of-shame
model: tencent/hy3:free
generated_at: '2026-08-08T06:55:50.860491'
score: 73
---

📌 【Assembly Hall of Shame】挑戰指令延遲極限：誰是 CPU 單一指令效能的最差紀錄保持者？

TL;DR：這是一個挑戰指令執行延遲下限的專案，透過極端手段讓單一指令耗時數秒。

當工程師討論指令效能時，目標通常是「如何更快」；但在 Assembly Hall of Shame 專案中，目標完全相反：搜尋單一指令效能的「絕對地板」。

🤔 **從效能優化轉向延遲極限挑戰**

通常我們致力於優化程式碼以提升效能，但這個專案透過各種手段，試圖找出哪些指令在最極端的條件下，會導致 CPU 產生最長的等待時間。這不僅是技術上的趣味挑戰，也揭示了硬體架構在處理特定指令時的極端邊界。

🧩 **x86 架構的當代冠軍：利用 PCIe 擁塞製造延遲**

目前 x86 榜單上的冠軍展示了何謂「極致的慢」：

- **策略**：使用 `fxrstor64` 指令從高延遲的 PCIe MMIO 區域載入 512 位元組的 FPU/MMX/XMM 狀態，並同時利用一群核心對另一個高延遲 MMIO 暫存器進行密集的 4 位元組讀取，藉由飽和 PCIe 根複合物 (Root Complex) 與端點 (Endpoint) 的非發送 (non-posted) 交易，讓 `fxrstor64` 必須在擁塞的流量中排隊。
- **測試平臺**：AMD Ryzen 7 5800H
- **🏆 評分**：198,002,498,236 cycles
- **⏱️ 耗時**：62 秒

⚠️ **規則說明**
為了公平比較，該專案制定了嚴格規則：
- 僅限單一指令計分（可進行任何必要的準備工作）。
- 被陷阱 (trapped)、模擬 (emulated) 或虛擬化 (virtualized) 的指令，僅能計算陷阱本身的耗時，而非處理程序 (handler) 的時間。
- 不得使用可中斷的指令（如 `rep movs`、`pause` 等）。
- 所有的時間數據皆根據 CPU 基準時脈進行歸一化。

📊 **x86 榜單節選：從微秒到毫秒的指令延遲**

以下列出部分具有代表性的指令及其延遲表現：

| 排名 | 指令 | 策略摘要 | 耗時 |
| :--- | :--- | :--- | :--- |
| 7 | `in` | 針對映射至 ACPI PM 區塊的 I/O 埠，觸發多次非發送載入 | 3.921 ms |
| 8 | `wbinvd` | 填滿 L1/L2/L3 快取並強制將髒資料寫回 DRAM | 506.165 μs |
| 10 | `rdmsr` | 使用未經文件說明的暫存器 (VIA Eden 處理器) | 202.004 μs |
| 12 | `wrmsr` | 觸發微碼同步 (microcode quiesce) 與硬體單元間的通訊 | 10.742 μs |
| 14 | `cpuid` | 尋找具備最高延遲的 CPUID leaves | 460 ns |
| 17 | `fadd` | 使用次正規化 (subnormal) 運算元觸發浮點微碼輔助 | 249 ns |
| 24 | `idiv` | 使用大於 64 位元除法結果範圍的除法，強迫微碼執行最長路徑 | 28 ns |

🎯 **實務啟示**

透過這項專案，底層工程師可以觀察到硬體在處理極端邊界情況（如次正規化數值、I/O 埠邊界、或 PCIe 擁塞）時的行為。了解這些「最慢指令」的觸發條件，對於開發極高時效性的系統（如即時系統或高效能運算）在進行效能預測與邊界測試時，具有重要的參考價值。

🔗 **來源**
- 標題：Assembly Hall of Shame
- 連結：https://github.com/xoreaxeaxeax/asm-hall-of-shame

#Assembly #x86 #LowLevel #CPU #Microcode #Performance #AMD #Intel #ComputerArchitecture #ComputerScience
