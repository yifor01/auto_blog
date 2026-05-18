---
title: "Dynamic Chunking for Diffusion Language Models"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.15676
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-18T20:30:22.440647
---

📌 **Dynamic Chunking for Diffusion Language Models：讓語言模型依照內容自動切塊**

你以為把文字切成固定長度的塊就能讓擴散模型又快又好？其實這種硬切可能把有意義的詞切斷，讓模型學到的結構是錯的。

🤔 **固定塊切割浪潮下的語義斷裂**  
現有的離散擴散語言模型會把序列依照位置劃成大小固定的塊，這樣做讓塊內可以並行去噪，但同時也把語義相關的 token 分離到不同塊，把無關的 token 強行放在一起。這種「位置定義」的切割方式浪費了序列本身已有的語義結構。

🧪 **透過可學習的 Chunking Attention 產生語義塊**  
本文提出 **D**ynamic **C**hunking **D**iffusion **M**odel (DCDM)。核心是一個可微分的 **Chunking Attention** 層，它會根據可學習的子空間把 token 路由到 K 個簇。這些簇的分配產生一個「塊因果」注意力遮罩，使得離散擴散去噪器在語義塊上自回歸地分解序列似然。這種設計嚴格概括了傳統的位置塊離散擴散，因而能捕捉到序列中的真實語義邊界。

📈 **在 1.5B 參數規模下，DCDM 優於無結構與固定塊擴散基線**  
在多個下游基準上，參數規模最高達到 1.5B 的 DCDM 同時優於既沒有任何塊結構的無結構擴散模型和使用固定位置塊的基線。優勢在不同參數規模下保持穩定，且在訓練早期就能觀察到。

🔍 **內容定義的塊讓去噪更符合語義，提升模型效率與品質**  
因為塊現在是依照語義內容而非位置劃分，去噪時塊內的 token 更可能屬於同一語義單元。這讓模型在學習序列結構時不再被人為的塊邊界干擾，從而在同等計算資源下獲得更好的生成品質。

⚠️ **尚未公開程式碼，實驗規模限於 1.5B，長期穩定性未見**  
論文未提供開源程式碼，實驗主要集中在最多 1.5B 參數的模型上，長期訓練穩定性以及更大規模的擴展行為尚未被報告。

🎯 **對擴散語言模型設計者而言，可考慮用可學習的聚類層取代硬切塊**  
如果你正在設計或調優離散擴散語言模型，這項工作表明：用可學習的聚類機制（Chunking Attention）來產生語義塊，能在不增加顯著計算開銷的情況下提升模型對結構的建模能力。未來可嘗試將此層整合至現有的擴散框架中，觀察在不同任務與規模下的具體提升。

🔗 **論文連結**  
📝 Dynamic Chunking for Diffusion Language Models  
👤 Yichen Zhu, Xiaoming Shi, Peng Zhao, Weiyu Chen, Debing Zhang  
🏫 CSE, HKUST; Xiaohongshu Inc.; Alibaba group; CityUHK  
🔗 https://arxiv.org/abs/2605.15676  

你有沒有嘗試過讓模型自行決定「塊」的邊界？歡迎在留言區分享你的想法與經驗 👇

#AI #DiffusionModels #LanguageModel #ChunkingAttention #HKUST #Xiaohongshu #Alibaba #CityU #GenAI
