---
title: 'Abnormal AI: Amazon Bedrock AgentCore for agentic email security at scale'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/abnormal-ai-amazon-bedrock-agentcore-for-agentic-email-security-at-scale/
model: claude-code/sonnet
generated_at: '2026-09-15T20:32:13.513775'
score: 89
---

📌 Abnormal AI 用沙盒讓 Agent 攔截威脅郵件

TL;DR：Abnormal AI 用 Bedrock AgentCore Code Interpreter 讓 agent 具備運算沙盒，強化生產環境郵件威脅偵測。

保護超過 25% 財星 500 大企業的行為式安全服務 Abnormal AI，每天要處理數十億封郵件。當語意推理不足以判斷一封信是否為威脅時，他們讓 agent 自己動手寫程式、在沙盒裡跑分析，而這套系統目前正實際處理數十億等級的流量。

🤔 語意推理不是萬能的

大型語言模型擅長推理與語意連貫，但文中指出許多真實世界的操作並非單靠語意推理就能完成，需要真正的運算能力來做資料聚合、分析與驗證。這正是 Amazon Bedrock AgentCore Code Interpreter 補上的一塊:它是完全代管的無伺服器執行環境，以 API 形式提供，不會限定 agent 的工作流程,只提供一個沙盒讓 agent 執行指令、上傳檔案、取回結果。架構上，agent 呼叫 Code Interpreter API，即會建立一個短暫的 MicroVM 沙盒 session 來執行程式碼、處理檔案輸出入並回傳結果。這種即插即用的設計，讓已經有自己 agent 基礎架構的團隊能直接整合。Abnormal AI 的 AI 策略副總 Shrivu Shankar 表示:「幾乎任何 agent，不論是不是在寫程式，都需要一個 code interpreter 沙盒，讓它能真正地處理資料、得出答案。」

🧩 三層式偵測架構，愈往後愈難、量愈少

Abnormal AI 用三層架構處理數十億封郵件流量：第一層是啟發式規則與輕量分類器（例如邏輯迴歸），處理每天數十億等級的最大宗流量——在這個量級上跑更大的模型既昂貴又沒必要，大多數郵件不需要深度分析即可判斷。第一層不夠有把握的郵件流向第二層，由機器學習與深度學習模型做更深入的行為訊號分析,量級是每天數百萬封。最困難、原本需要人類分析師介入的案例，才交給第三層的 inline agent 處理,量級是每天數萬筆:這些 agent 接收威脅情資資料，動態寫程式在沙盒中分析，評估其在整體行為模型中的意涵後做出判斷。誤判案例會交由另一套系統學習並持續改進。

除了這條即時分類管線，Abnormal AI 還部署了一個以批次模式運作的分析師 agent：它會攝入即時管線中的誤判案例，用 Code Interpreter session 分析型態，再把改良後的啟發式規則與模型回饋給第一層與第二層。這些批次工作可能持續超過 30 分鐘，Code Interpreter session 全程維持;也可能橫跨長達一整天的作業，agent 間歇性地使用 Code Interpreter——例如先跑一個 session、在外部訓練模型，再重新呼叫 Code Interpreter 處理訓練結果。

📊 AI 原生的開發方式延伸到生產環境

Abnormal AI 目前 80% 的程式碼變更以某種形式借助 agent 完成，其中 40% 是完全由背景 agent 端到端寫成（而非僅是 AI 輔助）。他們在生產環境威脅偵測系統中使用 Code Interpreter，正是同一套 AI 原生開發理念的延伸。基於安全考量，Abnormal AI 選擇 Code Interpreter 的沙盒（無對外連線）設定。

💡 生產環境中歸納出的實務作法

文中歸納出幾項做法：給 agent 一個輕量、通用的執行框架，而不是死板的逐步流程，提供高層次原則讓 agent 自行判斷解法;Code Interpreter 不只適合寫程式的 agent，做安全分析的 agent 同樣受益於運算暫存空間，可用於資料聚合、型態分析與驗證;讓 agent 在沙盒中先用單元測試、整合測試、linting 等程式化驗證工具自我檢查，能提升輸出品質;若作業時間超過單一 Code Interpreter session 的時限（例如模型訓練），可用檔案系統做檢查點——先在 Code Interpreter 中運算、把狀態寫入檔案、到外部執行長時間操作，再重新呼叫 Code Interpreter 處理結果，前述的分析師 agent 就是用這個模式處理長達一整天的模型訓練作業。

⚠️ 限制

Code Interpreter 的單一 session 有時間上限，跨越這個上限的長時間作業（如模型訓練）無法在單一 session 內完成，必須搭配檔案系統checkpoint 的模式拆解執行。

🎯 實務啟示

把 Code Interpreter 當成 agent 的基礎設施而非單純的程式碼執行工具:不論是否是寫程式的 agent，只要涉及資料聚合、驗證這類非語意推理的工作，都可以考慮給它一個運算沙盒;同時,三層式架構（便宜模型攔大宗、複雜模型攔次難、agent 攔最難)是控制大規模 AI 推論成本的實務做法。

🔗 來源
- 標題：Abnormal AI: Amazon Bedrock AgentCore for agentic email security at scale
- 作者／機構：Aswin Vasudevan（AWS）
- 連結：https://aws.amazon.com/blogs/machine-learning/abnormal-ai-amazon-bedrock-agentcore-for-agentic-email-security-at-scale/

#AI #AgenticAI #AWS #BedrockAgentCore #EmailSecurity #CodeInterpreter #CyberSecurity #LLM #ProductionAI #AbnormalAI
