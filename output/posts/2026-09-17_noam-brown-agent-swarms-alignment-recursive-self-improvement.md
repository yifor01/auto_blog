---
title: Noam Brown – Agent swarms, alignment, & recursive self-improvement
source: Dwarkesh
url: https://www.dwarkesh.com/p/noam-brown
model: claude-code/sonnet
generated_at: '2026-09-17T20:39:56.746701'
score: 80
---

📌 【OpenAI】10000 個 Agent、130 億 token，多 Agent 擴展的真相

TL;DR：OpenAI 研究者 Noam Brown 談用一萬個 Agent 解千禧年大獎難題的多 Agent 擴展規律與限制。

130 億 token,如果換成一個人全職思考、一週工作五天、每天八小時、從古蘇美文明一路算到今天不間斷地想，也才累積這麼多。而 OpenAI 的系統,用一萬個 Agent 在 88 小時內就燒掉了這個量級的算力，並宣稱解出了一個千禧年大獎難題(Millennium Prize Problem)。這是 Dwarkesh Patel 訪談 OpenAI 研究者 Noam Brown 的開場。Brown 是把 o1 等推理模型帶到現實的核心貢獻者之一，現在轉向研究多 Agent 系統。

🤔 **為什麼要多 Agent，而不是讓一個 Agent 想更久**

推理模型有個清楚的規律：把 test-time compute(推理時算力)拉高，模型在幾乎任何推理 benchmark 上的表現都會變好，道理就像人考試,五分鐘寫完整份考卷不如給五小時。但把單一模型的思考時間無限拉長，會撞上延遲瓶頸,沒有人想等一個回答等三年。解法是平行化：找一群 Agent 一起做，就像創業要找一個團隊而不是一個人單打獨鬥。多 Agent 因此是一種「平行擴展 test-time compute」的方式，而不是單一 Agent 序列式地想更久。Brown 也直言，這種方式效率較低,因為沒有一個 Agent 能獨佔全部上下文，但如果做得好，仍是有效的擴展路徑。

🧩 **平行化的代價：亞線性擴展，而且看任務**

OpenAI 在發布 GPT-5.6 時首次把正式的多 Agent 系統做成產品選項(Ultra Mode),預設是 4 個 Agent 協作，使用者可以自行調高。官方部落格公開了一些 benchmark 上的擴展曲線：某些 benchmark 中,4 個 Agent 協作能把作答時間縮短一半，代價是要多付 2 倍算力去換取 2 倍速度；擴大到 16 個 Agent 也能看到類似的模式，只是效率稍微下降,呈現「亞線性(sublinear)」而非線性的加速。

這個效果高度依賴任務種類。數學題目相當適合平行化(雖然不是最容易平行化的類型)；像 Deep Research 這種需要翻閱大量來源的網路搜尋任務,則是「極度」適合平行化。相對地，Brown 推測寫小說這類任務很難從平行化中獲益,就像找一萬個人一起寫同一本小說,大概也不會寫得更好。

💡 **一萬個 Agent 是目前唯一的一個資料點**

Brown 坦言,目前業界對多 Agent 擴展的科學認知其實還很薄弱。OpenAI 公開發布的擴展曲線只測到 16 個 Agent 左右的規模，要把這個規律驗證到一萬個 Agent 的量級非常昂貴,這次解出千禧年大獎難題的系統，某種意義上只是「一個週末做出來的一個資料點」，還稱不上系統性的科學結論。

⚠️ **這仍是未發布模型與早期觀察**

訪談中談到的多 Agent 系統尚未公開發布，Brown 自己也用「一堆天真的問題」來形容主持人的提問角度,顯示這整套多 Agent 擴展規律目前仍處於摸索階段,亞線性加速比例、平行化程度都因任務而異，缺乏大規模、系統性的驗證。

🎯 **實務啟示**

在設計多 Agent 系統之前,先問任務本身的可平行化程度：高度可分解、可獨立驗證的任務(數學驗證、多來源檢索、程式碼平行測試)適合用多 Agent 換速度；需要單一連貫脈絡與創造性判斷的任務(寫作、長篇規劃)則未必能靠堆更多 Agent 解決,反而可能只是多付算力錢。

🔗 **來源**
- 標題：Noam Brown – Agent swarms, alignment, & recursive self-improvement
- 作者／機構：Dwarkesh Patel(訪談對象：Noam Brown, OpenAI)
- 連結：https://www.dwarkesh.com/p/noam-brown

#OpenAI #MultiAgent #ReasoningModels #TestTimeCompute #AIAlignment #RecursiveSelfImprovement #NoamBrown #LLM #AgentSwarm #AIResearch
