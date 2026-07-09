---
title: NVIDIA/SkillSpector
source: GitHub Trending
url: https://github.com/NVIDIA/SkillSpector
score: 122
model: google/gemma-4-31b-it:free
generated_at: '2026-07-09T09:46:02.277115'
---

📌 **NVIDIA SkillSpector：AI Agent 技能安全掃描工具**

TL;DR：SkillSpector 在安裝前掃描 AI Agent 技能的弱點與惡意模式，給出 0‑100 風險分數並提供明確建議，協助工程師判斷是否安全使用。

🎣 根據公開研究，高達 **26.1%** 的 Agent 技能包含弱點，**5.2%** 疑似帶有惡意行為——換句話說，每四個技能中就有一個可能藏有安全問題。當 AI Agent（如 Claude Code、Codex CLI、Gemini CLI 等）預設信任並直接執行這些技能時，未經審查的風險就會被放大。

🧩 **方法或架構**  
SkillSpector 採用 **兩階段分析**：先進行快速靜態掃描，必要時再啟用可選的 LLM 語意評估以深度檢查複雜模式。它支援多種輸入格式——可直接掃描 Git 儲存庫、網址、壓縮檔、目錄或單一檔案。內建 **68 個弱點模式**，分為 17 類別，包括提示注入、資料外洩、許可權提升、供應鏈、過度代理、輸出處理、系統提示洩漏、記憶體毒染、工具濫用、惡意代理、反拒絕、觸發濫用、危險程式碼（AST）、汙點追蹤、YARA 簽章、MCP 最小許可權以及 MCP 工具毒染。掃描過程會即時查詢 **OSV.dev** 取得最新 CVE 資料，並具備離線 fallback 機制。最終會輸出 **0‑100 風險分數**，伴隨嚴重程度標籤與具體修復建議；為降低誤報，工具接受已知發現的 glob‑規則或指紋來進行基線抑制。結果可以終端機、JSON、Markdown 或 SARIF 格式產出，方便與現有 CI/CD 流程或安全儀錶板整合。

📊 **資料或結果**  
根據專案說明檔案中引用的研究：  
- **26.1%** 的 AI Agent 技能含有可被偵測到的弱點。  
- **5.2%** 的技能顯示出可能的惡意意圖。  
這些資料凸顯了在安裝前進行自動化安全檢查的必要性，而 SkillSpector 正是為此設計的掃描工具。

💡 **深入分析**  
兩階段設計讓使用者在資源受限時仍可依靠快速靜態規則獲得即時回饋；當需要更深層語意理解時，可選擇啟用 LLM 進行額外分析，這種彈性使得工具既適合本地開發也適合雲端 CI 環境。即時的 OSV.dev 查詢確保已知漏洞能被快速捕捉，而離線 fallback 則保證在網路受限環境下仍能運作。風險分數與明確建議則幫助工程師快速決策是否接受、修改或拒絕某個技能。

⚠️ **限制**  
- 可選的 LLM 語意評估依賴外部語言模型，若未配置則僅靠靜態規則進行檢測。  
- 偵測能力受限於內建的 68 個弱點模式與 17 個類別；未涵蓋的新興攻擊手法可能漏報。  
- 雖然提供基線抑制機制，但需要使用者自行維護 glob‑規則或指紋檔案，以免誤報影響工作流程。

🎯 **實務啟示**  
開發團隊可將 SkillSpector 加入專案的預提交鉤子或 CI 流程，自動對從外部來源取得的 Agent 技能進行安全掃描；同時，透過 Pi 擴充功能，工具亦可直接嵌入 Agent 工作階段內，讓開發者在對話中即時檢查即將使用的技能是否安全。這種「掃描即使用」的流程大幅降低了因盲目信任第三方技能而導致的供應鏈風險。

🔗 **來源**  
- 標題：SkillSpector  
- 作者／機構：NVIDIA — NVIDIA  
- 連結：https://github.com/NVIDIA/SkillSpector  

#AI #AgentSecurity #SkillSpector #NVIDIA #VulnerabilityScanning #LLM #DevSecOps #OpenSource #CyberSecurity #GitHubTrending
