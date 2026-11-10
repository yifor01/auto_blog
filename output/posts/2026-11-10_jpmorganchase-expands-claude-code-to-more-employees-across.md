---
title: JPMorganChase expands Claude Code to more employees across the firm
source: Claude Blog
url: https://claude.com/resources/articles/jpmorganchase-expands-claude-code
model: claude-code/sonnet
generated_at: '2026-11-10T00:48:02.374675'
pinned: true
---

📌 JPMorganChase 擴大導入 Claude Code，從工程師延伸到產品與顧問團隊

TL;DR：這家大型受監管銀行把 Claude Code 從軟體工程擴展到風控、顧問與資安，並公開了它的治理框架。

當一家全球性金融機構願意公開說「我們讓 AI agent 寫程式碼、做資安分析、甚至碰觸投資顧問的日常工作」，外界通常會先問一句：那風控怎麼做？JPMorganChase 這次對外說明的，正是答案的那一部分。

🤔 **從工程團隊擴展到非技術部門**

JPMorganChase 正在把 Claude 推廣到工程師以外的更多員工。在 Commercial and Investment Bank 部門，工作能更快進入上線階段，釋出的產能被重新投入到業務優先事項上。團隊也在用 Claude 現代化其他舊系統，工程師自行建置 pull request 審查 agent 與「自我修復」agent，並在內部分享做法。基礎設施與維運團隊則用 Claude Code 處理監控、告警與根因分析；資安團隊則運用 Anthropic 的前沿模型加快找出並修補弱點，這部分工作此前已在 Project Glasswing 中揭露過。

🧩 **產品與顧問團隊也開始用 Claude**

非技術團隊的應用同樣在推進：產品團隊直接把需求轉成工程待辦清單，其他團隊則用 Claude Code 執行風險與控制評估、專案規劃。在 Asset & Wealth Management 部門，JPMorganChase 把最懂業務與最有想法的人，與技術、產品專家一起編入小而被充分授權的團隊，藉此更容易為客戶規模化打造客製化的投資解決方案；Claude Code 已成為該部門工程流程的一部分，團隊在加快速度的同時，也讓每項變更接受更嚴格的測試後才交付給客戶。上個月，J.P. Morgan Asset Management 也宣布推出連接器，把 55ip 的 ActiveTax Technology® 整合進 Claude for Financial Advisors，讓具稅務考量的投資組合轉換分析成為顧問日常工作的一部分。

⚠️ **為受監管機構設計的治理模式**

Claude Code 在受控環境中執行，包括該行自建的容器化開發平臺 Devspace，並運行在自家基礎設施上，目的是避免 agent 直接取得員工憑證或存取內部系統。權限開放是分階段進行的,新的 Claude 模型在員工能使用前，須先通過該行自己的審核流程。程式碼上線同樣受到嚴格把關：每項變更都要經過上千個自動化測試與核准關卡，其中一道自動化關卡會回傳「通過」或「暫停」的硬性判定，並由流程強制執行,確保 Claude 無法替自己的工作背書；每一次正式環境的變更，最終都由真人負責。

🎯 **實務啟示**

JPMorganChase 過去一年對 Claude 的使用，已經從軟體工程擴散到資安防禦、再到金融顧問工具,而文章也指出，這家公司對 Anthropic 提出的需求，正在影響 Anthropic 為其他受監管機構打造產品的方向。對正在評估在合規要求嚴格環境中導入 AI agent 的團隊而言,這裡展示的「分階段開放權限＋隔離執行環境＋自動化關卡把關＋人員最終負責」架構,是一個具體可參考的治理範本,而不只是單純的工具導入案例。

🔗 **來源**
- 標題：JPMorganChase expands Claude Code to more employees across the firm
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/jpmorganchase-expands-claude-code

#Anthropic #Claude #ClaudeCode #EnterpriseAI #FinTech #AIAgents #Fintech #RegulatedIndustries #AIAdoption #DevSecOps
