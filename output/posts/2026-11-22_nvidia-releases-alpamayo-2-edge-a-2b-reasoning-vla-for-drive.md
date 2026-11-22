---
title: 'NVIDIA Releases Alpamayo 2 Edge: A 2B Reasoning VLA for DRIVE Thor'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/22/nvidia-alpamayo-2-edge-2b-reasoning-vla-drive-thor/
model: claude-code/sonnet
generated_at: '2026-11-22T22:36:09.377263'
score: 91
---

📌【NVIDIA最新發布】2B推理模型上車，塞進DRIVE Thor晶片

TL;DR：NVIDIA推出車載版VLA模型Alpamayo 2 Edge，在板載晶片上做即時推理規劃。

自駕系統的決策模型，過去多半得丟上雲端算力才跑得動。NVIDIA這次把一個會輸出「為什麼這樣開」推理軌跡的模型，直接塞進車上的DRIVE AGX Thor晶片。

🤔 問題：reasoning-based planning要在車上即時算完

Alpamayo 2 Edge 是一個 2B 參數的推理型視覺-語言-行動（VLA）模型，目標是在車載算力與延遲預算內完成「規劃軌跡並解釋理由」的任務，對象是 NVIDIA DRIVE AGX Thor，而非資料中心 GPU。它是 Alpamayo 家族的車內成員,旁邊還有一個 34B 的雲端版本 Alpamayo 2 Super。

🧩 架構：6支鏡頭看路，64個路徑點作答

根據模型卡，2.45B 的 backbone 由一個 1.96B 的語言模型與一個 0.41B 的 SigLIP2 編碼器組成,backbone 本身來自 NVIDIA Cosmos 3 Edge，以 Nemotron 為基礎；上面再疊一個 0.2B 的 diffusion 行動專家（action expert）。值得一提的是，NVIDIA 對外行銷的參數量標為 2B，但 Hugging Face 的 metadata 顯示為 3B,兩個數字對不上。

輸入端，模型讀取 6 支環車鏡頭、每次觀測共 22 幀（2 支前鏡頭各給 5 幀，其餘 4 支各給 3 幀），加上一條導航指令與 20 個歷史自身姿態（ego pose）。輸出則是從 0.1 秒到 6.4 秒、共 64 個路徑點：action expert 先預測加速度與曲率，再由一個 unicycle 模型把這兩個量積分成實際軌跡。文字輸出則是一條「因果鏈」（Chain-of-Causation，CoC）推理軌跡，模型也能就駕駛場景回答開放式問題。為了省算力，日常平穩駕駛時模型只輸出特殊的 <NOMINAL> token，不產生完整推理文字,只有場景真的需要解釋時才寫 CoC。

🧩 部署：從PyTorch到TensorRT，延遲160到190毫秒

Hugging Face 上的權重是 BF16 格式、以 PyTorch 執行。要在 Thor 上即時跑，需要透過 Alpamayo Developer Hub 提供的流程：先把 checkpoint 與 DFlash2 草稿模型一起分階段處理，校準 FP8 數值範圍，接著匯出 ONNX 圖，再用 TensorRT Edge-LLM 外掛建出 TensorRT 引擎。NVIDIA 公佈的像素到軌跡（pixel-to-trajectory）延遲是 160 到 190 毫秒，依推理量多少而變化，參考環境是搭載 DRIVE OS 7.2.7.0、CUDA 13.4、TensorRT 11.3.1.9 的 DRIVE AGX Thor-X。在 NVIDIA 的示範影片中，PyTorch BF16 版本以 0.76Hz 規劃，最佳化後的 FP8 Thor 管線在 AlpaSim 中可達 13.02Hz；合作夥伴 Embedl 則表示在 AGX Thor 上於 48 小時內做到 10Hz。若是跑在工作站 GPU 上，官方建議至少 16GB 記憶體，實測在單張 H100、6 個軌跡候選的設定下，峰值處理記憶體為 12.06GiB,其他 GPU 架構目前尚未驗證。

📊 數據：對比Qwen-Drive-1.0，閉環事故間距差了約60倍

NVIDIA 拿自家的 AlpaSim 把 Edge 和 Alibaba 的 4B 模型 Qwen-Drive-1.0 做對比：閉環駕駛測試中，Edge 平均每 15.15 公里才出現一次有責事故，Qwen-Drive-1.0 只有 0.25 公里，相差約 60 倍；開環 minADE（最小平均位移誤差）則是 0.53 公尺對 1.68 公尺。這些數字都是 NVIDIA 自行測得。此外，NVIDIA 同步發布了 AlpaJudge，一個經人類校準的推理軌跡評分器，用來篩選訓練資料並提供強化學習獎勵；作為 RL 獎勵訊號時，它把推理品質分別提升了 10.2%（由 AlpaJudge 自己評分）與 11.4%（由人類評分）。

⚠️ 限制：自家測試數字，且參數量標示本身就有矛盾

目前公開的對比數據全部來自 NVIDIA 自身的 AlpaSim 測試，不同資料來源用的指標也不統一（每公里事故數、AlpaSim Score、有責分數各不相同），比較時只能看同一列指標。硬體相容性方面，除了 H100 與 DRIVE AGX Thor 之外，其他 GPU 架構尚未驗證過。前面提到的「2B 對外行銷、3B metadata 標示」的差異，也值得在評估模型規模時留意。

🎯 實務啟示

權重採用 OpenMDW-1.1 授權，程式碼採用 Apache 2.0，推理程式碼已上 GitHub，且官方表示模型支援微調。對正在做車載或邊緣端自駕感知規劃的工程團隊來說，這是少數同時公開架構細節、部署流程與延遲數字的開源 VLA 模型，<NOMINAL> token 的設計思路（平時省算力、需要時才展開推理）也值得在其他需要「可解釋但要省算力」的場景中參考。

🔗 來源
- 標題：NVIDIA Releases Alpamayo 2 Edge: A 2B Reasoning VLA for DRIVE Thor
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/22/nvidia-alpamayo-2-edge-2b-reasoning-vla-drive-thor/

#NVIDIA #AutonomousDriving #VLA #EdgeAI #DRIVEThor #TensorRT #ReasoningModel #RoboticsAI #ModelDeployment #OpenWeights
