---
title: Why Dwarkesh is Wrong about Computer Use + How OpenAI shipped its Jev competitor
  in 1 Week
source: Latent Space
url: https://www.latent.space/p/devday-2026
model: claude-code/sonnet
generated_at: '2026-10-01T22:10:57.879143'
score: 81
---

📌 OpenAI DevDay 幕後：Computer Use 為何「180 度大逆轉」

TL;DR：OpenAI 近期在 DevDay 揭露 Computer Use 與 Decisions API 進展，agent 開發者必讀。

三個月前，以 RL 內容著稱的 Dwarkesh 為自己談 RLVR 的影片下了一個框架性問題，結果惹惱了一票 Computer Use 從業者。Latent Space 團隊曾在 Anthropic 發表 Computer Use 時在場，做過 Claude Cowork 的首個深度訪談，也籌辦過 AI Engineer 大會第一個 Computer Use 專場，並近距離觀察了讓 Codex 如今稱霸 Computer Use 的 OpenAI 併購 Sky Software 一事。基於這段淵源，他們找來 Sky 共同創辦人、現主導 OpenAI Computer Use 全線工作的 Ari Weinstein，以及 OpenAI API 團隊的 Nikunj Handa，在 DevDay 剛結束後錄下這集對談。

🤔 **為什麼 Dwarkesh 的框架讓 Computer Use 圈子不滿**

爭議的核心在於，外界常把 Computer Use 的進展速度低估為「還在早期」，但實際參與其中的人看到的是完全不同的畫面。這也是 Ari Weinstein 在訪談一開頭就強調 Computer Use「和幾個月前相比是 180 度的轉變」的原因。

🧩 **DevDay 一口氣發布了什麼**

根據 Ari Weinstein 的整理，這次 DevDay 的 Computer Use 相關發布包括：
- **Dots**：全新個人助理產品，每個 Dot 都配有自己的雲端 Linux 虛擬電腦，能執行完整桌面應用程式，也能使用瀏覽器，這和過去「僅能在雲端瀏覽器裡操作」或「操作使用者自己電腦」的模式不同。
- **GPT-6.1 Sol**：針對 Computer Use 最佳化的新模型，成本是 Astra 的五分之一，若單看 Computer Use 場景更只要七分之一的成本。
- **Agents API** 正式納入 Computer Use，讓開發者能用上與 Codex、ChatGPT 相同的底層能力。
- **App Shots**：能把使用者正在操作的應用程式上下文，快速帶入 Codex 或 ChatGPT。
- 原生 Mac 上的 Computer Use：可以自動擷取應用程式畫面，同時使用者仍能操作電腦上的其他工作。
- **Decisions API**：這次訪談著墨甚深的新 API。

💡 **Decisions API：目前只是「Luna 的包裝」，但團隊不諱言**

Ari Weinstein 坦言，Decisions API 目前「只是 Luna 的一層包裝」，但團隊認為只要是好的設計模式，複製別人家的做法並不丟人。Decisions API 的特點是支援平行推論（inference in parallel）、不具備 reasoning、模型規模比 Computer Use 所用的模型小，因此速度極快，但也因此較不擅長處理長時程、複雜度高的任務。Ari 直言這兩種能力如何結合仍是「open area of research」。OpenAI 內部已經用 Decisions API 做客服分類與內部工作流程。

Nikunj Handa 則補充了整個開發者技術棧的其他拼圖：async 工具呼叫讓模型在工具執行期間不必中斷推理、mid-turn steering 與 WebSockets 架構讓 agent 回應更即時、UltraFast 推論把延遲再往下壓、更長的 prompt caching 與 cache pre-warming、以及伺服器端 compaction 相對於開發者手動管理長時程 agent 對話串的取捨。

兩人也談到 Computer Use 的能力演進路徑：結合螢幕截圖、accessibility tree、DOM、Playwright 與產生出的程式碼，讓模型在操作軟體時不只是「看畫面」，還能拿到更豐富的語境，進而讓 Computer Use 具備自我除錯與失敗後恢復的能力，部分任務的完成速度已經超過一般人類，團隊的目標是朝「超人類等級」的軟體操作能力前進。

🎯 **實務啟示**

對正在用 Agents API 或 Computer Use 建構產品的工程師而言，這集對談點出了幾個值得關注的方向：Decisions API 適合低延遲、結構化判斷的場景（如分類），但長時程複雜任務仍應交給完整的 Computer Use 推論模型；而 App Shots、原生螢幕操作等能力，意味著把「寫程式」與「測試驗證」的迴圈收斂在同一個 agent 身上正變得可行。

🔗 **來源**
- 標題：Why Dwarkesh is Wrong about Computer Use + How OpenAI shipped its Jev competitor in 1 Week
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/devday-2026

#OpenAI #ComputerUse #AgentsAPI #DecisionsAPI #DevDay #AIAgents #LLM #PromptCaching #DeveloperTools #AIInfrastructure
