---
title: Tencent Hy4 is live on Together AI
source: Together AI
url: https://www.together.ai/blog/tencent-hy4
model: claude-code/sonnet
generated_at: '2026-11-20T23:22:26.659347'
score: 72
---

📌 Tencent Hy4上線Together AI,讀圖寫遊戲一次到位

TL;DR:Tencent 旗艦模型 Hy4 登上 Together AI,首度支援影像輸入與1M context,定價已公開。

一張截圖丟進去,模型不只讀出圖表上的數字,還把整張圖重新刻成一個網頁;換個提示詞,它又生出一個能玩、能輸的小遊戲。這不是示範影片,是 Together AI 自己動手測出來的結果。

🤔 **Hy4是誰:Tencent Hy家族的第一次「看圖」**

Hy4 是 Tencent 的旗艦模型,也是 Hy 系列第一個支援影像輸入的版本,延續前代 Hy4 Preview,新增了圖像理解與電腦操作(computer-use)能力。Tencent 官方宣稱,他們特別訓練這個模型去操作 Blender、CAD 等專業軟體,並與自家產品團隊合作,在辦公室事務、財務研究,以及使用 Unreal Engine、Unity、Godot 的遊戲開發場景上訓練與評估過 Hy4。

🧩 **架構與規格**

根據 Together AI 的介紹,Hy4 是一個 Mixture-of-Experts(MoE)模型,總參數量 770B,每個 token 實際啟用 49B 參數。它支援 1M token 的 context window,同時可接收文字與影像輸入,並支援 tool calling 與 JSON 輸出。

🧩 **怎麼用:Together Serverless Inference**

Hy4 現在可以透過模型字串 `tencent/Hy4` 在 Together 的 chat completions API 上直接呼叫。官方給出的範例是把一張圖表轉成 base64,連同文字提示一起送進去,並用 `response_format={"type": "json_object"}` 要求模型回傳結構化的 JSON:

```python
import base64
from together import Together

client = Together()
with open("chart.png", "rb") as f:
    image = base64.b64encode(f.read()).decode()

response = client.chat.completions.create(
    model="tencent/Hy4",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "Read this chart. Return a JSON object with a title and a list of bars, each with a label and a value."},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image}"}},
        ],
    }],
    response_format={"type": "json_object"},
)
print(response.choices[0].message.content)
```

安裝只需要 `pip install together` 並設定好 `TOGETHER_API_KEY`,也可以先在 playground 裡直接試用,不用寫程式碼。

📊 **實測:讀圖、重建圖表、寫遊戲**

Together AI 用自家部落格文章裡的一張圖表測試 Hy4 的 vision 能力,請它把圖表內容轉成 JSON,模型精準讀出標題與三個長條的數值;接著要求它只憑同一張截圖重建成單一 HTML 檔案,Hy4 不但還原了版面、標籤、數值、顏色,連虛線的天花板線與頁尾註腳都重現出來,只有字型因為被要求用通用字型而有差異。

第二個測試是純文字提示,要求 Hy4 寫一個單一 HTML 檔、不依賴任何函式庫或外部素材的小遊戲,附鍵盤控制、計分與輸局邏輯。Hy4 交出一款名為「Polarity」的遊戲:方塊從畫面上方落下,玩家要用空白鍵切換顏色去接住同色方塊,黃色危險方塊落地就結束遊戲。Together AI 表示,他們把回覆直接存成 HTML 檔案、不做任何修改就打開瀏覽器測試,結果可以完整玩完一輪並重新開始;Hy4 甚至主動加了說明規則的標題畫面,以及會跨局保留的最高分紀錄,這些都是提示詞裡沒有要求的。

💡 **定價怎麼算**

Together Serverless Inference 上的 Hy4 定價為每 1M input tokens 0.83 美元、每 1M cached input tokens 0.042 美元、每 1M output tokens 2.50 美元。cached input 的價格明顯低於一般輸入,對於重複帶入長 system prompt 或固定上下文的應用來說,這會是壓低成本的關鍵槓桿。

🎯 **實務啟示**

對於要做圖表理解、報表自動化,或是需要長 context 配合影像輸入的應用,Hy4 提供了一個可以直接在 serverless API 上測試的旗艦級選項;而 1M context 加上內建 tool calling 與 JSON 輸出,也讓它適合接入既有的 agent 工作流,不需要額外包一層格式轉換。

🔗 **來源**
- 標題:Tencent Hy4 is live on Together AI
- 作者/機構:Together AI
- 連結:https://www.together.ai/blog/tencent-hy4

#TencentHy4 #TogetherAI #MixtureOfExperts #MultimodalAI #LLM #VisionLanguageModel #ServerlessInference #AIAgents #ToolCalling #GenerativeAI
