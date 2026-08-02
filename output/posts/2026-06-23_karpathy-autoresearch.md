---
title: karpathy/autoresearch
source: GitHub Trending
url: https://github.com/karpathy/autoresearch
score: 88
model: google/gemma-4-31b-it:free
generated_at: '2026-06-23T20:30:32.620778'
---

📌 【Andre Karpathy 新專案】autoresearch：讓 AI Agent 自主迭代 LLM 訓練流程

TL;DR：透過 AI Agent 自主修改程式碼、訓練並驗證，實現「自動化 AI 研究」的實驗性框架。

想像一下，如果你不再需要親自調整超參數或修改訓練邏輯，而是讓 AI 在你睡覺時，自主嘗試數百次實驗，直到找到更好的模型，這會是什麼樣子？

🤔 **從「人類研究」轉向「程式化研究」**

在傳統的 AI 研究中，研究員（Karpathy 幽默地稱之為「肉體電腦」）透過思考、修改程式碼、訓練模型、分析結果，再反覆迴圈。而 `autoresearch` 的核心理念是將這個迴圈完全交給 AI Agent。

🧩 **自動化研究的運作機制**

該專案將一個簡化且可在單張 GPU 執行的 `nanochat` 訓練設定提供給 AI Agent，讓其在以下迴圈中自主運作：

1. **修改程式碼**：AI Agent 根據目標調整訓練程式碼。
2. **快速驗證**：執行訓練約 5 分鐘。
3. **結果評估**：檢查模型效能是否提升。
4. **決策反饋**：若結果改善則保留修改，否則捨棄，隨後進入下一次迭代。

💡 **透過 Markdown 檔案「程式設計」研究組織**

這個專案最獨特之處在於，研究員不再直接修改 Python 檔案。相反地，你是在編寫 `program.md` 檔案。

這些 Markdown 檔案的作用是為 AI Agent 提供上下文（Context），並定義你的「自主研究組織」如何運作。目前的 `program.md` 僅提供最基礎的基準線（baseline），但其設計目標是讓使用者能透過迭代這些指令，找出能達成最快研究進度的「研究組織程式碼」。

🎯 **實務啟示**

雖然這是一個高度實驗性的方向，但它提出了一個重要的思考：AI 的角色正從「輔助寫程式」轉向「自主管理研究流程」。對於工程師而言，未來的開發模式可能會從「撰寫實作程式碼」轉變為「設計引導 AI 的高層級指令（Meta-programming）」，讓 AI 在受控的環境中進行快速的試錯與最佳化。

🔗 **來源**
- 標題：autoresearch
- 作者／機構：karpathy
- 連結：https://github.com/karpathy/autoresearch

#AI #LLM #AutoML #AIAgents #MachineLearning #AutonomousResearch #Karpathy #Nanochat #AIResearch #SelfImprovingAI
