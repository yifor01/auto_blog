---
title: "LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.08083
score: 118
model: tencent/hy3-preview:free
generated_at: 2026-05-11T20:21:27.026612
---

📌 **UMD、UVA、WUSTL、UNC、Google、Meta 聯手提出：AutoTTS —  — 讓 LLM 自動尋找更好的推理時間擴展策略**

你以為手動調整「思考鏈」幅度、深度就是提升 LLM 推理效果的唯一方法？研究顯示，這種靠經驗打磨的啟發式其實留下了巨大的未探索空間。

🤔 **手動設計的 TTS 策略難以探索全部可能空間**

現有的 test‑time scaling（TTS）多半是研究者憑直覺設計的推理模式與啟發式規則。這種「手工藝」方式雖能帶來效能提升，但卻讓大量的計算分配可能性被忽略，導致資源使用與效果的權衡遠未達到理想狀態。

🧪 **以環境驅動的自動搜尋框架 AutoTTS**

研究團隊提出一個環境導向的框架——AutoTTS。其核心是把「設計個別 TTS 啟發式」轉變為「構建一個讓 TTS 策略能被自動發現的環境」。為了使搜尋可行，該環境必須將控制空間簡化，並提供廉價且頻繁的回饋，以供策略搜尋使用。

具體實作中，研究者將 width‑depth TTS 表現為對預先蒐集的推理軌跡與探測信號進行控制器合成：控制器決定何時分支、繼續、探測、剪枝或終止，且可以在不重複呼叫 LLM 的情況下以低成本評估。為進一步降低搜尋難度，他們引入了 beta 參數化，並利用細粒度的執行追蹤回饋來幫助代理診斷為何某個 TTS 程式失敗，從而提升發現效率。

🚀 **發現的策略在準確度‑成本權衡上優於手動基線**

在數學推理基準測試上的實驗表明，AutoTTS 所發現的 TTS 策略在準確度與計算成本的 trade‑off 上明顯優過強手動設計的基線。這些策略不僅在所見基準上表現更佳，亦能泛化至未見過的基準測試與不同規模的模型。

⚠️ **整個發現過程僅需 39.9 美元與 160 分鐘**

值得一提的是，從環境建置到策略搜尋的完整流程僅花費約 39.9 美元的計算資源與 160 分鐘的時間，且團隊將相關資料與程式碼開源（https://github.com/zhengkid/AutoTTS），方便後續研究與工程應用。

🎯 **工程師可直接採用的啟發：讓環境去尋找更好的推理方式**

- 若你正在為 LLM 推理尋找更好的計算分配策略，不妨考慮把「手動調節啟發式」轉換為「構建可搜尋的環境」。
- 低成本的環境模擬（如利用已蒐集的推理軌跡）能大幅減少實驗開銷。
- 開源的 AutoTTS 實作提供了可直接參考的起點，適合在數學推理或其他需要推理步驟的任務上進行試驗。

🔗 **論文連結**
📝 LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling  
👤 Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang (UMD; UVA; WUSTL; UNC; Google; Meta)  
🔗 https://arxiv.org/abs/2605.08083  

你有試過讓系統自己去搜尋最佳的推理策略嗎？歡迎在留言區分享你的想法或實驗經驗 👇

#AI #LLM #TestTimeScaling #AutoTTS #UMD #Google #Meta #機器學習 #推理優化 #開源代碼
