---
title: Which Routing Does Each MoE Model Use? DeepSeek, Qwen, Mixtral, Llama 4, gpt-oss
  Compared
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/08/moe-model-routing-comparison/
model: claude-code/sonnet
generated_at: '2026-11-08T21:19:20.640607'
score: 86
---

📌 從8到384個專家:五款主流MoE模型路由設計大比對

TL;DR:DeepSeek、Qwen、Llama 4、gpt-oss 都用MoE,但路由細節幾乎沒有一項相同。

同樣打著Mixture-of-Experts(MoE)的招牌,專家數可以從8個灌到384個,每個token啟用的專家數(top-k)可以是1,也可以是8。如果你以為「MoE模型都差不多」,直接套用別人的服務參數來部署,很可能第一步就會算錯GPU記憶體與通訊量。

🤔 **五個旋鈕,決定一個MoE模型的脾氣**

根據MarkTechPost對各模型Hugging Face設定檔(config.json)、模型卡與技術報告的整理(查證時間為2026年11月7日),目前所有列入比較的開源MoE模型都採用「token-choice routing」,也就是每個token自己挑專家,而不是反過來讓專家挑token。但在這個共同前提下,模型之間在五個關鍵欄位上分道而行:路由專家數、每token啟用數、是否有常駐的共享專家、評分函式,以及負載平衡方法。文章也特別提醒,Qwen3.6與Llama 4的公開資料並未揭露gating細節,gpt-oss與Llama 4也沒有列出負載平衡方法,這些空白在表格裡直接標記為未揭露,而非含糊帶過。

🧩 **逐個模型拆開看**

- **DeepSeek-V3**:256個路由專家,用sigmoid評分,再對選中的分數做正規化;另外用一個「per-expert bias」只影響top-8的挑選,不動實際的混合權重。專家被分成8組,路由器先保留4組,根據技術報告,每個token最多只會碰到4個節點。每個token都會額外跑一個常駐的共享專家。
- **DeepSeek-V4 Pro**:路由專家數拉高到384,但top-k從8降到6;評分函式換成sqrtsoftplus;前3層MoE改用hash routing(固定的token到專家對應表);原本的bias式noaux_tc負載平衡方法保留。
- **Qwen3(原始版)**:128個專家,每個token路由到8個。Qwen3拿掉了Qwen2.5-MoE原有的共享專家設計,改用全域批次(global-batch)的負載平衡損失。
- **Qwen3.6-35B-A3B**:路線轉向,依模型卡資料改成256個專家,8個路由加1個共享。
- **Llama 4 Maverick**:在MoE層與密集層之間交替,每個MoE層裡一個token會走1個共享專家加128個路由專家中的1個,這種top-1設計呼應了Switch Transformer的作法。即便總參數量達400B,實際啟用參數仍維持在17B。
- **gpt-oss-120b**:用線性路由器在128個專家裡取前4個,設定檔中沒有列出共享專家。它的MoE權重以MXFP4格式發佈,讓這個117B參數的模型能塞進單張80GB GPU。
- **Kimi K2**:沿用DeepseekV3ForCausalLM的架構類別與noaux_tc路由器,把路由專家數提高到384,top-k維持8。Kimi K2的報告指出,在固定啟用運算量的前提下,提高稀疏度能降低loss。
- **GLM-4.5**:選擇160個專家並堆疊更多層數,走的是「深度優先於寬度」的路線。

💡 **這些數字差異最終都會變成帳單**

每層放更多專家,代表要常駐在記憶體裡的權重更多,而且all-to-all通訊量也會增加。像DeepSeek-V4那樣調低top-k,可以直接壓低每個token的運算與通訊成本。而共享專家等於替每個token多開一條「必付」的密集路徑,不管路由結果如何都要跑。

🎯 **部署前,先把這四個欄位抄下來**

在幫任何MoE模型估算GPU用量之前,先去config.json或模型卡確認路由專家數、每token啟用數、是否有共享專家,以及評分與負載平衡方法。這四個欄位會直接決定記憶體佔用、節點間通訊模式,以及你該用多少張卡才撐得住。

🔗 **來源**
- 標題:Which Routing Does Each MoE Model Use? DeepSeek, Qwen, Mixtral, Llama 4, gpt-oss Compared
- 作者/機構:Michal Sutter(MarkTechPost)
- 連結:https://www.marktechpost.com/2026/11/08/moe-model-routing-comparison/

#MixtureOfExperts #MoE #DeepSeek #Qwen #Llama4 #gptoss #LLM #ModelArchitecture #GPUDeployment #MachineLearning
