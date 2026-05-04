---
title: "Thinking in Text and Images: Interleaved Vision--Language Reasoning Traces for Long-Horizon Robot Manipulation"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.00438
score: 123
model: tencent/hy3-preview:free
generated_at: 2026-05-04T19:58:00.465906
---

📌 【清華大學 × 小米】文字＋影像交錯：AI 機器人長視程成功率衝上 95.5%

長視程機器操作常因「只看文字邏輯」或「只看當下畫面」而斷線。最新研究顯示，交錯語義與幾何的全域 trace 不僅讓規劃變可解釋，更讓成功率翻倍。

🤔 **長視程機器操作：邏輯要通，位置要準**

從泡一杯咖啡到整理房間，機器人必須同時理解「因果順序」與「空間約束」。現有 VLA 策略往往把規劃藏在潛態，或只開放單一模態：純文字 chain-of-thought 能說明順序，卻抓不到空間；純視覺預測雖有幾何線索，卻常局限於局部、語義不足。結果就是：規劃難以驗證，出錯難以溯因。

🧪 **交錯視覺–語言推理（IVLR）：可緩存、可干擾的 trace 機制**

研究團隊以原生多模態 Transformer 為基礎，提出 Interleaved Vision–Language Reasoning (IVLR)。核心設計是 \trace{}：在完整任務視程內，交替生成文字子目標與視覺關鍵影格，形成全局語義–幾何軌跡。

執行階段分為兩步：
- 先從初始觀察與指令自產 trace 並緩存；
- 再以 trace、原始指令與當前觀察共同條件化閉迴圈動作解碼器。

因標準機器人資料集缺乏此類 trace，研究以示範時段分割加 VLM 標註構建偽監督，確保方法具備落地的可擴展性。

☑️ **LIBERO 平均成功率達 95.5%，長任務衝上 92.4%**

- LIBERO 平均成功率：95.5%
- LIBERO-Long：92.4%
- SimplerEnv-WidowX 綜合成功率：59.4%

消融實驗顯示雙模態的必要性：
- 無 trace：LIBERO-Long 跌至 37.7%
- 文字單模態 trace：62.0%
- 視覺單模態 trace：68.4%
- 完整交錯 trace：92.4%

💡 **文字與影像互補：trace 同時承載「為何」與「在哪」**

交錯結構讓語義子目標拉出因果骨架，視覺關鍵影果則釘住幾何約束。緩存 trace 讓動作解碼器在閉迴圈中不斷對齊「當前在哪、距離哪個子目標還差多少」，同時保留對當前觀察的閉迴圈校正能力。這使長視程規劃既具可解釋性，又不犧牲反應性。

⚠️ **樣本與干擾測試：局部可容錯，全局依賴仍關鍵**

壓力測試包含執行干擾與遮罩 trace 內容，系統呈現中等程度退化，顯示 trace 能容忍局部損壞與執行偏移；但若全局計畫過時或錯誤，整體仍受限。這說明 trace 提升了局部魯棒性，但長視程的正確性終究取決於初始規劃品質。

🎯 **工程啟示：把 trace 當作可讀、可控的中間語言**

- 將 trace 視為可緩存、可檢查的規劃外顯；
- 用 VLM 標註與時段分割建立偽監督，降低 trace 構建成本；
- 閉迴圈動作解碼器保留對當前觀察的校正，避免僵化執行；
- 模態消融作為常規檢查點，確保語義與幾何雙通道健全。

🔗 **論文連結**
📝 Thinking in Text and Images: Interleaved Vision–Language Reasoning Traces for Long-Horizon Robot Manipulation
👤 Jinkun Liu, Haohan Chi, Lingfeng Zhang, Yifan Xie, YuAn Wang  
🏛 Tsinghua University; Beijing Institute of Technology; Xiaomi Group  
🔗 論文：https://arxiv.org/abs/2605.00438

你認為這種「文字＋影像交錯 trace」最可能在哪些實體場景率先落地？歡迎留言討論 👇

#AI #Robotics #MachineLearning #VisionLanguage #長視程操作 #小米 #清華大學
