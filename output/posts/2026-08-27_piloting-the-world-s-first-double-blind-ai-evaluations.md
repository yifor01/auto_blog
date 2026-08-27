---
title: Piloting the world's first double-blind AI evaluations
source: Google DeepMind
url: https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations/
model: claude-code/sonnet
generated_at: '2026-08-27T17:13:28.788298'
pinned: true
---

📌 Google DeepMind 首創雙盲 AI 評測，杜絕模型「先看考題」

TL;DR：DeepMind 用密碼學技術打造雙盲評測環境，防止 benchmark contamination，讓第三方評測結果真正可信。

想像一位學生要參加一場高風險考試，如果他事先偷看到考題，就算拿到滿分，這個成績也毫無意義。要真正衡量他的實力，考題必須在考試開始前對他完全保密。這正是 AI 產業評測前沿模型時面臨的難題。

🤔 **模型「看過考題」，分數就不可信**

素材指出，業界稱這個現象為「benchmark contamination」（基準污染）：如果模型在訓練過程中已經接觸過測試題目，即使評測分數再高，也無法真實反映模型能力。隨著模型能力持續提升，確保模型未曾預先看過測試題目變得至關重要，因為這會扭曲評測結果。政策制定者、研究者與企業都需要信任 AI benchmark 能真實反映模型的能力與安全性，但只要模型有機會「偷看」評測題目，分數就可能被人為墊高，進而破壞外界對評測的信任。

🧩 **用密碼學打造互不可見的雙盲環境**

DeepMind 宣布推出全球首個針對專有前沿模型的雙盲評測，並與新加坡 AI Safety Institute、OpenMined、AVERI 與 MLCommons 合作，在隱私保護環境中對 Gemini Flash Lite 模型進行機密 benchmark 測試。

素材說明，過去外部高風險評測必須在兩種風險間二選一：評測方交出測試題目（模型提供者可能因此偷看到考題），或模型提供者交出模型權重（評測方可能因此取得敏感智慧財產）。雙盲評測透過 Google Cloud Confidential Computing 底下的 Confidential Space，建立一個雙方都無法窺視對方內容的「密碼學箱子」：評測方看不到 Gemini 的模型權重，Google 也看不到評測方的測試題目，並可用密碼學方式驗證雙方資料確實維持機密。

💡 **零日誌協議之外，再加一層技術保障**

素材提到，雖然業界長期以來已用零日誌協議（zero-logging protocol）與嚴格的合約條款來維持外部測試題目的機密性，但這次導入技術與密碼學層面的保障，是安全模型評測的重要進展。這類密碼學證據有助於防止 benchmark contamination，同時保護敏感資料，對於網路安全或政府單位使用的高敏感度評測尤其重要。

🎯 **對工程師與評測機構的意義**

雙盲評測讓獨立機構得以在不犧牲資料主權與安全性的前提下，嚴格測試先進模型。DeepMind 表示希望這次試點能為模型監督建立新標竿，協助整個產業打造更安全、更可靠、更值得信賴的 AI 系統。

🔗 **來源**
- 標題：Piloting the world's first double-blind AI evaluations
- 作者／機構：Google DeepMind（William Isaac, Sol Messing, Kristian Lum）
- 連結：https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations/

#GoogleDeepMind #AIEvaluation #BenchmarkContamination #ConfidentialComputing #AISafety #Gemini #ModelEvaluation #Cryptography #MLCommons #AIGovernance
