---
title: A thousand fewer paths to root
source: OpenAI Blog
url: https://openai.com/index/a-thousand-fewer-paths-to-root
model: claude-code/sonnet
generated_at: '2026-11-04T22:43:20.294954'
pinned: true
---

📌 一套自動化管線，堵住 Linux 核心 948 條提權漏洞

TL;DR：OpenAI 建了一套自主 pipeline，自動找出、驗證並修補 948 個 Linux 核心本地提權漏洞。

標題「A thousand fewer paths to root」本身就很有意思：對攻擊者來說，從一般使用者權限爬到 root，原本有近千條路可走，現在這些路被一條一條堵掉了。

🤔 **本地提權漏洞為什麼難防**

Local privilege escalation（LPE）漏洞指的是攻擊者已經拿到一般使用者權限後，進一步奪取 root 權限的管道。Linux 核心程式碼庫龐大且持續演進，單靠人工稽核很難覆蓋所有潛在路徑。

🧩 **流程：找出 → 驗證 → 產生修補**

OpenAI 打造的是一套自主（autonomous）pipeline，整體運作可以拆成三步：
1. 找出 Linux 核心中潛在的本地提權漏洞。
2. 驗證這些漏洞是否真的可被利用（而非誤報）。
3. 自動產生對應的修補程式（patch）。

📊 **總計處理 948 個漏洞**

這套管線最終找到、驗證並產生修補程式，涵蓋 948 個 Linux 核心本地提權漏洞，規模相當可觀。

🎯 **實務啟示**

對維護大型 C 語言程式碼庫（尤其是核心層級軟體）的團隊而言，這顯示 LLM 驅動的自動化管線已經能在「漏洞發現 + 可利用性驗證 + 修補生成」這條鏈路上規模化運作，值得關注是否有類似工具可以導入自己的安全稽核流程。

🔗 **來源**
- 標題：A thousand fewer paths to root
- 作者／機構：OpenAI
- 連結：https://openai.com/index/a-thousand-fewer-paths-to-root

#OpenAI #LinuxKernel #Cybersecurity #VulnerabilityResearch #PrivilegeEscalation #AIforSecurity #AutonomousAgents #PatchGeneration #OpenSourceSecurity #LLM
