---
title: 'Gemini 4 Argon: our next era of frontier intelligence'
source: Google DeepMind
url: https://deepmind.google/blog/gemini-4-argon-our-next-era-of-frontier-intelligence/
model: claude-code/sonnet
generated_at: '2026-09-30T21:33:57.242969'
pinned: true
---

📌 【Google DeepMind 官方發布】Gemini 4 Argon 輸出上限衝上百萬 token，先給資安防禦者用

TL;DR：Gemini 4 Argon 輸出 token 上限拉到 1M，長程推理與資安防禦能力領先，先透過 Fairwind Program 限量開放。

當多數模型還在用「輸出上限」保守限制單次推理長度時，Google DeepMind 直接把這個數字從 64K 拉高到 1M token，賭的是模型有更多思考空間才能一次解決真正複雜的問題。

🤔 **先給可信任的資安防禦者用，尚未全面開放**

Gemini 4 Argon 是 Google DeepMind 最新發布的前沿模型，目標是在長程、複雜的專業任務上維持深度推理能力，目前正透過 Fairwind Program 分階段開放給一批可信任的網路防禦者（cyber defenders）試用。Google 表示自己正積極參與美國政府針對前沿模型的自願性預發布存取流程，並會持續蒐集早期測試者的回饋、在正式對外開放給開發者、企業與消費者前逐步強化防護機制。模型的先期定價為輸入每百萬 token 2 美元、輸出每百萬 token 10 美元，快取輸入 token 則有 95% 折扣。

🧩 **把輸出上限拉到百萬級，換來單次軌跡的深度推理**

為了支援更長、更複雜的使用情境，Argon 的輸出 token 上限從前一代的 64K 大幅擴增至業界領先的 1M。素材指出，當模型有餘裕在單一軌跡中生成數十萬 token，就能為困難問題提供更深一層的推理，嘗試一次到位解決。在資安面，Google 針對可信任防禦者與內部團隊，釋出了「不含資安護欄」的版本，讓他們能發揮模型完整的前沿級網路防禦能力，用於自動找出、驗證並修補關鍵軟體漏洞。

📊 **多項基準測試皆居冠**

| 基準測試 | 項目 | Argon 表現 |
|---|---|---|
| DeepSWE v1.1 | 真實世界長程軟體工程任務 | 77.9%，創新高 |
| Vals Index | 涵蓋金融、程式、法律、稅務的經濟影響力綜合指標 | 排名第一 |
| AutomationBench（Zapier） | 跨核心商業職能的端到端執行 | 51.3%，排名第一 |
| LVBench | 長影片理解 | 91.7%，state of the art |
| CWE-bench v1 | 漏洞修復能力 | 68%，並列第一（前代 3.8 Flash Cyber 於 CWE-bench v0 已是前沿水準） |

此外在 Vals Finance Agent v2（多步驟金融研究）與 Harvey 的 Legal Agent Benchmark（法律研究與撰寫）上也維持領先表現。

💡 **Google 自家團隊已經在用它重寫關鍵系統**

素材給出幾個內部案例頗具參考價值：
- 量子演算法最佳化：Argon 協助量子運算研究員最佳化子程序的時空資源（qubits × gates），其中一個案例在數分鐘內就把發表過的 baseline 效能提升了 40%。
- 記憶體最佳化：一組 Argon agent 分析全機隊的效能剖析遙測資料，自動辨識並套用記憶體最佳化，上線後釋出超過 300 TiB 記憶體，估計總節省空間介於 500 TiB 到 1 PiB。
- 大規模程式碼庫遷移：Argon agent 正在協助把 C/C++ 程式碼庫遷移到 Rust，規模從 re2、libgav1 等核心函式庫的數萬行，到 Fuchsia OS Zircon 核心的 80 萬行以上。以 libgav1（Google 開源的影片解碼軟體）為例，Argon agent 在既有 Rust 移植版本的基礎上，透過多輪 profile-guided 實驗改寫了 3.2 萬行 SIMD 程式碼，讓編譯器能自動向量化，最終做出一個記憶體安全、輸出畫面完全一致、且比既有 Rust 版本快 2.7 倍的解碼器。

在資安應用上，資安公司 Wiz 已透過其「Scan for Good」計畫使用 Argon 進行防禦性掃描，並宣稱模型找出了先前前沿模型都漏掉的一個嚴重漏洞，該漏洞暴露了全球醫院使用的醫療軟體中的敏感個資。

⚠️ **大規模系統重寫仍需人工把關，模型也還在分階段釋出**

素材強調，像 Zircon 核心這類關鍵系統的大規模重寫，都必須經過嚴謹的自動化與人工稽核、模擬測試與審查後才會上線，並非模型產出即上線。同時 Google 也坦言，在對外廣泛開放 Argon 之前，仍在持續強化前沿安全防護，特別是防止模型被用於網路攻擊或 CBRN（化學、生物、放射性、核武）濫用的措施。

🎯 **實務啟示**

對正在處理長程 agentic 任務或大型程式碼庫遷移的工程團隊而言，1M token 的輸出上限代表可以把原本要拆成多輪的複雜重構任務，嘗試整合進單一推理軌跡；而資安團隊則可以留意 Fairwind Program 之後的公開時程，評估導入自動化漏洞修補的可行性。

🔗 **來源**
- 標題：Gemini 4 Argon: our next era of frontier intelligence
- 作者／機構：Koray Kavukcuoglu, Google DeepMind
- 連結：https://deepmind.google/blog/gemini-4-argon-our-next-era-of-frontier-intelligence/

#GoogleDeepMind #Gemini #Argon #LLM #SoftwareEngineering #Cybersecurity #FrontierAI #AgenticAI #RustMigration #AIatScale
