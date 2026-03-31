---
title: "AIRA_2: Overcoming Bottlenecks in AI Research Agents"
source: ChatPaper/AI
url: https://arxiv.org/abs/2603.26499
score: 105
model: gpt-4o-free
generated_at: 2026-03-31T00:36:05.421322
---

📌 【Meta FAIR】AIRA_2 突破三大瓶頸  

你以為讓 AI 自己做研究就能無限提升？實際上，現有研究代理卡在同步執行、評估噪聲與單次 LLM 能力的瓶頸，導致長時間搜尋反而變差。  

🤔 **同步單 GPU 限制樣本吞吐，搜尋收益受阻**  
現有代理多依賴單卡同步執行，實驗樣本產生速度受硬體瓶頸限制，無法充分發揮搜尋算法的潛力。  🧪 **非同步多 GPU 工作池 + Hidden Consistent Evaluation + ReAct agents**  
AIRA_2 採用三項架構設計：  
- 建立非同步多 GPU 工作池，讓實驗吞吐量隨 GPU 數量線性提升；  
- 提出 Hidden Consistent Evaluation 協議，提供穩定可信的評估訊號，降低驗證選擇帶來的性能衰退；  
- 使用 ReAct 動態範圍代理，讓模型在搜尋過程中可互動除錯與調整行動範圍。  

📈 **MLE-bench-30 上平均百分位從 69.9% 提升至 71.8% (24h)，並隨時間增長至 76.0% (72h)**  
在標準基準 MLE-bench-30 上，AIRA_2 在 24 小時時達到 71.8% 的平均百分位，超過之前最佳的 69.9%；隨著搜尋時間延長至 72 小時，表現持續提升至 76.0%。消融實驗證明，缺少任一組件都會顯著降低效果，而先前報告的「過擬合」主要來自評估噪聲而非真實資料記憶。  💡 **瓶頸不是資料記憶，而是評估與執行效率的系統性限制**  
結果表明，提升研究代理的上限不只是靠更大的模型或更多資料，而是要解決同步執行瓶頸、提供一致的評估訊號，以及讓代理具備互動除錯與動作範圍調整的能力。這三者缺一不可，才能讓搜尋過程在長時間內持續改善。  ⚠️ **實驗依賴多 GPU 資源，基準僅針對 MLE-bench-30**  
為了實現線性吞吐提升，方法需要多塊 GPU 進行非同步調度；此外，所有結果均來自單一基準 MLE-bench-30，是否在其他研究任務或不同硬體配置上具有同樣優勢仍需進一步驗證。  

🎯 **工程師可先嘗試非同步工作池與穩定評估機制，再逐步加入 ReAct 風格的互動除錯**  
- 若資源允許，將實驗調度改為非同步多 GPU 池，可直接提升樣本產生速度；  
- 在模型選擇步驟引入類似 Hidden Consistent Evaluation 的穩定評估緩衝，減少驗證噪勢導致的性能波動；  
- 在代理框架中加入簡易的互動除錯迴圈（思考→行動→觀察），讓模型能在搜尋過程中自我校正。  

🔗 **論文連結**  
📝 AIRA_2: Overcoming Bottlenecks in AI Research Agents  
👤 Karen Hambardzumyan, Nicolas Baldwin, Edan Toledo, Rishi Hazra, Michael Kuchnik (FAIR at Meta; UCL; Oxford)  
🔗 https://arxiv.org/abs/2603.26499  

你在構建 AI 研究代理時，是否曾遇到評估不穩定或單卡瓶頸的問題？歡迎在留言區分享你的經驗與解決方案 👇  

#AI #ResearchAgent #MetaFAIR #MLE-bench #ReAct #多GPU #AI研究 #機器學習
