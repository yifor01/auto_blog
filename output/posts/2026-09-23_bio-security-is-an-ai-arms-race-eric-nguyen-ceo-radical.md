---
title: 🔬Bio-security is an AI Arms Race - Eric Nguyen (CEO, Radical Numerics)
source: Latent Space
url: https://www.latent.space/p/bio-security-is-an-ai-arms-race-eric
model: claude-code/sonnet
generated_at: '2026-09-23T20:36:24.431758'
score: 95
---

📌 當 AI 能寫出整個病毒基因組，生物安全防線該怎麼補

TL;DR：Radical Numerics 執行長 Eric Nguyen 談基因語言模型如何同時提升生物風險與防禦能力。

OpenAI 到 Hugging Face 的攻擊事件讓人開始問：下一個風險領域在哪裡？Anthropic 的過濾機制點名了兩件事——資安與生物安全。Latent Space 這集訪談找來曾參與 Evo、Evo 2 開發的 Eric Nguyen，談的正是生物安全這條戰線。

🤔 從「沒人相信會有用」到生成完整病毒基因組

Eric 在史丹佛時期推動基因語言模型（Genomic Language Models, GLMs）長期得不到迴響：生物學家不相信這套方法可行，不確定該如何驗證輸出，也看不出比現有方法更重要的應用。他持續推進，最終協助在 Arc Institute 主導 Evo 與 Evo 2 的開發。根據訪談內容，這兩個模型後來被另一組 Arc／史丹佛團隊用來生成完整的噬菌體基因組，並合成為具功能性的病毒。

🧩 DNA 語言的特殊之處：字母表小、序列極長

早期 ChatGPT 生成詩與郵件，早期的 DNA 語言模型 Evo 與 Evo-2 則能從零建構一段基因組。DNA 和自然語言的差異在於字母表極小（僅 ACTG 四個字元），但序列長度驚人——整個人類基因組約 30 億長。訪談指出，長上下文模型的技術進展（註腳提到 striped hyena 架構）大約在三年前才讓這件事成為可能，時間點甚至早於前沿實驗室開始建構百萬級上下文模型。

Eric 與包括 Michael Poli（首席 AI 科學家，曾任 Liquid AI 創始科學家）、Stefano Massaroli（總裁，曾與 Yoshua Bengio 做博後研究、Liquid AI 創始團隊成員）、Armin W. Thomas（技術長，曾在史丹佛與 Chris Ré 合作、曾任職 Liquid AI）等人共同創立了 Radical Numerics，目標是擴大 GLM 的規模，處理遠超出「生成 DNA」的廣泛生物問題。

💡 模型在 DNA 序列中展現的「思維鏈」

由於 DNA 序列中已包含基因的清楚標記，而特定基因又編碼蛋白質，這些 GLM 在 RNA 與蛋白質上的表現也不錯——代表模型在還沒針對 3D 蛋白質結構、表觀遺傳學、自然語言等其他模態訓練之前，就已經能泛化到多種「語言」。

訪談中描述了一個實驗：研究團隊拿一組 aptamer（適體）資料集，保留其中表現最好的一部分不給模型看，只展示分數較低、依序遞增的序列，然後要求模型延續這個趨勢。結果模型能夠重現部分先前未曾展示過的高分序列——換句話說，這是在 DNA 語言中出現的思維鏈（chain-of-thought）現象。

⚠️ 防禦正在落後，但團隊選擇往前衝

訪談指出，正如長上下文推論、思維鏈與多模態感知解鎖了自然語言 LLM 的複雜推理能力，這些能力在 GLM 上同樣正在催生愈趨複雜的「生物智慧」，隨之而來的風險也在提高。Eric 表示，防禦端目前正在輸掉這場競賽，但 Radical Numerics 的立場是應該把前沿能力推得更快——這與 Hugging Face 的 Clem Delangue 主張資安防禦能力應保持開放、跟上前沿模型攻擊能力的邏輯類似。

🎯 實務啟示

對於關注 AI 安全與生物資訊交界的工程師與研究者而言，這集訪談呈現了一個值得留意的訊號：長上下文架構帶來的能力躍升，正從自然語言模型複製到基因語言模型上，而這個領域的攻防態勢遠比多數人想像的更早成形。完整討論還包括基因組作為「環境在 DNA 上留下的印記」這個框架，值得對照原始訪談收聽。

🔗 來源
- 標題：🔬Bio-security is an AI Arms Race - Eric Nguyen (CEO, Radical Numerics)
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/bio-security-is-an-ai-arms-race-eric

#BioSecurity #GenomicLanguageModels #AIatBio #Evo2 #RadicalNumerics #ArcInstitute #ChainOfThought #LongContext #AIRisk #Biotech
