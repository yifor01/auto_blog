---
title: 'OpenAI Details GPT-Red: An Internal Automated Red-Teaming Model That Beat
  Human Red-Teamers 84% To 13% On Prompt Injection'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/16/openai-details-gpt-red-an-internal-automated-red-teaming-model-that-beat-human-red-teamers-84-to-13-on-prompt-injection/
score: 92
model: tencent/hy3:free
generated_at: '2026-07-17T08:12:28.577305'
---

📌 【OpenAI 內部揭露】GPT-Red 自動紅隊模型在 Prompt Injection 上以 84% 擊敗人類 13%

TL;DR：OpenAI 內部自動紅隊模型 GPT-Red 專找 prompt injection 漏洞，勝率遠超人類。

當人類紅隊演員還在手動構造攻擊樣本時，OpenAI 已經讓一個模型自己對自己的模型發動攻擊——而且打得比人還準。

🤔 **為什麼需要自動化紅隊**

OpenAI 指出，人類 red-teaming 耗時且難以擴展；現有的 robustness 評測已被最新模型刷到飽和。同時攻擊面持續擴大：agent 會透過瀏覽器、連線的 app、本機檔案與工具讀取第三方資料，這些能力是實際工作所需，但也讓攻擊者能有機會在資料中埋入精心設計的指令（prompt injection）。

🧩 **GPT-Red 不是靜態基準，而是一個會迭代的攻擊模型**

GPT-Red 是 OpenAI 內部專用的自動化 red-teaming 模型，行為模式類似人類紅隊：傳送 prompt → 觀察回應 → 朝目標迭代。它是在與部分最大規模 post-training 相同的運算規模下訓練的，且純粹為了安全目的。

兩個部署決策值得注意：
- 與部署中的模型隔離，避免其惡意能力外流給對手。
- 同時做兩件事：部署前找漏洞，以及訓練中生成攻擊樣本（後者依賴下方訓練迴圈）。

🧩 **用 Self-Play RL 讓攻防雙方同步變強**

GPT-Red 使用 self-play reinforcement learning 訓練：attacker 與一組多樣的 defender LLM 在多種 red-teaming 場景中同時訓練。獎勵設計是核心——defender 不能靠全部拒絕來勝出，因為它仍須完成任務。每個環境都有 threat model，定義 GPT-Red 能控制什麼、什麼算成功（例如本機檔案的一部分、網頁 banner、郵件內文或工具輸出）。隨著 defender 變強，GPT-Red 被迫發現更強且更多樣的攻擊。

📊 **訓練結束時幾乎攻破所有對手模型**

OpenAI 表示，訓練末期 GPT-Red 幾乎攻破所有與其對抗的模型，包含內部與正式環境模型，最高到 GPT-5.5。在 prompt injection 任務上，GPT-Red 以 84% 勝過人類紅隊的 13%。訓練過程中也發現了一條新的 chain of thought（摘要在此處截斷，細節未提及）。

🎯 **實務啟示**

對工程師來說，這顯示大規模 self-play RL 可用於持續產出多樣攻擊，緩解人類紅隊無法擴展的瓶頸；在設計 agent 系統時，應預設第三方資料通道（檔案、網頁、工具輸出）都是潛在 injection 來源，並以「必須完成任務且不能被騙」作為防禦評估基準。

🔗 **來源**
- 標題：OpenAI Details GPT-Red: An Internal Automated Red-Teaming Model That Beat Human Red-Teamers 84% To 13% On Prompt Injection
- 作者／機構：Asif Razzaq
- 連結：https://www.marktechpost.com/2026/07/16/openai-details-gpt-red-an-internal-automated-red-teaming-model-that-beat-human-red-teamers-84-to-13-on-prompt-injection/

#OpenAI #GPTRed #RedTeaming #PromptInjection #LLM #SelfPlay #ReinforcementLearning #AIAlignment #AgentSecurity #Safety
