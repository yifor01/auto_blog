---
title: 'Closing the Binary Blind Spot: Domain-Knowledge Injection for LLM Malware
  Triage in npm Packages'
source: Databricks
url: https://www.databricks.com/blog/closing-binary-blind-spot-domain-knowledge-injection-llm-malware-triage-npm-packages
model: claude-code/sonnet
generated_at: '2026-10-16T20:12:47.807719'
score: 91
---

📌 npm 惡意軟體藏進二進位檔，LLM 審查為何更容易看漏

TL;DR：Databricks 研究顯示，注入預先編碼的領域知識可讓 LLM 偵測 npm 二進位惡意軟體的失敗率大幅下降。

一個被精心包裝成乾淨 npm 套件的惡意軟體，裡面藏的不是容易被掃到的 JavaScript 程式碼，而是一個被去除符號、字串也被加密的二進位檔，這種情況下連 LLM 都可能被騙去打上「無害」的標籤。Databricks 針對這個特定的攻擊面做了一次系統性的檢驗。

🤔 **二進位檔是 npm 惡意軟體裡的小眾但高風險類別**

Databricks 自 2025 年 11 月起持續蒐集 npm 惡意軟體樣本，在透過 OSV npm 惡意軟體公告交叉比對的 11,413 個套件版本中，96.2% 的惡意軟體把 payload 藏在套件原始碼裡，或是從外部伺服器下載；僅剩 3.8%（432 個套件版本）會直接打包一個二進位檔。數量雖小，風險卻不成比例：一個被去除符號、無原始碼可讀的二進位檔，可以被包裝在看起來乾淨的原始碼與 metadata 之下，容易把 LLM 的判斷帶偏向無害。團隊的分析也證實了這點——在 OSV 確認的 npm 惡意軟體中，含二進位檔的套件未能做出明確惡意判定的比例，是純原始碼套件的兩倍以上（14.4% 對 6.2%）。

🧩 **方法：把專家知識編碼進 prompt，而不是塞進權重**

既有研究多採用在開源模型上做指令微調（instruction-tuning），把專家知識直接「烤進」模型權重裡,但這種做法無法套用到封閉的託管模型，且隨著威脅手法演變就得重新訓練。Databricks 反過來，在推論時把專家知識以「預先算好的靜態證據」形式放進 prompt，讓模型在看到證據後才開始推理。

他們打造了一套即時監控 npm 註冊表的掃描器,在 LLM 審查前先跑一個靜態分析階段：用 YARA 掃 tarball、用 Semgrep 與 npm registry API 分析 JavaScript 與 metadata、再用一個二進位分析模組檢視編譯後的產物，把結果組裝成結構化 prompt，交給 LLM 判定並給出理由，最多可要求三輪額外檔案。

為了做對照實驗，團隊設計了五種原生 Node.js addon（.node 檔）payload 類型，涵蓋常見供應鏈攻擊手法，import 範圍從較無害的 fopen、connect、gethostname，到幾乎只會用於惡意目的的 execve 搭配 dup2，每個都包裝在專業的 package.json、README、JavaScript bindings 與 binding.gyp 之中。其中 sysmon 竊密軟體涵蓋從可讀基準版本到完全去除符號、字串以單位元組 XOR 加密的強化版本的一整套混淆程度；選用單位元組 XOR 而非 RC4 等更強加密是刻意的，因為前者不會在反組譯結果中留下結構性標記讓模型捕捉到。這些設計對應真實蒐集到的惡意軟體格式（PE、ELF 皆去除符號、Mach-O）與行為（竊取憑證與環境變數、持久化、資料外洩與 C2、主機偵察、dropper）。

團隊評測了來自七家供應商的九個模型：七個團隊實際上會在程式碼庫中大規模運行的「平價」模型（其中四個開源權重），以及兩個作為行為基準參照的高階模型；另外也把最貴的 Claude Opus 4.6 跑了一輪，僅作為成本參考。每個 payload 對每個模型跑兩次，一次不給領域知識、一次給，prompt、context 與二進位分析內容在兩種條件下完全相同，推論設定也全程固定：temperature 為 0、相同的系統與分析 prompt、輸出上限 8192 token。

📊 **注入領域知識後，失敗率大幅下降**

| 評測門檻 | 未注入 capability profile | 注入 capability profile 後 |
|---|---|---|
| 未達「高度可疑」（escalation）門檻失敗率 | 50%（35/70，其中 20 次直接判無害） | 4%（3/70） |
| 未達「惡意」（malicious）判定門檻失敗率 | 73%（51/70） | 34% |

作為對照，兩個行為基準模型在未注入知識時就沒有在 escalation 門檻失敗,只在一次（Sonnet 對 sysmon v3）未能達到惡意判定。注入 capability profile（一種把單一惡意技術，如憑證竊取或持久化，編碼成針對掃描器靜態證據的加權條件組合的宣告式規則）後，35 次原本失敗的案例中有 32 次（91%）恢復為成功偵測，沒有任何模型對任何 payload 給出無害判定；除了 GPT-5.4-nano 仍有三次停留在「可疑」層級外，所有原本失敗的模型都在加入 profile 後達到完整偵測。

最具代表性的案例是 Qwen3-Next 面對經過混淆的 sysmon 原生竊密軟體：在完全相同的輸入下，沒有 profile 時以 0.98 的信心判定為無害並建議放行，加入四個觸發的 profile 後則以 0.98 的信心判定為惡意並建議封鎖。而原本就判斷正確的基準模型（Sonnet、Kimi）在加入證據後判斷依然正確,顯示 profile 是在強化已經正確的推理，而不是扭曲它。

💡 **失敗不是隨機，而是有固定模式**

研究發現失敗模式在模型間呈現可重複的固定型態,而非隨機出錯。例如 Gemini 在沒有 profile 時雖然偵測率追上了基準模型，但靠的是「編造的推理」而非真正的分析。整體上，團隊歸納出四種橫跨大部分模型的失敗模式：從判定結果層面可觀察到的「輕易放行」與「模糊其辭」，以及從書面推理中可觀察到的「合理化」與「編造理由」，這四者並非互斥，一個無害誤判可能同時兼具放行與合理化兩種特徵。團隊認為背後有兩個因素：一是平價 LLM 普遍缺乏在套件情境中解讀二進位結構證據所需的領域知識，二是模型本身的原始能力落差。

⚠️ **侵限：規模小、聚焦單一生態系**

二進位檔攻擊在 npm 生態中本就是小眾（3.8%），實驗的十個 payload 也是人工設計而非全部來自真實野生樣本；評測的核心失敗分析集中在七個平價模型的 70 組測試，高階基準模型僅作參照用的 20 組測試。

🎯 **對維運套件安全掃描的工程團隊**

如果你的供應鏈安全流程已經引入 LLM 做套件審查，這項研究的做法值得參考：與其等著模型自己「看懂」二進位檔，不如把靜態分析（YARA、Semgrep、二進位結構特徵）預先轉換成結構化證據餵進 prompt，尤其是對預算有限、只能用平價模型大規模掃描的團隊，這種做法不需要重新訓練模型，就能大幅降低對混淆二進位 payload 的漏判率。

🔗 **來源**
- 標題：Closing the Binary Blind Spot: Domain-Knowledge Injection for LLM Malware Triage in npm Packages
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/closing-binary-blind-spot-domain-knowledge-injection-llm-malware-triage-npm-packages

#SupplyChainSecurity #LLMSecurity #MalwareDetection #npm #PromptEngineering #AISecurity #SoftwareSupplyChain #ThreatIntelligence #StaticAnalysis #Databricks
