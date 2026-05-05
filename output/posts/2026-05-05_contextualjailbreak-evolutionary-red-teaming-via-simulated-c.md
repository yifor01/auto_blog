---
title: "ContextualJailbreak: Evolutionary Red-Teaming via Simulated Conversational Priming"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.02647
score: 107
model: tencent/hy3-preview:free
generated_at: 2026-05-05T19:56:23.674423
---

📌 【IBM Research 聯合穆爾西亞大學】多轮演化红队突破LLM安全防线

現有自動化紅隊大多鎖定單輪 Prompt 攻擊，多輪對話的安全防護被認為更難突破？最新研究用演化搜索模擬對話引導，在 3 款主流開源模型上達成 100% 越獄成功率，閉源前沿模型也幾乎全面失守，僅有 Claude 系列倖免。

🤔 **自動化紅隊侷限單輪，多輪對話引導成攻擊盲區**
大型語言模型（LLM）至今仍易受越獄攻擊影響，這類攻擊會繞過安全對齊機制、誘發有害回覆。現有研究已證實，上下文引導（contextual priming，即透過前序對話隱性偏誤後續回覆）是極具威脅的攻擊面，手工設計的多輪對話支架效果穩定優於單輪操弄。但現有自動化優化紅隊大多侷限於單輪場景，僅針對靜態 Prompt 迭代，無法推理何種形式的對話引導會誘發模型輸出有害內容。近期雖有多輪搜尋式方法嘗試補足缺口，但有效引導對話的突變算子設計空間仍未被充分探索。

🧪 **演化搜索+5類突變算子+分級在環評分機制**
本研究提出 ContextualJailbreak，一種黑盒紅隊策略，針對模擬的多輪引導對話執行演化搜索。該策略採用兩級評判模型給出的 0-5 分危害評分作為環內訊號，不會直接丟棄部分有害的回覆，而是將其用於引導後續搜索方向。搜索過程由 5 種語義定義的突變算子驅動：角色扮演（roleplay）、場景設定（scenario）、內容擴展（expand）、故障排查（troubleshooting）、機制解釋（mechanistic），其中後兩者為本研究首次提出。

🔍 **3款開源模型越獄成功率100%，優於基線31-96個百分點**
研究在 50 種 HarmBench 代表行為上進行測試，結果顯示：ContextualJailbreak 在 gpt-oss:20B、qwen3-8B、llama3.1:70B 上的攻擊成功率（ASR）均達 100%，在 gpt-oss:120B 上也達到 90%。與 4 種單輪、多輪基線方法相比，本方法平均攻擊成功率高出 31 至 96 個百分點。

💡 **攻擊可跨模型遷移，廠商安全對齊差異顯著**
研究進一步測試攻擊的遷移性：針對 gpt-oss:120B 發現的 40 個最強有害攻擊，無需任何適配即可遷移至閉源前沿模型，其中 gpt-4o-mini 成功率達 90%，gpt-5 達 70%，gemini-3-flash 達 70%。但 Claude 系列模型表現出極強的防禦能力，claude-opus-4-7 成功率僅 17.5%，claude-sonnet-4-6 僅 15%，顯示不同廠商的模型在安全對齊魯棒性上存在顯著落差。

🎯 **安全團隊需強化多輪防護，關注廠商差異**
對於 GenAI 工程師與安全研究者而言，該框架的演化搜索邏輯、新型突變算子設計與分級在環評分機制，顯著推進了自動化多輪越獄優化的邊界。實務上可參考該方法補足多輪對話場景的紅隊測試覆蓋，同時針對不同廠商模型的防禦差異，制定更具針對性的安全對齊策略。

🔗 **論文連結**
📝 論文標題：ContextualJailbreak: Evolutionary Red-Teaming via Simulated Conversational Priming
👤 作者：Mario Rodríguez Béjar, Francisco J. Cortés-Delgado, S. Braghin, Jose L. Hernández-Ramos
🏫 所屬機構：Universidad de Murcia; IBM Research
🔗 論文連結：https://arxiv.org/abs/2605.02647
📚 來源：ChatPaper/Computation and Language

你的團隊在做 LLM 安全測試時，是否覆蓋了多輪對話場景？歡迎分享實務經驗 👇

#AI安全 #LLM #红队测试 #越狱攻击 #IBMResearch #生成式AI #穆尔西亚大学 #安全对齐
