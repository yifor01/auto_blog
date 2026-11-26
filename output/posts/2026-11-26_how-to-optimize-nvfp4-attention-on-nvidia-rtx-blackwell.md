---
title: How to Optimize NVFP4 Attention on NVIDIA RTX Blackwell Through Register Recycling
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/how-to-optimize-nvfp4-attention-on-nvidia-rtx-blackwell-through-register-recycling/
model: claude-code/sonnet
generated_at: '2026-11-26T01:07:40.154313'
score: 95
---

📌 暫存器回收術：替RTX Blackwell上的NVFP4 Attention填滿空檔

TL;DR：NVIDIA展示如何靠切半score tile、回收暫存器，消除SageAttention3在RTX Blackwell上的Tensor Core閒置時間。

在world foundation model這類需要處理長序列的推論任務裡，attention常常是效能瓶頸的罪魁禍首；而這次問題出在一張消費級／工作站GPU用的Tensor Core架構，跟資料中心版完全不同。

🤔 **FlashAttention那套pipeline搬不過來**

在NVIDIA Hopper與Blackwell資料中心GPU上，FlashAttention3與FlashAttention4靠著在thread block內讓矩陣乘加（MMA）運算與softmax互相重疊，拉高attention效能。但這些針對特定硬體設計的pipeline，沒辦法直接套用到NVIDIA RTX PRO 6000 Blackwell系列（SM120）上，因為它用的是不同的Tensor Core架構。文中指出一個關鍵差異：在BF16推論下，像影片生成模型這類工作負載，attention在RTX Blackwell上主要受MMA限制；而在資料中心版Blackwell上，softmax才是forward attention的主要瓶頸。NVFP4的出現帶來硬體加速的4-bit矩陣乘法，理論上能讓Tensor Core吞吐量超越BF16，但要維持高吞吐，softmax、資料搬移與中介儲存之間必須精細協調——這幾個階段的相依性，很容易讓Tensor Core閒置下來。

🧩 **兩級縮放，加上把score tile切成兩半**

Attention的兩個核心矩陣乘法分別是：QKᵀ，由Query與Key算出attention score，供softmax使用；以及PV，把softmax得出的權重拿去跟Value向量相乘，組合出輸出（這裡的P是尚未正規化的softmax權重，最終正規化要等tile間的輸出都累加完才做，做法類似FlashAttention）。SageAttention3是專為SM120設計的原生NVFP4 attention機制，QK與PV兩個矩陣乘法都走NVFP4。它的主要創新是對P做兩級縮放：NVFP4量化會同時產生一個NVFP4資料張量與一個FP8縮放張量，但softmax的輸出被限制在[0,1]這種窄範圍內，直接量化容易浪費NVFP4的動態範圍、造成精度損失；兩級縮放先把數值正規化、充分利用動態範圍，再進行量化。

原本的CTA（cooperative thread array）設計用4個producer warp加8個consumer warp。針對每個N128 tile，consumer依序執行QK、softmax與機率量化、再做PV，整段流程是嚴格序列化的，沒有任何重疊。問題出在兩個地方：一是TMA load綁定在128×128的形狀上，沒用滿就等於浪費頻寬；二是RTX Blackwell的OMMA運算被限制在m16、n8、k64（對應PTX指令mma.sync.aligned.kind::mxf4nvf4.block_scale.scale_vec::4X.m16n8k64），要覆蓋k=128的完整縮併維度，得連續發出兩道k=64的MMA指令。由於MMA是同步執行，發出指令的consumer warp必須等它跑完，才能繼續做online softmax與量化，使得整個迴圈裡出現一大段Tensor Core完全沒有排程工作的空檔，warp都在忙著算softmax、縮放與量化。暫存器資源也很緊張：producer warp用掉3,072個暫存器，consumer warp用掉59,392個，合計62,464個，佔了SM暫存器容量的95.3%，幾乎沒有空間再多放一份score tile。

最佳化後的設計保留一樣的4 producer、8 consumer warp結構，以及完整的N128 K/V tile載入，改變的是consumer計算與儲存attention score的方式：把每個N128 score tile切成兩個N64半邊，各自佔用獨立的暫存器槽。其中一半完成指數運算與量化之後，它的score暫存器就會被回收，拿去計算下一個tile對應那一半的QK，讓下一個tile的QK運算能跟目前tile剩下的softmax、量化與PV運算重疊進行。online softmax的狀態仍然要等完整的N128 score tile都更新完畢，才會被兩個半邊共同消費。這個做法不需要額外配置第二份完整的score tile，就能把Tensor Core原本空出來的時間填起來。

📊 **實際落地：Reactor把它用進正式serving stack**

Reactor，一個提供即時影片、機器人與world model部署與擴展用低延遲基礎設施及API的開發者平臺，將這顆kernel整合進自家正式的serving stack，用來處理真實客戶流量，並表示觀察到顯著的加速效果。

⚠️ **這是為SM120量身打造的方案**

這套設計明確是針對RTX Blackwell工作站卡（SM120）而做，正是因為它的Tensor Core架構和FlashAttention3/4鎖定的資料中心版Hopper／Blackwell不同，才需要另外想一套排程方式；素材中並未提供與BF16或原版SageAttention3之間的具體加速倍率數字。

🎯 **實務啟示**

如果你的推論工作負載跑在RTX Blackwell這類工作站GPU上、且attention是長序列場景下的效能瓶頸，資料中心取向的FlashAttention pipeline未必適用。遇到暫存器吃緊、MMA與softmax之間的相依性卡住Tensor Core排程的情況，「把score tile切半、讓已消費的半邊暫存器立刻被下一個tile回收」是一個不需要額外記憶體、就能提升pipeline重疊度的具體手法，值得在自行開發或移植attention kernel時參考。

🔗 **來源**
- 標題：How to Optimize NVFP4 Attention on NVIDIA RTX Blackwell Through Register Recycling
- 作者／機構：Atharva Joshi／NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/how-to-optimize-nvfp4-attention-on-nvidia-rtx-blackwell-through-register-recycling/

#NVIDIA #Blackwell #NVFP4 #FlashAttention #GPUKernel #Attention #DeepLearning #Inference #SageAttention #CUDA
