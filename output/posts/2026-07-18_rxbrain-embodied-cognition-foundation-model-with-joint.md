---
title: 'RxBrain: Embodied Cognition Foundation Model with Joint Language-Visual Reasoning
  and Imagination'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.14187
score: 91
model: tencent/hy3:free
generated_at: '2026-07-18T07:35:34.352716'
---

📌 【HuggingFace Papers】RxBrain：用語言與視覺想像統一體現認知規劃

TL;DR：RxBrain 以單一規劃序列結合語言與視覺想像，朝體現認知基礎模型邁出一步。

大多數 vision-language 模型專注於場景理解與文字決策， generative world model 則主要預測未來視覺狀態，但體現認知真正需要的，是把高層任務推理與物理狀態連起來。RxBrain 嘗試用一種不一樣的表示法來處理這件事。

🤔 **體現認知需要連線推理與物理狀態**

論文指出，embodied cognition（體現認知）要求 agent 將高層級的任務推理，連結到要達成的物理狀態。現有方法各有偏重：vision-language model 強調場景理解與文字決策，generative world model 偏重未來視覺狀態預測，兩者都沒有把語言與視覺想像放在同一個規劃表示中互補運作。

🧩 **單一規劃序列中的語言與視覺互補**

RxBrain（全名 Hy-Embodied-RxBrain）把體現計畫表示成單一 planning sequence，語言與 visual imagination 扮演互補角色：

- 語言提供計畫的抽象結構：任務分解、planning primitives、約束、時間順序、決策邏輯。
- 視覺想像透過 world state prediction 與 joint subgoal planning，把結構落到物理狀態，讓每個規劃步驟對應中間與最終物理狀態。

架構上，RxBrain 採用統一的多模態 Mixture-of-Transformers，在同一個模型內支援語言、影像與影片的理解與生成。

📊 **自動化資料管線與專用評測集**

為了訓練這種聯合能力，作者建立自動化 pipeline：將 embodied videos 分解為 planning steps，並對齊 visual state transitions，轉換成 joint text-visual planning supervision。

評測方面，論文提出 RxBrain-Bench，用來檢查模型能否透過聯合文字與視覺元件來表示體現計畫，而非各自獨立的理解或生成。

實驗顯示，RxBrain 能維持體現理解與生成能力，並產出具有耦合文字推理、world state prediction 與 joint subgoal planning 的計畫。作者也將 RxBrain 擴充套件到連續機器人動作生成，在無大規模 action-data 預訓練下，展現出有潛力的真實機器人表現。

⚠️ **仍是初步探索**

論文將這些結果定位為朝向 embodied cognition 基礎模型的初始一步，未提及具體資料、baseline 對比數值或完整限制清單。

🎯 **對工程師的實務啟示**

若你在做 robot planning 或 embodied AI，RxBrain 展示了一條不同路徑：不必分開訓練理解與生成，而是用統一序列把語言結構與視覺狀態預測綁在一起。其自動化從影片產生聯合監督的 pipeline，也值得參考用來解決體現資料稀缺問題。

🔗 **來源**
- 標題：RxBrain: Embodied Cognition Foundation Model with Joint Language-Visual Reasoning and Imagination
- 連結：https://huggingface.co/papers/2607.14187

#EmbodiedAI #RxBrain #VisionLanguageModel #Multimodal #MixtureOfTransformers #RobotPlanning #WorldModel #VisualImagination #FoundationModel #HuggingFacePapers
