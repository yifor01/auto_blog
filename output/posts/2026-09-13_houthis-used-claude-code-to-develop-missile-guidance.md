---
title: 'Houthis used Claude Code to develop missile guidance software: Anthropic'
source: Hacker News
url: https://clashreport.com/world/articles/houthis-used-claude-code-to-develop-missile-guidance-software-anthropic-s52mnx4pwpo
model: claude-code/sonnet
generated_at: '2026-09-13T19:39:22.874057'
score: 84
---

📌 Anthropic揭露：胡塞武裝曾用Claude Code開發飛彈導引軟體

TL;DR：Anthropic威脅報告指出，一個疑似與胡塞武裝有關的團隊，靠並行運作多個Claude Code實例完成原本需要整支飛彈工程團隊的工作。

一群人只要同時開好幾個Claude Code對話視窗，分別負責寫程式、做研究、審核成果，就能複製出一整支專業工程團隊的產出？Anthropic最新的威脅報告，記錄了這個假設在真實世界被驗證的過程。

🤔 一個葉門據點，複製出整支飛彈工程團隊

Anthropic 9月的威脅報告描述，一個以葉門北部為據點、被評估為「極可能」與胡塞武裝有關的團隊，使用Claude Code執行原本需要整支飛彈工程團隊才能完成的工作：開發一款導引火箭的控制軟體、一款射程超過2,000公里的彈道飛彈，以及代號「R2000」的高超音速滑翔載具概念的相關軟體。Anthropic指出，這是報告中生成式AI被直接用於傳統武器開發、而非僅止於研究蒐集資訊的最清楚案例之一。

🧩 平行AI工作流，取代原本分工的專業團隊

操作者同時運行多個Claude實例，讓不同對話分工：一個負責寫程式，一個負責研究，另一個負責審查成果，而非把工作依序丟給單一模型實例。這套工作流程讓一小群人得以重現原本分散在多個工程專業角色上的產出。技術範圍延伸到導航、飛控與模擬：操作者嘗試把開源自動駕駛軟體整合進手機等級的飛控電腦，並用Claude寫導航與控制程式碼；他們也開發了六自由度(6-DOF)彈道模擬，用來建模物體在空間中的運動與旋轉，並用強化學習調校飛控演算法。最終這個專案被編譯成一個可離線執行的獨立執行檔，意味著後續開發不再需要直接存取Claude。

📊 試射失敗後，幾小時內就回頭找AI做故障分析

該團隊確實在葉門試射了一枚導引火箭，根據Anthropic記錄的資料，這次試射似乎失敗了。但操作者在數小時內就回到Claude，開始分析發射遙測資料以調查失敗原因。從軟體開發、實體試射到快速的事後分析，這個循環顯示模型被整合進一套反覆迭代的武器工程流程，而不只是回答零散的技術問題。Anthropic表示沒有證據顯示該團隊成功部署出可作戰的武器，但在相關帳號被停用之前，操作者已經組裝出一套不再依賴Claude存取的離線工程工具鏈。

💡 安全防護被繞過的方式，是把任務拆碎

Anthropic的安全防護機制在此過程中攔阻了大量請求，操作者則透過模糊化個別任務的最終用途、把工作拆分到不同對話中等方式來規避限制，Anthropic隨後禁用了相關帳號。這個案例點出AI安全系統的一個結構性難題：當一個更大的工程專案被刻意拆散到多個對話裡時，單一請求看起來可能完全無害。這起葉門案例是Anthropic記錄的六起傳統武器相關案例之一，其中三起與中國有關、兩起與俄羅斯有關，涵蓋飛彈、武裝無人機、槍械與炸彈等領域。整份報告涵蓋2025年12月至2026年8月間Anthropic表示已中斷的多類操作，包括網路攻擊、影響力操作、監控、傳統武器、生物濫用風險、詐騙與非法模型蒸餾。報告也描述了一些生物研究案例，Anthropic坦言難以判斷相關科學家究竟是在進行合法研究還是追求武器化目標；Anthropic威脅情報主管Jacob Klein表示：「你看到的不是漫畫式那種『我要做生物武器殺光所有人』的橋段，這是一個非常細膩複雜的情境。」

⚠️ 尚未成為可作戰武器，但工具鏈已經離線化

必須強調的是，Anthropic並未發現該團隊成功讓武器達到可作戰狀態；報告本身也承認在生醫案例上存在難以判定意圖的灰色地帶。這類威脅報告的細節與判斷主要來自Anthropic自身的偵測與評估，外界目前難以獨立覆核。

🎯 實務啟示

對於正在打造agentic AI系統防護機制的工程團隊而言，這個案例的關鍵教訓不是「AI能不能被濫用」，而是單輪內容過濾對「刻意拆分到多個session」的工作流程效果有限；若要提升防禦力，需要考慮跨會話的行為模式偵測，同時也要意識到一旦攻擊者把成果編譯成可離線執行的工具，事後封鎖帳號的效果會大打折扣。

🔗 來源
- 標題：Houthis used Claude Code to develop missile guidance software: Anthropic
- 作者／機構：Ahmet Koçak, Clash Report
- 連結：https://clashreport.com/world/articles/houthis-used-claude-code-to-develop-missile-guidance-software-anthropic-s52mnx4pwpo

#Anthropic #ClaudeCode #AISafety #ThreatIntelligence #Houthis #WeaponsDevelopment #NationalSecurity #AIGovernance #DualUseAI #AIrisk
