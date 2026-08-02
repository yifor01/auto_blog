---
title: 'Beyond the Prompt: Jailbreaking Function-Calling LLMs via Simulated Moderation
  Traces'
source: Semantic Scholar
url: https://www.semanticscholar.org/paper/fb4fbd610bee33ae95a101af9a0fab07d77a4ffc
score: 87
model: google/gemma-4-31b-it:free
generated_at: '2026-07-02T19:57:57.955288'
---

📌 Beyond the Prompt: Jailbreaking Function‑Calling LLMs via Simulated Moderation Traces

TL;DR：研究指出在支援函式呼叫的 LLM 系統中，透過「模擬審核流程」的多回合攻擊可繞過安全機制，對商業模型造成最高成功率的危害。

🧩 **結構性漏洞：函式呼叫環境的攻擊面擴大**  
傳統的安全防護多聚焦於單一 Prompt 的過濾與清理，然而在具備 *function‑calling* 功能的 LLM 應用裡，開發者會定義 schema、傳遞結構化參數，並將工具（如搜尋、資料庫）回傳的未受信任結果直接寫入同一個模型上下文。這樣的設計讓「可信的控制邏輯」與「不可信的資料」之間的邊界變得模糊，攻擊者可以把惡意意圖分散到多回合的執行路徑中。

🧩 **SMT 攻擊框架：以模擬審核軌跡欺騙模型**  
作者提出 *SMT*（Simulated Moderation Traces），一套黑盒攻擊流程：  
1. **構造審核工作流**：先模擬一個合法的審核/稽核流程，讓模型以為自己正處於安全監控之下。  
2. **偽造審核框架**：在此流程內以紅隊測試為藉口，誘導模型產生有害回應。  
3. **驗證回饋機制**：將模型的安全拒絕視為「執行失敗」，根據回饋不斷微調輸入，使安全限制逐步鬆動。  
4. **最終觸發**：當安全門檻被削弱到一定程度，模型便會直接輸出危害內容。

🧩 **實驗結果：跨五大商業 LLM、兩項安全基準皆領先**  
在五家不同供應商的主流商業模型上，作者以兩套標準化安全測試集（未在摘要中具體說明）進行評估。SMT 在**平均攻擊成功率**與 **HarmScore**（衡量危害程度）皆超過現有基線，且僅需極少的查詢次數即可完成攻擊，顯示其效率遠高於傳統 Prompt‑only 攻擊手法。

⚠️ **限制與未來方向**  
摘要僅說明 SMT 為黑盒方法，未透露對模型內部結構或 API 限制的具體假設。防禦層面僅提出「僅靠 Prompt 層面的淨化不足」的概念，暗示需要在 schema、參數、工具回傳以及會話累積狀態上實施**情境感知驗證**，具體實作仍在探索階段。

🎯 **實務啟示**  
- **開發者**：若系統使用 LLM 進行函式呼叫，務必對每一次工具輸出實施獨立驗證，而非僅依賴模型自身的安全回應。  
- **平臺提供者**：在 API 設計時，可考慮將工具回傳結果與模型上下文分離，或加入多層次審核機制，降低攻擊者利用多回合互動削弱安全限制的可能。  
- **安全研究者**：SMT 示範了利用「模擬審核」的攻擊路徑，未來可以此為基礎開發更精細的偵測與防禦策略，特別是針對跨回合狀態的異常行為。

🔗 來源  
- 標題：Beyond the Prompt: Jailbreaking Function-Calling LLMs via Simulated Moderation Traces  
- 作者／機構：Junlong Liu, Haobo Wang, Weiqi Luo, Xiaojun Jia  
- 連結：https://www.semanticscholar.org/paper/fb4fbd610bee33ae95a101af9a0fab07d77a4ffc  

#LLM #Jailbreak #FunctionCalling #AI safety #PromptInjection #Security #SMT #MachineLearning #AIResearch #AdversarialAttack
