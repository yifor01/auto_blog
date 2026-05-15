---
title: "OpenDeepThink: Parallel Reasoning via Bradley--Terry Aggregation"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.15177
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-05-15T20:41:16.565671
---

📌 **OpenDeepThink：Bradley‑Terry 並行推理提升 Elo**

你以為讓 LLM 多跑幾次就能變聰明？事實上，單純增加樣本反而讓選擇變成瓶頸。OpenDeepThink 用配對投票讓模型自己決出最佳答案，八輪呼叫就讓 Gemini 3.1 Pro 的 Codeforces Elo 飆升 405 分。

🤔 **當樣本變多，選擇卻變難**

現有的 test‑time compute 方法多半透過延伸單一推理鏈來增加深度。雖然直接在平行取樣多個候選答案很直覺，但缺少真實標籤時，點wise LLM 評判會噪音且有偏見，導致選出「最佳」答案成為難題。

🧪 **每代隨機配對投票，保留優秀個體並變異**

OpenDeepThink 把這個問題轉換為配對比較：每一代讓 LLM 隨機抽取候選答案兩兩組成配對，進行 Bradley‑Terry 投票，彙總所有配對結果得到全域排名。排名靠前的候選被保留，前三分之二根據比較過程中產出的自然語言批判進行變異；最底下的四分之一則被淘汰。這樣的種群式演變過程在不需要外部驗證器的情況下，逐步聚焦於高品質答案。

💡 **八輪呼叫讓 Gemini 3.1 Pro Elo +405**

在實驗中，僅用八次連續的 LLM 呼叫（約 27 分鐘牆鐘時間），OpenDeepThink 讓 Gemini 3.1 Pro 在 Codeforces 上的有效 Elo 提升 405 分。同一套流程無需重新調參即可在較弱或較強的模型間遷移。在多領域 HLE 基準測驗中，效益主要出現在可以客觀驗證的題目上；而在主觀性較高的題目上，則出現反向的表現。

⚠️ **依賴大量 LLM 呼叫，尚未開放程式碼**

該方法的效果取決於大量的配對判斷，因此在資源受限環境下可能不易直接部署。此外，論文目前未公開實作程式碼，這限制了立即複製與進一步實驗的可能。

🎯 **適合需要可驗證推理的任務，可跨模型遷移**

對於那些答案可以透過程式或規則客觀驗證的場景（如競賽編程、數學證明），OpenDeepThink 提供了一種不依賴外部判斷器的 test‑time 擴展策略。它表明，透過結構化的配對投票與基於批判的變異，即使在沒有標準答案的情況下，也能有效地引導模型朝向更正確的解答。未來若能優化呼叫效率或開放程式碼，將有助於在更廣泛的推理任務中落地。

🔗 **論文連結**  
📝 OpenDeepThink: Parallel Reasoning via Bradley--Terry Aggregation  
👤 Shang Zhou, Wenhao Chai, Kaiyuan Liu, Huanzhi Mao, Qiuyang Mang (UC San Diego; Princeton University; University of Washington; UC Berkeley)  
🔗 https://arxiv.org/abs/2605.15177  

你認為這種配對投票式的 test‑time 擴展在你的工作中有什麼潛在用途？歡迎在留言區分享看法 👇

#AI #LLM #Reasoning #TestTimeScaling #BradleyTerry #OpenDeepThink #Gemini #Codeforces #機器學習 #深度學習
