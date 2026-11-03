---
title: 'CWE-bench v2: More coverage, quality, and transparency'
source: HuggingFace Blog
url: https://huggingface.co/blog/cwe-bench
model: claude-code/sonnet
generated_at: '2026-11-03T22:40:15.844655'
score: 78
---

📌 CWE-bench v2 公開 100 題,前沿模型仍有近兩成解不開

TL;DR：Collinear AI 擴充 CWE-bench 為公開 100 題的網路安全修補 benchmark,目前最強模型 pass@1 僅 67.8%。

一個防禦者必須預判攻擊者所有可能的入侵路徑,而且每一次都要做對——這正是 CWE-bench 想測試的能力邊界。v2 版本把這套測驗公開給所有人跑,結果顯示,即便是目前排名最高的模型,仍有近兩成的題目完全解不開。

🤔 **核心問題:能不能找到並修好安全弱點,而不破壞原功能**

CWE-bench 的任務設計很直接:agent 拿到一個真實開源 repository 的 checkout 與一段簡短指令,目標是找出並修復其中的安全弱點(security weakness),同時不能破壞既有功能。評分完全是程式化(programmatic)的,因此結果具有確定性,任何人都能複現,不需要額外成本。

v2 開放了一組公開的 100 個任務,涵蓋 91 種不同的 CWE(Common Weakness Enumeration),涵蓋範圍相當廣。團隊同時維持一組 held-out set,用來持續追蹤模型在「沒見過的題目」上的進展;如果想在這組 held-out set 上評估自己的模型,需要聯繫 cyber@collinear.ai。

🧩 **用 LLM judge panel 把關每一題的品質**

為了提升題目品質與透明度,團隊對每一題都檢查了以下幾個問題,並輔以 LLM judge panel 來把關難度與公平性:

- 指令讀起來像真實情境,而不是像評測題目?
- 每一個會被打分的行為,是否都能從指令中推論出來?
- 驗證器(verifier)檢查的是「正確行為」,而不是某一種特定修法的程式結構?
- 起始程式碼會失敗、而參考修法(reference fix)能通過嗎?
- 套用新修法後,原本的功能是否仍正常運作?
- 驗證器是否會讓「死記硬背的解法」(例如直接套用已知的上游 patch)無法通過?

每一題也都經過人工審查。公開這套題目集,正是這整套品質把關流程的延伸。

📊 **目前的排名:Gemini 4 Argon 微幅領先 Claude Opus 5.5**

本次共評估了 11 個模型,結果如下:

| 模型 | pass@1 | pass@4 |
|---|---|---|
| Gemini 4 Argon | 67.8% | 81.0% |
| Claude Opus 5.5 | 67.3% | 78.0% |

100 題中有 95 題至少被一個模型解開,顯示題目本身是可解的;但即便是排名最高的模型,仍有 19% 的題目在每一次嘗試中都失敗,代表長尾部分遠遠還沒被解決。

在成本面,DeepSeek V4.1 Flash(1017)、Claude Opus 5.5 與 Gemini 4 Argon 構成了一條 Pareto frontier:DeepSeek 以每次 rollout 0.04 美元的成本達到 57.0% pass@1,Opus 用 1.83 美元的成本再往上加十個百分點,Gemini 則以 3.92 美元的成本略微領先。

🧩 **怎麼跑:Harbor 直接從 Hugging Face repo 執行**

每個任務都是一個自成一體的 Harbor task(Docker 化環境 + 指令 + 確定性驗證器),資料集附帶 registry.json,因此 Harbor 可以直接從 Hugging Face repo 執行整套 benchmark,不需要自行 clone:

```
harbor run --repo "https://huggingface.co/datasets/collinear-ai/cwe-bench" -d cwe-bench@2.0 -k 4 \
  --agent <agent> --model <model> -- env docker \
  --allow-agent-host <model API host>
```

`-k 4` 代表每題跑 4 次嘗試,最終分數是全部 400 次試驗的平均 reward。資料集設有存取限制,須先在資料集頁面同意存取條件,並用 `hf auth login --token $HF_TOKEN --add-to-git-credential` 把 Hugging Face token 存進 git 的 credential helper,因為 Harbor 是用 git 抓取任務的。

⚠️ **這些任務同樣能拿來訓練防禦型 agent**

這些任務也被標記為 `rl-environment`,意味著同一套環境與驗證器不只能用於評估模型,也能作為訓練防禦型 agent 的 reward 來源。

🎯 **實務啟示**

對想評估自身模型網安修補能力的團隊,CWE-bench v2 提供了一套可直接重現、具成本/表現對照的公開基準;而成本與表現並非單純正相關的事實(DeepSeek 用極低成本達到不錯表現),也提醒在選模型時該把「每次 rollout 的實際花費」納入決策。

🔗 **來源**
- 標題：CWE-bench v2: More coverage, quality, and transparency
- 作者／機構：Gonzalo Gonzalez、Ajay Jagannath、Nazneen Rajani、Nathan Habib(Collinear AI)
- 連結：https://huggingface.co/blog/cwe-bench

#CyberSecurity #Benchmark #LLM #AIAgents #CWE #SecurityResearch #Claude #Gemini #DeepSeek #HuggingFace
