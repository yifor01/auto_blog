---
title: 'UAEF: A framework-agnostic system for closed-loop evaluation of AI agents'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/uaef-a-framework-agnostic-system-for-closed-loop-evaluation-of-ai-agents/
model: claude-code/sonnet
generated_at: '2026-11-11T23:50:25.720612'
score: 95
---

📌 AWS推UAEF:讓不同agent框架共用同一套評估標準

TL;DR:AWS發布UAEF,用adapter統一LangGraph、Strands等不同框架的trace格式,以36項指標跨框架評估agent品質。

同一家公司可能同時用LangGraph、LangChain、Strands Agents、Amazon Bedrock AgentCore跑不同的agent,但換一個框架,過去累積的評估指標、分數邏輯幾乎得重寫一遍。這正是AWS這篇文章想解決的問題。

🤔 背景:評估工具跟著框架綁死,換框架就要重做一次

不同agent框架記錄執行軌跡(trace)的方式各不相同,訊息結構、tool call格式、agent間的交接邏輯都不一樣。評估工具往往也跟著某個框架的trace格式打造指標、計分邏輯與結果儲存,一旦換框架或同時跑多個框架,就得重建一套。這讓一個基本問題變得難回答:換了prompt、模型或工具之後,agent到底有沒有變好?要回答這個問題,需要跨版本一致的指標,以及可供比對的歷史結果庫。同時,agent品質也涵蓋多個維度,tool calling、回應品質、responsible AI、效能、多輪對話、多agent協作、推理,單一準確率分數無法涵蓋。

🧩 架構:用adapter把所有框架的trace轉成同一種格式

UAEF是一個框架無關的評估系統,輸入是現有的agent與一份測試資料集。資料集提供每個測試案例的輸入,也可以附上ground truth(預期輸出);若要評估tool calling,ground truth還需包含預期呼叫哪些工具、順序與參數。整個流程是:

1. Adapter讀取agent原生的執行紀錄(訊息、tool call、agent間交接),轉換成統一的AgentTrace格式,不論原始框架是什麼,後續步驟都一致。
2. UAEF在儲存資料前先篩查trace中的PII(如email、電話、信用卡號)。
3. 評估引擎從36項內建指標、7個品質維度中挑選,對trace計分。
4. 執行結果作為一次「實驗」存入Amazon DynamoDB(中繼資料,供列表與比對)與Amazon S3(完整結果)。
5. 系統產出報告與洞察,說明哪裡變好或變差,驅動下一輪修改prompt、模型或工具的決策,形成closed loop。

trace的來源有兩種:一種是已存在的歷史紀錄、log或observability store(如Langfuse)直接交給對應adapter轉換;另一種是UAEF直接呼叫agent本身(透過runtime ARN或HTTP endpoint),對資料集逐筆跑過一次並即時轉換trace。

7個品質維度分別是:tool calling(工具選擇、順序、參數是否正確)、response quality(答案是否相關、完整、準確且有依據而非幻覺)、responsible AI(安全性、偏見、毒性、對prompt injection的抵抗力)、performance(延遲、token用量、吞吐量等運作成本)、multi-turn(多輪對話的上下文保持、連貫性與目標完成度)、multi-agent(多agent協作中的任務分派與分工)、reasoning(思維鏈的內部邏輯一致性)。每個指標回傳[0,1]區間的標準化分數,讓各維度與整體結果能放在同一尺度比較。

指標分兩類:deterministic指標直接從trace與ground truth算出分數,可重現;LLM-as-a-judge指標則用Amazon Bedrock上的裁判模型評分那些難以用公式定義的品質,例如回應相關性或安全性。團隊也可以加入自訂指標,或整合RAGAS、DeepEval。

💡 安全細節:避免agent操控自己的裁判分數

因為judge指標把agent自己的輸出餵回prompt,這段內容會被當作不可信輸入處理:rubric與內容分開傳送,內容會被escape避免跳出delimiter被當成指令解讀;每個裁判回應都嚴格解析,且必須引用它所評分內容中逐字出現的片段作為證據,找不到對應證據的分數會被拒絕而非記錄下來。文中也特別提醒,judge分數是評估訊號,不該用來當作安全管控的閘門,若要在agent runtime上做安全管控,應另外搭配Amazon Bedrock Guardrails。完整的安全模型記載在SECURITY.md。

📊 採用情況

文章提到電信、醫療、金融服務產業共12家組織已使用UAEF,以同一套指標評估agent,並在發布前比較不同版本。

🎯 實務啟示

如果團隊同時維護跨框架的agent,UAEF示範的「adapter正規化先行、評分邏輯後置」架構,是解決評估工具被框架綁死問題的務實做法;把每次評估存成可比對的實驗記錄,也讓「這次改prompt到底有沒有變好」這個日常問題有了可重複驗證的答案。LLM-as-judge的防注入設計(分離rubric與內容、要求逐字證據)也值得在自建評估系統時參考。

🔗 來源
- 標題:UAEF: A framework-agnostic system for closed-loop evaluation of AI agents
- 作者/機構:Samaneh Aminikhanghahi / AWS Machine Learning Blog
- 連結:https://aws.amazon.com/blogs/machine-learning/uaef-a-framework-agnostic-system-for-closed-loop-evaluation-of-ai-agents/

#AWS #AIAgents #AgentEvaluation #LangGraph #Bedrock #MLOps #LLMOps #AIObservability #MachineLearning #GenAI
