---
title: Microsoft’s Mustafa Suleyman says its AI outperforms doctors on hard cases
  as he chases ‘medical superintelligence’
source: TechCrunch AI
url: https://techcrunch.com/2026/10/22/microsofts-mustafa-suleyman-says-its-ai-outperforms-doctors-on-hard-cases-as-he-chases-medical-superintelligence/
model: claude-code/sonnet
generated_at: '2026-10-22T20:56:53.768080'
score: 87
---

📌 微軟 MAI-DxO：複雜病例診斷準確率 83% 對比醫師 36%

TL;DR：微軟在《Science》發表的研究顯示，其多代理診斷系統在複雜病例模擬中的準確率遠高於個別醫師，但數據也顯示多數進步其實來自底層模型本身的提升。

🎣 83% 對 36%，這是微軟這篇發表於《Science》的研究裡，兩組受試者在同一批複雜病例上的診斷準確率。一組是微軟的多代理系統，另一組是獨立看診、可查閱參考資料的一般內科與基層醫師。Microsoft AI 執行長 Mustafa Suleyman 稱這個結果是邁向「醫療超智慧（medical superintelligence）」的一步。

🤔 這是什麼系統

這套系統叫 MAI-DxO（簡稱 DxO），運作方式是協調多個 AI agent，模擬一個醫師會診小組：這些 agent 會詢問病患、安排檢驗、再彼此辯論診斷結果。測試用的病例取自《新英格蘭醫學期刊（NEJM）》裡公開的複雜病例。報導特別提醒一個對照上的限制：這類複雜度的病例現實中通常由專科醫師或醫療團隊處理，而不是由個別基層醫師單獨應對，但這次比較的對象正是後者。

🧩 多家模型都測過，但 OpenAI 的模型表現最好

微軟用多家公司的模型測試 DxO，包括 OpenAI、Google、Anthropic、Meta 與 DeepSeek，其中以 OpenAI 的 GPT-5 與 GPT-5.5 搭配 DxO 表現最佳。

📊 DxO 帶來的提升，在不同模型與病例類型上差異很大

| 模型／情境 | 單獨使用準確率 | 搭配 DxO 準確率 | 備註 |
|---|---|---|---|
| GPT-5，複雜病例 | 78.9%（約 8,400 美元／病例） | 約提升 4 個百分點 | DxO 把成本降了約 3,000 美元 |
| GPT-5.5（2026 年 4 月發布），複雜病例 | 72% | 近 87% | 成本略為下降 |
| GPT-5 / GPT-5.5，急診病例 | 約 85% | 幾乎沒有改善 | 準確率與成本都接近持平 |
| Gemini 2.5 Flash，複雜病例 | 46.4% | 近 69% | 提升幅度最大的案例之一 |

整體而言，DxO 在複雜病例、以及搭配能力較弱的模型時，帶來的提升最明顯；在急診病例上幾乎看不到改善。

💡 進步主要來自底層模型，而非協調系統本身

研究本身的數據指向一個值得注意的結論：多數的準確率提升，其實來自底層 AI 模型本身的能力進步，DxO 的多代理協調機制是疊加在上面的額外加分。微軟的研究人員也提到，隨著模型越接近理論準確率上限，準確率提升幅度自然會收斂變小；以 Gemini 2.5 Flash 和更強模型之間的差距為例，這個差距本身就比 DxO 帶來的提升幅度更大。微軟的官方說法則是，DxO 的協調機制有助於同時處理「準確率」與「成本」這兩個更廣泛的最佳化目標。

⚠️ 比較基準與未來驗證方式

這次研究用的是模擬情境，而微軟接下來計畫把驗證拉到真實臨床場景：透過與波士頓 Beth Israel Deaconess Medical Center 的新合作，讓同意參與的病患在接受標準治療（分級分類、專科時間、治療、檢查、是否可出院的判斷）的同時，平行讓 DxO 產生建議，再比較兩者的結果。Suleyman 也提到微軟正與 Mayo Clinic 合作訓練一個醫療領域的基礎模型，計畫明年發布，他認為醫療相關模型能力會在未來 24 到 36 個月內有「一個數量級」的提升。值得留意的是，Google 本月也在《The Lancet》發表了針對自家 AMIE 對話式診斷 AI 的真實世界急診評估研究，同樣與 Beth Israel 合作，顯示這類「多代理／對話式診斷 AI 對比臨床醫師」的驗證正在變成業界的共同賽道。

🎯 實務啟示

對做醫療應用的工程團隊而言，這份研究提供的更實用訊號可能不是「83% 對 36%」這個標題數字，而是其背後的結構：多代理協調系統的價值，很大一部分取決於它疊加在怎樣的底層模型之上，而且在急診這種高時間壓力、資訊不完整的場景，協調機制帶來的邊際收益明顯比在複雜病例上小得多。評估類似架構時，拆解「底層模型貢獻」與「協調層貢獻」會比只看總體準確率更有參考價值。

🔗 來源
- 標題：Microsoft's Mustafa Suleyman says its AI outperforms doctors on hard cases as he chases 'medical superintelligence'
- 作者／機構：Rebecca Bellan, TechCrunch
- 連結：https://techcrunch.com/2026/10/22/microsofts-mustafa-suleyman-says-its-ai-outperforms-doctors-on-hard-cases-as-he-chases-medical-superintelligence/

#Microsoft #MAIDxO #MedicalAI #AIinHealthcare #MustafaSuleyman #GPT5 #ClinicalAI #HealthTech #MultiAgentSystems #AIdiagnosis
