---
title: 'ShortOPD: Recovering Pruned LLMs with Short-to-Long On-Policy Distillation'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.13124
score: 99
model: tencent/hy3:free
generated_at: '2026-07-16T08:13:10.515824'
---

📌 【HuggingFace Daily Papers】剪枝後 LLM 崩潰？ShortOPD 用短到長蒸餾救回生成能力

TL;DR：ShortOPD 以短到長 on-policy 蒸餾，將壓縮模型分數拉回約 9 倍未修復值。

結構化剪枝（structured pruning）一直被視為對硬體友善的 LLM 壓縮手段，但多數驗證都停留在選擇題型的辨識任務。真正部署時需要的自由生成（free-form generation），同一個壓縮模型卻可能直接崩潰——這道鴻溝，比想像中更致命。

🤔 **壓縮後生成崩潰，但有用輸出沒被抹除**

作者觀察到兩個現象解釋了這個落差。第一，壓縮後 greedy pass@1 幾乎歸零，但在重複取樣下 pass@k 明顯回升：代表有用的生成只是被降權（demoted），而非被刪除。第二，可恢復的區間主要敗在「字尾重複」（suffix repetition）——模型一直重複尾巴的 token。

🧩 **用 On-Policy Distillation 在模型自身狀態上做修復**

修復方式應該是在壓縮模型自己的 on-policy 狀態上訓練，並給予密集的 token 等級監督。On-Policy Distillation（OPD）正是這麼做：把壓縮前的模型當成凍結教師（frozen teacher），重用來提供監督。

但長程 on-policy rollout 會把早期修復預算花在低資訊量的重複字尾上，拖慢 loss 下降。為此，本文提出 ShortOPD：一種 short-to-long 的 OPD 排程。

具體做法是：
- 偵測教師確認的重複字尾（teacher-confirmed repetitive suffixes）
- 將存活的字首（surviving prefix）視為該次 rollout 的「有效長度」
- 把未來的 rollout 預算分配給政策目前能用到的有效長度

也就是說，訓練預算不再浪費在模型已經陷入重複的尾巴，而是集中在真正能學到東西的字首區段，再逐步拉長。

📊 **數學、程式碼、開放生成全面回升**

在數學、程式碼與開放式生成任務上，ShortOPD 帶來的結果如下：
- 壓縮模型分數提升至約 9 倍於未修復值
- 為標準修復方法（SFT w/o KD、KD、SeqKD）的 1.6 到 4.4 倍
- 使用固定 8192 token rollout horizon 的對照：ShortOPD 在兩分內追平，但只花四分之一訓練時間（8.5 對 35.9 小時），且 rollout token 量少 71%

🎯 **讓結構化剪枝真正走向部署**

這份 recipe 的價值在於：它把結構化剪枝從「perplexity 與選擇題基準上的邊際增益」推往「部署等級的生成品質」。對工程師而言，若你手上有結構化剪枝後但生成會重複崩壞的 checkpoint，ShortOPD 提供了一條以自身 on-policy 狀態修復、且顯著省時省 token 的實作路徑。

🔗 **來源**
- 標題：ShortOPD: Recovering Pruned LLMs with Short-to-Long On-Policy Distillation
- 連結：https://huggingface.co/papers/2607.13124

#LLM #StructuredPruning #OnPolicyDistillation #ModelCompression #ShortOPD #TokenLevelSupervision #GenerationQuality #KnowledgeDistillation #InferenceEfficiency #HuggingFacePapers
