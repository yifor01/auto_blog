---
title: Setting up your spare Mac for Claude Code to control, a step-by-step guide
source: Hacker News
url: https://ykdojo.github.io/claude-controls-mac/
score: 66
model: tencent/hy3:free
generated_at: '2026-07-19T08:07:37.328505'
---

📌 【實戰指南】把閒置 Mac 交給 Claude Code 全權控管

TL;DR：逐步教學把備用 Mac 設成常駐機，用手機或 SSH 遠端指派 Claude Code 任務。

你手邊那臺吃灰的舊 Mac，其實可以變成一臺「永遠線上、Claude Code 能完全控制」的獨立工作站。作者 ykev 在 Hacker News 分享的完整教學，正是要解決「不想在主機上冒險跑 AI 代理」的痛點。

🤔 **為什麼不直接在主機上跑 Claude Code？**

Claude Code 在加上 `--dangerously-skip-permissions` 旗標、跳過許可權確認後，確實能更自主地做事，但在日常使用的主 Mac 上跑，本身就帶有風險。作者想建立一個分離的環境，把「某些研究任務、開發任務」委派給專門的機器，而不碰自己的主力裝置。

🧩 **備用 Mac 當作獨立可控環境的設計理念**

這份指南的核心想法是：用一臺備用 Mac 搭出 Claude Code 能完全控制、且啟用 computer use 的常駐環境。好處有兩個：一是隔離風險，把 Claude Code 能存取的範圍限制在這臺獨立機器上；二是隨時可從手機上的 Claude app 對話下指令，或從主 Mac 透過 SSH 連過去操作。

作者提到，他個人更偏好在手機上跟 Claude Code 講話、而不是用一般的 Claude 行動版，因為 Claude Code 往往能力更強、能實際動手做事。

💡 **關於容器化方案的取捨**

作者表明自己是「在容器（container）裡跑 Claude Code」的擁護者，甚至做過一整套方便這樣做的環境。但他發現容器方案有幾個限制（摘要在此處截斷，未說明具體限制內容），因此才轉向用實體備用 Mac 建立分離環境的做法。

🎯 **實務啟示**

如果你手邊正好有一臺閒置 Mac，又常想把耗時或高風險的開發／研究任務丟給 AI 代理自己跑，這篇指南提供了一個低門檻的隔離架構思路：把代理鎖在獨立機器上，主機安全、手機也能隨時遙控。入門者可以依此類推到任意兩臺機器的組合，不一定侷限 Mac 對 Mac。

🔗 **來源**
- 標題：Setting up your spare Mac for Claude Code to control, a step-by-step guide
- 作者／機構：ykev
- 連結：https://ykdojo.github.io/claude-controls-mac/

#ClaudeCode #Mac #AIagent #computeruse #SSH #remotecontrol #devops #LLM #automation #separateenvironment
