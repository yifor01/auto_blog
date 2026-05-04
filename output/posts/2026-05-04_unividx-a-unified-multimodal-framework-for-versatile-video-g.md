---
title: "UniVidX: A Unified Multimodal Framework for Versatile Video Generation via Diffusion Priors"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.00658
score: 128
model: tencent/hy3-preview:free
generated_at: 2026-05-04T19:55:41.110972
---

📌 UniVidX：打破「一任務一模型」，用 Diffusion 統一多模態視訊生成

過去要同時生成 RGBA 圖層與光影屬性，往往得為每種輸入–輸出對應訓練一組專屬模型；UniVidX 試圖告訴我們：視訊 Diffusion 的先驗本身已經足夠，只要用對框架，一組模型就能同時「聽懂」多種模態。

🤔 **多模態視訊生成長年被「固定映射」綁架**

近期研究證明，Video Diffusion Models (VDMs) 不僅能生成逼真視訊，還可以被挪用來處理多樣的圖形任務。但現有做法多半為「每個問題設定訓練一組模型」，這讓輸入–輸出映射被固定下來，跨模態的相關性難以被共同建模。結果就是：模型數量膨脹、知識無法共享、泛化受限。

🧪 **SCM + DGL + CMSA，讓一組 VDM 自由切換多模態任務**

研究團隊提出 UniVidX，將像素對齊任務統一視為「在共享多模態空間中的條件式生成」。核心設計包含三項機制：

- Stochastic Condition Masking (SCM)：訓練時隨機將模態劃分為「乾淨條件」與「含噪目標」，打破固定映射，實現全向條件生成。  
- Decoupled Gated LoRA (DGL)：為每種模態引入獨立 LoRA，僅在該模態作為生成目標時啟用，以此保留 VDM 主幹的強先驗。  
- Cross-Modal Self-Attention (CMSA)：跨模態共享 Key/Value、保留模態專屬 Query，促成資訊交換與模態間對齊。

實作上，團隊以兩個實例展現通用性：

- UniVid-Intrinsic：處理 RGB 視訊與內在屬性（albedo、irradiance、normal）。  
- UniVid-Alpha：處理前景–背景分離，生成混合 RGB 視訊及其對應 RGBA 層。

⚡ **不到 1,000 條視訊訓練，仍具備跨任務競爭力**

- 在各自任務上，兩個模型表現與當下 State-of-the-Art 相當。  
- 即使僅使用少於 1,000 條視訊訓練，模型在 in-the-wild 情境下仍展現穩健泛化。  
- 同一框架支援「生成、條件合成、分解」等多種模式，無需為新任務重新設計整體架構。

💡 **不是取代先驗，而是用條件機制重用先驗**

UniVidX 的關鍵並非拋棄 VDM 先驗，而是透過模態感知機制讓先驗「可重用、可切換」。SCM 打破訓練時的單向依賴，DGL 防止多任務干擾削弱生成品質，CMSA 則確保跨模態資訊在不混肴的前提下流通。這套設計讓多模態視訊生成從「拼裝式模型庫」邁向「統一生成空間」。

⚠️ **目前仍以 2D 為主，長期一致與動態場景待探索**

- 雖然支援多模態，但主要基於 2D 視訊空間，尚未明確針對長視距時間一致性或動態場景做最優化。  
- 極端條件或高頻細節的跨模態重建，仍可能受到訓練資料規模與分佈影響。  
- 與顯式 3D/場景表示的結合深度有限，延續工作需要額外幾何先驗或推論機制。

🎯 **工程實務：少即是多，條件控制比重新訓練更可擴展**

- 對於內容創作與 3D/AR 場景建構，可直接以 UniVidX 架構實現「單一模型、多元控制」的工作流程。  
- 條件掩蔽與模態專屬 LoRA 的設計，讓下游應用能輕鬆插入自定義模態，不需要完整重訂 VDM 主幹。  
- 少數據泛化能力適合長尾場景，讓小規模數據集也能獲得可控的視訊生成品質。

🔗 **論文連結**  
📝 UniVidX: A Unified Multimodal Framework for Versatile Video Generation via Diffusion Priors  
👤 Houyuan Chen, Hong Li, Xianghao Kong, Tianrui Zhu, Shaocong Xu (MMLab@HKUST, Beihang, Nanjing, BAAI, MMLab@CUHK, CUHK-Shenzhen, Stanford, Tsinghua)  
🔗 https://arxiv.org/abs/2605.00658  
🌐 Project page: https://houyuanchen111.github.io/UniVidX.github.io/

你會如何把這種「多模態統一生成」的能力，應用在 Agent 感知或 AR 內容生產流程中？欢迎留言討論 👇

#AI #VideoGeneration #Multimodal #Diffusion #UniVidX #DeepLearning #GenerativeAI
