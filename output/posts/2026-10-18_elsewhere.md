---
title: Elsewhere
source: Simon Willison
url: https://simonwillison.net/elsewhere/
model: claude-code/sonnet
generated_at: '2026-10-18T19:40:15.382135'
score: 63
---

📌 用「畫鵜鶘」土法測試：Gemini 4 Argon與Meta Muse Wonder怎麼評分

TL;DR：Simon Willison用招牌的鵜鶘SVG測試法，記錄了Gemini 4 Argon與Meta Muse Wonder的首次體驗與定價。

當模型跑分表格多到已經比不出差異時，Willison還是堅持用同一招——叫模型畫一隻鵜鶘，看圖說故事。這次輪到Gemini 4 Argon和Meta的Muse Wonder。

🤔 **一招用到底的非正式基準**

Willison長期用「請模型生成鵜鶘SVG」作為非正式但一致的模型能力快照。他在部落格「Elsewhere」欄位記錄了為llm-gemini與llm-meta-ai兩個外掛新增支援的過程，順手留下了兩個新模型的第一手觀察。

🧩 **Gemini 4 Argon：定價12月就翻倍**

Gemini 4 Argon今日透過Gemini API與每月100美元訂閱方案開放。Willison測了低、中、高三種推理強度，都生成出不錯的SVG——他指出Gemini一直在SVG生成上有口碑，是他所知唯一有員工專門鑽研SVG生成、並公開展示過鵜鶘作品的實驗室。高強度那張圖他算過成本是17.166美分。定價方面，Argon上市價是每百萬token輸入2美元、輸出10美元，與GPT-6 Sol同價，是Claude Opus 5.5的一半、Claude Fable 5.1與GPT-6 Astra的五分之一。但這個價格會在12月1日起翻倍，屆時將與Opus 5.5同價。

📊 **Artificial Analysis的「跑完整套測試總花費」才是真指標**

Artificial Analysis公布的「跑完整套benchmark總花費」指標上，Argon只要2,407美元，接近GLM-5.3，明顯低於OpenAI、Anthropic與Meta最新模型；即使12月漲價後，仍會比GPT-6 Astra略便宜。

📊 **Meta Muse Wonder：可能是Meta第一個Fable級模型**

Meta AI同期發布Muse Wonder與Muse Wonder Full，稱為「最強模型」。Willison觀察這看起來可能是Meta第一個Fable級模型——Artificial Analysis將Muse Wonder（Max）評為與GPT-6.1 Sol相當。他同步畫出六種推理等級（minimal、low、medium、high、xhigh、max）的鵜鶘，並與9月2日的Muse 1.3、8月5日的Muse 1.2做對比，觀察是：Meta幾乎每月都推新模型，至少從畫鵜鶘的結果看，每次迭代的進步都算實質。

💡 **定價已經不夠用來比較模型**

Willison特別提醒，現在光看每百萬token的定價已經意義有限，真正該比較的是一個模型在agentic harness裡完成同一個任務要耗掉多少token——這正是Artificial Analysis「跑完benchmark總花費」這個指標的價值所在，它把推理效率也算進了價格比較。

🎯 **實務啟示**

挑模型時，與其只看牌價，不如換算成「完成任務的總花費」。另外，Willison這次也把自己的tokenizer工具ttok從0.4升級成1.0正式版，順手把預設tokenizer從GPT-4切換成GPT-5/6家族——OpenAI官方尚未證實GPT-6與GPT-5家族共用同一套tokenizer，但社群已有實驗支持兩者很可能相同。這提醒如果你的工具鏈裡還掛著舊版token計數邏輯，可能已經在用錯誤的tokenizer估算新模型的用量。

🔗 **來源**
- 標題：Elsewhere
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/elsewhere/

#Gemini #GoogleDeepMind #MetaAI #LLM #AIBenchmark #ModelComparison #GenerativeAI #PelicanTest #AICost #DeveloperTools
