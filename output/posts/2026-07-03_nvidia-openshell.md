---
title: NVIDIA/OpenShell
source: GitHub Trending
url: https://github.com/NVIDIA/OpenShell
score: 90
model: google/gemma-4-31b-it:free
generated_at: '2026-07-03T19:56:16.604419'
---

📌 NVIDIA OpenShell：為自治 AI Agent 打造的安全沙盒執行環境

TL;DR：提供一個受 YAML 策略管控的私有執行環境，防止 AI Agent 造成資料外洩或未經授權的系統存取。

當我們將 AI Agent 的許可權從「建議」提升到「執行」時，最大的風險隨之而來：你真的敢讓一個自治 Agent 直接在你的伺服器上執行指令嗎？

🤔 **防止 AI Agent 的「失控」風險**

NVIDIA 推出的 OpenShell 旨在解決自治 AI Agent 在執行任務時的安全問題。它提供了一個沙盒化的執行環境（Sandboxed Execution Environments），確保 Agent 在運作時不會危及基礎設施、洩漏憑證或非法存取敏感資料。

🧩 **以宣告式策略管控執行許可權**

OpenShell 的核心設計理念是「Agent-first」，其安全機制主要透過宣告式的 YAML 策略來治理：
- **存取控制**：防止未經授權的檔案存取。
- **資料保護**：防止資料外洩（Data Exfiltration）。
- **網路管控**：限制不受控的網路活動。

此外，專案已內建多項 Agent 技能，涵蓋從閘道器故障排除（Gateway Troubleshooting）到自動生成策略等功能，方便開發者直接呼叫。

⚠️ **目前仍處於 Alpha 階段的「單機模式」**

儘管目標是邁向多租戶的企業級部署，但目前的版本仍處於 Alpha 階段，處於所謂的「Proof-of-life」狀態。目前的限制如下：
- **單人模式**：僅支援單一開發者、單一環境與單一閘道器。
- **開發狀態**：作者明確提醒目前仍有許多「粗糙之處」（Rough edges）。
- **K8s 支援**：Helm chart 目前屬於實驗性功能，且處於積極開發中，可能會有重大變更。

🎯 **實務啟示：如何快速部署測試**

對於想要嘗試讓 AI Agent 安全執行指令的工程師，可以透過以下方式快速啟動：
- **環境需求**：支援 macOS、Linux 或 Windows (需安裝 WSL 2)，並需安裝 Docker、Podman 或開啟主機虛擬化（以支援 MicroVM 沙盒）。
- **安裝方式**：
    - 推薦使用 Binary 安裝：`curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh`
    - 或透過 PyPI 安裝：`uv tool install -U openshell`

🔗 **來源**
- 標題：NVIDIA/OpenShell
- 作者／機構：NVIDIA
- 連結：https://github.com/NVIDIA/OpenShell

#NVIDIA #OpenShell #AIAgents #Sandboxing #CyberSecurity #AIInfrastructure #OpenSource #DevOps #YAML #AutonomousAgents
