---
title: 'From spectrum to structure: Identifying molecules with Mass Spec Skills for
  Google Antigravity'
source: Google DeepMind
url: https://deepmind.google/blog/interpreting-mass-spectra-with-google-antigravity/
model: gpt-6.1-terra
generated_at: '2026-11-28T05:50:04.647728'
pinned: true
---

📌 從質譜碎片推斷分子結構

TL;DR：Google DeepMind 結合 AI 推理與質譜工具，協助科學家提出可供審查的分子結構。

🎣 一份樣本可以產生數千筆質譜訊號，但查詢現有參考光譜庫，平均只能註解約 5% 的測得光譜；人類樣本約為 10%。

問題不一定是這些分子從未被收錄：有些已存在於化學資料庫，只是缺少可供比對的參考光譜。Google DeepMind 的 Mass Spec Skills 嘗試把分析化學家的逐步判讀流程串起來，從碎片訊號推斷候選結構。

🤔 **量到分子碎片，不代表知道分子結構**

串聯質譜（tandem mass spectrometry，MS/MS）會量測帶電分子的質量，以及它碎裂後產生的離子。這些數據提供了結構線索，卻不會直接給出完整結構。

分析化學家的常見流程是先查參考光譜庫，再推定分子式、從化學資料庫取得候選結構，最後檢查每個候選是否能解釋觀察到的碎片峰。各步驟已有公開工具，但逐筆操作相當耗時，難以跟上單次研究產生的數千筆光譜。

🧩 **讓 Gemini 推理串接專用化學工具**

Mass Spec Skills 是供 Google Antigravity 使用的一組領域技能，結合 Gemini 的化學推理、既有質譜工具與公開化學資料庫。研究者可以用自然語言描述任務及儀器的容許誤差，由代理選擇並串接相關技能。

整體流程包括：

1. **前處理訊號**：辨識前驅離子，清除背景雜訊。
2. **查詢參考光譜庫**：以碎片峰的餘弦相似度比對已知光譜。
3. **推定分子式並排序候選結構**：結合質量、碎片資訊與化學資料庫搜尋。
4. **交叉檢查並整理證據**：比對候選結構與觀察到的碎片、裂解路徑，產生可供化學家審查的報告。

這些步驟也可單獨執行，例如清理有雜訊的光譜、註解峰值或比較候選異構物。文章指出，LLM 單靠自身無法完成整個流程，因為其中需要精確質量計算、資料庫搜尋及化學鍵斷裂模擬。

📊 **案例中，工具以碎片證據區分 845 個異構物**

Google DeepMind 展示了一筆從原始光譜到候選結構的分析：

- 使用 **matchms** 去除 1,700 多個低強度背景雜訊訊號；查詢 GNPS 與 MoNA 參考光譜庫後，沒有找到高信心匹配。
- 使用 **SIRIUS** 的碎片樹評分推定分子式 C20H21ClN6O，質量誤差為 -1.5 ppm。
- 從 PubChem 取得 845 個異構物，結合 **MAGMa**、**MetFrag** 與中性損失分析進行比較。
- 頂尖候選結構可匹配前處理後 19 個峰中的 14 個，涵蓋碎片訊號總強度的 97.7%。當多個異構物得到相同覆蓋結果時，代理進一步檢查鍵結與官能基是否符合觀察到的裂解路徑。
- 最後使用 **RDKit** 驗證候選結構的化學有效性、精確質量與分子式，並繪製結構及標示主要斷裂位置。

這裡的 97.7% 是該案例中碎片訊號強度的涵蓋比例，不是整體分子辨識準確率。

⚠️ **候選結構仍需要專家審查**

對已收錄於資料庫的分子，這套流程可加速辨識。對尚未發現的分子，代理則可協助縮小分子式與碎片所支持的部分結構，為後續完整結構解析提供線索。

輸出重點不只是提出答案，也包括整理支持答案的化學證據，讓化學家能進一步審查。

🎯 **把自然語言介面用在可拆解的分析流程**

對 AI／ML 工程師而言，這個案例展示了一種工具整合方式：讓模型負責選擇步驟與整理推理，再將精確計算、資料庫查詢和模擬交給專用工具。完整流程可從單一請求啟動，各階段也能獨立使用，方便研究者依任務需求採用。

🔗 **來源**
- 標題：From spectrum to structure: Identifying molecules with Mass Spec Skills for Google Antigravity
- 作者／機構：Google DeepMind
- 連結：https://deepmind.google/blog/interpreting-mass-spectra-with-google-antigravity/

#MassSpectrometry #TandemMassSpectrometry #MolecularStructure #ChemicalReasoning #AIAgents #Gemini #GoogleAntigravity #AnalyticalChemistry #MolecularIdentification #ScientificAI
