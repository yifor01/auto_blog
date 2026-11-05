---
title: 'Gemini Omni 1.2 Flash: Fast and cost-effective with longer clips'
source: Google DeepMind
url: https://deepmind.google/blog/gemini-omni-12-flash-fast-and-cost-effective-with-longer-clips/
model: claude-code/sonnet
generated_at: '2026-11-05T22:50:44.807697'
pinned: true
---

📌 Google DeepMind 推出 Gemini Omni 1.2 Flash，影片長度拉到 15 秒、降價三成

TL;DR：Gemini Omni 1.2 Flash 支援 15 秒原生影片生成與多輪對話式編輯，720p 每秒只要 $0.07。

如果一支生成影片只能撐 10 秒，故事通常還沒講完就得剪斷。Google DeepMind 這次把生成長度上限往後推了 5 秒，還順手把價格砍了三成。

🤔 **從 10 秒到 15 秒，不只是變長**
Gemini Omni 1.1 Flash 原本支援到 10 秒的影片生成，1.2 版本原生支援到 15 秒，並且可以用 1 秒為單位，指定 3 到 15 秒之間的任意長度，讓完整故事、產品說明或完整社群廣告可以在單次生成裡完成，不用再靠多段拼接。

🧩 **更便宜、更快的工作流程**
除了直接降價 30%（720p 影片每秒 $0.07），素材描述的實際工作流程是：先用 360p 或 720p 快速起稿，用後續對話式編輯修正細節而不用整支重新生成,最後再把滿意的結果升級到 1080p 或 4K，整體成本因此壓低。

📊 **更強的參考一致性（reference adherence）**
生成時可以同時給角色、產品或風格的參考圖片、最長 3 秒的動態片段，以及音訊線索，1.2 Flash 能把這些細節從頭維持到尾，臉部、服裝、包裝字體與品牌色彩在不同鏡頭角度下都保持一致。素材舉的例子是：輸入一張模特兒照片，加上三套服裝的正反面照片，就能生成一支 15 秒、包含 360 度旋轉與 match cut 的虛擬試穿影片，模特兒身份以及每件服裝的剪裁、垂墜與背面細節全程保持一致。

📊 **更穩定的畫面一致性**
從第一格到最後一格，角色、物件與場景在運鏡與轉場之間的視覺漂移或變形更少。素材給出的對比是：給定同一張靜態攝影棚打光的展覽海報，和同一段五層動畫 prompt，Gemini Omni 1.1 Flash 跟參考圖的貼合度不如 1.2，1.2 版本能逐層組裝出材質、陰影與字體細節，並一路鎖定到最後一格。

📊 **多輪對話式編輯**
不用整支重新生成，就可以逐輪調整同一支影片，例如替換產品或背景、改變燈光或天氣、切換長寬比，而且這種編輯支援完整 15 秒片段，方便針對不同受眾或版位快速產出廣告變體，不用每次重新寫 prompt。

💡 **語音與運鏡也一併升級**
素材提到，1.2 Flash 能生成更流暢自然的對白、更清晰的口型同步，以及可區分的多角色語音條件；在運鏡上，可以執行像 FPV 穿越飛行、戲劇性 zoom-out 或環繞這類複雜連續運鏡，不必要的跳接更少、縮放更穩定，畫面也更接近電影質感。輸出內容會帶有不易察覺的 SynthID 水印，並提供 Provisioned Throughput。

⚠️ **仍有待改善的場景**
素材明確指出，團隊仍在持續改善快速體育動作、劇本快速變化與複雜物理這幾類場景的表現，代表這些目前還不是這個版本的強項。

🎯 **實務啟示**
「低解析度草稿 + 對話式局部編輯 + 最後升級解析度」這個工作流程本身就值得影片生成應用直接參考，能明顯降低迭代成本；reference adherence 的提升也意味著電商試穿、產品目錄這類需要跨鏡頭維持細節一致的場景，現在更適合用生成式影片取代一部分傳統拍攝流程。這個版本已經在 Gemini API、Google Cloud 與 Google Vids 上可用，可以直接在 Google AI Studio 裡試跑。

🔗 **來源**
- 標題：Gemini Omni 1.2 Flash: Fast and cost-effective with longer clips
- 作者／機構：Google DeepMind
- 連結：https://deepmind.google/blog/gemini-omni-12-flash-fast-and-cost-effective-with-longer-clips/

#GoogleDeepMind #Gemini #GenerativeAI #VideoGeneration #AIVideo #TextToVideo #GenAI #GeminiAPI #CreativeAI #MachineLearning
