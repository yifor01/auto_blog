---
title: 'AI #192: Anthropic Is Going Public'
source: Don't Worry About the Vase
url: https://thezvi.wordpress.com/2026/10/29/ai-192-anthropic-is-going-public/
model: claude-code/sonnet
generated_at: '2026-10-29T22:11:05.307459'
score: 76
---

📌 Anthropic遞交S-1、Gemini 4登頂、ETH遭雙重證偽

TL;DR：本週AI圈三件事同時發生：Anthropic走向IPO、Google新模型刷新榜一、兩大實驗室各自用AI推翻經典複雜度假設。

同一個被廣泛相信成立多年的數學假設,在同一天被兩家互相競爭的實驗室各自獨立推翻——這不是巧合,而是AI研究推進速度已經快到讓人措手不及的訊號。這是The Zvi本週AI動態彙整中最值得工程師留意的幾條線。

🤔 Anthropic走向公開市場

本週Anthropic遞交了S-1,準備IPO,但股價區間等許多數字仍未公布。作者形容Anthropic「依然是一家令人困惑的公司」,許多舉措彼此看起來互相矛盾,這次S-1的遞交至少讓外界多一個觀察Anthropic對投資人的說法跟平時言論是否一致的窗口。

📊 Gemini 4 Carbon登上新基準榜首

Google發布新模型Gemini 4 Carbon,登上Artificial Analysis剛升級的AA v5基準指數榜首,據稱相較僅兩週前發布的Argon又是一次大幅躍進。但一般使用者目前還無法實際使用,Google只給出發布公告,實際查詢功能要等上數週才會開放。Artificial Analysis同時把自家綜合評測指數升級到v5版,新增兩個基準並升級三個既有項目,且首次讓指數的多數內容建立在私有資料集上。

🧩 兩家實驗室,同一天各自推翻ETH

Exponential Time Hypothesis(指數時間假設,ETH)過去被廣泛認為成立,如今被OpenAI與Anthropic分別用AI獨立證偽,兩邊發現的日期都追溯到10月16日,兩個反例所證明的複雜度上界都落在大約exp(O(n/√log n))這個量級。OpenAI的結果將交由Russell Impagliazzo(UC San Diego)、Ramamohan Paturi(UC San Diego)與Ryan Williams(MIT)帶領的團隊驗證——其中Impagliazzo與Paturi正是最初提出ETH假設的兩人之一。OpenAI承諾公開所有原始資料供社群獨立驗證,並出資舉辦一場研討會討論這個結果對整個領域的影響。據Anthropic統計,至少有800篇論文的論證依賴ETH為真,但OpenAI也確認目前對現有加密系統沒有影響。Anthropic表示自家這次的發現完全是透過Claude達成的。

同一時期,OpenAI另外發布了Kakeya conjecture在所有維度下的局部平滑證明,以及一個嚴謹的四維交互量子場論存在性證明(涵蓋含規範場與費米子的QCD,以及標準模型的統一完成),被認為可能角逐Fields Medal與千禧年問題等級的成果。

📊 新模型與定價動態

GPT-6.1 Terra已經上線,基準測試在依模型大小調整後,表現與GPT-6.1 Sol相當。Kimi K3.1 Pro也已發布,定價為每百萬token輸入/輸出$2/$10、快取$0.20,高速版則是$4/$20。Moonshot(Kimi背後團隊)表示會刻意壓低開源權重模型的攻擊性網路安全能力,使其低於自家pipeline能產出的上限、也低於前沿閉源模型,但會隨時間逐步放寬開源權重中可用的能力。

⚠️ 安全隱憂未解

被稱為「The Hackening」的一系列安全事件仍在持續,目前多數重大攻擊行動來自紅隊與白帽研究者,尚未造成重大實際損害。文中提到最驚悚的一起,是紅隊人員透過第三方漏洞取得了Anthropic的Slack存取權,這凸顯出OpenAI與Anthropic兩家公司核心溝通工具(都主要建立在Slack上)的供應鏈風險。

🎯 實務啟示

對工程團隊而言,這週的訊息至少有三點可行動：一是基準指數換代(如AA v5)會讓模型排名劇烈變動,評估模型時務必確認比較的是同一版本的基準;二是像ETH這種被視為穩固的理論假設都可能在短時間內被AI研究推翻,提醒我們不該把任何「已解決」的問題當成不會再被攻破的邊界;三是企業核心協作工具(Slack等SaaS)本身可能是最大的攻擊面,供應鏈安全審查不能只看自家程式碼,也要看日常依賴的第三方工具。

🔗 來源
- 標題：AI #192: Anthropic Is Going Public
- 作者／機構：TheZvi
- 連結：https://thezvi.wordpress.com/2026/10/29/ai-192-anthropic-is-going-public/

#AI #Anthropic #OpenAI #IPO #GeminiCarbon #ArtificialAnalysis #ExponentialTimeHypothesis #AIResearch #AISecurity #LLM
