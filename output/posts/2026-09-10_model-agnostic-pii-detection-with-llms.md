---
title: Model-agnostic PII detection with LLMs
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/model-agnostic-pii-detection-with-llms/
model: claude-code/sonnet
generated_at: '2026-09-10T20:08:46.878720'
score: 82
---

📌 換模型不用重訓：AWS的模型無關PII偵測器怎麼設計

TL;DR：AWS釋出以LLM為核心的可設定PII偵測器，換模型或加新實體類型只需改提示詞，不必重新標註訓練。

拿一份客服對話紀錄去微調模型，你以為在教它學新任務，實際上可能同時餵給它使用者的身分證字號、銀行帳號與生日。等到有人用一句巧妙的提示把它問出來，洩漏的就是真實個人資料。

🤔 **傳統token classification工具卡在哪**

PII很少乖乖待在制式欄位裡，它藏在客服逐字稿、HR紀錄、聊天紀錄，以及團隊拿來微調的長篇自由文字欄位中，格式混亂且多語言。慣用做法是雙向的token分類模型，也就是在訓練時就把每個token標記固定的PII類型的transformer標註器。問題在於，像員工編號或加密貨幣錢包地址這類客製化微調語料常見的領域專屬識別碼，天生就不在這套固定schema範圍內；要新增，就得重新標註、重新訓練，而且模型被鎖死在單一模型與單一部署方式上。

🧩 **把LLM當成可替換元件**

AWS這篇文章介紹的偵測器把語言模型當成可設定、可替換的元件：將輸入文字包進一段指示中，定義要偵測的PII實體與輸出格式，模型回傳結構化的偵測實體列表。這帶來兩個關鍵設計自由度：第一是模型本身，決定準確度、延遲與成本，可以選Amazon Bedrock上的前沿模型，也可以選單一GPU上就能跑的小型開源模型；第二是實體集合，定義什麼算PII，新增或移除一種識別碼只需改一行指示文字，不必重新訓練或重新部署。

🧩 **架構拆成四塊：schema、backend、offset還原、呼叫序列**

偵測器由四部分組成。核心是一份系統提示範本（schema），裡面定義了十五個實體類別，每個類別附一行定義、一份「不要標記」清單，並可選擇加入few-shot範例。模型被要求以JSON列表回應，每個物件帶實體類型與找到的原文文字，但不含字元位移，因為LLM無法可靠地產生精準offset；這一步交由後處理層還原成有位置座標的完整span，並去除重複。因為判斷邏輯全在提示詞裡，backend可以自由選擇：套件內建一個名為Inferencer的輕量介面（輸入訊息、輸出文字），並提供一個透過Converse API封裝的Amazon Bedrock轉接器，因此同一套偵測器可以打在Bedrock上的受管模型，也可以打在自架於Amazon EC2上的開源模型。

🧩 **怎麼跑：從虛擬環境到一行換模型**

該偵測器以pii-detector套件形式釋出於sample-llm-pii-detection repo。使用方式是建立虛擬環境並安裝boto3，設定PYTHONPATH讓pii_detector模組可解析，並將Boto3指向已啟用Amazon Bedrock存取的帳號與地區（建議用IAM角色或SSO設定檔而非長期存在的靜態金鑰）。repo附有可直接執行的examples/detect.py範例。實際使用時，只需用任一Amazon Bedrock Converse模型ID（例如amazon.nova-lite-v1:0或mistral.mistral-large-3-675b-instruct）建立Inferencer，包進PiiDetector，呼叫後就能拿到帶精確字元offset的偵測結果，可直接餵給下游的遮罩（redaction）流程。因為Amazon Bedrock是全代管服務，沒有基礎設施需要管理，按token用量計費。

📊 **評測基準：涵蓋八種語言的五個公開語料庫**

評測採用五個來自Hugging Face的公開PII語料庫，每個資料集抽樣約一萬筆，合計四萬九千三百六十五筆紀錄、二十二萬兩千一百一十四個ground-truth核心span，涵蓋德文、英文、西班牙文、法文、印地文、義大利文、荷蘭文與泰盧固文八種語言，領域從多語言合成個人檔案到英文HR與客服文件都有。文章將此偵測器與另外八個LLM-based偵測器（包括OpenAI PrivacyFilter）放在同一套ground-truth下比較，比對方式是預測span與ground-truth的(start, end, label)精準重疊（IoU=1.0），以Precision、Recall、F1評分。

⚠️ **跨資料集比較沒有想像中直觀**

文章特別提到，把這些偵測器放在同一批資料上比較，比看起來難，因為不同工具、不同資料集的標籤本身就對不齊，這也是為何後製的offset還原與去重邏輯格外重要。

🎯 **實務啟示**

如果你的微調語料本身就是PII的高風險來源，這種「schema即提示詞」的設計讓你不必為了新增一個內部識別碼類型就重新標註整個訓練集；換一顆更便宜或更快的模型也只是改一行模型ID，值得作為微調前資料清洗流程的參考架構。

🔗 **來源**
- 標題：Model-agnostic PII detection with LLMs
- 作者／機構：Christophe Dupuy, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/model-agnostic-pii-detection-with-llms/

#PII #LLM #AmazonBedrock #DataPrivacy #FineTuning #NLP #ResponsibleAI #DataRedaction #MachineLearning #AWSML
