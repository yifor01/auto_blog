---
title: Nanbeige Releases Nanbeige4.3-33B, a 33B Open Agentic Coding Model
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/25/nanbeige-releases-nanbeige4-3-33b-open-agentic-coding-model/
model: claude-code/sonnet
generated_at: '2026-10-26T21:52:50.146993'
score: 83
---

📌 Nanbeige4.3-33B開源:33B dense模型主打agentic coding

TL;DR：招聘平臺BOSS直聘旗下實驗室開源33B dense編碼agent模型,支援52萬token上下文。

當多數團隊忙著堆疊MoE參數時,Nanbeige LLM Lab選擇用一個「老派」架構打agentic coding戰場——沒有專家路由,33B參數全部參與每一次推理。

🤔 誰在做、為什麼做

Nanbeige LLM Lab隸屬於招聘平臺BOSS直聘,在Hugging Face以Apache 2.0授權發布了Nanbeige4.3-33B,定位是處理agentic coding與辦公室「cowork」類任務的33B dense語言模型。團隊同時發布了對應的Base版本供外部做客製化post-training。該實驗室的策略是先打造一個夠強的「teacher」模型,之後再把agentic能力蒸餾(distill)到更小的模型上,第一個目標是Nanbeige4.3-3B。

🧩 架構與agent介面設計

根據config.json,Nanbeige4.3-33B採用標準的LlamaForCausalLM架構,沒有expert routing,代表全部33B參數會在每個token上運算,屬於dense模型而非MoE。其chat template對外開放三個控制項:enable_thinking用來切換推理模式,預設為開啟;preserve_thinking會保留前幾輪對話中的推理內容,官方建議在多輪工具呼叫與coding agent場景下開啟;另外傳入tools參數即可啟用工具呼叫,官方建議搭配XML格式的呼叫語法。模型支援524,288 token的上下文窗口。

📊 自評benchmark:贏17個,但有3個輸且有數據存疑

Nanbeige在自家模型卡中,用相同的推理強度設定、共享的超參數與測試harness,將Nanbeige4.3-33B與三個約30B規模的開源模型——Qwen3.8-27B、Muse-Glimmer-30B、Gemma4-31B——做了20項benchmark比較,宣稱領先17項。

| Benchmark | Nanbeige4.3-33B | 對手分數 | 領先者 |
|---|---|---|---|
| SWE-Bench Pro | 60.3 | Qwen3.8-27B 61.7 | Qwen3.8-27B |
| GDPval | 84.8 | Qwen3.8-27B 86.4 | Qwen3.8-27B |
| GPQA Diamond | 89.5 | Gemma4-31B 91.3 | Gemma4-31B |

Base模型版本則在8項報告的任務上全數領先Gemma4-31B-Base,例如MMLU-Pro(66.9 vs 59.3)與GPQA(62.0 vs 41.5)。

需要留意的是,這些分數全部由Nanbeige自行測量並公布,對手模型的數字則取自各家自己的Hugging Face模型卡,不同harness的差異可能解釋了部分落差。文中特別提到SWE-Bench Pro那一行的數字「看起來像是對調了」,因此這份比較表應視為初步參考,等待獨立第三方測試驗證後再下判斷。

🛠️ 怎麼跑起來

模型卡提供了Transformers、SGLang與vLLM三種部署範例,伺服器範例使用4-way tensor parallelism,搭配Qwen3的reasoning與tool-call解析器。官方建議的推理設定分兩套:agent使用情境下temperature 1.0、top_p 0.95、最大生成長度65,536 token;一般推理與對話情境下temperature 0.6、最大生成長度262,144 token。

依config.json推算,BF16權重約需66 GB記憶體,KV cache每個token約佔208 KiB(BF16),若要跑滿524,288 token的完整上下文,KV cache本身就需要約112 GB。截至發布時,Hugging Face Inference Provider尚未上架此模型,意味著想用需要自行架設推理服務。

🎯 實務啟示

對於想要自架agentic coding模型的團隊,Nanbeige4.3-33B提供了Apache 2.0授權、長上下文與現成的部署範例,是一個可以納入評估清單的選項;但自評數據的落差提醒我們,在投入生產環境前,至少該用自己的任務集重新跑一次SWE-Bench Pro之類的測試,而不是直接拿模型卡上的表格做決策。另外,112 GB的滿載KV cache需求也意味著長上下文場景的部署成本不容小覷。

🔗 來源
- 標題：Nanbeige Releases Nanbeige4.3-33B, a 33B Open Agentic Coding Model
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/25/nanbeige-releases-nanbeige4-3-33b-open-agentic-coding-model/

#OpenSourceLLM #AgenticCoding #Nanbeige #HuggingFace #LLM #DenseModel #vLLM #SGLang #LongContext #AICoding
