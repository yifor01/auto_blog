---
title: "WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.10912
score: 124
model: tencent/hy3-preview:free
generated_at: 2026-05-12T20:24:17.668284
---

📌 WildClawBench：真實 CLI 環境下的長程 Agent 基準測試  

你以為現在的前沿模型已經能在終端機裡自動完成複雜工作？在真實的 CLI 執行環境裡，他們的表現卻遠低於預期。  

🤔 **合成沙盒無法反映真實終端機的複雜性**  
現有的 Agent 基準多依賴合成沙箱、短程任務或模擬 API，這使得我們無法知道模型在實際部署的運行時是否真的能完成長時間、多步驟的工作。為了填補這個空白，研究團隊設計了一個在原生 CLI 環境中運行的基準。  

🧪 **60 個雙語多模態任務，平均 8 分鐘、超過 20 次工具調用**  
WildClawBench 包含 60 份由人類編寫的雙語、多模態任務，橫跨六個主題類別。每項任務平均約需 8 分鐘的牆鐘時間，並會觸發超過 20 次真實工具調用。所有任務都放在可重現的 Docker 容器內，容器中裝有實際的 CLI Agent harness（OpenClaw、Claude Code、Codex 或 Hermes Agent），並且能直接存取真實的系統工具而非模擬服務。  

📊 **Claude Opus 4.7 在 OpenClaw 下僅達 62.2%，其他模型皆低於 60%**  
在對 19 種前沿模型的評估中，最高分為 Claude Opus 4.7 在 OpenClaw harness 下的 62.2%；其餘模型的總體分數均未突破 60%。這表明，即便是目前最強的模型，在真實終端機上完成長程工作仍有顯著差距。  

💡 **更換 Agent harness 就能讓單一模型成績波動高達 18 分**  
僅 soltanto 更換所使用的 Agent harness（例如從 OpenClaw 換成 Claude Code），同一模型的得分就可能上下浮動多達 18 點。這顯示出評估結果高度依賴於具體的執行環境與工具鏈，基準本身的設計對最終得分影響甚大。  

⚠️ **目前僅涵蓋四種 Agent harness，未涵蓋所有可能的運行環境**  
基準的任務設計與評估流程均在 OpenClaw、Claude Code、Codex、Hermes Agent 四種 harness 下進行。因此，結果可能無法直接推廣至其他未被納入的 CLI 環境或工具組合。  

🎯 **釋出任務、程式碼與容器化工具，支援可重現的長程 Agent 評估**  
研究團隊同時開放了所有任務說明、評估程式碼以及完整的容器化工具鏈，使得研究者與工程師能在同一套環境下重現評估，進一步檢視自己的 Agent 在真實終端機上的長程能力。  

🔗 **論文連結**  
📝 WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation  
👤 Shuangrui Ding, Xuanlang Dai, Long Xing, Shengyuan Ding, Ziyu Liu 等  
🔗 https://arxiv.org/abs/2605.10912  

你在開發或評估 CLI Agent 時，是否也會考慮切換不同的 harness？歡迎在留言區分享你的經驗與看法 👇  

#AI Agent #長程評估 #CLI #WildClawBench #ShanghaiAILab #CUHK #Fudan #USTC #SJTU #Tsinghua #NTU #基準測試 #機器學習 #自然語言處理 #多模態
