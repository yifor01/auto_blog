---
title: 'Meet Grok Voice 3.0: SpaceXAI Voice Agent Model Ranks #1 on Artificial Analysis'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/14/meet-grok-voice-3-0-spacexai-voice-agent-model-ranks-1-on-artificial-analysis/
model: claude-code/sonnet
generated_at: '2026-10-15T20:47:25.103929'
score: 85
---

📌 Grok Voice 3.0 奪語音測試冠軍，延遲卻不如前代

TL;DR：Grok Voice 3.0 登上 Artificial Analysis 語音榜首，但首音延遲比 2.0 版還慢。

🎣 一款新模型拿下榜首聽起來是全面勝利，但把四個子項分數拆開來看，故事沒那麼單純，SpaceXAI 自己引用的數據裡，就藏著一個退步的指標。

🤔 Speech-to-Speech 榜單登頂

SpaceXAI 發布 Grok Voice 3.0，一款能聽、能推理、能呼叫工具、也能說話的 speech-to-speech 模型，目前在 Artificial Analysis 的 Speech-to-Speech Index 排名第一，得分 86.9。對開發者而言，呼叫端點、事件格式與每分鐘 $0.08 的價格都與 Grok Voice 2.0 相同。模型以 grok-voice-3.0 的名稱掛在 /v1/realtime WebSocket 端點上，而 grok-voice-latest 這個別名已經指向新版，等於既有的 agent 會自動切換到 3.0。SpaceXAI 並未公開參數量或架構細節。預設會開啟 reasoning（reasoning.effort 設為 "high"），也可以設為 "none" 來換取更快的回應速度；barge-in（使用者插話）由伺服器端的語音活動偵測處理；工具呼叫（collections 搜尋、網路搜尋、X 搜尋、遠端 MCP 伺服器、自訂函式）都在對話 session 內執行。

📊 四項子指標與對手的比較

Artificial Analysis 的 Speech-to-Speech Index 是四個子項的等權重平均：Big Bench Audio 推理能力、τ-Voice agentic 表現、Speech Agent Arena 偏好度，以及任務成功率。

| 模型 | AA 綜合分數 |
|---|---|
| Grok Voice 3.0 | 86.9 |
| GPT-Live-1（Astra, medium） | 83.2 |
| Gemini 3.8 Live Extended Thinking | 82.6 |
| Grok Voice 2.0 | 81.3 |

不過子項表現並非全面領先：在 ServiceNow 用來評估企業語音 agent 準確度與體驗的 EVA-Bench 上，SpaceXAI 自己公布的最高準確度分數是 74%。

💡 延遲聲稱「降低 40%」，但其實比前代慢

Artificial Analysis 測得 Grok Voice 3.0 的首音延遲（time to first audio）為 0.81 秒，GPT-Live-1（Astra, medium）為 1.34 秒，SpaceXAI 宣稱「延遲降低 40%」確實成立，但對照自家前代 Grok Voice 2.0 的 0.70 秒，3.0 版反而變慢了。

| 模型 | 首音延遲 |
|---|---|
| Grok Voice 2.0 | 0.70 秒 |
| Grok Voice 3.0 | 0.81 秒 |
| GPT-Live-1（Astra, medium） | 1.34 秒 |

在成本方面，SpaceXAI 引用 Artificial Analysis 的「每個 Big Bench Audio 任務成本」數據：

| 模型 | 每任務成本 |
|---|---|
| Grok Voice 3.0 | $0.025 |
| GPT-Live-1（Astra, medium） | $0.030 |
| GPT-Realtime-2.1（High） | $0.055 |

但若換算成「每小時輸入語音的成本」，Gemini 3.8 Live Extended Thinking 反而更便宜：$3.50，Grok Voice 3.0 則是 $4.80。文中也提醒，各家牌價其實不能直接比較：GPT-Live-1 每分鐘 $0.05，但後端模型與工具使用是另外計費；Gemini 則是語音按分鐘計費外加文字 token 費用。以上 benchmark 數據皆來自 Artificial Analysis，截至 2026 年 10 月 14 日。SpaceXAI 的部落格文章也列出了凝固時間點的 Arena Elo 值：GPT-Live-1 為 1048，Gemini 為 990。

⚠️ 架構黑盒，且榜首地位靠的是綜合分數

SpaceXAI 沒有公開 Grok Voice 3.0 的參數量或架構設計，外界無法得知效能提升的技術來源；而「榜首」頭銜是四項子指標等權重平均後的結果，單看延遲或 EVA-Bench 準確度，Grok Voice 3.0 並非每一項都領先對手。

🎯 實務啟示

API 與 Grok Voice 2.0 相容，且與 OpenAI Realtime API 相容，遷移主要只需換端點網址與金鑰；但正式環境建議直接指定 grok-voice-3.0，而不要依賴會自動變動的 grok-voice-latest 別名，避免模型升級帶來非預期的延遲或行為變化（本次 3.0 版的首音延遲其實比 2.0 版慢就是一例）。Grok Voice 2.0 目前已標示為棄用（deprecated）。

🔗 來源
- 標題：Meet Grok Voice 3.0: SpaceXAI Voice Agent Model Ranks #1 on Artificial Analysis
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/14/meet-grok-voice-3-0-spacexai-voice-agent-model-ranks-1-on-artificial-analysis/

#GrokVoice #SpaceXAI #SpeechToSpeech #VoiceAI #RealtimeAPI #ArtificialAnalysis #AIBenchmark #ConversationalAI #MCP #AIAgent
