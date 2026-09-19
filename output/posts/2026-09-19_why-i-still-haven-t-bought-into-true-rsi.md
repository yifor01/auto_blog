---
title: Why I still haven’t bought into true RSI
source: Interconnects
url: https://www.interconnects.ai/p/where-i-stand-on-rsi
model: claude-code/sonnet
generated_at: '2026-09-19T19:30:04.899278'
score: 73
---

📌 千個 Agent 同時運轉，算不算 AI 在自我改進？

TL;DR：Interconnects 作者 Nathan Lambert 認為，OpenAI 與 Anthropic 內部堆疊的大量 agent 只是「有損自我改進」，還稱不上真正的遞迴自我改進（RSI）。

當一間公司內部同時有數千個 agent 在跑，員工每天親眼看著這種規模的自動化運作，對 AI 進步速度與風險的預期自然會被迅速拉高。但這種「規模上的震撼」，真的等於超級智能近在眼前嗎？Nathan Lambert 在 Interconnects 的最新文章給出了保留意見。

🤔 **舊金山的焦慮文化，會放大任何 AI 風險訊號**

Lambert 觀察到，前沿實驗室加上舊金山 AI 圈那種競爭激烈的文化，容易把任何 AI 風險放大解讀。他回顧 2023、2024 年那波 AI 安全辯論，當時預測的多數風險並未如期出現；如今兩大實驗室員工對 AI 風險與進步速度的焦慮，在 2026 年初 agent 產品找到市場定位後只會更加強化。他引用 Richard Ngo 的說法：AI 安全社群目前普遍默認「幾年內會出現智能爆炸」，而 Lambert 預期最終結果會是「方向大致正確、但具體判斷是錯的」——不會在 8 年內出現超級智能，但進展速度仍快到讓當年主張短時間線的人看起來像是說對了。

🧩 **「有損自我改進」：Lambert 的替代論述**

相對於「真·RSI」，Lambert 提出他稱為 lossy self-improvement（有損自我改進）的替代情境，核心是三點：
- 可自動化的研究範圍太窄，面對 scaling laws 的指數級成本，不足以帶來大規模的淨加速
- 平行堆疊更多 AI agent 的邊際報酬遞減是真實存在的現象
- 資源瓶頸與政治因素，才是打造強大 LLM 的主要限制，AI 在這方面能幫上的忙有限

💡 **三位研究者的能力門檻時間線**

Lambert 整理了 Dwarkesh 訪談中 Charlie O'Neill、Beren Millidge、John Schulman 三人對三個問題的時間線預測（自訪談當日起算）：

| 問題 | Charlie O'Neill | Beren Millidge | John Schulman |
|---|---|---|---|
| 連續一個月頂替白領遠端工作者 | 程式化工具存取約 1 年；僅靠瀏覽器約 2 年 | 完全通用約 3 年；80-90% 涵蓋率更快 | 約 1 年出現「堪用」版本，能力不均但持續改善 |
| AI 研究者生產力提升 10 倍 | 5-10 年，瓶頸在吸收資訊、決定下一步實驗 | 認為 John 的約 2 年估計合理，未給獨立時間線 | （未提供獨立答案） |
| 超越頂尖人類專家的全電腦端工作（ASI） | 5-10 年，受限於記憶與 context 長度 | 實驗室聚焦領域約 5 年，通用版本無明確時間線 | 3-4 年，空間／物理領域可能更久，需解決長視野學習 |

Lambert 特別點出一個反覆出現的問題：智慧本身缺乏明確規格。LLM 的智慧型態與人類差異很大，我們卻用人類形狀的職業門檻去預測它，AI 不會離散式地跨過「遠端工作者」或「AI 研究員」這種門檻，而是一種緩慢擴散、長尾永遠存在的過程。

💡 **科學進步的瓶頸不是實驗速度，是理解本身**

他認同實驗設計與測試的循環未來可能加快 10 倍，但假設生成與直覺建立不會同步加快。很多人低估了科學有多依賴溝通與同儕間的標準建立；AI 工具再怎麼進步，人類在這方面的能力提升仍然有限，真正的收穫會是讓人類把更多時間投入到這一塊，而不是讓人類自己變得指數級聰明。回到推理容量的討論，Lambert 認為 agent swarm 在近期最擅長解決有明確、可驗證答案的清晰問題；RSI 對改善 AI 模型本身的幫助，更多體現在效率而非拓展智慧上限，因為 LLM serving 有清楚可衡量、可調整的指標，這會讓 inference-time scaling 與多 agent 系統的效率持續提升。

⚠️ **他自己也不確定**

Lambert 坦言，他無法排除實驗室內部已經看到某些尚未公開、真正驚人的突破，只是傾向認為目前的 AI 安全焦慮多半來自「規模化的 agent 確實在運作」這個事實本身，而非未公開的根本性突破，但他對此仍抱持高度不確定性。

🎯 **實務啟示**

與其押注「奇點將至」，不如把注意力放在 RSI 目前真正能兌現的地方：有明確驗證指標的任務，例如 inference-time scaling 與多 agent 系統效率優化。至於研究直覺、假設生成這類需要長期理解累積的工作，短期內仍難以被自動化取代。

🔗 **來源**
- 標題：Why I still haven't bought into true RSI
- 作者／機構：Nathan Lambert，Interconnects
- 連結：https://www.interconnects.ai/p/where-i-stand-on-rsi

#RSI #AIsafety #AGI #Interconnects #OpenAI #Anthropic #AIagents #FutureOfAI #MachineLearning #AIAlignment
