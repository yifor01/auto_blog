---
title: 'GLM-5.3-Flash vs Qwen3.8-Flash-Next: Two Chinese AI Labs Independently Converge
  on the Same Model Architecture'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/28/glm-5-3-flash-vs-qwen3-8-flash-next-two-chinese-ai-labs-independently-converge-on-the-same-model-architecture/
model: claude-code/sonnet
generated_at: '2026-08-29T11:59:48.401696'
score: 105
---

📌 兩家中國實驗室不約而同，做出幾乎相同的高效注意力架構

TL;DR：GLM-5.3-Flash與Qwen3.8-Flash-Next獨立設計,卻在多項架構細節上高度收斂。

這週內先後上線的兩款開源模型,設定檔讀起來幾乎像互相抄襲——但兩個團隊其實是各自獨立設計的。

🤔 **一天內接連發布的兩款Flash模型**

Z.ai發布GLM-5.3-Flash,一個320B參數的多模態MoE模型,啟用參數18B。隔天,阿里巴巴Qwen團隊發布Qwen3.8-Flash-Next,125B參數、啟用參數6B,作為Qwen4架構的預覽版。兩隊各自設計,卻同時採用3:1的linear attention與full attention混合比例、以2048 token為上限的壓縮索引器(indexer)、把殘差流(residual stream)拓寬成4條閘控分支,並且都用Muon優化器,且在正交化前都先把融合的參數矩陣拆開。

GLM-5.3-Flash是GLM-5系列中第一個原生多模態模型,以MIT授權釋出於Hugging Face。Z.ai先前以「Ox Alpha」的匿名身份在OpenRouter上測試,結果成為當週最受歡迎的模型。它在30T token的多模態語料上訓練,支援1M token上下文窗口。Z.ai宣稱其效能超越GLM-5.2,價格卻只要十分之一,在coding與agentic類基準上逼近Claude Opus 4.8。定價為每百萬input token 0.15美元、每百萬output token 0.50美元。

Qwen3.8-Flash-Next扮演的角色,如同Qwen3-Next之於Qwen3.5——是下一代架構家族的早期公開預覽。模型卡顯示主模型125B,外加51B參數的n-gram embedding表,每個token實際啟用6B參數。原生上下文長度為262,144 token,透過YaRN可延伸至1M。Qwen團隊表示,訓練這個模型所需算力只有Qwen3.7-Plus的約九分之一。

🧩 **拆開設定檔:同一套配方的兩種實作**

| 設計元素 | GLM-5.3-Flash | Qwen3.8-Flash-Next |
|---|---|---|
| 層數與比例 | 45層(34線性+11全注意力) | 48層,3個Gated DeltaNet+1個QSA重複 |
| 線性注意力 | Kimi Delta Attention(KDA),per-channel decay gate | Gated DeltaNet(GDN),per-head gate |
| 全注意力 | NoPE多頭潛在注意力(MLA,DeepSeek風格) | GQA(在QSA內) |
| 索引器 | 32-head lightning indexer,top-2048,搭配IndexPool壓縮4個key向量為1個 | 以4-token微區塊評分,取top-512區塊(=2048 token) |
| 殘差流 | Manifold-Constrained Hyper-Connections(mHC),4分支 | Gated Residual,4分支,讀寫閘各自獨立 |
| 位置編碼 | 捨棄RoPE(qk_rope_head_dim=0),完全NoPE | 保留RoPE |
| 優化器 | Muon(融合矩陣先拆分再正交化) | 同左,並拆分QKV/SwiGLU/GDN投影 |

兩者的線性注意力層都把歷史資訊壓縮進固定大小的遞迴狀態,讓每個token的運算量不隨上下文長度增加;真正做長距離精確檢索的,是那四分之一的全注意力層,而這正是KV cache真正存在的地方。兩隊也不約而同地,都不讓全注意力層看完整上下文,而是各自加了一個小型索引器,先把歷史壓縮4倍再挑出重要片段——GLM的indexer取top-2048,Qwen的QSA則取top-512個4-token區塊,換算下來同樣是2048 token的注意力預算。

