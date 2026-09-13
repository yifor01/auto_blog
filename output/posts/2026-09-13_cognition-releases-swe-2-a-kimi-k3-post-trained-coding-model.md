---
title: 'Cognition Releases SWE-2: A Kimi K3 Post-Trained Coding Model That Matches
  Fable 5.1 on FrontierCode at 64% Lower Cost'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/12/cognition-releases-swe-2-a-kimi-k3-post-trained-coding-model-that-matches-fable-5-1-on-frontiercode-at-64-lower-cost/
model: claude-code/sonnet
generated_at: '2026-09-13T19:39:22.873945'
score: 88
---

📌 SWE-2：3T規模RL逼近旗艦，卻只能鎖在Devin裡

TL;DR：Cognition以強化學習後訓練2.8兆參數的Kimi K3打造SWE-2，FrontierCode成績逼近Fable 5.1、成本卻低64%，但無開放權重、只能在Devin內執行。

如果把強化學習的訓練規模直接衝上兆級參數的底座模型，程式碼代理人會變成什麼樣子？Devin背後的公司Cognition給出了一個具體答案，但這個答案目前只租給你用，不賣斷。

🤔 從SWE-1.7到SWE-2，規模跳了將近3倍

Cognition發布SWE-2，是公司目前最強的程式碼模型，以強化學習(RL)對Moonshot AI開源的2.8兆參數模型Kimi K3進行後訓練而成。SWE-2延續了SWE-1.7的基礎建設與訓練配方（SWE-1.7是以Kimi K2.7後訓練而成），這次底座模型參數量提升到將近前代的3倍。Cognition表示，即便底座已經是K3，RL訓練仍能在多項benchmark上再加5到6分，顯示後訓練階段還有明顯的加分空間。這也是Cognition第一個支援可選推理強度(reasoning-effort)等級的模型，三個等級是在同一次RL訓練中一起練出來的。

🧩 一套演算法，同時練出三種成本／效能組合

過去若要提供多種推理強度，往往得分別訓練或事後調整。SWE-2的做法是讓每個推理等級各自帶有一個成本懲罰項，寫成獎勵函數R等於S減去lambda乘以C，其中S是任務是否成功的二元訊號，C則綜合了推理成本（美元）與rollout時間。Cognition證明，只有線性懲罰能讓這個目標函數單純取決於平均成本與解題率；每個推理等級的lambda，則設定為該等級在基礎模型Pareto曲線上的局部斜率，讓等獎勵線與效能前緣相切，這樣一來獎勵想要提升，就只能靠把整條前緣往上推。另外Cognition也分享了自SWE-1.6沿用至今的長度加權獎勵基線：由於梯度大小和rollout長度高度相關，group baseline改用token數加權計算(sum(R×L)除以sum(L))，在消融實驗中能讓推理與訓練之間的KL散度更低、訓練更穩定，且不需要額外算力。在rollout服務層面，prefill delayer會把相近請求批次處理，讓每張GPU的TPM與每個請求的TPS提升10%到20%；搭配DSpark推測解碼加速rollout，草稿模型透過SpecForge重新訓練，讓接受長度延長15%，並與策略模型一起線上訓練；NVFP4與FP8核搭配量化感知訓練(QAT)，則讓記憶體用量與訓練推論落差都低於SWE-1.7。資料端則把RL環境數量擴增至三倍，加入指令遵循的覆蓋任務，並用先前的SWE-2 checkpoint建立飛輪，修補驗證器裡的偽陽性與偽陰性。

📊 FrontierCode差1分，但Terminal-Bench 4輸了30分

在FrontierCode 1.1 Main上，SWE-2拿下50.0%，距離Fable 5.1僅差1分，成本卻低64%；在Terminal-Bench 2.1上領先，且在每一項指標上都超越K3基礎模型；與GPT-6 Astra相比差距僅幾分，成本卻只要對方的四分之一。不過Terminal-Bench 4是明顯弱點，落後Fable 5.1與GPT-6 Astra約30分（需注意FrontierCode是Cognition自家benchmark，對手成績也來自Cognition自己的評測環境）。SWE-2也修正了SWE-1.7在簡單任務上過度探索的問題，官方稱之為「focused exploration」：在FrontierCode 1.1 Main上，SWE-2 medium的分數高於SWE-1.7，但回合數減少58%、成本降低81%；平均每次任務的步驟數從SWE-1.7的127步，降到medium的53步、high的80步、max的98步；SWE-2 medium做出第一次實質編輯的中位數步驟數是18步，SWE-1.7則要48步。Cognition並指出三種行為模式的改善：更完整的端對端測試覆蓋、工具受阻時更懂得變通，以及被質疑時會重新推導結論而不是重複主張原答案。在信任度測試上，SWE-2對145個涉及中國政治敏感議題的問題整體通過率98.0%（英文99.8%、簡體中文95.2%、繁體中文99.1%），另一項針對不同客戶情境框架的漏洞測試中，沒有任何框架讓任何模型出現統計上顯著的行為變化。

💡 成績亮眼，但驗證管道是封閉的

這裡值得留意的落差在於：所有對比數字，無論是SWE-2自己的還是對手的，都是Cognition在自家harness與benchmark下跑出來的，缺乏第三方復現。技術上，把RL post-training擴大到多兆參數規模、並用Pareto斜率去校準多等級推理成本，是相當紮實的工程設計；但這些成果目前無法被外部社群直接檢驗。

⚠️ 沒有開放權重，也沒有獨立API

SWE-2無法部署在自己的基礎設施上，也沒有獨立對外的API，只能透過Devin使用：目前是Desktop與CLI，Devin Web與Fusion正在推出中。對於希望自架模型、或需要脫離特定產品使用API的團隊來說，這是硬性限制。

🎯 實務啟示

即使無法直接用到SWE-2本身，這套「單次RL訓練同時對齊多個成本／效能等級」的做法，值得做agentic coding模型後訓練的團隊參考；但在評估是否採用SWE-2作為工作流程一環之前，得先接受它綁死在Devin生態系裡這個前提。

🔗 來源
- 標題：Cognition Releases SWE-2: A Kimi K3 Post-Trained Coding Model That Matches Fable 5.1 on FrontierCode at 64% Lower Cost
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/12/cognition-releases-swe-2-a-kimi-k3-post-trained-coding-model-that-matches-fable-5-1-on-frontiercode-at-64-lower-cost/

#Cognition #SWE2 #Devin #KimiK3 #ReinforcementLearning #CodingAgent #LLM #AgenticAI #FrontierCode #AIcoding
