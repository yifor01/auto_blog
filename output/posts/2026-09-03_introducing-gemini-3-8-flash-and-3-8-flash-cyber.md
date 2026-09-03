---
title: Introducing Gemini 3.8 Flash and 3.8 Flash Cyber
source: Google DeepMind
url: https://deepmind.google/blog/introducing-gemini-3-8-flash-and-38-flash-cyber/
model: claude-code/sonnet
generated_at: '2026-09-03T20:09:42.227974'
score: 124
---

📌 【Google DeepMind】Gemini 3.8 Flash登場：同核心模型，資安版2小時抓到重大漏洞

TL;DR：Google六週內三度更新Flash模型，新推資安專用版，防禦效能大幅超前但僅開放受信任機構。

從發布3.7 Flash算起才三週，Google DeepMind就交出3.8，這已經是六週內第三次Flash發布。這次更新到底是持續逼近前沿的高頻迭代，還是換湯不換藥的包裝更新？

🤔 **背景：兩個變體，同一套基礎智慧**

這次推出的Gemini 3.8有兩個版本：Gemini 3.8 Flash，定位為工作馬（workhorse）模型，主打軟體工程、agentic任務與特定領域的多步驟推理；以及Gemini 3.8 Flash Cyber，鎖定漏洞偵測與自動修補的資安專用模型，透過新推出的Fairwind Program開放給受信任的防禦方。官方說明兩者共用同一套基礎智慧，並透過長時間運作的agentic loop反覆評估與精進底層模型，資安領域的高強度訓練也回饋提升了共用核心的coding與推理能力。

🧩 **3.8 Flash：設計上就是「多做一步」**

官方指出效能提升的核心設計選擇是模型會更努力工作，在複雜任務上執行更多推理步驟、反覆呼叫工具，效果拉高時也可能用掉更多token，尤其在較高的effort等級。對計算成本敏感的應用，開發者可以調低effort等級，或繼續使用仍完整支援、效率優先的Gemini 3.7 Flash。

📊 **數據看效能**

- DeepSWE v1.1（長時程軟體工程benchmark）：3.8 Flash在自主解決複雜工程問題的端到端表現上，超越多數更大型的前沿模型，成本卻低上許多
- Vals Finance Agent V2、Harvey's Legal Agent Benchmark：3.8 Flash優於3.7 Flash與其他前沿模型
- HLE-Verified：達到54.9%，展現跨STEM、人文、專業領域的多步驟推理能力
- CyberGym（業界標準漏洞探索benchmark）：3.8 Flash Cyber達到前沿等級表現，超越3.5 Flash Cyber與更大型的前沿模型
- 內部橫跨20種程式語言的自建benchmark：成功率超過70%
- CWE-Bench（由Collinear執行）的修補能力測試：3.8 Flash Cyber pass@1達47.2%，逼近某領先前沿模型的47.8%，成本卻明顯更低

在實際場域，Chrome Security團隊發現3.8 Flash Cyber產出的正確修補數量是同類更大型商用模型的2.6倍；Wiz的內部滲透測試benchmark顯示，3.8 Flash Cyber的召回率高出7.5%至9.7%，成本卻只要對手的1/2.3至1/5.2；Google Cloud Vulnerability Research團隊更用它在不到2小時內找到一個原本需要數月研究的關鍵基礎漏洞。

💡 **深入分析：價格不變，但准入門檻拉高**

3.8 Flash維持與3.7 Flash相同的入門價格，每百萬input token 0.75美元、output token 3.75美元。安全性上，3.8 Flash依循Frontier Safety Framework，針對化學、生物、輻射、核（CBRN）與網路攻擊濫用設有防護；3.8 Flash Cyber則採用較寬鬆的資安能力限制，因此只開放給有實際防禦需求的受信任對象。官方也提到，Gemini 3.8系列在Gray Swan的測試中，prompt injection的抵禦能力有明顯躍進。

⚠️ **限制**

3.8 Flash Cyber目前僅透過Fairwind Program開放給政府機構、關鍵基礎設施營運方與軟體維護者申請使用，一般開發者無法直接取得完整資安能力；而3.8 Flash在追求最高效果時，token用量可能明顯提高，需要依任務調整effort等級。

🎯 **實務啟示**

對一般應用開發者而言，3.8 Flash提供了在同一價格帶下更強的agentic與推理能力，值得針對長時程任務重新測試；對資安團隊來說，CWE-Bench與Chrome、Wiz的實測數字說明自動化修補已經逼近可用門檻，若符合條件，申請Fairwind Program會是值得評估的路徑。

🔗 **來源**
- 標題：Introducing Gemini 3.8 Flash and 3.8 Flash Cyber
- 作者／機構：Google DeepMind（Tulsee Doshi、Raluca Ada Popa）
- 連結：https://deepmind.google/blog/introducing-gemini-3-8-flash-and-38-flash-cyber/

#Gemini #GoogleDeepMind #LLM #Cybersecurity #AIAgents #SoftwareEngineering #VulnerabilityResearch #AISafety #CodeGeneration #AgenticAI
