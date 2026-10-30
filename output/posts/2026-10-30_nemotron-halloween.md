---
title: nemotron-halloween
source: HuggingFace Blog
url: https://huggingface.co/blog/nvidia/nemotron-halloween
model: claude-code/sonnet
generated_at: '2026-10-30T21:46:51.875625'
score: 76
---

📌 用 NVIDIA Nemotron 打造一隻會抱怨的萬聖節鬼屋

TL;DR：用開源 Nemotron 模型群堆出會嫌棄訪客、聽到「請」才肯給糖的萬聖節互動鬼屋。

當車庫門長出一張嘴，用海盜口音抱怨你打擾了它休息，萬聖節的糖果就不再是單向發放了。這是 NVIDIA 員工 Rick Grandy 用公司自家開源 Nemotron 模型群打造的作品：MonsterHouse。

🤔 從一張嘴開始的鬼屋

作者想讓造訪的孩子們有獨特互動體驗：房子負責發糖，但個性設定成「嫌棄多過驚嚇」。最後的解法是給車庫門裝一張嘴，教它抱怨。MonsterHouse 的背景故事被設定成一艘沉沒海盜船的殘骸木材重建而成的建築，因此帶著滿腹牢騷與海盜式抱怨。

🧩 六道技術管線：聽、想、說、動、看、指揮

整套系統建立在 NVIDIA Nemotron Voice Agent 這個協調框架上，由多個模型分工：
- 聽（ASR）：NVIDIA Nemotron 3 ASR 將訪客語音轉成文字（作者標記使用的是 nemotron-speech-streaming-en-0.6b.q8_0.gguf）。
- 想（對話）：NVIDIA Nemotron 3.5 Bolt E4B 4GB，一個為對話代理設計的開源小型語言模型，負責生成每句回覆，個性由一個 LoRA adapter 賦予。
- 說（語音合成）：NVIDIA Magpie TTS Zeroshot 只需一段簡短的參考語音樣本，就能用角色聲音念出回覆。
- 動（動畫）：NVIDIA Audio2Face-3D 把乾淨的語音轉成嘴型動畫，驅動 Unreal Engine 5 中的角色。
- 看（視覺）：NVIDIA Nemotron 3 Nano Omni 負責描述訪客的服裝，YOLO 與 ByteTrack 負責計數與追蹤訪客。
- 指揮：整套系統由 NVIDIA Nemotron Voice Agent 在單一工作站上協調，硬體是一張 NVIDIA RTX PRO 6000 Blackwell Max-Q 加一張 NVIDIA RTX PRO 4000 Blackwell。

角色模型（SkelMesh）在 Autodesk Maya 中製作，匯出到 Unreal Engine 後再加上虛擬火焰效果；由於沒有眼睛、眉毛，也不會眨眼，作者形容這是「相當經濟的怪物」。

💡 用 5000 筆對話訓練出的壞脾氣

為了讓車庫門個性鮮明又不會無限跳針，作者設計了一套對話流程：一開始會用「我正忙著抱怨，去煩鄰居吧！」打發訪客，但訪客若持續禮貌以對，一句「請」就能馬上破冰，一句「謝謝」則能換來溫暖道別，一旦訪客贏得好感，角色就會記住這段互動，不再重新刁難。

作者測試了十幾個模型，最終選擇 Bolt E4B 作為對話引擎，使用 4-bit 量化版本（名稱中的「4GB」）作為預設回覆模型，並保留 BF16 版本供比較。作者提到自己身為 NVIDIA 員工，得以在正式發布前測試 Bolt E4B，並認為其記憶體佔用比 Qwen3 30B-A3B 與 Qwen 3.6 35B-A3B 更小。為了讓角色性格更穩定，作者建立了一個超過 5000 筆多輪對話的資料集，為每個候選模型訓練專屬 LoRA，訓練時間從約一小時到數小時不等，資料集本身則由一套本地代理搭配一個大型 LLM 共同生成並評分。

📊 回應速度：1.70 秒 vs 快取後 0.72 秒

為了讓鬼屋「反應夠快，才有威嚴」，作者在管線中做了兩種捷徑：已撰寫好的文字可跳過即時生成對話，已儲存的音訊則可跳過語音合成。文中數據顯示，使用 Bolt Q4 搭配 TTS 的「語音結束到回覆音訊輸出」中位數時間為 1.70 秒，若命中快取的常見回覆則可降到 0.72 秒（目前語音結束偵測需等待 300 毫秒的靜音）。

Magpie TTS Zeroshot 的零樣本語音克隆技術只需一段簡短參考樣本就能套用角色聲線，作者為角色設計了七種情緒（從不爽、具威脅感到驚喜、欣喜），每種情緒各錄製一段 3 到 10 秒的語音樣本，再透過 prompt 範本與 LLM 給出的情緒標籤，決定每句臺詞該用哪種語氣演出。

⚠️ 自我侷限：離線運算預算下的角色設計

作者強調，因為希望整套系統能離線、自主運行，記憶體與運算資源都有明確上限，角色不能只靠一句「扮演壞脾氣」的 prompt 撐起來，還必須遵循一套完整對話流程、追蹤互動狀態，同時留出足夠運算資源給管線其他環節（語音辨識、語音合成、動畫）同時運作。

🎯 實務啟示

這個專案示範了一條完整的「開源小模型拼裝」路徑：ASR、小型 LLM、TTS、動畫驅動模型各自負責單一任務，再用一個協調框架與 LoRA 微調把它們黏成一個有個性的即時互動角色。對想在邊緣裝置或單一工作站上做即時語音代理的工程師來說，這套管線分工與延遲最佳化手法（文字／音訊快取、情緒標籤、流式輸出）比任何單一模型的效能數字都更值得參考。

🔗 來源
- 標題：nemotron-halloween: Building a Haunted House with NVIDIA Nemotron Open Models
- 作者／機構：Rick Grandy、Maryam Motamedi（NVIDIA）, HuggingFace Blog
- 連結：https://huggingface.co/blog/nvidia/nemotron-halloween

#NVIDIA #Nemotron #OpenSourceAI #VoiceAgent #TextToSpeech #LoRA #EdgeAI #ConversationalAI #UnrealEngine #Halloween
