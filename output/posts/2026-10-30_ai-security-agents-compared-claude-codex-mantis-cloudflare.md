---
title: 'AI Security Agents Compared: Claude, Codex, Mantis, Cloudflare'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/30/ai-security-agents-claude-codex-mantis-cloudflare/
model: claude-code/sonnet
generated_at: '2026-10-30T21:39:05.595122'
score: 98
---

📌 四家AI安全掃描agent不約而同走向同一種架構

TL;DR：Anthropic、OpenAI、Google、Cloudflare的AI抓漏agent各自獨立開發，卻都收斂到同一個設計：找漏洞的agent,不能自己說自己對。

如果一套掃描工具抓出的漏洞,九成以上是誤報,那它對團隊來說根本是負資產。這正是四家公司不約而同要解決的問題,而它們交出的答案,驚人地相似。

🤔 **雜訊是共同敵人,攻擊者也已經動手**

MarkTechPost 整理了 Anthropic、OpenAI、Cloudflare、Google 四家各自的 AI 安全掃描 agent 後發現,問題的根源在於雜訊。Google 安全團隊指出,草率的 AI 程式碼掃描會產生大量幻覺出來的漏洞,真陽性率不到 7%。一個九成三時間都在說謊的掃描器,帶給審查者的成本遠高於它省下的時間。另一股驅動力是攻擊端已經搶先一步:Anthropic 團隊表示,其掃描器部分原因是攻擊者已經在用 AI 模型尋找可利用的漏洞(引用自 The Hacker News);Google 在介紹 Mantis 的文章開頭也提到,模型現在能在幾乎不需要人力協助的情況下發現並利用漏洞。

🧩 **共識架構:發現者與驗證者分離**

四套工具的共同骨架,是「找出者永遠不能驗證自己的發現」。Cloudflare 的 README 直接寫明這條規則;Anthropic、OpenAI、Google 也各自描述了類似的驗證流程。具體實作則各有特色:

- **Claude Security / Claude Code 外掛**:在 Claude Code session 內執行的多 agent 掃描器,是 Anthropic 託管版 Claude Security 的本地版本。多個 agent 分工繪製架構圖、建立威脅模型、跨元件搜尋並獨立驗證每項發現,輸出 Markdown 報告與相容 GitHub code scanning 的 SARIF 2.1.0 檔案,修補程式會以 F<n>.patch 的形式產生在暫存副本中,外掛本身不會自動 commit、push 或開 PR。掃描用量計入既有的 Claude 方案額度,不需額外 API key。外掛於 2026 年 7 月 22 日進入公開 beta,8 月時託管掃描器升級到 Claude Mythos 5。
- **@openai/codex-security**:以 CLI 與 TypeScript SDK 形式提供,可掃描整個儲存庫、指定路徑或 Git diff,`--mode deep` 會啟動平行探索 worker。它會驗證候選發現、產生修補程式,也能反過來驗證既有修復是否確實生效,還能透過 `cs policy` 指令生成 SECURITY.md 讓後續掃描知道什麼才算是這個專案的漏洞。輸出支援 SARIF、JSON、CSV 並可發布到 Linear。客戶端採 Apache-2.0 授權,但背後的掃描服務仍在限量 beta,目前支援 OpenAI、Amazon Bedrock、OpenRouter、Fireworks AI 作為模型供應商。
- **Cloudflare security-audit-skill**:MIT 授權的技能(skill),能讓任何支援工具呼叫與平行子 agent 的程式碼 agent 變成安全稽核員,跑完整六階段稽核,需要作業系統層級的沙箱且無外部網路存取,否則發現項目只會停留在 needs_validation 狀態而不會被執行驗證。這套約 450 行的 skill 是 Cloudflare 內部掃描框架的種子,目前已用於掃描 128 個儲存庫。
- **Google Mantis**:Apache-2.0 授權的安全審查技能與 ADK 參考框架,會讀取儲存庫歷史學習過去的安全修復模式,並建立分層摘要樹,把檔案逐層濃縮成目錄與根目錄摘要。

📊 **驗證機制確實降低了誤報**

Cloudflare 報告,更好的背景資訊(recon context)讓第一輪的拒絕率從 40% 降到 11%。Google Mantis 的分層摘要樹設計,則讓 token 開銷降低超過 85%。Mantis 的特色還包括嘗試實際重現每個漏洞(從靜態的 exploit 草圖一路做到單元測試或 mock server),並透過對抗式迴圈攻擊自己提出的修補程式,同時依據一套嚴重度量表校正,避免出現「數千個 critical」的失真結果,學到的經驗再透過 mantis-advise 回饋進程式碼生成環節。

💡 **分工背後的邏輯:確定性引擎驗證,模型負責推理**

MarkTechPost 統計,2026 年內至少還有超過 12 個以 agent 為基礎的漏洞工具上線或公開,包含 Anthropic 的 defending-code-reference-harness、Trail of Bits、Capital One 的 vulnhunter,以及 Cisco 的 ai-deep-sast(其中 Cisco 的版本完全在本地的 Foundation-Sec-8B 上執行,程式碼不會離開機器)。這些工具幾乎都重複同一套「找出後獨立驗證」的迴圈,差異主要在是開放給自行架設的免費框架,還是商用或內部平臺。這個格局背後的共同邏輯是:確定性引擎或驗證器負責證明,模型負責推理,而人類核准每一個修補。Cloudflare 的架構也暗示了一個實用組合:用一個工具或模型做發現,換另一個做驗證,因為不同模型抓到的漏洞比例本來就不一樣。

⚠️ **各家仍有明顯限制**

Codex Security 背後的掃描服務並非開源,仍限於經核准的客戶;Cloudflare 的技能若缺乏沙箱環境,驗證流程就無法真正執行;整體而言,這類工具目前仍以「輔助審查」而非「自動核准」為定位。

🎯 **實務啟示**

如果要自建或導入 AI 安全掃描流程,單一 agent 一次掃完就出報告的模式很難信任。更務實的做法是明確區分「發現」與「驗證」兩個角色,甚至讓它們使用不同模型或不同工具鏈,降低單一模型系統性誤判帶來的風險。

🔗 **來源**
- 標題:AI Security Agents Compared: Claude, Codex, Mantis, Cloudflare
- 作者/機構:Michal Sutter,MarkTechPost
- 連結:https://www.marktechpost.com/2026/10/30/ai-security-agents-claude-codex-mantis-cloudflare/

#AISecurity #VulnerabilityScanning #Claude #Anthropic #OpenAI #GoogleDeepMind #Cloudflare #SAST #AIAgents #CyberSecurity
