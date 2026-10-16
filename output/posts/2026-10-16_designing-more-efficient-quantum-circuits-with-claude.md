---
title: Designing more efficient quantum circuits with Claude
source: Anthropic Research
url: https://www.anthropic.com/research/designing-efficient-quantum-circuits
model: claude-code/sonnet
generated_at: '2026-10-16T20:06:19.068317'
pinned: true
---

📌 【Anthropic】Claude 設計量子電路，效率超越現有最佳方案

TL;DR：Anthropic 讓 Claude 自主設計 8 種量子電路，部分任務用量比現有最佳公開設計省了一個數量級以上。

量子電腦的 qubit 數量稀缺、又極易受噪音干擾，這意味著決定一個量子演算法能不能跑起來的，往往不是硬體，而是電路設計本身夠不夠精簡。這次 Anthropic 的實驗顯示，這個設計工作現在可以交給 AI 自己迭代完成。

🤔 **qubit 很貴、很脆弱，電路設計決定一切**

與傳統電腦用 0 與 1 表示的位元不同，量子電腦用 qubit 儲存資訊，可以由單一原子、超導電路或光子構成，並利用 superposition（量子疊加）等現象處理某些傳統電腦難以解決的化學、材料科學、數論問題。但目前的量子電腦只有數百到數千顆 qubit，且對熱、震動甚至宇宙射線都極度敏感，微小擾動累積起來就會讓計算出錯。因為 qubit 與運算時間都是稀缺資源，研究者長期致力於重新設計演算法，讓它用更少 qubit、花更少時間完成。一個具體例子是模擬 FeMoco（固氮酶核心的鐵硫簇，理解它有助於設計更好的工業催化劑）：2017 年估計需要約 50 兆個 Toffoli gate 才能算出其基態能量；經過一連串演算法進步，這個數字已降到約 3.4 億個，縮減約 15 萬倍，相當於在未來約三百萬顆物理 qubit 的機器上運算數小時。這些進步主要來自重新設計電路，而不是硬體升級。

🧩 **給 Claude 文字規格，讓它自己跟評分器對話**

這項研究由 Andi Gu 在 Anthropic STEM Fellows Program 中主導，由 Anthropic 量子物理學家 Alek Kemeny 指導，並與哈佛大學的 Susanne Yelin、以及哈佛大學與 QuEra Computing 的 Mikhail Lukin 合作完成。研究團隊只給 Claude 八個量子電路的「plain-language」規格描述，涵蓋化學、最佳化、物理模擬與數論領域，再搭配一個自動評估器檢查正確性，並用「qubit 數乘以 gate 數」作為運算耗時的代理指標來打分。Claude Mythos 5 能在一個封閉迴圈裡自主運作：提出設計、拿到評估器的回饋與分數、再據此修改下一版，整個過程不需要人介入。選擇 Claude 來做這件事有幾個理由：量子電路可以用程式碼描述，因此能直接借用 Claude 的程式撰寫能力去寫、跑、修改設計；研究團隊關注的這類量子演算法每個輸入都對應一個確定輸出，一般電腦就能驗證正確性；設計量子電路還有兩個傳統程式沒有的限制——電路無法像一般程式那樣做「if-then」分支判斷（因為量子電腦會同時對疊加狀態中的所有輸入運算，兩條分支的操作都得留著），也不能任意丟棄中間資料（每一步都必須可逆，留著又會污染最終結果）。

📊 **八個任務全面超越現有最佳公開設計**

在涵蓋化學、最佳化、量子模擬、數論與數值計算的八個基礎運算元上，Claude 找到的設計在 qubit 數與 gate 數上都優於先前發表過的最佳演算法。例如在為鐵硫化合物模擬編譯電路時，Claude 注意到分子的對稱性與重複結構，讓某些計算結果只需算一次就能重複使用，不必對系統每個部分都重算一遍；在其他案例中，它發現既有電路裡有些昂貴的元件其實只是為了處理極罕見的輸入情況，於是重新設計並移除了這些元件。文章特別點出兩個發現：一是針對模組反運算（modular inversion，橢圓曲線運算中最昂貴的一步）設計出新的可逆演算法；二是讓某個主流量子最佳化演算法中最貴的一步，成本降低約 12 倍。

💡 **進步來自新的數學洞察，不是調參**

Anthropic 強調，這些改善每一個都來自 Claude 對問題結構與數學性質的新發現，而不是對現有設計做微調最佳化。這代表 AI 不只能最佳化傳統演算法，也開始具備重新設計量子電路的能力，而這正是讓量子演算法更快、更容易實際運行的關鍵一步。研究團隊認為，更快的電路設計工作，有機會讓量子電腦真正能解決的問題——從設計新藥、更好的電池，到找出更乾淨的肥料製造方式——提前到來。

🎯 **實務啟示**

這個案例的核心模式值得類推到其他領域：只要任務能被形式化成「可執行、可自動驗證正確性、有明確計分指標」，就有機會套用「AI 提出方案 → 自動評估器打分 → AI 根據回饋自我迭代」的封閉迴圈，讓 AI 在沒有人力逐步介入的情況下持續逼近更優解。對做演算法最佳化或電路設計相關工作的工程師，這類可驗證的自動化迴圈，是比單純靠人工調參更值得投資的方向。

🔗 **來源**
- 標題：Designing more efficient quantum circuits with Claude
- 作者／機構：Andi Gu（Anthropic STEM Fellows Program），Alek Kemeny（Anthropic），Susanne Yelin（Harvard University），Mikhail Lukin（Harvard University / QuEra Computing）
- 連結：https://www.anthropic.com/research/designing-efficient-quantum-circuits

#Anthropic #Claude #QuantumComputing #QuantumCircuits #Qubits #FeMoco #AIforScience #AlgorithmDesign #QuantumOptimization #STEMFellows
