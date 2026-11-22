---
title: 'Security event: Prompt leakage for requests in June and July of 2026'
source: Together AI
url: https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026
model: claude-code/sonnet
generated_at: '2026-11-22T22:44:14.153686'
score: 57
---

📌 AI coding agent不小心commit金鑰，Together AI爆資料外洩

TL;DR：Together AI公告，AI coding agent誤提交私有repo憑證，導致2026年6、7月部分使用者的prompt遭下載外洩。

當大家在討論怎麼讓 AI coding agent 自動化更多開發流程時，Together AI 的這起事故提供了一個現實案例：讓 agent 碰觸憑證管理，風險可能比想像中更直接。

🤔 **事情怎麼發生的**

根據 Together AI 官方公告，這起事件源自一次例行軟體測試。團隊收集了經授權用於該用途的 prompt 樣本，存放在一個私有的 Hugging Face repository 中，樣本來自 MiniMax M3、GLM-5.2、Kimi K2.6 這幾個模型的請求，主要集中在 2026 年 6 月 24 日、7 月 4 日、7 月 8 日與 7 月 14 日。問題出在開發公開 GitHub repo「xorl」的過程中，一個 AI coding agent 把一組能存取私有 Hugging Face repo 的憑證提交了進去。公司的自動化掃描偵測到這組暴露的憑證並復原了該 commit，但在暴露的時間窗口內，有未經授權的第三方取得了這組憑證，並用它下載了儲存的 prompt 樣本。

🔍 **外洩的prompt還被拿去試其他服務的憑證**

更值得注意的是,該第三方取得樣本後，進一步在這些 prompt 內容裡搜尋是否藏有其他服務的憑證，並測試這些憑證是否仍然有效。公告指出，被測試的憑證中有五組是與 Dragos 一項安全實驗相關的 canary 憑證（即蜜罐型偵測用憑證）。Together AI 已與外部鑑識調查公司及執法機關合作調查，目前的審查結果顯示沒有發現本次事件之外的額外 prompt 外洩證據，但對受影響 prompt 內容的審查仍在進行，以確認是否有敏感個人資訊或其他客戶資料被暴露。

🛠️ **公司做了哪些調整**

公告列出事後強化的控管措施：改用有範圍限制或短期有效的憑證，並在支援的情境下採用無金鑰（keyless）存取，降低憑證一旦暴露的影響範圍；對所有 pull request 檢查是否含有憑證；將零資料保留（ZDR）設為新帳戶的預設選項；以及更新了管理 AI coding agent 使用方式的開發流程。公司也建議處理敏感 prompt 資料的客戶，在帳戶設定中啟用 ZDR，並提供 security@together.ai 供有疑慮的客戶聯繫。

🎯 **實務啟示**

這個案例值得所有在開發流程中導入 AI coding agent 的團隊留意：agent 自動 commit 的內容，同樣需要納入憑證掃描與 PR review 的範圍，不能因為是 AI 寫的就降低檢查標準。另外，「測試用 prompt 樣本」本身可能也含有敏感資訊,收集與儲存這類資料時,存取控制與保留政策（如 ZDR）的設計同樣重要,不只是防堵程式碼層級的憑證洩漏。

🔗 **來源**
- 標題：Security event: Prompt leakage for requests in June and July of 2026
- 作者／機構：Together AI
- 連結：https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026

#TogetherAI #SecurityIncident #AIAgents #CredentialLeak #DataBreach #LLMSecurity #ZeroDataRetention #AICodingAgent #InfoSec #CloudSecurity
