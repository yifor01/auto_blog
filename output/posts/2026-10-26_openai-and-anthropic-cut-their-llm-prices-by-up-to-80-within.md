---
title: OpenAI and Anthropic cut their LLM prices by up to 80% within a few months.
  Why?
source: Max Woolf
url: https://minimaxir.com/2026/10/cheap-llms/
model: claude-code/sonnet
generated_at: '2026-10-26T21:52:50.147209'
score: 79
---

📌 OpenAI、Anthropic半年內降價八成,發生了什麼事

TL;DR：幾個月內主流LLM定價腰斬甚至砍八成,根源是開源模型逼近與agent市場的低轉換成本。

如果你覺得這半年用API跑agent突然變便宜了不是錯覺——從6月到現在,同一等級的模型定價,有的砍了超過七成。

🤔 半年內的降價時間線

把OpenAI與Anthropic過去幾個月的主要模型發布串起來看,會發現一場明顯的「以牙還牙」:OpenAI發布GPT-5.6 Sol與Luna,Sol維持GPT-5.5原價$5/$30/$0.50,Luna主打便宜場景訂在$1/$6/$0.10;Anthropic則推出Claude Sonnet 5,以「暫時優惠」價$2/$10/$0.20上市,以及被視為Opus 4.5接班人的Claude Opus 5,定價$5/$25/$0.50。接著OpenAI把GPT-5.6 Luna直接砍價80%到$0.20/$1.20/$0.02,Anthropic隨即把Sonnet 5原本「暫時」的優惠價改為永久,OpenAI再把GPT-5.6 Sol降約20%至$4/$20/$0.40(為期三個月)。

Anthropic接著發布Claude Fable 5.1,定價$10/$50/$0.25,相較6月的Fable 5($10/$50/$1)在效能全面提升的同時,把cache read成本砍了75%。由於agent coding場景下cache read佔總token花費的96%至99%,且cache命中率常態在90%至100%之間,這個動作實際上讓使用成本整體下降了70%到75%。OpenAI則發布與Fable 5.1規格相近的GPT-6 Astra,定價同為$10/$50/$1但沒有砍cache成本,隨後又推出GPT-6 Sol,價格$2/$10/$0.20,直接是打折後Sol價格的一半,同步發布的GPT-6 Luna也是前代價格的一半($0.10/$0.50/$0.01)。

就在同一天,Anthropic發布Claude Opus 5.5,定價$4/$20/$0.20,官方明確表示「Opus 5.5所需的運算資源比Opus 5更低,定價也反映了這一點」,靠20%的輸入輸出降價加上更大幅的cache成本削減,總成本比Opus 5降了40%到60%,但效能評測優於Fable 5.1。後來GPT-6 Sol被發現效能不如預期,一週後OpenAI推出GPT-6.1 Sol,效能追平Astra,同時把cache價格再砍半到$2/$10/$0.10,符合Anthropic「cache read為input價5%」的比例,使這個模型家族累計降價達75%。

📊 降價時間線總覽

| 模型 | 定價(input/output/cache read, $/MTok) | 備註 |
|---|---|---|
| Claude Sonnet 5(上市優惠) | $2/$10/$0.20 | 原定暫時,後改永久 |
| Claude Opus 5 | $5/$25/$0.50 | — |
| GPT-5.6 Luna(降價後) | $0.20/$1.20/$0.02 | 降80% |
| GPT-5.6 Sol(降價後) | $4/$20/$0.40 | 降約20%,限三個月 |
| Claude Fable 5.1 | $10/$50/$0.25 | cache read降75% |
| GPT-6 Astra | $10/$50/$1 | 未砍cache成本 |
| GPT-6 Sol | $2/$10/$0.20 | 效能不如預期 |
| GPT-6 Luna | $0.10/$0.50/$0.01 | 前代一半價 |
| Claude Opus 5.5 | $4/$20/$0.20 | 總成本降40%-60% |
| GPT-6.1 Sol | $2/$10/$0.10 | cache再砍半 |

根據Vercel AI model gateway的數據,每token成本已經降到2026年4月水準的43.3%,但整體花費卻在上升,原因是模型進步的速度比降價速度更快,用量跟著膨脹。

💡 為什麼沒人敢降價低於八成以下的理由很簡單:開源模型在後面追

這波降價背後的驅動力,文章作者認為是模型逐漸商品化:要在自己的程式碼庫上試新模型,只需要在像OpenCode、Zed Agent這類harness裡切換一個選項,或換一個OpenRouter的API endpoint字串,轉換成本低到幾乎沒有護城河,加上Google、Meta等大廠與大量開源模型都是「足夠好」的替代品,價格壓力自然出現。

開源陣營的案例很具體:2026年4月發布的DeepSeek V4 Flash定價$0.14/$0.28/$0.0028,爆紅的關鍵其實是那個$0.0028——cache read只佔input價的2%,遠低於OpenAI、Anthropic當時5%到10%的比例,讓實際有效成本比表面定價更低,當時OpenAI也還沒有對應的小模型可以競爭。文章作者猜測,7月GPT-5.6 Luna那次80%的降價,正是為了對抗這類開源小模型。而最新的DeepSeek Flash V4.1 1017版本,在Artificial Analysis指數上的表現由24分跳到45分,價格卻維持在相近水準($0.15/$0.60/$0.003)。在OpenRouter上,承載DeepSeek V4 Flash的獨立供應商從5月的13家增加到1017版本的29家,其中Cloudflare、DeepInfra的有效成本已經逼近DeepSeek官方定價的10%以內,但這些低價供應商目前仍只佔整體token用量的少數。另外,Moonshot AI近期發布的Kimi K3.1 Pro,效能已與Claude Opus 5.5相當(Kimi得分55,Opus 5.5得分58),價格卻是input/output打五折,cache read價格與Opus 5.5相同($2/$10/$0.20)。

🎯 實務啟示

對正在規劃agent或RAG系統成本結構的工程師,這波降價代表幾件可行動的事:一是重新計算cache read在你的任務流程中佔比——如果你的agent大量依賴多輪對話與長上下文,cache價格的調整幅度對總成本的影響可能遠大於input/output價格本身;二是在OpenRouter之類的多供應商平臺上,同一個開源模型不同供應商的有效成本可能有明顯差距,值得用「最低價格」路由策略做測試;三是模型選擇的「黏性」已經很低,建立一套可以快速切換模型與harness的評測pipeline,會比押注單一供應商更划算。

🔗 來源
- 標題：OpenAI and Anthropic cut their LLM prices by up to 80% within a few months. Why?
- 連結：https://minimaxir.com/2026/10/cheap-llms/

#LLMPricing #OpenAI #Anthropic #DeepSeek #OpenRouter #AgenticAI #AICoding #CloudCost #LLMCompetition #AIInfrastructure
