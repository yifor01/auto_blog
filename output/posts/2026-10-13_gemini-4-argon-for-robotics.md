---
title: Gemini 4 Argon for Robotics
source: Google DeepMind
url: https://deepmind.google/blog/gemini-4-argon-for-robotics/
model: claude-code/sonnet
generated_at: '2026-10-13T21:58:59.579618'
pinned: true
---

📌 【Google DeepMind】Gemini 4 Argon 讓機器人學會「自己練習再上場」

TL;DR：Argon 在空間推理基準 ERQA 拿下 87%，並被用來串起從技能學習到模擬資料生成的整個機器人工作流程。

一個語言模型要操控機械手臂、理解接觸力學、還要在模擬環境裡自我排練，這聽起來像是分屬不同領域的三件事。但 Google DeepMind 展示的案例顯示，Gemini 4 Argon 正把這些環節串成同一條工作流。

🤔 **從「看得懂」到「做得到」**

DeepMind 表示 Argon 在物理理解、程式碼生成與視覺語意推理上出現明顯躍進，朝「physical AGI」邁進一步。在測試模型理解 3D 環境中物理與空間問題能力的 Embodied Reasoning（ERQA）基準上，Argon 純推理拿下 87%，優於其他前沿模型。

🧩 **四大應用場景：學技能、建分身、下指令、評表現**

DeepMind 展示了 Argon 在機器人生命週期中的代表性用法：

- 學習新技能：操控 Boston Dynamics 的 Spot 四足機器人（12 自由度腿部＋6 自由度手臂），在踩踏板丟垃圾前，先用 MuJoCo 打造帶鉸鏈的垃圾桶數位分身反覆練習動作。
- 視覺閉環控制：透過 Gemini Omni World Model 操控機器人，將打散的 Scrabble 字母磚重新排列成單字，過程中 Argon 會寫出帶時間戳的動作提示、檢視模擬關鍵影格，再反覆修正指令，而非下一次性的靜態指令。
- 建立數位分身：觀看一段真實機器人遠端操作錄影，自動建立外觀與接觸行為都相符的模擬資產，並以視覺推理迭代調校場景與物理參數。
- 人類動作重定向：從第一人稱操作影片中辨識關鍵物件，把簡單的邊界框換成可處理凹面容器的凸分解網格，再把人類手部軌跡重定向到一個 76 自由度、雙手各 22 自由度的雙手人形機器人上，於 MuJoCo 接觸物理中運作。

📊 **用模擬資料把真實成功率從 56% 拉到 75%**

Argon 也被用來當作生成式視覺-語言-動作（VLA）模型的資料來源：只靠一張真實桌面的 RGB 照片，Argon 就能自動建出校準過的 MuJoCo 模擬分身、定義新任務，並合成閉環動作產生器，收集超過 4,500 筆領域隨機化（domain-randomized）模擬情節，最終把真實機器人的任務成功率從 56% 提升到 75%，完成時間則從 35 秒縮短到 24 秒。

💡 **不只是控制器，還是評分員**

DeepMind 也示範 Argon 作為機器人任務的「通用價值函數」：分析一段 60 秒的雙手環形分揀操作錄影，Argon 能同步檢視頭部與左右夾爪的攝影機畫面，在接觸轉換點前後產生任務進度預測，並把整段軌跡拆成 28 個正、中性、負進度片段。另一個案例中，針對一段 136 秒的雙手摺紙影片，Argon 產出四層時間對齊的事後標註：整體目標、6 個語意子任務、17 個接觸級原子動作，以及能在操作失誤時讓任務進度持平、不會誤判的品質控制重加權機制。此外，給定一張紙本手繪草圖，Argon 也能自動建構 GPU 加速的 mujoco_warp 場景、合成 76 自由度全身動作軌跡，並驗證物理閉環中的結果。

🎯 **實務啟示**

對機器人團隊而言，比起單一能力提升，更值得關注的是 Argon 把「建模擬環境、生成訓練資料、評估操作品質」這幾個通常需要不同工具鏈的步驟，收斂成同一個模型的自然語言工作流程，這可能顯著降低 sim-to-real 資料生產的門檻。

🔗 **來源**
- 標題：Gemini 4 Argon for Robotics
- 作者／機構：Google DeepMind
- 連結：https://deepmind.google/blog/gemini-4-argon-for-robotics/

#GeminiArgon #Robotics #GoogleDeepMind #PhysicalAGI #MuJoCo #VLA #EmbodiedAI #Sim2Real #RoboticsAI #ERQA
