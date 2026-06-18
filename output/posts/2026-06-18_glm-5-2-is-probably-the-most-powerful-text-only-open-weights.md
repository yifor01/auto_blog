---
title: GLM-5.2 is probably the most powerful text-only open weights LLM
source: Simon Willison
url: https://simonwillison.net/2026/Jun/17/glm-52/
score: 97
model: google/gemma-4-31b-it:free
generated_at: '2026-06-18T20:52:52.786768'
---

📌 【Z.ai 最新發布】753B 參數怪獸 GLM-5.2：目前最強的純文字開源權重模型？

當大多數開源模型在追求「輕量化」與「端側部署」時，中國 AI 實驗室 Z.ai 選擇走極端路線，直接釋出一個 1.51TB 的權重巨獸。

這不只是一個參數規模的競賽，更是在開源社群中罕見地將 753B 級別的 Mixture-of-Experts (MoE) 模型完全開放，這將如何改變我們對開源 LLM 上限的認知？

🤔 **開源權重與封閉權重的權力移轉**

長期以來，頂尖性能的模型（如 GPT-4 或 Claude 3.5）大多被封閉在 API 之後。Z.ai 的這次動作非常激進：GLM-5.2 在 6 月 13 日先提供給訂閱用戶，隨後在 6 月 16 日立即以 MIT 授權（MIT license）公開所有權重。

這意味著工程師與研究者現在可以跳過 API 限制，直接在自有基礎設施上部署、研究並微調這個等級的模型，對於追求數據隱私與高度自定義的企業來說，這是一個巨大的轉折點。

🧪 **753B 參數與 MoE 架構的資源挑戰**

GLM-5.2 的規格堪稱「怪物級別」：
- **總參數量**：753B (7530 億) 參數。
- **權重體積**：高達 1.51TB。
- **架構設計**：採用 Mixture of Experts (MoE) 設計，每次推理僅激活 40B 參數。

這種設計在維持極高模型容量（Capacity）的同時，試圖透過 MoE 降低推理時的計算開銷。但對於部署者而言，1.51TB 的權重意味著極高的 VRAM 門檻，除非擁有頂級的 H100 集群或極其高效的量化方案，否則單機部署幾乎是不可能的任務。

🚀 **上下文窗口從 20 萬暴增至 100 萬**

除了規模，最顯著的進步在於對長文本的處理能力。GLM-5.2 的上下文窗口 (Context Window) 從 GLM-5.1 的 200,000 tokens 提升到了 1,000,000 tokens。

這意味著它能一次處理約 100 萬個 token 的資訊量。對於需要分析超長文檔、整個程式碼庫 (Codebase) 或大規模法律文件的應用場景，這將大幅減少對 RAG (檢索增強生成) 的依賴，讓模型能直接在上下文中處理海量資訊。

⚠️ **純文字導向，視覺能力需依賴獨立模型**

需要注意的是，GLM-5.2 是一個「純文字輸入 (Text-only)」模型。雖然 Z.ai 擁有強大的視覺模型家族（如 GLM-5V-Turbo），但視覺模型目前並未採取開源權重策略。因此，如果你需要多模態能力，仍需透過 Z.ai 的其他產品線，無法單靠 GLM-5.2 完成。

🎯 **工程實踐：部署挑戰與測試方向**

對於 GenAI 工程師，這款模型的到來帶來了幾個實踐方向：
- **量化實驗**：測試 4-bit 或更低精度的量化後，性能下降程度與記憶體需求的平衡點。
- **長文本壓力測試**：驗證 1M token 窗口在實際應用中的「大海撈針 (Needle In A Haystack)」檢索準確率。
- **MoE 效率分析**：研究 40B 激活參數在實際推理時的延遲 (Latency) 與吞吐量。

🔗 **資訊來源**
📝 GLM-5.2 is probably the most powerful text-only open weights LLM
👤 Simon Willison
🔗 文章：https://simonwillison.net/2026/Jun/17/glm-52/

面對這種 1.51TB 的權重巨獸，你會嘗試部署它，還是傾向於使用更輕量的小模型？歡迎在評論區分享你的看法 👇

#AI #LLM #OpenWeights #GLM52 #Zai #MoE #MachineLearning #開源模型
