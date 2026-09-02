---
title: Claude Fable 5.1 made me a really nice animated pelican
source: Simon Willison
url: https://simonwillison.net/2026/Sep/1/claude-fable-5-1/
model: claude-code/sonnet
generated_at: '2026-09-02T10:24:09.505165'
score: 84
---

📌 花 3.3 美元讓 Claude Fable 5.1 畫一隻騎腳踏車的鵜鶘，值得嗎

TL;DR：Simon Willison 實測 Fable 5.1 五種推理層級畫鵜鶘 SVG，token 用量與費用差距高達 33 倍。

同一個提示詞、同一個模型，只是把推理力度從 low 調到 max，輸出 token 數就能從不到兩千飆升到超過六萬五千。Simon Willison 用經典的「畫一隻騎腳踏車的鵜鶘」測試，把這個差距具體量化了出來。

🤔 **背景：鵜鶘基準測試正在失靈**

Anthropic 於 9 月 1 日發布 Fable 5.1，宣稱它「為程式編寫、知識工作與長時間問題解決任務樹立新標準」。官方公告花了不少篇幅談科學研究能力，宣稱在 8 月 27 日才首次公布的新基準測試 Terminal-Bench-Science 0.1 上拿下 52.6% 的分數。其他基準測試分數雖有小幅提升，但都不如這項科學基準測試亮眼。Willison 提到自己在今年 7 月曾寫過，他對「鵜鶘基準測試」（讓模型畫一隻騎腳踏車的鵜鶘 SVG）的信心正在下降，因為它與模型在其他任務上的表現之間的關聯性，似乎不像 2025 年那麼強了。他認為現在這項測試最有價值的地方,是拿來比較同一個模型家族內部的差異，特別是同一個提示詞在不同推理力度（reasoning effort）下的表現。

🧩 **五種推理層級，同一句提示詞**

Fable 5.1 提供五種推理力度：low、medium、high、xhigh、max，且沒有完全關閉推理的選項。Willison 先修好了 llm-anthropic 套件中一個導致推理過程未被正確記錄的問題，接著用「Generate an SVG of a pelican riding a bicycle」這句提示詞，跑遍全部五個層級。

📊 **token 用量與費用：33 倍差距**

| 推理層級 | 輸出 token 數 | 耗時 | 費用 |
|---|---|---|---|
| low | 1,998 | 23.8 秒 | $0.10017 |
| medium | 1,977 | 23 秒 | $0.09912 |
| high | 2,612 | 29.6 秒 | $0.13087 |
| xhigh | 36,767 | 7 分 51 秒 | $1.83 |
| max | 65,927 | 13 分 54 秒 | $3.30 |

有趣的是，low 與 medium 兩個層級的推理紀錄裡完全沒有摘要文字出現，且 medium 的輸出 token 數（1,977）還比 low（1,998）少了 21 個，像是這兩個層級對這個提示詞直接跳過了推理。到了 high，才開始出現簡短的推理摘要，內容大致是規劃 SVG 版面：天空與地面背景、雙輻條車輪、車架、坐墊與把手，以及白色身體、長脖子、橘色喙的鵜鶘,但與 low、medium 的成果相比並沒有明顯差異。真正出現質變的是 xhigh 與 max：xhigh 的推理紀錄相當冗長，裡面能看到「刻意讓鵜鶘的比例大於腳踏車以營造喜感」「接受畫面稍粗算是討喜、而不是過度雕琢」這類細節推敲；max 則是 Willison 見過 Anthropic 所有模型中畫得最好的一隻鵜鶘，背景配色協調、雙腳確實分別跨在車架兩側、腳踩在踏板上、翅膀搭在把手上，還多了一頂藍色小帽與一個裝著魚的籃子。他也坦言,論視覺巧思仍比不上 Gemini 3.7 Flash，但強調自己要的本來就只是一張 SVG，而模型也確實給出了 SVG。

max 版本的推理紀錄裡還能看到不少具體的設計權衡，例如考慮要不要加圍巾或帽子但選擇從簡、在腳踏車安全帽與鵜鶘招牌冠羽之間拉鋸取捨、因為喙與安全帽形狀重疊而縮小安全帽弧度、加上深色羽尖與鋸齒狀羽緣讓翅膀更自然、檢查安全帽通風孔是否落在邊界內、決定省略把手鈴鐺與輪胎反光等「非必要」細節，以及調整前叉曲線控制點讓車頭角度更順。

💡 **HN 網友的加碼提案：那動畫版呢？**

在 Hacker News 討論串中,網友 swalsh 留言：「這個基準測試都被解出來了，能不能做出動畫版？」Willison 不想再花 3 美元重跑一次 max，於是把 max 版本產出的 SVG 丟回模型，用預設的 High 推理層級請它做成動畫：輸入 6,121 token、輸出 26,201 token，費用 $1.37。轉出的影片中車輪轉動方向是反的，但他判斷這是轉檔成 MP4 時產生的瑕疵，原始 SVG 裡的方向其實是對的。

🎯 **實務啟示**

這組數據對正在用 Claude 系列模型做 agent 或內容生成的工程師有直接參考價值：推理力度每往上一階，token 與費用的增幅並非線性，而是在 xhigh、max 這兩檔出現跳躍式成長。若任務本質上不需要精雕細琢的長鏈推理，low 或 medium 檔位可能已經足夠且成本差距可觀；只有在真正需要模型反覆自我修正細節的任務上，才值得把推理力度開到 xhigh 甚至 max，並事先把費用預期抓好。

🔗 **來源**
- 標題：Claude Fable 5.1 made me a really nice animated pelican
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Sep/1/claude-fable-5-1/

#ClaudeFable #Anthropic #LLMBenchmark #PelicanBenchmark #ReasoningEffort #PromptEngineering #SVG #AIcost #TokenUsage #LLMEvaluation
