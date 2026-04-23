---
title: "Alibaba Qwen Team Releases Qwen3.6-27B: A Dense Open-Weight Model Outperforming 397B MoE on Agentic Coding Benchmarks"
source: MarkTechPost
url: https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/
score: 117
model: tencent/hy3-preview:free
generated_at: 2026-04-23T19:36:15.502209
---

📌 【Alibaba Qwen 團隊】27B 密集模型 Agentic 編程超 397B MoE

🎣 **折疊區優化 (The Hook)**
27B 參數的密集模型，性能壓過 397B 的 MoE 巨獸？
這款剛釋出的開源模型專為 Coding Agent 優化，還用上了混合注意力架構。
參數規模不再是唯一指標，小模型也能在垂直場景打爆大模型。

🤔 **Agentic 編程需求提升，參數規模非唯一指標**
當前 Coding Agent 需要處理倉庫級代碼推理、多文件編輯、前端工作流等複雜任務，產業普遍認為更大參數的 MoE 模型才能滿足性能需求。Alibaba Qwen 團隊此前已釋出 Qwen3.6-35B-A3B（3B 激活參數的 MoE 模型）、Qwen3.5 系列的 397B-A17B MoE 模型，而最新推出的 Qwen3.6-27B 是 Qwen3.6 家族首個密集架構模型，僅 27B 參數，卻在多項 Agentic 編程基準上超越上述兩款更大規模的 MoE 模型。

🧪 **混合架構+思維保留機制，Apache 2.0 開源**
Qwen3.6-27B 採用混合架構，結合 Gated DeltaNet 線性注意力與傳統自注意力機制，同時引入新穎的 Thinking Preservation（思維保留）機制，提升複雜任務的推理連貫性。模型採用 Apache 2.0 許可，完全開源可商用，提供兩個權重版本：BF16 精度版與採用 128 塊大小細粒度 FP8 量化的版本，後者性能與原版幾乎一致。兩個版本均兼容 SGLang (>=0.5.10)、vLLM (>=0.19.0)、KTransformers 與 Hugging Face Transformers，可直接從 Hugging Face Hub 下載。

💡 **27B 模型 Agentic 編程分數領先 397B MoE**
在 Agentic 編程相關基準測試中，Qwen3.6-27B 的表現優於更大規模的 MoE 模型：
- QwenWebBench（內部英中雙語前端代碼生成基準，涵蓋網頁設計、網頁應用、遊戲、SVG、數據可視化等7類）得分 1487，遠高於 Qwen3.5-27B 的 1068、Qwen3.6-35B-A3B 的 1397
- 在測試倉庫級代碼生成的 NL2Repo 基準上也有顯著提升，性能超過 Qwen3.6-35B-A3B 與 Qwen3.5-397B-A17B MoE 模型

🧠 **針對性優化比盲目堆參數更有效**
Qwen 團隊表示，此次發布優先考慮「穩定性與實際效用」，是根據社群直接反饋調整產品方向，而非單純優化基準測試分數。混合注意力架構平衡了線性注意力的推理效率與傳統自注意力的表現上限，Thinking Preservation 機制則避免了複雜任務中的推理中斷問題；針對前端工作流與倉庫級推理的專項優化，讓模型在 Coding Agent 所需的核心能力上表現突出，而非追求通用基準的虛高分。

⚠️ **公開資訊未提及特定限制，實測反饋待觀察**
目前官方公開資訊未提及明確限制，現有測試基準僅覆蓋 Agentic 編程的特定場景，其他場景的實際表現可關注後續社群實測回饋。

🎯 **Coding Agent 開發者可低成本獲得高性價比方案**
- 開發 Coding Agent 的團隊可優先測試該模型，27B 參數的密集架構部署成本遠低於 397B MoE 模型，且針對垂直場景性能更優
- 可根據部署環境選擇權重版本：BF16 版適合高精度需求場景，FP8 量化版可在幾乎不損失性能的前提下降低算力與顯存需求
- 模型兼容主流推理框架，可快速集成到現有工作流中，Apache 2.0 許可支持商用，無合規風險

🔗 **相關資源**
📝 新聞來源：MarkTechPost (2026 年 4 月 22 日)
✍️ 作者：Asif Razzaq
🔗 新聞連結：https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/
🤗 模型下載：Hugging Face Hub
- BF16 版：https://huggingface.co/Qwen/Qwen3.6-27B
- FP8 量化版：https://huggingface.co/Qwen/Qwen3.6-27B-FP8

你會考慮用 Qwen3.6-27B 搭建 Coding Agent 嗎？歡迎分享你的看法 👇

#Qwen #Alibaba #AI #CodingAgent #機器學習 #開源模型 #軟體工程 #AgenticAI #程式開發
