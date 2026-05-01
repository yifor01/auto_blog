---
title: "google-research/timesfm"
source: GitHub Trending
url: https://github.com/google-research/timesfm
score: 127
model: tencent/hy3-preview:free
generated_at: 2026-05-01T19:27:33.706463
---

📌 【Google Research】TimesFM 2.5 時序基模開源

模型參數從 500M 降至 200M，上下文長度卻從 2048 拉到 16k。
這款時序基礎模型的反直覺升級，還能直接整合進 BigQuery、Google Sheets 等生產工具。

🤔 **Google Research 開發預訓練時序基礎模型**
TimesFM 是 Google Research 開發的預訓練時間序列基礎模型，專用於時間序列預測。相關論文為 decoder-only 架構的時序基礎模型研究，收錄於 ICML 2024。所有模型檢查點已上架 Hugging Face 集合，同時提供 Google Research 官方部落格說明。

🧪 **2.5 版核心規格對比前代大幅升級**
TimesFM 2.5 於 2025 年 9 月 15 日發布，對比 2.0 版本的核心升級包括：
- 參數量從 500M 壓縮至 200M
- 最大上下文長度從 2048 提升至 16k
- 支援可選的連續分位數預測，最高可覆蓋 1k 預測 horizon
- 2025 年 10 月新增 XReg 協變量（covariate）支援

💡 **已落地多款 Google 第一方生產產品**
TimesFM 已整合至 Google 官方產品場景：
- BigQuery ML：支援企業級 SQL 查詢，兼顧擴展性與可靠性
- Google Sheets：可直接用於日常表格預測場景
- Vertex Model Garden：提供 Docker 化端點，支援 Agent 調用

💡 **輕量化設計兼顧效率與長期建模能力**
2.5 版本將參數壓縮至 200M 顯著提升推理效率，16k 上下文長度強化了
