---
title: How Claude designed protein binders against scorpion neurotoxins
source: Anthropic Research
url: https://www.anthropic.com/research/claude-scorpion-toxin-binder-design
model: claude-code/sonnet
generated_at: '2026-10-20T20:41:49.741817'
pinned: true
---

📌 【Anthropic 研究】Claude 自主設計出對抗蠍子神經毒素的蛋白質結合體

TL;DR：Claude 以近乎全自主方式設計 211 個蛋白質結合體，其中 17 個通過實驗室驗證，為蠍毒解毒劑研究開了一道門。

每年全球有超過 120 萬人被蠍子螫傷，造成逾 3,250 人死亡，受害者多是醫療資源匱乏地區的兒童。這是一個長期被製藥產業忽視的問題，而 Anthropic 這次讓 Claude 親自下場，試著用 de novo 蛋白質設計解決它。

🤔 **被忽視的熱帶病：蠍毒解毒劑為什麼這麼難做**

蠍毒中最危險的神經毒素會附著在神經細胞的鈉離子通道上，讓神經異常放電，釋放大量壓力性化學物質（如腎上腺素），嚴重時可導致心臟衰竭與肺部積液。目前的解毒劑多以免疫動物（如馬）的抗體製成，製程需耗時數月，先從數千隻蠍子採毒、免疫馬匹、再純化馬血中的抗體，且通常只對少數幾種神經毒素有效,成本高、供應也常不足。由於開發成本難以回收，蠍螫傷害長期被視為一種「被忽視的熱帶病」。

🧩 **讓 Claude 自己挑目標、設計結合體**

Anthropic 的生命科學研究團隊與金融投資研究機構 Citrini Research 合作，先透過與 Claude 腦力激盪找出題目，最終選定蠍子神經毒素作為設計目標。團隊沿用了此前蛋白質結合體研究的提示詞，並與 Citrini 一起修改後交給 Claude。

接下來的 64 小時，一個在 Claude Science 內部運作的研究模型以主要自主的方式工作，研究團隊僅給出 4 次追加指示。Claude 自行搜尋 Protein Data Bank（PDB）與 AlphaFold 資料庫（AFDB）挑選毒素結構，並為每個毒素選出 5 個「熱點」（hotspot，結合體要鎖定的特定胺基酸位置）。

這次campaign 鎖定來自四個地區的五種蠍毒神經毒素：

| 毒素 | 所屬家族 | 來源地區 |
|---|---|---|
| Cn2 | β 家族 | 墨西哥 |
| Ts1 | β 家族 | 巴西 |
| AaH I | α 家族 | 北非 |
| AaH II | α 家族 | 北非 |
| LqhIII | α 家族 | 中東 |

這五個毒素雖共享相同的整體蛋白折疊形狀，但彼此的胺基酸序列相似度僅 26% 至 62%，是一個頗具挑戰性的多毒素設計測試。Claude 被要求設計四種結合體：針對五種毒素各自設計的單一結合體、同時鎖定 β 家族（Ts1、Cn2）的結合體、同時鎖定 α 家族（AaH I、AaH II、LqhIII）的結合體,以及同時鎖定全部五種毒素的「廣效型」結合體。多毒素結合體背後的實際考量，是能減少通用解毒劑配方所需的分子數量，理論上會是最具成本效益且不受地域限制的治療方案。

📊 **318,484 個設計、211 個送測、17 個命中**

在整個設計過程中，Claude 總共產生了 318,484 個蛋白質設計，並從中選出 180 個進行實驗測試；研究團隊再加上 Claude 協助挑選的 31 個，合計 211 個設計。合作夥伴 Adaptyv Bio 與 Twist Bioscience（兩家合約研究機構，CRO）對全部 211 個設計進行了實驗室結合測試，最終有 17 個設計符合結合標準，分別對應四種神經毒素。

值得注意的是，這次測試只驗證了「是否能緊密結合目標毒素」，並未在細胞環境中確認這些結合體能否真正中和蠍毒,因此 Anthropic 並未宣稱已做出解毒劑。團隊將研究結果送交兩位外部專家，西班牙國家癌症研究中心（CNIO）的 Susana Vázquez Torres 與丹麥技術大學（DTU）的 Timothy P. Jenkins 審閱，兩人皆認為這是一個有潛力的初步成果；Jenkins 更指出，在數天內平行針對五種毒素設計出可信的結合體，展現了 AI 驅動的治療發現正在經歷的範式轉移，對長期缺乏商業投資動機的動物毒傷害（如蛇咬、蠍螫）研究尤其有意義。

⚠️ **結合不再是瓶頸，但離真正的藥物還很遠**

Anthropic 在文中直言，現在針對幾乎任何目標都能快速取得高親和力的結合體,「結合」本身已不再是主要瓶頸。真正的挑戰在於後續的藥物開發管線：如何把這些結合體轉化為安全、負擔得起、且能廣泛取得的藥物，這對毒蛇、蠍子等造成大量傷亡卻長期缺乏商業投資的疾病領域而言，才是決定實際影響力的關鍵。

🎯 **實務啟示**

這個案例展示了一種可複製的研究模式：給模型一個清楚的提示詞與結構化資料來源（PDB、AFDB），再搭配少量人工追加指示，讓 AI 近乎自主完成數十萬規模的生成與篩選,大幅壓縮了傳統濕實驗室前期探索的時間。Anthropic 也公開了全部 211 個設計與相關資料供研究社群使用,對關注 AI for Science 的工程師與研究者而言，這是一份可直接拿來分析或延伸的真實資料集。

🔗 **來源**
- 標題：How Claude designed protein binders against scorpion neurotoxins
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/research/claude-scorpion-toxin-binder-design

#Anthropic #Claude #ProteinDesign #DrugDiscovery #AIforScience #DeNovoDesign #Biotech #NeglectedDiseases #ComputationalBiology #LLMAgents
