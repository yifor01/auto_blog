---
title: NVIDIA/NemoClaw
source: GitHub Trending
url: https://github.com/NVIDIA/NemoClaw
score: 98
model: google/gemma-4-31b-it:free
generated_at: '2026-06-24T20:03:16.728631'
---

📌 【NVIDIA 開源】NemoClaw：為常駐型 AI Agent 打造的沙盒化安全執行堆疊

TL;DR：NVIDIA 提供一套參考堆疊，讓 AI Agent 在 OpenShell 沙盒中安全執行，並整合生命週期管理與網路策略。

當 AI Agent 從「對話視窗」轉向「常駐執行（Always-on）」時，最核心的風險在於：如何讓 Agent 在執行自動化任務時，不會對宿主系統造成不可預期的損害？

🧩 **透過 OpenShell 沙盒實現安全隔離**

NVIDIA 推出的 NemoClaw 是一個開源的參考堆疊（Reference Stack），其核心目標是讓 AI Agent 能在 NVIDIA OpenShell 沙盒中更安全地執行。它不只提供隔離環境，還將複雜的部署流程整合進單一 CLI 中，包含以下關鍵能力：

- 導引式啟動（Guided Onboarding）：簡化開發者進入門檻。
- 硬化藍圖（Hardened Blueprint）：提供經過安全加固的部署配置。
- 路由推論（Routed Inference）：管理推論請求的流向。
- 網路策略（Network Policy）與生命週期管理：精準控制 Agent 的網路許可權及其執行生命週期。

⚙️ **支援多種 Agent 框架與快速啟動**

NemoClaw 提供靈活的 Agent 選擇，使用者可根據需求切換不同的執行核心：

- **OpenClaw**：系統預設的 Agent。
- **Hermes**：安裝前設定 `NEMOCLAW_AGENT=hermes` 或使用 `nemohermes` 別名即可啟動。
- **LangChain Deep Agents Code**：針對 LangChain 生態系的深度 Agent 支援。

🎯 **實務啟示：從「能執行」轉向「安全執行」**

對於開發 AI Agent 的工程師而言，NemoClaw 的價值在於將「沙盒隔離」與「生命週期管理」標準化。開發者不再需要自行設計複雜的隔離層，而是可以直接利用其硬化藍圖與網路策略，將 Agent 限制在受控環境中，這對於需要執行程式碼（Code Execution）或長期執行的自動化 Agent 來說，是降低系統風險的必要基礎設施。

🔗 **來源**
- 標題：NVIDIA/NemoClaw
- 作者／機構：NVIDIA
- 連結：https://github.com/NVIDIA/NemoClaw

#NVIDIA #AIAgents #OpenShell #Sandbox #CyberSecurity #OpenSource #LangChain #AIInfrastructure #NemoClaw #AgentLifecycle
