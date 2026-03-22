---
title: "HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.08703
score: 128
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-10T23:52:13.613507
---

📌 【HiAR：高效自迴歸長視頻生成的新突破】

當 AI 生成短視頻已經相當成熟，長視頻生成卻面臨一個根本性挑戰：如何保持時間上的連續性，同時避免錯誤累積導致的畫質退化？

🤔 **AI 長視頻生成的核心矛盾**

現有自迴歸擴散模型通常透過高度去噪的上下文來確保時間連續性，但這種做法反而會將預測錯誤以高確定性傳播下去，導致畫質逐漸劣化。這就像用放大鏡看照片，越放大瑕疵越明顯。

🧪 **從雙向去噪模型獲得靈感**

來自中國科學技術大學、香港中文大學、同濟大學和騰訊混元的研究團隊提出了一個反直覺的洞察：我們其實不需要高度乾淨的上下文！他們從雙向去噪模型獲得靈感，發現讓每個幀在相同的噪聲水平下去噪，同時保持一致性，就能提供足夠的時間連續性信號，同時有效緩解錯誤傳播。

💡 **HiAR 的創新分層去噪架構**

HiAR 提出了一種顛覆傳統的生成順序：

傳統做法：逐塊完成 → 每塊依賴高度去噪上下文
HiAR 做法：在每個去噪步驟中，跨所有塊進行因果生成 → 每塊始終依賴相同噪聲水平的上下文

這種分層結構自然地支持管線式平行推斷，在 4 步設定下實現了 1.8 倍的實時加速！

🎯 **解決運動多樣性損失的關鍵技巧**

研究團隊進一步發現，在這種新范式下，自我滾動蒸餾會放大低運動的捷徑。為了解決這個問題，他們引入了一個前向 KL 正則化器（在雙向注意力模式下），這能在不干擾蒸餾損失的情況下，為因果推斷保留運動多樣性。

📊 **VBench 上的領先表現**

在 20 秒視頻生成任務的 VBench 測試中，HiAR 取得了：
- 所有參與方法中的最佳總體得分
- 最低的時間漂移（Temporal Drift）

這意味著生成的視頻不僅畫質優秀，而且時間一致性極佳，不會出現畫面「飄移」或「跳動」的問題。

⚠️ **技術細節與實務考量**

- 採用前向 KL 正則化而非僅依賴 reverse-KL，是保持運動多樣性的關鍵
- 分層去噪架構需要精確的噪聲水平控制
- 管線平行推斷雖然加速，但硬體佈署需支援

🎯 **對開發者的啟示**

這項研究為長視頻生成提供了全新的技術路徑：
- 不再需要等待整個上下文完全去噪
- 可以實現真正的長視頻流式生成
- 在保持畫質的同時大幅提升效率

🔗 **論文連結**
📝 HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising
👤 Kai Zou, Dian Zheng, Hongbo Liu, Tiankai Hang, Bin Liu
🏛️ University of Science and Technology of China; The Chinese University of Hong Kong; Tongji University; Tencent Hunyuan
🔗 arxiv.org/abs/2603.08703

你認為這種分層去噪的方法能應用到哪些實際場景？歡迎分享你的想法 👇

#AI #視頻生成 #機器學習 #計算機視覺 #長視頻 #DiffusionModel #科技創新
