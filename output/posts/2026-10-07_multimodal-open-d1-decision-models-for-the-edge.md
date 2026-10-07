---
title: Multimodal open d1 decision models for the edge
source: HuggingFace Blog
url: https://huggingface.co/blog/LiquidAI/open-d1
model: claude-code/sonnet
generated_at: '2026-10-07T22:17:45.938682'
score: 103
---

📌 Liquid AI 開源 d1 決策模型，邊緣裝置 16 毫秒出答案

TL;DR：Liquid AI 推出 d1-3B 與實驗性 d1-omni-600M，單次前向就能完成多模態決策，同量級分數與速度雙雙領先。

多數 LLM 要「生成」答案，一個 token 接一個 token 吐出來。但如果你要的只是「是或不是」「選哪個選項」「打幾分」，何必跑完整套生成流程？Liquid AI 這次釋出的 d1 系列，把決策壓縮成一次前向運算（forward pass），而不是一串 token。

🤔 決策模型跟生成模型，根本不是一回事

d1 決策模型家族建立在 Liquid AI 自家的 Liquid Foundation Models（LFM）之上。與一般生成式模型不同，它們不產生文字輸出，而是針對設定好的「問題」直接在一次前向運算中給出結構化答案，天然適合分類、路由、評分這類場景。

🧩 兩種骨幹，兩種模態組合

d1-3B 與 d1-omni-600M 分別從截然不同的骨幹模型訓練而來：

- d1-3B 以最新的 VLM、decoder-only 架構的 LFM2.5-VL-3B 為基礎，接受文字與影像輸入。
- d1-omni-600M 以雙向編碼器 LFM2.5-Encoder-350M 為基礎，額外加上視覺與音訊編碼器，可接受「文字＋影像」或「文字＋音訊」兩種組合。此模型目前仍是早期研究版本，持續開發中。

📊 同量級最高分，速度也不輸

在涵蓋閱讀理解、毒性偵測、意圖分類、醫療問答與跨語言理解的七個公開資料集上：

| Benchmark | d1-omni-600M | d1-3B | Decider 2B | Decider 4B |
|---|---|---|---|---|
| SQuAD 2.0 | 74.0 | 83.3 | 67.7 | 76.0 |
| Civil Comments | 95.8 | 93.3 | 93.6 | 92.8 |
| MASSIVE intent | 86.1 | 86.9 | 81.1 | 88.3 |
| PubMedQA | 61.3 | 68.3 | 65.7 | 63.3 |
| BoolQ | 77.7 | 86.3 | 87.3 | 89.0 |
| XNLI | 74.7 | 85.6 | 85.0 | 88.6 |
| PAWS-X | 79.5 | 76.4 | 59.5 | 69.8 |
| **平均** | **78.4** | **82.9** | **77.1** | **81.1** |

d1-3B 平均 82.9 分，是表中最高分，超越 Decider 4B；d1-omni-600M 以四分之一的參數量拿下 78.4 分，超越 Decider 2B。在官方 Decision Index 0.2.1 上，d1-3B 拿下 48.57 分，是 10B 以下最佳決策模型，超越所有 4B、9B 模型，也超過 Decider 35B-A3B 的 47.11 分。

延遲表現方面，Liquid AI 與 NVIDIA 合作在多種邊緣與 GPU 平臺測試：

| 裝置 | 單一問題 | 3 個問題 | 384px 影像 |
|---|---|---|---|
| Jetson AGX Thor | 16 ms | 20 ms | 35 ms |
| Jetson AGX Orin 64GB | 26 ms | 35 ms | 83 ms |
| Jetson Orin Nano | 50 ms | 73 ms | 202 ms |
| NVIDIA RTX 4090 | 8 ms | 21 ms | 17 ms |

d1-3B 在每一款測試裝置上都能在 50 毫秒內回答單一問題，而且問三個問題只比問一個問題多花約 1.3 倍時間，顯示批次打包（packing）帶來的效率優勢。

💡 為什麼沒有視覺／音訊 benchmark 分數

團隊驗證了 d1-3B 保留了其骨幹 LFM2.5-VL-3B 的視覺能力，d1-omni-600M 也能處理三種模態，但並未公開視覺或音訊的 benchmark 分數。原因是目前的 Decision Index v0.3 只包含私有的視覺測試集，而音訊決策的評測標準本身仍是一個尚待解決的開放問題。

⚠️ 仍在研究階段的部分

d1-omni-600M 標註為「早期研究釋出」，本次並未公布它的速度數據；加上缺乏公開的視覺／音訊 benchmark，使用者在實際落地前仍需自行驗證多模態表現。

🎯 實務啟示

安裝需求是 `transformers>=5.14`，模型附帶自家程式碼，載入時要加上 `trust_remote_code=True`：

```python
from transformers import AutoModel
model = AutoModel.from_pretrained("LiquidAI/d1-3B", trust_remote_code=True)

questions = {
    "team": {
        "type": "choice",
        "instructions": "Which team should handle this?",
        "criteria": {"billing": "Charges, refunds, invoices", "technical": "App or site faults"}
    }
}
print(model.system_one("I was charged twice this month.", questions))
```

對需要在端側（edge）即時做多模態分類、路由或評分的場景，例如客服單據分流、產品影像檢查，d1-3B 提供目前同量級最佳的準確度；若裝置資源更吃緊，d1-omni-600M 用四分之一參數量換取可接受的效能損失，是值得評估的替代方案。

🔗 來源
- 標題：Multimodal open d1 decision models for the edge
- 作者／機構：Liquid AI（Aurelien Lac、Fernando Fernandes Neto、Edoardo Mosca、Maxime Labonne、Leonie Monigatti）
- 連結：https://huggingface.co/blog/LiquidAI/open-d1

#LiquidAI #EdgeAI #MultimodalAI #DecisionModels #VLM #OnDeviceAI #OpenWeights #NVIDIAJetson #MachineLearning #LLM
