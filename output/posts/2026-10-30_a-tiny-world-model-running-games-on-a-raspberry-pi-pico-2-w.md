---
title: A tiny world model running games on a Raspberry Pi Pico 2 W
source: Hacker News
url: https://github.com/SheepSeb/tinyworldformer
model: claude-code/sonnet
generated_at: '2026-10-30T21:36:01.037717'
score: 109
---

📌 兩個小網路,在一片 Pico 2 W 上同時「造夢」又「玩夢」

TL;DR:looped transformer 世界模型塞進微控制器,邊生成遊戲邊自己玩。

通常我們想到「世界模型生成遊戲畫面」,腦中浮現的是跑在 GPU 叢集上的大型 diffusion 模型。但這個專案把整套生成-決策迴圈,塞進了一片售價不到幾塊美元、只有 FPU 但沒有真正浮點加速器集群的 Raspberry Pi Pico 2 W 裡。

🤔 **想驗證:權重重複使用的 looped transformer,能不能小到塞進微控制器**

作者對 looped transformer 感興趣:同一個 transformer block 用相同權重反覆套用多次,而不是疊很多層不同的層。這種做法對記憶體很划算,因為不需要為每一層儲存獨立權重,於是作者想驗證一個 looped 世界模型是否能小到能在微控制器上執行。選擇 Pico 2 W 是因為它便宜且有 FPU;選擇小遊戲則是因為可以直接用 numpy 寫出遊戲的真實版本,逐格比對世界模型生成的畫面是否正確。後續又加上一個 streaming RL agent,讓板子可以在自己生成的「夢境」裡邊玩邊學。

🧩 **兩個網路各管一邊,互不碰觸真實遊戲**

整套系統由兩個小型神經網路組成:

- **世界模型網路**:輸入目前畫面 + 動作,預測下一幀畫面與 reward。架構是量化到 int8 的 looped transformer,參數量 26k–131k,每幀成本 2–8M 次乘加,靠錄製下來的真實遊玩資料訓練。
- **actor 網路**:輸入畫面,輸出動作。架構是雙隱藏層的 float32 MLP,參數量僅 9k–16k,每幀成本 9k–16k 次乘加,靠 streaming RL(stream-x)在真實遊戲或自己的夢境裡學習。

關鍵設計是:這兩個網路都從未接觸真正的遊戲引擎,actor 只看得到世界模型生成的畫面,世界模型也只接收 actor 給的動作。兩者都跑在 RP2350 的 core 1 上,core 0 則負責 USB 與顯示輸出。預訓練好的 actor 可以換成一個從零開始學習的全新 stream-x agent,而任何按鍵都能把控制權交還給玩家本人,直接進入夢境裡操作。

畫面會被切成一個個 2×2 到 6×6 不等的 cell patch(依遊戲而異,共 36 到 80 個 token),每個 patch 的 embedding 是各 cell 學到的向量加總,再加上位置向量與動作向量。模型本身是單一個 transformer block(attention + ReLU MLP),套用 1 到 4 次,每次輸入都會被加回去,且每一次通過後的輸出都會對照下一幀做訓練,因此實際執行時的迴圈次數就是在速度與準確度之間做取捨。Pico 上為了維持可用的 frame rate,選擇用 2 個迴圈。

📊 **五款小遊戲,準確率差距頗大**

作者用 numpy 寫了五款經典小遊戲,各自的世界模型表現(2 迴圈下,held-out 資料的「完全正確幀」比例):

| 遊戲 | 畫面大小 | 參數量 | 每幀乘加數 | 完全正確幀比例 |
|---|---|---|---|---|
| Breakout | 20×16 | 26k | 4.3M | 99.99% |
| Doom-lite(第一人稱 raycast) | 32×32 | 55k | 4.2M | 83.6% |
| Flappy Bird | 24×24 | 46k | 2.0M | 100% |
| Pong | 20×32 | 46k | 2.3M | 99.45% |
| Pac-Man lite | 48×48 | 131k | 8.2M | 86.4% |

