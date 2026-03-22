---
title: "AWS 開源 Agentic 文件處理框架：IDP Accelerator 拆解"
date: "2026-03-02"
paper_url: "https://arxiv.org/abs/2602.23481"
paper_title: "IDP Accelerator: Agentic Document Intelligence from Extraction to Compliance Validation"
tags: [Agent, Document AI, MCP]
tldr: "AWS 開源 Agentic 文件智能框架"
---

你有沒有處理過一整疊混雜的文件？保險理賠單夾著醫療報告、合約裡插著附件表格，光是把它們分開歸類就夠頭痛了，更別說還要從裡面挖出結構化資料、再跑一輪法規合規檢查。AWS 最近開源了一個叫 **IDP Accelerator** 的框架，目標就是把這整條流程用 Agentic AI 串起來，從文件分類到合規驗證一條龍搞定。

## 🔍 為什麼現有的文件處理 Pipeline 不夠用

企業裡的文件處理有個很現實的痛點：文件不是一張一張來的，是一疊一疊來的。一個理賠案件可能包含申請表、診斷書、收據、授權書，全部掃成一個 PDF。傳統的 IDP 系統通常假設輸入是單一文件類型，碰到這種「**document packet**」就直接投降。

就算你用 LLM 做 zero-shot extraction，還是會碰到兩個硬傷：第一，多文件之間的**交叉推理**（比如核對申請表上的日期跟收據是否吻合）；第二，合規檢查的邏輯太複雜，寫死規則引擎維護成本超高，但純靠 LLM 又怕它幻覺。

## 🛠️ 四個核心模組怎麼運作

IDP Accelerator 拆成四塊，每塊解決一個具體問題：

- **DocSplit**：負責把混雜的文件包拆開。做法蠻有意思的，他們用 BIO tagging 的方式來標記頁面邊界，搭配多模態分類器判斷每一頁屬於哪種文件類型。這不是用啟發式規則切的，而是真的在學頁面之間的語義邊界。他們還為此建了一個 benchmark dataset，這點我覺得對社群蠻有價值的，因為「文件包分割」這個任務一直缺公開資料集。
- **Extraction Module**：用多模態 LLM 把非結構化內容轉成結構化資料。這塊比較標準，但他們強調「可配置」，意思是你可以用 config 定義想抽取的欄位，不用改程式碼。
- **Agentic Analytics Module**：這是我覺得最值得關注的部分。它遵循 **Model Context Protocol（MCP）**，透過 sandboxed code execution 讓 Agent 可以安全地查詢和分析抽取出來的資料。用 MCP 這件事很有意義，代表它可以跟其他 MCP-compatible 的工具鏈串接，不是封閉生態系。
- **Rule Validation Module**：用 LLM 取代傳統的確定性規則引擎來做合規檢查。坦白說，這塊我有點疑慮。合規檢查是 high-stakes 場景，LLM 的不確定性在這裡是雙面刃。不過他們的思路是：與其維護一堆 if-else 規則（每次法規改動就要重寫），不如讓 LLM 直接理解法規文本來判斷。這在維護成本上確實有吸引力。

## 💡 實際部署的數字與我的看法

他們在一家大型醫療機構做了 production deployment，報出來的數字蠻漂亮的：

- 文件分類準確率 **98%**
- 處理延遲降低 **80%**
- 營運成本降低 **77%**

這些數字看起來很亮眼，但要注意幾件事。第一，**98%** 的分類準確率是在他們自己建的 benchmark 上測的，不同產業、不同文件複雜度可能差很多。第二，成本降低 **77%** 的 baseline 是「legacy baselines」，也就是跟舊系統比，不是跟其他現代方案比。

我覺得這個框架最大的價值不在於單一模組有多強，而在於它把 Document AI 的完整流程用 **Agent 架構**串起來了。以前你要自己串 OCR、分類、抽取、驗證，每個環節都是獨立工具，中間的資料流轉和錯誤處理都要自己搞。IDP Accelerator 提供了一個統一的框架來處理這件事。

不過，**LLM-driven 合規檢查**在受監管產業能被接受到什麼程度，我覺得還是個開放問題。醫療、金融、保險這些領域的合規部門通常需要可解釋、可稽核的判斷依據，「LLM 說 OK」可能不夠。如果你在這類場景評估這個框架，Rule Validation Module 那塊建議做嚴格的 human-in-the-loop 驗證。

另一個值得觀察的是 **MCP** 的採用。如果越來越多的 Document AI 工具開始支援 MCP，那 Agentic 文件處理的互操作性會大幅提升，這對整個生態系都是好事。

