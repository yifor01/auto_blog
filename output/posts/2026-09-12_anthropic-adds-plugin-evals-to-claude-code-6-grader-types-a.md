---
title: 'Anthropic Adds Plugin Evals to Claude Code: 6 Grader Types, a No-Plugin Baseline,
  and a CI Gate for Skills'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/11/anthropic-adds-plugin-evals-to-claude-code-6-grader-types-a-no-plugin-baseline-and-a-ci-gate-for-skills/
model: claude-code/sonnet
generated_at: '2026-09-12T19:32:19.862175'
score: 83
---

📌 外掛到底有沒有用？Claude Code用一個指令幫你量出來

TL;DR：`claude plugin eval`讓外掛開發者能用A/B比較，量化Skill是否真的被觸發、是否真的比裸模型更好。

外掛裝了，Skill也寫了，但它到底有沒有在關鍵時刻被觸發？換一個模型版本後，行為還穩不穩定？如果拿掉這個外掛，模型會不會照樣做得一樣好？這三個問題,過去的`claude plugin validate`完全答不出來,因為它只檢查manifest語法與schema，不檢查行為。Anthropic這次補上的正是這一塊。

🤔 **語法檢查驗證不了行為，這是新工具要補的洞**

Anthropic為Claude Code發布了全新的plugin evals工作流程。`claude plugin eval`指令會用真實情境的提示詞去跑一個外掛，替Claude產生的結果打分，再拿來跟「不載入外掛」時的結果對照。這個工具需要Claude Code v2.1.269以上版本，可用於任何含有`plugin.json`、`.claude-plugin/plugin.json` manifest,或skills目錄型外掛的專案。要注意的是，每一次eval執行與判分呼叫都是真實的模型呼叫,會計入你的方案或API帳單。

🧩 **每個案例都跑兩次，Δ值就是外掛真正的貢獻**

一個eval suite放在外掛的`evals/`目錄下，每個測試案例是一個子目錄，內含`prompt.md`和`graders/`資料夾。`prompt.md`的內容會原封不動送給Claude，其中的`@path`不會被展開；frontmatter可以設定`max_turns`（預設10）、`timeout_seconds`（預設300）、`model`、`tags`與`allowed_tools`。

評分器（grader）是一份markdown檔案，frontmatter設定`type`、選填的`weight`與`arm`。共有6種類型：`regex`、`tool_used`、`tool_order`、`file_exists`這4種完全免費，因為它們是根據執行軌跡與磁碟上的檔案直接計算；另外`llm`（依你寫的散文標準,由判分模型打分）與`baseline`（拿參考答案做比較）這2種則需要呼叫判分模型,會產生費用。`claude plugin eval init`會讀取外掛內容,詢問「好的結果長什麼樣」,自動提出測試案例與評分器並試跑，最後寫成檔案；在CI環境中,加上`--bare <name>`則只會寫出空白範本。

每個測試案例預設會跑兩輪：載入外掛的with-arm,以及不載入外掛的without-arm，兩者的差值Δ就是這個外掛真正的貢獻。如果一個案例在兩種情況下都拿到1.0分,代表外掛根本不是它通過的原因。官方文件範例顯示,某案例在6次執行中WITH拿到1.00分、W/OUT拿到0.33分,Δ為+0.67,估計花費0.41美元、耗時74秒。標記為with-only的評分器（通常是`tool_used: Skill`）會被回報為指標，但不計入總分,因為without-arm本來就沒有skill可以觸發。

📊 **最常見的問題：Δ趨近於零,代表Skill根本沒被自然語言觸發**

Anthropic特別點出最常見的第一個發現：Δ值趨近於零,同時`tool_used: Skill`評分器判定失敗,意味著Claude在自然的提問方式下根本沒有選用這個skill。這正是`claude plugin validate`看不到的缺陷,因為validate只查manifest語法,不查實際行為。

執行結果會存放在`evals/results/<timestamp>/report.html`,附上每個評分器的判定與判分模型的投票結果；若帳號支援,報告預設也會發布到claude.ai,除非加上`--no-publish`。一個suite的實際執行量大致是「案例數 × 執行次數 × 兩種arm」次agent運行,再加上每次執行中每個`llm`或`baseline`評分器對應的3次簡短判分呼叫,且結果在不同次執行之間會有變動。文件提供的CI指令需要安裝Claude Code並具備如`ANTHROPIC_API_KEY`之類的憑證；若沒有加上`--trust-plugin`,在沒有終端機的環境下,未受信任的checkout會直接以exit code 1拒絕執行。報告本身出問題不會改變exit code,`--json`則會抑制進度輸出。

⚠️ **會產生實際費用,且結果本身不是完全可重現**

由於每次執行都是真實的模型呼叫並計費,加上判分模型帶來的額外呼叫,跑一次完整的eval suite並非零成本;同時因為模型輸出本身的變異性,同一個suite在不同次執行之間的分數也會有所浮動,不是一次跑完就能定案的數字。

🎯 **實務啟示**

如果你有在維護Claude Code外掛,這個工具值得直接排進CI流程:它能在合併前就抓出「Skill寫了但沒被自然語言觸發」這種validate抓不到的行為缺陷,也能在換模型版本或改prompt後,快速確認外掛的實際貢獻(Δ值)是否還在,而不是憑感覺覺得「應該還能用」。

🔗 **來源**
- 標題：Anthropic Adds Plugin Evals to Claude Code: 6 Grader Types, a No-Plugin Baseline, and a CI Gate for Skills
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/11/anthropic-adds-plugin-evals-to-claude-code-6-grader-types-a-no-plugin-baseline-and-a-ci-gate-for-skills/

#ClaudeCode #Anthropic #DevTools #AIEvaluation #CICD #PluginDevelopment #LLMTooling #SoftwareEngineering #AgenticAI #QualityAssurance
