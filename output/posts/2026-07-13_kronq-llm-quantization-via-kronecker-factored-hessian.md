---
title: 'KronQ: LLM Quantization via Kronecker-Factored Hessian'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.07964
score: 88
model: google/gemma-4-31b-it:free
generated_at: '2026-07-13T09:01:37.660908'
---

📌 KronQ：結合 Kronecker‑Hessian 與梯度共變異的 LLM 後訓練量化新框架  

TL;DR：KronQ 透過 Kronecker 分解的 Hessian 與梯度共變異，同時考慮輸入與輸出統計，實現 2‑bit 量化 LLaMA‑3‑70B 時將 perplexity 降至 7.93，顯著優於 GPTQ 系列。

在大語言模型部署時，後訓練量化（PTQ）是唯一不需要再訓練就能壓縮模型的選項。然而，多數第二階 PTQ（如 GPTQ）僅以輸入 activation 統計構建量化目標，等同於假設所有輸出通道對層級重建誤差的貢獻相同，這在高維度模型上往往導致量化品質下降。  

🧩 **KronQ 以 Kronecker‑分解 Hessian 同時引入 activation 與梯度共變異**  
- 透過 Kronecker‑factored Hessian 近似，量化損失同時依賴 **activation covariance**（輸入）與 **gradient covariance**（輸出）。  
- 這樣的雙向依賴使得量化目標能捕捉到「輸入‑輸出」雙向的訊號變異，避免了僅看輸入統計的偏差。

⚙️ **雙向不一致性處理 (Bidirectional Incoherence Processing)**  
- 在現有 PTQ 中，僅在輸入端做隨機旋轉 (random rotation) 以降低權重在輸入維度的方差。  
- KronQ 擴展此做法至 **輸出維度**，使用梯度共變異資訊對權重在輸出方向的變異進行調整，從而同步降低兩側的權重幅度差異。

📊 **新感度指標驅動跨層混合精度配置**  
- KronQ 推匯出基於 **gradient 與 activation Hessian trace** 的感度度量，作為每層選擇量化位寬的依據。  
- 這使得不同層可以根據其對最終損失的敏感度分配不同的位寬，實現更靈活的混合精度佈局。

🎯 **實驗亮點：2‑bit 只量化 LLaMA‑3‑70B**  
- 在 WikiText‑2 測試集上，GPTQ 與 GPTAQ 在 2‑bit weight‑only 量化時出現極端失敗（perplexity 超過 2000），屬於「退化量化」情形。  
- KronQ 則成功將 perplexity 降至 **7.93**，證明在極端低位寬下仍能保持可用的語言模型品質。

💡 深入分析  
- 透過引入梯度共變異，KronQ 能夠捕捉到輸出端的訊號分佈，這在大模型的高維參數空間中特別重要。  
- Kronecker 分解提供了計算上可接受的近似，使得在不增加大量額外開銷的前提下，同時利用兩種統計資訊。

⚠️ 限制與未來方向  
- 文章僅報告了 LLaMA‑3‑70B 的 2‑bit weight‑only 量化結果，未涉及啟用量化或更高位寬的混合配置。  
- 量化流程依賴梯度資訊，需在模型前向傳播後額外儲存梯度統計，對記憶體佈局有一定要求。

🎯 實務啟示  
- 若你正考慮在資源受限的推論環境部署大型 LLM，KronQ 提供了一條在極低位寬仍能保有語言品質的路徑。  
- 在實作時，可先利用現有的 PTQ 工具鏈（如 GPTQ）收集 activation 統計，再額外計算 gradient covariance，依照 KronQ 的感度指標分配層級位寬。

🔗 來源  
- 標題：KronQ: LLM Quantization via Kronecker-Factored Hessian  
- 連結：https://huggingface.co/papers/2607.07964  

#LLM #Quantization #PTQ #KroneckerHessian #ModelCompression #KronQ #MixedPrecision #DeepLearning #AIEngineering #HuggingFaceDailyPapers
