---
title: Four Amazon Bedrock inference choices that affect cost
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/four-amazon-bedrock-inference-choices-that-affect-cost/
model: claude-code/sonnet
generated_at: '2026-11-12T23:09:30.025524'
score: 82
---

📌 Amazon Bedrock帳單悄悄變貴？四個常被忽略的推理設定

TL;DR：四個request層級設定，就能悄悄推高Bedrock帳單。

把prompt調到完美、應用邏輯也最佳化過了，Bedrock的帳單卻還在往上爬，問題往往不在模型或prompt本身，而是藏在幾個容易被忽略的request層級設定裡。

🤔 你沒換模型，帳單卻在變

AWS這篇文章指出，Amazon Bedrock的usage metadata裡，input和output token都會依照呼叫的模型與service tier計費，cache的讀寫各有獨立的token計數器，而reasoning token則算在output token裡。如果重複的system指令、工具定義或參考內容在cache到期後被重新處理，成本就會不知不覺往上疊。文章整理了四個會直接影響費用、但跟換模型或改prompt無關的request層級選擇：cache持續時間、service tier、reasoning effort，以及maxTokens。

🧩 cache TTL：時間拉長不代表便宜

Bedrock的prompt caching支援的Anthropic模型有5分鐘和1小時兩種TTL，支援的GPT-5.6模型則有30分鐘的最低TTL。除了這種需要主動設定cache控制的explicit caching，Bedrock也提供implicit caching，會盡量重用符合條件的prompt前綴，但不保證命中。

以Anthropic Claude Sonnet 5與Claude Opus 5在Bedrock上的費率為例：5分鐘的cache write是輸入費率的1.25倍，1小時write是2倍，cache read則只要0.1倍。這意味著5分鐘cache只要在5分鐘內被重用一次就能回本；如果同一個前綴的請求間隔經常超過5分鐘，5分鐘cache會不斷以1.25倍的費率重寫，這時1小時cache從第二次請求開始反而更便宜。

這裡有個容易踩到的坑：checkpoint的驗證順序是tools、system、messages，前面的區塊一旦變動，後面的checkpoint也會一起失效。AWS的測試團隊在Claude Sonnet 5上用1小時checkpoint跑了六次呼叫，只要改動一次system prompt或一次工具定義，那次呼叫就會零cache read、並重新寫入，等於cache完全沒發揮作用。多租戶情境下，文章建議在可快取的前綴前面加上租戶專屬的SHA-256雜湊，並在組裝prompt之前就先做好租戶授權驗證；如果業務上需要硬性的資料邊界，則應該讓不同租戶使用不同的AWS帳戶，而不是只靠雜湊隔離。

🧩 service tier：Flex不是每個模型都能用

Bedrock的Flex tier費率比Standard低，但支援度因模型而異。文章指出，Amazon Nova 2 Lite和OpenAI gpt-oss-120b的model card列為支援Flex，但Claude Sonnet 5與Claude Opus 5的model card則標示不支援。AWS團隊實際對Claude Sonnet 5發出Flex請求，結果直接收到ValidationException錯誤，而不是被悄悄降回Standard執行。如果應用邏輯允許用Standard做為後備，可以捕捉這個不支援的錯誤，重試一次default tier，但不該對所有ValidationException都無差別重試，因為請求格式錯誤也會丟出同樣的例外。

📊 實測數據：Flex省一半，reasoning effort省token但可能影響準確度

AWS團隊在Amazon Nova 2 Lite上，交錯送出200個default請求與200個Flex請求做對照。結果兩種tier處理的input/output token數量相同，全部400個請求都確實落在各自要求的tier上，延遲差異小到無法與雜訊區分。截稿時，us-west-2的Nova 2 Lite的Flex費率是Standard的一半，實際帳單也反映了這個差距。

至於reasoning effort，文章提醒reasoning token一律算作output token計費。Claude Sonnet 5和Claude Opus 5即使request裡沒帶thinking欄位，預設仍會用高強度的adaptive thinking，也就是說，如果應用是從Claude Sonnet 4.6直接搬過來、沒調整任何設定，會無聲無息開始被收thinking token的費用，而maxTokens這時限制的是thinking加上回覆文字的總和。Claude Haiku 5.5則預設medium。三款模型都支援low、medium、high、xhigh、max五個等級。

在一個基於Claude Opus 5的工具呼叫agent測試中，AWS團隊針對三個各有唯一正確答案的任務，在每個effort等級各跑了八次。另一個在Bedrock Samples「程式碼生成」工作負載上的測試顯示，low等級的median output token是676，high等級是743，差距在run-to-run的正常波動範圍內，而且兩個等級產生的程式都通過了測試。換句話說，降低reasoning effort能不能省錢、省了會不會傷到準確度，高度取決於任務本身，沒有放諸四海皆準的答案。

🎯 實務啟示

這四個槓桿的共通點是：它們都藏在request層級，換模型、改prompt都不會動到它們，但只要有一個設定不對，帳單照樣往上衝。具體作法上，文章建議用per-request的output token數、CloudWatch的OutputTokenCount指標、invocation log，再配合任務通過率，去驗證每個選擇的實際效果；cache盡量維持5分鐘預設，只有同一個前綴一小時內重複出現兩次以上、且間隔超過5分鐘時才換成1小時；reasoning effort則從低於high的等級開始測，只有品質測試證明真的需要high時才拉高，省下token卻讓任務失敗，不算省到錢。

🔗 來源
- 標題：Four Amazon Bedrock inference choices that affect cost
- 作者／機構：Sai Pavan Kasani，AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/four-amazon-bedrock-inference-choices-that-affect-cost/

#AmazonBedrock #AWS #LLMOps #CostOptimization #PromptCaching #ClaudeAI #CloudComputing #MLOps #GenerativeAI #AIInfrastructure
