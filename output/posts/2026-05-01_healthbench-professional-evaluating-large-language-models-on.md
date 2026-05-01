---
title: "HealthBench Professional: Evaluating Large Language Models on Real Clinician Chats"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2604.27470
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-05-01T19:55:53.411399
---

📌 【OpenAI 最新研究】真實診間對話打擂台，LLM 真的贏過醫師了？

百萬臨床工作者已經把 ChatGPT 帶進診間，但「模型在真實醫療場域的對話表現」卻長期缺乏嚴格評估。當 AI 參與診斷、病歷書寫與研究，評估標準如果只靠單一 benchmark，我們真能相信它「對病人安全」嗎？

🤔 **日常診療真實對話，才是醫療 AI 的終極試煉場**

HealthBench Professional 直指當前醫療 AI 評估的盲點：大多數 benchmark 難以反映臨床工作者實際使用 LLM 的情境。OpenAI 團隊聚焦三個日常核心任務——照護諮詢、書寫與文書、醫學研究，並以真實醫師與 ChatGPT 的對話為基礎，建構一個開放、可追蹤、且具對抗性的評估框架。這不僅是測模型「能不能做」，更要測「在專業場域裡能否被信任」。

🧪 **真實醫師對話 x 三階段審查 x 對抗性測試**

本研究從 15,079 個範例中嚴格篩選並加權「對最新模型具難度」的案例，難度相對富集的樣本約增加 3.5 倍；約三分之一案例為醫師主動進行的對抗性測試。每則對話由三位以上醫師依據共同討論並反覆校正的評分規範獨立評分，確保評估的一致性與臨業合理性。同時，研究以「不設時間限制、專科對應、可上網查證」的人類醫師回覆作為強力基線，讓模型與人類在同一標尺下被檢驗。

☑️ **GPT-5.4 在 ChatGPT for Clinicians 拿下最高分，勝過其他模型與人類醫師**

- 最佳系統：GPT-5.4（ChatGPT for Clinicians 版本）
- 表現對象：勝過基線 GPT-5.4、所有其他比較模型，以及人類醫師組
- 評估場域：照護諮詢、文書與寫作、醫學研究三大真實任務
- 評分機制：醫師共同撰寫並反覆裁定評分規範，多階段審查

這一結果並非宣告「模型已全面超越臨床判斷」，而是指出：在嚴謹設計的真實對話評估中，特定系統版本的表現已能穩定超越人類基線，並在多面向任務中展現較高的一致性。

💡 **從「用 AI 產出內容」到「用 AI 建立可驗證的理解」**

本研究隱含的方法論轉向值得關注：高表現不只取決於模型能力本身，更取決於「如何與模型對話並檢驗其輸出」。評估設計強調可解釋性、邏輯連貫與臨業合理性，並透過對抗性測試主動暴露模型邊界。這意味，未來的醫療 AI 落地，將更依賴「人機協作的可稽核性」，而非單向的自動化。

⚠️ **以特定模型版本為基準、難度經過過濾，長期與跨情境穩定性仍待觀察**

研究坦承其設計取徑：以當前 OpenAI 前沿模型表現為難度依據，並刻意加權挑戰性案例；評估對象受限於特定模型版本與對話界面；長期表現、跨機構穩定性與真實臨床決策的因果影響並未測試。這是一個為「持續追蹤進步」而生的 benchmark，而非臨床部署的直接證據。

🎯 **開放評估框架讓進步可被看見，但「可信任」仍需人機共駕**

- HealthBench Professional 提供可公開追蹤的進度尺，讓產業與研究者能持續檢視模型在真實場域的演化
- 醫師參與設計與評分，使專業可解釋性與安全邊界具體化
- 實務上，應將高分視為「協作品質提升」的指標，而非「取代專業判斷」的授權

🔗 **論文連結**  
📝 HealthBench Professional: Evaluating Large Language Models on Real Clinician Chats  
👤 Rebecca Soskin Hicks, Mikhail Trofimov, Dominick Lim, Rahul K. Arora, Foivos Tsimpourlas @ OpenAI  
🔗 論文：https://arxiv.org/abs/2604.27470

你認為，當模型在真實醫療對話中表現勝過人類，我們該如何重新定義「人機協作的責任邊界」？歡迎留言討論 👇

#AI #Healthcare #LLM #OpenAI #MachineLearning #醫療科技 #模型評估 #人機協作
