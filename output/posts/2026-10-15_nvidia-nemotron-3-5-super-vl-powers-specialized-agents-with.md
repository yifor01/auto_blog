---
title: NVIDIA Nemotron 3.5 Super VL Powers Specialized Agents with Multimodal Reasoning
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/
model: claude-code/sonnet
generated_at: '2026-10-15T20:41:33.850717'
score: 97
---

📌 NVIDIA Nemotron 3.5 Super VL：用多模態推理撐起企業專用 Agent

TL;DR：120B MoE 多模態模型結合推理、工具使用與視覺理解，多家企業實測延遲與成本大幅下降。

一個企業 agent 要讀文件、跨來源核對資訊、遵守公司政策、再呼叫好幾個工具——這種任務如果拆成文字模型和視覺模型兩個分開跑，上下文在兩者間傳遞本身就是一道效能瓶頸。

🤔 一個模型，同時扛文字與視覺

NVIDIA Nemotron 3.5 Super VL 是一個開放、可客製化的多模態模型，專門給這類長流程、多步驟的企業工作負載使用。它把推理、指令遵循、工具使用，和文字、圖像、文件、影片理解整合進同一個模型裡，團隊不需要再分別部署文字模型與視覺語言模型，也不用在兩者之間傳遞任務上下文。文件指出，它適用的場景包括程式碼測試與修正、跨網站的研究型檢索與驗證、從表格圖表中擷取資訊產出報告的文件理解、資安弱點辨識與威脅分級，以及影片內容的搜尋與事件分析。

在 NVIDIA 的模型體系中，Nemotron 3.5 Super VL 定位在中間層：規模較小的 Nemotron 3.5 Lightning 處理大量文字任務，前沿模型 Nemotron 3 Ultra 負責複雜的規劃與協調，而 Super VL 則專注在需要推理、工具使用與圖文理解同時出手的專用任務。

🧩 架構細節：120B MoE、蒸餾自 Ultra、兩階段視覺訓練

Super VL 採用 120B 參數的 mixture-of-experts 架構，每個 token 僅啟用 12B 參數，在模型容量與推論效率間取得平衡。模型是從 Nemotron 3 Ultra 蒸餾而來，蒸餾過程中使用的 SkewReverse loss 搭配 Ultra 原有的程式能力，一併提升了程式碼準確度。

視覺理解能力涵蓋圖表、表格、OCR、多頁文件與影片，透過兩階段 SFT 流程訓練語言與視覺元件，訓練資料結合視覺證據、推理、對話、安全性、長上下文資料與 agent 軌跡。文件理解任務中，模型可以讀懂文件裡某一頁的圖表，再對照文件其他地方的表格資訊，整合後產出摘要。NVIDIA 也透過 NeMo Data Designer 產生多樣化訓練資料，用於強化圖表理解能力。

推論端則用了混合架構、speculative decoding、context reuse 與混合精度等技術，降低 agent 重複呼叫時的推論負擔。模型訓練也獲得 Nemotron Coalition 成員的支援：Perplexity 提供的高品質資料集協助改善中期訓練，Prime Intellect 提供的環境則用於打造更好的教師模型。

開發者可以用 NVIDIA NeMo AutoModel 進行 SFT 與 LoRA 微調，教模型學會特定領域的行為；也可以用 NeMo RL 搭配 NeMo Gym 做強化學習與環境式評估。NVIDIA 同時在 Hugging Face 釋出配套的開放資料集，包括 agentic 工具使用與對話資料、金融推理與工具呼叫資料、指令遵循與對話資料、長上下文轉錄翻譯資料、公平性資料，以及 40 個視覺語言資料集。

📊 效能數據與企業實測結果

在單張 GPU 上，Super VL 針對 agentic 任務的吞吐量比同規模的其他開源模型高出最多 5 倍；在 Baseten 端點上，於 Artificial Analysis Intelligence Index 的 agentic 任務測試中超過 600 TPS。在圖表推理基準 CharXiv 上，模型得分 80.8%，相較 Nemotron 3 Nano Omni 的 63%；搭配 Python 程式碼解讀功能則拉高到 84%。它也是 OCRBench v2 排行榜上排名領先的開源模型之一。

| 模型 | Hermes Bench | LangChain Evals |
|---|---|---|
| Nemotron 3 Ultra | 56.33% | 84.3% |
| Nemotron 3.5 Super VL | 63.44% | 87.05% |

文件指出，憑藉更高的吞吐量與 token 使用效率，Super VL 的任務完成速度快了 4 倍；EXO Labs 的獨立評測也顯示，Super VL 在 NVIDIA DGX Spark 本機環境上，於準確度與任務完成時間的權衡上落在 Pareto frontier 上。

企業導入成果方面：AI 資料與技術供應商 Scale AI 為媒體娛樂公司 Skydance Corporation 的供應商信用審核流程做了後訓練，推論成本預計降低 40 倍、延遲降低 5 倍；財務營運平臺 Ramp 用它把收據圖片轉成含商家資訊、日期、付款資料的結構化 JSON，預期吞吐量提升最多 50%、延遲降低 10 倍；AI21 與 Alice 則針對威脅情報與弱點分析做後訓練，準確度提升 41%。

🎯 實務啟示

Super VL 的價值在於把「理解文件/圖像」和「推理、呼叫工具」這兩件事合併到一個模型裡，省掉模型間傳遞上下文的工程成本。如果你的 agent 任務本質上是多模態又需要多步驟工具呼叫（像是文件稽核、資安分級、收據處理），用 NeMo AutoModel 做 SFT/LoRA 針對自家資料與工具後訓練，再視任務複雜度決定是否交由 Lightning 或 Ultra 分工，會是比單押一個模型更合理的部署策略。

🔗 來源
- 標題：NVIDIA Nemotron 3.5 Super VL Powers Specialized Agents with Multimodal Reasoning
- 作者／機構：Michelle Horton（NVIDIA Developer）
- 連結：https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/

#NVIDIA #Nemotron #MultimodalAI #MixtureOfExperts #AIAgents #LLM #NeMo #EnterpriseAI #VisionLanguageModel #OpenWeights
