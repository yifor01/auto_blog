---
title: 'BottleCap AI Releases ThinkingCap-Qwen3.8-27B: 37.2% Fewer Thinking Tokens
  at a 0.86pp Accuracy Cost'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/24/bottlecap-ai-releases-thinkingcap-qwen3-8-27b-37-2-fewer-thinking-tokens-at-a-0-86pp-accuracy-cost/
model: claude-code/sonnet
generated_at: '2026-09-24T20:42:24.782535'
score: 92
---

📌 ThinkingCap-Qwen3.8-27B：少想 37.2% 的 token，只換 0.86 個百分點準確率

TL;DR：BottleCap AI 微調 Qwen3.8-27B，大砍推理思考長度，多數基準幾乎不掉分，可直接替換部署。

推理模型愛「多想一點」，但多想的那些 token，真的都用在刀口上嗎？BottleCap AI 用一份跨 12 項基準的實測資料回答了這個問題。

🤔 **思考更久不等於答得更好**

BottleCap 的立場很直接：推理模型在回答問題時，經常花費超過問題本身所需的思考 token，而這些多出來的 token 往往不會改變最終答案。ThinkingCap-Qwen3.8-27B 是該系列的第二款模型（第一款曾應用在 Qwen3.6-27B 上），這次的目標刻意設定得保守——不試圖增加知識或改變回答風格，推理能力、指令遵循與安全行為都應維持不變，只針對「縮短思考長度」下手，並把重點放在數學、推理、長文本與 agentic 類基準上。

🧩 **微調方向：只砍冗餘思考，不動能力**

模型是 Qwen3.8-27B 的微調版本，bf16 checkpoint 有 28B 參數，可接受圖片與文字輸入。所有主要數據都使用聊天模板預設的 reasoning_effort=xhigh 設定進行評測。

📊 **12 項基準全面縮短思考長度，平均少想 37.2%**

以下摘錄部分具體基準數據（皆對比 Qwen3.8-27B 基礎模型，xhigh 設定）：

| 基準測試 | Thinking Token 變化 | 準確率變化 |
|---|---|---|
| MMMLU | -65.5%（1,656 → 571 tokens） | 未提供 |
| MMLU-Pro | -57.3% | 未提供 |
| GPQA-Diamond | -43.1%（12,772 → 7,267 tokens） | 未提供 |
| IFBench | -46.4% | 79.75% → 79.71%（幾乎持平） |
| AA-LCR | -38.6% | 81.75% → 84.00%（+2.25pp） |
| LiveCodeBench v6 | -20.3% | +0.07pp |
| τ²-bench | -30.9% | -1.01pp |
| Terminal-Bench 2.1 | -10.7% | -0.56pp（落在 ±4.26 信賴區間內） |
| AIME 2026 | -30.2% | 98.13% → 94.27%（-3.85pp，代價最高） |

整體而言，宏觀平均準確率從 86.65% 降至 85.79%（-0.86pp），12 項基準的平均思考 token 削減幅度為 37.2%，池化平均思考 token 則從 15,735 降到 12,144。在 16K token 的回應上限測試中，ThinkingCap 的得分反而高於基礎模型：截斷比例從 0.51% 降到 0.34%，迴圈（looping）比例從 0.06% 降到 0.05%。

💡 **不同 reasoning effort 下，壓縮效果依然存在**

Qwen3.8-27B 本身支援 reasoning-effort 設定，這項壓縮效果可以與之疊加（以下數據皆相對各自模型在 xhigh 設定下的表現，取 11 項基準平均）：

| Reasoning Effort | 基礎模型 | ThinkingCap |
|---|---|---|
| medium | tokens -52.1%，準確率 -9.16pp | tokens -60.2%，準確率 -9.90pp |
| low | tokens -55.4%，準確率 -9.71pp | tokens -62.3%，準確率 -10.79pp |
| 關閉思考 | — | 落後基礎模型 5.7pp |

此外，MTP 投機解碼（3 個草稿 token）在 AIME 2026 上被測得對準確率中性，接受草稿 token 的比例為 53%，平均每步約 2.6 個 token，與基礎模型相當。測試統一在單張 NVIDIA H200、vLLM 0.29.0 上進行，取樣參數為 temperature 1.0、top_p 0.95、top_k 20、min_p 0.0，多種子平均並附 95% 信賴區間（AIME 2026 用 32 個種子，MMLU-Pro 與 MMMLU 各用 1 個種子；MMMLU 採固定 10,000 題樣本，其餘基準跑完整題集）。

⚠️ **AIME 2026 是代價最高的一項，思考關閉模式仍會退步**

在所有測項中，AIME 2026 的準確率損失最大（-3.85pp），是壓縮效果最不划算的基準；而完全關閉思考模式時，ThinkingCap 會落後基礎模型 5.7pp。BottleCap 團隊建議實務上仍以 xhigh 為準確率與 token 效率的最佳平衡點，並表示針對個別 thinking mode 的最佳化將留待未來版本處理。目前 Hugging Face 上也尚未有推論服務商上架此模型。

🎯 **實務啟示**

模型可直接替換部署於 vLLM 或 SGLang，並提供 FP8、NVFP4、GGUF、MLX 等量化版本，服務端沿用基礎模型的 --reasoning-parser qwen3 與 qwen3_xml 工具呼叫解析器，思考內容會回傳在獨立的 reasoning 欄位。若你的服務對回應延遲或 token 成本敏感（尤其是知識型與多語言任務，減幅最明顯），這類「只砍冗餘、不動能力」的壓縮微調值得評估；但需留意授權條款——repo 為 gated，採用 PolyForm Small Business 1.0.0 授權，商用超出小型企業規模需另簽 BottleCap 協議（上游 Qwen 材料本身仍為 Apache-2.0）。

🔗 **來源**
- 標題：BottleCap AI Releases ThinkingCap-Qwen3.8-27B: 37.2% Fewer Thinking Tokens at a 0.86pp Accuracy Cost
- 作者／機構：Michal Sutter，MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/24/bottlecap-ai-releases-thinkingcap-qwen3-8-27b-37-2-fewer-thinking-tokens-at-a-0-86pp-accuracy-cost/

#LLM #ReasoningModels #Qwen #ModelCompression #Inference #vLLM #SGLang #AIDeployment #EfficientAI #MachineLearning
