---
title: 'Anthropic Releases FlashProve: Cryptographic Proofs That a Reply Came From
  Committed Weights'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/03/anthropic-flashprove-provable-inference-zksnark/
model: claude-code/sonnet
generated_at: '2026-11-04T22:47:12.598702'
score: 103
---

📌 Anthropic 開源 FlashProve:用零知識證明證明「這真的是模型本人回答」

TL;DR：zkSNARK 系統可證明一段回覆來自特定模型權重,卻不會洩漏權重本身,為 API 可驗證性提供新解法。

你呼叫一個標價昂貴的旗艦模型 API,但怎麼知道後端沒有偷偷換成一個便宜模型回答你?目前的答案是:你沒辦法知道。Anthropic 的 Frontier Red Team 想補上這個缺口。

🤔 **你無法驗證,到底是哪個模型回答了你**

素材指出一個在 API 時代被長期忽視的信任問題:使用者查詢模型,卻無法驗證究竟是哪個模型產生了這段回應。路由服務可能悄悄把請求導向一個更便宜的模型;攻擊者可能竄改 token 串流;單純從輸出品質去判斷模型身分並不可靠。FlashProve 正是針對這個「可驗證推理」(provable inference)問題提出的開源研究原型。

🧩 **Prover 與 Verifier,兩階段完成「不洩漏權重的證明」**

FlashProve 的架構分成 prover(模型提供方)與 verifier(使用者)兩端,整個流程跑在兩個階段中。其證明系統把一個互動式 oracle 證明(interactive oracle proof)編譯成基於雜湊函式的密碼學證明,Anthropic 表示這種做法具備後量子安全性(post-quantum security),採用的技術家族與 Starknet 等有效性證明(validity-proof)Layer 2 網路所使用的相同。整個證明過程不會洩漏模型權重的任何資訊,只證明「這段回覆確實來自被承諾(committed)的那個模型」。

三個工程決策是速度的關鍵:第一,prover 的運算量只隨實際啟用的參數量增長,而非整個模型規模,例如在混合專家(MoE)模型中只需對應啟用的那部分參數計算量;第二,請求是事後分批證明(proved in batches after the fact),類似推理中的 prefill 階段;第三,權重可以從主機記憶體串流讀取,因此單張 80GB GPU 就足以運作,不需要多卡集群。

📊 **4000 億參數的 MoE 模型,單張 H100 跑出每秒 110 token 的證明速度**

Anthropic 在 Llama 4 Maverick(一個 4000 億參數的 MoE 模型)上做了實測:使用公開的 4-bit Maverick 權重,在搭配 24 顆 CPU 核心的 1 張 H100 上,FlashProve 可以達到約每秒 110 個 token 的證明速度。根據其 repo 的效能指南,與在 8 張 H100 上以 FP8 跑 Maverick 的 vLLM 相比,證明每個批次所需的 GPU 時間大約是 vLLM 的 72 倍;在 vLLM 最高負載測試下,這個差距擴大到約 94 倍。

考量到密碼學程式碼出錯代價極高,Anthropic 用 Lean 將整套協定形式化,證明了完備性(completeness)、健全性(soundness)與零知識性(zero knowledge)。README 中指出,一個作弊的模型提供方被抓到的機率除了約 q/2^124 + 2^-101 這個極小的例外以外,幾乎必然會被識破。FlashProve 也附上兩套 verifier:一套是日常使用的高速 C++ verifier,但不具備形式化保證;另一套是速度較慢的 Lean verifier,經過證明只會接受符合健全性定理的結果。文中也提到,Anthropic 團隊表示 Claude 協助最佳化了這套系統。

⚠️ **效能代價仍相當可觀**

72 倍到 94 倍的 GPU 時間成本,意味著 FlashProve 目前仍是一套研究原型,距離大規模生產部署還有明顯的效能落差需要跨越。

🎯 **實務啟示**

對建置模型路由或多供應商推理服務的團隊來說,FlashProve 展示了一條用密碼學(而非信任)解決「模型身分驗證」問題的路徑。目前的效能代價決定了它現階段更適合高信任需求、可以忍受延遲與算力成本的場景,而不是通用的線上推理服務,但這套開源原型與形式化驗證的協定規格,值得關注後續的最佳化進展。

🔗 **來源**
- 標題：Anthropic Releases FlashProve: Cryptographic Proofs That a Reply Came From Committed Weights
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/03/anthropic-flashprove-provable-inference-zksnark/

#Anthropic #FlashProve #zkSNARK #ZeroKnowledgeProof #ProvableInference #AISecurity #Cryptography #LLM #MoE #OpenSource
