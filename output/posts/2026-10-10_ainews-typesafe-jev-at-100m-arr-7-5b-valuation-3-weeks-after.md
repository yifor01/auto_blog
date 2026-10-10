---
title: '[AINews] TypeSafe/Jev at >$100M ARR, $7.5B valuation 3 weeks after launch'
source: Latent Space
url: https://www.latent.space/p/ainews-typesafejev-at-100m-arr-75b
model: claude-code/sonnet
generated_at: '2026-10-10T20:44:14.729390'
score: 80
---

📌 「Decision Model」一天內被五家公司同時推出，Jev成了業界的基準線

TL;DR：Jev掀起的「決策模型」賽道一天內湧入多家對手，TypeSafe則傳出首週就破億美元ARR。

同一天內，OpenAI、Microsoft、Perplexity、Cloudflare、Liquid五家公司不約而同推出同一種東西：不輸出長篇文字，只回傳機率、選項或分數的「決策模型(decision model)」。而這整個賽道的參考基準，正是TypeSafe推出的Jev——根據Latent Space的AINews彙整，TypeSafe對外宣布了「Series AI」募資，Sequoia方面則「流出」消息稱Jev首週營收就衝破年化1億美元(ARR)。雖然也有人質疑這是否涉及炒作(astroturfing)，但這波「決策模型」的產品型態擴散速度，確實值得工程師關注。

🤔 為什麼忽然大家都在做「決策模型」

這類模型的共同特徵，是把本來要靠LLM生成長文字再解析的任務，改成單次前向傳播直接回傳型別化答案：判斷某個條件成立的機率、從清單中挑一個選項、或依等級打分。好處很直接——Agent流程中很多步驟本質上就是yes/no的判斷，不需要生成，只需要決策。

📊 一天內湧入的對手名單

| 產品 | 定位 / 特色 |
|---|---|
| OpenAI Decisions API | 三種請求型態（機率、選清單、評分），支援文字+圖片，跑在GPT-6 Luna上，$0.10/M輸入token、輸出免費，官方宣稱「快達10倍」 |
| Microsoft-Decision-1 | 定位用於LLM判官與科學假設篩選，但早期評測者指出在一致性與複雜決策上仍有困難 |
| Perplexity pplx-decider-v1.1-27b | 宣稱在1,071個案例的Decision Bench中準確率達94.5%，成本每千次決策$0.017 |
| Cloudflare clef | clef-omni支援音訊、影片、圖片與文字；clef-flash比Jev更便宜，整體速度約快2倍；權重已上架Hugging Face |
| Liquid d1 | 上架Vercel AI Gateway，支援視覺輸入的分類、路由、評分任務 |

此外，vLLM Semantic Router推出Decision 2.0，能在一次前向傳播中針對同一輸入回答多個問題並附上每個選項的機率；LangSmith則直接拿Jev當judge，針對每一筆trace分別回傳難度與正確性的型別化答案。想自己訓練的話，Unsloth釋出免費notebook，能在8GB VRAM上把Qwen3.5-4B訓練成決策模型；另一篇walkthrough指出，用Qwen3.5-0.8B在60步、4GB VRAM、約10分鐘內，準確率就能從37%提升到65%。

💡 省錢的關鍵：把「該不該生成」也外包給小模型

LangChain方面指出，把每個任務路由給「夠用就好」的最便宜模型，讓Open SWE的任務中位數成本下降了64%。這也呼應了Apple與CMU提出的Selection-based Structured Reasoning（SSR）研究方向：在agent內部，用六種自然語言策略、以長度正規化的log-likelihood在一次共享KV cache的batched前向傳播中打分。結果是單輪推理延遲下降超過90%，但端到端延遲只下降28%到54%；在Qwen3-VL-4B搭配GRPO的設定下，平均成功率61.37%，相較TAPO+GSPO基線的61.25%幾乎持平。

⚠️ 熱度與雜音並存

Microsoft-Decision-1的早期評測者已點出其在一致性與複雜決策上的弱點，顯示「決策模型」距離成熟仍有落差。而TypeSafe/Jev這則「首週破億ARR」的消息，本身也伴隨外界對炒作的質疑，Latent Space在報導中也特別提及這點，讀者應把這類募資/估值消息當作尚待驗證的業界傳聞來看待，而非定論。

🎯 實務啟示

如果你的agent流程裡有大量yes/no、分類、打分的步驟，與其每次都呼叫完整的生成式LLM，評估改用decision model（或至少把這類步驟拆出來路由到更便宜的模型/端點）可能是立即能省下成本與延遲的切入點，LangChain的64%成本下降數字就是一個現成的參考案例。

🔗 來源
- 標題：[AINews] TypeSafe/Jev at >$100M ARR, $7.5B valuation 3 weeks after launch
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-typesafejev-at-100m-arr-75b

#DecisionModels #Jev #TypeSafe #LLMRouting #AgentEngineering #AIInfra #OpenAI #Perplexity #Cloudflare #LangChain
