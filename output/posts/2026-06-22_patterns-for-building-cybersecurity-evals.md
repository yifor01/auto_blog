---
title: Patterns for Building Cybersecurity Evals
source: Eugene Yan
url: https://eugeneyan.com//writing/cybersecurity-evals/
score: 79
model: google/gemma-4-31b-it:free
generated_at: '2026-06-22T21:09:32.513501'
---

📌 如何評測 AI 的資安能力？建立 Cybersecurity Evals 的四個核心元件

TL;DR：透過沙盒環境、分級輸入與結果導向的評分機制，量化 AI 發現漏洞與利用漏洞的能力。

當我們將 AI Agent 引入資安領域，一個關鍵問題隨之而來：我們如何定義 AI 的資安能力？它在何時能真正幫助防禦者，又在何時會變成攻擊者的強大武器？要回答這個問題，不能僅靠簡單的對話測試，而需要一套嚴謹的評測框架（Evals）。

🤔 **衡量 AI 漏洞利用能力的挑戰**

評測資安能力的核心在於衡量模型是否能「發現」並「利用」安全漏洞。這不僅涉及程式碼分析，更包含在複雜網路環境中的操作能力。為了量化這種能力，目前的評測基準（Benchmarks）通常從簡單的 CTF（Capture-the-Flag）練習，延伸到在擁有 50 個主機的網路中進行資料外洩（Data Exfiltration）的複雜任務。

🧩 **資安評測框架的四個核心元件**

儘管不同的基準測試目標不同，但大多數資安評測都遵循一套由四個原語（Primitives）組成的設計模式：

1. **沙盒目標（Sandboxed Target）**
為了安全與可重複性，漏洞系統必須執行在 Docker 容器中。這可以是單一的漏洞程式碼容器，也可以是一個包含多個服務、資料庫與主機的模擬網路。

2. **影響難度的輸入（Inputs）**
透過調整提供給 AI 的資訊量，來模擬不同的攻擊情境：
- **最高難度（Zero-day 情境）**：僅提供漏洞程式碼，模擬漏洞與補丁均未知的狀態。
- **中等難度（One-day 情境）**：提供漏洞描述或補丁（Patch），模擬攻擊者透過逆向工程補丁來建構 exploit 的過程。
- **輔助提示**：提供崩潰追蹤（Crash trace）或可觸發漏洞的 PoC（Proof of Concept）以降低難度。

3. **工具集（Tools）**
AI Agent 需要適當的工具來執行任務，常見的工具包括：
- 基礎操作：Bash shell、讀寫工具。
- 分析工具：除錯器（Debuggers）、靜態分析器（Static analyzers）。
- 輔助功能：網路搜尋或用於追蹤長週期任務狀態的輔助服務。

4. **評分機制（Grader）**
由於漏洞利用的路徑是開放式的，評測通常採取「結果導向」而非「過程導向」。評分機制通常是決定性的（Deterministic），常見的成功定義包括：
- **記憶體漏洞（C/C++）**：成功觸發 Sanitizer 崩潰。
- **未授權程式碼執行**：成功獲取僅能透過漏洞利用才能存取的隱藏 Flag 字串。
- **審計機制**：透過自動化的紀錄審計（Transcript audits）來確認執行過程。

🎯 **實務啟示**

對於開發資安 AI 的工程師來說，建立評測時應將「難度」引數化。不要只測試 AI 能不能寫出 exploit，而應透過控制「輸入資訊」（從僅有 Code 到提供 Patch）來定義模型的能力邊界。同時，建立一個決定性的 Grader（如 Flag 檢索）比審查 AI 的思考過程更能準確衡量其在現實世界中的實戰效能。

🔗 **來源**
- 標題：Patterns for Building Cybersecurity Evals
- 作者／機構：Eugene Yan
- 連結：https://eugeneyan.com//writing/cybersecurity-evals/

#Cybersecurity #AI #LLM #Eval #Agent #Vulnerability #Docker #ZeroDay #CTF #SecurityEngineering
