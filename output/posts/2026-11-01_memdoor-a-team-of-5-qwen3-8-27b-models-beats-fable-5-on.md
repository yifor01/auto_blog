---
title: 'Memdoor: A team of 5 Qwen3.8-27B models beats Fable 5 on LiveCodeBench Hard'
source: Hacker News
url: https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve
model: claude-code/sonnet
generated_at: '2026-11-01T21:17:19.181519'
score: 97
---

📌 五個 27B 小模型組隊寫程式,成績打平頂級模型

TL;DR：開源工作流用五個分工的 Qwen3.8-27B 模型協作解題,在 10 題抽樣中成績逼近對照組,但作者誠實列出取樣與污染風險。

多模型協作聽起來像是堆料換分數的老套路,但這次 Hacker News 上一篇題為「Memdoor: A team of 5 Qwen3.8-27B models beats Fable 5 on LiveCodeBench Hard」的貼文,把重點放在「能不能被完整複現」上,而不是炫耀分數。

🤔 **五個角色,只靠硬碟上的檔案交談**

這個名為 team-solve 的工作流,是把論文 GVS5H（Lee, 2026）提出的方法,改寫成 Memdoor 的八個 YAML 檔案,沒有額外程式碼,也沒有指定任何模型。五個角色分別是:規劃者(planner)、兩位構想者(ideator)、求解者(solver)、管理者(manager),再加一個修復工(repair worker)。每個角色都從全新的 context 開始,彼此只透過硬碟上的檔案交談,不依賴對話記憶。判定成功與否的是一支跑測資的腳本,不是模型自己說了算。

🧩 **流程:plan → ideate-a / ideate-b → solve → test → review → repair → verify**

整個工作流的資料流是:

- plan(agent):讀 task.md,寫出 plan.md 與 notes.md。
- ideate-a、ideate-b(agent,並行):各自讀取計畫,提出一個方案,一個走最直接可證明的演算法,另一個走完全不同的方法家族。
- solve(agent):讀兩份方案,寫出 solution.py,並把決策記在 notes.md。
- test(command):跑 tests/ 底下的樣例,輸出 test-output.log(這一步本身不會讓流程失敗)。
- review(agent):讀測試輸出,把修復指示寫進 notes.md。
- repair(agent):依指示修好 solution.py,或者判斷不需要修改。
- verify(command):再跑一次 tests/,回傳的非零結束碼才會讓整個流程失敗。

每個 agent 的提示詞都寫著「全新 context,讀檔案,不要依賴對話記憶」,作者認為這種「紀錄紀律」正是效果的來源。要換模型只需改 /model 指向,連本地模型都支援;要改角色行為,只需改 steps/ 底下對應的提示詞。

📊 **10 題、5 次通過的對照結果**

作者用同一顆模型 Qwen3.8-27B、同一套提示詞、迴圈與 128K 回覆上限,在對方 LiveCodeBench Hard 清單的前 10 題上,各跑 5 次,用修正過的評分器對照每一個隱藏測試,得到:

| 題號 | 本工作流 | 作者原始 harness | Fable 5(單次呼叫) |
|---|---|---|---|
| 1 | 10 / 10 | 9 | 7 |
| 2 | 10 / 10 | 10 | 8 |
| 3 | 10 / 10 | 10 | 10 |
| 4 | 10 / 10 | 9 | 8 |
| 5 | 9 / 10 | 10 | 7 |
| 平均 | 9.8 | 9.6 | 8.0 |

「作者原始 harness」與「Fable 5」兩欄是對方倉庫裡重新評分過的結果檔案；本工作流的結果全部存放在 bench/results/parity-5pass/,包含每一次請求與回覆、產生的程式、評分器輸出與花費。單次執行中位數耗時 40 分鐘、花費 0.39 美元,50 次總共 35.79 美元。

⚠️ **作者自己列出的限制,相當誠實**

文章特別強調「這個結果能證明什麼,不能證明什麼」:10 題、5 次通過,不是對方原本的 100 題規模,在這麼小的樣本下,9.8 和 9.6 其實是同一個數字,整篇文章的主張是「與對方的 harness 打平」,不是「超過」。這些題目出自 2025 年春季的競賽,模型可能在訓練時就見過,污染無法排除,且適用於所有欄位。Fable 5 那一欄是單次呼叫,來自對方的檔案,並沒有在這個工作流裡實際跑過。在這 10 題上,作者原本的五次通過資料顯示 Fable 5 是 80 分、他們的 harness 是 96 分,本工作流 98 分重現了那個差距；但放到對方完整的 100 題上,harness 與 Fable 的差距縮小為 92.4 比 90.4。另外,loop 只看得到公開樣例,但最終評分用的是隱藏測試。唯一輸掉的一題,是因為管理者捏造了一個錯誤的反例,導致團隊把原本正確的程式改錯；另外兩次正確程式被覆寫後又被救回,這些都是對方原始迴圈的既有行為,作者原樣保留未修改。逐字節比對請求的驗證過程、換過的環境與第一次執行的發現,都記錄在 NOTES.md。

🎯 **實務啟示**

如果你想拿自己的題目試試,流程很直接:

```
curl -fsSL https://memdoor.ai/install.sh | bash
memdoor connect openrouter
git clone --depth 1 https://github.com/guregodevo/memdoor
mkdir -p ~/.memdoor/workflows
cp -r memdoor/examples/workflows/team-solve ~/.memdoor/workflows/
mkdir my-problem && cd my-problem
cp -r ../memdoor/examples/workflows/team-solve/sample/* .
memdoor workflow run team-solve --wait
```

把 task.md 換成自己的題目,tests/N.in 與 tests/N.out 成對放好即可,solution.py 需要 Python 3 與 bash 環境。這套「每個角色只靠檔案交談、全新 context」的設計,對想做可審計、可重現多 agent 協作的工程師,是一個值得參考的工程紀律範例,而不只是分數。

🔗 **來源**
- 標題：Memdoor: A team of 5 Qwen3.8-27B models beats Fable 5 on LiveCodeBench Hard
- 作者／機構：guregodevo，Hacker News
- 連結：https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve

#AI #LLM #MultiAgent #Qwen #CodeGeneration #LiveCodeBench #OpenSource #Reproducibility #Benchmarking #AIAgents
