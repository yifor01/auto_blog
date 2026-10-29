---
title: Can Frontier Models See Past a Decoy? Elorian Tests Visual Reasoning
source: Latent Space
url: https://latent.space/p/elorian/
model: claude-code/sonnet
generated_at: '2026-10-29T22:07:09.597930'
score: 89
---

📌 新基準DecoyCount考倒前沿模型：鏡子裡的蘋果都數不對

TL;DR：Elorian推出視覺推理模型Glimpse，搭配新基準DecoyCount揭露frontier models數數時依賴視覺捷徑的通病。

鏡子前放一顆蘋果，人一看就知道只有一顆；但在類似的測試裡，GPT-6 Astra、Gemini與Claude的正確率卻連五成都不到。

🤔 **從Google DeepMind出走，押注「視覺思考」**

Elorian今年4月以5500萬美元種子輪（Striker Venture Partners、Menlo Ventures與Altimeter Capital共同領投）從隱身模式中問世，本月發布首款視覺推理模型Glimpse，主打「從所見之物推理物理世界」的新型態視覺思考系統。為了驗證這個主張，Elorian與AI資料公司Mercor合作推出DecoyCount基準。CEO Andrew Dai並非新面孔，他2015年在Google任職期間就與Quoc Le共同發表過semi-supervised sequence learning論文，示範了後來被大型語言模型廣泛採用的pretrain-then-fine-tune做法，之後在Google DeepMind參與過GLaM MoE、PaLM 2與Gemini的開發，今年才離開Google共同創辦Elorian。

🧩 **把「沒看到」和「看錯了」分開檢驗**

DecoyCount專門測試語言模型是否「真的在數東西」，還是依賴視覺捷徑與替代性heuristic。它把vision（有沒有看到）與reasoning（看到之後判斷對不對）分開檢驗：鏡子前的蘋果，模型可能完全漏看是視覺問題，也可能把蘋果和鏡像都算成兩顆是推理問題；但多數基準只看最終數字，無法分辨錯誤出在哪一層。根據Dai，DecoyCount能揭露七種可解釋的計數失敗機制。

📊 **Glimpse 50.48%，GPT-6 Astra 43.17%**

根據論文，受測的frontier models在DecoyCount上全部低於50%正確率：表現最好的是GPT-6 Astra，43.17%；Gemini-3.8-flash為32.71%；Qwen3.8-max為28.31%；Claude-Fable-5.1為25.22%，這些數字是三次執行的平均。Elorian的Glimpse並未被納入該論文，但Dai透過email告訴Latent Space，Glimpse在1,660題的DecoyCount內部測試中拿到50.48%，是唯一跨過50%門檻的模型，比GPT-6 Astra高出約7個百分點；評測圖像與文字都被排除在Glimpse的訓練資料之外，污染檢查也沒有發現重疊。論文結論是：更強的通用推理能力，本身並不會自動遷移到對齊良好的視覺推理上。

💡 **圖像生成與編輯，是推理鏈的一部分**

Dai的設計理念源自心理學的「visual thinking」。人在思考空間或視覺問題時，會在腦中生成與編輯圖像，例如想像沙發放進客廳的樣子，或數桌邊人數時心裡一個一個劃掉。Glimpse的做法是把圖像生成與編輯當成推理鏈的一部分，而不只是輸出。這也讓Elorian與「world models」（例如World Labs的Atlas、Google的Genie 4）劃出界線：world models讓你對世界做「直接行動」，也就是3D模擬、導航與操作；Glimpse做的是「間接行動」，用視覺推理輔助判斷或工作流程，例如審核使用者上傳影片是否違規，不需要3D渲染就能做到。Dai也舉了倉儲機器人數箱子裡零件的例子：一個12格托盤可能只裝了10個零件，標示24入的包裝也未必剩24個，只靠預期去數會在真實場景中出錯，Glimpse被設計成把計數結果建立在可見證據上，而非依賴容易被誤導的表面線索。Elorian還在機器人相關的WGO Bench與ERQA兩項基準上聲稱表現與frontier models相當甚至更好，而且成本更低。

⚠️ **比較條件並非完全對等**

需注意公平性：Glimpse的50.48%來自單次執行，沒有agent或工具輔助；論文中六個frontier models則是各自三次執行取平均，嚴格來說並非完全對等的比較條件。Dai本人也承認，人類與機器之間仍有巨大差距。

🎯 **拆解視覺錯誤來源，再決定怎麼修**

如果你在打造需要「數東西」或做視覺判斷的agent，例如倉儲盤點、內容審核或品管，別只看模型在單一數字上的準確率。DecoyCount這種拆解vision與reasoning錯誤來源的評測方法值得借鏡：先搞清楚模型是「沒看到」還是「看錯了」，才能決定該換模型架構，還是調整prompt策略。

🔗 **來源**
- 標題：Can Frontier Models See Past a Decoy? Elorian Tests Visual Reasoning
- 作者／機構：Latent Space
- 連結：https://latent.space/p/elorian/

#VisualReasoning #ComputerVision #Benchmark #AGI #MultimodalAI #Elorian #Glimpse #DecoyCount #LLMEval #AIResearch
