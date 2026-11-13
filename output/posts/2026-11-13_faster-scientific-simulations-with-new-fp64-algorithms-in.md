---
title: Faster Scientific Simulations with New FP64 Algorithms in NVIDIA cuBLAS
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/faster-scientific-simulations-with-new-fp64-algorithms-in-nvidia-cublas/
model: claude-code/sonnet
generated_at: '2026-11-13T22:56:40.925116'
score: 80
---

📌 cuBLAS 新演算法讓 FP64 矩陣乘法跑在整數 Tensor Core 上

TL;DR：NVIDIA cuBLAS 用 Ozaki-II 與 2M 演算法，讓 DGEMM/ZGEMM 在不犧牲精度下大幅加速。

科學模擬最燒時間的地方,往往不是演算法邏輯本身,而是最基礎的雙精度矩陣乘法。量子化學、材料科學的模擬,大部分執行時間都花在 DGEMM（real 64-bit 矩陣乘法）與 ZGEMM（complex 64-bit 矩陣乘法）上。問題是,FP64 硬體的運算速度,遠遠跟不上低精度 Tensor Core 的進展速度。NVIDIA 在 CUDA Toolkit 13.4.2 的 cuBLAS 更新,試圖打破「精度」與「速度」只能二選一的局面。

🤔 **FP64 速度被低精度硬體甩在後面**

近年低精度硬體（如整數 Tensor Core）進展飛快,促使業界探索一類新演算法：把雙精度數字拆解成多個整數片段,放到更快的整數 Tensor Core 上做乘法,再把結果精確重組回完整的雙精度數值。這個思路建立在先前 cuBLAS 提出的 Automatic Dynamic Precision（ADP）框架之上,該框架會把 FP64 運算映射到整數 Tensor Core,同時保留原生 FP64 的精度水準。

🧩 **Ozaki-I 到 Ozaki-II：用中國剩餘定理省掉一半運算**

Ozaki-I 與 Ozaki-II 共用同一個第一步：將輸入矩陣的指數對齊,轉換成共享指數、可變長度的整數表示,讓乘積可以在整數 Tensor Core 上精確累加。兩者的差異在於「大整數乘法」怎麼做。

Ozaki-I 把每個大整數切成 8-bit 的片段,再用三角形模式把 A 的片段與 B 的片段相乘,因此所需的 Tensor Core GEMM 數量會隨片段數量的平方增長。Ozaki-II 則採用基於中國剩餘定理（Chinese Remainder Theorem, CRT）的更快大整數乘法：把量化後的運算元對一組互質的小整數取模,每個模數只做一次整數 GEMM,再從餘數還原出精確乘積。這讓 GEMM 數量隨模數數量線性增長,而不是像 Ozaki-I 那樣呈平方成長。在要求匹配 FP64 精度的情況下,Ozaki-I 所需的 Tensor Core GEMM 數量大約是 Ozaki-II 的兩倍。

為了同時解決 ZGEMM（複數矩陣乘法）的效能問題,cuBLAS 也引入了 2M 演算法,把一次複數矩陣乘法從原本的四次實數乘法,縮減為兩次。cuBLAS 會以 heuristics 自動在 Ozaki-I 與 Ozaki-II 之間選擇最佳方案,整數寬度則由 ADP 在執行時動態決定,使用者也可以手動指定。若執行時所需的 mantissa bits 超過預設或使用者設定的上限,cuBLAS 會自動退回原生 FP64 MMA 指令的路徑,確保正式環境使用時的數值精度無虞。

📊 **DGEMM 快上 5.5 倍,應用端實測也跟著加速**

cuBLAS 在 CUDA Toolkit 13.4.2 公布的效能數據包括：
- DGEMM 搭配 Ozaki-II,在 NVIDIA VR NVL72 與 GB200 上分別比原生 FP64 快 5.5 倍與 3.9 倍;在 GB200 上也比 Ozaki-I 快 2 倍。
- 量子化學中的 CCSD（coupled cluster singles and doubles）案例,使用 Ozaki-II DGEMM 在 VR NVL72 與 GB200 上分別達到 2 倍與 1.4 倍的端到端加速（全 FP64 精度）;若採用特定領域的混合精度模式,加速幅度可達 5 倍與 3.5 倍。
- ZGEMM 搭配 2M 演算法,在 GB200 上比原生 Complex FP64 快 5 倍;材料科學案例 BerkeleyGW 在 VR NVL72 與 GB200 上分別達到 6.6 倍與 3.9 倍加速。
- DGEMM 搭配 Ozaki-II 在 VR NVL72、GB200、RTX PRO 6000 上分別達到最高 175、147、37 TFLOPS。

在 CCSD 的實測中,以 cc-pVTZ 基底組計算 S22 資料庫中五個中型分子系統（24-28 個原子,約 590-630 個原子軌域）,Ozaki-II DGEMM 在全 FP64 精度下讓效能隨世代單調提升,Rubin 相對 A100 總計加速 4.7 倍;若採用 32-bit mantissa 的混合精度模式,總加速可達 11.5 倍,且 CCSD 相關能量誤差小於 10^-14 Eh,與原生 FP64 結果幾乎無法區分。

💡 **Rubin 架構加入專用數字格式**

NVIDIA Rubin 架構引入了新的數字格式 TI16（12-bit 整數,sign-magnitude 表示,範圍 [-2047, +2047]）,專門用來加速 Ozaki 系列的運算。cuBLAS 13.4 透過 tcgen05.mma 指令,在 Rubin GPU（compute capability 10.7）上以 TI16 格式加速 Ozaki-I 與 Ozaki-II 的計算。

⚠️ **記憶體用量需要特別處理**

由於 Ozaki-II 每個模數都要materialize 一對餘數,若實作方式天真,工作空間（workspace）會比 Ozaki-I 大得多。cuBLAS 的做法是沿用先前 CTK 13.3 為 Ozaki-I 引入的節省記憶體的 tiling 策略,每做完一次 GEMM 就立即丟棄對應的餘數對,讓工作空間維持在可管理的範圍。

🎯 **對 HPC 開發者而言不用改一行程式碼**

cuBLAS 會自動對 DGEMM 與 ZGEMM 套用加速,應用程式端完全不需要修改程式碼。對仰賴高精度矩陣運算的量子化學、材料科學等模擬工作而言,這代表只要升級 CUDA Toolkit,就有機會在既有硬體上直接拿到顯著的效能提升,同時保留 FP64 等級的精度保證。

🔗 **來源**
- 標題：Faster Scientific Simulations with New FP64 Algorithms in NVIDIA cuBLAS
- 作者／機構：Cole Brower @ NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/faster-scientific-simulations-with-new-fp64-algorithms-in-nvidia-cublas/

#NVIDIA #cuBLAS #HPC #GPU #FP64 #TensorCore #QuantumChemistry #ScientificComputing #CUDA #LinearAlgebra
