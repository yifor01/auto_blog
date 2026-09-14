---
title: 'The generative AI customization spectrum: From prompt engineering to custom
  models on AWS'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/the-generative-ai-customization-spectrum-from-prompt-engineering-to-custom-models-on-aws/
model: claude-code/sonnet
generated_at: '2026-09-14T21:09:47.701252'
score: 78
---

📌 從提示工程到自訓模型:AWS 生成式 AI 客製化八階梯

TL;DR：AWS 提出一套 8 步驟決策框架,幫工程團隊判斷該用提示工程、RAG、微調還是從頭訓練,避免過度投資或投資不足。

有了 Amazon Bedrock 就能叫用 Anthropic Claude、Amazon Nova、Llama 等基礎模型,但「能叫用」跟「能把它用好」是兩件事。該寫更好的提示詞,還是接上檢索增強生成(RAG,Retrieval Augmented Generation)?該微調,還是直接從頭訓練?選項太多反而讓人無從下手,而選錯代價不小:文章直言,不少團隊直接跳去微調,結果一個結構清楚的提示詞下午就能解決;也有團隊困在提示工程裡好幾週,其實用例早就明顯需要領域訓練資料。這兩種誤判燒的都是真金白銀的算力、真實的時間與團隊在關係人面前的信任。

🧩 一道有三層樓的階梯,原則是「先簡單,不夠再升級」

這套「生成式 AI 客製化光譜(customization spectrum)」把八個步驟分成三大類:

USE(用):不動模型,只改你跟它說話的方式。
- Step 1:直接呼叫基礎模型,零客製化,適合摘要、翻譯、腦力激盪、程式碼生成等對準確度要求不高的通用任務。
- Step 2:提示工程,加入系統指令、few-shot 範例、chain-of-thought 推理。文章建議用五個要素組織每個提示詞:明確的指令(用動詞、指定範圍)、足夠的上下文(現況、依賴關係、限制)、具體需求(功能與非功能)、輸出格式,以及品質指標(預期行為、邊界情況、效能目標)。常見的錯誤是指令堆太多或塞了一堆沒有針對性的上下文,提示詞的詳細程度應該跟任務複雜度成比例。

ENHANCE(強化):在模型周圍加東西,權重不動。
- Step 3:用 Amazon Bedrock Knowledge Bases 做 RAG,在推論時餵給模型你自己的私有、常更新或領域特定資料,降低幻覺但不需重新訓練。
- Step 4:對高頻重複查詢的提示前綴(系統指令、few-shot 範例、大量上下文)做快取,降低延遲與成本但不改變輸出品質。
- Step 5:知識蒸餾(distillation),把大型「老師」模型的知識轉移給小型「學生」模型,在已驗證過的特定用例上用更低成本、更低延遲拿到近似品質。

TRAIN(訓練):真的動模型本身。
- Step 6:用你自己標註過的資料做微調(fine-tuning)。
- Step 7:用大量未標註語料做持續預訓練(continued pre-training),擴充模型的基礎知識。
- Step 8:用 Amazon Nova Forge 從零打造完全客製化的模型。

文章給出的核心原則很直白:從 Step 1 開始,只有在目前這一步無法滿足準確度、延遲或領域需求時才往上升級,而多數工作負載根本不需要超過 Step 3。

💡 用主廚比喻串起整套光譜,也給每一步都定義了「該升級的訊號」

文章用一個主廚比喻貫穿八個步驟:模型就是主廚,寫更精準的點單(提示工程)幾乎零成本,但送主廚去進修(微調)要花掉數月投資與產能損失。蒸餾的比喻則是:「主廚的品嚐菜單很完美,但一盤要花 45 分鐘、食材成本高昂;把三款最受歡迎的菜教給二廚,10 分鐘出餐、成本只要三分之一。」

每個步驟也對應明確的升級訊號,例如:輸出太籠統、格式錯誤或不符合領域慣例,就該從 Step 1 升到 Step 2;提示詞超過約 2000 個 token、仍在幻覺領域事實、或需要模型本來就沒有的知識,就該升到 RAG;檢索延遲超標、上下文視窗爆掉、或模型還是無法正確推理檢索到的內容,就該考慮快取或更換模型規模;已經用大模型驗證過品質,但需要更便宜、更快或能部署到邊緣裝置,就是蒸餾的時機。這套光譜也對應到具體的 AWS 服務:Amazon Bedrock、Amazon SageMaker 與 Amazon Nova Forge,分別覆蓋不同階段。

🎯 實務啟示

這篇文章本身沒有新技術,價值在於把「該選哪種客製化手段」這個常被憑感覺決定的問題,變成一套有明確升級訊號的檢查清單。對工程團隊來說,最實際的行動是把這套光譜當成技術決策前的一道關卡:先問「Step 1、2 真的不夠嗎」,再決定要不要往 RAG、快取、蒸餾甚至微調投入資源,而不是憑團隊的技術偏好或流行趨勢直接跳級。

🔗 來源
- 標題：The generative AI customization spectrum: From prompt engineering to custom models on AWS
- 作者／機構：Bhavya Sruthi Sode(AWS Machine Learning Blog)
- 連結：https://aws.amazon.com/blogs/machine-learning/the-generative-ai-customization-spectrum-from-prompt-engineering-to-custom-models-on-aws/

#AWS #Bedrock #PromptEngineering #RAG #FineTuning #KnowledgeDistillation #SageMaker #NovaForge #GenAI #LLMOps
