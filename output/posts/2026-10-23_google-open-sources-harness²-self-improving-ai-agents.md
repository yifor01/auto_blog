---
title: 'Google Open-Sources Harness²: Self-Improving AI Agents Without Retraining'
source: KDnuggets
url: https://www.kdnuggets.com/google-open-sources-harness-self-improving-ai-agents-without-retraining
model: claude-code/sonnet
generated_at: '2026-10-23T20:39:10.721454'
score: 108
---

📌 【Google Research】免訓練也能自我進化的 Agent 框架 Harness²

TL;DR：Harness² 不動模型權重，靠兩層遞迴改寫 prompt、工具與記憶，讓 agent 自我進化。

手動調校 agent 大概是這樣的循環：工程師盯著 agent 失敗、改一下 prompt、加一個工具、再跑一次。這套做法在你事先想得到的任務上還算管用，但一旦碰上論文所稱的「open world」——agent 遇到沒人預料過的任務——就立刻破功。Google Research 這次開源的 Harness²，就是想把這個手動迴圈自動化，而且完全不碰模型權重。

🤔 harness 不是模型，是模型的全部周邊

論文對 harness 的定義很直白：讓模型能以 agent 身分行動的一切周邊，包括 prompt、工具、記憶、技能與編排邏輯；「harnessing」則是優化這套周邊的工作。Harness² 的核心主張是，與其重新訓練模型，不如把力氣花在打磨這層周邊——它在 README 中強調「保持模型權重不變」，沒有 fine-tuning，也不需要新的訓練資料，改變的只有模型的「外部環境」。

🧩 八個可編輯元件，兩層遞迴

Harness² 可以編輯八種元件：

| 元件 | 在 agent 中的作用 |
|---|---|
| 系統提示（System prompt） | 模型最先讀取的標準指令 |
| 護欄（Guardrails） | 規範 agent 該做與不該做的事 |
| 記憶（Memory） | 跨步驟保留的長期筆記 |
| 技能（Skills） | 特定任務的可重複使用指引 |
| 工具指引（Tool guidance） | 何時、如何使用各項工具 |
| 腳本（Scripts） | agent 可執行的輔助程式碼 |
| 子代理（Subagents） | 負責局部任務的委派助手 |
| 外掛（Plugins） | 在工具迴圈中塑造行為的中介層 |

名稱裡的平方「²」指的是兩層遞迴。第一層（Loop 1）是任務層級的「Propose—Probe—Compose」：harness 編輯器先提出通用與領域專屬的修改建議（Propose），agent 用每一版修改過的 harness 重跑同一任務（Probe），最後由 composer 比較各次執行結果、合併有效的修改（Compose）。關鍵在於這個過程「從執行之間的行為對比中學習，不需要正確答案」——它比較的是兩次執行的差異，而不是對照標準答案，這正好契合 open world 裡沒有人能給出答案的現實。

第二層（Loop 2）則是跨任務的「harnessing 層級遞迴」：每個任務結束後，experience reflector 會把被採用的 harness 與「有證據支持的經驗」寫進一個持久化的 improvement harness，用來指導下一個任務的修改方向。簡單說，第一層讓 agent 在這個任務上變強，第二層讓整套框架在未來任務上變得更會改進 agent。

此外還可以用 budget 參數 k 搭配 parallel 或 sequential 模式調整投入的算力：parallel 模式一次提出 k 個通用與 k 個領域候選，再對整個候選池做 k 次獨立合成，偏向廣度探索；sequential 模式則是連續跑 k 輪 Propose—Probe—Compose，把精煉過的 harness 一路往下帶，偏向深度打磨。

📊 三個 benchmark 上的提升幅度

Google 用 GLM-5 和 Gemini 3.5 Flash 在三個 benchmark 上測試，單步（k=1）就能讓兩個模型都優於各自的基礎 harness：

| Benchmark | 測試內容 | 最佳提升幅度 |
|---|---|---|
| WorkBuddy-Bench | 辦公、網頁與程式碼任務 | 最高 +11.5 分 |
| LAB | 法律工作任務（源自 Harvey 的 harvey-labs） | 最高 +11.8 個百分點（Partial pass rate） |
| JobBench | 專業工作任務 | 最高 +4.5 分 |

需要留意的是，這些是「up to」的最佳表現數字，不是平均值，而 LAB 的數字特別是在 Partial 分數（通過的評分標準比例）上取得。README 也提到更大的 k 會帶來進一步提升，詳細的逐配置數字則在論文裡。

💡 為什麼值得關注

讓模型變強通常要靠繼續訓練，但這需要訓練資料、GPU 與模型權重的存取權——大多數透過 API 使用模型的團隊三者皆無。Harness² 把每一次改進都留在純文字檔案裡：改寫過的 prompt、修好的腳本、新增的護欄。這帶來三個實務上的好處：改動可以被讀懂、可以被 diff；它能用在你無法訓練的模型上（executor 和 improver 在設定檔裡只是模型 ID，這次釋出就是用 GLM-5、Gemini 3.5 Flash 當 agent，搭配 Vertex Gemini 或 Claude 當 improver）；它不需要標準答案，靠的是同一任務不同執行之間的行為對比。

🎯 實務啟示：自己動手跑跑看

Google 提供的免費 demo 用「確定性編輯器與真實 Python 執行」運作，不需要模型金鑰。流程大致是：安裝 Astral 的 Python 套件管理工具 uv；`git clone` google-research/harness2 專案並進入資料夾；用 `uv venv --python 3.12 .venv` 建立並啟用虛擬環境；最後執行 `uv pip install -e '.[render]'` 以可編輯模式安裝，順便裝進輸出試算表與投影片用的 `openpyxl`、`python-pptx`。安裝完成後會註冊 `harness2`、`harness2-demo`、`harness2-setup` 等指令，可以直接在本機體驗兩層遞迴的運作。要留意的是，benchmark 結果目前都是 Google 自家測出來的，獨立重現的結果會更有參考價值。

🔗 來源
- 標題：Google Open-Sources Harness²: Self-Improving AI Agents Without Retraining
- 作者／機構：Shittu Olumide, KDnuggets（研究出處：Google Research）
- 連結：https://www.kdnuggets.com/google-open-sources-harness-self-improving-ai-agents-without-retraining

#GoogleResearch #AIAgent #Harness2 #OpenSource #PromptEngineering #AgentFramework #RecursiveLearning #LLMAgents #AIAutomation #MachineLearning
