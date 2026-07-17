---
title: WanSong v1.0 Technical Report
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.14749
score: 89
model: tencent/hy3:free
generated_at: '2026-07-17T08:14:01.065464'
---

📌 【HuggingFace Daily Papers】WanSong v1.0：純擴散模型單次生成 5 分鐘雙音軌歌曲

TL;DR：WanSong 用純 diffusion 單次產出多語言 5 分鐘歌曲與人聲/伴奏雙音軌，並支援步數蒸餾加速。

音樂生成基礎模型近來備受產業關注，但要在高效生成、高保真長音訊與可控性之間取得平衡，始終是難題。多數做法仰賴自回歸（AR）或「AR 接 diffusion」的多階段串接管線，而 WanSong 選擇了一條更直接的路。

🤔 **長篇幅歌曲生成的三大痛點**

技術報告指出，現有音樂生成面臨三項挑戰：難以高效生成、難以兼顧高保真與長形式音訊、以及可控性不足。這也是 WanSong 想要解決的核心問題。

🧩 **純擴散架構，單次推理輸出雙音軌**

WanSong 不像常見的 AR 或級聯式多階段管線（例如先 AR 再 diffusion），而是一個純 diffusion-based 模型。它的設計理念是簡單但強大，直接生成高保真、多語言、最長 5 分鐘的歌曲，且在單一次推理運算中輸出雙 stem（人聲與背景音樂）。

🚀 **用步數蒸餾換取更快推論與客製化彈性**

報告提到，其 diffusion 框架透過 step-distillation（步數蒸餾）實現更快的 inference；同時也提供高效路徑供 fine-tuning 與客製化，以支援下游的編輯任務。

🎯 **實務啟示**

對工程師而言，WanSong 展示了一種繞開 AR 與多階段管線複雜度的可能性：若你的應用需要長音樂、雙音軌分軌與後續編輯，純擴散單次生成的設計在部署與微調上可能更單純，也更易做推理加速。

🔗 **來源**
- 標題：WanSong v1.0 Technical Report
- 連結：https://huggingface.co/papers/2607.14749

#MusicGeneration #DiffusionModel #WanSong #SongGeneration #MultiLingual #DualStems #StepDistillation #FineTuning #AudioAI #HuggingFacePapers
