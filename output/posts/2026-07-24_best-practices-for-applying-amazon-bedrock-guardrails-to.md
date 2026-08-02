---
title: Best practices for applying Amazon Bedrock Guardrails to code generation workflows
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/best-practices-for-applying-amazon-bedrock-guardrails-to-code-generation-workflows/
model: tencent/hy3:free
generated_at: '2026-07-24T08:18:23.702700'
score: 82
---

📌 Amazon Bedrock Guardrails 應用於程式碼產生工作流程的最佳實踐  

TL;DR：正確設定 Guardrails 可在程式碼產生時同時防護不安全內容與控管成本、延遲。  

🎣 當 AI 程式設計助手如 Claude Code、Kiro、OpenAI Codex 開始產出數千字元的程式碼時，安全過濾若未妥善調整，可能造成節流、費用飆升或回應變慢。  

🤔 背景或問題  
文章指出，隨著企業大規模採用以程式碼為核心的生成式 AI 工作流程，長串串流輸出、同時進行的開發者會話以及重複的情境評估會讓 Guardrails 的預設設定面臨吞吐量挑戰。若未進行適當配置，容易導致節流錯誤、成本增加以及次佳的延遲表現。  

🧩 方法或架構  
作者說明如何針對程式碼產生的特殊特性調整 Amazon Bedrock Guardrails：  
- 啟用內容過濾器以偵測並阻擋不安全或不想要的程式碼樣式。  
- 使用 prompt attack 防護（包括 jailbreak、prompt injection、prompt leakage）來保護模型不受惡意提示影響。  
- 敏感資訊過濾器負責遮蔽與封鎖個人識別資訊（PII）。  
- 針對長串串流輸出與併發會話，調整 Guardrails 的容量與節流閾值，以維持穩定的吞吐量。  

📊 資料或結果  
雖然文章未提供具體實驗資料，但作者強調透過上述最佳設定，可以克服因不當設定而可能產生的節流錯誤、成本上升與延遲惡化問題，同時保持對不安全程式碼的全面防護。  

💡 深入分析  
內容  
文章進一步說明，這些設定不僅適用於單一助手，也能擴展至多助手、多會話的環境，幫助組織在規劃容量時獲得更可預測的資源使用與費用結構。  

⚠️ 限制  
文中提到，若未依照建議進行配置，Guardrails 在處理長串流程式碼、高併發開發者會話或重複情境評估時，可能會成為效能瓶頸，導致額外的節流、費用與延遲。  

🎯 實務啟示  
對於正在將 AI 程式設計助手納入開發管線的團隊，建議先參考此文中的配置指引：  
1. 評估自身工作流程的串流長度與併發程度。  
2. 依照內容過濾、prompt 防護與 PII 過濾的需求開啟對應的 Guardrails 功能。  
3. 根據實際流量調整節流閾值與容量規劃，以避免不必要的成本與延遲。  
如此即可在保持程式碼安全的同時，獲得更可預測的效能與費用表現。  

🔗 來源  
- 標題：Best practices for applying Amazon Bedrock Guardrails to code generation workflows  
- 作者／機構：Sandeep Singh @ AWS ML  
- 連結：https://aws.amazon.com/blogs/machine-learning/best-practices-for-applying-amazon-bedrock-guardrails-to-code-generation-workflows/  

#AWS #Bedrock #Guardrails #CodeGeneration #AIAssistant #PromptInjection #PIIFilter #CapacityPlanning #Safety #LLM
