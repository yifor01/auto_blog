---
title: 'Agent Seer: Synthesizing Scenarios from Specification Understanding'
source: Apple ML
url: https://machinelearning.apple.com/research/agent-seer-synthesizing-scenarios
model: claude-code/sonnet
generated_at: '2026-08-28T18:00:47.219774'
score: 105
---

📌 不用人工寫案例,靠工具規格就能生成 Agent 測試場景

TL;DR:Apple ML 提出 Agent Seer,只讀一份 MCP 工具規格就能自動合成多輪對話評測場景,免除人工標註。

每次工具 API 一改版,人工手寫的 agent 評測集可能就跟著過期。當你的 agent 要串接的工具生態系越來越大,靠人力寫測試場景這件事,本質上就不可能跟得上。

🤔 **靜態 benchmark 追不上會演化的 API**

評測會呼叫外部工具的 AI agent,需要能反映真實使用情境的測試場景,包含實務上工具如何被組合使用、以及跨對話輪次的迭代過程。但用人工方式建構這類場景,需要深厚的領域知識,難以在不同工具生態系間規模化,而且做出來的 benchmark 是靜態的,無法追蹤持續演化的 API。作者觀察到,工具規格本身,包括函式名稱、自然語言描述、以及型別化的參數 schema,其實已經蘊含足夠的語意資訊,可以用來合成真實的評測場景,不需要人工整理,也不需要實際執行工具。

🧩 **從一份 MCP 規格,不靠範例、不靠實際執行**

Agent Seer 就建立在這個觀察之上:只需要一份 Model Context Protocol(MCP)規格,不需要任何範例、不需要即時的工具存取權限、也不需要針對特定領域做調校。整條 pipeline 的運作方式是:先對原始 schema 做語意上的補充強化,接著生成分級的場景並搭配合成的工具輸出結果,最後再把這些場景擴展成以模擬資料為基礎的多輪對話,呈現出良好的工具呼叫正確性與對話連貫性。

📊 **參數 schema 複雜度,是品質落差的最強相關因素**

研究團隊把這套 pipeline 套用在七份涵蓋不同領域、不同工具數量規模的 MCP 規格上,測量工具呼叫正確性與對話連貫性。結果顯示 pipeline 在所有領域都維持不錯的品質,在中小型規格上更達到完整的工具涵蓋率。分析中浮現兩個重點發現:一是參數 schema 的複雜度,是評測品質落差的最強相關因素,相較之下工具數量規模的影響較小、且是獨立於前者的另一個變因;二是在品質不完美的場景中,參數數值準確度(argument value accuracy)才是主要的失敗模式,而這是傳統粗粒度的「名稱比對」指標完全看不到的問題。

💡 **粗粒度指標會漏掉真正的錯誤**

這個發現值得注意的地方在於,如果評測只看工具名稱是否叫對,會誤以為場景品質很高,但實際上模型可能只是「叫對工具、傳錯參數值」,這種錯誤在生產環境中一樣會導致任務失敗,卻不會被傳統的 name-match 指標抓到。

🎯 **實務啟示**

如果你的團隊正在為工具呼叫型 agent 建立評測集,與其花人力逐一撰寫多輪對話腳本,更值得思考的是能不能直接從既有的工具規格(尤其是 MCP 這類已經結構化的 schema)反推出評測場景;同時評測指標也不能只停在工具名稱比對,參數數值層級的正確性才是真正該盯緊的環節。

🔗 **來源**
- 標題:Agent Seer: Synthesizing Scenarios from Specification Understanding
- 作者/機構:Harish Karumuri, Mahesh Vemula, David Lopes Pegna(Apple ML)
- 連結:https://machinelearning.apple.com/research/agent-seer-synthesizing-scenarios

#AIAgent #MCP #ToolCalling #Evaluation #LLMAgents #AppleML #BenchmarkDesign #ConversationalAI #SyntheticData #AgentEvaluation
