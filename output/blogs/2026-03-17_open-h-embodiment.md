---
title: "手術室裡的 AI 終於有數據可以練了——NVIDIA 聯合 35 機構開源 778 小時醫療機器人數據集"
date: "2026-03-17"
paper_url: "https://huggingface.co/blog/nvidia/physical-ai-for-healthcare-robotics"
paper_title: "The First Healthcare Robotics Dataset and Foundational Physical AI Models for Healthcare Robotics"
tags: [Robotics, Healthcare, Physical-AI, NVIDIA, Dataset]
tldr: "778 小時醫療機器人數據集 + 手術 VLA 模型"
---

自駕車有 nuScenes，通用機器人有 Open X-Embodiment，但醫療機器人呢？幾乎是空白。每個實驗室各自用自己那幾十小時的數據訓小模型，格式不通、機器人不通、做完就沒了。NVIDIA 這次拉了 Johns Hopkins、TU Munich 等 35 個機構，開源了一個 778 小時的醫療機器人數據集，還附上一個跨機體的 VLA 模型。我第一次看到有人認真從數據層開始做醫療機器人基礎模型這件事。

🏥 為什麼這個領域一直起不來

醫療機器人的數據困境不難理解。手術數據涉及隱私，採集成本極高，每個團隊用的機器人平台還不一樣。你拿 dVRK 手臂錄的手術示範，想拿來訓練 Franka 的控制策略？門都沒有。結果就是各自為政，每篇論文都是從零開始，模型離開自己實驗室就不能用。

簡單講，這個領域不是缺方法，是缺共享基礎設施。

Open-H-Embodiment 就是來補這個洞的。Steering committee 由 Johns Hopkins 的 Axel Krieger 教授、TU Munich 的 Nassir Navab 教授和 NVIDIA 的 Mahdi Azizian 博士帶領。

📦 數據集：778 小時、9 種機器人

幾個關鍵規格：

→ 778 小時操作數據，CC-BY-4.0 授權（可商用）
→ 35 個機構貢獻，32 個子數據集
→ 涵蓋 9 種機器人平台：商用的 CMR Surgical、Rob Surgical、Tuodao，研究用的 dVRK、Franka、Kuka
→ 任務類型：手術操作、超音波掃描、大腸鏡檢查

778 小時跟通用機器人數據集比不算多，但考慮到醫療領域之前大部分論文用的是幾十分鐘到幾個小時的數據，這直接跳了兩個數量級。

🤖 GR00T-H：一個模型操控九種機器人

光有數據還不夠，你得證明混合訓練有用。NVIDIA 做了 GR00T-H 這個 VLA 模型來驗證。基於 Isaac GR00T N 框架，視覺語言骨幹用 Cosmos Reason 2 2B，吃了大約 600 小時的數據。

架構上有幾個設計我覺得很值得聊：

Embodiment Projectors。每種機器人有自己的 MLP 投影層，把不同機器人的運動學空間映射到共享表示。想像成翻譯機：dVRK 的 7 軸關節角度和 Franka 的 7 軸關節角度，物理意義不同但都被投影到同一個「語言」。不用強迫所有機器人共享同一個 action space。

State Dropout 100%。訓練時完全丟掉機器人本體感知輸入，只靠視覺。這很激進。好處是推論時不依賴精確的狀態估計，壞處是......你真的確定在手術這種精度要求的場景，不看自己的手在哪裡沒問題嗎？論文沒有跟有狀態輸入的版本做 ablation，我很想看這個比較。

Relative EEF Actions。用相對末端執行器動作而不是絕對關節角度，進一步抹平不同機體的差異。

整體思路：投影層處理硬體差異、相對動作處理運動學差異、prompt 處理任務差異。每一層都在做抽象化。

🎮 World Model 模擬器：40 分鐘頂 2 天