「完全正確幀」是指 held-out 資料裡,預測畫面每一格都跟真實遊戲一致的比例(隨機事件剛發生後的幀被排除,因為那種幀本來就只能取樣、無法預測)。作者特別說明 Doom-lite 的 3D 視角有 768 個 cell,只要有一格牆面陰影錨錨錯,整幀就被算作錯誤,所以它的數字看起來比實際遊玩體驗差。

解碼規則也很關鍵,作者總結出三條:背景格(牆、磚塊、地板)各自獨立取最可能的 token;「單一物件」(球、玩家、每個鬼魂)要在所有 (格子, token) 組合裡做一次全局唯一選擇,確保畫面上永遠只有一個;隨機事件發生後(例如重新發球、重生),選項會從最佳選擇附近 2.2 logit 內取樣,而不是直接平均。作者提到,正是加入「單一全局選擇」這條規則,才把 Breakout 的完全正確幀比例從 91.6% 拉到 99.7%(原本第一版模型會同時畫出兩顆球)。

💡 **光靠錄製資料的準確率不夠,還要在夢境裡「抓換**

作者強調,光看錄製資料上的準確率不夠,因為 agent 會把夢境帶到訓練資料從未出現過的狀態,任何在那裡出現的錯誤都可能被 agent 利用。因此主要的檢驗方式是:一邊讓 agent 玩夢境,一邊把夢境畫面讀回遊戲狀態、套用真實規則算出正確結果,再跟模型預測的下一幀與 reward 比對。在每款遊戲跑 5,000 個夢境步驟(2 迴圈)的結果顯示,Flappy Bird 和 Pong 幾乎零錯誤,Pac-Man 相對較多(742 次錯誤遊戲狀態、38 次錯誤 reward),Doom-lite 每步平均只有 1.50 個錯誤格。

訓練流程是先讓 agent 玩真實遊戲、把每一步 (畫面, 動作, 下一幀, reward) 都記錄下來(每款遊戲 1–3 百萬筆),部分 episode 故意從不尋常狀態開始(如有破洞的磚塊牆)以增加資料覆蓋面;接著用逐格的 cross-entropy loss 訓練世界模型,30k 步裡前 3–4k 步用 float 跑,之後切到 int8 量化訓練(QAT)。最終 int8 權重會寫成 Rust 原始碼,每個 float 都以精確位元儲存,並用 cargo test 驗證跟 Python 整數規格逐位元一致,再把固件燒進 Pico。

⚠️ **agent 會抓世界模型的漏洞**

作者也坦言,在不同遊戲裡訓練出的 agent 曾經學會利用世界模型的弱點,例如對「這格有變化」加權的 loss 會讓模型偏向預測變化,結果同時畫出兩顆球、打破兩塊磚。最終靠改成針對輸入幀中「可能發生變化的位置」加權,加上前述的全局單一選擇規則才解決。

🎯 **實務啟示**

這個專案證明了「世界模型 + 決策網路」這套架構並不一定要堆到數十億參數才能運作,只要遊戲狀態足夠簡單、可以被完整編碼進一張畫面,幾萬參數的 looped transformer 配上幾千參數的 MLP 就能在微控制器上即時生成並遊玩。對嘗試邊緣裝置部署生成式模型的工程師而言,這提供了一個具體的可複現案例:權重重複使用(loop 而非疊層)是壓縮模型尺寸的有效手段,而嚴謹的「夢境內校驗」機制則是避免 agent 利用模型漏洞的關鍵防線。

🔗 **來源**
- 標題:A tiny world model running games on a Raspberry Pi Pico 2 W
- 作者/機構:airinei(SheepSeb)
- 連結:https://github.com/SheepSeb/tinyworldformer

#WorldModel #LoopedTransformer #EdgeAI #Microcontroller #RaspberryPiPico #Quantization #ReinforcementLearning #GenerativeModel #INT8 #EmbeddedML
