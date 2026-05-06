---
title: "Revisiting General Map Search via Generative Point-of-Interest Retrieval"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.03397
score: 117
model: tencent/hy3-preview:free
generated_at: 2026-05-06T20:11:06.655718
---

📌 【腾讯地图 x 北京交大】生成式POI检索框架GenPOI

在地图搜「下班路上安静的咖啡馆」，结果出了一堆吵闹的连锁店？传统POI检索靠表面语义匹配，根本处理不了带上下文的模糊查询。

🤔 **傳統POI檢索過度依賴表面語意匹配，難處理模糊查詢**
興趣點（Point-of-Interest, POI）檢索是從大規模POI數據庫中識別相關候選的技術，是各類位置服務的核心基礎。但在通用地圖搜索場景下，傳統方法過度依賴表面層級的語意匹配，面對用戶輸入的欠規範（underspecified）查詢時越來越吃力。此類查詢往往高度依賴上下文、具備個性化特徵，現有檢索範式很難有效整合異構上下文，完成複雜的搜索意圖推理。

🧪 **千萬級騰訊地圖POI工業數據集驗證**
針對上述限制，團隊從生成式視角重新審視通用地圖搜索，提出生成式POI檢索框架GenPOI。該框架將異構搜索上下文與POI統一為結構化序列，借助大語言模型（LLM）的強上下文建模能力，實現空間感知的候選生成。核心創新包含兩點：一是Geo-Semantic POI Tokenization，將每個PO
