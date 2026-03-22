---
title: "LLM 說「Wait」的時候到底在幹嘛——用資訊理論拆解 Aha moment"
date: "2026-03-17"
paper_url: "https://arxiv.org/abs/2603.15500"
paper_title: "Understanding Reasoning in LLMs through Strategic Information Allocation under Uncertainty"
tags: [Reasoning, Information-Theory, Chain-of-Thought, Aha-Moment]
tldr: "Aha moment 不是頓悟，是不確定性外顯化"
---

你一定看過 DeepSeek-R1 推理時突然冒出「Wait, let me reconsider」的行為。社群把這個叫 Aha moment——好像模型真的在那個瞬間「想通了」什麼。但它真的頓悟了嗎？Microsoft Research、KAIST 和 Seoul National University 的團隊用資訊理論拆開來看了。

結論有點殘酷：那些「Wait」token 不是頓悟，是模型在喊「我不確定」。

🧩 推理 token 不是每個都一樣值錢

這篇論文做的第一件事，是把推理鏈裡的 token 分成兩類：

→「procedural information」：一步一步的計算推導，展開方程式、代入數值、符號操作
→「epistemic verbalization」：模型把自己的不確定性講出來，像是「Wait」「Perhaps」「Let me reconsider」「I'm not sure about this」

然後用 mutual information 去量化：哪一類 token 對「最終答案對不對」這件事提供了更多資訊？

答案是後者。而且差距大到讓人意外。

🔬 純計算推理會「卡住」

最反直覺的發現：純粹的 procedural reasoning 會資訊停滯。

什麼意思？當模型走上一條錯誤的推理路徑，後續每一步計算提供的新資訊量急速衰減。想像你算錯了第三步，之後的第四、五、六步都基於錯誤前提在推，每步都很「自洽」，但對判斷答案對不對幾乎沒有幫助。模型困在自己的邏輯裡出不來。

論文用了一個很漂亮的方式驗證這件事。他們看了 Figure 2 裡 token-level entropy（模型在每個位置的預測信心）在正確和錯誤解答中的變化。結論是：兩者的下降趨勢幾乎一模一樣。

模型在寫錯誤答案的時候一樣「很有信心」。

局部的信心跟全局的正確性完全脫鉤。你沒辦法靠看模型「有多確定」來判斷它對不對。

而 epistemic verbalization 打破的就是這個停滯。當模型說出「Wait」，它在做的事情是把原本隱性的不確定性變成顯性的文字。這個「外顯化」動作本身攜帶了資訊，讓模型有機會跳出錯誤軌道。mutual information 的 peak 出現在 evaluative behaviors，也就是模型自我評估的段落，而不是計算段落。

📊 數字講話

實驗在 DeepSeek-R1-Distill 的 1.5B、14B、32B 三個尺寸上做的，另外也測了 Qwen2.5/3、LLaMA-3.1、Mistral。Benchmark 涵蓋 AIME24、AIME25、MATH、AMC、LIMO-v2（800 個樣本）。

幾個關鍵結果：

→ 把 epistemic token 遮掉：32B 模型表現掉「25%」，14B 掉「19%」
→ 蒸餾時拿掉 epistemic 內容：Qwen3-14B-Base 在 AIME24 從「60.0%」暴跌到「13.3%」，直接廢掉
→ LIMO 資料集裡，每 100 個樣本「Wait」出現「77」次
→ 小模型用更多 epistemic marker：1.5B 相比 14B，「Wait」多了「75%」，「Perhaps」多了「235%」

最後一點特別有意思。小模型能力上限比較低，所以更頻繁地需要外顯不確定性來幫助自己。跟人很像，越不熟一個題目，越會停下來說「等等，我想一下」。

🤔 所以呢

這篇改變了我對幾件事的看法。

第一，CoT 壓縮。現在很多人在研究怎麼把推理鏈縮短省 token。但這篇告訴你，不是所有 token 都一樣值錢。壓縮時如果不小心把 epistemic verbalization 砍掉，模型就失去了自我修正的能力。「13.3%」對「60.0%」，這個差距大到不能忽視。selective compression（保留 epistemic signal，壓縮 procedural redundancy）才是正確方向。

第二，RLVR 為什麼有效。論文暗示了一個前提：模型需要在預訓練階段就學會怎麼表達不確定性。如果 epistemic token 根本不在模型的 vocabulary support 裡（就像 Qwen2.5-Math-7B 那樣，那些 token 的 log probability 低到幾乎不會被生成），你再怎麼用 RL 推都推不出 Aha moment。

這解釋了為什麼有些模型怎麼練都練不出 reasoning 能力。不是訓練方法的問題，是底子就沒有。

第三，我們可能一直在用錯的指標評估推理品質。Token-level entropy 看起來像好指標，但它什麼都沒告訴你，模型可以一路自信地走到錯誤答案。真正該看的是 trajectory-level 的 mutual information，但這在部署環境幾乎不可能即時算。

一個開放問題：既然小模型需要更多 epistemic marker 來補償能力不足，蒸餾的時候有沒有可能刻意保留甚至放大這些 marker，而不是像現在大部分做法那樣把老師的推理鏈原封不動灌給學生？

📄 論文：https://arxiv.org/abs/2603.15500

<!-- fb -->

你一定看過 DeepSeek-R1 推理時冒出「Wait, let me reconsider」。社群叫這個 Aha moment，好像模型真的頓悟了。Microsoft Research、KAIST、SNU 的團隊用資訊理論拆開了這件事——那些「Wait」不是頓悟，是模型在喊「我不確定」。

🧩 推理 token 分兩類

→ procedural information：計算步驟
→ epistemic verbalization：不確定性外顯（Wait、Perhaps、I'm not sure）

純計算推理會「資訊停滯」，走上錯誤路徑後，後續每步都很自洽但提供不了新資訊。模型在寫錯答案時一樣「很有信心」。Epistemic verbalization 打破這個停滯。

📊 關鍵數字
→ 遮掉 epistemic token：32B 掉「25%」，14B 掉「19%」
→ 蒸餾不保留 epistemic 內容：AIME24 從「60.0%」暴跌到「13.3%」
→ 小模型用更多 epistemic marker：1.5B 比 14B 多「75%」的 Wait、「235%」的 Perhaps
→ Token-level entropy 在正確和錯誤解答中趨勢幾乎一樣，局部信心跟全局正確性脫鉤

🤔 CoT 壓縮不能亂砍 epistemic token。RLVR 有效的前提是模型已有 epistemic 詞彙。我們可能一直在用錯的指標評估推理品質。

#GenAI #Reasoning #InformationTheory #ChainOfThought #AhaMoment #DeepSeekR1 #LLM
