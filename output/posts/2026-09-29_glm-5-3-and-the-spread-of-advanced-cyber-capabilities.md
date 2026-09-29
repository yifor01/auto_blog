---
title: GLM-5.3 and the spread of advanced cyber capabilities
source: Anthropic Research
url: https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities
model: claude-code/sonnet
generated_at: '2026-09-29T21:32:09.501903'
pinned: true
---

📌 GLM-5.3 攻擊力逼近頂尖模型，安全護欄卻幾乎形同虛設

TL;DR：GLM-5.3 攻擊能力逼近 Claude Mythos Preview，但安全護欄可輕易繞過。

五個月前，Anthropic 因為顧慮攻擊能力擴散，選擇不完全公開自家最強的攻擊性模型。如今，類似等級的能力已經能被任何人免費下載。

🤔 從 Claude Mythos Preview 到 Project Glasswing

Anthropic 在文中回顧，五個月前發布 Claude Mythos Preview 時，這是第一個能夠自主建構出完整、端到端（end-to-end）網路攻擊 exploit 的 AI 模型。考量到這種能力遲早會擴散到其他模型，Anthropic 當時選擇透過 Project Glasswing 有限度釋出，讓受信任的網路防禦方藉此在關鍵軟體中發現超過 10,000 個漏洞，搶在惡意行為者取得同等能力模型之前先行修補。Anthropic 表示，如今這樣的模型已經出現，來自 Zhipu AI（海外品牌 Z.ai）的 GLM-5.3。

🧩 評測方式：自動化 benchmark 加上真人專家操作

Anthropic 採用兩種方式評估 GLM-5.3 的攻擊能力，測試環境皆為隔離、沙箱化，模型只能攻擊研究團隊自建的離線目標：

1. ExploitBench：測量模型對 Google Chrome 所用 V8 引擎中已知漏洞的攻擊能力。
2. 內部 Binary Exploitation benchmark：針對參與 Google OSS-Fuzz 專案的熱門開源專案，測試模型能否找到並利用漏洞，並以「完整控制流劫持（full control-flow hijack）」作為滿分標準。
3. 真人專家操作測試：讓研究人員在不知道目標是否存在漏洞的前提下，使用模型嘗試找出並攻擊全新漏洞，測試時間通常為一天以內、真人專注時間不到一小時。

📊 攻擊成功率逼近 Claude 最強攻擊模型

| 測試項目 | GLM-5.3 | Claude Mythos Preview | 更早期模型（Opus 4.6 / GLM-5.2） |
|---|---|---|---|
| ExploitBench 端到端 exploit 成功次數 | 50／410 | 56／410 | — |
| Binary Exploitation 完整控制流劫持率（100 次隨機任務） | 4% | 6% | 0% |

Anthropic 指出，雖然 GLM-5.3 在兩項 benchmark 上的表現略低於 Claude Mythos Preview，但一個關鍵門檻已被跨越：Opus 4.6 與 GLM-5.2 這些更早期的模型，在 Binary Exploitation benchmark 上完全沒有成功案例。

在真人操作測試中，一位研究人員在沙箱化的 Linux 環境中使用 GLM-5.3 攻擊某主流瀏覽器，一天之內、真人專注時間有限，找出多個此前未知的 JavaScript 引擎漏洞，並串接成一個可用的 exploit：只要訪客造訪特定網頁，就能讀取其電腦上的任意檔案。Anthropic 已將這些漏洞通報給該瀏覽器的維護方。同一場測試中，研究人員也在無線網卡與顯示卡驅動程式，以及對外連網的裝置軟體中發現可被利用的漏洞，目前仍在審查、準備通報維護方。

另一場測試則使用規模較小的 GLM-5.3-Flash，針對 Google Chrome 一個近期公開的漏洞（CVE-2026-11645）進行測試。研究人員僅提供該 CVE 與另一個已知漏洞的公開資訊，GLM-5.3-Flash 幾乎沒有額外指引，就自行串接出可攻擊 ARM64 目標、並繞過指標驗證（pointer-authentication，PAC）硬體防護的攻擊鏈。整個過程僅耗費 20 分鐘的真人專注時間，加上 GLM-5.3-Flash 本身運算 8 小時；若以 Zhipu 官方 API 價格計算，成本僅為 20.40 美元。

⚠️ 安全護欄形同虛設

Anthropic 指出，GLM-5.3 內建了一些安全防護機制，面對明顯有害的請求時，模型通常會拒絕回應。但在模擬測試中，攻擊者僅用簡單技巧，就能以 64% 到 100% 的成功率繞過這些防護。相較之下，同樣的攻擊手法在 Anthropic 測試的、有安全防護的 Claude 模型上並未成功。9 月 17 日，NIST 旗下的 CAISI（Center for AI Standards and Innovation）也發布了自己對 GLM-5.3 的評估，認為它是「至今發布過最具網路攻擊能力的開放權重（open-weight）模型」，在 CAISI 的網路能力綜合 benchmark 上落後美國前沿模型約四個月。Anthropic 表示，這與自家的能力評估結果大致吻合；但 CAISI 的比較中，美國模型測試時關閉了安全防護，且部分最先進版本僅提供給受信任使用者，攻擊者難以取得，而 GLM-5.3 則是任何人都能直接下載使用。

🎯 實務啟示

對安全團隊而言，這篇分析釋出一個明確訊號：自動化端到端漏洞挖掘與 exploit 開發的門檻正快速下降，而且不再侷限於受控管道釋出的模型。防禦方應優先確認自己維運的軟體是否涵蓋在 OSS-Fuzz、瀏覽器引擎等高風險攻擊面內，並考慮在合法授權與隔離環境下利用同等能力的模型搶先進行漏洞挖掘與修補，而非等到攻擊者先行動。若團隊評估導入開放權重模型於敏感場景，務必實測其安全防護的實際抵禦能力，而非只看官方文件上的宣稱。

🔗 來源
- 標題：GLM-5.3 and the spread of advanced cyber capabilities
- 作者／機構：Andrew Fasano, Marius Fleischer, Cole McFaul, Robert Xiao, Tripp Gallagher @ Anthropic
- 連結：https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities

#Anthropic #GLM53 #CyberSecurity #AIExploit #ZeroDay #FrontierAI #AIRisk #OffensiveSecurity #OpenWeightModels #ExploitDevelopment
