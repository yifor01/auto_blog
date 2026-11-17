---
title: Post-Training NVIDIA Nemotron to Increase Accuracy in Your Scientific Domain
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/post-training-nvidia-nemotron-to-increase-accuracy-in-your-scientific-domain/
model: claude-code/sonnet
generated_at: '2026-11-17T01:03:12.515497'
score: 89
---

📌 NVIDIA Nemotron for Science：用可驗證獎勵把科學模型練準

TL;DR：NVIDIA 示範如何用 NeMo Gym 建 RL 環境、以 NeMo RL 做 post-training，讓 Nemotron 3.5 Super VL 在藥物代謝預測上明顯更準。

當研究者開始用自然語言向 agent 描述科學假設，讓它自主規劃任務、跑模擬、評估結果、再自我修正，一個現實問題隨之浮現：沒有驗證機制，錯誤會在多輪迭代中不斷累積，延遲與算力成本也會跟著倍增。NVIDIA Nemotron for Science 正是針對這個痛點打造的一套模型、資料集、工具與訓練配方合集。

🤔 科學 agent 需要什麼

Nemotron for Science 的核心是 Nemotron 3.5 Super VL，一個開放、可客製化的多模態模型，專為處理愈趨視覺化、愈趨複雜的科學工作流設計；配套的 NVIDIA Nemotron Litmus-Bench V2.0 則是一個開源化學推理資料集與 benchmark，用來訓練與評測 LLM／agentic AI 模型在分子性質預測上的能力。文中指出，Nemotron 在多項科學 benchmark 上即具備 frontier 級準確率，並在科學程式設計任務上提供最快的求解時間。NVIDIA 強調的重點是：這些模型支援 post-training，讓團隊可以針對自己的研究領域再做客製化，進一步提升準確率。

🧩 從一份實驗 CSV 到一個可訓練的 RL 環境

這套配方的起點很樸素：一份記錄既有實驗結果的 CSV 檔，裡面可能是序列、SMILES 字串（一種描述分子原子與鍵結的文字表示法）、反應條件等任何中繼資料，搭配量測到的性質或結果。這些輸入輸出對會被重新整理成問答或 user/assistant 的 prompt 格式，實驗真值則當作 verifier 來給模型的回答打分——這樣就組成了一個基本的 RLVR（reinforcement learning with verifiable rewards）環境，完全不需要人工偏好標註，獎勵訊號直接來自資料本身。verifier 的精細程度可以依任務調整：簡單的序列相似度函式就能當輕量 verifier，更進階的化學資訊工具、分子模擬器，甚至接上一座真實的自動化實驗室當工具呼叫，都可以接進這個評分層，工具愈精細，模型就愈能被導向化學或生物上真正有意義的輸出。

以文中的藥物代謝預測為例：模型拿到母體分子與代謝酵素，提交一個預測的代謝物；verifier 用 Tanimoto similarity 比較預測分子與參考分子的指紋（分子結構特徵的數值化表示），這個指標是計算兩個集合交集與聯集的比值，分數落在 0 到 1 之間，愈高代表愈相似。範例資料來自 MetxBioDB，一個收錄實驗驗證生物轉化反應的資料庫。

訓練時用的是 GRPO（group relative policy optimization）搭配 LoRA 進行微調：環境把實驗輸入交給模型，要求它先逐步推理，再透過工具呼叫提交預測答案，每次提交都由 verifier 自動評分，形成一個不需額外標註、密度很高的獎勵訊號。訓練迴圈、reward server、harness 與 rollout worker 都是自我包含的設計，理論上能套用到任何「能回傳一個標量獎勵」的領域。

📊 SFT 先墊底、RL 再加碼

在 16,384-token 輸出預算、藥物代謝 RLVR 環境下，SFT（監督式微調）先讓 Nemotron for Science 的準確率提升 12%，接著的 RL post-training 再往上拉高 17%。這說明即便是已經相當能力的指令微調模型，給予針對性的 RL 回饋後仍能有明顯提升。

🧩 用更強模型「暖身」再進 RL

如果 base model 在進入 RL 前能力還不夠，或是 RL 收斂太慢，文中提供了一個可選的蒸餾步驟：先用一個更強的 teacher model（文中用的是 Anthropic 的 Claude Sonnet 5.5）在同一個環境裡跑一輪，產生推理軌跡，再依 Tanimoto similarity 評分，只保留答對的（問題、推理軌跡）配對，拿來對 student model 做 SFT 或 on-policy distillation，作為進入 RL 前的「暖身」起點，通常能加速收斂、拉高效能下限。在這個環境裡，團隊從 1,934 筆訓練 prompt 中，以 Tanimoto 閾值 ≥ 0.7 篩出了 1,123 條高品質推理軌跡作為 SFT 語料。文中也附上一條實際的蒸餾推理軌跡範例（CYP1A2 N-去甲基化反應），其預測結果與真值的 Tanimoto similarity 達到 1.0，完全吻合。

🎯 實務啟示

這套流程的價值不只在藥物代謝這一個案例：只要能把自己的實驗資料整理成「輸入、輸出、驗證方式」三件事，就能套用同一套 RLVR 配方，把一個通用的多模態模型逐步調教成貼合自己研究領域的專用模型，對正在把 LLM 導入實驗室流程的團隊而言,是一條相對具體可行的路徑。

🔗 來源
- 標題：Post-Training NVIDIA Nemotron to Increase Accuracy in Your Scientific Domain
- 作者／機構：Gautham Dharuman, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/post-training-nvidia-nemotron-to-increase-accuracy-in-your-scientific-domain/

#NVIDIA #Nemotron #ReinforcementLearning #RLVR #GRPO #LoRA #ScientificAI #DrugDiscovery #AgenticAI #PostTraining
