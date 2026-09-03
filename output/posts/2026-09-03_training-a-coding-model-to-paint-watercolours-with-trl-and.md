---
title: Training a coding model to paint watercolours with TRL and OpenEnv
source: HuggingFace Blog
url: https://huggingface.co/blog/train-to-paint-with-code
model: claude-code/sonnet
generated_at: '2026-09-03T20:09:42.228386'
score: 105
---

📌 【HuggingFace複現】用TRL＋OpenEnv訓練一個會畫水彩畫的coding模型

TL;DR：工程師把爆紅的水彩畫AI專案完整開源複現，用強化學習教模型學「品味」而非「正確答案」。

8月23日，一支AI畫水彩畫的影片衝上150萬次觀看，特別的是它不是生成圖片，而是模型寫出JavaScript程式碼去「畫」出來的。原作者只公開了故事與構想，沒有公開任何模型或程式碼。Hugging Face工程師Sergio Paniego決定把整條複現路徑完整攤開發布。

🤔 **背景：這次生成的不是圖片，是畫畫的程式碼**

原始靈感來自Surya Narreddi，模型透過p5.brush這個「替p5.js加上自然繪畫工具」的函式庫，寫出JavaScript程式作畫。Narreddi的部落格文章說明了較早、較窄的訓練階段，也就是畫特寫花朵，而非影片中完整的構圖，但當時沒有公開任何artifacts，完整技術報告仍待發布。本文作者複現的重點放在工程實作面，把參考圖庫、RL環境、訓練腳本、訓練完成的模型全部公開。

🧩 **整條pipeline都跑在Hugging Face上**

訓練用Jobs執行，RL環境與評分模型部署成Spaces，pairwise judge透過Inference Providers呼叫，所有artifacts彙整在Hub上的一個collection。複現後只要架好兩個Space，設定reward mix的環境變數，就能用一行指令啟動訓練，範例中使用Qwen/Qwen3.5-35B-A3B搭配LoRA、GRPO演算法進行訓練。

🧩 **獎勵函式：兩個模型代表兩種「品味」**

文章指出，近期LLM上的RL work多半用可驗證的獎勵，例如有標準答案的數學題、能通過測試的程式碼；但這個專案更接近RLHF的路線，獎勵來自人類偏好，沒有標準答案。獎勵函式由四項組成：

| 項目 | 權重 | 衡量什麼 |
|---|---|---|
| gate | 0.05 | 程式碼能編譯、有畫出東西、沒有作弊 |
| length | 0.05 | 溫和引導產生較長的程式碼片段 |
| pairwise judge | 0.60 | 風格是否貼近參考圖庫 |
| HPSv3 | 0.30 | 渲染結果的美學偏好 |

HPSv3是一個開源的7B偏好模型，訓練自大量人類對圖片配對的選擇，分數代表多數人偏好的平均值；pairwise judge則是透過HF Inference Providers呼叫的Qwen3-VL-30B-A3B-Instruct，讓候選畫作與從圖庫隨機抽出的四張參考圖並列比較，並附上該注意哪些特徵（暈染、半透明水漬、柔邊）的文字說明，每次比較都會交換呈現順序各跑一次，最終分數是候選畫作贏得比較的比例。

🧩 **三組訓練跑法，只改獎勵比例**

作者訓練了三個run，差別只在pairwise judge與HPSv3的權重分配：judge-led（judge 0.60／HPSv3 0.30，原始配方，跑到第110步）、hps-led（judge 0.30／HPSv3 0.60，中間點，跑到第110步）、hps-only（judge 0.00／HPSv3 0.90，驗證用，跑到第60步）。作者先用hps-only確認pipeline能否學起來，確認獎勵在上升、指標健康後，才啟動兩個更長的run。

💡 **深入分析：把權重交給pairwise judge，等於把「多數人的品味」換成「作者自己的品味」**

judge權重越高，獎勵函式反映的就越接近作者自己在圖庫裡標註的偏好，而非普遍審美，理論上應該更難提升分數，甚至在風格與平均審美差太遠時讓訓練停滯不前。但文章提到，兩個開啟pairwise judge的run最終都順利學起來，代表用手動標註的圖庫確實能引導policy往特定風格前進。模型輸出約150行JavaScript程式碼，風格上的限制來自於只允許使用該函式庫的十個方法。

⚠️ **限制**

文章明白指出，前沿模型本來就能單靠prompt生成畫水彩畫的JavaScript程式碼，這不是這個專案要解決的問題；真正的工作是教一個更小的模型，結合特定個人的藝術偏好去畫畫，而不是比拚生成能力本身。

🎯 **實務啟示**

這個專案示範了一種可以直接搬到其他「品味類」任務的RL套路：用可驗證的gate、length獎勵把輸出限制在合法範圍內，再疊加一個開源偏好模型與一個LLM-as-judge，兩者權重可依需求調整。對想在自己的agent或生成任務上做偏好對齊、卻沒有現成標準答案的工程師，這套獎勵設計與全部跑在Hugging Face上的pipeline（Jobs訓練、Spaces環境、Inference Providers judge）是可以直接參考的架構樣板。

🔗 **來源**
- 標題：Training a coding model to paint watercolours with TRL and OpenEnv
- 作者／機構：Sergio Paniego，Hugging Face
- 連結：https://huggingface.co/blog/train-to-paint-with-code

#ReinforcementLearning #TRL #OpenEnv #GRPO #HuggingFace #GenerativeArt #LLM #RLHF #CreativeAI #OpenSource
