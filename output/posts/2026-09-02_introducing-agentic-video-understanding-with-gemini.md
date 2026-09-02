---
title: Introducing agentic video understanding with Gemini
source: Google DeepMind
url: https://deepmind.google/blog/introducing-agentic-video-in-gemini/
model: claude-code/sonnet
generated_at: '2026-09-02T10:02:01.685838'
pinned: true
---

📌 Gemini新增agentic影片理解，token省下最多88%

TL;DR：Gemini 3.7/3.6 Flash與3.5 Flash-Lite新增agentic影片理解，長影片分析成本可降66%、準確度可升7%。

分析一支90分鐘的演講影片，過去意味著要嘛付出天量token成本，要嘛犧牲關鍵細節。Google DeepMind這次的做法，是讓模型自己決定要看哪裡、用什麼速度看。

🤔 **問題出在固定幀率**

過去Gemini處理影片是「靜態」方式：模型以固定的每秒幀數（預設1 FPS，可透過API調整）攝入整支影片。這種方式對長影片特別不利——從10分鐘的教學影片到90分鐘的演講、甚至數小時的錄影，開發者往往得在「高token成本」與「犧牲細節的取樣技巧」之間二選一。

🧩 **運作方式：模型自己決定看哪裡、怎麼看**

Agentic影片理解的概念與先前推出的agentic vision（結合程式碼執行與模型原生圖像理解）相似，這次則是讓Gemini結合原生影片工具，主動、有目標地決定要觀察影片的哪個片段、以什麼速度、透過哪種模態（畫面幀、音訊或字幕逐字稿），只擷取真正需要的時刻與訊號。實作上，模型會透過一個agentic loop呼叫內部工具、載入影片中相關的片段，取代開發者過去得手動撰寫的邏輯，大幅降低開發負擔。

啟用方式也很直接，只需在API設定中把processing設為"agentic"：

```python
from google import genai
client = genai.Client()
interaction = client.interactions.create(
    model="gemini-3.7-flash",
    input=[
        {
            "type": "video",
            "uri": "https://youtu.be/7Z5Vy9JBANs",
            "processing": "agentic"
        },
        {
            "type": "text",
            "text": "What are the 3 most important announcements in this keynote?",
        },
    ],
)
print(interaction.output_text)
```

📊 **效能數字：省token、省成本、還更準**

| 指標 | 改善幅度 |
|---|---|
| Token消耗 | 最多降低88% |
| 分析成本 | 最多降低66% |
| 準確度 | 最多提升7% |

這項改善在長影片場景中特別明顯。在LongVideoBench這個長影片理解基準測試上，搭配agentic影片理解的Gemini 3.7 Flash展現出大幅的token節省與準確度提升，讓它在準確度與成本的權衡上落在目前受測模型中的柏拉圖前緣（pareto frontier），也就是同一成本下準確度最高、或同一準確度下成本最低的位置。

🧩 **四個具體應用場景**

- **次秒級時刻檢索**：抓出容易被1 FPS漏掉的瞬間狀態變化與精準剪輯點，讓自動化影片剪輯成為可能。
- **長影片「大海撈針」搜尋**：在數小時的影片中回答複雜問題，而不需要消耗數百萬token。
- **異常偵測**：針對有趣的時間窗以更高FPS重新取樣，檢視快速動作或細微的視覺異常。
- **動作與物件計數**：準確追蹤重複性的物理動作與畫面中不同的物件。

🎯 **實務啟示**

這項功能目前已透過Google AI Studio與Gemini Enterprise Agent Platform的Gemini API開放，涵蓋影片上傳與YouTube影片，採用標準token計價、沒有額外功能費用，等於是把processing參數改成"agentic"就能立即測試的低成本升級。如果你的產品涉及長影片摘要、內容審核、動作計數或影片問答，值得優先評估將現有pipeline切換到agentic模式，尤其在處理多小時錄影或教學影片時，token與成本的節省會更顯著。Google也提到未來幾個月會把此能力帶進Gemini app與YouTube的「Ask YouTube」功能，代表這項技術路線會持續擴大應用面。

🔗 **來源**
- 標題：Introducing agentic video understanding with Gemini
- 作者／機構：Google DeepMind — Rohan Doshi, Mario Lučić
- 連結：https://deepmind.google/blog/introducing-agentic-video-in-gemini/

#GoogleDeepMind #Gemini #AgenticAI #VideoUnderstanding #ComputerVision #AIStudio #MachineLearning #LLM #GenerativeAI #GeminiFlash
