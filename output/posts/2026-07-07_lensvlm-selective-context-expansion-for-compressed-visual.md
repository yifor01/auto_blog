---
title: 'LensVLM: Selective Context Expansion for Compressed Visual Representation
  of Text'
source: Apple ML
url: https://machinelearning.apple.com/research/lensvlm-context-expansion
score: 100
model: google/gemma-4-31b-it:free
generated_at: '2026-07-07T21:07:44.610622'
---

📌 LensVLM：以選擇性展開提升壓縮文字影像的視覺語言模型效能  

TL;DR：LensVLM 讓 VLM 在 4.3× 壓縮下仍保持與完整文字相同的準確度，最高可達 10.1× 壓縮優於其他壓縮基線。

🎣 開場  
想直接把文字渲染成圖片讓視覺語言模型（VLM）處理，聽起來可以省去繁雜的斷詞與長序列問題；但當文字被壓縮到一定程度，字元會變得太小，模型幾乎無法辨識，精度立刻崩潰。LensVLM 提出「只在需要的地方」把壓縮影像還原成高解析度，成功在極高壓縮率下仍保有原始文字的辨識能力。

🤔 為何需要選擇性展開？

- VLM 的影像編碼器只能接受固定大小的視覺 token，渲染解析度成為「壓縮旋鈕」：解析度越低，視覺 token 越少，計算與記憶體需求越小。  
- 當文字縮小到視覺編碼器的有效解析度以下時，字元變得模糊，模型只能靠噪聲猜測，導致準確度急速下降。  
- 直接使用高解析度影像則失去壓縮帶來的效能好處，特別是在資源受限的推論環境中不實用。

🧩 LensVLM 的核心方法  

1. **壓縮影像掃描**：先以低解析度渲染整段文字，送入 VLM 進行快速推論。  
2. **相關區域偵測**：模型內建的學習工具會判斷哪些視覺 token 可能包含關鍵資訊（例如問答中的關鍵詞或程式碼片段）。  
3. **選擇性展開**：只對被標記為「相關」的區塊重新渲染為未壓縮的高解析度影像，再次送入 VLM 進行精細閱讀。  
4. **後訓練食譜**：在 Qwen3.5-9B-Base 基礎上進行微調，使模型能在不同壓縮設定下仍保持穩定表現，並學會在高壓縮情況下更依賴展開的內容。

📊 成效與比較  

| 基線型別 | 最大壓縮倍率 | 在七項文字 QA 基準測試的相對準確度 |
|----------|--------------|-----------------------------------|
| 完整文字（上限） | 1× | 100%（基準） |
| LensVLM | 4.3× | 與完整文字相當 |
| 其他檢索式、文字壓縮、視覺壓縮基線 | 最高 10.1× | 劣於 LensVLM，差距隨壓縮率增加而擴大 |

- 在多模態檔案與程式碼理解任務上，LensVLM 的準確度提升幅度隨壓縮率上升而更明顯。  
- 分析顯示，模型在高壓縮下會更依賴展開的高解析度內容，而非僅靠模糊的視覺閱讀。

💡 深入分析  

- **訓練穩健性**：研究指出，透過後訓練，模型對渲染方式的選擇變得不敏感，換句話說即使使用不同的字型或排版，壓縮後的表現仍保持穩定。  
- **工具選擇指引**：實驗發現，對於純文字渲染，使用「文字展開」工具最有效；若處理的是原生檔案（如 PDF）且版面資訊對任務重要，則「高解析度影像展開」更適合。

⚠️ 限制  

- 文章僅說明了在 Qwen3.5-9B-Base 上的實驗結果，未提供其他模型或規模的驗證。  
- 具體的展開判斷模型與工具實作細節在摘要中未揭露，讀者若要自行復現仍需參考完整論文或原始程式碼。

🎯 實務啟示  

- **資源受限的推論服務**：可先以低解析度渲染文字，大幅降低 GPU 記憶體與計算需求；只有在模型指示需要時才觸發高解析度展開，兼顧速度與精度。  
- **多模態檔案處理**：在檔案檢索或程式碼說明的場景，使用 LensVLM 可在不犧牲準確度的前提下，減少傳輸與儲存成本。  
- **未來整合**：開發者可將 LensVLM 的選擇性展開邏輯封裝為前置服務，與現有 VLM API 串接，實現「先粗後精」的推論流程。

🔗 來源  
- 標題：LensVLM: Selective Context Expansion for Compressed Visual Representation of Text  
- 連結：https://machinelearning.apple.com/research/lensvlm-context-expansion  

#VisionLanguageModel #Compression #SelectiveExpansion #AIInference #MultimodalAI #TextUnderstanding #AppleML #Qwen #DocumentAI #CodeUnderstanding
