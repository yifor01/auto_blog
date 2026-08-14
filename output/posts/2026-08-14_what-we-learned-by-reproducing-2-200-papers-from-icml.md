---
title: What We Learned by Reproducing 2,200 papers from ICML
source: HuggingFace Blog
url: https://huggingface.co/blog/icml-2026-open-reproductions
model: claude-code/sonnet
generated_at: '2026-08-14T07:23:44.467937'
score: 93
---

📌 【Hugging Face】1,221人、19天、重現三分之一的 ICML 論文

TL;DR：一場社群黑客松用 AI coding agent 重現了 2,226 篇 ICML 2026 論文，23% 的論文至少有一個主張被推翻。

一篇拿到 spotlight 的 ICML 2026 論文，審稿人在評語裡寫下：「我給的信心分數偏低，是因為我沒有仔細檢查所有證明。」這篇論文最後拿到不錯的分數與 spotlight 殊榮。等到 Hugging Face 發起的社群黑客松真的把證明仔細檢查了一遍，會發生什麼事？

🤔 **投稿量翻倍，審稿量卻沒有跟上**

論文可重現性的問題由來已久，但規模讓它更嚴重。ICML 2026 收到 23,918 篇投稿、接受 6,352 篇，大約是前一年的兩倍，延續著一個至少部分由 AI agent 加快實驗與寫作速度所驅動的指數成長趨勢。然而審稿量並沒有跟著翻倍,大多數會議的審稿人是志願性質，未必有足夠時間或專業深度做完整審查。文章指出，過去仔細查核一篇論文可能要花審稿人一整個週末，現在一個 coding agent 一個下午就能嘗試一次，而且可以平行跑上千次。

🧩 **選一篇論文、帶上自己的 Agent、重現後全部公開**

2026 年 7 月 15 日至 8 月 2 日，ICML 2026 Open Reproductions 挑戰賽這樣運作：Hugging Face 團隊先為全部 6,341 篇被接受的論文整理摘要並拆解出核心科學主張，讓 agent 有一個具體、可驗證的目標，而不是一份 40 頁的 PDF；同一篇論文允許多人重現。參與者自帶工具，包括 Claude Code、Codex、Cursor、OpenResearch 的 orx 等各種 agent 框架。每次重現都要產出一份 Trackio logbook：一個靜態的 Hugging Face Space，內含寫作說明、實際跑過的程式碼、產出的成果物，以及選擇性上傳到 Hugging Face Dataset 的完整 agent 執行紀錄，讓查核過程本身也可被查核。最後由一個自動化的 Logbook Judge（採用開權重模型 GLM-5.2）重新閱讀每份 logbook，針對每個主張給出 verified（已驗證）、falsified（已推翻）、toy（縮小規模的證據）或 inconclusive（無法判斷）的判決，且被明確指示要把 logbook 自我評估視為不可信。參與者可獲得 20 美元的 HF 運算額度在 HF Jobs 上跑實驗；若原始資料集為專有或 checkpoint 未釋出而無法完整重現，參與者會改用模擬原始資料特性的合成資料做縮小規模重現。

📊 **超過三分之一的論文被實際重現過**

這場黑客松的規模數字：1,221 位社群成員加入、發布 6,816 份重現 logbook、嘗試了 2,226 篇論文（佔整個會議的 34%，其中許多論文由多個獨立團隊分別嘗試）、35,908 個主張被判決，所有判決結果在挑戰賽結束時凍結並公開為資料集，並啟動了 2,962 個 HF Jobs 雲端任務,其中 274 個完整 agent 執行紀錄資料集被公開發布到 Hugging Face。

以論文為單位彙總主張層級的判決結果：51% 的受檢論文（1,103 篇）至少有一個主張被獨立驗證，其中 266 篇所有被拆解出的主張都獲得驗證，另有 632 篇部分獲得驗證且沒有任何主張被推翻,總計 3,978 個個別主張透過實際實驗獲得確認。23% 的受檢論文（496 篇）至少有一個主張被推翻或存在爭議，其中 49 篇論文所有主張都被推翻、沒有任何一項獲得驗證，而最耐人尋味的是有 242 篇論文出現不同重現團隊對同一主張給出相反判決的情況。文章因此提出一個值得留意的觀點：可重現性不是二元的，而是對抗性的。剩下的論文中，502 篇只有縮小規模的證據，280 篇則因缺少成果物等原因而無法判定,是最常見的成因。

💡 **三個被推翻的具體案例**

有 35 位參與者正式聲稱推翻了某項主張，Hugging Face 團隊對每一個推翻聲明都做了對抗性複核：重新閱讀論文、重新閱讀 logbook，並從論文原文重新推導數學或重新實作實驗。其中幾個確認被推翻的案例：

- 開頭提到的那篇論文《Towards Optimal Robustness in Learning-Augmented Paging》宣稱其演算法達到 H_k + O(1) 的穩健性,一位參與者的 logbook 測出額外項實際上以 0.38 ln k 的速度成長,並定位出證明崩潰的確切步驟。團隊自行的重新實作把掃描範圍延伸到 k = 1,024，以約九個標準差的顯著程度確認這個成長趨勢，真正的穩健性應為 H_k + Θ(log k)。
- 《Attention's forward pass and Frank-Wolfe》證明「只要原點一開始就在 token 粒子的凸包內，這些粒子就會收斂到原點」，三個獨立團隊各自找到反例，違反情況分別最早出現在第 224、約第 3,800 與第 6,416 步,這也解釋了為什麼其他人「驗證」了這個主張：有限步數的檢查往往太早結束。其中最乾淨的反例用精確有理數表述，不存在浮點數誤差可以拿來搪塞。
- 《Self-Distillation Enables Continual Learning》的核心公式與理論章節分析的是 reverse KL 散度，但論文作者表示產出所有結果的釋出程式碼，預設實際計算的卻是 forward KL。抓出這個問題的 logbook 同時也指出，用作者自己的程式碼與資料，無法重現論文宣稱的 +4pp 提升結果。作者已在同一天確認此事，並已上傳修正版本到 arXiv。

⚠️ **不是所有論文都能被「證明」是對的**

文章也點出一些表現優異的案例：《Flat Minima and Generalization: Insights from Stochastic Convex Optimization》被 20 個獨立團隊重現，其中 12 個驗證了每一項主張；《A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness》這篇討論「LLM 評審不可靠」的論文，17 份 logbook 中有 14 份驗證了每一項主張。不過整體而言，缺少成果物仍是無法判定結果最常見的原因，代表可重現性的驗證品質很大程度取決於論文本身是否釋出完整的程式碼、資料與 checkpoint。

🎯 **實務啟示**

對正在用 coding agent 做研究或審查論文的工程師與研究者來說，這場黑客松示範了一種可規模化的查核方式：把論文拆解成可檢驗的具體主張，讓 agent 針對主張而非整篇論文動手驗證，再用獨立的第二層判決機制（且不信任自我評估）去把關結果。案例也提醒，數學證明的反例可能要跑到很晚的步數才會出現，程式碼與論文理論章節的細節（例如用錯 KL 散度方向）也可能悄悄影響最終數據，這些都是傳統審稿流程未必能抓到、但 agent 大規模平行複核有機會抓出來的問題。

🔗 **來源**
- 標題：What We Learned by Reproducing 2,200 papers from ICML
- 作者／機構：Abubakar Abid，Hugging Face Blog
- 連結：https://huggingface.co/blog/icml-2026-open-reproductions

#Reproducibility #ICML2026 #HuggingFace #AIAgents #ScientificResearch #MachineLearning #OpenScience #CodingAgents #ResearchIntegrity #AIforScience
