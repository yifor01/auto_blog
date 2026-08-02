---
title: GLM-5.2 is probably the most powerful text-only open weights LLM
source: Simon Willison
url: https://simonwillison.net/2026/Jun/17/glm-52/
score: 88
model: google/gemma-4-31b-it:free
generated_at: '2026-06-26T20:07:41.954210'
---

📌 753B 參數且 MIT 開源：GLM-5.2 挑戰最強純文字開源模型

TL;DR：Z.ai 開源 GLM-5.2，提供 753B 參數規模、1M token 上下文且採用 MIT 授權。

當大多數開源模型在參數規模與授權條款之間權衡時，Z.ai 直接釋出了一個 1.51TB 的「巨獸」，且採取最寬鬆的 MIT 授權。這讓開發者能直接獲取一個具備極大規模參數且支援超長上下文的純文字模型。

🧩 **753B 參數規模與 MoE 架構**

GLM-5.2 在規模上延續了先前 GLM-5 與 GLM-5.1 的設計，是一個擁有 753B 參數、總體積達 1.51TB 的大型模型。為了在運算效能與規模間取得平衡，該模型採用了 Mixture of Experts (MoE) 架構，每次推論僅需 40B 個 active parameters。

💡 **從 20 萬擴展至 100 萬 token 上下文**

相較於前代 GLM-5.1 僅支援 200,000 token 的上下文視窗，GLM-5.2 將其大幅提升至 1 million (1M) token。這意味著模型能處理更長的檔案或更複雜的上下文資訊，顯著提升了處理長文本的能力。

⚠️ **純文字輸入限制與版本區分**

需要注意的是，GLM-5.2 是一個純文字輸入 (text-only) 的模型。雖然 Z.ai 擁有視覺模型系列（如 GLM-5V-Turbo），但該視覺系列並不包含在這次的開源權重之列。

🎯 **實務啟示**

對於需要部署超大規模模型且對授權有嚴格要求的工程師來說，MIT 授權提供了極高的自由度。然而，1.51TB 的模型體積對硬體記憶體的需求極高，實作時需重點評估基礎設施是否能承載如此巨大的權重檔案。

🔗 **來源**
- 標題：GLM-5.2 is probably the most powerful text-only open weights LLM
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Jun/17/glm-52/

#LLM #OpenWeights #GLM52 #Zai #MoE #MITLicense #LargeLanguageModel #ContextWindow #MachineLearning #AI
