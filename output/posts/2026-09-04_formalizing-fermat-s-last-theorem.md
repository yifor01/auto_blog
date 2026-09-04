---
title: Formalizing Fermat's Last Theorem
source: Anthropic Research
url: https://www.anthropic.com/research/formalizing-fermats-last-theorem
model: claude-code/sonnet
generated_at: '2026-09-04T19:40:10.007607'
pinned: true
---

📌 【Anthropic 官方研究】Claude 花 11 天，讓費馬最後定理成為電腦可驗證的證明

TL;DR：Claude 近乎自主寫出 1,300 萬行 Lean 程式碼，完成史上第一個端到端、電腦可驗證的費馬最後定理（FLT）證明。

1637 年，費馬在書頁邊緣留下一句話：「我發現了一個真正美妙的證明，但這裡的空白太窄，寫不下。」358 年後，Andrew Wiles 終於在 1995 年給出正確證明，長達 129 頁，光是驗證就耗費數月人力。如今，Anthropic 揭露 Claude 只花了 11 天，就讓這個證明變成電腦可以逐行檢查、確定無誤的形式化版本。

🤔 **驗證一個證明，為什麼比想像中難**

證明數學定理需要串起極長的邏輯鏈，只要有一環出錯，後面的一切都可能崩塌。FLT 正是最好的例子：1908 年曾有人懸賞 10 萬德國金馬克（約合今日 100 至 200 萬美元）徵求正確證明，光是第一年就收到 621 個錯誤嘗試。1993 年 Wiles 公開演講宣布證明完成，兩個月後審查者的一個提問，卻揭露了證明中的致命缺口。Wiles 花了將近一年、一度瀕臨放棄，才和學生 Richard Taylor 一起找到修補方法，最終在 1995 年 5 月發表正式證明。由於至今找不到「初等」證明，數學界普遍相信費馬當年寫在邊注裡的那個「美妙證明」其實是錯的。

想用電腦徹底排除這類人為疏漏，就需要「形式化」（formalization）：把人類寫給人看、會跳過許多「顯然」步驟的證明，改寫成 Lean 這類證明助手（proof assistant）能逐步驗證的形式，且不能遺漏任何一個環節。荷蘭電腦科學家 Jan Bergstra 十年後首度提議形式化 Wiles 的證明，Imperial College London 的 Kevin Buzzard 則在 2024 年發起多年期的社群協作計畫，光是初期規劃的 blueprint 文件就長達 86 頁，社群原本預期整個形式化工程要耗時數年。

🧩 **dozens 個 Claude agent，靠 Prove2Me 協同作戰**

這項工作是 Anthropic 研究員、哥倫比亞大學團隊負責人 Tianyi Peng 發起的實驗：測試 Claude 能否推進 FLT 的形式化。Claude 遵循的是 Darmon、Diamond 與 Taylor 版本、經過簡化的 Wiles 證明路線，過程中人類提供的數學輸入僅限於少數高階指示，例如「Jacobian as a scheme 這個優先度較高」「把 Mazur 定理推進完成」。

最初的嘗試並不順利：多個 agent 一開始有些進展，但很快就丟失了專案的整體狀態，彼此協作失效，這些失敗的努力最終只貢獻了最終證明中約 7% 的非樣板程式碼。真正的突破來自改用 Prove2Me，一個由 Tianyi Peng 團隊設計的開放式數學形式化協作平臺。Prove2Me 的關鍵作用包括：維護一張定理陳述的有向無環圖（DAG），讓 agent 能判斷下一步該證明什麼，緩解多 agent 並行時的「記憶退化」問題；把定理陳述與證明拆到不同檔案分別維護，加快 Lean 編譯速度並降低資源消耗；以及替每個定理維護自然語言描述，讓 agent 能搜尋、重用既有成果，走出更簡潔的證明路徑。

📊 **1,300 萬行 Lean，是 Mathlib 的 5 倍以上**

最終，Claude 寫出了 3 萬 300 個可電腦驗證的定理，其中 2 萬 9,500 個被用進最終證明；整個證明累計 1,300 萬行 Lean 程式碼，超過社群主要數學證明庫 Mathlib 的 5 倍規模。Kevin Buzzard 看過成果後評論：這項自動形式化的成就「除了數學公理之外不依賴任何假設」，過程中涉及代數、調和分析、幾何與數論的自動形式化，也證明了 AI 自動形式化產出的成果已經足夠穩固，可以被後續工作繼續疊加。

💡 **這次的重點不是發現新數學，而是「可信任」**

Anthropic 特別強調，這和近期 AI 在黎曼猜想（Riemann hypothesis）上產出新數學的工作不同，FLT 這次的創新在於「驗證」，也就是像用計算機驗算一樣，逐步確認已知結論的正確性。隨著 AI 產出越來越多數學結果，能否快速將其形式化，將直接影響評估新成果所需的時間，而評估一個重大結果原本可能要花上數年。

🎯 **實務啟示**

對 AI/ML 工程師而言，這是自動形式化工具鏈成熟度的一次實戰驗證：多 agent 協作在缺乏共享狀態管理時很容易失效，而透過 DAG 追蹤任務依賴、拆分編譯單元、輔以自然語言索引，是讓大規模自動化證明／驗證工作可行的關鍵基礎設施設計，這些思路同樣適用於任何需要長時間、多 agent 協作維護「狀態」的複雜工程任務。

🔗 **來源**
- 標題：Formalizing Fermat's Last Theorem
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/research/formalizing-fermats-last-theorem

#Anthropic #Claude #FormalVerification #Lean #Mathematics #FermatsLastTheorem #Autoformalization #AIforMath #ProofAssistant #AIAgents
