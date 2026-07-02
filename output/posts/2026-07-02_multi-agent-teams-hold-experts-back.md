---
title: Multi-Agent Teams Hold Experts Back
source: Apple ML
url: https://machinelearning.apple.com/research/multi-agent-teams-experts
score: 96
model: google/gemma-4-31b-it:free
generated_at: '2026-07-02T19:49:57.578266'
---

📌 【Apple 研究】多代理團隊反而拖累專家？自組織 LLM 團隊的協作陷阱

TL;DR：研究發現自組織 LLM 團隊無法有效利用專家能力，效能甚至比單一專家低 41.1%。

當我們將多個 LLM 代理（Agents）組成團隊，並讓它們自由互動而非執行固定工作流時，我們直覺地認為「集思廣益」能產生協同效應。但事實上，這種自組織的協作模式可能反而成了專家的絆腳石。

🤔 **自組織協作能否產生協同效應？**

目前的多代理系統正逐漸從「固定工作流」轉向「自主協作」，讓代理之間自由互動以產生湧現的協調能力。然而，大多數研究仍依賴預設角色或聚合規則來強制協調。Apple 的這項研究探討了一個核心問題：在沒有約束的自組織團隊中，LLM 能否實現強大的協同效應（Synergy），使團隊表現達到或超越最優秀的個體成員？

📊 **效能不升反降，最高損失達 41.1%**

研究人員在人類啟發的基準測試與前沿 ML 基準測試中發現，LLM 團隊的表現與人類團隊截然不同：

- **無法匹配專家效能**：LLM 團隊始終無法達到其團隊中最強代理（專家）的表現。
- **明確告知也無效**：即便明確告知誰是專家，團隊效能依然下滑。
- **效能損失嚴重**：在 ML 基準測試中，效能損失最高達 41.1%。

💡 **瓶頸不在「辨識」，而是在「利用」**

透過對失敗原因的分解與對話分析，研究揭露了 LLM 團隊協作的深層問題：

- **整合式妥協（Integrative Compromise）**：LLM 傾向於在專家與非專家之間採取「平均化」的折衷方案，而非根據專業程度給予適當權重。
- **規模負面影響**：這種追求共識的行為會隨著團隊規模增加而加劇，且與效能呈負相關。
- **魯棒性與效能的權衡**：有趣的是，這種追求共識的行為雖然降低了效能，卻提升了對對抗性代理（Adversarial Agents）的魯棒性。這顯示了在「對齊」與「有效利用專業知識」之間存在權衡。

🎯 **實務啟示**

對於開發多代理系統的工程師來說，這項研究提供了一個重要警訊：簡單地將多個 LLM 組合在一起並讓其「自由討論」，並不等同於提升能力。若要有效利用專家代理的知識，不能僅依賴自發性的對話，而需要設計能有效權衡專業權重、避免盲目追求共識的協調機制。

🔗 **來源**
- 標題：Multi-Agent Teams Hold Experts Back
- 作者／機構：Aneesh Pappu, Batu El, Hancheng Cao, Carmelo di Nolfo, Yanchao Sun, Meng Cao, James Zou @ Stanford University, Emory University
- 連結：https://machinelearning.apple.com/research/multi-agent-teams-experts

#LLM #MultiAgent #MachineLearning #AppleML #Collaboration #AI #Expertise #ICML #AutonomousAgents #OrganizationalPsychology
