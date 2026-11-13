---
title: 'Perplexity Releases Decider v1.3: Open-Weight Decision Models Add Locate'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/13/perplexity-decider-v1-3-open-weight-decision-models-locate/
model: claude-code/sonnet
generated_at: '2026-11-13T22:54:45.735380'
score: 83
---

📌 Perplexity Decider v1.3：決策模型不生成文字，只回傳機率

TL;DR：Perplexity 推出開放權重決策模型新版，新增 Locate 文字定位功能，Apache 2.0 授權開放下載。

多數 LLM 的賣點是「寫得多好」，但 Perplexity 的 Decider 系列反過來做：它不寫答案，只針對 yes/no、多選、評分這類問題回傳每個選項的機率。v1.3 更進一步，讓它能從一段文字裡「挖」出確切的片段位置。

🤔 **把分類任務直接變成機率輸出，省掉生成再解析這一步**

分類、路由、評分這類任務常見的痛點，是硬用生成式 LLM 做反而要先生成文字、再解析出結構化結果，多繞一圈也多一層出錯機會。Decider 的設計理念是把任務改寫成「共享的 state + 一個或多個帶標籤選項的問題」，模型直接輸出每個選項的機率，而不是寫一句話當答案。

🧩 **分類頭 + 雙向 attention + 新的 inter-question attention 規則**

Perplexity 把一個生成式 LLM backbone 改造成分類器：輸出層從 base model 的 LM head 剪裁，只保留選項 token（A、B、C）；一個 linear decision head 讀取 <|marker|> token 的 hidden state，輸出各選項機率；原本的 full-attention layer 被改成雙向，Perplexity 的 ablation 顯示這樣效果更好。

v1.3 另一個關鍵改動是問題之間的 attention 規則。v1.2 時每個問題能看到其他所有問題，結果同一批問題放在一起問，答案會互相影響；v1.3 改成只有 state 能看到全部問題，每個問題只能看到 state 跟自己，但同一個輸入的所有問題仍在同一次 forward pass 裡算完。最終權重是在 3 個 random seed 上取平均。Flash 版本則是用 KL divergence 最小化的方式，從大模型蒸餾出來的。

新功能 Locate 用來抓文字片段的起訖字元位置，欄位可以是短標籤（像「location」）也可以是一句指令（像「抽取出工作地點的城市名稱」），主要瞄準 NER、PII 偵測跟抽取式 QA。做法是每個被要求的欄位都新增一個 <|locate|> token，另外訓練一個 span head 加上 LoRA adapter，backbone 和原本的 decision head 全部凍結不動。值得注意的是，這個 adapter 並沒有被 merge 回主模型，因為 Perplexity 發現 merge 會傷害原本的 decision 準確度。

📊 **價格與延遲：Flash 版本快了 3 倍，output token 不收費**

根據 Perplexity 自報的數字：API 端點為 POST https://api.perplexity.ai/v1/decisions，model ID 為 pplx-decider-v1.3 與 pplx-decider-flash-v1.3（皆提供 -latest alias）；輸入計價為每百萬 token 0.02 美元（v1.3）與 0.01 美元（Flash），輸出不計費。延遲測試中，一個約 243K token 的請求在 v1.3 上耗時 16 秒，Flash 版本只要 5 秒。Locate 單次請求最多支援 128 個 questions。

⚠️ **這是分類器，不是生成模型**

以上 benchmark 數字均為 Perplexity 自行公布，尚無第三方驗證。另外 Decider 系列本質是專用的 classifier / extractor，不適合拿來取代一般需要生成自然語言回應的場景。

🎯 **適合拿來做路由、審核、PII 抽取這類判斷題**

如果你的系統只需要做分類路由、內容審核評分，或是需要抽取特定文字片段（像 PII redaction、NER、抽取式 QA），這類 decision model 可以取代「硬用生成式 LLM 做完再解析」的繞路做法，省下延遲與 token 成本。本地部署可用 pplx_decider 套件的 Decider.from_pretrained() 載入，記得 full-attention layer 必須以 noncausal 方式執行；Perplexity 建議精細 rubric 用 v1.3，高流量路由場景用 Flash。

🔗 來源
- 標題：Perplexity Releases Decider v1.3: Open-Weight Decision Models Add Locate
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/13/perplexity-decider-v1-3-open-weight-decision-models-locate/

#Perplexity #OpenWeightModels #DecisionModel #MachineLearning #NER #PIIDetection #LLM #Classification #ApacheLicense #AIInference
