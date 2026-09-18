---
title: 'Working at the frontier: How Balyasny Asset Management evaluates and governs
  Claude Fable 5'
source: Claude Blog
url: https://claude.com/blog/working-at-the-frontier-how-balyasny-asset-management-evaluates-and-governs-claude-fable-5
model: claude-code/sonnet
generated_at: '2026-09-18T19:43:28.318915'
pinned: true
---

📌 【Anthropic 客戶故事】管理 380 億美元資產的公司,怎麼評測 Claude Fable 5

TL;DR：BAM 用數千筆真實金融任務測試 Fable 5,結果從「查資料」進化到「做任務」的 agent 時代正式開始。

當一家管理約 380 億美元資產、旗下約 2,000 名投研與行政人員的機構,決定把前沿 AI 模型放進真實交易與研究流程時,它會怎麼把關?Anthropic 近日專訪 Balyasny Asset Management（BAM）Chief AI Officer Charlie Flanagan,揭露這家全球多策略投資公司如何評估與治理 Claude Fable 5。

🤔 **從「AI 做搜尋」到「AI 做工作」**

Flanagan 指出,2026 年最大的轉變不只是模型本身,而是像 Claude Code 這樣的 harness（執行框架）。過去 AI 只能回應提示、產出片段結果;現在可以被交付一個「目標」而非「提示」,持續工作到完成為止。

一個具體例子是併購套利（merger-arbitrage）分析。當交易宣布後,agent 會建立初步的交易分析包:估計交易成交機率與所需時間、擷取關鍵經濟與法律條款、辨識條件與里程碑,並標出需要投資人自行判斷的部分。這套流程過去需要三到五天,分散在人工研究與各自獨立的工具之間;現在則不到一天完成,agent 執行約 30 分鐘,任何重大結論在採用前仍須經過人工審查。BAM 使用 Anthropic 的前沿模型,但執行 harness、資料存取與審查控管等基礎設施多為自建。

🧩 **用數千筆真實金融任務評測,而非通用基準**

BAM 多年前就投入建立自己的評測系統,測試新模型時橫跨股票、總體經濟、大宗商品,使用數千筆有可驗證結果的真實金融任務,而非依賴通用 benchmark 或單一展示案例。

評測分兩個層次:模型單獨表現,以及模型在 agentic 環境中(使用與使用者相同的工具、檔案與需求）的表現。評估重點包括:能否規劃任務、選對並用對工具、找到並分析證據、從錯誤中恢復、檢查中間結果,以及產出有根據的成果。BAM 也特別留意特定失敗模式,例如數值錯誤、遺漏覆蓋範圍、缺乏依據的結論,以及檢索問題。

📊 **在相關任務子集上,Fable 拿下 89.4% 對比前代的 86.1%**

在數千筆任務的相關子集上,Fable 5 的表現為 89.4%,優於前一代生產模型的 86.1%,其中在複雜規劃、分析與 agentic 執行上表現最為突出。

Flanagan 特別提到一組經濟學問題:過去測試過的所有模型都未曾成功解出,直到 Fable 5 出現。由於這代表相較於過往所有測試過的模型都是一次顯著跳躍,BAM 一開始還懷疑是評測本身出了問題,於是重跑評測、獨立檢查任務與計分邏輯,並與 Anthropic 一同review 結果後,才確認這項進步是真實的。如今,BAM 的投研團隊已把 Fable 當作系統性分析與程式撰寫工作的首選前沿模型,並依效率與成本提供何時該用 Fable、何時用其他模型的指引。

💡 **安全不是選模型的一次性決定,而是產品與營運層面的持續設計**

Flanagan 強調,BAM 把安全視為產品與營運模式的問題,而非單純的模型選擇。關鍵問題不只是模型能做什麼,還包括它能存取什麼資料、能用什麼工具、能採取什麼行動、哪些事項必須留給人工核准,以及如何得知出錯。這代表控管要圍繞在模型「外部」,而不是假設模型本身就是控管機制。

具體作法包括:核准的資料邊界、最小權限存取、工具層級的權限管控、日誌與可追溯性、重大產出的人工審查,以及明確的例外升級流程。BAM 也會在擴大存取範圍前先測試對抗性與失效情境。即便換上更強大的 Fable 5,這套安全設計並未因此鬆動——更強的推理與規劃能力,不代表模型能自動獲得更大權限。模型只能使用該使用者與任務所核准的工具與資料來源,且無法自行擴權;投資判斷與究責仍留在人身上。

為了落實這套治理,BAM 花了六個月建置內部平臺 BAMAgent,目前支援數千個全天候運作的自主 agent。相較於聊天介面幫助人吸收與整理資訊,BAMAgent 執行的是可能跑上數小時甚至數天、多個 agent 平行運作的多步驟研究與分析,最終產出可供人審查的成果,例如建立並維護公司研究檔案、準備財報或總經事件簡報,或把新證據轉換成財務情境。Fable 5 是規劃與分析階段的首選模型,因為這個階段一旦出錯,會影響後續所有產出。

在實際應用上,一個 BAMAgent 曾執行稅損收割（tax-loss harvesting）分析,探索了 9 萬張資料庫表格,找出相關的共同基金持股資料,並自行建立權重系統,經團隊審查後,結果比傳統做法更全面。此外,BAM 的首席經濟學家設定的 agent 工作流程,把一項例行的央行分析作業從約兩天縮短到約 30 分鐘,經濟學家仍保留審查與判斷的角色。

🎯 **給工程團隊的啟示**

BAM 的案例說明,導入前沿模型的關鍵不只是「換模型」,而是同步投資評測系統與治理架構:用貼近真實業務的可驗證任務取代通用 benchmark,並把權限控管、日誌追溯、人工審查機制建在 agent 執行環境的每一層,而不是寄望模型自我約束。正如 Flanagan 所說,今年的轉折點是「從人們擁有工具,變成擁有隊友」。

🔗 **來源**
- 標題：Working at the frontier: How Balyasny Asset Management evaluates and governs Claude Fable 5
- 作者／機構：Anthropic
- 連結：https://claude.com/blog/working-at-the-frontier-how-balyasny-asset-management-evaluates-and-governs-claude-fable-5

#Anthropic #ClaudeAI #ClaudeFable5 #AgenticAI #EnterpriseAI #FinTech #AIGovernance #ClaudeCode #AIagents #ResponsibleAI
