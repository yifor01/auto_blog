---
title: How Public Evals Work and Fail, and What Should Change
source: Eugene Yan
url: https://eugeneyan.com/writing/public-evals
model: claude-code/sonnet
generated_at: '2026-11-21T22:20:11.975205'
score: 93
---

📌 公開評測有多可信?12個基準裡8個的裁判會誤殺正確答案

TL;DR:系統性檢視12個熱門 Agent 評測,發現多數 grader 會誤判正確解,分數該看可靠性而非單一平均值。

模型發布時,大家第一眼看到的往往是一串榜單分數。但如果連裁判本身都會判錯呢?Eugene Yan 這篇文章檢視了12個公開評測基準,其中8個被發現有「裁判誤殺正確答案」的證據,這讓榜單分數的可信度打上問號。

🤔 評測任務的四個組成部分

大多數評測任務都由四個元素構成:instruction(聽起來像真實使用者請求的提示,agent 通常只在開頭拿到一次,不能追問)、environment(工作環境,程式碼評測常是特定 git commit 的容器,知識工作評測可能是裝好軟體的 VM 或一堆文件)、grader(決定工作是否通過,可能是確定性程式碼檢查、LLM judge 打分,或兩者混合)、以及可選的 reference(人類專家解答,用來證明任務可解或建立人類基準)。

評測基準本身也越來越像軟體一樣被版本化維護,透過 issue 與 PR 接受修正。Agents' Last Exam v1.1 退役了30個任務、修訂了57個;Harvey LAB 的公開任務集從2026年5月上線時的約1250個,成長到2010個。但像軟體一樣的版本更新也會帶來破壞性變化,例如 Terminal Bench 每個版本都會丟棄已經飽和的任務,導致不同版本之間的分數難以直接比較。

🧩 評分設計反覆出現的四個原則

第一,優先用確定性檢查而非 LLM judge。確定性的程式碼檢查結果可重現,不會因為裁判模型升級而改變排名。DeepSWE 和 AutomationBench 完全不用 LLM judge,Agents' Last Exam 也盡量把 LLM judge 的使用降到最低。即使真的需要裁判(例如評估法律備忘錄或臨床回應),也會把裁判的任務限縮成逐條是非題式的 rubric,而不是整體打一個分數。

第二,grader 只檢查結果,不檢查過程。目的是讓任何能產出正確結果的做法都算通過,Terminal Bench 只檢查容器的最終狀態,忽略 agent 中間下了哪些指令或輸出了什麼;AutomationBench、OSWorld 2.0、DeepSWE 也採用同樣做法。

第三,全對才算過(all-pass scoring)相當常見,因為部分完成的工作往往沒辦法直接拿來用。DeepSWE、Terminal Bench、Terminal Bench Science、AutomationBench、Harvey LAB 都採用這種計分方式,Harvey LAB 的說法是:「抓到十個風險裡的八個不算八成完成,而是不完整。」但這種計分方式也很脆弱,一個寫錯的檢查項就能讓原本正確的解答整題失敗。另一種做法是部分計分,每個檢查項帶權重,任務得分落在0到1之間,FrontierSWE 和 HealthBench Professional 採用這種方式,Agents' Last Exam、Finance Agent、OSWorld 2.0 則兩種都回報。

第四,任務會被刻意調難以減緩飽和。AutomationBench 加入無關資料與互相衝突的政策讓簡單任務變難;HealthBench Professional 讓困難任務的比例提高到基礎集的約3.5倍;BrowseComp 只保留當時最強模型都解不出的問題;Terminal Bench 則會在任務飽和後直接退役。

📊 模型常犯的兩種錯

錯誤分析中反覆出現兩種失敗模式。第一種是跳過驗證或提早收工:OSWorld 2.0 上,agent 在沒檢查最終狀態的情況下就提交了工作;Harvey LAB 上,沒有自我審閱就直接交稿的 agent 分數較低;AutomationBench 上,模型只處理了清單的一部分,卻當作已經全部完成來總結,錯誤地宣告成功。第二種是漏掉明確寫出的要求:在 GDPval 上,「沒follow指令」是最常見的失敗原因;OSWorld 2.0 上,agent 會丟掉提示裡明確寫出的限制條件。這些大多是基本的驗證步驟就能攔住的非強迫性錯誤。

💡 grader 自己也會出錯:誤殺正確解與放過錯誤解

並非所有失敗都是模型的錯,評測本身也常有兩類漏洞。第一類是偽陰性,也就是誤判正確工作為失敗,常見原因是檢查標準比提示實際要求更嚴格,或悄悄加入了提示沒寫的要求。審查者發現 Terminal Bench 4.0 有41/65個任務是依照未明示的要求來評分;DeepSWE 有23/113個任務把正確解答判成失敗;OSWorld 2.0 上,外部審查者回報108個任務中有23個檢查項會誤殺正確工作,例如有個檢查項用的軟體根本打不開該任務自己提供的起始檔案。偽陰性也可能來自錯誤或模糊的標準答案:BrowseComp 上,解出題目的人類訓練員有50/367題(14%)不認同參考答案;一篇後續論文在重用 BrowseComp 題目的 BrowseComp-Plus 裡,抽樣200題確認其中10題有錯;Harvey LAB 從held-out集合中移除了17個無解的評分項,有貢獻者表示他在任何來源文件中都找不到題目要求的賠償金額估計。

第二類是偽陽性,也就是放過了錯誤的工作。評分項通常只檢查某個預期要點是否存在,而不檢查其餘部分是否正確。在 Harvey LAB 上,Artificial Analysis 用 LLM judge 把交付成果對照原始文件重新檢查,發現超過60%通過所有評分項的結果其實含有嚴重的幻覺內容。在 AutomationBench 上,55%的評分項只檢查訊息或記錄是否包含或不包含某個字串,這讓 agent 有機會只對上關鍵字卻把其餘內容做錯,例如某任務要求寄出一封列出待審與不需審核項目數量的郵件,評分只檢查信裡有沒有出現「3」和「4」這兩個數字,任何把這兩個數字對調的郵件都會通過。

💡 該換個方式看分數:平均通過率不等於可靠性

多數評測只回報平均通過率,但這會掩蓋生產環境中巨大的差異。設想兩個 agent 都拿到70%的分數,第一個每次都能穩定解出70%的任務,第二個則是對每個任務都有70%的機率解對。第一種可以放心信任它能穩定解出的那70%,第二種則幾乎每次輸出都要人工複查。用τ-bench帶起來的 pass^k 指標,只把連續k次嘗試都通過的任務算作真正解決,在五次試驗下,第一種agent仍然維持70%,第二種則會掉到17%。

🎯 實務啟示

看到一個新模型的榜單分數時,值得先問清楚評分方式:是確定性檢查還是 LLM judge?是全對才算過,還是部分計分?評分項是否只做字串比對式的鬆散檢查?如果榜單只提供單次平均通過率,不妨要求或自行驗證多次試驗下的 pass^k 表現,因為那才更接近這個模型在生產環境裡實際能被信任的程度。

🔗 來源
- 標題:How Public Evals Work and Fail, and What Should Change
- 作者/機構:Eugene Yan
- 連結:https://eugeneyan.com/writing/public-evals

#AIEvaluation #Benchmarks #LLMAgents #EvalDesign #AIReliability #MachineLearning #AgentBenchmark #ModelEvaluation #AIBenchmarking #PassK
