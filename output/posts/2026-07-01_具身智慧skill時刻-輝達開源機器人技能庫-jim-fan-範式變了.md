---
title: 具身智慧Skill時刻！輝達開源機器人技能庫，Jim Fan：範式變了
source: 量子位
url: https://www.qbitai.com/2026/07/441396.html
score: 93
model: google/gemma-4-31b-it:free
generated_at: '2026-07-01T20:35:55.876781'
---

📌 【NVIDIA 最新研究】不再依賴梯度下降？ASPIRE 讓機器人透過「技能庫」持續進化

TL;DR：NVIDIA 推出 ASPIRE，將機器人學習從權重更新轉向「程式碼經驗沉澱」，實現可複用的技能持續學習。

當我們談論機器人訓練時，直覺反應通常是採集海量資料、進行梯度下降、調整模型權重。但 NVIDIA 提出的 ASPIRE 則採取了一種完全不同的路徑：如果機器人能像工程師一樣，在失敗後分析原因、修改程式碼並記錄經驗，它是否能越做越聰明？

🤔 **Code as Policy 的困境：會執行但「不長記性」**

在 ASPIRE 出現前，Code as Policy 範式已讓大模型不再直接輸出動作，而是撰寫可執行的控制程式碼（呼叫感知模組、規劃 API 與控制原語）。但這種方式面臨兩個核心痛點：
1. **失敗原因不明**：系統僅知道「任務失敗」，無法分辨是感知錯誤、抓取不穩還是路徑碰撞。
2. **經驗無法沉澱**：除錯過程中的修復方案與 Prompt 寫法在任務結束後即被丟棄，下次遇到類似問題仍需重新試錯。

🧩 **ASPIRE 的運作邏輯：將失敗轉化為可複用的 Skill**

ASPIRE（Agentic Skill Programming through Iterative Robot Exploration）將機器人的學習過程轉化為一個「分析 $\rightarrow$ 修復 $\rightarrow$ 沉澱」的迴圈。其核心流程如下：

1. **記錄過程**：機器人執行任務時，將感知、導航、抓取、碰撞與運動規劃的過程完整記錄。
2. **Agent 診斷**：呼叫 GPT 或 Claude 等大模型扮演研究員，回放執行軌跡並分析失敗原因（例如：判斷目標點落在碰撞緩衝區內）。
3. **迭代修復**：Agent 修改控制程式碼以解決問題。
4. **沉澱技能**：將驗證成功的修復經驗（Code Repair Pattern）寫入技能庫（Skills Library）。

例如，若機器人因障礙物無法靠近目標，ASPIRE 會總結出一條新技能：「若規劃失敗，嘗試從 45°、90°、180° 等不同角度重新接近」。未來無論目標物是收音機或微波爐，只要場景類似，即可直接複用此經驗。

💡 **Jim Fan 指出的範式轉移：從權重到技能庫**

NVIDIA 機器人主管 Jim Fan 表示，ASPIRE 代表了一種全新的持續學習範式，將傳統訓練邏輯徹底翻轉：

- **訓練目標**：從「梯度下降」 $\rightarrow$ 「不斷打磨技能 (Skill Refinement)」。
- **模型產出**：從「浮點權重」 $\rightarrow$ 「持續擴充的感測運動技能庫 (Sensorimotor Skills)」。
- **訓練方式**：從「集中訓練」 $\rightarrow$ 「一群 Agent 各自練習不同技能，再將經驗彙總至同一個技能庫」。

🎯 **實務啟示：從端到端模型轉向「可解釋」的經驗積累**

對於 AI 工程師而言，ASPIRE 的啟示在於將 LLM 的推理能力應用於「閉環除錯」。與其追求一個巨大的端到端 VLA 模型，建立一套能讓 Agent 自行分析軌跡並將修復經驗程式化（Code-based）的機制，能讓機器人的能力成長變得可追溯且易於複用，大幅降低重複試錯的成本。

🔗 **來源**
- 標題：具身智慧Skill時刻！輝達開源機器人技能庫，Jim Fan：範式變了
- 作者／機構：henry / 量子位
- 連結：https://www.qbitai.com/2026/07/441396.html

#NVIDIA #EmbodiedAI #ASPIRE #CodeAsPolicy #Robotics #ContinualLearning #LLM #JimFan #AgenticAI #SensorimotorSkills
