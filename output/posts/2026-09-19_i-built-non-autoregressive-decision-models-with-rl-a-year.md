---
title: I built non-autoregressive decision models with RL a year ago
source: Hacker News
url: https://laya.convaiinnovations.com/
model: claude-code/sonnet
generated_at: '2026-09-19T19:26:48.731086'
score: 104
---

📌 搶先Jev一年的開源決策模型:Laya

TL;DR:他一年前就發表同概念論文與開源模型,如今推出更快版本迎戰爆紅的Jev。

這幾天AI圈都在討論一種「不是自迴歸、不生成文字、只吐出結構化機率」的新架構,聽起來像是憑空冒出的突破。但開發者 nandakishor_ml 說,這件事他一年前就做過了。

🤔 為什麼用LLM做決策是殺雞用牛刀

現代AI pipeline有個常見的效能黑洞:用生成式LLM去回答本該簡單、結構化的問題。像是客服單該分派到哪個部門、一封email是不是釣魚信、一段prompt是不是想做jailbreak或prompt injection、緊急程度該打幾分(0到3)。這些問題丟給8B、70B甚至frontier等級的生成式LLM處理,等於是用500到2000毫秒的token streaming時間、真金白銀的推論成本,換來一段還要自己寫regex或JSON parser去解析的自由文字。更麻煩的是,LLM很愛生成「假自信」:輸出「confidence: 0.95」時,它其實只是在預測聽起來很有把握的token,背後沒有任何數學上的校準(calibration)。作者認為,這類任務需要的是人腦System 1式的反射決策:30到35毫秒內給出誠實、經過校準的機率。

🧩 三個決策原語與三個checkpoint

作者去年3月發表的arXiv論文(arXiv:2503.23303)用PPO在sequence representation上訓練模型,針對垂直領域的銷售對話輸出逐輪的轉換機率(0.0到1.0),同步釋出模型權重(sales-conversion-model-reinf-learning)、開放資料集(saas-sales-conversations)與PyPI套件。今年9月,他又發表第二篇論文(arXiv:2510.01237),把「由強化學習引導的schema-based決策」框架系統化。

這次推出的Laya,把整個做法收斂成三種決策原語,對任何狀態(純文字、email、工單或JSON文件)做單次前向傳播即可完成判斷:

- choice:從一組候選字典中選一個選項,回傳選中的key、跨所有選項的機率分布,以及校準過的信心分數。
- score:把狀態放到一個順序量表(0、1、2……)上,回傳期望等級、各等級分布與信心。
- noul:直接的布林問題,回傳校準過的P(true)(0.0到1.0,P(false)=1-P(true))。

由於輸出空間純粹是機率與數字,模型不會生成文字,也就不可能出現hallucination,更不會有格式錯誤或JSON壞掉的問題。

Laya釋出三個專門化checkpoint,統一放在同一個Hugging Face repository下:

| Checkpoint | 骨幹 | 參數量 | Context | 主要強項 |
|---|---|---|---|---|
| laya | ModernBERT-large | 421M | 512 | 英文文字分類、guardrail、email分流 |
| laya-multilingual | mmBERT-base(256k詞表) | 322M | 1024(最高8k) | 100+語言、速度快2.2倍、跨語言NLI |
| laya-typed-decisions | ModernBERT-large | 421M | 1024 | Agent可觀測性、客服、發票處理、資安警示(準確率0.766) |

透過Hugging Face的allow_patterns,SDK可以只下載需要的subfolder,例如只抓英文模型(約808MB)或多語言子資料夾(約647MB),不必整包下載2.5GB。

⚠️ 信心分數會騙人:不同文字系統的災難性失效

作者在MASSIVE benchmark(20個選項,隨機基準線0.050)上對51種語言做了掃描,結果顯示英文模型一旦離開拉丁字母系統就會全面失準:高棉語準確率0.000,但平均信心高達0.952;亞美尼亞語準確率0.050(等於隨機猜),信心卻有0.885;希伯來語準確率0.060、信心0.964;孟加拉語準確率0.080、信心0.945;印地語準確率0.100、信心0.941。整整51種語言掃下來,英文checkpoint的平均信心從未低於0.885,不管實際準確率是82%還是0%。這代表信心分數本身完全無法提示「這個模型看不懂這段文字」,該用哪個checkpoint必須在做前向傳播之前就決定好,而不是靠模型自己的confidence把關。

為此Laya內建一個Router,能辨識22種文字系統(天城文、CJK漢字、西里爾字母、阿拉伯文、希伯來文、泰米爾文、泰文等)並分析拉丁停用詞分布:一般英文文字偵測開銷只要0.09毫秒,天城文/印度語系文字0.54毫秒,大型200列巢狀JSON文件0.73毫秒。相較於33毫秒的前向傳播,路由開銷可以忽略不計(<2%)。搭配Router(preload=True)把所有checkpoint常駐在VRAM/RAM中,還能完全消除語言切換時7到10秒的冷啟動代價。

💡 蹭熱度,還是站在自己一年前的肩膀上

九月,由前OpenAI「ChatGPT共同發明人」Diogo Almeida創辦的TypeSafe AI推出了Jev,主打的正是同樣的非自迴歸、輸出校準信心分布的決策概念,取名RLCD(Reinforcement Learning for Calibrated Decisions),定價每百萬input token 0.042美元,回應時間約150毫秒。但作者指出,Jev沒有附上技術論文,沒有開放權重,也沒有公開訓練資料集。相比之下,他把這一年的經驗全部重做一遍,做出完全開放、跑在雙向編碼器(bidirectional encoder)上的Laya:單張GPU上32.8毫秒即可完成推論(批次處理時每題僅7.2毫秒),號稱比Jev快6到8倍,支援100多種語言,沒有API訂閱費用,並以Apache 2.0授權完全開源。

🎯 實務啟示

如果你的系統裡有大量「分類/評分/是非題」式的判斷,卻在用GPT等級的生成式模型硬解,這篇分享值得參考:先問自己是否真的需要生成文字,還是只需要一個誠實、快速、可校準的機率。另一個更重要的提醒是,confidence gating並不安全,當輸入語言或格式超出模型訓練分布時,模型可能依然自信滿滿地給出錯誤答案,路由與語言偵測必須做在推論之前,而不是事後靠信心分數把關。

🔗 來源
- 標題:I built non-autoregressive decision models with RL a year ago
- 作者/機構:nandakishor_ml(Hacker News)
- 連結:https://laya.convaiinnovations.com/

#NonAutoregressive #DecisionModels #ReinforcementLearning #ModernBERT #OpenSource #LLMRouting #Calibration #MachineLearning #NLP #HuggingFace
