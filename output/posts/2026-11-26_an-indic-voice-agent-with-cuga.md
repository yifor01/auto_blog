---
title: An Indic Voice Agent with CUGA
source: HuggingFace Blog
url: https://huggingface.co/blog/ibm-research/an-indic-voice-agent-with-cuga
model: claude-code/sonnet
generated_at: '2026-11-26T01:10:18.917747'
score: 76
---

📌 跨語言檢索才是硬仗：用 CUGA 打造印度語音農業助手

TL;DR：IBM Research 用開源 agent harness CUGA 搭出印地語／泰米爾語等語音農業助手，真正的難點不是語音，是跨語言向量檢索。

大多數有用的知識都是用英文寫下並數位化的，但真正需要這些知識的人，說的、想的卻是印地語、坦米爾語、泰盧固語這類區域語言，而且他們更想用說的，不想用打的。IBM Research 做了一個小型語音 agent 來補上這個落差，而且發現真正難搞的部分完全不是語音辨識。

🤔 **場景：農夫用母語問一句話，答案要可查證**

這個 Farm Assistant 的使用流程是這樣的：農夫用自己的語言口頭提問，例如如何分辨好種子和壞種子；agent 把語音轉成文字，搜尋一份 154 頁、以英文撰寫的農業手冊，用提問時使用的語言給出兩到四句語音回答，只根據手冊內容作答，同時附上可查證的來源頁碼並唸出答案。如果有人問起板球或寫程式，它會禮貌地把話題帶回農業，而不是硬掰答案。

🧩 **CUGA 只是一顆「純文字進、純文字出」的大腦**

CUGA（ConfigUrable Generalist Agent）是 IBM Research 開源的 agent harness，負責處理模型串接、工具管理、狀態與護欄，開發者只需要寫工具和 prompt，不用自己實作 agent 迴圈。在這個專案裡，CUGA 承擔三件事：一是模型可替換，透過一個設定值就能在 watsonx 和 OpenAI 之間切換；二是知識引擎，用 `agent.knowledge.search()` 在本地解析、切塊、embedding 並搜尋 PDF；三是對話 thread 管理，每個問題都開新的 thread，避免不同使用者的語言或上下文互相汙染。

整個系統的設計思路可以用一行文字流程表示：

語音 → 語音轉文字 → knowledge.search → CUGA（基於檢索內容作答）→ 文字轉語音 → 語音

因為 CUGA 本身只處理文字，團隊可以先用純文字測試並打磨 agent，再疊上「耳朵」和「嘴巴」這兩層。語音供應商也可以自由替換：一種是直接從瀏覽器呼叫 Sarvam AI 的雲端語音 API，另一種是在自己的伺服器上跑開源模型（語音轉文字用 SraVaani，文字轉語音用 Svara）。

💡 **真正的硬仗：印地語問題要能找到英文段落**

語意檢索的運作方式是把文字轉成向量，再找出最接近的段落。但 CUGA 預設的 embedding 模型是英文專用的，碰到印地語或坦米爾語問題時，轉出來的向量幾乎不帶有效語意。結果是系統依然會回傳五段內容，只是全部答非所問；而模型被正確要求「只根據提供的內容回答」，於是會很乾脆地回「手冊沒有提到這個」。整條鏈路上每一層都「正常運作」，沒有任何錯誤或警告，問題卻悄悄地發生了。

解法是換用多語言 embedding 模型（團隊採用 `intfloat/multilingual-e5-large`），讓同樣的語意無論用哪種語言表達都落在向量空間的相近位置，概念上並不複雜，但要接進 CUGA 需要一點額外的工作（教學文件中有說明）。換過之後，一份英文文件就能服務所有語言，不需要為每種語言各自維護一份翻譯版本。團隊給的建議是：在調整任何 prompt 之前，先用非英文語言問一個問題，確認系統有找到正確的頁面。

🎯 **讓回答聽起來自然、而且守住邊界**

幾個小決定對最終體驗影響不小：prompt 要求模型不要輸出 Markdown、條列符號、引用標籤或「小米（बाजरा）」這類括號翻譯，因為這些東西唸出來會很奇怪，另外還有一層輕量格式化器會把漏網的部分再濾掉一次；護欄設計上，簡單的輸入檢查就能攔住明顯離題的問題，萬一漏網，模型會在回覆開頭輸出 `OFF_TOPIC`，由應用程式換成禮貌的引導語，全程不需要再呼叫一次 LLM，語音互動的回應速度才能維持；至於金鑰安全，使用 Sarvam 選項時瀏覽器直接對 Sarvam 通訊，伺服器端只收到文字，完全不會接觸到使用者的金鑰。

⚠️ **這個架構並不只適用於農業**

團隊表示，只要換掉手冊內容，例如改成福利政策文件、衛生宣導或法律指南，就能變成完全不同的助手；換掉語音供應商，也能在「雲端換取速度」與「地端部署換取資料主權」之間切換，不需要重寫 agent 本身。文章也提到這套做法與 IBM Bharat Core（建構在 IBM Sovereign Core 之上、針對印度生態系最佳化的 AI 堆疊）的定位相互銜接，適合需要資料主權的場景，例如地方語言 KYC 系統或多語言政府服務機器人，但這部分屬於產品方向說明，並非本文的技術實作細節。

🔗 **來源**
- 標題：An Indic Voice Agent with CUGA
- 作者／機構：IBM Research（HuggingFace Blog）
- 連結：https://huggingface.co/blog/ibm-research/an-indic-voice-agent-with-cuga

#VoiceAgent #CUGA #MultilingualAI #RAG #CrossLingualRetrieval #AgentHarness #IBMResearch #SpeechToText #OpenSourceAI #IndicLanguages
