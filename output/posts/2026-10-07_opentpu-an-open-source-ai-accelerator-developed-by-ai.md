---
title: OpenTPU – An open-source AI accelerator, developed by AI
source: Hacker News
url: https://github.com/FeSens/openTPU
model: claude-code/sonnet
generated_at: '2026-10-07T22:14:29.853580'
score: 113
---

📌 openTPU:讓 AI agent 自己設計、也自己跑在上面的開源推理晶片

TL;DR:一個由 AI agent 設計的開源 AI 加速器,從 SystemVerilog 硬體到編譯器全棧開源,實機跑出與模擬器逐 bit 一致的結果。

AI 能不能設計硬體,這件事討論很久了。但 openTPU 問的問題更進一步:AI agent 設計出來的晶片,能不能拿來跑它自己的 inference?這個專案在 Hacker News 上拿下 334 點、388 則留言,顯然戳到了不少工程師的好奇心。

🤔 **從 auto-arch-tournament 延伸到真實晶片**

openTPU 延續 auto-arch-tournament 的精神,把範圍從軟體架構擴展到 AI 加速器本身。它同時是一個可供學習的專案:整個加速器放在一個小型 monorepo 裡,從頭到尾可讀完,包含硬體設計(SystemVerilog)、指令集(ISA)、逐 bit 精確的模擬器、一套 kernel 語言與其編譯器,以及驅動真實 PCIe 卡的 host 軟體。如果想搞懂一個 AI 加速器怎麼從 Python 裡的一次 matmul 落到實體電路的線路,README 指出這是個不錯的起點。

🧩 **沒有 cache、沒有隱藏排程的簡單機器**

這臺機器刻意做得很簡單:一個 sequencer 每個 cycle 發一個指令給少數幾個單元,DMA 負責搬資料,matrix unit 把從 DRAM 串流進來的 int8 權重做乘法,vector unit 做 fp32 運算,quantizer 把結果轉回 int8。沒有 cache、沒有隱藏排程,每一次資料搬動都是一條指令,因此追蹤執行軌跡能精確看到每個 cycle 花在哪裡。

Kernel 層用一套叫 ol 的語言搭配 @ol.jit 裝飾器撰寫,README 給出的範例示範了如何用它寫一個簡化版的 MLP kernel,透過 load、quantize、dot、all_gather 等算子描述資料流。整個軌跡是:ol 語言與編譯器 → ISA(每條指令 8 個 32-bit word)→ ISA 模擬器與 RTL(逐 bit 一致,由測試驗證)→ Vivado bitstream → FPGA 卡,再透過 PCIe 連到 host,由 otpu-chat、otpu-smi、otpu-lens 等工具操作。

📊 **十個真實模型跑在 Kintex-7 FPGA 卡上,逐 token 比對模擬器**

硬體用的是 Inspur YPCB-00338 卡(Xilinx Kintex-7 xc7k480t,兩個 DDR3 channel),實機輸出與模擬器逐 bit 相同。README 列出的部分效能數據(decode 為device 端量測,DRAM 頻寬為卡上計數器讀值,DDR3-1066 理論峰值 17.1 GB/s):

| 模型 | 權重精度 | Decode(device) | Prefill(device) | DRAM 使用率 |
|---|---|---|---|---|
| LFM2.5-230M | int8 | 59.0 tok/s | 295.6 tok/s | 85% |
| LFM2.5-230M | 4-bit,int8 head | 85.8 tok/s | 335.4 tok/s | 82% |
| Qwen3.5-0.8B | int8 | 17.6 tok/s | 61.4 tok/s | 85% |
| LFM2-2.6B | 4-bit,int8 head | 10.96 tok/s | 20.6 tok/s | 93% |
| SmolLM3-3B | 4-bit,int8 head | 8.74 tok/s | 22.8 tok/s | 92% |

README 說明這是以單一 bitstream(133.33 MHz)搭配四欄 systolic matrix unit 跑完所有模型,解碼速度受限於 DRAM 頻寬,讀取速度落在 DDR3 峰值的 82% 到 94% 之間。與前一代採用 Xilinx MIG、兩欄 matrix unit、120.755 MHz 時脈的 se-cand3 影像相比,decode 效能相差在 2.3% 以內,但 prefill 快了 1.3 到 2.0 倍。

對於超過 4 GiB 卡上記憶體的 MoE 模型,README 描述了一種把專家權重從 host 儲存裝置串流進卡的方案:卡負責路由每個 token 並計算每個專家,host 只在缺少對應專家時把它從 pool file 複製進卡上的插槽。像 Qwen3.5-35B-A3B 這種 34.7B 參數、3.0B active 的模型,實測可達 3.95 tok/s,專家命中率 62%。

💡 **量化換速度,但有可量測的精度代價**

4-bit 權重採用 FP4 數值搭配兩層 block scale,平均每個權重 4.25 bits,LM head 保留 int8 以維持準確度。README 指出這能把每個 token 的傳輸量減少約三分之一,decode 速度提升 40%(Qwen3.5)到 45%(Qwen3、LFM2),但也帶來可量測的 perplexity 代價,具體數字依模型列在文件中。

⚠️ **侵限與門檻**

這終究是一塊 FPGA 卡而非量產晶片,時脈僅 133.33 MHz,效能被 DDR3 記憶體頻寬牢牢卡住;Qwen3.5-4B 的 int8 image 已經超過 4 GiB,更大模型得靠 MoE offload 的方式迂迴處理。對於想直接拿來生產部署的讀者,這仍是一個研究與教學導向的專案。

🎯 **對工程師的意義**

比起效能數字本身,這個專案真正的價值在於它把「一個 matmul 怎麼從 Python 落到電路」的全部中間層都攤開可讀:指令集、模擬器、編譯器、RTL 全部在同一個小型 monorepo 裡逐 bit 對應。對想理解 AI 加速器底層運作,或想評估 agent 在硬體設計上能走多遠的工程師,這是一份值得逐行讀的素材。

🔗 **來源**
- 標題:OpenTPU – An open-source AI accelerator, developed by AI
- 作者／機構:fsbonetto(Hacker News)
- 連結:https://github.com/FeSens/openTPU

#OpenTPU #AIAccelerator #FPGA #HardwareDesign #SystemVerilog #Quantization #Inference #OpenSource #AIAgents #ChipDesign
