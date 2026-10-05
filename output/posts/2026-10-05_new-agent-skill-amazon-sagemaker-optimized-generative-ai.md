---
title: 'New agent skill: Amazon SageMaker optimized generative AI inference for your
  coding agent'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/new-agent-skill-amazon-sagemaker-optimized-generative-ai-inference-for-your-coding-agent/
model: claude-code/sonnet
generated_at: '2026-10-05T23:26:06.364301'
score: 82
---

📌 讓coding agent懂SageMaker推理最佳化：aws-ai-ml技能上線

TL;DR：裝上aws-ai-ml技能，Kiro、Claude Code、Codex都能幫你benchmark端點、推薦部署設定並產出可執行程式碼。

多數工程師在部署大型語言模型時,面對的不是模型本身，而是Amazon SageMaker AI那片廣闊又深不見底的設定表面：該選哪個instance家族？哪種serving容器？on-demand還是保留容量？多數人帶著的其實是「我要多快的回應」「我的預算上限是多少」這類目標,而不是對SageMaker底層選項的熟悉度。aws-ai-ml這個新技能,就是想補上這個落差。

🤔 **問題不是模型不夠好，是你不知道該選哪種部署設定**

SageMaker AI支援real-time、batch、asynchronous等多種serverful託管模式,搭配on-demand與保留容量、異質instance、VPC隔離、自動擴展等選項。工程師通常不是帶著「我該用哪個container」這種問題進場,而是帶著效能目標與成本上限。aws-ai-ml技能的設計目的,就是讓coding agent扮演類似solutions architect的角色,透過自然語言對話理解你的業務限制,最終產出可審閱、可修改、可在自己環境執行的SageMaker Python SDK v3程式碼。

🧩 **一個外掛，讓任何支援MCP的coding agent變成推理最佳化專家**

aws-ai-ml是透過Agent Toolkit for AWS安裝的工具包,可以外掛到任何支援Model Context Protocol（MCP）的coding agent,包括Kiro、Claude Code與Codex。整個過程中,agent每一步都以程式碼形式呈現、可供審閱與提問,不會隱藏在不透明的UI介面後面。

安裝方式有兩條路：
1. 本機安裝：先裝好Agent Toolkit for AWS（需要AWS CLI 2.35以上版本與uv）,它會自動偵測你的agent、安裝技能並設定AWS MCP伺服器,之後安裝aws-ai-ml技能,在agent聊天視窗問「What skills are available?」確認技能已載入,之後就能用自然語言描述需求。
2. 在Amazon SageMaker Studio的JupyterLab空間中使用：開啟Studio,建立一個私人的JupyterLab空間（技能僅會同步到私人空間）,在映像檔選單中選擇已內建aws-ai-ml技能的映像檔,啟動空間後在終端機中以身分提供者授權coding agent,同樣以「What skills are available?」確認。文章也提醒,若技能列表是空的,可嘗試重啟Jupyter伺服器再重新整理頁面。

必要條件只有一項：你的AWS憑證要有呼叫SageMaker AI API（建立端點、執行benchmark與推薦任務）的權限,技能產出的程式碼會以你的憑證執行,技能本身不需要額外的IAM設定。文章也提到,Kiro與Claude Code可以在執行期透過AWS MCP伺服器動態搜尋並載入技能,不必事先本機安裝。

💡 **三種核心用法：benchmark、選instance、比對結果**

- **Benchmark既有端點**：告訴agent要測哪個端點,它會用SageMaker Python SDK的Workload.synthetic()與start_benchmark() API產出一份Python notebook來做負載測試。因為benchmark會對正式端點送出真實流量,agent會先確認端點適合做負載測試。測完後拿到的是實測吞吐量、延遲百分位等數據報告,而非估算值,agent也會建議像prefill decoding這類提升效能的機制。範例提問：「Benchmark my Llama endpoint on SageMaker AI.」
- **幫模型挑合適的instance**：不論模型放在哪裡、怎麼取得的,agent都能產出程式碼去評估模型在候選instance與設定組合下的表現,並依吞吐量、延遲百分位、time-to-first-token與併發量列出排序後的部署選項,讓你依成本與效能需求自行決定。
- **比對兩次benchmark結果**：提供兩個benchmark job名稱,agent會算出吞吐量、延遲百分位、time-to-first-token等指標的變化百分比（正值代表變好）。若其中一次benchmark還沒跑過,agent會主動提議先跑完再比對。範例提問：「I have two benchmark runs and I want to compare them. Which one is faster?」

⚠️ **這是工具整合,不是新模型或新演算法**

這則發布本質上是把既有的SageMaker AI推理最佳化能力,透過MCP包裝成coding agent可呼叫的技能,屬於開發體驗層面的增量改進,而非底層推理技術的突破。

🎯 **對工程團隊的實務意義**

如果你的團隊已經在用Kiro、Claude Code或Codex這類coding agent,裝上aws-ai-ml技能幾乎是零成本的效率提升：不必先搞懂SageMaker所有instance家族與serving容器的排列組合,只要用自然語言描述效能目標與預算,就能拿到可審閱、可直接執行的部署程式碼,把「選型」這個耗時的嘗試過程,交給agent在你的真實benchmark數據上完成。

🔗 **來源**
- 標題：New agent skill: Amazon SageMaker optimized generative AI inference for your coding agent
- 作者／機構：Mona Mona, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/new-agent-skill-amazon-sagemaker-optimized-generative-ai-inference-for-your-coding-agent/

#AWS #SageMaker #MCP #CodingAgent #ClaudeCode #LLMInference #MLOps #InferenceOptimization #AIAgent #ModelContextProtocol
