---
title: Cognition Open-Sources an Agent Plugin that Helps Secure Systems against Recent
  Cybersecurity Threats
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/24/cognition-devin-vulnerability-fixes-plugin-php2shell-nodejs-gitlab/
model: claude-code/sonnet
generated_at: '2026-10-25T19:48:02.663815'
score: 79
---

📌 Cognition把自家修漏洞SOP，包成免費Agent Skill

TL;DR：三組開源skill自動修補PHP、Node.js、GitLab重大漏洞並送出PR。

一個CVSS 10.0的漏洞，多數團隊還在手動翻CVE清單、改版本號、重建映像檔。Cognition這次做的事很直接：把他們內部用來修補漏洞的流程，包成任何讀得懂SKILL.md的coding agent都能執行的技能。

🤔 三個目標明確的漏洞
Devin Vulnerability Fixes plugin針對三個近期的重大RCE（remote code execution）通報：PHP2Shell、2026年10月21日發布的Node.js安全更新，以及CVSS滿分10.0的self-managed GitLab漏洞。這些skill可以在Devin裡執行，也能在任何讀取SKILL.md檔案的coding agent上執行。

🧩 五步驟流程，連修補的常見陷阱都寫進去
這個plugin由三組Agent Skills組成，分別找出並修補脆弱的PHP、Node.js、self-managed GitLab部署，原始碼公開在GitHub上，採MIT授權。每個skill都遵循相同的五步驟：盤點(inventory)、核准(approve)、修補(patch)、測試(test)，最後每個repo送出一個PR(ship)。

這些skill也把實務上容易踩雷的細節寫進流程：
- Debian與Ubuntu常用backport方式修補，不會改變upstream版本號，單靠`php -v`可能誤判（例如Ubuntu 24.04的修復版本其實是`8.3.6-0ubuntu0.24.04.13`）。
- 用digest pin住的映像檔，需要換成新的digest才算真正修補完成。
- 只改Composer的`require.php`版本限制，並不會真的修補任何東西。

🧩 怎麼安裝
在Devin App裡，從Customize進入Plugins，點Browse Marketplace搜尋「Vulnerability Fixes」即可；Devin CLI使用者可執行`devin plugins install CognitionAI/devin-marketplace#plugins/devin-vuln-fixes`；其他agent可用`npx skills add CognitionAI/devin-vuln-fixes`；Claude Code使用者則是加入該marketplace後執行`/plugin install vuln-fixes@cognition-skills`。安裝後可以直接用自然語言下指令，例如「幫我修PHP漏洞」，也支援`/fix-php-vuln`、`/fix-node-vuln`、`/fix-gitlab-vuln`這類slash指令。

⚠️ 跟Dependabot不是做同一件事
報導特別點出定位差異：Dependabot與常見的code-fix agent，處理的是應用程式依賴套件與原始碼層級的問題；Cognition這個plugin瞄準的是runtime layer，也就是base image、OS套件與infrastructure-as-code，兩者是互補而非取代關係。

🎯 實務啟示
對維運大量repo與base image的團隊來說，把「盤點→核准→修補→測試→送PR」標準化成可重複執行的agent skill，確實能減少手動對照CVE清單的瑣碎工作，也讓修補過程更容易稽核。但值得留意的是，這套流程的本質是把Cognition既有的內部SOP包裝並開源，而不是全新的修補技術；導入前仍建議先在測試環境確認agent產出的PR是否符合預期，再放行到production。

🔗 來源
- 標題：Cognition Open-Sources an Agent Plugin that Helps Secure Systems against Recent Cybersecurity Threats
- 作者／機構：Michal Sutter（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/10/24/cognition-devin-vulnerability-fixes-plugin-php2shell-nodejs-gitlab/

#DevSecOps #AgentSkills #Cognition #Devin #VulnerabilityManagement #CyberSecurity #CodingAgents #RCE #OpenSource #AppSec
