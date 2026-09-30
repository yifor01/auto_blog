---
title: Introducing SynthID Bio
source: Google DeepMind
url: https://deepmind.google/blog/introducing-synthid-bio/
model: claude-code/sonnet
generated_at: '2026-09-30T21:33:57.243047'
pinned: true
---

📌 【Google DeepMind 官方發布】幫 AI 設計的蛋白質打上浮水印，功能不受影響

TL;DR：SynthID Bio 讓 AI 生成的蛋白質序列與結構帶上可驗證浮水印，生物功能維持不變。

AI 已經能設計出資料庫裡從未出現過的全新蛋白質序列，這本是好事，但也意味著傳統的 DNA 合成篩檢再也無法單靠「這序列看起來眼熟」來判斷風險。Google DeepMind 這次要解決的，正是「怎麼證明一段生物設計是不是 AI 做出來的」這個問題。

🤔 **AI 設計的生物序列，正在讓篩檢與資料庫失靈**

素材指出，生成式 AI 已被用於預測蛋白質結構（AlphaFold）、設計全新蛋白質（AlphaProteo、ProteinMPNN），乃至近期開發新的噬菌體。但這也帶來兩個具體問題：AI 設計的新穎序列可能繞過既有的 DNA 合成篩檢資料庫比對；而被錯誤標記的合成 3D 結構，一旦混入公開資料庫，可能誤導後續研究，甚至影響生物安全的判斷。

🧩 **依資料型態調整策略：序列微調胺基酸，結構微調原子座標**

SynthID Bio 是一套專門為合成生物學設計的浮水印方法家族。針對蛋白質序列，它會細膩地引導胺基酸的選擇；針對預測出的 3D 結構，則調整原子座標，藉此產生可供偵測的訊號。研究團隊用自家的結合體設計方法 AlphaProteo，搭配內建 SynthID Bio 的 ProteinMPNN（常用的蛋白質序列生成方法），驗證了這套做法在「蛋白質結合體（binder）」上的可行性。在結構預測方面，SynthID Bio 則是微調 AlphaFold 3 擴散網路的一小部分，把浮水印能力直接內建進模型權重，讓任何人執行該模型產生的 3D 座標都天生帶有可偵測的訊號。

📊 **濕實驗室測試：加了浮水印，結合力與命中率沒有打折**

團隊針對三個目標蛋白（VEGF-A、SARS-CoV-2 spike RBD、PD-L1）進行濕實驗室測試，結果顯示帶浮水印的設計在命中率、結合親和力（以 KD 值衡量）與天然序列多樣性上，都與未加浮水印的版本相當，成功做出史上第一批「帶浮水印且具生物功能」的蛋白質結合體。在結構預測這一側，SynthID Bio 同樣維持了 AlphaFold 3 的預測準確度，同時提供近乎完美的可偵測性，並在關鍵結構特徵分布與面對數位雜訊、微小座標變動時都保有穩健性。

團隊也與史丹佛大學 Hie 實驗室及 Arc Institute 合作，把 SynthID Bio 整合進進階基因體模型 Evo 2，為 Evo 2 設計的噬菌體基因體打上浮水印；早期在細菌培養中的實驗室測試證實，這些帶浮水印的噬菌體仍具備功能，團隊表示後續會發布技術手稿分享更多細節。

💡 **生物安全的「瑞士乳酪」防禦模型多了一層**

文中把生物安全比喻為「瑞士乳酪」式的多層防禦，每一層安全措施都可能有漏洞，需要彼此互補。SynthID Bio 被定位為嵌入生物設計本身的驗證層，尤其對站在生物安全第一線的 DNA 合成篩檢特別關鍵：過去看到陌生序列，篩檢單位可能假設它是尚未被發現的天然生物；但現在 AI 能設計出與已知威脅幾乎不相似的全新序列，這個假設已不再成立，人工逐一審核又可能拖慢重要研究。SynthID Bio 可以提供自動化的驗證訊號，證明某筆訂單源自於內建安全機制的可信模型。生物安全政策專家 Sarah Carter 評論這是「追蹤生物設計來源拼圖中的重要一塊」；Twist Bioscience 政策與生物安全副總裁 James Diggans 則表示浮水印為篩檢工具箱帶來新選項，有助於把資源集中在真正需要仔細審查的序列上。此外，這套機制也有機會協助 Protein Data Bank、UniProt、GenBank 等開放提交的公開資料庫，在收件時標記或篩出合成項目，避免污染資料庫。

⚠️ **抗竄改能力還在路上，不是萬靈丹**

Google DeepMind 也坦言，SynthID Bio 目前只是邁向「可靠識別與追蹤 AI 生成生物序列與結構」的第一步，接下來的關鍵挑戰包括讓浮水印更能抵禦刻意竄改，未來也可能搭配類似 C2PA 的來源中繼資料機制，或集中式的 AI 生成生物資料儲存庫來加強追蹤。團隊強調沒有任何單一的生物安全介入手段是萬靈丹，真正落地仍需要跨生物安全、基因合成與政策領域的社群協作。目前團隊已發表方法論文，並開源程式碼與體外（in vitro）資料，同時將權重釋出給研究社群。

🎯 **實務啟示**

對做蛋白質設計或基因體模型的研究團隊來說，這代表未來合成生物流程中，「模型輸出是否可驗證來源」可能會逐漸變成篩檢與資料庫收錄的標準環節；也值得留意 SynthID Bio 開源的程式碼與模型權重，評估是否能整合進自家的設計與篩檢流程中。

🔗 **來源**
- 標題：Introducing SynthID Bio
- 作者／機構：Pushmeet Kohli, David Stutz, Ali Cowen-Rivers, Jeremy Ratcliff（Google DeepMind）
- 連結：https://deepmind.google/blog/introducing-synthid-bio/

#GoogleDeepMind #SynthIDBio #Biosecurity #AlphaFold #ProteinDesign #SyntheticBiology #AIWatermarking #AlphaProteo #GenomicAI #ResponsibleAI
