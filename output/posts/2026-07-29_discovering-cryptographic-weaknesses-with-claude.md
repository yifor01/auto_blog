---
title: Discovering cryptographic weaknesses with Claude
source: Anthropic Research
url: https://www.anthropic.com/research/discovering-cryptographic-weaknesses
model: tencent/hy3:free
generated_at: '2026-07-29T08:27:42.892017'
pinned: true
---

📌 【Anthropic 研究】Claude 能發現演算法本身的數學缺陷，而不僅僅是實作錯誤

TL;DR：Anthropic 發現 Claude 能自主發現加密演算法的數學漏洞，對抗量子計算的 HAWK 與 AES 均受影響。

當我們討論 AI 安全時，通常關注的是 AI 是否會產生惡意程式碼，或是 AI 輔助攻擊軟體漏洞。但 Anthropic 的最新研究顯示，AI 的威脅層級正在進化：它不再只是發現程式碼寫錯（Implementation errors），而是能直接從數學邏輯上找出加密演算法本身的設計缺陷。

🤔 **從「寫錯程式碼」進化到「發現數學漏洞」**

過去透過 Claude Mythos Preview 進行紅隊演練（Red Teaming）時，AI 發現的漏洞大多屬於「實作錯誤」——也就是工程師在呼叫加密函式庫時，寫錯了參數或邏輯。

然而，這次研究取得重大突破：Claude 已展現出發現演算法本身數學缺陷的能力。這意味著即便程式碼寫得完全正確，如果演算法本身的數學結構有問題，AI 也能識別出攻擊路徑。

🧩 **兩項關鍵發現：威脅後量子簽章與對稱加密**

研究人員利用 Claude Mythos Preview 進行測試，取得了兩項具代表性的進展：

1.  **削弱 HAWK 數位簽章方案**：HAWK 是一種專為後量子時代（Post-quantum world）設計的數位簽章演算法。研究發現，Claude 成功找到了一種能顯著削弱該演算法安全性攻擊方式。
2.  **針對 AES 的新攻擊手段**：研究識別出一種針對「輪次減少版 AES」（round-reduced AES）的新攻擊方法。AES 是目前全球最廣泛使用的對稱加密 cipher。

⚠️ **目前尚不影響實際生產系統**

儘管這兩項發現代表了 AI 在密碼學研究領域的重大進步，但 Anthropic 特別強調，這些漏洞目前僅限於研究層面，並不會影響現有的任何生產系統（Production systems）。

🎯 **實務啟示**

隨著 AI 模型能力的提升，密碼學領域正進入一個新時代。開發者與安全專家必須意識到，未來的安全防線不僅要防止程式碼實作錯誤，更要面對 AI 可能從數學底層發起的挑戰。

🔗 **來源**
- 標題：Discovering cryptographic weaknesses with Claude
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/research/discovering-cryptographic-weaknesses

#AI #Cryptography #Anthropic #Claude #CyberSecurity #PostQuantum #AES #HAWK #RedTeaming #MachineLearning
