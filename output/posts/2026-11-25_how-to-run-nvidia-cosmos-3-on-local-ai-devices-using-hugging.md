---
title: How to Run NVIDIA Cosmos 3 on Local AI Devices Using Hugging Face Diffusers
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/how-to-run-nvidia-cosmos-3-on-local-ai-devices-using-hugging-face-diffusers/
model: claude-code/sonnet
generated_at: '2026-11-25T01:45:12.984891'
score: 95
---

📌 12GB顯卡也能跑？NVIDIA Cosmos 3 Nano本機生成教學

TL;DR：用記憶體offloading技巧，讓12GB VRAM顯卡也能跑Cosmos 3 Nano影片生成模型。

影片生成模型動輒需要數十GB的GPU記憶體，一般工程師手上的消費級顯卡常常連載入權重都不夠。NVIDIA這篇教學給出一個務實解法：把大部分模型權重先放進系統RAM，用到哪個部分才搬到GPU上運算。

🤔 **影片生成模型的老問題：權重比VRAM還大**

NVIDIA Cosmos 3 Nano是支援物理AI（physical AI）開發的世界基礎模型（world foundation model），可以從文字、圖片等輸入生成影片。問題是，模型權重與推論過程中的中間資料一旦超過GPU可用記憶體，就無法在小顯卡上執行。這篇教學示範如何用Hugging Face Diffusers搭配NVIDIA的standalone offloading套件，讓生成作業可以在低至12GB VRAM的GPU上進行。

🧩 **把權重當成「借」的：系統RAM當後備儲存**

這套方案建立在Diffusers原生的group offloading機制之上，核心邏輯是用系統RAM作為權重的後備儲存，執行時依序把需要的transformer區塊搬上GPU：

- 目前用不到的checkpoint權重（BF16或checkpoint本身的FP8格式）留在系統RAM。
- 需要用到的下一個transformer區塊才被搬到GPU。
- 所有矩陣乘法與attention運算都在CUDA上執行。
- adapter另外管理denoising、負責影片編解碼的VAE，以及安全檢查三個階段各自的記憶體需求。

Cosmos 3的transformer內部分成兩條路徑：理解（understanding）路徑負責解讀prompt與其他條件輸入，這部分在生成過程中維持不變；生成（generation）路徑則在每一步denoising時處理不斷演化中的影片、聲音或動作表徵，同時引用理解路徑算出的結果作為上下文。由於條件輸入與精度固定，adapter只需算一次理解上下文,之後重複使用，不必每步重算；若FP8精度在denoising過程中改變，才會重新整理這個上下文。

以一次35步denoising、36個transformer區塊（索引0到35）的請求為例：每一步denoising都會依序走完全部36個區塊，走完第35個區塊後，scheduler更新生成狀態，下一步再從區塊0開始，直到最後一步結束才進入VAE解碼。另外，Hugging Face的classifier-free guidance（CFG）需要同時算「有prompt」與「沒有prompt」兩種預測，adapter讓這兩種預測共用同一次搬上GPU的區塊，而不是為每個分支各搬一次權重，省下重複傳輸的成本。當GPU記憶體還有餘裕時，下一個區塊甚至可以提前開始搬運，和目前區塊的運算同時進行；遇到更吃記憶體的請求（例如12GB GPU上的720p Transfer模態），則自動切換到更保守的低記憶體排程，使用者不需要自己調參數。

整個pipeline仍沿用Diffusers官方的modular pipeline處理prompt、條件與latent準備、denoising迴圈與UniPC scheduler、遮罩與CFG輸出、VAE解碼、安全檢查與輸出轉換，offloading adapter只負責在這些既有環節之間插入記憶體管理邏輯。

🎯 **動手跑一次：從git clone到輸出MP4**

教學的安裝與使用流程相當直接：

```
git clone https://github.com/NVIDIA/cosmos-framework.git
cd cosmos-framework/packages/diffusers-cpu-offloading
uv pip install '.[benchmarks]'
```

接著把Hugging Face repository ID直接丟給`build_pipeline`，搭配`StreamingConfig`指定device，第一次載入會下載checkpoint，之後則重複使用快取檔案。預設設定會自動選擇合適的省記憶體行為，起手式是BF16精度搭配PyTorch的scaled dot-product attention（SDPA），這也是NVIDIA在四張受測GPU上都使用的基準設定。文章示範以189張畫面、720p、24fps、35步denoising生成一段「廚房裡的機械手臂」影片，若要在12GB GPU上加快疊代速度，可以把解析度降到480×848或240×432。生成完成後用`diffusers.utils.export_to_video`存成MP4即可。文章也提到可以進一步換上FP8 checkpoint，再降低記憶體需求。

⚠️ **這不是免費午餐：犧牲延遲換記憶體**

這個方法的代價很清楚：換取較小的GPU記憶體需求，必須付出更多系統RAM用量與PCIe傳輸頻寬。文章特別強調這不提供互動式延遲，也不是直接從硬碟串流權重做推論。測試用的消費級GPU主機約有128GB系統RAM，但文章說明這並非經過量測的最低需求，實際可行的下限仍待使用者自行驗證。

🎯 **實務啟示**

對沒有多張A100或H100、只有消費級顯卡的工程師來說，這提供了一條在本機驗證世界基礎模型的務實路徑：先用小解析度快速疊代prompt與參數，再視需要切換到FP8 checkpoint或更高解析度做最終輸出。但如果專案目標是低延遲、互動式的生成服務，這套CPU offloading方案並不適用，仍須評估足夠的GPU記憶體或雲端資源。

🔗 **來源**
- 標題：How to Run NVIDIA Cosmos 3 on Local AI Devices Using Hugging Face Diffusers
- 作者／機構：Atharva Joshi, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/how-to-run-nvidia-cosmos-3-on-local-ai-devices-using-hugging-face-diffusers/

#NVIDIA #Cosmos3 #DiffusionModels #VideoGeneration #HuggingFace #Diffusers #PhysicalAI #GPUMemory #WorldModel #LocalInference
