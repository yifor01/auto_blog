---
title: Progress on provable inference for large language models
source: Anthropic Research
url: https://www.anthropic.com/research/provable-inference
model: claude-code/sonnet
generated_at: '2026-11-03T22:31:22.597953'
score: 106
---

📌 Claude 打造可驗證推理的零知識證明系統

TL;DR：Anthropic 用 Claude 打造 FlashProve，以零知識證明驗證推理身分。

跟朋友講話，你能看到、聽到、握手確認對方身分；跟 AI 模型對話時，幾乎沒有任何方法確認背後真的是你選的那個模型，而不是路由服務偷偷換成別的模型，甚至是被攻擊者竄改過的 token 串流。光看輸出品質並不可靠，即使回答看起來很好。

🤔 你怎麼知道回答真的來自那個模型？

這個問題的解法方向被稱為 provable inference（PI，可證明推理）：讓用戶在不知道模型權重、運算資源有限的情況下，也能驗證一段回應真的來自指定的模型。獨立評測者需要確認測試對象沒被偷換、使用第三方路由服務的客戶想確認付費用的真的是宣稱的模型，這些場景都需要這樣的保證。

🧩 用 zkSNARK 讓證明和驗證都很「便宜」

Anthropic 選擇的技術路線是 zkSNARK（zero-knowledge succinct argument of knowledge，零知識簡潔知識論證）。簡單說，prover（模型提供者）可以附上一段簡短的「證書」，讓 verifier（用戶）快速確認某個計算確實被正確執行過，而且這份證書不會洩漏計算本身以外的任何資訊（也就是不會洩漏權重），同時驗證速度比重新執行整個計算快上指數級。Anthropic 用 Claude 針對這個問題做了一系列最佳化，打造出名為 FlashProve 的原型系統。這套系統對模型「承諾」（commit），之後每次推理都能提出證明，承諾與證明都刻意隱藏模型權重，但不隱藏模型架構。由於 Claude 做最佳化時常做出難以逐步評估的決策，Anthropic 另外提供了用 Lean（一套形式驗證語言）寫成的頂層安全性聲明，方便外部稽核。

📊 一張 H100，每秒 110 個 token 的證明速度

在 400B 參數的 mixture-of-experts 模型 Llama 4 Maverick 上（4-bit 量化、prefill 階段用整數運算），單張 H100 GPU 可以用約 110 tokens/秒的速度產生證明，每個 1,024-token 請求的證明大小約 19 MB。對照常見的開源推理函式庫 vLLM 直接跑完同樣長度 prompt 所需的 GPU 時間，這套證明系統大約要多花 70 到 95 倍的運算時間。文中指出，相較於先前的開源系統，這個速度已經快了幾個數量級。

⚠️ 仍是中途進度，不是完整方案

Anthropic 在文中明確表示，這篇研究分享的是「中途進度」，而不是一份完整的研究成果，目的是希望其他人接手並持續改進。系統隱藏了模型權重，但不隱藏模型架構，架構資訊仍會暴露；70 到 95 倍的運算開銷，也意味著大規模商用部署前還有相當落差要補。

🎯 實務啟示

Anthropic 把 prover、兩種 verifier（C++ 版與 Lean 版）以及 Lean 證明都以 Apache 2.0 授權開源，加上技術報告與協定規格文件。對想研究模型身分驗證、或是評估未來合規稽核工具的工程師，現在就有完整的程式碼與形式化證明可以直接檢視，不必從零開始。

🔗 來源
- 標題：Progress on provable inference for large language models
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/research/provable-inference

#Anthropic #Claude #zkSNARK #ProvableInference #Cryptography #LLM #ZeroKnowledgeProof #AIRegulation #FormalVerification #OpenSource
