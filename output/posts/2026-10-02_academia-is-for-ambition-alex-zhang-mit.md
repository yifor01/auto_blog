---
title: Academia is for Ambition — Alex Zhang, MIT
source: Latent Space
url: https://www.latent.space/p/rlm
model: claude-code/sonnet
generated_at: '2026-10-02T21:38:26.865823'
score: 81
---

📌 MIT學者談RLM：模型外的「哈尼斯」才是關鍵

TL;DR：Alex Zhang從GPU kernel優化談到遞迴語言模型與代理群，核心論點是包裝模型的系統設計才是能力上限所在。

如果現在的前沿模型其實還有大量能力被浪費在原始的系統設計裡，那麼真正的突破點，或許不在下一個更大的模型，而在包住模型的那層「殼」。

🤔 從GPU Mode到RLM的研究路徑

Alex Zhang是MIT博士生，同時活躍於GPU Mode社群(前身為CUDA Mode，由Mark Saroufim、Andreas與Jeremy Howard發起，最初是一個教人寫GPU kernel的Discord)。他在Snapchat實習、對推薦系統工作感到無聊時，因為嘗試為Google的Infinite Attention論文寫專用kernel而加入社群，進而參與催生了KernelBench，一個測試LLM能否自動化生成GPU kernel的基準。Latent Space這次專訪延續他們挖掘「新星博士生」的傳統，前兩年分別介紹了後來打造OpenAI Operator、現任騰訊首席AI科學家的Shunyu Yao，以及共同創辦估值6億美元Engram的Jack Morris。

🧩 RLM：讓模型自己管理上下文與子代理

今年稍早，Zhang提出的Recursive Language Models(RLM，遞迴語言模型)概念在社群內引發討論，核心想法包括context offloading(上下文卸載)、程式化的子代理呼叫，以及共享記憶的持久子代理(persistent subagents)。根據Latent Space的描述，一個基於RLM的任務執行框架是最早「近乎解出」ARC-AGI-3的方案，時間甚至早於OpenAI的Astra。訪談中也談到Prime Agent、持久化的代理間溝通，以及一個更激進的想法：未來你所查詢的「語言模型」，底層可能其實是一整群看不見的代理(agent swarm)在協同運作，只是對外呈現一個簡單的介面。

💡 代理群背後的規模與浪費

Latent Space提到OpenAI曾做過一次上萬代理(10,000-agent)規模的實驗，輸出token量達1,300億(130B)，相當於投入約4,000萬美元等值的運算去解決問題。但對談中也點出，這類大規模代理群當中很大一部分搜尋其實是浪費的，讓多個代理的結果收斂(convergence)仍是困難的問題。訪談同時比較了Kimi與OpenAI在多代理系統上的不同取向，並提及Sakana AI在開放式(open-ended)生成與「從大量產出中找出隱藏寶石」方向上的探索。另一個被提出的觀點是「能力過剩(capability overhang)」：現有前沿模型可能已經具備遠超目前任務設計所釋放的能力，推測性的程式化工具呼叫與重疊工具執行等做法，都是試圖把這部分能力榨出來的方向。對談最後也拋出一個開放問題：英文、程式碼、還是某種全新的「Neuralese」，才是真正限制模型推理方式的語言載體。

🎯 給工程師的啟示

Zhang的核心論點值得工程團隊借鏡：Claude Code、Codex、Pi這類工具在結構上其實相似度很高，真正拉開差距的往往不是底層模型，而是任務執行框架(harness)的設計，也就是它如何做組合式的泛化(compositional generalization)。與其一味等待更強的模型，不如投資在如何設計更好的上下文管理、子代理協作與任務邊界。

🔗 來源
- 標題：Academia is for Ambition — Alex Zhang, MIT
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/rlm

#RLM #RecursiveLanguageModels #AgentSwarm #GPUMode #KernelBench #AIAgents #LLM #MIT #CapabilityOverhang #AIResearch
