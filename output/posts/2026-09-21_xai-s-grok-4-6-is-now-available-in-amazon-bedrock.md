---
title: xAI’s Grok 4.6 is now available in Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/xais-grok-4-6-is-now-available-in-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-09-21T21:19:53.746171'
score: 80
---

📌 xAI Grok 4.6 登陸 Amazon Bedrock，500K 上下文全面支援 Converse API

TL;DR：Grok 4.6 正式上架 Bedrock，補齊 runtime 端點與 Converse API，agent 開發整合門檻更低。

如果你已經在用 Amazon Bedrock 建置 agent，卻因為 xAI 模型只能走 OpenAI 相容介面而多繞一圈，這次的更新值得留意。

🤔 **從 Bedrock Mantle 到原生 Runtime 支援**

xAI 的 Grok 4.6 已於 2026 年 8 月 18 日在 Amazon Bedrock 上線，這是 xAI 在 Bedrock 上的第二款模型。先前 Grok 4.3 上線時，xAI 以模型供應商身分加入 Bedrock，但當時只能透過 Bedrock Mantle（Bedrock 中與 OpenAI 相容的推論引擎）存取。這次 Grok 4.6 大幅擴大了可用介面：同時支援 bedrock-mantle 與 bedrock-runtime 兩個端點，並且能透過 Converse API、Chat Completions API 與 Responses API 呼叫，Invoke API 則不支援。

🧩 **500K 上下文與四段推理強度**

根據 xAI 的發布資訊，Grok 4.6 提供 500K token 的上下文窗口，並支援四個等級的推理強度（reasoning effort）：low、medium、high、xhigh。xAI 表示，Grok 4.6 是在 Grok 4.5 的基礎上，針對長時間運行的 agent 與更複雜的互動、視覺任務做強化，訓練上採用了比 Grok 4.5 更長的補充訓練，使用經過篩選的模型生成資料來加強推理與技術概念，並改進了優化器與訓練流程；接著再用 Grok 4.5 針對不同推理強度、agent harness 與 STEM、軟體工程、知識型工作等領域重新生成監督式微調（SFT）軌跡，並以模型自身檢查過濾掉有問題的軌跡。之後模型再經過涵蓋通用知識工作、程式撰寫，以及核心優化、網頁開發、電腦輔助設計等特定領域的 agentic 強化學習訓練。xAI 也提到，模型在較長任務軌跡中展現出更多自我測試與驗證行為，在視覺與互動類專案上則能在單次生成就建立起較完整的結構與視覺語言。

📊 **這次 Bedrock 上新增的能力**

這篇 AWS 官方部落格整理出幾項 Grok 4.6 在 Bedrock 上「這次才有」、而非沿用自 Grok 4.3 的功能：

- **bedrock-runtime 端點**：可直接透過 AWS SDK 與標準 Bedrock 控制介面存取，不再侷限於 OpenAI 相容客戶端。
- **Converse API（含串流）**：converse 與 converse_stream 均可用，統一了跨模型的訊息格式，並可透過標準 Converse 事件（messageStart、contentBlockDelta、contentBlockStop、messageStop、metadata）處理串流，不需自行解析 SSE。
- **xhigh 推理強度**：在 Converse 中透過 additionalModelRequestFields={"reasoning_effort": "xhigh"} 設定，為需要更深入分析的任務保留更高強度選項。
- **跨區域推論**：bedrock-runtime 提供兩個推論設定檔，us.xai.grok-4.6 將流量限制在美國地理範圍內以滿足資料落地需求，global.xai.grok-4.6 則面向全球以取得最大容量池；global 版本輸入定價為每百萬 token 2.00 美元，比 us 版本的 2.20 美元便宜，因此在沒有資料落地限制的情況下通常是較佳預設選擇。
- **Amazon Bedrock Guardrails**：Grok 4.6 在 bedrock-runtime 的各 API 上皆支援 Guardrails，可設定內容過濾、禁止主題、個資（PII）遮蔽與詞彙政策，並同時檢查提示詞與模型回應，對需要長時間無人值守運行的 agent 工作流有實際意義。
- **模型呼叫日誌**：啟用後，每次呼叫的請求內容、回應內容、token 用量（含推理 token）與所使用的推論設定檔，都會被完整記錄到 CloudWatch，方便稽核 agent 的實際行為。
- **Prompt caching**：快取後的輸入 token 費用約為標準輸入費率的四分之一，對於每輪都會重送大量系統提示或文件的 agent 場景，能有效降低成本；快取套用於重複的前綴內容，因此建議把穩定不變的內容放在請求最前面，並透過 usage 區塊中的快取 token 數確認折扣是否確實生效。

模型目前接受文字與圖片輸入、輸出文字，不支援音訊、語音、影片或 embedding 模態，也不具備圖片生成能力。工具呼叫、結構化輸出、圖片輸入、串流回應與加密推理內容等功能則是延續自 Grok 4.3 上線時的支援範圍。

🎯 **實務啟示**

對已經在 Bedrock 生態系建置 agent 的團隊來說，這次更新最值得關注的是 bedrock-runtime 與 Converse API 的支援：意味著可以用同一套 SDK 與訊息格式在不同模型供應商之間切換，不必再為 Grok 系列單獨維護一套 OpenAI 相容的呼叫邏輯。若工作負載是推理密集型的長時間 agent，prompt caching 與跨區域推論設定檔的選擇（尤其是 global 版本的價格優勢）也值得在成本模型中提前納入評估。

🔗 **來源**
- 標題：xAI's Grok 4.6 is now available in Amazon Bedrock
- 作者／機構：Suheel Farooq, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/xais-grok-4-6-is-now-available-in-amazon-bedrock/

#Grok46 #AmazonBedrock #xAI #AWS #AgenticAI #LLM #CloudAI #ConverseAPI #PromptCaching #AIInfrastructure
