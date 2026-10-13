---
title: 'Import AI 476: Creativity and RSI; worse-than-China open weight models; AI
  goes to space'
source: Import AI
url: https://jack-clark.net/2026/10/12/import-ai-476-creativity-and-rsi-worse-than-china-open-weight-models-ai-goes-to-space/
model: claude-code/sonnet
generated_at: '2026-10-12T23:59:43.451245'
score: 73
---

📌 AI 週報：模型看不懂暗示、研究品味正起飛、太空競賽將開打

TL;DR：Import AI 476 期彙整三則訊號：視覺常識新基準揭露 AI 弱點、AI「研究品味」基準逼近甚至超越人類、以及 AI 與太空競賽的思考。

人類看一眼書架，立刻知道還能不能再塞幾本書；但目前最強的 AI 系統面對這類「畫面沒說但其實暗示了」的題目，分數只拿到人類的一半出頭。

🤔 **新基準 HSS：AI 缺乏「看懂暗示」的直覺**

AI 新創 Elorian 與 Scale AI 合作推出 Humanity's Sixth Sense（HSS），測量模型能否推理一個視覺場景「暗示但未明示」的資訊——例如一張書架照片，問還能不能塞更多書；或馬匹拉犁的照片，問鎖鏈是否撐得住犁的拖拉重量。HSS 共 522 題，涵蓋 288 張圖片與 234 段影片（總長 17.6 小時），分為四類：時間與因果動態、物理與空間邏輯、社會理解（意圖、注意力、歸屬感），以及抽象與情境推論。

📊 **人類打 93 分，最強 AI 只拿一半**

人類基準的整體 pass@1 平均為 93.1（圖片 94.1、影片 91.9、時間 97、空間 94.9）。相較之下，表現最好的 AI 系統 GPT 6 Astra 只拿到 53.6（圖片 55.6、影片 51.1、時間 58.2、空間 53.6）。值得注意的是，中國開源模型在這裡表現明顯更差：GLM-5.3-flash 得分 26.8，Kimi K3 得分 25.5。最常見的兩種錯誤分別是遺漏決定答案的關鍵細節（佔失敗案例 21%）與誤判物件、人物或角色（佔 20%）。

💡 **這說明了什麼：世界模型可能是「湧現」出來的**

Import AI 作者 Jack Clark 認為，這個結果更有趣的解讀不是「AI 做得不好」，而是像 GPT、Claude 這類語言模型，在沒有專門的空間感知 2D／3D 世界模型的情況下，已經能在這類任務上做到這個程度——某種程度上反駁了「真正的視覺推理必須依賴專屬世界模型」這個長期被廣泛假設的論點。

🧩 **第二則：TasteVal 測的是 AI 的「研究品味」**

AI 新創 P-Zero Research 推出 TasteVal，測試 AI 系統是否具備人類研究者所說的「良好科學品味」。基準涵蓋 8 項代表前沿 AI 開發的任務，橫跨預訓練資料策劃、預訓練與微調、偏好建模，以及對抗性提示的穩健性。測試方式是給模型一個固定的研究問題，觀察它如何迭代設計實驗、並從結果中得出結論；對照基準則來自 24 位曾在 OpenAI、Google DeepMind、NVIDIA、Microsoft Research 工作過的專家（每項任務至少兩位）。

📊 **Opus 5.5 已經超越人類專家基線**

結果顯示，前沿模型在實驗性研究品味上的能力，自 2025 年 12 月以來每 3.0 個月翻倍一次（95% 信賴區間 1.7 至 5.0 個月）。表現最好的模型 Opus 5.5 顯著超越人類基線，算力倍增係數達 2.30 倍（95% 信賴區間 1.15 至 4.37 倍），而每次嘗試的成本僅約人類專家基線平均成本的 1/30。

💡 **為何重要：這是遞迴自我改進（RSI）的風向球**

Jack Clark 在先前的分析（Import AI 455）中就指出，創造力是 AI 系統能否發展出自我改進能力的關鍵變數；他當時認為 AI 系統還沒有在創造力上展現出重大突破。如今他表示，近期在數學研究突破與這類研究品味基準上看到的進展，讓他把「完全 RSI 可能發生」的預期時間點，從原本的 2028 年提前到 2027 年——但這仍是他個人的判斷，並非確定的結論。

🤔 **第三則：AI 競賽正在走向太空**

AI Frontiers 一篇文章討論，隨著 Starship 等平臺提升軌道運載能力，2030 年代太空經濟（太空發電、運算、製造）可能大規模興起。文章指出，太空飛行器可以圍繞「主要服務 AI 而非人類」重新設計——例如不需要加壓與載人安全冗餘的無人飛行器，即使遭遇太空垃圾撞擊，也能維持大部分功能運作。文章也提出一個令人警覺的可能性：率先在太空建立據點的一方，可能透過「基礎設施帶來更多能源與製造產能、進而帶來更多基礎設施」的工業飛輪、太空領域的感知優勢，以及自我複製探測器，形成經濟與戰略上難以追趕的複合優勢。

🎯 **實務啟示**

這三則消息對工程師的共同提示是：模型「通用推理」能力的邊界，正在被一個又一個新基準持續刻劃，不論是視覺常識還是科研判斷力。如果你的工作涉及 agentic 研究輔助或自動化實驗設計，TasteVal 這類基準值得持續追蹤後續模型的分數變化，把它當作觀察 RSI 進展速度的一個領先指標；同時 HSS 的結果也提醒我們，純文字／多模態 LLM 在缺乏專屬世界模型的情況下，視覺常識推理的能力邊界究竟在哪裡，仍是值得關注的開放問題。

⚠️ **限制**

HSS（522 題）與 TasteVal（8 項任務）都是剛推出的新基準，樣本規模與任務設計可能帶有特定視角的局限；Jack Clark 對 RSI 時程的推估，也是作者本人的主觀判斷，而非已驗證的事實。

🔗 **來源**
- 標題：Import AI 476: Creativity and RSI; worse-than-China open weight models; AI goes to space
- 作者／機構：Jack Clark
- 連結：https://jack-clark.net/2026/10/12/import-ai-476-creativity-and-rsi-worse-than-china-open-weight-models-ai-goes-to-space/

#ImportAI #AIResearch #BenchmarkEvaluation #VisualReasoning #RecursiveSelfImprovement #AIAlignment #MultimodalAI #AIAndSpace #OpenWeightModels #FrontierModels
