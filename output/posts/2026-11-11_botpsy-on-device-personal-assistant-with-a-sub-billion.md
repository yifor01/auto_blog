---
title: 'BotPsy: On-Device Personal Assistant with a Sub-Billion-Parameter Agentic
  Language Model'
source: HuggingFace Blog
url: https://huggingface.co/blog/qvac/botpsy
model: claude-code/sonnet
generated_at: '2026-11-11T23:53:54.573985'
score: 94
---

📌 0.8B 參數小模型，代理能力打贏 2.5 倍大的對手

TL;DR：Tether AI Research 推出開源 0.8B 代理模型 BotPsy，六項工具呼叫基準大幅領先同級甚至更大的模型，且可完全在裝置端運行。

雲端的前沿大型語言模型固然強大，但成本會不定期波動，供應商隨時可能更動、限制或棄用存取權限，加上客製化空間有限、隱私與資料控制風險始終存在。更重要的是，並非每個任務都需要前沿級智慧，小型專用 agent 在特定任務上同樣能打，而且跑在裝置端的成本遠低於呼叫雲端模型。

🤔 **為什麼要把 agent 塞進手機，而不是丟給雲端？**

Tether AI Research 認為，隨著每個參數所能承載的智慧持續快速提升，自架、隱私優先的小模型正站在趨勢前緣。他們推出的 BotPsy 正是這個方向的具體成果：一個只有 0.8B 參數、專為 function calling 與 agentic workflow 設計的模型。

🧩 **站在 Qwen3.5-0.8B 肩膀上的個人助理**

BotPsy 以 Qwen3.5-0.8B 為基礎模型打造，定位是「個人助理」，透過工具呼叫為使用者完成各種簡單任務，涵蓋網路搜尋與研究、旅遊與生活、商務與金融、企業與客服營運、裝置與車輛控制、檔案與文件、日曆，以及電子郵件與訊息等領域。由於參數量小，BotPsy 最適合處理中低難度的任務，官方也明確說明它不適用於高風險場景。

📊 **六項基準全面開花，只在一項輸給 2.5 倍大的對手**

| 基準測試 | BotPsy | 基礎模型 Qwen3.5-0.8B-Think | Qwen3.5-2B-Think（2.5倍參數） |
|---|---|---|---|
| BFCL v4 | 44.0 | 23.4 | 37.7 |
| ACEBench | 58.7 | 30.1 | 55.4 |
| τ-bench（零售/電信/銀行平均） | 51.5 | 23.2 | 46.5 |
| ToolSandbox | 64.6 | — | 41.2 |
| Claw-Eval | 46.5 | — | 48.9（唯一輸給 2B 模型） |
| BrowseComp-Plus | 4.5 | — | 2.8 |

在多輪任務上，BotPsy 的優勢更明顯：τ²-bench 電信場景拿下 82.5 分，領先 Qwen3.5-2B-Think 的 69.3；BFCL v4 的多輪任務分數從基礎模型的 7.5 大幅提升到 46.1，接近 Qwen3.5-2B-Think（23.8）的兩倍。依應用領域拆解，BotPsy 在商務服務類多步驟任務（58.3，次佳為 47.4）與裝置系統管理（46.1 比 31.9）皆領先所有受測模型。

💡 **懂得何時不出手，也更懂得安全**

一個會行動的 agent，也要知道什麼時候不該行動。在 BFCL v4 的 hallucination 測試（檢測模型是否在無合適工具時正確拒絕）中，BotPsy 拿下所有受測模型中最高的 86.1 分；ACEBench 的特殊案例（請求不完整、參數錯誤或工具無法滿足需求）分數也從基礎模型的 13.7 跳升到 51.3。

指令遵循方面，IFEval 從 59.7 提升到 90.8，IFBench 從 22.0 提升到 55.9，同樣是所有受測模型中最高。一般知識也沒有犧牲：GPQA Diamond 從 33.2 升到 38.1，MMLU-Pro 從 41.6 升到 48.9，在這四項基準上都超越所有 1.2B 參數以下的受測模型。

安全性上，自動化紅隊測試（六大傷害類別）顯示 BotPsy 產生不安全回應的比例為 21%，優於基礎模型的 36%，也是所有 1.2B 參數以下模型中最低（LFM2.5-1.2B-Think 為 35%，MiniCPM5-1B-Think 為 47%）。面對 prompt injection 攻擊時，不安全回應率也從基礎模型的 46% 降到 31%。

效率方面同樣有感：在五個模型都答對的題目上，BotPsy 在 GPQA Diamond 用約 1/3 的推理 token 數就得出答案（3,690 比基礎模型的 11,563），MMLU-Pro 則省下約 2.7 倍（1,912 比 5,105）。陷入重複推理迴圈的比例從 22.9% 降到 1.4%，撞到 32k token 上限的比例從 28.3% 降到 0.2%，這些都意味著端側延遲會更低。

⚠️ **終究還是個小模型**

官方坦言 BotPsy 仍會犯錯，不建議用於高風險場景；整體知識量仍主要取決於參數規模，指令累積過多時表現會下降，在低資源語言上也相對落後。六項基準中唯有 Claw-Eval 輸給 2.5 倍大的 Qwen3.5-2B-Think。

🎯 **實務啟示**

對想在裝置端部署 agent 的工程師來說，BotPsy 提供了一個可直接落地的選項：Apache 2.0 開源授權，提供 bf16、Q8、Q4 三種精度的 safetensors 與 GGUF 檔案，可直接用於 QVAC SDK 或 llama.cpp。若應用場景是中低難度的日常工具呼叫任務，且重視隱私與成本，BotPsy 值得納入評估清單。

🔗 **來源**
- 標題：BotPsy: On-Device Personal Assistant with a Sub-Billion-Parameter Agentic Language Model
- 作者／機構：Tether AI Research（QVAC）
- 連結：https://huggingface.co/blog/qvac/botpsy

#OnDeviceAI #AgenticAI #FunctionCalling #SmallLanguageModel #LLM #OpenSource #Qwen #EdgeAI #Privacy #ToolUse
