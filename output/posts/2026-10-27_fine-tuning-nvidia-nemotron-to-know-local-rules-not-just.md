---
title: Fine-Tuning NVIDIA Nemotron to Know Local Rules, Not Just Local Languages
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/fine-tuning-nvidia-nemotron-to-know-local-rules-not-just-local-languages/
model: claude-code/sonnet
generated_at: '2026-10-27T21:36:49.825961'
score: 86
---

📌 當地護照規定 AI 答不出來？NVIDIA 用「在地人設」微調 Nemotron

TL;DR：NVIDIA 攜手 Pleias 與 KU Leuven 推出 Nemotron-Personas 資料集，讓開源模型學會當地法規細節，而不只是當地語言。

同一句法語問題，通用模型給出的答案聽起來很流利，卻可能完全不符合實際行政程序——這正是語言能力與在地知識之間的落差，也是 NVIDIA 這篇教學要解決的問題。

🤔 **流利的法語，錯誤的行政流程**

NVIDIA 舉了一個具體案例：有人問法國護照申請窗口，「我因為健康因素無法出門，該怎麼申請護照？」未經後訓練的基礎模型回答：可以用郵寄方式申請，把完整文件以掛號信寄到財政總局。但實際規定是，這種情況必須由政府人員到府辦理，郵寄申請並不適用。這類答案不只不精確,還直接牴觸官方文件。

🧩 **用「接地氣」的虛構居民生成訓練資料**

NVIDIA 的解法是 Nemotron-Personas 資料集，目前已涵蓋 12 個國家，France 和 Belgium 版本分別與法國新創 Pleias、Pleias 加比利時魯汶大學（KU Leuven）合作打造。每個 persona 是一個根據區域人口統計、地理、語言與文化分布生成的合成居民：不是「一個需要護照的法國成年人」這種空泛描述，而是帶有年齡、所在市鎮、職業、家庭狀況，並符合法國人口普查分布的具體角色，外加其工作與日常生活的書面描述。這會改變提問的方式,甚至改變正確答案本身——例如法屬圭亞那（French Guiana）居民申請護照的印花稅是 43 歐元，而法國本土則是 86 歐元。

這些 persona 會與官方程序文件配對，用來生成微調用的合成對話，藉此擴大涵蓋範圍。微調後,同一個問題的回答變成：如果健康狀況無法出門，可以申請官員到府服務,需要提供三個月內的醫療證明,可以透過 ANTS 網站線上申辦或到有登記站的市政廳辦理，並記得攜帶身分證件、照片、住址證明和繳納印花稅。NVIDIA 指出，這個版本更精簡、語氣更貼近客服人員，而且聚焦在解決問題所需的具體資訊，這才像是真正的客服回覆。

同樣的流程換成 Belgium 版本（涵蓋荷語、法語、德語、英語）也適用，只需要替換 persona 資料集、更新行為規範與審查者，其餘工作流程不變。

🧩 **怎麼跑這個工作流程**

NVIDIA 把流程整理成四個階段：定義目標行為、生成訓練資料、微調、部署與評估，並透過 NeMo 開源訓練堆疊提供可重用的步驟模組。環境需求包括 Python 3.11 至 3.13、uv、Git、Docker、NVIDIA Container Toolkit，以及一臺 NVIDIA DGX Station GB300 或 DGX Spark（教學也指出可適配其他 NVIDIA GPU 系統）。安裝方式為：

```
git clone https://github.com/NVIDIA-NeMo/Nemotron.git
cd Nemotron
git checkout v0.2.0
uv sync --extra data-sdg --extra evaluator
uv run nemotron steps --help
```

教學以 `french-public-service-assistant` 這個範例資料夾走完全流程，第一步是定義目標行為並凍結一組 holdout 資料，包含受眾（不同技術水平的法國成年人）、任務（回答身分證件與車輛登記相關程序問題）、語言語氣（法語、冷靜且有禮貌）、以及允許引用的事實依據來源,這些需求同時指導資料生成與後續審查。

💡 **實際應用：脊椎照護助理 Lamina**

Pleias 在旗下合作夥伴的脊椎照護助理 Lamina 專案中，使用了包含 France 與 Belgium 在內的三個 Nemotron-Personas 資料集，把少量真實病患案例擴展成多樣化的訓練對話，也用來在不同病患輪廓下測試助理表現。Pleias 的說法是：「更有根據的資料，才是讓小型高效的區域專用模型可行的關鍵。」

⚠️ **persona 接地氣不等於公平**

NVIDIA 特別提醒，persona grounding 的目的是提升訓練資料的覆蓋率、減少盲點，而不是保證公平性或適當的代表性，這點在實際部署前需要額外評估。

🎯 **實務啟示**

如果你的應用需要模型遵守特定地區的行政術語、正式程度或流程規則，單靠通用模型的語言能力並不夠；用結構化的在地人設生成合成資料，再搭配官方程序文件做事實依據，可以系統性地補足模型在特定市場的知識缺口，而且整套流程是可重複、可替換到其他國家/語言市場的模組化工作流程。

🔗 **來源**
- 標題：Fine-Tuning NVIDIA Nemotron to Know Local Rules, Not Just Local Languages
- 作者／機構：Shara Tibken（NVIDIA Developer）
- 連結：https://developer.nvidia.com/blog/fine-tuning-nvidia-nemotron-to-know-local-rules-not-just-local-languages/

#NVIDIA #Nemotron #FineTuning #LLMLocalization #SyntheticData #NeMo #OpenModels #AIAgents #Pleias #PostTraining
