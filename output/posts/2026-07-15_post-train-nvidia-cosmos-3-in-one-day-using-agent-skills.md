---
title: Post-Train NVIDIA Cosmos 3 in One Day Using Agent Skills
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/post-train-nvidia-cosmos-3-in-one-day-using-agent-skills/
score: 99
model: tencent/hy3:free
generated_at: '2026-07-15T08:13:08.724763'
---

📌 【NVIDIA】一天後訓練 Cosmos 3 準確率達 93%

TL;DR：結合 TAO agent skills 與 LoRA，不到一天將 Cosmos 3 影片問答準確率從 54% 提升至 93%。

開發者想把視覺推理模型套用到生產級影片任務時，往往耗費數天在資料格式調整、容器設定與超引數搜尋上，卻還不確定後訓練是否真的有用。如果有一套 agent 能幾乎自動搞定呢？

🤔 **後訓練視覺模型的前置作業吃掉數天**
開發者適應視覺推理模型到生產影片任務時，常迷失在資料格式化、容器建置、訓練指令碼、基線評估與超引數掃描中，才能知道後訓練有無提升準確率。

🧩 **Cosmos 3 混合 Transformer 架構搭配 TAO Agent Skills**
NVIDIA Cosmos 3 是開放實體 AI 世界基礎模型，採用 mixture-of-transformers 架構統一多模態輸入，並分離推理與生成路徑。TAO agent skills 將後訓練工作流程封裝起來，透過 TAO AutoML 自動化資料集處理、基線評估、LoRA 配置與超引數最佳化，實現極少人工介入的領域適應。

📊 **Woven 交通資料集準確率從 54.41% 升至 93.35%**
在 Woven Traffic Safety 資料集上，整合 Cosmos 3 與 TAO agent skills 加上 LoRA 的完全自動化後訓練，將影片問答準確率從 54.41% 大幅提升到 93.35%，耗時不到一天且僅需最少人工介入。

💡 **Cosmos 3 Reasoner NIM 直接以相容 OpenAI 端點部署**
生產部署透過 Cosmos 3 Reasoner NIM 簡化，它直接使用預建 NVIDIA 微服務，將後訓練的 LoRA 介面卡作為相容 OpenAI 的 API 端點提供服務，排除傳統基礎設施與 CUDA 依賴的複雜度。

🎯 **把後訓練工程開銷壓到最低**
對工程師而言，這套組合讓視覺語言模型的領域微調從數天壓縮到一天內，且不需深陷訓練指令碼與環境設定。若手上已有 Cosmos 3 與 TAO，可優先評估用 agent skills 加速垂直場景適配。

🔗 **來源**
- 標題：Post-Train NVIDIA Cosmos 3 in One Day Using Agent Skills
- 作者／機構：Tanya Lenz
- 連結：https://developer.nvidia.com/blog/post-train-nvidia-cosmos-3-in-one-day-using-agent-skills/

#NVIDIA #Cosmos3 #TAO #AgentSkills #LoRA #PostTraining #VisionLanguage #NIM #AutoML #VideoQA