這個部分我覺得最有意思。Cosmos-H-Surgical-Simulator 不是傳統的物理模擬器，而是從 Cosmos Predict 2.5 2B 微調出來的 world foundation model。你給它初始畫面和一串機器人動作指令，它就「想像」出接下來的手術場景。

action space 有 44 維，在 64 張 A100 上訓練了大約 10000 GPU 小時。

最吸引人的數字：生成 600 個訓練 rollout 只要 40 分鐘，同樣的量在實體 benchtop 上要 2 天。快了大約 72 倍。

這代表什麼？未來你想微調手術機器人策略，不一定要真的有一台手術機器人。先在「想像出來的手術室」裡大量練習，再到真機上做少量 fine-tuning。

但 world model 生成的影片跟真實物理之間的 gap 有多大？在你信任這些合成數據之前，這個問題必須有答案。

🤔 我怎麼看

正面的部分很清楚。醫療機器人領域太需要一個共享數據集了，Open-H-Embodiment 至少把大家拉到同一個湖裡。CC-BY-4.0 授權友善，商業公司可以直接拿去用。Embodiment Projector 的「讓每種機器人保留自己的表示，用輕量投影層對齊」思路值得其他做跨機體遷移的研究參考。

但我也有幾個疑慮。

778 小時分散在 32 個子數據集裡，平均每個才 24 小時。對某些特定機器人或任務，數據量可能還是不夠。GR00T-H 用了 600 小時訓練，但沒有 per-embodiment 的 breakdown，是不是某些機器人佔了大頭，其他的只是陪跑？

State Dropout 100% 讓我不太放心。完全不看本體感知，純靠視覺，在需要亞毫米精度的手術場景，這個 trade-off 能撐到什麼程度？

他們在 Future Directions 提到 reasoning-capable autonomy：機器人不只模仿動作，還要理解「為什麼做這個動作」。這需要全新類型的標註，包括 task traces、intent capture、outcome tracking。目前的 778 小時裡還沒有這些，下一步的數據採集會比現在難得多。

不管怎樣，有人把第一步踏出來了。如果你做 embodied AI 或醫療機器人，這個數據集值得花時間翻翻。如果你做的是通用機器人，Embodiment Projector 和 world model 合成數據的思路也可以借鑑。

一個我想不通的問題：當 world model 能生成以假亂真的手術影片時，我們怎麼確認用這些合成數據訓練出來的策略，在真實手術中是安全的？

📄 原文：https://huggingface.co/blog/nvidia/physical-ai-for-healthcare-robotics

<!-- fb -->

自駕車有 nuScenes，通用機器人有 Open X-Embodiment，但醫療機器人呢？幾乎是空白。NVIDIA 聯合 Johns Hopkins、TU Munich 等 35 個機構，開源了 778 小時醫療機器人數據集 Open-H-Embodiment，還附上跨機體的 VLA 模型 GR00T-H。

📦 數據集規格
→ 778 小時，CC-BY-4.0（可商用），32 個子數據集
→ 9 種機器人平台（dVRK、Franka、Kuka、CMR Surgical 等）
→ 涵蓋手術操作、超音波、大腸鏡

🤖 GR00T-H
→ 基於 Cosmos Reason 2 2B，約 600 小時訓練
→ Embodiment Projectors：每種機器人用 MLP 映射到共享空間
→ State Dropout 100%：純靠視覺，不吃本體感知

🎮 World Model 模擬器
→ 600 個 rollout 只要 40 分鐘，實體要 2 天，快 72 倍
→ 64 張 A100，約 10000 GPU 小時訓練

🤔 我怎麼看
醫療機器人太需要共享數據集了。但 778 小時分散在 32 個子集，每個平均才 24 小時。State Dropout 100% 在手術精度場景也需要更多驗證。最大的問題：world model 合成的手術數據，怎麼確認在真實手術中是安全的？

#GenAI #Robotics #Healthcare #PhysicalAI #NVIDIA #OpenSource #VLA
