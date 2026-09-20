---
title: 'TypeSafe AI Releases Jev: A System One Model That Returns Typed, Calibrated
  Decisions Instead of Text'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/19/typesafe-ai-releases-jev/
model: claude-code/sonnet
generated_at: '2026-09-20T19:32:12.422738'
score: 92
---

📌 TypeSafe AI 發布Jev：不寫文字，只回傳型別化決策

TL;DR：Jev是Transformer模型但不生成文字，直接回傳附機率的型別化決策，目前為候補制API。

2022年那場 ChatGPT 時刻，教會了 AI 如何跟人對話。這次 TypeSafe AI 押注的方向完全相反：讓 AI 直接跟程式碼對話。

🤔 **RLHF 帶來的對話能力，也帶來了過度自信**

TypeSafe 團隊發布 Jev。這是一個以 Transformer 為基礎的模型，但它不是大型語言模型，也不會生成文字。開發者傳入一個狀態（state）與型別化的問題，模型回傳附帶機率的型別化決策，讓程式碼可以直接依此分支處理。TypeSafe 團隊主張，RLHF 把模型調校成迎合人類偏好，因此產生了「聊天」這種輸出形式，也帶來過度自信與模式丟失（mode dropping）等問題，這些缺陷使得系統仍需要人類留在決策迴圈中把關。

Jev 的名字借用了 Daniel Kahneman 對快速直覺與慢速推理的區分。TypeSafe 表示 Jev 使用一套新的技術堆疊：新架構、平行取樣器（parallel sampler），以及「校準決策強化學習」（Reinforcement Learning for Calibrated Decisions，RLCD）。不過具體架構細節，TypeSafe 目前並未公開。

🧩 **一個端點處理所有型別化問題**

Jev 只用單一端點運作：POST https://api.typesafe.ai/v1/systemone。請求內容帶有 state、model，以及一組問題（questions）的映射。文件定義了3種問題類型，這些問題會針對同一個狀態並行、彼此獨立地執行；TypeSafe 表示，增加問題數量對回應時間幾乎沒有影響。其中 Choice 類型的問題最多可支援255個選項。

開發串接方式包括 pip install typesafe-sdk（需 Python 3.10 以上）、JavaScript SDK @typesafe-ai/sdk，快速入門文件也涵蓋 cURL 呼叫方式，以及供 Claude Code 使用的 Agent Skill。

每一個 Choice 與 Score 類型的答案都會附帶一個介於0到1之間的信心值，這個數值是根據機率分布的形狀推導而來。文件範例中，「billing」選項以0.84的機率勝出，但信心值僅0.596，原因是「technical」選項仍保有0.159的機率。文件建議依此設計3條路徑：高信心值直接執行、中間值交由人工複核、低信心值則轉交人類判斷；判斷門檻應隨錯誤決策的代價高低而調整。

📊 **號稱快193.6倍、便宜444.6倍，但數據來自自家評測**

Jev 的定價為每10億個輸入 token 收費42美元，TypeSafe 則引用現有 LLM 的報價區間為每百萬輸入 token 0.20美元至10美元。在其公開的錄製示範中，Jev 耗時0.114秒、花費0.000081美元完成任務，而 GPT-5.6 Terra 耗時8.566秒、花費0.013880美元；TypeSafe 據此宣稱快193.6倍、便宜444.6倍。這些數字來自 TypeSafe 自家的 workflow 評測，並非第三方獨立驗證的結果。

⚠️ **「零幻覺」指的是格式，不是答案正確性**

文件中所謂的「零幻覺」，指的是結構化輸出的 schema 一定會匹配成功，這個0%的數字並非經驗性的正確率保證——答案本身仍可能是錯的。目前 Jev 僅以早期候補（waitlist）形式提供 API 存取，TypeSafe 尚未公開權重、參數量，也沒有提供自架部署選項。文章也提到，社群專案在發布後幾天內就已經出現。

🎯 **實務啟示**

如果你的 Agent 系統裡有大量「選A還是選B」「這句話是不是詐騙」這類原子化判斷，Jev 展示的型別化決策介面值得關注：把慢思考（規劃、生成）與快判斷（分類、評分）拆開處理，理論上能同時省下延遲與成本。但在架構未公開、僅有候補制 API 存取的情況下，實際效能與穩定性仍需自行驗證，不宜直接沿用官方評測數字做容量規劃。

🔗 **來源**
- 標題：TypeSafe AI Releases Jev: A System One Model That Returns Typed, Calibrated Decisions Instead of Text
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/19/typesafe-ai-releases-jev/

#TypeSafeAI #Jev #AgentArchitecture #SystemOneThinking #CalibratedAI #TypedAPI #RLCD #AIInfrastructure #FastInference #AIDecisionMaking
