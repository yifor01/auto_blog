---
title: '[AINews] Xiaomi MiMo-V2.6-Pro 1T-A42B: the new top Open Weights model, trained
  for $3M'
source: Latent Space
url: https://www.latent.space/p/ainews-xiaomi-mimo-v26-pro-1t-a42b
model: claude-code/sonnet
generated_at: '2026-09-22T20:21:16.793230'
score: 112
---

📌 小米MiMo-V2.6-Pro:2.6M美元RL訓練衝上開源智慧指數第一

TL;DR：小米首度公開全模態開源前沿模型,RL訓練過程罕見透明,登頂Artificial Analysis開源智慧指數。

在多數開源模型仍圍繞著Qwen、DeepSeek、Kimi這幾個熟面孔打轉時,一家做手機的公司,突然把自己的強化學習訓練過程攤在陽光下,還一舉拿下開源模型智慧指數榜首。這家公司是小米。

🤔 **不在「六小虎」名單裡的黑馬**

根據Latent Space彙整的AI News報導,小米過去並不被視為中國前沿AI實驗室的代表(即所謂「六小虎」)之一,這次MiMo-V2.6系列的發布因此顯得格外突然。官方描述中,MiMo-V2.6-Pro是小米目前最強的模型,MiMo-V2.6-Flash則在智慧、效率與成本之間取得平衡,兩者都是「natively omnimodal」,也就是原生支援多模態輸入輸出的模型。此外還同步推出MiMo-V2.6-Pro-UltraSpeed版本,在相同品質下輸出速度最高可達20倍。

促成這次關注度的另一個因素,是曾任職DeepSeek的工程師羅福莉(Fuli Luo)加入小米後,直接把最終階段的RL訓練過程即時公開,呈現出不尋常的內部指標透明度。

🧩 **RL規模化的三個方向**

根據Latent Space引述的小米技術報告,這次RL訓練沿著三個軸線擴大規模:

- **更大批次與更高吞吐量**:採用完全非同步架構,每次更新1,568個樣本,訓練上下文長度最高達1M,每步處理3.5至3.7B個token。
- **更多任務、更豐富的環境**:訓練套件橫跨程式碼、通用Agent、視覺與資安任務,並混用多種訓練框架(harness),讓不同能力互相強化。
- **更多裁判算力**:在同組內做相對比較,為長任務RL提供更精確、更多樣的獎勵訊號,形成自我改進的閉環,並引導模型用更短路徑、更少token完成任務。

小米表示,除了完整的7,000多個任務資料集尚未釋出外,環境程式碼與訓練配方(涵蓋程式碼、ARVO漏洞重現環境、通用知識工作、視覺/網頁開發、音樂生成、可組合的mini-harnesses等)全數開源。

📊 **開源智慧指數登頂,MIT授權**

Artificial Analysis的數據顯示,MiMo-V2.6-Pro以Intelligence Index 46分,成為目前排名第一的開源權重模型,總參數1.02T、啟用參數42B,輸入/輸出成本分別約為每百萬token 0.435美元與0.87美元。根據報導,模型以MIT授權釋出。

社群反應也相當熱烈:有評論指出,這次背後的RL run耗時130小時、處理75B token,花費約2.6萬美元(原文標題則提及訓練總花費約3百萬美元);另有觀察指出,小米的MiMo系列在JAX與TPU上進行RL擴充,擴大規模「多半只是改配置,而非重寫程式碼」。

💡 **開源RL環境,可能是下一個戰略資源**

多位評論者認為,高品質的開源RL訓練環境,未來的戰略重要性可能不亞於上一輪循環中的預訓練語料庫。這也呼應了報導中提到的更大背景:過去十週內,Kimi K3、Qwen3.8-Max、DeepSeek V4-Pro、GLM-5.3等一連串開源前沿模型密集發布,開源陣營正以遠低於閉源模型的成本持續逼近前沿能力。

🎯 **實務啟示**

如果你在評估要不要自建RL訓練管線,小米這次釋出的環境程式碼、訓練配方與mini-harnesses,值得作為起點研究,尤其是「裁判算力」這個常被忽視、卻直接影響獎勵訊號品質的環節。

🔗 **來源**
- 標題：[AINews] Xiaomi MiMo-V2.6-Pro 1T-A42B: the new top Open Weights model, trained for $3M
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-xiaomi-mimo-v26-pro-1t-a42b

#Xiaomi #MiMo #OpenSource #ReinforcementLearning #LLM #OpenWeights #AgentAI #MoE #AITraining #ArtificialAnalysis
