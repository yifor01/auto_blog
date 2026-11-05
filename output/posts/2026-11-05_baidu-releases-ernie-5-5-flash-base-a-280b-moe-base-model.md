---
title: 'Baidu Releases ERNIE 5.5 Flash Base: A 280B MoE Base Model With 14B Active
  Parameters'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/05/baidu-ernie-5-5-flash-base-280b-moe/
model: claude-code/sonnet
generated_at: '2026-11-05T23:05:25.902171'
score: 93
---

📌 百度開源280B MoE基礎模型：文心5.5 Flash Base

TL;DR：百度公開最新MoE基礎模型的純pre-training checkpoint，附完整評測數據與部署方案。

一個號稱280B參數的大模型，官方公布的六項基準測試卻輸給對手，這不是失敗的發布，而是刻意的設計選擇——因為這是一個「什麼都還沒調過」的乾淨起點。

🤔 **為什麼要發乾淨的base model**

Baidu發布的ERNIE 5.5 Flash Base是其新一代sparse Mixture-of-Experts（MoE）語言模型的原始pre-training checkpoint。這個模型權重只停留在pre-training結束的狀態，沒有經過任何mid-training或post-training（例如instruction tuning、RLHF）的加工。對於想要比較不同fine-tuning、instruction tuning或RL方法效果的團隊來說，從同一個起點出發，才能做出公平的對照實驗。

🧩 **架構與訓練規模**

ERNIE 5.5 Flash Base是純文字（text-only）的MoE基礎模型，總參數280B，每個token只啟動14B參數，共43層、hidden size為4096。模型從零開始以33.5T tokens進行pre-training，使用Muon最佳化器。Tokenizer共有201,216個詞條，數字編碼方式是「從右到左、每3位數分一組」。

值得注意的是，Baidu團隊在訓練階段把「啟動運算量」、「KV cache」與「長文本成本」視為同一個整體預算來做取捨，而不是分開最佳化。這也反映在pre-training資料的選擇上：資料大量納入repository等級的程式碼與長文本材料，原因是這類資料事後很難補進去。

📊 **四模型同框評測，輸了六項**

Baidu團隊用同一套評測pipeline、相同prompt與few-shot設定，對四個base model做比較評測（以下數據皆為Baidu自行量測與公布）。ERNIE 5.5 Flash Base在六個任務上輸給對手：DeepSeek-V4-Flash-Base在ChineseSimpleQA、INCLUDE-lite、HELMET-Rerank與InfiniteBench上領先；Hy3-preview-Base則在BBH CoT與FullStackBench上領先。

有趣的是，Baidu量測出的競品分數和各家官方自己公布的數字並不完全一致：DeepSeek官方公布MMLU-Pro為68.3，Baidu量到69.2；Tencent官方公布Hy3的MMLU-Pro為65.76，Baidu量到66.9。這種評測pipeline差異提醒工程師，跨實驗室的benchmark數字不能直接並排比較，要留意評測harness本身的影響。

💡 **部署細節：完整支援SGLang與vLLM**

模型權重已上架Hugging Face與ModelScope，提供FP8與BF16兩種格式。官方文件說明可用SGLang（範例指令使用`--tp 4`）或vLLM（需0.32.0版本加上vLLM-ERNIE plugin）進行serving，兩種伺服器都支援最長1,048,576 tokens的輸入。由於這是一個base model，必須透過completions端點呼叫，而非chat端點。

訓練端則採用Baidu自研的FlashMask-4 kernel，支援SM90與SM100架構GPU。根據Baidu團隊公布的數據，在SM100上，FlashMask-4比FlashAttention-4 MaskMod的forward運算快上175%、backward運算快74%。

⚠️ **這次公開的是checkpoint，不是突破**

這次發布的重點並非架構上的全新突破，而是把一個完整訓練好的大型MoE base model乾淨地公開出來，連同VHA、Multi-Router MoE與ECHO等相關技術論文一併釋出。對研究社群而言，價值在於「可比較性」：有了同一個未經任何後訓練加工的起點，才能更公平地評估各種fine-tuning或對齊方法的實際效果。

🎯 **對工程師的意義**

如果你的團隊正在比較不同的instruction tuning或RL alignment方法，ERNIE 5.5 Flash Base提供了一個難得的乾淨基準：同一套底層能力，排除了「別人的post-training手法干擾結果」的變數。部署面也相對友善，SGLang與vLLM的serving路徑都已有官方範例可直接參考。

🔗 **來源**
- 標題：Baidu Releases ERNIE 5.5 Flash Base: A 280B MoE Base Model With 14B Active Parameters
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/05/baidu-ernie-5-5-flash-base-280b-moe/

#ERNIE #Baidu #MoE #LLM #BaseModel #MachineLearning #OpenWeights #vLLM #SGLang #AIInfrastructure
