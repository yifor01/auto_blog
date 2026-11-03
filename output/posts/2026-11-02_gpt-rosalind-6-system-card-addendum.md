---
title: GPT-Rosalind-6 System Card Addendum
source: Hacker News
url: https://deploymentsafety.openai.com/gpt-rosalind-6
model: claude-code/sonnet
generated_at: '2026-11-03T00:11:43.293222'
score: 81
---

📌 OpenAI推出GPT-Rosalind-6：生醫推理模型，審核後才能用

TL;DR：同款GPT-6 Astra權重，拒答門檻放寬到雙重用途生物議題，但只開放給審核通過的機構。

當一個模型在生醫研究上愈強，代表它離「幫忙設計病原體」也愈近一步——這正是OpenAI在GPT-Rosalind-6身上必須正面處理的矛盾。

🤔 **為什麼要做一個「拒答比較少」的模型**

一般前沿模型對涉及病原體、毒素、蛋白質設計等敏感查詢，會傾向保守拒答，這雖然安全，卻也擋住了合法的藥物研發與轉譯醫學需求。GPT-Rosalind-6 的做法是把「拒答少、能力強」與「存取權受控」拆開處理：它在雙重用途生物查詢上的拒答率比一般版本低，但只透過 Research 計畫提供給經過審核的科學家、研究機構、企業與政府合作夥伴，OpenAI 會審查申請者的用途、安全控管與治理機制後才授予存取權。即便拿到存取權，模型仍對生物武器化請求與其他安全議題保持拒答。

🧩 **同一套權重，只是換了一層審查邏輯**

GPT-Rosalind-6 使用與旗艦推理模型 GPT-6 Astra 完全相同的權重，OpenAI 並未為此版本新增訓練資料或額外進行後訓練（post-training）。因此它的評測策略也延續 Astra 的 Preparedness Framework（OpenAI 用來追蹤並準備前沿能力所帶來新風險的框架）：一方面重新跑了生物能力評測，另一方面也引用 Astra 的「helpful-only」評測結果作為補充證據——helpful-only 版本拿掉了安全拒答機制，用來還原安全訓練可能掩蓋的真實能力上限。

評測分兩層：High capability 評測測的是濕實驗室知識與疑難排解能力，例如 ProtocolQA Open-Ended（把公開發表的實驗步驟改成開放式問答，要求模型找出並修正刻意植入的錯誤，門檻 54%）與 TroubleshootingBench（用非公開、具有科學家親自撰寫的實驗協定，測試難以言傳的實務知識，門檻 36.4%）。Critical capability 評測則更進一步，測的是可能協助專家開發高危新型威脅的生物設計能力，包括 AAV 病毒顆粒包裝預測、SHP2 蛋白質功能預測、冠狀病毒與 ACE2 的細胞進入篩選、噗菌體與質體共演化預測。

📊 **三個生醫研究基準上，分數幾乎翻倍**

| 基準 | 說明 | Rosalind-6 | Rosalind-5.5 |
|---|---|---|---|
| MedChemBench v7 | 化學結構解讀、結構-活性關係、藥物毒性與效力預測 | 49.6% | 28.9% |
| GeneBench Pro v13 | 規劃並執行生物資料的量化分析（單次嘗試成功率） | 37.7% | 16.7% |
| LifeSciBench Gold | 來自執業生命科學家貢獻的研究任務 | 61.3% | 44.0% |

以上均取最高推理運算量（reasoning budget）下的分數，且兩版本使用相同題組，因此分數可直接對照。

💡 **風險分級：生物化學是「高」，網路安全是「關鍵」**

依 Preparedness Framework，OpenAI 將 GPT-Rosalind-6 在生物與化學領域歸類為 High capability，低於 Critical 門檻。至於其他風險維度，它沿用 GPT-6 Astra 的評估結果：在網路安全（Cybersecurity）上被列為 Critical，在 AI 自我提升（AI Self-Improvement）上則低於 High。換句話說，這個模型在生醫能力被「鬆綁」的同時，其他維度的風險分級並沒有因為用途不同而改變，依然沿用母模型最嚴格的評估結果。

⚠️ **這些評測測的是「能力片段」，不是「造成傷害的完整證據」**

OpenAI 自己強調，這些評測提供的是特定能力的證據，而非對生物傷害能力的完整測試；Critical capability 的門檻本身也只是專家判斷下的初步估計值，未來可能隨評測方法調整而改變。LifeSciBench Gold 的 94 題也是從原始題庭中排除 6 題有潛在問題後才拿來比較，顯示評測基準本身仍在持續修正。

🎯 **實務啟示**

對藥物研發、轉譯醫學團隊而言，這代表「申請審核存取」會成為用上前沿生醫 AI 能力的必要門檻，而不只是技術整合問題；治理與安全控管文件的準備,可能和技術評估本身一樣重要。

🔗 **來源**
- 標題：GPT-Rosalind-6 System Card Addendum
- 作者／機構：OpenAI（經 Hacker News 用戶 gmays 分享）
- 連結：https://deploymentsafety.openai.com/gpt-rosalind-6

#OpenAI #GPTRosalind #AIforScience #DrugDiscovery #BiosecurityAI #PreparednessFramework #DualUseAI #LLM #TrustedAccess #AIsafety
