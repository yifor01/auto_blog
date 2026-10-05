---
title: 'The Story of Qwen: Alibaba’s AI Models From 7B to 2.4T'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/04/the-story-of-qwen-alibabas-ai-models-from-7b-to-2-4t/
model: claude-code/sonnet
generated_at: '2026-10-05T23:29:06.156049'
score: 68
---

📌 從 70 億到 2.4 兆參數：Qwen 三年半的模型進化史

TL;DR：回顧阿里雲 Qwen 系列如何從一支聊天機器人 demo，三年半內演進成 2.4 兆參數的開源模型家族。

2023 年 4 月，阿里雲發表了一個名字取自「千問」的聊天機器人 demo。三年半後，它的後代已經以開放權重形式，推出 2.4 兆參數的模型。這是 Qwen 一路走來的故事。

🤔 2023：跟上 ChatGPT，但晚得不多

2023 年 4 月 7 日，阿里雲開始向企業客戶發放通義千問的邀請碼，名字部分取自孟子。四天後，時任 CEO 張勇在北京的阿里雲峰會上正式公開這個模型，並宣布會將其導入 DingTalk、天貓精靈等業務線。真正的轉折在同年 8 月：8 月 3 日，阿里巴巴開源了 Qwen-7B 與 Qwen-7B-Chat，直接對上 Meta 的 Llama 2。Qwen-7B 在超過 2.2 兆 token 上預訓練，context 長度為 2,048，授權則是月活躍使用者低於 1 億可免費商用。同月底，首個視覺語言分支 Qwen-VL 上線；9 月 13 日通義千問對一般大眾開放，Qwen 技術報告也在 arXiv 發布。年底，阿里巴巴釋出 72B 與 1.8B 模型，讓 Qwen 的開放權重涵蓋從筆電等級到前沿等級。

🧩 2024：三代模型、八個月，Qwen 成為開發者的預設選項

2024 年 2 月 5 日，Qwen1.5 以「Qwen2 beta版」之姿推出，涵蓋 0.5B 到 72B 的密集模型，並在每個尺寸都提供穩定的 32K context，隨後再追加一個 14B、啟用 2.7B 參數的 MoE 模型，以及家族首個破百億參數的 110B 密集模型。6 月初，Qwen2 以 5 種尺寸（0.5B 到 72B）發布，其中 Qwen2-57B-A14B 是首個開放的 MoE 旗艦，訓練資料新增 27 種語言，7B、72B 的 instruct 版本可處理 128K token；更關鍵的是授權調整，除 72B 外的所有尺寸都改用 Apache 2.0。夏天陸續推出 Qwen2-Math、Qwen2-Audio，以及能分析超過 20 分鐘影片的 Qwen2-VL。9 月 19 日的雲棲大會上，阿里巴巴一口氣釋出超過 100 個開源模型，即 Qwen2.5 系列，預訓練資料從 7 兆 token 擴大到 18 兆 token，尺寸涵蓋 0.5B 到 72B，context 達 128K、生成長度 8K。阿里巴巴表示，當時 Qwen 模型下載量已突破 4,000 萬次，在 Hugging Face 上催生超過 5 萬個衍生模型。11 月 11 日，Qwen2.5-Coder 全系列上線；11 月底，首個推理模型 QwQ-32B-Preview 以 Apache 2.0 釋出，挑戰 OpenAI 的 o1；12 月 24 日，實驗性的視覺推理模型 QVQ-72B-Preview 為這一年收尾。

📊 2025：推理與規模的軍備競賽

