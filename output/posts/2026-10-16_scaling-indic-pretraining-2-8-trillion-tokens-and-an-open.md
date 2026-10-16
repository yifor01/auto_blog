---
title: 'Scaling Indic Pretraining: 2.8 Trillion Tokens and an Open Data Generation
  Pipeline'
source: HuggingFace Blog
url: https://huggingface.co/blog/nvidia/scaling-indic-pretraining
model: claude-code/sonnet
generated_at: '2026-10-16T20:15:08.412755'
score: 84
---

📌 NVIDIA與IIT Madras開源2.8兆Tokens印度語語料

TL;DR：NVIDIA攜手AI4Bharat開源22種印度語言、2.8兆tokens的訓練語料，外加可重複使用的GPU資料生成管線。

印度有22種憲法認可的語言，涵蓋全國97%人口，將近12億人。但這些語言的AI技術長期落後英語，AI4Bharat負責人Mitesh Khapra點出的原因很直白：「我們沒有足夠的印度語言資料。」NVIDIA與IIT Madras旗下的AI4Bharat實驗室這次給出的回應，是一次性釋出2.8兆tokens的語料，以及產生這批語料的完整管線。

🤔 **印度語言資料為何總是不夠**

Naive RAG 時代的英語世界有海量網路文本、程式碼與數學語料可用於預訓練，但印度語言缺乏對應規模的資料。AI4Bharat此前推出的Sangraha語料庫雖已為開源印度語言模型研究打下基礎，但要支援技術解釋、推理與問答等能力，仍需要把英語世界豐富的數學、程式碼、問答內容轉譯進印度語言體系。這正是Nemotron-pretraining-Indic-v1要補上的缺口。

🧩 **四階段管線：翻譯、評分、修補、羅馬化**

這批語料源自15個Nemotron-CC-v2子集，涵蓋網路文本、問答素材、數學與程式碼。團隊使用NVIDIA開源的NeMo Data Designer框架，搭配Gemma-4-31B-it模型執行以下流程：

1. 翻譯：針對12種雙文字語言，完整翻譯整份文件以保留段落、表格與公式間的上下文，並用prompt明確區分「要翻譯的散文」與「要保留原樣的內容」（程式碼、公式、URL、格式）。
2. 品質評估：用同一模型，依據參考MQM（Multidimensional Quality Metrics）框架的評分表，從語意、流暢度、術語、風格、格式五個面向打分，滿分100分，只保留75分以上的輸出。
3. 修補：分數不足的輸出會依評估回饋進行修正，再重新評分，此流程額外挽回了4384億tokens。
4. 羅馬化：先產出的原生文字翻譯再轉換為拉丁字母，並與原生文字版本互相比對。團隊在人工比較中發現，這種「先翻譯再轉寫」的兩步驟做法，比直接從英語生成羅馬化文字產生更少的幻覺內容與殘留英語。

其餘10種只有原生文字、沒有雙文字支援的語言，則採用另一套「Indic Translate」工作流，用以處理長文件品質與文字穩定性問題。

📊 **語料組成：2601億原生文字tokens + 2246億羅馬化tokens**

以Gemma-4 tokenizer計算，語料包含2,601.0億原生文字tokens與224.6億羅馬化tokens，涵蓋34種語言文字組合：
- 原生文字＋羅馬化皆有：孟加拉語、古吉拉特語、印地語、坎納達語、馬拉雅拉姆語、馬拉提語、尼泊爾語、奧裡亞語、旁遮普語、坦米爾語、泰盧固語、烏爾都語（共12種）
- 僅原生文字：阿薩姆語、博多語、多格里語、喀什米爾語、孔卡尼語、邁蒂利語、曼尼普爾語、梵語、桑塔利語、信德語（共10種）

需注意的是，文件紀錄包含同一份原始文件的多個翻譯與文字版本，並非獨立英語文件的計數；token數字也反映「保留下來的語料規模」，而非某次訓練實際用掉的token預算，兩者需分開解讀。

💡 **可追溯來源，是開放資料真正能用的關鍵**

整套流程始終保留每筆資料的來源識別碼，使得任何一筆輸出都能回溯到原始英語文件。團隊也透過人工抽樣審查與刻意植入錯誤的測試，找出遺漏與殘留英語問題，持續修正prompt與檢查機制。這種可追溯性,讓合成資料不只是「看起來像」印度語言文本,而是有憑有據。NVIDIA也強調,這批合成資料是用來補強、而非取代自然書寫的印度語文本,後者對在地知識與文化脈絡仍不可或缺。據悉Nemotron 3.5 Super VL的持續預訓練已從12種語言子集中抽取100億Indic tokens使用。

🎯 **實務啟示**

這次釋出的價值不只在語料本身，而是連同prompt、LLM工作流程與品質檢查機制一併開源。想做印度語言模型的團隊，可以直接套用語料，也可以把管線接到自己的來源文件上，依樣畫葫蘆產生客製化資料。對於資源有限、無法自建大規模翻譯評分系統的團隊而言，這是一條現成可複製的路徑。

🔗 **來源**
- 標題：Scaling Indic Pretraining: 2.8 Trillion Tokens and an Open Data Generation Pipeline
- 作者／機構：NVIDIA與AI4Bharat（IIT Madras）
- 連結：https://huggingface.co/blog/nvidia/scaling-indic-pretraining

#NVIDIA #AI4Bharat #IndicNLP #LLMPretraining #OpenDataset #SyntheticData #NeMo #LowResourceLanguages #MachineTranslation #DataPipeline
