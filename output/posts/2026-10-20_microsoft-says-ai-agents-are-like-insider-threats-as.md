---
title: Microsoft says AI agents are like insider threats as ‘frontier models can’t
  be trusted’
source: TechCrunch AI
url: https://techcrunch.com/2026/10/19/microsoft-says-ai-agents-are-like-insider-threats-as-frontier-models-cant-be-trusted/
model: claude-code/sonnet
generated_at: '2026-10-20T20:55:28.803619'
score: 84
---

📌 微軟：別信任前沿模型，連自家 AI 都要被看管

TL;DR：微軟推出 Guardian Agents，把企業部署的 AI agent 視為潛在內部威脅並加以監控。

一家與 OpenAI、Anthropic 關係密切、甚至自己也有 AI 實驗室的公司，公開說「前沿模型不能被信任」——而且說的不是對手的模型,是所有模型,包含自家的。這正是微軟這次安全產品發表釋放出的訊號。

🤔 **從「防外部駭客」到「防自家 agent」**

微軟週一發表新的安全功能，核心是 Guardian Agents，屬於今年 6 月推出的 Project Perception 的一部分。Project Perception 原本是微軟對 Anthropic 的 Mythos、Fable 等駭客模型，以及 OpenAI 漏洞掃描系統 Daybreak 的回應，當初設計了三種角色的 agent：扮演駭客發動攻擊的「red team」、偵測並評估 red team 發現漏洞的「blue team」，以及負責修復的「green team」。這套架構的前提假設是 AI 駭客來自企業外部。

但微軟執行長 Satya Nadella 近期多次公開警告，真正的敵人可能就是企業自己部署、付費使用的那些 agent，如同一名「內鬼」（insider threat）。他在個人部落格中寫道，企業應該停止信任 AI 模型供應商，即便對方做出安全保證也一樣，並呼籲企業建立「不受 AI 實驗室控制」的獨立系統來監看和管控這些 agent：「我們無法把智慧體代為我們採取行動的責任外包出去。模型供應商的保證並不能免除我們的責任……我們需要把『智慧的供應』與『智慧的控制權』分開。」

微軟安全業務負責人 Hayete Gallot 在發表 Guardian Agents 時說得更直白：「不幸的是，無論來源為何，前沿模型都不可信任」,原因不是它們惡意或容易被駭，而是它們「不可預測」——它們被訓練來完成任務，而非遵循組織規範或判斷；再加上它們往往被賦予存取敏感資料與執行關鍵任務的權限，風險因此被放大。

💡 **矛盾的立場，但邏輯站得住腳**

這個主張對微軟而言頗為矛盾：微軟投資了 OpenAI 與 Anthropic 兩家公司，OpenAI 也是其雲端最大客戶之一，微軟自己也有 AI 實驗室,換句話說,微軟正在為自家部分商業利益製造不信任感。另一方面,這也相當自利:微軟希望企業向身為雲端供應商的自己購買 agent 安全產品,而非向 Anthropic、OpenAI 購買。但撇開利益衝突,這套邏輯本身有其道理——監控 agent 行為的軟體理應獨立於 agent 供應商之外,就像稽核人員必須獨立於被稽核的組織。

🧩 **具體功能：偵測、限權、人工核准**

除了 Guardian Agents,微軟也在 Microsoft Defender 中加入 agent 偵測功能,可找出員工私自帶進職場的多達 60 種 agent,包括 Claude Code、Codex 與 OpenClaw。另外還新增限制 agent 存取資料與系統的功能,並能依任務動態調整 agent 權限,當 agent 做出高風險決策時要求人工核准。

這種「把 agent 當作內部威脅」的思維正在業界擴散:微軟是 Nvidia 新推出的 Open Agent Safety Platform 的創始成員,該平臺已獲得超過 100 家科技公司支持,它讓 agent 運作在隔離的安全環境中,並可透過硬體層級監控與停止其行為,類似「斷電開關」。這也延續了微軟先前發表、搭載 Nvidia 晶片並內建 agent 安全控管的 Surface Laptop Ultra PC。

🎯 **實務啟示**

如果你的團隊正在企業內部部署 agent,這波動作提示一個現實:agent 的監控與治理機制,最好不要完全交由提供模型的同一家供應商來做。在設計 agent 權限模型時,把「誰能賦予權限」與「誰能監控行為」分開,是值得現在就評估的架構原則,而不是等出事才補。

🔗 **來源**
- 標題：Microsoft says AI agents are like insider threats as 'frontier models can't be trusted'
- 作者／機構：Julie Bort, TechCrunch AI
- 連結：https://techcrunch.com/2026/10/19/microsoft-says-ai-agents-are-like-insider-threats-as-frontier-models-cant-be-trusted/

#Microsoft #AgentSecurity #AIGovernance #InsiderThreat #ProjectPerception #GuardianAgents #Nvidia #EnterpriseAI #Satya Nadella #AgenticAI
