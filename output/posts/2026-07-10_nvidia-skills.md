---
title: NVIDIA/skills
source: GitHub Trending
url: https://github.com/NVIDIA/skills
score: 99
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T08:05:40.689842'
---

📌 **NVIDIA 發布官方 AI Agent Skills 目錄，提供即用的 CUDA‑X 與 AI Blueprint 教學**

TL;DR：透過 npx skills CLI，開發者可直接為 AI 代理安裝 NVIDIA 認證的技能，讓代理在遇到相關任務時自動獲得使用 NVIDIA 軟體的指引。

🎣 **為何 AI 代理需要「技能」？**  
當代理被要求執行如「使用 cuOpt 解線性規劃問題」時，若缺乏對應的使用說明，它只能靠通用推理，往往會失敗或產生次佳結果。NVIDIA 因此提供一套標準化的「Skill」，讓代理在載入技能後，能直接依照預先編寫的指令走訪對應的 API。

🧩 **技能的結構與維護方式**  
- 每個 Skill 是一套可攜帶的指令集，專門教導 AI 代理如何最佳使用 NVIDIA 軟體，涵蓋 CUDA‑X 函式庫、AI Blueprints 與平臺工具。  
- 官方說明指出，這些 Skill 實際上維護於各自產品的原始專案中，而本倉庫（NVIDIA/skills）僅透過每日自動同步管線，將最新版本映象過來，形成一個可瀏覽的目錄。  
- 由於 Skill 會持續新增，使用者被鼓勵定期檢查更新；同時，專案歡迎社群貢獻，未來規劃可參考 Roadmap。

🚀 **如何安裝與使用 Skill**  
1. **預設流程（會提示選擇）**  
   ```bash
   npx skills add nvidia/skills
   ```  
   CLI 會透過 npx 執行，接著提示你選擇想安裝的 Skill 以及安裝目的地。無需手動克隆此倉庫或複製資料夾。  
2. **直接安裝特定 Skill（跳過提示）**  
   若已知 Skill 名稱，可使用：  
   ```bash
   npx skills add nvidia/skills --skill <skill-name> --yes
   ```  
   例如，安裝 cuOpt 數值最佳化 API 的 Skill：  
   ```bash
   npx skills add nvidia/skills --skill cuopt-numerical-optimization-api --yes
   ```  
   `<skill-name>` 必須來自於 Skill 目錄中的名稱。  
3. **指定目標代理**  
   透過 `--agent` 參數可以將 Skill 安裝到特定的代理環境中（具體用法請參考專案說明）。  
4. **使用時機**  
   安裝完成後，該 Skill 會在代理下次載入技能並遇到相關任務時自動生效。例如，對代理說「solve a linear programming problem with cuOpt」，它會依照該 Skill 的指引呼叫 cuOpt Python API。

🎯 **實務啟示**  
- 對於需要快速讓 AI 代理具備 NVIDIA 軟體操作能力的團隊，這套 Skill 目錄提供了「即插即用」的方式，減少撰寫樣板程式與查閱檔案的時間。  
- 由於 Skill 與原始產品專案同步，更新時能即時取得最新用法，有助於保持代理與 NVIDIA 平臺的相容性。  
- 然而，這些 Skill 目前僅涵蓋 NVIDIA 自家的軟體與工具，若代理需要跨廠商或開源庫的操作，則仍需自行撰寫或尋找其他來源的指導資料。

⚠️ **限制與注意事項**  
- 本專案只映象 NVIDIA 生態系內的 Skill，非 NVIDIA 軟體的使用案例不會在此處出現。  
- Skill 的品質與完整度取決於各產品專案的維護情況，儘管有自動同步機制，但若來源專案更新頻率低，對應的 Skill 也可能滯後。  
- 目前檔案僅提到基於 npx 的 CLI 安裝方式，其他語言或框架的整合方式未在摘要中說明，使用者需自行參考官方檔案或專案的後續更新。

🔗 **來源**  
- 標題：NVIDIA/skills  
- 連結：https://github.com/NVIDIA/skills  

#NVIDIA #AIAgent #SkillsCatalog #CUDA-X #AIBlueprints #CLI #OpenSource #DeveloperTools #AgenticAI #SkillSharing