📊 **效率提升的具體數字**

Qwen表示QSA在1M token上下文下,可帶來最高7.6倍的prefill加速與4.9倍的decoding加速。GLM這邊,相較完整版GLM-5.3,Flash架構把注意力運算量削減約3倍、KV cache大小削減4.4倍,啟用參數幾乎砍半(18B對32B),層數也從92層降到45層。

💡 **殘差流拓寬與RoPE的分歧**

兩個團隊都放棄了自2017年Transformer以來單一殘差流的設計,改成4條並行分支,由閘門控制每個區塊讀寫的內容。GLM採用DeepSeek原創的mHC設計;Qwen則自行設計Gated Residual,用逐元素、資料相關的讀取閘與逐分支的純量寫入閘來調節資訊流動——Qwen表示這個做法省去了Hyper-Connections額外的分支混合步驟,降低記憶體存取開銷,且閘門本身足以抑制活化值離群,讓殘差可以用FP8儲存。Qwen對兩種做法都做過消融實驗,發現品質大致相當。

真正分歧的地方是全注意力層的RoPE(旋轉位置編碼)。GLM-5.3-Flash直接捨棄RoPE,讓稀疏MLA層完全採用NoPE,位置資訊改由遞迴的線性層隱式傳遞。Qwen也試過同樣做法,但最終保留了RoPE——根據Qwen3.8-Next的技術報告,NoPE在預訓練階段沒有造成可觀測差異,問題出在後訓練(post-training)之後:採用NoPE的版本經常無法正常停止生成。這對整個領域是個值得留意的警訊:預訓練的loss曲線可能掩蓋只有在RLHF階段調校後才會浮現的行為缺陷。

這套配方也不只兩家在用。DeepSeek在DeepSeek-V3.2-Exp中率先提出「稀疏索引器+2048預算」的DSA設計,mHC同樣源自DeepSeek;Moonshot的Kimi則貢獻了KDA這個GLM採用的線性注意力層。中國的開源模型生態明顯正在互相交叉引用架構元件,並收斂到相近的設定值。

⚠️ **不是所有人都買單:MiniMax的反例**

MiniMax是明確的異數。在M2開發過程中,團隊大規模測試了線性注意力與滑動視窗注意力,發現在SFT後、尤其是超過32K上下文時,多跳推理(multi-hop reasoning)能力有明顯缺陷,因此M2最終每一層都採用完整的softmax注意力。到了M3,MiniMax改用自家的MiniMax Sparse Attention(MSA),透過區塊選擇稀疏化softmax注意力,但完全不包含線性注意力層。換句話說,Z.ai、Qwen、DeepSeek與Kimi都押注3:1的線性混合架構能保留推理能力,而MiniMax的消融實驗結果,至少在他們自己的模型堆疊上並不支持這個結論。這個領域顯然還沒有定論。

🎯 **實務啟示**

對於要選型或自建高效MoE架構的工程師,GLM與Qwen的收斂提供了一份可信度較高的「共識配方」:3:1線性/全注意力混合、2048 token索引預算、4分支殘差流、Muon優化器搭配矩陣拆分。但MiniMax的反例也提醒,這套配方在長上下文多跳推理上是否穩健,仍需依自身任務實測驗證,不宜照單全收。

🔗 **來源**
- 標題：GLM-5.3-Flash vs Qwen3.8-Flash-Next: Two Chinese AI Labs Independently Converge on the Same Model Architecture
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/28/glm-5-3-flash-vs-qwen3-8-flash-next-two-chinese-ai-labs-independently-converge-on-the-same-model-architecture/

#LLM #MoE #Attention #GLM #Qwen #OpenWeights #ModelArchitecture #DeepLearning #AIResearch #Transformer
