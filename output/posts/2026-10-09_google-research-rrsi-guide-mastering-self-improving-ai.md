---
title: 'Google Research RRSI Guide: Mastering Self-Improving AI Agents'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/08/google-research-rrsi-guide-mastering-self-improving-ai-agents/
model: claude-code/sonnet
generated_at: '2026-10-09T21:55:35.334242'
score: 102
---

📌 【Google Research】讓LLM Agent改寫自己，又不讓它作弊的RRSI

TL;DR：拆解RRSI如何用統計門檻與洩題偵測，防止Agent自我改寫harness時overfit評測。

如果讓一個LLM agent自己改寫自己的prompt、工具、記憶甚至子agent，而且改寫的對象是凍結不動的底層模型，它要怎麼知道自己是真的變強，還是只是運氣好或是在作弊？MarkTechPost的這篇教學，直接把Google Research的RRSI（Regularized Recursive Self-Improvement）方法裡決定「哪些修改該留下來」的核心規則，用純Python跑了一遍。

🤔 完整迴圈很重，但決策規則可以單獨拆出來跑

RRSI完整的運作迴圈，是用Claude Opus（跑在Vertex AI上）起草修改方案，再放進Docker benchmark裡評分，這不是一般筆記本環境能跑的規模。但教學作者指出，真正承載論文核心想法的部分，其實是「決定該留下哪些修改」的規則，這部分是單純的Python函式，可以直接拿來操作、驗證。作者還搭了一個模擬agent（成功率是harness能力減去任務難度的邏輯函數），因為自己掌握「真實效果」，所以能拿來對照RRSI的判斷是否正確。

🧩 RRSI怎麼分辨「真的變強」和「剛好這次運氣好」

- 兩個核心指標：S是所有任務、所有trial的平均reward；C是每個trial平均花掉的policy token數。一個容易被忽略的細節是遺漏trial的處理方式：如果某個候選方案在最難的任務上直接crash，把缺失的trial「丟棄不算」會讓分數從0.500變成虛假的0.750，看起來像是進步；RRSI的作法是把每個缺失trial算作reward為0，分母維持原樣，分數依然是0.500，讓crash不可能偽裝成改善。像Harvey LAB這類用評分表（rubric）打分的任務集，則改用加權reward，S變成「所有評分項目中通過的比例」而不是任務平均分的平均。
- 校準噪音帶（calibrate）：對同一個未改動的harness，在40個任務、每個2次trial的設定下重複評估6次，分數本身就會自然飄動0.113。delta定義為兩次重複評估之間差值的2倍標準差；80個trial時delta約0.108，3,200個trial時delta降到約0.013，落在論文回報的0.004~0.020範圍內。任何小於delta的進步，在統計上都和「重跑同一個harness」沒有區別。
- 選擇演算法（Algorithm 2／judge函式）：分數低於floor（史上最高分減去delta）的候選直接淘汰；進步幅度超過delta的候選，還得符合成本規則，相對token成本增加必須小於0.10加上40倍的進步幅度（例如進步6分、token多20%可以接受，但進步3分、token多150%就不行）；落在delta區間內的分數視為平手，改用shaped score（100倍進步減15倍成本變化，外加「從未被採用過的結構性元件」小額加分）決定取誰；另外還有一個domain guard，只要觸發，不管分數多高都會被否決。
- select_round把judge套用在同一輪所有候選上，只保留分數最高且通過審核的那一個。作者給的例子裡，分數最高的候選因為3分進步換不回150%的token成本而落選，被critic直接擋掉的候選根本沒進入評分，最終贏家甚至讓incumbent分數略降了半分，但token成本砍掉五分之一。
- 關鍵保險：floor（S*）只會上升，錨定在「史上最高分」而不是「目前的incumbent分數」，這樣一連串「更便宜但略差」的交換，就不會在很多輪之後把分數慢慢拖垮。
- 退火式編輯預算（edit_budget）：用cosine schedule從b_max退火到b_min，預設前8輪每個候選最多4處協同修改，接下來5輪降到3處，最後7輪降到2處；公式的上界要到t=T+1（跑完之後再多一步）才會真正降到最小值1，這是讀公式時很容易忽略的細節。
- 兩層critic：第一層是不呼叫模型的確定性檢查，比對憑證字串與domain自訂的denylist，能擋掉背答案（記住task_007的答案）、直接讀取預期輸出、洩漏API key、或空白diff這幾種情況；第二層才是交給Claude做意圖審查。教學作者也抓到一個實務上的坑：如果沒設定RRSI_VERTEX_PROJECTS環境變數，rrsi.llm.generate會在try區塊外計算「索引 mod 專案數」，直接丟出ZeroDivisionError，導致程式原本設計好的友善設定錯誤訊息根本不會被看到。
- normalize會檢查每個宣稱的元件標籤是否真的有diff證據支持，避免一個單純的prompt微調冒充成「新技能」去搶novelty bonus。
- history把每次編輯寫成一筆JSONL紀錄，衍生出四種摘要：tried（排除被critic擋掉、從未被實際評測的編輯）、recent yield（每個元件在最近n_prune輪內測得的最佳進步）、prune set（最近沒有正向收益、但machinery還留在incumbent裡的元件）、以及stall旗標（最近w輪的分數變化小於delta就觸發），exploration再依此寫出下一輪該優先嘗試哪些「還沒試過的元件」的指示。

📊 噪音有多大：三組數字看懂delta怎麼算

| 重複評估規模 | delta（2倍標準差） |
|---|---|
| 單次校準（40任務x2 trial x6次重複） | 分數本身飄動0.113 |
| 80個trial | 約0.108 |
| 3,200個trial | 約0.013（論文回報範圍0.004~0.020） |

⚠️ 容易踩的坑：環境變數沒設，錯誤訊息根本看不到

除了上面提到的ZeroDivisionError陷阱，這篇教學也只能示範RRSI裡「決策規則」的部分；要完整重現論文的自我改寫迴圈，仍然需要Claude Opus透過Vertex AI出手，並在Docker benchmark裡實際跑分，這部分不是免費的筆記本環境能負擔的規模。

🎯 對工程師的實務啟示

即使不打算複刻整套RRSI迴圈，它處理「缺失trial」、「噪音門檻delta」、「洩題偵測」和「只升不降的分數地板S*」這幾個設計，都是任何自我改寫或自動prompt優化系統該抄的作業：少一個環節，agent就可能找到辦法讓分數看起來變好，而實際上什麼都沒改善。

🔗 來源
- 標題：Google Research RRSI Guide: Mastering Self-Improving AI Agents
- 作者／機構：Sana Hassan，MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/08/google-research-rrsi-guide-mastering-self-improving-ai-agents/

#RRSI #SelfImprovingAI #AIAgent #GoogleResearch #LLM #PromptEngineering #AIAlignment #ClaudeOpus #AgentHarness #MachineLearning
