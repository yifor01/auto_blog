---
title: Cerebras Deploys Trillion-Parameter AI Models
source: Hacker News
url: https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras
model: claude-code/sonnet
generated_at: '2026-10-25T19:43:11.030225'
score: 103
---

📌 Cerebras揭密：3兆參數模型怎麼塞進晶圓

TL;DR：Cerebras拆解如何把3兆參數模型跨59片晶圓部署，實現千token級推論速度。

一片Cerebras WSE-3T晶圓只有44 GB的晶片上記憶體，而一個3兆參數的前沿模型，權重本身就要吃掉好幾TB。這題要怎麼解？Cerebras在部落格裡，用開源模型Kimi K3當例子，拆解了整套部署邏輯。

🤔 **單晶片裝不下，但晶片之間要怎麼接才不拖慢速度**

Kimi K3是一個開源的3兆參數模型，有69層linear attention加24層dense attention，總共93層。這顆模型在Terminal-Bench 2.1拿下88.3%（對照GPT-5.6 Sol的88.8%），在BrowseComp拿下91.2%（對照GPT-5.6 Sol的90.4%），展現出前沿級的coding與agentic能力。Cerebras用的假設是：平均請求長度256k、4-bit權重量化（跟Hugging Face實作一致）、8-bit KV cache。

🧩 **先算每層多重，再決定幾片晶圓，最後只讓activation跨晶片跑**

第一步是算每一層的大小：3兆參數全部用4-bit儲存，除以93層，平均每層大約16 GB。

第二步決定每片44 GB晶圓能放幾層，答案依層的類型而不同。Dense層（全attention）需要額外空間放KV cache，因為每個dense層要為所有進行中的請求存放key跟value，所以一片晶圓只放一個dense層，其餘空間留給KV cache。Linear attention層不需要額外KV cache空間，因為它只為每個請求保留一個固定大小的state，不管context多長都一樣，所以一片晶圓可以放兩個linear層（2×16 GB=32 GB）。照Kimi K3的69個linear層跟24個dense層去算，總共需要59片晶圓（linear層部分約35片，加上24片dense層）。

第三步是把晶圓接起來。Cerebras的編譯器把模型層對應到晶圓上的區域後，runtime會規劃token在晶圓之間流動的路徑。因為只需要傳activation，用RDMA over Ethernet就能做到，每一跳大約2微秒。關鍵是：每片晶圓有44 GB晶片上SRAM，每層只要16 GB，所以多數情況下整層權重都能直接放進單片晶圓，權重本身幾乎不需要搬動，只有activation要跨晶圓傳遞。

📊 **把晶圓當成生產線，同時塞進多個不同的請求**

處理單一請求時，每片晶圓就像生產線上的一站：晶圓1跑第1到2層，把activation送給晶圓2；晶圓2跑第3到4層，再傳給晶圓3，依此類推，直到最後一片晶圓產出下一個token。

真正serve大量請求時，不會一次只送一個請求等它跑完才送下一個，那樣等於把pipeline閒置掉。做法是讓整條pipeline同時塞滿不同的請求：晶圓3在處理請求A的token時，晶圓2可能同時在處理請求B，晶圓1在處理請求C。每個stage還能一次處理一小批請求（micro-batch），所以同時在飛行中的請求數，大致是stage數乘上micro-batch大小。micro-batch越小，單一請求的延遲越低；越大，整體throughput越高，這是一個需要權衡的參數。

💡 **能同時服務多少請求，由dense層晶圓剩下的KV cache空間決定**

因為linear層不佔額外KV cache空間，真正限制同時服務請求數的，是每片已經放了一個dense層（16 GB）的44 GB晶圓，剩下能分給KV cache的空間。這個剩餘空間除以單一256k請求在8-bit KV cache下佔用的大小，就是這個配置能撐住的並行請求數上限。Cerebras也提醒，單看並行請求數或batch size都不足以判斷inference系統效率好壞，比較公平的指標是在同樣輸出速度下，每單位電力能跑出多少token（tokens per second per megawatt）。

⚠️ **這套算法可以往上長，但終究是晶片數堆出來的**

Cerebras強調，同一套方法可以套用到比3兆參數更大的模型：算出權重跟請求狀態需要的記憶體，把模型拆到晶圓上，再把晶圓接成pipeline。每多一片晶圓就多一份算力跟晶片上記憶體，讓系統能撐住超出單一晶片容量的模型。換句話說，模型規模的上限幾乎等於你願意買多少片晶圓。

🎯 **對做大模型inference的工程師，這是一份少見的「怎麼拆模型」實戰筆記**

比起單純公告支援多大的模型，這篇文章難得把「每層多大、放幾片晶圓、怎麼接、怎麼serve並行請求」的計算過程完整攤開。對於正在評估wafer-scale或其他非GPU加速方案的團隊，這套「先算層大小，再算晶圓數，再決定pipeline深度」的思路，也適用於評估自己要用多少硬體資源來撐住一個超大模型。

🔗 **來源**
- 標題：How we deploy Trillion-parameter frontier models on Cerebras
- 作者／機構：Sarah Chieng／Cerebras
- 連結：https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras

#Cerebras #WaferScaleEngine #LLMInference #TrillionParameters #KimiK3 #AIInfrastructure #ModelServing #Pipelining #AIHardware #Inference
