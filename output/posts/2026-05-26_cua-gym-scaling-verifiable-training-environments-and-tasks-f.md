---
title: "CUA-Gym: Scaling Verifiable Training Environments and Tasks for Computer-Use Agents"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.25624
score: 92
model: tencent/hy3-preview:free
generated_at: 2026-05-26T21:06:04.390359
---

📌 **CUA‑Gym：可擴展驗證環境**  
你以為訓練電腦使用代理只需要真實資料？CUA‑Gym 證明，合成環境也能超越真實資料的表現。  
這篇論文如何透過可擴展生成管線解決資料稀疏問題？

🤔 **資料稀疏限制電腦使用代理的訓練效果**  
目前，訓練能夠自動操作桌面或網頁的電腦使用代理（Computer‑Use Agents）常受限於真實互動資料的取得成本與多樣性不足。當資料稀疏時，模型難以學會穩健的操作策略，亦難以在未見任務上遷移。

🧪 **可擴展的合成任務與環境生成管線**  
CUA‑Gym 提供一套可擴展的生成管線，能自動構建多樣化的合成電腦使用任務與對應的虛擬環境。透過這種方式，研究團隊得以大量產出可驗證的訓練樣本，並在標準的驗證與遷移基準上測試模型表現。

🚀 **在驗證與遷移基準上表現優於現有方法**  
摘要指出，該框架透過可擴展生成管線與合成環境，解決了資料稀疏問題，並在驗證（verification）及遷移（transfer）基準上獲得了較現有方法更好的成績。具體的數據提升幅度需參考原文細節。

🔍 **可擴展生成如何提升代理學習**  
透過程式化地變更任務目標、環境狀態與操作難度，CUA‑Gym 能產出涵蓋邊界案例的訓練樣本。這種設計讓代理在訓練階段就接觸到多樣化的情境，有助於學得更具泛化能力的策略，亦使得後續在真實軟體上的表現更具可靠性。

⚠️ **作者未在摘要中說明具體實驗規模或長期穩定性評估**  
摘要著重於框架的設計與基準表現，未詳細說明使用的合成任務數量、多樣性指標，或是代理在長時間互動中的穩定性。如需了解這些實驗細節，建議直接閱讀完整論文。

🎯 **工程師可直接採用的訓練環境管線**  
對於正在開發電腦使用代理的團隊，CUA‑Gym 提供一套可即插即用的合成任務生成工具與驗證基準。透過調整管線參數，可快速產出符合特定應用場景的訓練資料，降低對真人標註或真實環境依賴的成本。

🔗 **論文連結**  
📝 CUA‑Gym: Scaling Verifiable Training Environments and Tasks for Computer-Use Agents  
🔗 https://huggingface.co/papers/2605.25624  

你是否曾因缺乏真實互動資料而瓶頸在代理訓練上？歡迎在留言區分享你的看法或使用經驗 👇  

#AIAgents #ComputerUse #RLVR #SyntheticData #HuggingFace #AgentTraining #機器學習 #強化學習
