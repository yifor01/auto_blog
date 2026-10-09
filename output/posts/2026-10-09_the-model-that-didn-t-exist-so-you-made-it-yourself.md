---
title: The model that didn't exist, so you made it yourself
source: HuggingFace Blog
url: https://huggingface.co/blog/building-with-ml-intern
model: claude-code/sonnet
generated_at: '2026-10-09T21:55:35.334078'
score: 102
---

📌 找不到的模型，自己叫Agent做一個：HuggingFace的ML Intern實驗

TL;DR：用agent自動規劃、訓練、評估並發布客製小模型，六個專案總成本都在幾十美元內。

當Hub上找不到你想要的那個「小」模型，多數人會將就用壓縮版湊合。HuggingFace的兩位工程師選擇了另一條路：在HuggingChat裡打開ML-intern，描述需求，隔天就拿到一個能在CPU上跑、99.7%輸出有效的客製模型，整個專案花費16美元。

🤔 從一個找不到的模型開始

作者想要Qwen-Image 2.1內建的prompt rewriter的小型版本。官方版本是9B參數，需要約20GB記憶體，而且要先「想」上千個token才會寫出第一段文字。Hub上能找到的，只有同一個9B模型的壓縮版本，沒有真正重新訓練過的小模型。於是作者直接把需求描述給ML-intern。

🧩 ML-intern怎麼運作：先報價，再動手

ML-intern的工作流程是：先規劃工作內容，在花錢之前先向使用者要預算，接著跑一個小規模測試驗證可行性，確認沒問題才進入正式訓練、評估，最後把結果發布到Hugging Face。每個專案都是從HuggingChat裡的一則訊息開始，結束時變成Hub上一個公開模型，評估結果就寫在model card裡。

作者分享了自己的提示工程心得：第一則提示最重要，從450字（第一個citrus模型）寫到後來近2000字（第六個專案），因為每個專案都會教她下一次該多寫什麼。所有七份提示都公開在GitHub的yvrjsharma/ml-intern-prompts。提示的固定結構包括：一行講清楚想法與動機；明確點名資料集、基礎模型、訓練腳本；把已經確認過的事實放進標題寫著「Verified facts, do not re-derive」的區塊，讓agent的預算花在真正的工作上而不是重新查證。她特別強調兩行提示最關鍵：一是要求訓練前先跑基礎模型的zero-shot分數作基準，否則「你會得到一個訓練好的模型，卻不知道它到底有沒有比原來好」；二是要求先用小規模（例如50步）做smoke test並檢查權重真的有變化，再付費跑正式訓練。提示最後會寫清楚交付項目與花費上限，例如「總花費上限USD 12，超過要先問我」。因為ML-intern每個任務都是從零預算開始，沒有授權就不會執行要花錢的工作，這個上限會被嚴格遵守；如果沒設定預算，agent則會依專案規模提出幾個方案讓使用者選。

📊 六天做了多個模型，花費都是個位數到幾十美元

| 專案 | 內容 | 關鍵數據 | 成本 |
|---|---|---|---|
| Pocket Rewriter | Qwen-Image 2.1 prompt rewriter縮小版 | 0.8B，99.7%輸出有效，token用量約為9B教師模型的四分之一 | 全專案約USD 16（含用9B模型標註8,797筆請求） |
| Citrus disease VLM | 柑橘病害診斷，微調Qwen3.5-2B | 335張測試照片，基礎模型準確率14.9%→微調後52.8%（2 epoch，1張A10G） | 約USD 1.90 |
| Huggy LoRA | FLUX.2 klein base 4B上的角色LoRA | 84張標註圖，第200步就on-model，第500步後風格開始外溢 | 約USD 7.60 |
| 相機視角LoRA | Qwen-Image 2.1的物件視角變換 | 1,030個物件x24角度=24,722張透明圖，最終461物件訓練/40測試，2,000步約90分鐘（1張A100） | 約USD 16（48個job） |
| Doodle-in LoRA | 用塗鴉取代後生成指定物件 | 6,042組訓練對+160組測試（40組來自23個未見過的類別），2,000步1小時38分（1張A100），偵測率67.5%、4.7秒/次編輯，未見類別65.0% vs 已見64.2% | 約USD 24（59個job） |

每個專案的資料集與模型都公開在Hub上，citrus模型甚至還做了一個Citrus Doctor App可以直接試用。

💡 把「驗證過的事實」寫進提示，比多寫需求更重要

作者提到，第一次嘗試（citrus模型）其實沒有寫「verified facts」區塊，ML-intern依然做出一個準確率比基礎模型翻三倍以上的成果；但後續專案把這個區塊補上之後，agent不需要重新摸索哪個訓練腳本剛加了透明圖支援、哪個GitHub issue讓備援訓練器變得不穩，工作效率明顯提升。這也呼應她反覆強調的兩個關鍵提示：沒有基準分數，訓練結果就沒有意義；沒有smoke test，正式訓練的錢可能白花。

🎯 對工程師的實務啟示

這整套方法把「自主訓練agent」的風險收斂成三個可控機制：預算上限、zero-shot基準、小規模smoke test。對任何想用agentic workflow做客製化小模型蒸餾的團隊來說，這組提示範本（尤其是「Verified facts, do not re-derive」與花費上限兩個設計）值得直接搬進自己的prompt。

🔗 來源
- 標題：The model that didn't exist, so you made it yourself
- 作者／機構：Yuvraj Sharma、Abubakar Abid，Hugging Face
- 連結：https://huggingface.co/blog/building-with-ml-intern

#HuggingFace #ModelDistillation #LoRA #AIAgent #FineTuning #OpenSource #QwenImage #MachineLearning #MLOps #GenerativeAI
