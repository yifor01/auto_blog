---
title: '[AINews] Death of Params: Z.ai CEO Jie Tang on GLM 5.3 and the new Post-training
  Scaling Law'
source: Latent Space
url: https://www.latent.space/p/ainews-death-of-params-zai-ceo-jie
model: claude-code/sonnet
generated_at: '2026-08-20T06:30:41.384461'
score: 99
---

📌 參數量之死?GLM 5.3 的後訓練縮放律

TL;DR:GLM 5.3 的能力躍進,靠的是 RL 長時序環境,而非更多參數。

多年來,我們習慣用參數量當作模型強弱的簡稱:70B、200B、2兆……數字越大代表越聰明。但 Z.ai 的 Jie Tang 教授在 X 上潑了一盆冷水:單獨看參數量,「不再足夠」。

🤔 為什麼 Chinchilla 的假設在今天失靈

Jie Tang 指出,在「推論反曲」(Inference Inflection)的世界裡,並不存在單一固定的 tokens-per-parameter 比例——業界過去引用的 200 到 900 這個區間,其實高度取決於任務類型(引用 Roberts et al. 的說法)。他把這個現象濃縮成一句話:記憶偏好更多參數,推理偏好更多後訓練資料與有效深度。這也解釋了為什麼近期不少中等參數量的模型,靠後訓練就能追上、甚至超越參數量大上數十倍的對手。

🧩 GLM-5.3 的躍進,來自合成到底的長時序環境

依 Jie Tang 的說法,GLM-5.3 這一輪的能力提升幾乎全部來自「長時序環境」(long horizon environments)上的強化學習,而非參數規模擴張。這些環境的設計貼近真實工程與研究工作的實際流程,涵蓋範圍遠比過去廣,部分任務甚至相當於一位資深工程師好幾天的工作量。舉例來說,在一個 ML 基礎設施任務中,模型會拿到跟工程師相同的工作環境:運算叢集、儲存系統、內部文件、程式碼庫與實驗結果。它必須自行診斷訓練堆疊中的瓶頸、實作最佳化、跑實驗,並在維持正確性的前提下交出可量測的端到端加速成果。這種等級的訓練,推動模型從「使用者拆解問題、每一步都要被監督」,轉向「對整段工作端到端負責」。

更關鍵的是,整套環境、判分與驗證流程是「從頭到尾合成」出來的:研究型 agent 從真實工作中蒐集任務模式,轉換成具有多步依賴與隱藏狀態的可執行長時序環境;接著由一個判斷型 agent 嘗試每個任務,驗證它確實可解。驗證器(verifier)在完全看不到參考答案的情況下被合成出來,而求解軌跡(solver trajectories)則被用來找出並封堵獎勵訊號的漏洞(reward shortcuts)。只有通過 oracle、no-op、未解狀態三種檢查的驗證器,才會產生足夠可靠、可直接拿來訓練的二元獎勵訊號。Jie Tang 認為,隨著 agent 能力提升,後訓練擴張的難點,已經從「模型」本身轉移到「環境」的建構與驗證上——而且需要的是大量環境,不是少數手工打造的範例。

💡 五個縮放旋鈕,取代單一參數量

為了終結對參數量的執念,Jie Tang 提出了五個縮放旋鈕(scaling knobs),其中包括以新的 XA-YB 記號來表示 MoE 稀疏度。他特別點出,像挖掘軟體漏洞這類進階能力,並不是檢索或記憶問題,而是需要在 20 步以上的推論鏈中,不斷維持因果關係而不「斷線」。一旦模型的知識儲備跨過某個門檻,這種能力就不再隨總參數量線性成長,換句話說,參數量對這類能力的邊際效益正在遞減。

⚠️ 概念清楚,細節仍待補齊

素材中除了 MoE 稀疏度的 XA-YB 記號外,其餘四個縮放旋鈕的具體定義並未展開說明,獎勵訊號合成的演算法細節、驗證器如何精確判定「oracle / no-op / 未解狀態」也僅止於概念層級。這篇來自 X 的說法目前更像是研究方向的宣示,而非可重現的技術報告。

🎯 環境品質,可能取代模型大小成為新戰場

如果這個方向成立,對工程團隊的啟示很直接:與其把資源全押在堆參數量,不如投資在建構貼近真實工作流程的評測與訓練環境,以及能自動合成、驗證獎勵訊號的 pipeline。對於正在打造 agentic 系統的團隊,「環境的品質與覆蓋範圍」可能會取代「模型大小」,成為下一階段的核心競爭力。

🔗 來源
- 標題:[AINews] Death of Params: Z.ai CEO Jie Tang on GLM 5.3 and the new Post-training Scaling Law
- 作者／機構:Latent Space
- 連結:https://www.latent.space/p/ainews-death-of-params-zai-ceo-jie

#GLM53 #ZhipuAI #ScalingLaws #ReinforcementLearning #LLM #AgenticAI #PostTraining #OpenWeights #AIResearch #MachineLearning
