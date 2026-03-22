---
title: "Test-Time Scaling with Diffusion Language Models via Reward-Guided Stitching"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2602.22871
score: 108
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-02-27T23:29:32.868778
---

📌 **【Huawei 最新研究】擴散模型也能推理？用獎勵引導縫合提升 23.8% 準確率**

當我們談論大語言模型的推理能力時，通常會想到多個推理路徑的聚合策略。但傳統方法往往只在**整條路徑層級**做選擇（如選最佳路徑或投票），這會浪費那些「幾乎正確」但中途有瑕疵的嘗試。Huawei London Research Center 提出了全新架構：**Stitching Noisy Diffusion Thoughts**，讓擴散模型也能參與複雜推理。

🤔 **為什麼擴散模型能用來推理？**

擴散模型傳統上用於生成圖片，但最近的研究發現它們也能生成文字。關鍵洞察是：**擴散模型可以快速生成多樣化的低成本推理嘗試**，雖然個別嘗試可能不完美，但其中包含的「步驟級」思考過程是有價值的。

🧪 **獎勵引導縫合的三步驟架構**

1. **多樣探索**：使用 masked diffusion language model 生成多條低成本的推理路徑
2. **步驟評分**：每個中間步驟都用 process reward model (PRM) 評分
3. **縫合重組**：將不同路徑中最高品質的步驟縫合成完整推理，再由 autoregressive solver 計算最終答案

這個設計的巧妙之處在於：**將探索（diffusion）與評估和解決方案合成分離**，避免 monolithic 的統一架構，同時保持廣泛的搜索能力。

 **實驗結果：23.8% 準確率提升，1.8x 延遲降低**

- 在六個數學和編程任務上平均提升 **23.8% 準確率**
- 相比傳統擴散模型 (Dream, LLaDA) 和統一架構 (TiDAR)，延遲降低 **1.8 倍**
- 在更難的問題上效果更顯著，驗證了步驟級重組的價值

💡 **關鍵洞察：步驟級重組 vs. 路徑級選擇**

研究發現，當問題越困難時，**步驟級重組的優勢越明顯**。這是因為複雜問題往往需要將不同嘗試的優點結合起來，而非單純選擇最佳路徑。最終的 autoregressive solver 扮演關鍵角色，將縫合後但仍不完美的推理轉化為準確答案。

⚠️ **訓練免費的模組化設計**

值得注意的是，這個框架是**訓練免費**的，它利用現有的 PRM 和 AR 模型，通過巧妙的組合達到更好的效果。這種模組化設計也更容易整合到現有的推理系統中。

🎯 **實務啟示：測試時擴展的新思路**

這項研究為 test-time scaling（測試時擴展）提供了新思路：不只是生成更多路徑，而是更聰明地重組和利用這些路徑中的有用資訊。對於需要複雜推理的應用場景（如數學、程式設計、科學推理），這種方法可能提供更好的性價比。

🔗 **論文連結**
📝 Test-Time Scaling with Diffusion Language Models via Reward-Guided Stitching
👤 Roy Miles, Aysim Toker, Andreea-Maria Oncescu, Songcen Xu, Jiankang Deng @ Huawei London Research Center; MVP Lab
🔗 論文：arxiv.org/abs/2602.22871
🔗 程式碼：github.com/roymiles/diffusion-stitching

你認為擴散模型未來在推理領域還有哪些應用可能？歡迎留言討論 👇

#AI #擴散模型 #推理 #大語言模型 #Huawei #TestTimeScaling #程式設計 #數學推理
