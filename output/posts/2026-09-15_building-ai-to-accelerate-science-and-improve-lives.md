---
title: Building AI to accelerate science and improve lives
source: Google AI Blog
url: https://blog.google/innovation-and-ai/technology/ai/ai-applications-science-people/
model: claude-code/sonnet
generated_at: '2026-09-15T20:23:22.607248'
pinned: true
---

📌 從 90 億種基因變異到氣象預報，Google 揭露 AI 科學進展全貌

TL;DR：Google 公布 AlphaGenome、WeatherNext 3 等多項 AI 科學應用最新進度。

🎣 人類基因體裡，理論上可能出現的單一鹼基變異總共有 90 億種。Google 最近做的其中一件事，是用 AlphaGenome Atlas 把這 90 億種可能性全部圖譜化，並開放給研究者免費使用。這只是 Google 在過去幾週內公布的其中一項科學進展。

🤔 一篇總覽文章，串起四個焦點領域
Google Research, Labs, Technology & Society SVP James Manyika 在文章中指出，Google 把 AI 科學投入聚焦在四個領域：讓疾病可偵測、可治療、可預防；預測天然災害；擴大學習機會；為更多人創造經濟機會。文章同時提到一項里程碑：Google 的技術與產品現已支援超過 300 種語言，涵蓋 70 億使用者、佔全球人口 86%。

🧩 疾病偵測：從蛋白質結構到智慧型手機
- AlphaFold 已預測出科學界已知的全部 2 億個蛋白質結構，目前有 190 個國家、400 萬名研究者在使用，應用範圍從藥物開發到查加斯病、利什曼病等被忽視疾病的研究。
- AlphaMissense 協助研究者預測致病基因突變，新推出的 AlphaGenome Atlas 則進一步提供基因變異如何改變細胞行為的預測性洞察。
- 與 Imperial College London、英國 NHS 合作的乳癌研究顯示，AI 在 175,000 名女性的乳房攝影影像中，多偵測出 25% 原本會被漏診的間隔癌（interval cancer）。
- 結核病方面，全球約 40% 感染者未被確診，Google 的胸腔 X 光模型（由 Nexus Intelligence 使用）已在 6 個國家、40 個地點篩檢超過 25,000 張 X 光片，同時也在用 Health Acoustic Representations 這類生物聲學模型，嘗試透過咳嗽聲偵測結核病。
- 糖尿病視網膜病變篩檢模型已支援超過 115 萬次篩檢，目標在未來十年擴大到 600 萬次。
- Google 也在用一般智慧型手機與穿戴裝置嘗試偵測心血管疾病、胰島素阻抗、高血壓、脈搏消失與心率變化。
- Co-Scientist 這類協作型 AI 工具協助研究者加速產生與驗證假說（例如找出急性骨髓性白血病既有藥物的新用途），DeepConsensus、DeepVariant、DeepPolisher 等開源工具則協助完成人類基因體定序與首個泛基因體草圖。AMIE（Articulate Medical Intelligence Explorer）正與 Beth Israel Deaconess 等醫療機構合作，進行首次全國性真實場域臨床試驗。

🧩 天災預測：從颶風路徑到洪水地圖
- WeatherNext 3 是目前最精準的全球氣象模型，對一天以上的降水預報準確度提升 50%，且已用於 Google 產品中。
- Planetary Prediction Engine 整合全球健康、糧食安全、社會經濟資料，已被用於剛果民主共和國的伊波拉疫情應對，也在美國協助辨識 21 項 CDC 健康指標下的脆弱社區。
- 去年牙買加當局用 WeatherNext 準確預測颶風 Melissa 的路徑，提前取得防災資金並展開緊急應變；數個月前，Google 的地震警報系統也在地震發生前示警了委內瑞拉數百萬民眾。
- 2025 年，Google 的季風預測服務為印度 3,800 萬農民提供資訊；Flood Hub 現已涵蓋河川洪水與瞬間洪水，覆蓋超過 150 個國家、20 億處於洪災風險中的人口。
- 野火邊界預測已在美國及另外 33 個國家提供協助，Google 也在推動 FireSat 衛星星系計畫，目標偵測過去在地球上難以察覺的小型野火；2025 年，Google Search 上總共產生超過 520 則危機警報，觸及超過 7,500 萬使用者。
- 此外，Google 也在擴大 AI 研究以降低航空業的氣候衝擊，目前已在英國（與英國政府合作）與亞洲地區落地應用。

⚠️ Google 自己承認的前提
文章特別強調：這些效益並非必然發生。要真正把潛力轉換成實際成果，並降低相關風險與挑戰，需要整個社會共同努力，這也是 Google 在文中明確標註的限制。

🎯 實務啟示
這篇總覽最值得工程師關注的，是背後幾種可重複使用的技術模式：把基礎模型（AlphaFold）延伸到下游任務（AlphaGenome Atlas 的變異效應預測）、跨資料源融合做預測（Planetary Prediction Engine 結合健康、糧食、社會經濟資料），以及用更輕量的架構做到高解析度即時推論（WeatherNext 3 不需要龐大超級運算資源即可運作，對資料稀疏地區特別友善）。這些都是把研究成果轉為可規模化系統時值得借鏡的設計思路。

🔗 來源
- 標題：Building AI to accelerate science and improve lives
- 作者／機構：Google — James Manyika
- 連結：https://blog.google/innovation-and-ai/technology/ai/ai-applications-science-people/

#Google #AlphaFold #AlphaGenome #WeatherNext #AIforScience #HealthAI #DisasterPrediction #GoogleDeepMind #ClimateAI #GenomicsAI
