---
title: 'Reflection AI Introduces Beam: A 501B Open-Weight MoE Model With 23B Active
  Parameters for Coding and Agentic Workloads'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/05/reflection-ai-introduces-beam-a-501b-open-weight-moe-model-with-23b-active-parameters-for-coding-and-agentic-workloads/
model: claude-code/sonnet
generated_at: '2026-10-05T23:19:30.925840'
score: 98
---

📌 Beam架構全公開:501B MoE只啟用23B參數卻還在紅隊測試中

TL;DR:Reflection AI的Beam把訓練與基礎設施細節全數公開,但目前仍無法自行部署。

一個模型的技術報告裡,能同時看到「52層殘差穩定技巧」「1.3億個沙箱環境」「新權重12秒內上線推論叢集」這種等級的細節並不常見。Reflection AI 這次對 Beam 的揭露,顆粒度遠超一般的模型發布文。

🧩 **架構:稀疏MoE,混合local/global attention**

Beam 是從零訓練的稀疏 Mixture-of-Experts 模型,總參數 501B,每個token僅啟用 23B。架構在local與global attention之間交錯安排,搭配細粒度的routed experts。負載平衡沿用 DeepSeek-V3 的auxiliary-loss-free balancing,再加上expert-bias更新的cosine decay,根據Reflection AI說法，pretraining結束時最繁忙的expert負載也只是平均值的1.04倍。全部52層中,殘差穩定靠的是depth-based scaling、SandwichNorm、attention gating,以及FP32殘差累加。

📊 **訓練規模:23.8兆token預訓練,RL才是重頭戲**

Reflection AI表示，預訓練用了23.8兆token,來源是網路、公開資料與自有授權資料集;團隊稱其資料清理流程過濾掉約95%的原始網路token,但同時保留了約1.8兆筆「傳統過濾器會誤刪」的高品質token。預訓練在6,144張 NVIDIA GB300 NVL72 GPU上不到4週完成,末期goodput達92.3%,過程中有9次半自動rewind。Midtraining階段把有效context延伸到1M token。

真正被Reflection AI視為核心擴展軸的是強化學習(RL):動用10.5K張GB300 GPU訓練4週,產生超過1億次rollout,單次rollout context上限達256K token,訓練與評分合計耗用約13億個sandbox,涵蓋近100萬個coding、agentic與STEM環境。訓練採用完全非同步的policy gradient,每個token都標記產生它的policy版本,即使落後107個權重版本(約一天延遲)仍能保持訓練穩定,團隊表示RL運算量增加時沒有出現plateau。基礎設施面,平均同時跑著11萬個rollout,新權重上線推論叢集的中位時間約12秒,期間71次推論事故都在不中斷訓練的情況下排除。一個可控的長度懲罰機制讓Beam學會用更少token解題;有趣的是,即便RL訓練組合裡沒有瀏覽任務,瀏覽能力依然提升,暗示agentic能力之間存在遷移效果。

💡 **安全對齊走多教師蒸餾路線**

Reflection AI團隊從預訓練checkpoint另外訓練了一個安全對齊teacher,再透過multi-teacher on-policy distillation把它與RL teacher合併,安全訓練採用deliberative alignment,具體安全評測數字將在技術報告中公布。

📊 **跑分對比**

| 基準 | Beam | 對比對象 |
|---|---|---|
| SWE-bench Verified | 80.9 | Nemotron 3 Ultra 70.7 |
| Terminal Bench v2.1 | 80.1 | GLM 5.2 81.0、DeepSeek V4.1 Flash 90.6、Kimi K3 88.3 |

（數字取自Reflection AI公布的對照表,對手分數引用自Artificial Analysis與DataCurve）值得注意的是,Beam是這張表中總參數最小的模型，23B的active參數也低於GLM-5.2、Nemotron 3 Ultra與Kimi K3。授權方面,Beam採Apache 2.0與MIT這類標準寬鬆授權,相較之下Kimi K3的自訂授權對超大型產品另有歸屬要求。

⚠️ **目前還不能自行部署**

根據MarkTechPost報導，Beam仍在進行最終紅隊測試,尚未開放self-hosting,只能透過Reflection平臺的候補名單取得early access。

🎯 **實務啟示**

對於評估要不要等待Beam的工程團隊,現階段能做的只有先研究其公開的架構設計(例如reasoning effort參數讓你依任務難度調整推理長度),真正的落地測試得等紅隊測試結束、權重開放之後才能進行。

🔗 **來源**
- 標題:Reflection AI Introduces Beam: A 501B Open-Weight MoE Model With 23B Active Parameters for Coding and Agentic Workloads
- 作者／機構:Asif Razzaq, MarkTechPost
- 連結:https://www.marktechpost.com/2026/10/05/reflection-ai-introduces-beam-a-501b-open-weight-moe-model-with-23b-active-parameters-for-coding-and-agentic-workloads/

#ReflectionAI #Beam #MixtureOfExperts #OpenWeightLLM #ReinforcementLearning #LLMTraining #AgenticAI #CodingLLM #MoE #AIInfrastructure
