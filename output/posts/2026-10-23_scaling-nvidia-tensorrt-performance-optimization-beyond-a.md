---
title: Scaling NVIDIA TensorRT Performance Optimization Beyond a Single Build Route
  with the Global Performance Tuner, Part 2
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/scaling-nvidia-tensorrt-performance-optimization-beyond-a-single-build-route-with-the-global-performance-tuner-part-2/
model: claude-code/sonnet
generated_at: '2026-10-23T20:42:18.297945'
score: 92
---

📌 TensorRT 的「多條建置路線」：讓編譯器自己挑最快的那條

TL;DR：NVIDIA TensorRT 的 Global Performance Tuner 把編譯最佳化選項變成可搜尋的「build route」，自動在準確度門檻內找出最快的引擎。

同一個模型，用兩種不同的融合策略編譯，效能可能差上一大截，而且沒有一種策略能通吃所有模型。TensorRT 11.1 推出的 Global Performance Tuner，正是為了讓編譯器不再只用單一「預設路線」硬幹到底。

🤔 **排程（scheduling）選擇多，但每次只能選一條路**

這是系列文章的第二篇，延續第一篇對排程問題與數學理論的鋪陳，這篇聚焦在演算法與架構設計本身，並給出實務建議。

🧩 **把每一種最佳化組合，變成一條可搜尋的「build route」**

Global Performance Tuner 的核心設計，是把編譯器裡每一個可調整的設定（稱為 compiler knob，例如某個融合策略、某種程式碼產生路徑）明確列出來，每個 knob 都有有限的可選值與一個預設值。一個「build route」就是一組具體的 knob 數值組合；若不指定任何 route，TensorRT 就會用每個 knob 都取預設值的「預設 build route」。

文章用一個假想的三階段編譯器 f1 → f2 → f3 來說明：假設有一個二元 knob p 控制 f2 的融合策略，p=1 時用水平融合，p=0 時用垂直融合。這兩個值就定義出兩條 build route，對同一個輸入模型 m 會產生兩個候選解。沒有哪一種融合策略是普遍更好的，水平融合可能在某個模型上更快，垂直融合則可能在另一個模型、另一種張量形狀甚至另一款 GPU 上勝出。要知道哪條路線比較好，唯一的辦法就是把兩個候選引擎都建出來，實際比較端到端效能。

要注意的是，knob 組合只是「build route 的規格」，並不等於最終引擎的完整描述——TensorRT 仍會執行其餘的建置階段（例如 tactic selection），並依照網路本身的限制調和各個 knob 的實際取值。TensorRT 對外提供了精簡的 API：一組 setter／getter 用來套用與讀取某一條固定的 build route（C++ 對應 IBuilderConfig::setBuildRoute 與 getBuildRoute），另一個 getter（getAllBuildRoutes）則用來列出所有可調整的 knob、其允許值、預設值與用途，方便開發者自行實作客製化的 tuner。trtexec 中已附帶一個範例實作：使用者給定輸入模型與一個類似 regex 的可調整 build route 運算式，trtexec 會依搜尋演算法把它展開成一串具體的 build route，逐一建置、量測準確度與效能，凡是建置過程崩潰或準確度不合格的路線都會被排除，最後選出實測端到端效能最好的那個引擎。TensorRT 11.1 目前提供超過 200 個可調 knob，而對應的 Python 實作預計在 Torch-TensorRT 2.15 釋出。

📊 **10 個工作負載，實測快了 1.14 到 1.63 倍**

文章提供的 Figure 1 比較了預設 build route（統一標準化為 1.0 倍）與調校後找到的最佳可行路線，在 10 個受測工作負載上，調校帶來的效能提升範圍是 1.14 倍到 1.63 倍。文中強調，不同模型之間的落差正是重點所在：每個模型暴露出的最佳化機會不一樣，單一的預設排程策略注定無法讓每個模型都發揮出最佳效能。

💡 **準確度與效能互相拉扯，怎麼解？**

文章接著用一個思想實驗說明準確度感知（accuracy-aware）調校如何處理「效能—準確度糾纏」問題。假設一個簡單的神經網路模型，有 knob 可以強制某些中間運算改用低精度 kernel，效果等同於在運算之間插入 Q/DQ 節點做量化（注意：TensorRT 11.0 之後已不支援 weakly typed API，所以這類操作本身不再被支援，純粹是思想實驗）。若模型有 4 個可插入 Q/DQ 的位置，各自由一個二元 knob 控制，就會產生 2 的 4 次方、也就是 16 種候選解。效能最好的解，顯然是全部插入量化的那個，但它未必能通過準確度要求；完全不量化的解準確度最好，但效能最差。要在這 16 個候選中間找到「兩者都兼顧」的那個，關鍵在於定義清楚的準確度容忍邊界，而這個邊界必須由使用者提供的準確度指標與黃金資料集（golden dataset）來支撐。Global Performance Tuner 內建一個準確度容忍門檻 ε：當 ε 設為 0，意味著在精確匹配（exact-match）的指標下，候選輸出必須和參考輸出逐位元相同——只要任何一個低精度替換改變了哪怕一個評估輸出，最終唯一合格的解就只剩下完全不做低精度替換的那一個。

⚠️ **目前揭露的仍是單一案例片段**

素材中僅完整呈現了 ε=0 這種最嚴格的情境，其餘容忍門檻下的行為未在本篇摘要中展開，實務上的調校策略還需參考官方文件。

🎯 **實務啟示**

對於需要在多種硬體、多種模型形狀上反覆部署的團隊，Global Performance Tuner 提供的「自動搜尋＋準確度門檻把關」思路，比起人工試驗各種 TensorRT 編譯旗標組合要systematic 得多；尤其是在準備把模型做量化或精度混用時，明確定義好準確度容忍邊界與黃金資料集，會是能不能安全享受效能提升的關鍵前提。

🔗 **來源**
- 標題：Scaling NVIDIA TensorRT Performance Optimization Beyond a Single Build Route with the Global Performance Tuner, Part 2
- 作者／機構：Tanya Lenz, NVIDIA Developer Blog
- 連結：https://developer.nvidia.com/blog/scaling-nvidia-tensorrt-performance-optimization-beyond-a-single-build-route-with-the-global-performance-tuner-part-2/

#NVIDIA #TensorRT #CompilerOptimization #DeepLearning #Quantization #PerformanceTuning #GPU #ModelOptimization #TorchTensorRT #MLOps
