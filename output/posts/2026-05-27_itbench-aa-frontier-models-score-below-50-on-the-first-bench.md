---
title: "ITBench-AA: Frontier Models Score Below 50% on the First Benchmark for Agentic Enterprise IT Tasks — by Artificial Analysis and IBM"
source: HuggingFace Blog
url: https://huggingface.co/blog/ibm-research/itbench-aa
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-05-27T20:47:59.540085
---

📌 ITBench-AA 基準測試  
你以為最強的 AI 模型已經能輕鬆處理企業運維？  
實際測試卻顯示它們在真實的 Kubernetes 故障場景中，成功率竟不到一半。  
這到底意味著什麼？

🤔 **企業 IT 基準測試的空白點**  
現有基準多聚焦單輪對話或簡單程式碼生成，缺少對多步驟、真實企業 IT 操作的評估。ITBench-AA 正是要填補這個 gap，從 Site Reliability Engineering（SRE）的 Kubernetes 事件響應開始，測試模型在讀取日誌、追蹤依賴、辨識根本原因等複雜工作流上的表現。

🧪 **IBM 與 Artificial Analysis 共同打造的評估資料集**  
資料集來源於 IBM 在企業 IT 運維的深度經驗，涵蓋真實的 Kubernetes 環境與故障注入場景。Artificial Analysis 在過去六個月協助實作此資料集，並設計評估協議，首先聚焦 SRE，未來將擴展至 Financial Operations（FinOps）與 Chief Information Security Officer（CISO）任務。

📊 **前沿模型在 SRE 基準上的表現**  
- Claude Opus 4.7（Adaptive Reasoning, Max Effort）最高達 47%  
- GPT-5.5 (xhigh) 緊隨其後，得分 46%  
- Qwen3.7 Max 得分 42%  
- GLM-5.1 (Reasoning) 為開放權重模型領先，得分 40%，與 Gemini 3.5 Flash (high) 持平  
所有評測模型均未突破 50%，使 ITBench-AA SRE 成為目前最不飽和的 agentic 基準之一。

🔍 **轉數與準確度的關係**  
轉數（模型與環境互動的來回次數）在任務間差異近三倍。更多的轉數並不一定帶來更高的準確度：  
- GPT-5.5 (xhigh) 平均 31 次轉數，準確度 46%  
- Gemini 3.1 Pro Preview 平均 83 次轉數，準確度僅 30%  
過度調查往往會將上游故障注入機制或共現症狀誤判為根本原因，導致假陽性增加。

💡 **實務啟示**  
在將 AI 引入企業運維前，團隊應該：  
1. 使用類似 ITBench-AA 的多步驟基準，實際測試模型在真實故障場景中的可靠度。  
2. 注意模型的「調查深度」：過長的互動循環可能降低效果並增加誤判。  
3. 將模型當作輔助診斷的工具，而非完全取代人工專家的判斷，特別是在根本原因分析這類需要上下文理解的任務上。

🔗 **論文與資源連結**  
📝 ITBench-AA: Frontier Models Score Below 50% on the First Benchmark for Agentic Enterprise IT Tasks  
👤 Ayhan Sebin, Saurabh Jha, Rohan Arora (IBM Research & Artificial Analysis)  
🔗 https://huggingface.co/blog/ibm-research/itbench-aa  

你在企業 IT 中使用 AI 輔助工具時，有否注意到類似的「過度調查」現象？歡迎在留言區分享經驗 👇

#AI #IT運維 #SRE #基準測試 #IBM #ArtificialAnalysis #AgenticAI #Kubernetes #DevOps #FinOps #CISO
