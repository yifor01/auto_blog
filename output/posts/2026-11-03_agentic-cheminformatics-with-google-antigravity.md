---
title: Agentic cheminformatics with Google Antigravity
source: Google DeepMind
url: https://deepmind.google/blog/agentic-cheminformatics-with-google-antigravity/
model: claude-code/sonnet
generated_at: '2026-11-03T22:26:21.591620'
pinned: true
---

📌 【Google DeepMind 官方發布】用 AI Agent 跑完整套新藥設計工作流，只要一小時

TL;DR：Google Antigravity 搭配新推出的 Cheminformatics Skills，讓 agent 自動完成文獻檢索、分子分析到候選藥物設計。

藥物設計有一個反直覺的瓶頸：真正卡住研發的往往不是化學直覺,而是「資料整理」。一顆分子可能在論文裡是 IUPAC 命名、在專利裡是 Markush 結構、在供應商目錄裡又變成一個 SDF 檔，稍有不慎改錯一個原子或鍵結,整個分子就變成另一種化合物。Google DeepMind 這次展示的,正是如何用 agent 把這段繁瑣的資料工作自動化。

🤔 **化學是最豐富卻最難統一的公開資料**

摘要指出,化學資訊橫跨數百萬筆結構,散落在期刊論文與供應商目錄中,是連結物理、數學與生命科學的共通語言。但分子的表示方式太多元,傳統 cheminformatics 系統必須同時處理這些來源的格式差異與潛在錯誤,而這個任務「沒有犯錯空間」。

🧩 **語言模型做決策,確定性工具做計算**

Google DeepMind 為 Google Antigravity 打造了一套 Cheminformatics Skills,把這個介面變成計算化學家與實驗化學家共用的協作工作臺。這套 skills 的設計理念是分工:底層語言模型負責工作流編排、資料庫導航與科學推理,而確定性的化學工具負責實際的分子計算。整套系統奠基於 RDKit(由全球社群開發二十年的開源 cheminformatics 工具),並串接 ChEMBL 與 PubChem 等策展資料庫,把領域最佳實踐直接寫進 agent 的工作流程裡。

📊 **案例:讓分子變「硬」來提升藥效**

文中以「rigidification(剛性化)」這個經典藥物化學技巧做示範。許多藥物分子透過可旋轉鍵連接多個次結構,使其在溶液中可以扭轉成多種構型(conformation),這種「軟」分子要結合目標蛋白時會付出熵的代價,削弱結合力與藥效。化學家的解法是在分子上新增一個鍵,把兩個次結構鎖在正確的形狀上。

素材以第一代 TKI 藥物 crizotinib(五個主要可旋轉鍵)與第三代藥物 lorlatinib(末端環化、可旋轉鍵數降為零、藥效提升)為對照案例。Google DeepMind 讓 agent 搜尋文獻中這兩種藥物及其類似物,agent 在幾分鐘內檢索出數千個化合物,過濾掉緩衝液、溶劑等無關分子,並在報告中標註來源。報告也指出,這批巨環化合物(macrocycle)大多預測具有腦穿透性,這點對於容易轉移至腦部的肺癌治療特別重要。

agent 接著啟動互動式檢視器,讓科學家瀏覽每一個檢索到的化合物、點擊查看 metadata,並自訂散佈圖。例如把藥效對應可旋轉鍵數畫圖、以是否為巨環上色,立刻能看出 lorlatinib 這類巨環分子可旋轉鍵較少、藥效較高。

💡 **從配對分析到機器學習建模**

agent 自主建議進行 matched molecular pair analysis(MMPA),這是一種藥物化學技巧,透過比較僅有單一變化的分子配對,來獨立分離出該變化的效應。分析結果顯示,環化會減少可旋轉鍵數並普遍提升藥效,與預期一致。

agent 也使用不同特徵集與模型架構,針對四種實驗讀出值建構並比對多個藥效預測模型,並以 scaffold split 評估 out-of-distribution 表現。Skills 內建了建模的最佳實踐指引,例如在有時間資訊時優先使用 chronological split(用舊化合物預測新化合物),否則退回 scaffold split 來更準確估計泛化能力。

最後,agent 依據學習結果提出多個改良版巨環分子的設計方案,並建議對應的反應與合成路線,還能把這些化合物準備好交給 AlphaFold 或分子動力學模擬做進一步分析。Skills 也賦予 agent 操作與驗證反應、產生電子推移箭頭圖、以及查詢公開資料庫中相似反應的能力。

🎯 **實務啟示**

這個案例示範了一種「人機協作」的 agentic 工作模式:語言模型處理推理與編排,確定性工具保證計算正確性,科學家則保留在互動檢視器中隨時介入、驗證與迭代的空間。對於需要處理大量異質科學文獻與資料格式的團隊,這種分工方式值得參考。

🔗 **來源**
- 標題:Agentic cheminformatics with Google Antigravity
- 作者/機構:Zoi Tsangalidou, Ruijie (Kelly) Zhang, Sukhdeep Singh, Michael V. LeVine @ Google DeepMind
- 連結:https://deepmind.google/blog/agentic-cheminformatics-with-google-antigravity/

#Cheminformatics #DrugDiscovery #GoogleDeepMind #AIAgent #RDKit #MachineLearning #MolecularDesign #LLM #ComputationalChemistry #AntigravityAI
