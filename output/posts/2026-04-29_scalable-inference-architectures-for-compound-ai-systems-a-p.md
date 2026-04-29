---
title: "Scalable Inference Architectures for Compound AI Systems: A Production Deployment Study"
source: ChatPaper/AI
url: https://arxiv.org/abs/2604.25724
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-04-29T20:57:15.309940
---

📌 【Salesforce 實戰】Compound AI 系統尾延砍半、吞吐躍升 3.9 倍的擴散架構

多模型 Agent 系統上線後，尾延（P95）不降反升、零星冷啟動像骨牌般蔓延，導致成本失控——這正是複合式 AI 系統在企業落地時最常踩的隱形深坑。

🤔 **多模型疊加讓擴散成本失控，而非單模型優化**

企業級 AI 正從單一模型走向 Compound AI Systems：多模型疊代、檢索器與工具鏈交織，構成 Agentic Workflow。這類系統在生產環境中會引發異構調用、突發 fan-out 與冷啟動傳播，若沿用傳統靜態部署模式，尾延與成本將同步失控。

🧪 **模組化、無伺服器與 MLOps 串聯的生產實驗**

Salesforce India 團隊針對 Agentforce（自主 Agent 平台）與 ApexGuru（AI 驅動程式碼分析）部署一套平台無關的推論架構，整合以下設計：
- 無伺服器執行與動態自動擴縮
- 多模型並行 fan-out 排程與佇列隔離
- MLOps 管道支援模型快速迭代與 A/B 切流
測試場景涵蓋多 Agent 協同、突發多模型調用與異構運算負載，並在生產環境持續觀測尾延、吞吐與成本。

📉 **尾延（P95）下降 50%，吞吐提升 3.9 倍，成本節省 30–40%**

- P95 尾延：減少超過 50%
- 系統吞吐：最高達 3.9 倍提升
- 運算成本：30–40% 節省（相較先前靜態部署）
在多模型 fan-out 場景中，並行化與隔離排程有效抑制長尾，並避免單一熱點阻塞整體流程。

🔍 **用並行 fan-out 與隔離擴縮取代單點擴散，斷冷啟動傳播**

生產環境中凸顯三項 Compound System 獨有挑戰：
- 多模型 fan-out 開銷疊加導致吞吐瓶頸
- 冷啟動在模型與檢索器間傳播，引發階段式停滯
- 異構模型（大小、框架、載入時間）導致擴縮動態不同步
透過無伺服器執行與動態擴縮組合，將「佇列隔離 + 批量預熱 + 階段式擴縮」機制化，減少冷啟動傳播並穩定尾延。

⚠️ **以現有工作負載與短期穩定度為基線，長期擴散與故障模式待驗證**

本研究基於當前 Agentic 場景與生產流量模式，未涵蓋極端突發、跨區多活與長期模型漂移下的擴散穩定性；同時異構冷啟動行為依賴特定無伺服器平台特性，換置不同執行環境時需重新校準擴縮策略。

🎯 **以隔離排程與動態擴縮換取成本、尾延、吞吐的可控平衡**

- 將 fan-out 視為系統級問題，而非單模型調優
- 無伺服器 + 自動擴縮應針對異構載入時間分層設定
- MLOps 與推論管道緊密整合，支援 Agent 快速迭代
- 將冷啟動傳播視作可觀測指標，並在部署階段主動壓制

🔗 **論文連結**
📝 Scalable Inference Architectures for Compound AI Systems: A Production Deployment Study
👤 Srikanta Prasad V S & Utkarsh Arora @ Salesforce India Pvt Ltd
🔗 論文：https://arxiv.org/abs/2604.25724

你的團隊在推動 Agentic AI 時，尾延與成本是否也曾卡在「多模型疊加」這一關？欢迎分享實戰經驗 👇

#AI #AgenticAI #MLOps #Inference #Scalability #Salesforce #CompoundAI #生產實戰
