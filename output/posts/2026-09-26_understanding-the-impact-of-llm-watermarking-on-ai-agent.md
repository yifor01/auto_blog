---
title: Understanding the Impact of LLM Watermarking on AI Agent Behavior
source: Hacker News
url: https://www.lasso.security/blog/the-provenance-tax-understanding-the-impact-of-llm-watermarking-on-ai-agent-behavior
model: claude-code/sonnet
generated_at: '2026-09-26T19:55:53.672505'
score: 84
---

📌 浮水印藏在文字裡,卻可能悄悄改變Agent的行動

TL;DR:研究發現LLM浮水印會改變token取樣結果,連帶影響Agent的工具呼叫正確率與模型拒絕回答的行為。

當Anthropic宣布未來的Claude模型會在輸出中嵌入不可見浮水印時,多數人聯想到的是「防偽溯源」。但Lasso Security的研究團隊提出一個容易被忽略的問題:浮水印技術改變的是模型產生每一個token的方式,而這個改變,可能悄悄影響Agent實際呼叫哪個工具、傳入什麼參數。

🤔 為什麼浮水印不只是「加個標記」這麼簡單

背景是Anthropic宣布未來Claude模型將嵌入不可見浮水印,並揭露該技術基於Google DeepMind的SynthID-Text。文字浮水印本身不是新技術,但其部署如今具有監理意義:歐盟AI法案第50(2)條要求生成合成文字的AI系統提供者,必須以機器可讀格式標記輸出,並使其能被偵測為AI生成或操縱的內容。研究團隊指出,浮水印雖然是為了溯源而設計,但SynthID-Text實際上改變了模型產生每個下一個token的過程。在模型層級,這可能影響安全行為,包括模型是否拒絕有害請求,以及該拒絕在prompt injection下是否依然成立;在Agent層級,同樣被取樣改變的token,也可能決定Agent呼叫哪個工具、傳入什麼參數。研究團隊將這種行為層面的影響稱為「sampling drift(取樣漂移)」。

🧩 用「錦標賽取樣」嵌入浮水印,原理與實驗設計

文字浮水印的做法包括後處理式方法,以及直接整合進LLM生成過程的方法,後者又包含logits偏置、無失真的加密取樣、具密碼學動機的建構方式,以及SynthID-Text所採用的「Tournament取樣」。研究團隊採用的是SynthID的非失真(non-distortionary)設定:這種設定保證在浮水印隨機性之上,期望值會維持原始token分布不變,但在固定的浮水印金鑰下,個別生成結果仍可能不同。研究引用Dathathri等人的說法,指出在近兩千萬次Gemini回應的測試中未觀察到可量測的品質下降。

團隊採用配對式(paired)實驗設計,涵蓋兩項測試:工具呼叫使用BFCL v4 single-turn AST基準;拒絕行為則使用200則HarmBench有害請求,加上100則JailbreakBench良性對照組,並分別在「原始請求」與「加上一種固定的prompt injection手法」兩種情境下測試。浮水印實作採用HuggingFace未經修改的SynthIDTextWatermarkLogitsProcessor,設定為30層Tournament、n-gram長度5、取樣表大小2的16次方、上下文歷史長度1024。每一筆測試項目都會在相同種子、批次組成與順序下,分別產生有浮水印與無浮水印兩個版本,確保浮水印處理器是唯一變因。

📊 淨準確率變化不大,但「翻盤率」高得多

結果顯示,在需要呼叫工具的測試項目中,加入浮水印後,7個模型裡有6個準確率下降,其中4個下降幅度達到統計顯著。但研究團隊強調,單看整體準確率的淨變化容易產生誤導:一筆原本正確的呼叫變錯誤,可能剛好被另一筆原本錯誤變正確的呼叫抵銷,導致整體數字看起來變化不大,實際上模型在兩筆項目上的行為都已改變。

為此,團隊另外量測「配對不一致率」(churn),即同一測試項目在有無浮水印兩種條件下,判定結果不同的比例。以BFCL中1,150筆固定的non-live呼叫項目為例,在溫度T=1.0時,phi-4有16.8%的呼叫判定結果因浮水印而改變,但其淨準確率僅下降2.87分;Llama-3.1-8B也呈現相同模式,9.9%的判定結果改變,淨準確率卻只掉了0.87分。橫跨21組「模型×溫度」組合,churn平均達6.5%,且其bootstrap信賴區間在每一組合中都不包含零。

💡 深入分析:結構化輸出的「不確定位置」最容易被影響

研究指出,Tournament取樣在模型本身不確定的地方,更有機會改變token選擇結果。在JSON等結構化輸出中,大括號、鍵名、函式名稱通常高度可預測,但查詢字串、數字、路徑、收件人等數值型參數的不確定性較高。這意味著,一個在一般文字中只會造成用詞小差異的變動,放到Agent的工具呼叫參數上,就可能變成執行了錯誤的動作。研究也特別強調,「非失真」保證是針對浮水印隨機性的期望值而言,固定金鑰下的實際取樣仍會改變,而且效果會因模型與金鑰不同而異。

⚠️ 限制

研究團隊指出,浮水印造成的行為變化是模型與金鑰相依的,且在聚合分數(net accuracy)中容易被方向相反的變化互相抵銷所掩蓋,因此他們同時報告淨效能與配對不一致率兩種指標,以避免結論被平均數字誤導。

🎯 實務啟示

對正在或計畫部署具浮水印LLM作為Agent推理核心的團隊而言,這項研究提醒:即使供應商保證浮水印「不失真」,也不代表在固定金鑰下每次生成結果完全一致。若Agent的工具呼叫涉及金額、路徑、收件人等高風險參數,建議在導入浮水印模型前後,針對關鍵任務進行配對式的行為一致性測試,而不只是看整體準確率是否下降。

🔗 來源
- 標題:Understanding the Impact of LLM Watermarking on AI Agent Behavior
- 作者/機構:Andrea Siposova(Lasso Security)
- 連結:https://www.lasso.security/blog/the-provenance-tax-understanding-the-impact-of-llm-watermarking-on-ai-agent-behavior

#LLMWatermarking #SynthID #AIAgents #AISafety #PromptInjection #ToolCalling #ResponsibleAI #EUAIAct #MachineLearning #AIAlignment
