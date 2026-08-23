---
title: Inherent, founded by DeepMind alumni, says its AI ‘teammate’ just outperformed
  Anthropic and OpenAI at replicating research
source: TechCrunch AI
url: https://techcrunch.com/2026/08/22/inherent-founded-by-deepmind-alumni-says-its-ai-teammate-just-outperformed-anthropic-and-openai-at-replicating-research/
model: claude-code/sonnet
generated_at: '2026-08-23T06:25:21.298242'
score: 49
---

📌 DeepMind 校友新創 Inherent：27B 小模型在論文複現任務上贏過更大的前沿模型

TL;DR：Inherent 的 AI agent Faraday 用強化學習訓練「研究品味」，號稱在論文複現任務上勝過 Claude Opus 4.8 與 GPT-5.5。

當所有人都在比模型參數量的時候，一家倫敦新創卻選擇反其道而行。由 Google DeepMind 校友創立的 Inherent，在剛結束隱身模式、完成 5,000 萬美元種子輪募資沒多久後，宣布旗下 AI agent Faraday 在一項特定任務上，擊敗了規模大得多、名氣也更響亮的模型。

🤔 **任務：不劇透答案，獨立複現論文結果**

根據 TechCrunch 報導，Faraday 的測試任務是獨立重現已發表科學論文的研究結果，且過程中不會被告知正確答案。共同創辦人暨首席科學家 Edward Hughes 表示，論文複現本身就是人類科學家的標準訓練項目，許多博士生也是從這裡起步的。Inherent 更長遠的目標並非只是驗證舊結果，而是打造能發現新科學知識的 AI；擊敗其他前沿 agent 不是重點，「怎麼做到的」才是他們真正在意的部分。

🧩 **用強化學習訓練「研究品味」，而非規則式教學**

Inherent 為 Faraday 設定的成功標準不只是準確度，還要求它展現「研究品味」（research taste）——也就是判斷哪些實驗值得做、如何設計出好實驗的直覺。這種難以言傳的能力,很難靠規則教會,因此 Inherent 選擇仰賴強化學習：獎勵好的結果，而非明確規定該怎麼做。Hughes 表示，相較於主要用「科學研究方法論」去訓練 agent，他們押注這種獎勵導向的方法能更好地泛化到 Inherent 長期目標——打造能貢獻於多個科學領域的 agent。值得注意的是，Faraday 並未使用 Inherent 自建的程式撰寫工具，而是直接採用 OpenAI 的 GPT-5.5 Codex，理由是人類科學家也習慣沿用既有軟體，而非事事自己重造。

📊 **以小博大：Qwen 3.6 27B 對上 Claude Opus 4.8 與 GPT-5.5**

報導指出，Faraday 底層使用的是參數量僅 270 億的 Qwen 3.6，相較之下，被拿來比較的 Anthropic Claude Opus 4.8 與 OpenAI GPT-5.5 都是規模大得多的前沿級系統。文中將「參數量」視為模型規模與訓練成本的粗略代理指標。

⚠️ **自報成績，細節有限**

必須留意的是，這項「勝出」的結果來自 Inherent 自身對外揭露，報導中並未提供具體的評測基準、樣本數或可供第三方覆核的數據，技術細節也僅止於高層次描述，尚無法獨立驗證其嚴謹程度。

💡 **倫敦十二人團隊，與「花園假期」的人才拉鋸**

Inherent 目前僅十餘名員工，全數在倫敦國王十字車站附近的辦公室現場工作，Hughes 認為倫敦仍是 AI 人才密度最高的地點之一。他也提及英國常見的「garden leave」（離職後數月內不得加入或創立競爭對手的限制）曾影響自己，並公開呼籲終結這項美國研究者普遍不需面對的限制。Inherent 計畫在年底前將團隊擴大到約 20 至 25 人。

🎯 **實務啟示**

對工程師而言，Faraday 的案例值得關注的不是「贏了誰」，而是它示範的路徑：用強化學習訓練難以規則化的直覺能力，並刻意選擇沿用既有工具（如 GPT-5.5 Codex）而非重造輪子。在缺乏公開評測細節的情況下，這類宣稱仍應保持一定的觀望態度，靜待更多可驗證的資訊釋出。

🔗 **來源**
- 標題：Inherent, founded by DeepMind alumni, says its AI 'teammate' just outperformed Anthropic and OpenAI at replicating research
- 作者／機構：Anna Heim, TechCrunch AI
- 連結：https://techcrunch.com/2026/08/22/inherent-founded-by-deepmind-alumni-says-its-ai-teammate-just-outperformed-anthropic-and-openai-at-replicating-research/

#AIAgents #ReinforcementLearning #DeepMind #Anthropic #OpenAI #ScientificAI #StartupNews #Qwen #ResearchTaste #London
