---
title: 'Google Releases Gemini 4 Hydrogen: 2.5x Faster Than Gemini 3.8 Flash'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/13/google-gemini-4-hydrogen/
model: claude-code/sonnet
generated_at: '2026-11-13T22:44:52.288526'
score: 98
---

📌 【Google DeepMind】Gemini 4 Hydrogen 快 2.5 倍，但參數與架構一字不提

TL;DR：Gemini 4 Hydrogen 號稱比 3.8 Flash 快 2.5 倍，定價公開但架構細節完全保密。

Google 把 Gemini 4 Hydrogen 定位成「agentic 工作流的日常座駕」，速度數字很亮眼,但關於它到底是什麼模型,Google 幾乎什麼都沒說。

🤔 **一個「從 Carbon 改造而來」卻不公開身世的模型**

Gemini 4 Hydrogen 是 Google DeepMind 的閉權重（closed-weights）模型,定位在前沿模型 Gemini 4 Carbon 與 Gemini 4 Argon 之下，透過 Gemini API 與 Google 各項產品提供服務。模型卡（model card）寫明它是從 Gemini 4 Carbon 改造而來，但 Google 並未公開參數量、架構或訓練硬體。知識截止日期為 2026 年 3 月。輸入支援文字、圖片、音訊、影片、PDF、表格與圖表，輸出僅為文字；100 萬 token 的視窗由輸入、思考與輸出 token 共用。

開發者可在 generation_config 裡設定 thinking_level，可選值為 low、medium、high 與新增的 xhigh，預設值是 high（3.8 Flash 的預設是 medium）；若設定為過低的等級會直接回傳錯誤，模型卡也提醒思考等級越高會消耗越多 token。

🧩 **核心設計：角色分工而非單一模型包辦**

Hydrogen 的關鍵設計思路是跨模型的角色分工。在 Google Antigravity 中,Orchestrator 選項可以讓同一個任務中途切換模型：Carbon 負責探索、消解模糊與規劃，Hydrogen 負責編輯檔案、更新套件、執行測試，一旦 Hydrogen 卡住就把控制權交還給 Carbon。素材指出，在 Terminal-Bench 4.1 上，這種搭配達到接近 Carbon 單獨執行的任務成功率，同時少用 24% 配額、速度快 19%；Antigravity SDK 也開放同樣的角色分工介面，供開發者打造自訂多 agent 系統。

📊 **速度與安全性數字（以下皆為 Google 自行回報）**

- 在預設 high 等級下，Hydrogen 完成任務速度比 Gemini 3.8 Flash 快 2.5 倍。
- 在合作夥伴測試中，速度快 2 到 2.8 倍，token 用量少 12% 到 23%。
- 比 3.8 Flash 減少 5 倍以上的捏造內容（fabricated claims），在內部 agent 誠實度評測中拿下 96.7%。
- 在 Gray Swan 的基準測試中，對間接提示注入（indirect prompt injection）的抵抗力提升 2.3 倍。

💡 **定價：現在跟 3.8 Flash 一樣貴，但那是因為 3.8 Flash 之後會漲價**

Hydrogen 的 API 定價為每百萬輸入 token 1.50 美元、每百萬輸出 token 7.50 美元，整個上下文視窗統一定價，輸出計價包含思考 token；隱性快取（implicit caching）可將 4,096 token 以上的提示輸入價壓到每百萬 token 0.075 美元,但不支援顯性快取（explicit caching）。

對照之下，Gemini 3.8 Flash 目前（至 2026 年 12 月 31 日前）定價為 0.75 美元／3.75 美元，2027 年 1 月 1 日起才會漲到與 Hydrogen 相同的 1.50 美元／7.50 美元；Argon 現價 2 美元／10 美元，2026 年 11 月 30 日後漲到 4 美元／20 美元。

模型 ID 為 gemini-4-hydrogen，已在 Gemini API、所有層級的 Google AI Studio、Android Studio、Gemini for business、Gemini App、Google Search 與 Sheets 上線；Antigravity 存取需要 Google AI Pro 或 Ultra 訂閱。素材提到的發布文章中並未提及 Vertex AI 的支援狀況。

⚠️ **從 3.8 Flash 遷移要改幾個地方**

Google 的遷移指引指出：temperature、top_p、top_k 參數伺服器端會直接忽略,需要移除；cached_content 欄位需要移除；寫死的 max_output_tokens 上限要調高到 65,536。另外要注意 Terminal-Bench 4.0 與 4.1 是不同版本，跨版本的分數不能直接比較。

🎯 **實務啟示**

如果你的系統現在用 3.8 Flash，遷移前先盤點程式碼裡有沒有寫死的 sampling 參數與 cached_content 呼叫；如果你在評估要不要導入 Orchestrator 式的角色分工，先用 Terminal-Bench 這類你自己的任務場景驗證「配額省了多少、速度快了多少」是否真的對你的 workload 成立，而不是直接套用 Google 公布的整體數字。

🔗 **來源**
- 標題：Google Releases Gemini 4 Hydrogen: 2.5x Faster Than Gemini 3.8 Flash
- 作者／機構：Michal Sutter（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/11/13/google-gemini-4-hydrogen/

#Gemini4Hydrogen #GoogleDeepMind #LLM #AIAgents #APIpricing #PromptInjection #AIsafety #DeveloperTools #Coding #MachineLearning
