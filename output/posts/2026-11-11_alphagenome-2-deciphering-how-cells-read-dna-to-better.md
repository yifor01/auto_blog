---
title: 'AlphaGenome 2: Deciphering how cells read DNA to better understand disease'
source: Google DeepMind
url: https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/
model: claude-code/sonnet
generated_at: '2026-11-11T23:36:39.858662'
pinned: true
---

📌 AlphaGenome 2：讓 AI 讀懂特定細胞如何解讀 DNA

TL;DR：Google DeepMind 推出次世代 AlphaGenome 2，可預測 DNA 變異對特定細胞類型的影響。

人體裡每顆細胞都帶著同一份 DNA 藍圖，但心肌細胞與對抗感染的免疫細胞，開啟的基因完全不同。一個 DNA 上的微小變異，可能只在某種特定細胞裡才會「出事」，放進整個組織的平均值裡看，訊號就被稀釋掉了。這正是 Google DeepMind 想用 AlphaGenome 2 解決的問題。

🤔 核心問題：組織平均值蓋住了細胞層級的訊號
去年發布的 AlphaGenome，可以預測 DNA 變異對廣泛組織層級分子活性的影響，後續的 AlphaGenome Atlas 更涵蓋人類基因組中全部90億種可能的單點變異預測。但要預測變異如何影響「特定細胞類型」中的基因表現，仍是未解難題，而這正是驅動人類特徵與疾病的關鍵因素。像 Human Cell Atlas 這類全球計畫已經在繪製數百萬顆細胞的基因表現圖譜，缺的是一個能把這些圖譜變成「預測引擎」的模型。

🧩 方法與架構：從平行輸出改為條件式模型
AlphaGenome 1 的作法，是把一段100萬個字母長的 DNA 序列丟進模型，一次平行輸出數千個實驗、涵蓋多種組織的預測結果。這種平行架構雖然有效率，但模型容量被攤薄，難以捕捉相近細胞類型之間的細微差異。

AlphaGenome 2 改成條件式模型（conditional model）：除了輸入 DNA 序列，還會在架構的每一個階段，把「目標生物條件」（組織、細胞類型或狀態）作為輸入條件一起餵進模型。這個條件可以來自既有的細胞類型參考目錄，也可以透過團隊設計的 cell encoder，直接從研究者自己的 single-cell 實驗資料即時生成。

這個設計帶來一個額外能力：跨模態補值（cross-modality imputation）。因為模型把「細胞的生物狀態」與「輸出的實驗讀數」拆開處理，只要研究者輸入一種量測資料（例如 single-cell 基因活性），模型就能預測其他沒有量測過的性質，例如染色質可及性（chromatin accessibility），幫助研究者決定下一步該做哪個實驗。

除了基因表現、組蛋白修飾（histone modification）與染色質可及性，AlphaGenome 2 也新增預測 DNA 甲基化（DNA methylation），這是研究社群多次要求的讀數項目。

📊 資料與訓練
AlphaGenome 2 同時使用人類與小鼠的 bulk 與 single-cell 資料訓練，總計超過107百萬筆個別細胞圖譜，涵蓋68種組織。

📊 實驗結果：變異偵測率幾乎翻倍
在 TenK10K 資料集（一份涵蓋28種原發性免疫細胞類型的大型 single-cell 圖譜）上，AlphaGenome 2 對比經 single-cell 資料微調後的原版 AlphaGenome 與其他專用工具，表現如下：

| 指標 | AlphaGenome 1（微調版） | AlphaGenome 2 |
|---|---|---|
| 可靠識別的因果變異比例 | 16% | 30% |
| 方向性基因效應識別比例 | 23% | 43% |

另外，在一項發現「某個遠端調控開關變異會過度活化 ETS2 基因，進而在腸道巨噬細胞中誘發 IBD（發炎性腸道疾病）」的標竿研究中，AlphaGenome 2 針對腸道各種免疫細胞類型進行預測，成功在計算上重現這個發現：它精準指出該因果變異，並顯示這個變異只選擇性地提升腸道巨噬細胞中 ETS2 的表現，其他細胞類型與基因大致不受影響。

團隊也測試模型在「完全沒見過的細胞狀態」上的泛化能力：只要上傳幾十顆細胞的 single-cell RNA-seq 基因活性快照，AlphaGenome 2 就能把這份資料壓縮成細胞狀態表徵，再用它來條件化模型，對全新的細胞狀態做預測，表現可以媲美甚至超越直接在該資料集上訓練或微調的模型。例如面對一份 COVID-19 mRNA 疫苗研究的全新 single-cell 資料，AlphaGenome 2 能區分「被疫苗活化的 T 細胞」與「靜止狀態的 T 細胞」，並發現一個與重症 COVID-19 相關的變異，在細胞處於活化狀態時，對基因活性的干擾明顯更強，而這個效應在未活化的細胞中根本不會被觀察到。

💡 深入分析
劍橋大學幹細胞醫學教授、Human Cell Atlas 共同創辦人 Sarah Teichmann 指出，AlphaGenome 2 真正令人興奮的地方，在於它能直接套用到新的 single-cell 資料上而不需重新訓練，即使只拿到少量細胞的資料，也能預測 DNA 變異在這些新發現的細胞狀態中會如何作用。這等於把「人類遺傳學」與「單細胞生物學」這兩條原本分開發展的研究路線，接上了同一套預測引擎。

🎯 實務啟示
對做基因體學或生物資訊的工程團隊而言，AlphaGenome 2 的條件式架構提供了一個重要參考：當預測目標本質上是「輸入 X + 條件 C → 輸出 Y」，把條件直接注入架構每一層，往往比平行輸出多個頭（multi-head）更能捕捉細膩差異，也更容易泛化到訓練時沒見過的新條件。AlphaGenome 2 目前透過 AlphaGenome API 開放非商業研究使用，商業研究則是私測階段。

🔗 來源
- 標題：AlphaGenome 2: Deciphering how cells read DNA to better understand disease
- 作者／機構：Adam Gayoso, Natasha Latysheva, Pushmeet Kohli, Žiga Avsec — Google DeepMind
- 連結：https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/

#AlphaGenome #GoogleDeepMind #Genomics #ComputationalBiology #SingleCell #DNA #PrecisionMedicine #MachineLearning #HumanCellAtlas #BioAI
