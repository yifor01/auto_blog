---
title: Expanding the Cyber Verification Program
source: Anthropic News
url: https://www.anthropic.com/news/cyber-verification-program
model: claude-code/sonnet
generated_at: '2026-10-06T21:47:55.000061'
pinned: true
---

📌 Anthropic 擴大 Cyber Verification Program,把攻防能力分級開放給防禦者

TL;DR:Anthropic 將網路安全驗證方案擴充為三個存取層級,讓資安團隊依工作性質申請解除 Claude 的攻防限制。

🎣 同一套能找出漏洞的能力,放在防禦者手上是修補系統的利器,放在攻擊者手上卻是武器。這正是 Anthropic 在擴大 Cyber Verification Program(CVP)時,反覆強調的「雙重用途」難題——而他們選擇用分級授權,而不是一刀切的方式來解。

🤔 為什麼 Claude 平常對 cyber 工作這麼保守

Anthropic 指出,網路安全本質上是雙重用途:同樣的能力既能幫助安全團隊找出並修補漏洞,也能幫助惡意行為者發動攻擊。因此 Claude Opus 5.5、Claude Fable 5.1、Claude Sonnet 5.5 等一般可用模型,都內建了保守的 cyber 安全防護,會封鎖大部分攻防相關任務。但防禦者同樣需要存取最強能力才能守住系統,過去半年 Anthropic 透過 Project Glasswing(開放 Claude Mythos 給守護關鍵軟體的組織)與既有 CVP(開放 Claude Opus / Sonnet 的降階防護給受驗證的資安團隊)兩個計畫提供信任存取。這次則是把兩者整合成一套擴大版方案。

🧩 三個存取層級怎麼分

- **Defense Access**:適用防禦性工作,包括 SOC 與事件應變、惡意軟體逆向工程、漏洞分析與驗證。適用對象涵蓋企業/非營利/大學/政府的資安團隊、區域醫院或市政公用事業等關鍵基礎設施營運者、中小型資安公司、開源專案維護者,以及有漏洞回報紀錄的個人研究者。Anthropic 預期多數防禦性工作團隊可在這一層獲準,審核約數天內回覆。
- **Red Team Access**:在 Defense Access 之上,加入經授權的滲透測試與紅隊演練,適用對象包括企業內部紅隊、政府紅隊、滲透測試公司。僅能對已獲授權的系統進行測試,且對可能造成實體傷害或大規模破壞的行為(如部署 ransomware、破壞實體系統、對高風險安全系統進行滲透測試)仍會即時封鎖。審核約需數週,目前僅開放給組織,個人研究者不適用;審核期間會先以 Defense Access 層級啟用。
- **Specialized Access**:封鎖最少的層級,保留給經過深度審查、可測試影響人身安全或市場運作的安全系統的組織,例如飛航操作系統、電網、電信網路、跨行轉帳基礎設施與政府行政網路。這一層由 Anthropic 與美國政府共同深度審查,現有 Project Glasswing 成員將直接轉入此層,現有模型無需重新審核。

各層級都能存取 Claude Opus 5.5、Claude Sonnet 5.5、Claude Mythos 5.1 及未來新模型。一般可用模型則仍可用於程式碼審查、修補已知問題、在自有原始碼中找漏洞,以及資安警示分流等工作。

📊 用 CyScenarioBench 驗證分級是否有效

Anthropic 以 CyScenarioBench(評估模型能否在真實限制下規劃並執行多階段攻防行動)測試 Claude Opus 5.5 在不同層級防護下的表現,針對 10 道題目各測試 5 次(共 50 次試驗):

| 存取層級 | 封鎖情況 | 成功完成任務數 |
|---|---|---|
| 無 CVP 存取 | 每個任務在第一個 prompt 就被封鎖 | 0/50 |
| Defense Access | 50 次中有 46 次在過程中被封鎖 | 4/50 |
| Red Team Access | 完全無封鎖 | 34/50(成功率 67.6%,等同無防護基準的 Specialized Access 表現) |

此外,透過 Project Glasswing,Anthropic 的合作夥伴在 2026 年 4 月至 7 月間,已找出至少 129,000 個經驗證的軟體漏洞;Anthropic 自身的開源程式碼掃描計畫則在 4 月至 10 月間額外找出 5,500 個經驗證漏洞。這些漏洞中,超過 33,000 個被評為重大或高風險等級。多個合作夥伴表示,Claude Mythos 讓他們找漏洞的速度加快了數月甚至數年。

⚠️ 幾個需要留意的限制

Anthropic 坦承,上述漏洞數據是以 33 份合作夥伴報告與開源合作為基礎,屬於部分取樣,實際影響可能被低估,甚至可能達到現有數字的 5 倍以上。另外,加入 CVP 的組織目前必須接受資料保留(以監控濫用情況),要等到今年秋季稍後上線的 Enterprise Frontier Safeguards(EFS)才能在兼顧零資料保留隱私的同時仍享有防護;在那之前,僅有已取得 Claude Fable 5.1 或 Claude Mythos 5.1 零資料保留存取權的組織,才能以零資料保留方式使用 CVP。

🎯 實務啟示

對資安團隊而言,這套分級制度提供了一條明確的申請路徑:純粹防禦工作走 Defense Access,授權紅隊演練走 Red Team Access,涉及關鍵基礎設施的高敏感測試則需走 Specialized Access 並接受更嚴格審查。選擇適合自己工作範疇的層級申請,而不是預設只能用被動保守的一般可用模型,可能是取得更強攻防輔助能力的關鍵。

🔗 來源
- 標題:Expanding the Cyber Verification Program
- 作者/機構:Anthropic
- 連結:https://www.anthropic.com/news/cyber-verification-program

#Anthropic #Claude #Cybersecurity #CyberVerificationProgram #RedTeam #VulnerabilityResearch #AIforSecurity #ClaudeOpus #ProjectGlasswing #InfoSec
