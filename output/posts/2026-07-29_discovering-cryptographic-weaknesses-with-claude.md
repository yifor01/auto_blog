---
title: Discovering cryptographic weaknesses with Claude
source: Anthropic Research
url: https://www.anthropic.com/research/discovering-cryptographic-weaknesses
model: tencent/hy3:free
generated_at: '2026-07-29T14:06:52.193394'
pinned: true
---

📌 【Anthropic 研究】Claude 突破實作層面，開始能發現密碼學演算法本身的數學漏洞

TL;DR：Anthropic 研究人員利用 Claude Mythos Preview 發現了密碼學演算法的數學缺陷，而非僅僅是程式碼實作錯誤。

🔐 **從「實作錯誤」演進到「數學漏洞」**

過去，當我們利用 Claude 針對加密函式庫（Cryptographic libraries）進行紅隊演練時，發現的漏洞多半源於「實作錯誤」——也就是程式設計師在呼叫演算法時的錯誤用法。但透過 Claude Mythos Preview，研究人員現在能發現演算法本身的數學缺陷，這對數位安全的基礎構建提出了新的挑戰。

🧩 **兩項重大的研究發現**

研究人員利用 Claude 發現了兩種攻擊加密演算法的新方法，這些發現代表了 AI 在密碼學研究領域的重大進展：

- **攻擊後量子數位簽章方案 HAWK**：第一項攻擊顯著削弱了 HAWK，這是一種專為後量子時代（Post-quantum world）設計的數位簽章方案。
- **攻擊輪數減少後的 AES**：第二項研究則識別出一種攻擊「輪數減少版 AES（round-reduced AES）」的新方法。AES 是目前全球使用最廣泛的對稱加密算法（Symmetric cipher）。

⚠️ **目前不影響實際生產系統**

儘管這些發現具備重大的研究價值，但作者強調，這些漏洞目前並不會影響任何現有的生產系統。

💡 **數位安全的新挑戰**

密碼學是數位安全的基石。從瀏覽器檢查網站身分的數位簽章方案，到確保通訊隱私的對稱加密，若這些系統失效，電子郵件與網路銀行等服務將面臨駭客攔截或竄改的風險。隨著強大 AI 模型的出現，如何應對 AI 可能發現的演算法數學漏洞，將成為密碼學領域的重要議題。

🔗 **來源**
- 標題：Discovering cryptographic weaknesses with Claude
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/research/discovering-cryptographic-weaknesses

#AI #Cryptography #Anthropic #Claude #Cybersecurity #PostQuantum #AES #HAWK #RedTeaming #MachineLearning