框架已經開源，想玩的人可以直接去試。

[論文連結](https://arxiv.org/abs/2602.23481)

<!-- fb -->

你有沒有處理過一整疊混雜的文件？保險理賠單夾著醫療報告、合約裡插著附件表格，光是把它們分開歸類就夠頭痛了，更別說還要從裡面挖出結構化資料、再跑一輪法規合規檢查。AWS 最近開源了一個叫 IDP Accelerator 的框架，目標就是把這整條流程用 Agentic AI 串起來，從文件分類到合規驗證一條龍搞定。

🔍 為什麼現有的文件處理 Pipeline 不夠用

企業裡的文件處理有個很現實的痛點：文件不是一張一張來的，是一疊一疊來的。一個理賠案件可能包含申請表、診斷書、收據、授權書，全部掃成一個 PDF。傳統的 IDP 系統通常假設輸入是單一文件類型，碰到這種「document packet」就直接投降。

就算你用 LLM 做 zero-shot extraction，還是會碰到兩個硬傷：第一，多文件之間的交叉推理（比如核對申請表上的日期跟收據是否吻合）；第二，合規檢查的邏輯太複雜，寫死規則引擎維護成本超高，但純靠 LLM 又怕它幻覺。

🛠️ 四個核心模組怎麼運作

IDP Accelerator 拆成四塊，每塊解決一個具體問題：

第一塊是「DocSplit」，負責把混雜的文件包拆開。做法蠻有意思的，他們用 BIO tagging 的方式來標記頁面邊界，搭配多模態分類器判斷每一頁屬於哪種文件類型。這不是用啟發式規則切的，而是真的在學頁面之間的語義邊界。他們還為此建了一個 benchmark dataset，這點我覺得對社群蠻有價值的，因為「文件包分割」這個任務一直缺公開資料集。

第二塊是 Extraction Module，用多模態 LLM 把非結構化內容轉成結構化資料。這塊比較標準，但他們強調「可配置」，意思是你可以用 config 定義想抽取的欄位，不用改程式碼。

第三塊是 Agentic Analytics Module，這是我覺得最值得關注的部分。它遵循 Model Context Protocol（MCP），透過 sandboxed code execution 讓 Agent 可以安全地查詢和分析抽取出來的資料。用 MCP 這件事很有意義，代表它可以跟其他 MCP-compatible 的工具鏈串接，不是封閉生態系。

第四塊是 Rule Validation Module，用 LLM 取代傳統的確定性規則引擎來做合規檢查。坦白說，這塊我有點疑慮。合規檢查是 high-stakes 場景，LLM 的不確定性在這裡是雙面刃。不過他們的思路是：與其維護一堆 if-else 規則（每次法規改動就要重寫），不如讓 LLM 直接理解法規文本來判斷。這在維護成本上確實有吸引力。

💡 實際部署的數字與我的看法

他們在一家大型醫療機構做了 production deployment，報出來的數字蠻漂亮的：

文件分類準確率 98%
處理延遲降低 80%
營運成本降低 77%

這些數字看起來很亮眼，但要注意幾件事。第一，98% 的分類準確率是在他們自己建的 benchmark 上測的，不同產業、不同文件複雜度可能差很多。第二，成本降低 77% 的 baseline 是「legacy baselines」，也就是跟舊系統比，不是跟其他現代方案比。

我覺得這個框架最大的價值不在於單一模組有多強，而在於它把 Document AI 的完整流程用 Agent 架構串起來了。以前你要自己串 OCR、分類、抽取、驗證，每個環節都是獨立工具，中間的資料流轉和錯誤處理都要自己搞。IDP Accelerator 提供了一個統一的框架來處理這件事。

不過，LLM-driven 合規檢查在受監管產業能被接受到什麼程度，我覺得還是個開放問題。醫療、金融、保險這些領域的合規部門通常需要可解釋、可稽核的判斷依據，「LLM 說 OK」可能不夠。如果你在這類場景評估這個框架，Rule Validation Module 那塊建議做嚴格的 human-in-the-loop 驗證。

另一個值得觀察的是 MCP 的採用。如果越來越多的 Document AI 工具開始支援 MCP，那 Agentic 文件處理的互操作性會大幅提升，這對整個生態系都是好事。

框架已經開源，想玩的人可以直接去試。

論文連結：https://arxiv.org/abs/2602.23481

#GenAI #Agent #DocumentAI #MCP #AWS #LLM
