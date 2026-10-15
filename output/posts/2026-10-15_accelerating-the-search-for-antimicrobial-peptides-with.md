---
title: Accelerating the search for antimicrobial peptides with Google Antigravity
source: Google DeepMind
url: https://deepmind.google/blog/accelerating-antimicrobial-discovery/
model: claude-code/sonnet
generated_at: '2026-10-15T20:27:54.049745'
pinned: true
---

📌 Google DeepMind 用 AI 代理，從蛋白質「暗物質」裡挖出抗菌候選肽

TL;DR：Google Antigravity 結合 ProtNLM，協助研究者在單一工作階段內找到具潛力的新型抗菌胜肽候選分子。

全球每年可能有數百萬筆蛋白質序列被定序出來，卻因為和已知蛋白質不夠相似，始終被歸類在資料庫裡的「暗物質」區，沒有人知道它們到底是做什麼的。Google DeepMind 這次展示的案例，就是如何用 AI 代理把這些沉睡的序列，變成具體的抗菌候選分子。

🤔 **背景：抗生素抗藥性是迫切危機**

文中指出，抗生素抗藥性持續上升是當前最緊迫的全球健康危機之一，若不加以因應，到 2050 年估計每年可能造成一千萬人死亡。抗菌胜肽（antimicrobial peptides, AMP），尤其是細菌素（bacteriocin），被視為傳統抗生素的一種有潛力替代方案，因為它們演化上針對的是競爭菌種的根本弱點，從細胞外殼到關鍵胞內機制都可能是目標，使病原體較難產生抗藥性。基因體與總體基因體定序量爆炸性成長，讓全球資料庫累積了數十億筆天然胺基酸序列，但其中許多序列仍缺乏功能註解。全球最大的公開蛋白質序列與功能資訊資源 UniProt，就有數百萬筆直接從定序計畫轉入、功能未知的序列。為了解決這個問題，Google 開發了 ProtNLM（Protein Natural Language Model），這是一個直接學習胺基酸序列背後演化「文法」的深度學習模型，可以直接從原始蛋白質序列預測其生物功能，為大量未命名的 UniProt 條目補上具高信心度的功能標籤。

🧩 **工作流程：研究者與代理的多輪協作**

研究團隊在 Antigravity 中設定了一個明確的生物學目標：在 Streptococcus pseudopneumoniae（假肺炎鏈球菌）中尋找並以運算方式驗證新型抗菌胜肽。整個過程由研究者引導策略方向、決定要問什麼問題與蒐集哪些證據，代理則負責執行跨資料庫查詢、結構分析與文獻整合等繁重工作，步驟大致如下：

1. **搜尋海量資料庫**：代理查詢資料庫，從數百萬筆條目中篩選出少數值得關注的候選者，找到一個長度 97 個胺基酸、屬於 Lactococcin 972 家族的細菌素（UniProt ID：A0A0U0D591）。
2. **驗證新穎性**：研究者引導代理透過 EMBL-EBI 的 NCBI-BLAST 服務，將候選分子與 Swiss-Prot 中經人工審核的蛋白質比對，確認它與已知審核蛋白質之間沒有具意義的序列同源性。
3. **結構層面的推理**：代理從 AlphaFold 蛋白質結構資料庫取得候選分子的 3D 模型，與實驗測定的結構比對以尋找遠緣同源物並疊合評估相似度，結果顯示該候選分子的摺疊結構與一個經實驗驗證的細菌素高度吻合，與 ProtNLM 的預測互相印證。
4. **解讀基因體上下文**：代理檢視候選基因周邊的「鄰居」基因，發現這個先前未被定性的候選者，座落在一個緊密耦合的操縱子（operon）上游，距離一個 ABC 轉運蛋白通透酶（permease）及其可能的 ATP 結合蛋白伴侶僅 6 個鹼基對，旁邊還有另一個已標註的細菌素與一個 XRE 轉錄調控因子，這些都是支持其屬於一套運作中細菌素系統的有力情境證據。
5. **從文獻建立機制假說**：代理回顧既有文獻，提出該分子可能的作用機制與目標病原體，推測其作用機制與細菌細胞分裂有關，並預測其潛在效力範圍涵蓋多種具抗藥性的病原體。
6. **產出實驗計畫**：代理將這些電腦運算發現轉譯為可執行的濕實驗（wet-lab）方案，涵蓋蛋白質表現、抗菌敏感性測試、標的結合測試與體外毒性測試。文中提到，這個候選分子連同同一流程發現的其他候選者，目前已進入濕實驗驗證階段。

📊 **一個共享的 3D 工作畫布**

為了支援這整套端到端工作流，團隊在 Antigravity 中引入了「Biomolecular Structure Viewer」，一個內嵌的 3D 視覺化工具。研究者與代理共享同一個視覺化狀態，當代理從 AlphaFold 資料庫或研究者自己產出的預測結果中取得結構時，可以即時驅動檢視器，例如高亮標示關鍵功能區域來視覺化解釋其假說。

⚠️ **仍只是運算推論，還需濕實驗驗證**

文中明確指出，本案例找到的候選分子是一個「具生物學可行性、並有結構與基因體證據支持的候選者」，但仍需要濕實驗驗證才能得出最終結論。這次示範也只聚焦在單一病原體的一段胺基酸窗口，研究者仍可引導代理調整篩選條件、探索不同序列長度，或鎖定其他優先病原體。

🎯 **實務啟示**

這個案例展示了「人類設定策略方向、AI 代理執行繁瑣跨資料庫查核」的協作模式，把原本需要橫跨多個資料庫、耗時數天的零散查找工作，壓縮成一次互動式的工作階段。對打造科學研究用 agentic workflow 的工程師而言，值得關注的重點在於如何讓代理的每一步推理（資料庫篩選、結構比對、基因體上下文、文獻綜合）都能附上可追溯的證據鏈，而不是只給出一個黑箱結論，這也是本案例中研究者能持續介入與驗證的關鍵設計。

🔗 **來源**
- 標題：Accelerating the search for antimicrobial peptides with Google Antigravity
- 作者／機構：Pengfei Tian, Maxwell L. Bileschi, Zoi Tsangalidou, Sukhdeep Singh and Lucy J. Colwell（Google DeepMind）
- 連結：https://deepmind.google/blog/accelerating-antimicrobial-discovery/

#GoogleDeepMind #Antigravity #ProtNLM #AMR #DrugDiscovery #AIforScience #Bioinformatics #AlphaFold #AgenticWorkflow #AntimicrobialPeptides