| 時間 | 發布內容 | 重點 |
|---|---|---|
| 1 月 26 日 | Qwen2.5-VL（3B/7B/72B） | 可操控 PC 與手機 |
| 1 月 29 日 | Qwen2.5-Max | 阿里巴巴宣稱效能超越 DeepSeek-V3 |
| 3 月 6 日 | QwQ-32B | 基於 Qwen2.5-32B、以強化學習訓練，宣稱效能可比 DeepSeek-R1（671B），VRAM 需求約 24GB 對比後者逾 1,500GB |
| 3 月 26 日 | Qwen2.5-Omni-7B | 文字／圖片／音訊／影片輸入，文字或語音輸出 |
| 4 月 29 日 | Qwen3（6 個密集模型 + 2 個 MoE） | 旗艦 Qwen3-235B-A22B，支援混合式思考模式切換，預訓練約 36 兆 token，語言覆蓋從 29 種增至 119 種 |
| 7 月 21 日 | Qwen3-235B-A22B-Instruct-2507 | 把混合思考拆回獨立版本，原生 262K context |
| 7 月 22 日 | Qwen3-Coder-480B-A35B + Qwen Code | 瞄準 agentic coding |
| 8 月 4 日 | Qwen-Image（20B MMDiT） | 專攻圖片中的文字渲染 |
| 9 月 5 日 | Qwen3-Max-Preview | 首個破兆參數的 Qwen 模型，僅開放 API |
| 9 月中旬 | Qwen3-Next-80B-A3B | 混合 Gated DeltaNet 線性注意力與 gated attention，宣稱訓練成本僅 Qwen3-32B 的 10%，32K token 以上推論吞吐量提升 10 倍 |
| 9 月 24 日 | Qwen3-Max 正式發布 | CEO 吳泳銘表示投入將超過三年 530 億美元的 AI 與雲端計畫規模 |
| 11 月 17 日 | Qwen App 公測 | 第一週下載量突破 1,000 萬次 |

💡 2026：分裂的路線與人事震盪

2026 年開局很快：1 月 26 日推出閉源推理模型 Qwen3-Max-Thinking，阿里巴巴稱其在 19 項基準上可比擬 GPT-5.2-Thinking、Claude Opus 4.5 與 Gemini 3 Pro；2 月 2 日推出面向 agentic coding 的小型混合模型 Qwen3-Coder-Next；2 月 10 日，Qwen-Image-2.0 把生成與編輯合併為單一模型。2 月 16 日除夕，阿里巴巴發表定位「agentic AI 時代」的 Qwen3.5，開放版 Qwen3.5-397B-A17B 啟用 17B／397B 參數，延續 Qwen3-Next 預覽過的混合線性注意力架構，託管版 Qwen3.5-Plus 則提供 100 萬 token context。3 月初，技術負責人林俊暘宣布卸任，是 2026 年內第三位離開的 Qwen 核心人物，後訓練負責人俞波也離職，編程負責人惠斌於 1 月已加入 Meta；據報導，導火線是團隊要拆成預訓練、後訓練與多模態三條水平線。3 月 16 日，阿里巴巴將 AI 相關單位整併到由 CEO 吳泳銘領軍的新集團之下。截至當時，阿里巴巴已釋出超過 400 個開放 Qwen 模型，累計下載超過 10 億次。4 月 2 日，專有託管模型 Qwen3.6-Plus 上線，呼應中國 AI 大廠轉向專有模型以創造營收的更大趨勢；但開放這條線並未停下，4 月 16 日面向 agentic coding 的 Qwen3.6-35B-A3B 以 Apache 2.0 釋出，之後一週內又有兩個模型跟進。

🎯 實務啟示

對選型開源基礎模型的工程團隊來說，Qwen 的時間軸本身就是一份參考指標：授權從早期的使用者數限制轉向 Apache 2.0、context 長度從 2K 一路拉到百萬級、焦點也從單純的對話模型逐漸轉向 agentic coding 與多模態。如果你的專案需要頻繁追蹤開源模型的授權條款與版本迭代速度，Qwen 系列的release 節奏（以月為單位、常伴隨架構實驗如線性注意力混合）會是觀察中國大型模型生態演進很具代表性的樣本。

🔗 來源
- 標題：The Story of Qwen: Alibaba's AI Models From 7B to 2.4T
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/10/04/the-story-of-qwen-alibabas-ai-models-from-7b-to-2-4t/

#Qwen #AlibabaCloud #OpenSourceAI #LLM #MoE #Apache2 #AgenticAI #ChineseAI #OpenWeights #AIHistory
