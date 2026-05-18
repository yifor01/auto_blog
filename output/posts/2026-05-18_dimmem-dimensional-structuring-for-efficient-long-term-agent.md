---
title: "DimMem: Dimensional Structuring for Efficient Long-Term Agent Memory"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.15759
score: 98
model: tencent/hy3-preview:free
generated_at: 2026-05-18T20:41:43.025399
---

📌 【結構化記憶讓 AI 更省】DimMem：維度化記憶框架提升效率  

你以為長對話記憶只能靠存完整歷史才準確？其實結構化的「維度」可能讓 AI 既省 Token 又不失精準。  

🤔 **長期記憶需要既準確又省資源，現有方法難兩全**  
LLM Agent 想利用過去互動的資訊，卻常面臨完整對話歷史耗費大量 Token，或是僅保留事實/摘要時會遺失結構導致召回不精確的兩難。  

🧪 **以時間、地點、原因、目的、關鍵詞為欄位的原子記憶單元**  
DimMem 將每筆記憶設計為具備明確欄位（time、location、reason、purpose、keywords）的自含單元，這種結構化表示同時支援維度感知的檢索、記憶更新以及選擇性地將相關內容放入模型情境，無需在 context 中保存完整對話歷史。  

📈 **在 LoCoMo-10 與 LongMemEval-S 上分別達到 81.43% 與 78.20% 準確率，且每查詢省下 24% Token**  
實驗顯示，DimMem 在兩個長期記憶基準上優於現有輕量級記憶系統，同時將 LoCoMo 每查詢的 Token 消耗降低了 24%。  

💡 **維度化結構使記憶可被學習提取，小模型 Qwen3-4B 經微調後即可媲美大型 extractor**  
進一步研究表明，維度記憶的抽取是可學的：在 DimMem schema 上微調後，Qwen3-4B 的 extractor 不僅超過使用 GPT-4.1-mini 的 LightMem，在關鍵設定下的表現甚至可與或優過遠 larger 的 extractor。  

⚠️ **目前僅在兩個基準測試上驗證，長期實際使用效果尚未長期追蹤**  
該研究主要在 LoCoMo-10 與 LongMemEval-S 上進行評估，尚未報告長期部署或真實使用場景的追蹤結果。  

🎯 **開發 LLM Agent 時可採用 DimMem schema，搭配輕量 extractor 降低成本並保留結構化檢索**  
對於需要長期記憶的 Agent 系統，可直接採用此維度化記憶表示，並配合經過少量資料微調的小型 extractor，在保持檢索精度的同時顯著降低 Token 開銷與計算成本。  

🔗 **論文連結**  
📝 DimMem: Dimensional Structuring for Efficient Long-Term Agent Memory  
👤 Wentao Qiu, Haotian Hu, Fanyi Wang, Jinwei Kong, Yu Zhang (StepOS; Xiamen University; ShanghaiTech University)  
🔗 https://arxiv.org/abs/2605.15759  
💻 程式碼：https://github.com/ChowRunFa/DimMem  

#AI #LLM #AgentMemory #DimMem #StepOS #XiamenUniversity #ShanghaiTech #資訊檢索 #機器學習
