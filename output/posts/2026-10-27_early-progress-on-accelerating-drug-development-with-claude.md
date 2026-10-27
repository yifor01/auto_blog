---
title: Early progress on accelerating drug development with Claude
source: Anthropic Research
url: https://www.anthropic.com/research/early-progress-drug-development
model: claude-code/sonnet
generated_at: '2026-10-27T21:23:29.230992'
pinned: true
---

📌 【Anthropic 官方發布】六家藥廠實測 Claude：新藥研發的瓶頸不只在分子設計

TL;DR：Anthropic 公開與六家生技公司合作的早期數據，顯示 Claude 在藥物研發多個環節都帶來實測可量化的加速效果。

多數人想到 AI 做藥物研發，第一反應是「幫忙設計新分子」。但 Anthropic 這次公開的案例告訴我們：真正拖慢新藥上市的瓶頸，散落在從早期研究到法規文件的每一個階段，而不只是分子設計那一步。

🤔 **瓶頸分散在整條研發流程**

Anthropic 的生命科學團隊過去幾個月與六家組織（BigHat Biosciences、Bristol Myers Squibb、Divergence Labs、Enveda、Generate Biomedicines、The Column Group）展開深度研究合作，並同步啟動自己的藥物發現專案，包括針對罕見兒童肌肉萎縮症的計畫。Anthropic 指出，藥物開發涵蓋標的辨識、分子設計、量產最佳化、法規文件撰寫、臨床試驗設計等眾多任務，瓶頸分布在整條流程中，因此策略是讓 Claude 深入參與所有這些任務，而非只解決單一問題。

🧩 **五個案例，各自攻克不同環節**

- **Generate Biomedicines（細胞治療工程）**：六位科學家用 Claude Code 重新設計 CAR T 細胞治療的部分基因指令，目標是讓原本只能治療血癌的療法也能對付實體腫瘤。
- **Divergence Labs（候選藥物生成）**：開發能把 IgE 從免疫細胞上「拆下來」的食物過敏新療法，需要雙臂結構的精密抗體設計，由 Claude 轉化目標為詳細設計方案並大量生成候選分子。
- **BigHat Biosciences（候選藥物最佳化）**：Claude 連結 BigHat 的實驗室資料系統 Reccy，針對兩個抗體片段的結合力、穩定性、抗聚集性提出改良方案，並在過程中協助重新分析可疑的檢測指標。
- **Enveda（量產與法規文件）**：把製造文件串接給 Claude，由其標記潛在問題，並協助撰寫法規文件初稿。
- **The Column Group（新創公司模式）**：與 Claude 合作成立新公司 Pleiades，嘗試用 Claude 讓一個小團隊能同時推進更多、更複雜的藥物研發專案。

📊 **實測數據**

| 案例 | 關鍵數據 |
|---|---|
| Generate Biomedicines | 新設計比標準版短約 70%；受體數量增加約 10 倍；殺腫瘤細胞更有效率，免疫細胞存活更久 |
| Divergence Labs | 約一個月內生成約 35,000 個抗體設計；篩出 3 個結合型 hit、20 個拆解型 hit，其中 3 個拆解效果優於標準藥物 |
| BigHat Biosciences | 約 10 週內測試約 1,010 個變體；最佳版本結合力提升逾 10 倍，熱穩定性提升 18°C，抗聚集速度減緩逾 100 倍 |
| Enveda | 在 1,061 頁文件測試中，抓出全部 11 個人工審查員發現的問題，另外多抓出 7 個；人工審查時間從 25 小時以上降至不到 3 小時（減少 89%）；一份法規文件草稿從約 3 個月縮短為 4 小時 |

⚠️ **仍是早期階段，成效待後續驗證**

Anthropic 自己也坦言，這些案例的正向效果能否持續，仍需後續追蹤；是否能真正產出有效新藥，要等臨床與法規流程走完才能確認。文中也提到團隊已根據這些合作經驗，優先調整了 Claude 在特定能力上的改進方向，顯示目前模型仍有待補強之處。

🎯 **實務啟示**

對想把 AI 導入研發流程的團隊來說，這些案例的啟示是：別只盯著「AI 設計分子」這個最顯眼的應用，文件審查、法規草稿、實驗數據重新分析這類「重複但高風險」的工作，往往才是導入 AI agent 能最快看到時間節省的地方。

🔗 **來源**
- 標題：Early progress on accelerating drug development with Claude
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/research/early-progress-drug-development

#Anthropic #Claude #DrugDiscovery #AIinBiotech #LifeSciences #ClaudeCode #BiotechAI #DrugDevelopment #AIResearch #Pharma
