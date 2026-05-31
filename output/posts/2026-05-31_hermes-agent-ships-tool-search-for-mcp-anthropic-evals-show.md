---
title: "Hermes Agent Ships Tool Search for MCP: Anthropic Evals Show 49% to 74% Accuracy Gain on Opus 4"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/29/hermes-agent-ships-tool-search-for-mcp-anthropic-evals-show-49-to-74-accuracy-gain-on-opus-4/
score: 107
model: tencent/hy3-preview:free
generated_at: 2026-05-31T19:26:54.459720
---

📌 **Hermes Agent Ships Tool Search for MCP: 49‑74% Accuracy Gain on Opus 4**

You’ve probably noticed AI agents slowing down when they’re hooked up to dozens of MCP tools—every turn drags in tens of thousands of token‑heavy schema definitions.  
What if the model only loaded the tools it actually needed, on demand?  
Hermes Agent’s new Tool Search does exactly that, cutting schema overhead by up to 85% and boosting accuracy on Opus 4 by nearly three‑quarters.

🤔 **Why MCP tool overload matters**  
When multiple MCP servers are attached to an agent, each tool’s JSON schema is sent to the model on every turn, even if only a handful of tools are used. In a real‑world deployment with five MCP servers and 34 tools, the average prompt size balloons to ~45 000 tokens per turn, of which roughly 22 000 tokens (≈50 %) are pure schema overhead. Anthropic’s internal measurements show that unoptimized tool definitions can consume as many as 134 000 tokens, creating a “MCP Tools Tax” of 15 000‑60 000 tokens per turn. This bloated context not only wastes compute but also triggers decision paralysis: the model struggles to pick the right tool from a long list of irrelevant options, leading to false positives.

🧪 **How Tool Search works**  
Tool Search is an opt‑in, progressive‑disclosure layer for MCP and non‑core plugin tools. Instead of uploading every tool schema upfront, the model keeps only three bridge tools visible in its tool array. At runtime, the model:  

1. Searches the bridge set for the functionality it needs.  
2. Loads the full schema of the selected underlying tool on demand.  
3. Invokes the real tool, while all hooks, guardrails, and approval checks still reference the original tool name—not the bridge.  

Because the heavy schema definitions are fetched only when required, the token cost per turn drops dramatically. Anthropic’s data reports an **85 % reduction** in tool‑definition token usage while preserving full access to the entire tool catalog.

📈 **Core finding: accuracy uplift on Opus 4**  
By stripping away unnecessary tool choices from the context window, Tool Search alleviates decision paralysis. According to Anthropic’s internal MCP evaluations, this translates into a **49 %‑74 % accuracy gain** on the Opus 4 benchmark, depending on the tool density of the deployment.

💡 **Why the gain happens**  
The improvement is two‑fold:  

* **Token efficiency** – fewer schema tokens mean more space for actual task‑relevant information, allowing the model to reason longer without hitting context limits.  
* **Cleaner decision space** – with irrelevant tool definitions hidden, the model’s probability mass concentrates on the truly applicable options, reducing mistaken tool selections and the associated error propagation.

⚠️ **Known limitations**  
* The reported numbers come from Anthropic’s internal MCP evals; external benchmarks may vary.  
* Tool Search introduces an extra lookup step (search → load → call), which adds a small latency overhead that was not quantified in the source material.  
* The feature is currently opt‑in; existing workflows must be updated to enable the bridge‑tool pattern.

🎯 **Practical takeaways for engineers**  
* If you run agents with many MCP servers (e.g., >3 servers or >20 tools), enable Tool Search to cut schema token consumption by up to five‑fold.  
* Monitor latency; the search‑load call is usually negligible compared with the savings in prompt processing time.  
* Combine Tool Search with existing MCP best practices (versioned schemas, scoped tool sets) to keep both token usage and reliability under control.

🔗 **Reference**  
📄 Article: Hermes Agent Ships Tool Search for MCP: Anthropic Evals Show 49% to 74% Accuracy Gain on Opus 4  
🔗 https://www.marktechpost.com/2026/05/29/hermes-agent-ships-tool-search-for-mcp-anthropic-evals-show-49-to-74-accuracy-gain-on-opus-4/  

#HermesAgent #MCP #ToolSearch #AIAgents #Opus4 #NousResearch #Anthropic #LLMOps #TokenOptimization
