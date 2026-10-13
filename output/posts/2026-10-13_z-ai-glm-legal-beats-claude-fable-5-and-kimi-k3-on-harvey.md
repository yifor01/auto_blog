---
title: Z.ai GLM-Legal Beats Claude Fable 5 and Kimi K3 on Harvey LAB
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/13/zai-glm-legal-harvey-lab-legal-ai-model/
model: claude-code/sonnet
generated_at: '2026-10-13T22:11:41.855431'
score: 87
---

📌 Z.ai推出GLM-Legal：Harvey LAB拿下19.2%全通過率，但API仍是申請制

TL;DR：GLM-Legal在嚴苛的法律agent基準Harvey LAB上拿下19.2%全通過率，是base模型的近3倍，但目前API僅限申請開放。

法律AI評測最怕的就是「表面厲害」。Harvey LAB用「全通過」(all-pass)這種近乎苛刻的標準逐條拆解模型的真實能力，而Z.ai的新模型，剛好在這個標準下交出了一張漂亮的進步成績單——只是細看官方圖表，故事沒那麼單純。

🤔 **法律工作的核心痛點，與一個不輕易過關的基準**

GLM-Legal定位給律師事務所、企業法務與compliance團隊使用，主打合約審閱（contract review）、證據分析（evidence analysis）與法規遵循研究（compliance research）。用來驗證它的Harvey LAB是一套開源基準，涵蓋1,250個任務、24個法律實務領域，背後有超過75,000條專家撰寫的評分標準（rubric criteria）。它採用「全通過」評分：一個任務要所有標準都過才算通過。負責跑榜的Vals AI用兩個LLM judge、關閉網路連線的環境評測，agent可取用檔案工具以及docx、pptx、xlsx技能。

🧩 **底層模型：320B參數、原生多模態，agent harness跟著模型一起進化**

GLM-Legal是Z.ai旗下GLM-5.3-Flash的領域專精版本。GLM-5.3-Flash是Z.ai第一個原生多模態的GLM-5系列模型，總參數320B、啟用參數18B，混合sparse attention與linear attention來壓低長context的服務成本，輸入支援文字、圖片、影片與檔案，輸出文字。Z.ai團隊描述，在post-training階段，agent harness與模型是共同演化的：訓練中出現的邊界案例（edge case）暴露了harness的瓶頸，修好harness之後又讓模型接觸到更真實的限制條件，如此反覆。

📊 **19.17% vs 6.67%，但官方圖表藏了6個排名更高的模型**

GLM-Legal在Harvey LAB上拿下19.17%，在79個模型中排名第7；base模型GLM-5.3-Flash只有6.67%，12.5個百分點的提升已由獨立評測方（Vals AI）重現。Z.ai的發表圖表把GLM-Legal放在Kimi K3（12.92%）、Claude Fable 5（11.25%）與GPT-6 Astra（5.42%）之前，這幾個數字也與Vals AI吻合——但圖表省略了排名更高的6個模型，其中第一名是Muse Spark 1.2的25.42%。另外GLM-Legal在單條criteria上的通過率為92.5%，頭部模型大致落在90%到95%之間。Z.ai還宣稱在LegalBench與中文向的PLawBench上與對手打平，但沒公布自家數字；Vals AI的實測是GLM-Legal 86.23%，Claude Fable 5領先於88.56%，Kimi K3為86.21%（以上均為Vals AI截至2026年10月12日的跑分，兩個GLM模型的計費都是每百萬token輸入$0.075、輸出$0.25）。

⚠️ **能看榜，但還摸不到模型**

截至2026年10月13日，Hugging Face上沒有GLM-Legal的模型庫，API也還是申請制，Z.ai沒公布價格。官方說GLM-Legal未來會進駐旗下桌面agent應用AutoClaw，但沒給時間表。目前可以直接用的是base模型GLM-5.3-Flash，每百萬token輸入$0.15、輸出$0.5。

🎯 **實務啟示**

在拿到GLM-Legal存取權之前，團隊可以先用base模型GLM-5.3-Flash把法律agent pipeline搭起來，之後換個model ID即可銜接。同時別只看廠商發表的對比圖，直接查Vals AI的Harvey LAB榜單，才能看到完整排名與被省略的對手。

🔗 **來源**
- 標題：Z.ai GLM-Legal Beats Claude Fable 5 and Kimi K3 on Harvey LAB
- 作者／機構：Michal Sutter（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/10/13/zai-glm-legal-harvey-lab-legal-ai-model/

#LegalAI #GLM5 #ZAI #LLM #HarveyLAB #AgenticAI #ContractReview #Multimodal #BenchmarkEvaluation #AIModelRelease
