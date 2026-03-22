---
title: "BeyondSWE: Can Current Code Agent Survive Beyond Single-Repo Bug Fixing?"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2603.03194
score: 103
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-04T19:22:19.440918
---

📌 **Code Agent 的真實能力，遠不如你想像**

當你看到 GitHub Copilot、Cursor 等 AI 助手能快速修復單一 repo 的 bug 時，你可能以為它們已經很厲害了。但最新研究顯示，當這些 code agent 面對更複雜的現實任務時，表現其實慘不忍睹。

🤔 **單一 repo 修 bug，只是冰山一角**

目前評估 code agent 的標準，多半只看它能不能在一個 repo 內修好一個 bug。但真實開發場景遠比這複雜：

- 需要跨 repo 協作解決問題
- 需要 domain 專業知識
- 需要處理 dependency 驅動的遷移
- 需要整個 repo 的重構生成

這些能力，現有 benchmark 都沒測到。

🧪 **500 個真實案例，揭露 code agent 的真實能力**

來自中國人民大學、獨立研究員和 AweAI Team 的研究團隊，設計了 BeyondSWE 這個全新 benchmark，用 500 個真實案例測試 code agent 的極限能力。

結果很殘酷：

- 即使是最先進的模型，成功率也停滯在 45% 以下
- 沒有任何一個模型能在所有任務類型上保持穩定表現
- 跨 repo 推理、domain 專業問題、dependency 遷移，都是重大挑戰

💡 **為什麼搜尋輔助沒想像中有效？**

研究團隊還開發了 SearchSWE 框架，讓 code agent 整合深度搜尋能力。結果發現：

- 搜尋輔助帶來的收益不一致
- 在某些情況下甚至會降低表現
- 這反映出 code agent 難以模仿開發者在 coding 過程中搜尋與推理交織的工作流程

⚠️ **這代表什麼？**

這意味著當前 code agent 的能力被嚴重高估了。它們擅長的是狹隘、封閉的任務，一旦面對現實開發的複雜性，就會暴露根本性的局限。

🎯 **對開發者與研究者的啟示**

- 別被單一 repo 的修 bug 表現騙了，真實需求更複雜
- 跨 repo 協作、domain 知識整合、dependency 管理，是 code agent 的下一個挑戰
- 搜尋與推理的結合，是關鍵但困難的技術方向

🔗 **論文連結**
📝 BeyondSWE: Can Current Code Agent Survive Beyond Single-Repo Bug Fixing?
👤 Guoxin Chen, Fanzhe Meng, Jiale Zhao, Minghao Li, Daixuan Cheng
🏛️ Renmin University of China; Independent Researcher; AweAI Team
🔗 論文：arxiv.org/abs/2603.03194

這項研究提醒我們：AI coding 工具的發展，還有很長的路要走。你認為 code agent 還需要多久才能真正理解開發者的工作方式？

#AI #Coding #CodeAgent #MachineLearning #軟體工程 #Benchmark #研究
