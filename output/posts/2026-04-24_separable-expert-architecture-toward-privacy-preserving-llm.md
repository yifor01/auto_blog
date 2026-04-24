---
title: "Separable Expert Architecture: Toward Privacy-Preserving LLM Personalization via Composable Adapters and Deletable User Proxies"
source: ChatPaper/AI
url: https://arxiv.org/abs/2604.21571
score: 110
model: tencent/hy3-preview:free
generated_at: 2026-04-24T19:33:55.004060
---

📌 【Microsoft AI 最新研究】個人化與可刪除：LLM 隱私的新解耦架構

你以為把使用者資料餵給大模型就能獲得更貼近自己的 AI？研究顯示，只要個人資料進入共享權重，「真正刪除它」幾乎等同於重訓整個模型。

🤔 **當個人化等於把隱私寫進共享權重**

目前的 LLM 個人化做法，往往將使用者資訊直接熔入共享參數。結果是：一旦需要履行被忘記權或移除特定用戶資料，只能選擇成本高昂、幾近不可行的重訓。這種「隱私與個人化綁定在同一組權重」的架構，已成為合規與安全的瓶頸。

🧪 **三層解耦架構與可刪除使用者代理**

本研究提出可分專家架構（Separable Expert Architecture），在 Phi-3.5-mini 與 Llama-3.1-8B 上驗證以下設計：
- 靜態基礎模型作為共享知識核心，不接觸個人資料
- 可組合領域專家 LoRA 適配器，用來塑形行為但不攜帶使用者資訊
- 每使用者代理構件（per-user proxy），承載個人化訊號並可確定性刪除

刪除代理即視同確定性遺忘操作，無需動態權重編輯或重訓。

☁️ **刪除代理後 KL 散度約 0.21 nats，跨用戶污染接近零**

- 代理移除後模型行為回歸基線（KL 約 0.21 nats）
- 遺忘驗證通過率落在 82–89%
- 跨用戶資訊交叉污染近乎零
- 由構造上降低對共享模型的模型反演、成員推論與訓練資料擷取風險

💡 **用可刪除代理隔離個人化，而非將其寫入共享權重**

本研究的核心洞察在於：個人化與共享知識可以且應該分離。當使用者資訊永不入參，忘記操作便從「不可行的權重修正」化約為「刪除代理構件」的確定性命題。這種設計順利相容差分隱私訓練（DP-SGD），讓共享模型在隱私保護下持續改進，而不損及個人化能力。

⚠️ **架構仍依賴代理管理與驗證基礎設施，長期穩定性待觀察**

研究未涉及代理存儲擴展、版本控制或長期部署下的穩定性問題；遺忘驗證雖具備高通過率，但仍依賴後端刪除操作的確實執行。跨任務與長時間跨度的遺忘穩健性，尚待進一步實驗。

🎯 **將遺忘操作轉為 DevOps 流程，並以 LoRA 組合維持彈性**

- 個人化能力可透過可組合 LoRA 適配器疊加與切換
- 忘記操作轉化為代理刪除，適合現有合規與稽核流程
- 可與 DP-SGD 並行運作，兼顾共享模型改進與隱私保證

🔗 **論文連結**  
📝 Separable Expert Architecture: Toward Privacy-Preserving LLM Personalization via Composable Adapters and Deletable User Proxies  
👤 Chris Schneider, Philipp Schoenegger, Ben Bariach @ Microsoft AI  
🔗 https://arxiv.org/abs/2604.21571

你會願意把個人化訊號放在可刪除的代理中，而不是寫進模型權重嗎？歡迎留言討論 👇

#AI #LLM #Privacy #MachineUnlearning #LoRA #MicrosoftAI #DifferentialPrivacy
