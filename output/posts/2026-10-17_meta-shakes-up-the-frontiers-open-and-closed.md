---
title: Meta shakes up the frontiers, open and closed
source: Interconnects
url: https://www.interconnects.ai/p/meta-shakes-up-the-frontiers-open
model: claude-code/sonnet
generated_at: '2026-10-17T19:35:05.718625'
score: 90
---

📌 Meta 開放權重模型反攻，美中差距一夜砍半

TL;DR：Meta 發布 816B 參數的 Muse Spark Open，暫居美國最強開放權重模型，但授權條款埋了不少坑。

如果你這幾個月持續關注開放權重模型排行榜，應該會注意到一個奇怪的現象：榜單前二十名幾乎被中國團隊包辦。這個局面在本週出現轉折，Meta 一口氣丟出開放與封閉兩條產品線的新模型，把美系陣營從「幾乎無關」拉回「落後但有存在感」。

🤔 **美國開放模型一直在吃土**

在 Muse Spark Open 出現之前，若拿掉 Meta 與新創 Reflection 的模型，市面上會有 20 多個中國團隊發布的開放權重模型效能優於最好的西方模型。這不是單一指標的落差，而是整條戰線的全面劣勢。Mistral 同期宣布了 Mistral Large 4，在 Artificial Analysis Intelligence Index 拿到 38 分的高分，但權重尚未公開，暫時無法下場比拼。

🧩 **816B 參數、1M context，但授權很「Meta」**

根據 Hugging Face 上的模型卡，Muse Spark Open 是一個 816B 總參數、42B 啟用參數的 MoE 模型，支援 1M token 的 context window，主打程式撰寫與 agentic 任務，且原生支援多模態。模型卡特別強調，這個開放版本經過額外的安全性後訓練（safety post-training），目的是讓它在沒有系統層防護的情況下獨立使用時更難被濫用；官方建議還是要搭配額外的 guardrail 部署在更大的 AI 系統中。

有觀察者一度認為這個模型是在安全調校過程中被「調壞」了，因為它是在 Muse Spark 1.3 之後才發布。但從 Artificial Analysis Index 的分數落差（約只掉 1 分）來看，更可能的情況是：這其實是 Muse Spark 1.2 的安全加固版。這也與 Meta 先前發布 30B agentic 模型 Muse Glimmer 時，Alex Wang 曾透露「準備把 Muse Spark 1.2 以開放權重形式發布」的說法互相印證。

效能上，Muse Spark Open 落在 GLM 5.2 之上、接近 DeepSeek V4.1 Flash，但仍落後 GLM 5.3 與 Kimi K3。用一句話形容：不是最強，但「夠用」，剛好卡進目前 agentic 應用快速擴張的需求帶。

⚠️ **真正的門檻不是技術，是授權條款**

Muse Spark Open 的客製授權幾乎把過去幾年開放模型社群批評過的限制全部集合在一起：
- 用這個模型做產品，必須在產品上標示「Built with Muse」（Llama 和 Kimi 都做過類似要求，但幾乎沒人真的遵守）。
- 設有營收門檻：公司整體月營收超過 2000 萬美元，就必須另簽授權，這是為了鋪陳未來的推理轉售分潤機制。
- 要求使用者同意一份可接受使用政策（acceptable use policy），這讓它在嚴格定義下完全稱不上「open source」。
- 上述限制同樣適用於模型輸出與衍生作品，因此拿它產生的合成資料（synthetic data）是否能安全使用，存在法律灰色地帶。
- 授權允許將模型用於內部研究與應用。

這套授權目前法律效力未經檢驗,許多開發者大概會選擇性忽視,Meta 也可能只會針對明顯惡意的違規出手。但對一個想重新搶市佔的實驗室而言,用複雜、非標準的授權條款自我設限,其實是不必要的策略風險。

💡 **封閉模型線也同步亮劍**

就在 Muse Spark Open 發布前幾天，Meta 也公開了封閉的前沿模型 Muse Wonder 與 Muse Wonder Full，傳統 benchmark 上僅次於 Anthropic 的 Opus 5.5，與 OpenAI 的 GPT-6-Astra、Google 的 Gemini-4-Argon 相近。這距離 Zuckerberg 發表引發爭議的「Personal Superintelligence」文章剛好滿一年。Meta 如今是唯一同時擁有前沿開放與封閉模型的美國公司，Alibaba 的 Qwen 走的是類似但更偏開放的路線。Alex Wang 治下的團隊採用高度扁平的組織（200 多個直屬報告），被視為是持續產出穩定模型迭代的關鍵之一。

🎯 **實務啟示**

對選型的工程團隊來說，Muse Spark Open 的效能定位意味著它適合作為「先頂上」的美系選項，尤其是對授權合規要求嚴格、但又想避開中國模型地緣政治爭議的企業。但部署前務必讀懂授權條款，尤其是營收門檻與合成資料的灰色地帶，這會直接影響你能不能放心把它用在商業產品鏈上。

🔗 **來源**
- 標題：Meta shakes up the frontiers, open and closed
- 作者／機構：Nathan Lambert, Interconnects
- 連結：https://www.interconnects.ai/p/meta-shakes-up-the-frontiers-open

#Meta #OpenWeights #LLM #AIModels #OpenSourceAI #FrontierAI #MuseSparkOpen #AICompetition #MachineLearning #TechIndustry
