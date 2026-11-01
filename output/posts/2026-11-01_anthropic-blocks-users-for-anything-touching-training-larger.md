---
title: Anthropic blocks users for anything touching training larger models
source: Hacker News
url: https://twitter.com/jiahaoshao1/status/2116475922190922088
model: claude-code/sonnet
generated_at: '2026-11-01T21:24:00.185086'
score: 53
---

📌 一則推文炸出爭議：Anthropic被控亂封「訓練模型」用戶

TL;DR：一位研究者聲稱只因工作流程碰到訓練更大模型，就被Claude降級或斷線，引發HN熱議。

如果你的研究工作流程需要提交訓練任務、跑分析，而不是直接拿Claude的輸出去蒸餾訓練競爭模型，結果卻被系統判定為「訓練競爭者」而被降級甚至斷線——這是研究者Jiahao Shao在X上拋出的指控，短時間內衝上Hacker News首頁並累積441分、247則留言。

🤔 **當事人說了什麼**

Jiahao Shao（@jiahaoshao1）在推文中表示，自己從未蒸餾（distill）Claude：訓練用的rollout資料來自一個強大的開源模型，Claude只是協助提交任務、跑分析。即便如此，他的帳號仍被標記為「training a competitor」（訓練競爭者）。他說此後只要碰到RFT、SFT，或任何牽涉訓練更大模型的操作，就會被封鎖、Opus 5.5被降級為Opus 5，或session直接被終止。他在推文中批評Anthropic用全世界的資料訓練模型，卻把付費做研究自動化的使用者當成敵人對待。

💡 **問題核心：反蒸餾政策的誤判風險**

這則指控如果屬實，反映的是平臺用來防堵「拿輸出去訓練競爭模型」的偵測機制，可能連帶誤傷正常的機器學習研究自動化流程——例如用Claude協助管理訓練任務、跑分析，而非直接拿輸出做蒸餾。這類自動化判定一旦觸發，使用者體驗到的是模型能力被動降級或session被殺，但未必能清楚申訴或還原原因。

⚠️ **目前只有單方說法**

這起事件的全部素材來自一則X推文與對應的HN討論串，材料中沒有出現Anthropic官方的回應或說明。換言之，目前能確認的只是「一位使用者公開的指控、以及它引發的大量關注」，至於平臺偵測邏輯的具體規則與是否誤判，仍待更多資訊佐證。

🎯 **給工程師的啟示**

如果你的工作流程涉及用Claude處理訓練管線、提交RFT/SFT相關任務，這起爭議提醒你：留意平臺對「訓練競爭模型」的自動化偵測可能存在誤判空間，必要時保留清楚的使用情境說明，並關注官方後續是否對這類誤判機制做出調整。

🔗 **來源**
- 標題：Anthropic blocks users for anything touching training larger models
- 作者／機構：Jiahao Shao（@jiahaoshao1），由pretext轉貼至Hacker News
- 連結：https://twitter.com/jiahaoshao1/status/2116475922190922088

#Anthropic #Claude #AIPolicy #LLM #ModelTraining #AIResearch #HackerNews #AIEthics #APIAccess #AICommunity
