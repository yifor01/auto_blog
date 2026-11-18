---
title: OpenAI Releases GPT-6.2 Astra and Sol With a 20% Cheaper Astra API
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/17/openai-gpt-6-2-astra-sol-release/
model: claude-code/sonnet
generated_at: '2026-11-18T23:42:37.690496'
score: 95
---

📌 GPT-6.2 Astra、Sol 登場，Astra API 降價 20%

TL;DR：OpenAI 推出新一代 Astra／Sol 雙模型，主打用更少 output token 完成任務、降低每任務成本。

模型升級的敘事常常停在「更聰明」,但這次 OpenAI 把重點放在一個更貼近工程師錢包的指標：每個任務要花多少 token、多少錢。GPT-6.2 Astra 與 GPT-6.2 Sol 的發布,把「成本調整後的效能」擺上了檯面。

🧩 兩個分層：深度任務與日常任務

GPT-6.2 Astra 是接替 GPT-6 Astra 的前沿推理模型,主打複雜、長流程的專業工作;OpenAI 表示它能產出更貼合範本與欄位慣例的投影片、試算表與文件,也能做出更好的前端介面、遊戲與 3D 場景。GPT-6.2 Sol 則取代 GPT-6.1 Sol,作為日常使用的高效率模型。兩者都支援文字與圖片輸入、輸出文字,共享相同的 context 上限,差別在於成本與推理深度。兩個模型都不支援 reasoning effort 設為 none;OpenAI 建議保持 prompt 前綴不變、只在後面附加新指令,以提升快取重複使用率並維持跨輪次的推理一致性。兩個模型現在都已在 OpenAI API 上線,代號分別為 gpt-6.2-astra 與 gpt-6.2-sol。

📊 第三方評測:成本效益排到中段,但單任務成本明顯更低

MarkTechPost 引用 Artificial Analysis 的獨立評測數據:

| 模型 | Intelligence Index 分數(max effort) | 每任務成本 |
|---|---|---|
| Fable 5.2 | 65 | — |
| GPT-6.2 Astra | 62 | $4.00 |
| Gemini 4 Carbon | 60 | — |
| Claude Opus 5.5 | 59 | — |
| GPT-6.2 Sol | 57 | — |

值得注意的是,Sol 的分數追上了前代 GPT-6 Astra,但每任務成本僅約為後者的 15%。在法律領域基準 Harvey LAB-AA 上,Astra 通過 15.0% 的法律任務,針對法律場景調校的 Astra for Law 配置則通過 20.8%。Epoch 的 Capabilities Index 給 Astra 174 分,與 Fable 5.2 並列。

價格方面,Astra 的輸入與輸出單價較 GPT-6 Astra 下降 20%,快取輸入價格更便宜 60%;Sol 則維持 GPT-6.1 Sol 原價。若單次請求輸入超過 272K tokens,輸入與快取費率會變成兩倍,輸出費率變成 1.5 倍;批次(batch)請求為標準費率的 50%;Ultrafast 模式在 2027 年 2 月 28 日前為標準費率 3 倍,之後調整為 6 倍。

💡 「AI 自我改進」門檻

報導指出,Astra 是 OpenAI 目前發布的模型中,第一個達到「High」等級 AI 自我改進(AI self-improvement)門檻的模型。文中沒有進一步說明這個門檻的具體定義或評估方式,但這是 OpenAI 官方公告中特別標註的一點。

🎯 實務啟示

對已經在用 GPT-6 系列的團隊,Sol 用更低成本打平前代 Astra 的分數,是值得優先評估替換的目標,尤其是大量日常任務場景;真正需要前沿推理深度的工作流再上 Astra。另外,善用「保持 prompt 前綴不變、只追加新指令」這個官方建議,能直接影響快取命中率與成本,是遷移時容易忽略但效益明確的調整項目。

🔗 來源
- 標題：OpenAI Releases GPT-6.2 Astra and Sol With a 20% Cheaper Astra API
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/17/openai-gpt-6-2-astra-sol-release/

#OpenAI #GPT6 #LLM #AIModels #APIpricing #ArtificialAnalysis #AgenticAI #Benchmarking #AIInfra #MachineLearning
