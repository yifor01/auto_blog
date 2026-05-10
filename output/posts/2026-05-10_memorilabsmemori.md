---
title: "MemoriLabs/Memori"
source: GitHub Trending
url: https://github.com/MemoriLabs/Memori
score: 77
model: tencent/hy3-preview:free
generated_at: 2026-05-10T19:31:31.853883
---

📌 **MemoriLabs/Memori：讓 AI 代理的記憶來自「做什麼」而非僅「說什麼」**

你以為大型語言模型的記憶只能靠提示詞或對話歷史？Memori 提出另一種思路：記憶應該源於代理實際執行的動作，而不僅是它說過的話。

🤔 **現有 AI 記憶方案往往依賴於對話紀錄或額外的向量資料庫，卻難以無縫貼合既有系統**

當開發者想讓 LLM‑based agent 「記住」使用者偏好、任務狀態或過去的決策時，常見做法是手動將對話存入向量庫或自行設計快取層。這不僅增加實作複雜度，也常導致記憶與代理真實行為脫節——代理可能「說」它記得某件事，但實際上沒有根據該記憶執行對應動作。

🧪 **框架與資料庫不可知的 SDK，直接記錄代理的行為與上下文**

Memori 的核心設計是：

- **LLM、資料庫、框架皆可插拔**：不要求你改用特定向量庫或換掉現有 LLM 封裝。  
- **零設定雲端服務**（Memori Cloud）：註冊後取得 API key，即可開始使用。  
- **TypeScript 與 Python SDK**：  
  - 安裝：`npm install @memorilabs/memori` 或 `pip install memori`  
  - 初始化範例（TypeScript）  

```ts
import { OpenAI } from 'openai';
import { Memori } from '@memorilabs/memori';

const client = new OpenAI(); // 需要 MEMORI_API_KEY 與 OPENAI_API_KEY 環境變數
const mem = new Memori()
                .llm
                .register(client)
                .attribution('user_123', 'support_agent');

async function main() {
  // 第一次對話：儲存使用者偏好
  await client.chat.completions.create({
    model: 'gpt-4o-mini',
    messages: [{ role: 'user', content: 'My favorite color is blue.' }],
  });

  // 第二次對話：Memori 能在背景自動回憶該偏好
  const response = await client.chat.completions.create({
    model: 'gpt-4o-mini',
    messages: [{ role: 'user', content: "What's my favorite color?" }],
  });
  // response 應該包含「blue」這個答案
}
```

- **Python SDK** 使用方式類似，僅需 `from memori import Memori` 並設定相同的環境變數。

💡 **記憶來源於「做什麼」**：Memori 會在代理呼叫 LLM 時，自動將輸入、輸出以及使用者指定的上下文（如 `attribution`）持久化；後續請求時，它會在背景檢索相關紀錄並注入到 prompt 中，無需開發者額外編寫快取或檢索邏輯。

⚠️ **目前仍是 SDK 層級的工具，未提出新演算法或架構**  
根據 GitHub Trending 的說明與提供的評分理由，Memori 的價值在於「簡單、框架不可插拔、易於安裝與使用」；它沒有提出新的記憶檢索演算法、新的資料結構或新的訓練方法，因此在學術創新程度上屬於實用工具而非突破性研究。

🎯 **適合想快速為現有 LLM agent 加入持久化記憶的開發者**  
- 若你的專案已經使用 OpenAI、Anthropic 或其他 LLM 套件，只需加入 Memori SDK 與設定兩個 API key。  
- 透過 `attribution` 參數，你可以將記憶依使用者、代理或任務進行分區，避免跨領域干擾。  
- 記憶的讀寫完全在背景進行，對延遲影響極小，適合即時對話或代理工作流程。

🔗 **專案資訊**  
📦 專案名稱：MemoriLabs/Memori  
🔗 GitHub：https://github.com/MemoriLabs/Memori  
☁️ Memori Cloud 註冊與文件：app.memorilabs.ai 、 memorilabs.ai/docs/memori-cloud/  

你有試過讓 AI 代理「根據它做過的事」記憶嗎？歡迎在留言區分享你的使用經驗或改進建議 👇

#AI #LLM #Agent #Memori #開發工具 #TypeScript #Python #GitHubTrending #記憶系統 #软體開發
