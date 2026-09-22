---
title: Evaluate skill-equipped agents with Strands Evals and Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/evaluate-skill-equipped-agents-with-strands-evals-and-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-09-22T20:39:16.374292'
score: 82
---

📌 Agent 選對了技能，卻沒照著做？AWS 推出 Skill 評測新解法

TL;DR：Strands Evals 與 Amazon Bedrock AgentCore Evaluations 新增 skill 專屬評測器，能抓出「選錯技能」與「半途而廢」兩種隱藏失敗。

一個 agent 產出流暢、看似合理的回應，不代表它真的用上了你精心設計的領域知識——這正是 skill 架構帶來的新盲點，而一般的輸出品質評分完全看不出來。

🤔 把所有流程塞進一個 system prompt，遲早會撐不住

合規檢查、文件處理流程、升級政策、工程慣例……把這些通通寫進一個 system prompt 或應用邏輯裡，維護與更新的成本會迅速失控。Skill 是一種模組化的替代方案：一個 skill 是可重複使用的一組指令，通常存放在 SKILL.md 檔案裡，教會 agent 執行特定領域任務，例如遮蔽合約敏感資訊、核對發票，或遵循團隊的 pull request 慣例。因為 skill 遵循開放的 Agent Skills 標準，可以跨相容 harness 移植，agent 在執行時也只載入當下需要的那個 skill，而不必把所有程序都塞進核心指令。

這種 skill 組合性帶來兩種一般輸出品質指標抓不到的失敗模式：agent 呼叫了不適合這個任務的 skill；或者 agent 呼叫對了 skill，卻跳過或只部分遵循了其中的指令。兩種情況都可能產出流暢、看似合理的回應，卻根本沒有真正用上你預先設計好的領域知識。想抓出這類問題，評測就不能只看最終回應。

🧩 三個 skill 評測器，分別盯緊不同環節

Strands Evals SDK 與 Amazon Bedrock AgentCore Evaluations 為此加入了三種 skill 導向的評測器：

- Skill Selection Accuracy：檢查每個被呼叫的 skill 是否適合任務，agent 是否選對了正確的 skill。
- Skill Instruction Following：評估 agent 對該 skill 規定步驟的完整遵循程度，採五級評分——Fully Followed（1.0）、Mostly Followed（0.75）、Partially Followed（0.5）、Minimally Followed（0.25）、Not Followed（0.0），達到 Mostly Followed 以上才算通過。
- SkillInvoked：純粹的確定性檢查，不呼叫任何模型，是 Strands Evals 專屬的功能。

文中舉了一個 HR 助理 agent 的例子：它同時具備 PTO（特休）規劃與員工福利兩個 skill。若員工詢問牙科、視力福利，agent 是否呼叫對了 benefits skill，屬於 Skill Selection Accuracy 要抓的路由問題。而當 agent 正確呼叫了 PTO 規劃 skill，該 skill 要求依序辨識 employee_id、檢查 PTO 餘額、對照最新 HR 政策核對 rollover 規則、才能提交 PTO 申請——如果 agent 檢查了餘額卻跳過 rollover 規則，依然可能給出看似合理的回應，但已經違反了規定流程，這正是 Skill Instruction Following 要揪出的執行失敗，並能指出具體是哪一步被跳過。

💡 兩種失敗，兩種不同的修法

選錯 skill 通常指向 skill 描述彼此重疊或定義模糊；指令遵循不完整，則可能需要更清楚的步驟拆解、不同的 skill 結構，或換一個能力更強的 agent 模型。由於 judge-based 評測器會針對每個被呼叫的 skill 回傳結果，即使是多 skill 串接的執行流程，依然可以逐一診斷——你能明確定位是哪個 selection 或 instruction-following 的結果拉低了整體分數。如果整趟執行完全沒有呼叫任何 skill，judge-based 評測器就不會產出分數，這時建議搭配 SkillInvoked 用在已知 routing 需求的 regression test 上。

AgentCore Evaluations 可以直接讀取既有的 OpenTelemetry traces，支援即時評測、對已儲存 session 做批次處理，也能對線上流量持續取樣。每個評測結果都會附上 spanContext，包含辨識出的 skill invocation 所在的 sessionId、traceId、spanId。除了兩個內建的 skill 判斷型評測器，開發者還能在 TOOL_CALL 層級自訂評測器，樣板可以引用 {invoked_skill}、{skill_content} 這類 skill 佔位符——引用了哪個佔位符，也決定了這個評測器會在什麼時機被觸發。

🎯 實務啟示

如果你的 agent 架構已經在用 skill／plugin 這類模組化方式注入領域知識，光看最終輸出的品質分數並不足夠——你需要額外檢查「有沒有選對 skill」與「有沒有照著 skill 的步驟走完」這兩層。對正在建置 HR、法遵、客服等企業級 agent 的團隊來說，這套 Skill Selection Accuracy／Skill Instruction Following／SkillInvoked 的組合，提供了一個相對具體、可落地的評測起點。

🔗 來源
- 標題：Evaluate skill-equipped agents with Strands Evals and Amazon Bedrock AgentCore
- 作者／機構：Sangmin Woo（AWS ML Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/evaluate-skill-equipped-agents-with-strands-evals-and-amazon-bedrock-agentcore/

#AWS #AgentCore #StrandsEvals #AIAgents #LLMOps #AgentEvaluation #OpenTelemetry #SkillMd #GenAI #AIObservability
