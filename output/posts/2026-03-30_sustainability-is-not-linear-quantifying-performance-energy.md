---
title: "Sustainability Is Not Linear: Quantifying Performance, Energy, and Privacy Trade-offs in On-Device Intelligence"
source: ChatPaper/AI
url: https://arxiv.org/abs/2603.26603
score: 112
model: gpt-4o-free
generated_at: 2026-03-31T00:26:31.296744
---

📌 【University of Naples Federico II & VU Amsterdam】量化真的能省電嗎？旗艦手機實測揭開對Device‑端LLM的三重權衡

你以為把大語言模型搬到手機上，只要用最新的 importance‑aware 量化就能同時得到更小的記憶體佔用、更低的耗電與不犧牲品質？最新的實測卻告訴我們，事實遠比線性直覺複雜。

🤔 **效能、耗電與隱私不是線性 trade‑off，而是一個多目標的曲面**

隨著 LLMs 從雲端遷移到邊緣裝置，開發者面臨三個硬性限制：手機電池容量、散熱上限以及記憶體容量。理論上，量化技術應該能同時壓縮模型大小與降低能耗，但實際裝置上的測量卻很少見。這篇研究正是要在真實使用條件下，量化這三個指標的具體關係。

🧪 **在 Samsung Galaxy S25 Ultra 上建構免 root 的量測管線，測試 0.5B‑9B 八種模型**

研究團隊設計了一套可重現的實驗流程，不需要 root 權限即可擷取細粒度的功耗、延遲與生成品質數據。他們在旗艦 Android 設備 Samsung Galaxy S25 Ultra 上進行案例研究，涵蓋從 0.5B 到 9B 參數的八種開源 LLM（包括標準混合精度與 importance‑aware 量化版本），以及幾種 Mixture‑of‑Experts (MoE) 架構。所有測量均在相同的基準負載下進行，確保結果反映一般使用者的真實情境。

🚀 **量化‑能耗悖論：重要性感知量化省電效果微乎其微**

- 在相同模型大小下，importance‑aware 量化與標準混合精度的能耗差異幾乎不可測量（在實測誤差範圍內）。
- 這意味著，**對於電池壽命來說，模型的架構（例如層數、注意力頭數）才是決定能耗的主因**，而量化方案的選擇影響有限。
- 因此，僅靠量化來延長續航的期待需要重新檢視。

🔍 **MoE 架構打破大小‑能耗的線性趨勢：用 1B‑2B 的能耗擁有 7B 的儲存容量**

- 研究發現，某些 MoE 模型在參數數量上僅相當於 1B‑2B 模型，但其專家混合機制讓它能儲存與 7B 相當的知識量。
- 在同樣的功耗預算下，這些 MoE 模型在生成品質上表現優於同尺寸的密集模型，且遠低於傳統 7B 模型的能耗。
- 這為在記憶體受限的邊緣裝置上運行較大知識庫的模型提供了可行路徑。

💡 **多目標分析指出：中等規模模型（如 Qwen2.5‑3B）是能耗與品質的實用甜點**

- 透過 Pareto 前線分析，研究團隊指出在效能（延遲）、能耗與生成品質三個維度上，**Qwen2.5‑3B 等 3B 參數左右的模型** 能在不顯著犧牲回覆品質的前提下，提供較低的能耗與良好的延遲表現。
- 對於大多數日常對話或代碼補全場景，這類模型即可滿足需求，同時顯著延長電池續航。

⚠️ **樣本限制：僅單一旗艦設備、短時間基準測試、未涵蓋所有量化方法**

- 實驗僅在 Samsung Galaxy S25 Ultra 上進行，不同廠商或較舊機型的結果可能有所差異。
- 能耗測量基於固定的基準負載，長期使用中的熱節流與電池老化效應未被捕捉。
- 雖然涵蓋了 importance‑aware 與標準混合精度量化，但未測試極端低位元（如 2‑bit）或新興的 sparsity 技術。

🎯 **實務啟示：選模型時先看架構，再考慮量化；MoE 與中等規模模型值得優先評估**

- 若目標是延長電池續航，優先評估模型的結構設計（層數、注意力寬度）而非 soltanto 追求更激進的量化。
- 對於記憶體受限但願意犧牲少量峰值功耗的場景，MoE 架構提供了「小模型能耗、大模型知識」的折衷方案。
- 在需要平衡回覆品質與能耗的產品中，可先試用 Qwen2.5‑3B 等中等規模模型，再根據實測功耗微調。

🔗 **論文連結**
📝 Sustainability Is Not Linear: Quantifying Performance, Energy, and Privacy Trade-offs in On-Device Intelligence  👤 Eziyo Ehsani, Luca Giamattei, Ivano Malavolta, Roberto Pietrantuono (University of Naples Federico II; Vrije Universiteit Amsterdam)  
🔗 https://arxiv.org/abs/2603.26603  

你的手機端 AI 部署策略是否已考慮到這些非線性的 trade‑off？歡迎在留言區分享你的經驗與觀察 👇

#AI #OnDeviceLLM #EdgeAI #Quantization #MoE #BatteryLife #SamsungGalaxyS25 #UniversityOfNaples #VUAmsterdam #MachineLearning #AIResearch
