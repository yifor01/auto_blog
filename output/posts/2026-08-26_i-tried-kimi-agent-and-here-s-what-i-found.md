---
title: I Tried Kimi Agent and Here’s What I Found
source: KDnuggets
url: https://www.kdnuggets.com/i-tried-kimi-agent-and-heres-what-i-found
model: claude-code/sonnet
generated_at: '2026-08-26T06:29:50.845447'
score: 69
---

📌 拆解 Kimi Agent：一個名字底下藏了六個產品

TL;DR：Kimi Agent 不是單一產品，而是模型、群體代理架構、桌面應用與 CLI 的集合，實測 API 與定價後發現免費層限制不小。

當你聽到「Kimi Agent」，很容易以為在講一個單一工具。但實際動手測試後會發現，這其實是一整個產品家族的統稱，不先把它拆開，很難公平評價其中任何一塊。

🤔 **先搞清楚：Kimi Agent 到底是哪六個東西**

Kimi K3 是底層模型：一個 2.8 兆參數的混合專家（MoE）模型，每個 token 從 896 個專家中啟動 16 個，具備 100 萬 token 的上下文窗口，由北京的 Moonshot AI（背後有阿里巴巴支持）開發。Agent Swarm 是建構在其上的架構，能在單一任務中同時拉起數十甚至數百個協同子代理，而非依序處理。Goal 是自主多步驟目標功能，設定一個自然語言目標，代理會自行規劃並執行。OK Computer 則是內建在 Kimi 聊天介面中的代理模式，能從單一提示生成多頁網站或簡報。Kimi Work 於 2026 年 6 月 10 日推出，是一款獨立的 macOS（Apple Silicon）與 Windows 桌面應用，透過名為 WebBridge 的瀏覽器控制擴充功能，直接在你的電腦上搜尋、捲動、填寫表單，模擬真人操作。Kimi Claw 則是雲端版本，讓任務在筆電闔上時仍能持續運行，彌補 Kimi Work 本機任務會隨螢幕休眠而中斷的限制。Kimi Code 則是專門的程式開發指令列介面（CLI）。

🧩 **Agent Swarm：少見公開自曝失敗模式的架構**

Agent Swarm 是這個家族中最受矚目的功能，Moonshot 官方對它的描述也比多數廠商行銷用語來得具體。它於 2026 年 1 月 27 日隨 Kimi K2.5 首次推出，被描述為一種可規模擴展的架構，能在沒有預先定義角色或人工設計工作流的情況下協調子代理協作。到了 2026 年 4 月 20 日推出的 K2.6，容量出現實質跳躍：單一任務最多可同時運行 300 個子代理實例，並執行超過 4000 次工具呼叫，Moonshot 宣稱相較單一代理依序處理同一任務，速度可提升 4.5 倍。Agent Swarm 目前也已運行於 K3 之上，Moonshot 表示在大規模平行搜尋上有進一步改善，但沒有公布超越 K2.6 的新容量數字。

值得直接肯定的是，Moonshot 並未只談成果，還公開記錄了這套架構的兩種失敗模式：一是「序列化崩潰」（serial collapse），也就是協調器雖然把工作分派出去，但子代理最終仍互相卡住、彼此等待；二是「假性平行」（fake parallelism），看起來工作被分散處理，但實際上彼此依賴度過高，根本無法從平行化中獲益。這對任何在評估「這個任務該不該拆給多個代理處理」的工程師來說，都是一個實用的判斷框架，而不只是 Kimi 專屬的警語——廠商願意連同能力數字一起公開自家的失敗分類，並不常見。

🧩 **實測 API：與 OpenAI SDK 相容，但有一個關鍵差異**

不需要付費方案，也能驗證幾件事。在 kimi.com 註冊只需要一組 Google 帳號，約十秒鐘即可完成，不需信用卡。免費層確實提供真實可用的功能，但限制不小：根據 TechRadar Pro 的實測評論，免費層將你限制在同一時間只能執行一個並行代理任務，而完整的代理功能集（也就是真正大規模使用 Agent Swarm）只有在每月 39 美元以上的方案才會解鎖——如果吸引你的正是群體代理架構，這道門檻相當關鍵，畢竟單一並行任務基本上違背了平行子代理的初衷。

Moonshot 的 Kimi API 與 OpenAI 相容，這意味著標準的 openai Python SDK 只需更換 base URL 與模型名稱就能直接對接：

```python
import os
import json
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["MOONSHOT_API_KEY"],
    base_url="https://api.moonshot.ai/v1",
)

MODEL = "kimi-k3"

TOOLS = [{
    "type": "function",
    "function": {
        "name": "count_words",
        "description": "Counts the number of words in a block of text.",
        "parameters": {
            "type": "object",
            "properties": {"text": {"type": "string"}},
            "required": ["text"],
        },
    },
}]

def count_words(text: str) -> int:
    return len(text.split())

def run_task(task: str, max_turns: int = 6) -> dict:
    messages = [{"role": "user", "content": task}]
    for turn in range(max_turns):
        response = client.chat.completions.create(
            model=MODEL,
            max_tokens=1024,
            tools=TOOLS,
            messages=messages,
            reasoning_effort="max",
        )
        message = response.choices[0].message
        if response.choices[0].finish_reason != "tool_calls":
            return {"answer": message.content, "turns_used": turn + 1}
        messages.append(message.model_dump(exclude_none=True))
        for tool_call in message.tool_calls:
            if tool_call.function.name == "count_words":
                args = json.loads(tool_call.function.arguments)
                result = count_words(args["text"])
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result),
                })
```

工具呼叫以熟悉的 message.tool_calls 格式回傳，finish_reason == "tool_calls" 是該執行工具並回頭迴圈的訊號，與標準 OpenAI chat-completions 契約一致。有一點 K3 特有的細節值得標註：K2 系列的舊參數 thinking 在 K3 中已被移除，改為 reasoning_effort，而截至目前為止 "max" 是唯一支援的數值，官方表示未來會推出更多層級。

📊 **定價跳了 5 倍，但快取能救回不少**

在定價上——這對 Kimi 整體訴求至關重要——K3 的價格為每百萬輸入 token 3 美元、每百萬輸出 token 15 美元，且整個 100 萬 token 上下文窗口內採固定費率，不依長度分級。這比 K2.6 的定價大約貴了 5 倍，值得留意的是，這代表 Moonshot 正在遠離 Kimi 系列賴以建立聲譽的極致低價定位。不過自動前綴快取（prefix caching）會將快取輸入的費率降至每百萬 token 0.30 美元，對長上下文、多輪對話的使用情境而言，這項機制明顯改變了成本結構。

💡 **獨立測試者怎麼說**

在正面評價方面，TechRadar 的實測發現 Kimi 在文件密集型任務上表現扎實：在同一段對話中丟入兩份長篇 PDF，要求交叉引用特定段落，回覆準確且組織良好，即使經過多輪追問也維持水準——長上下文處理被形容為 Kimi 最強項之一，且免費層就能使用。同一份評論也測試了 Kimi Code 在 Python 重構任務上的表現，輸出乾淨，架構層面的推理禁得起追問，雖然還不到 Claude Code 那種結構化解說的水準，但評論者認為考量價格差異，這樣的取捨是值得的。而在同一討論串中，一位 Hacker News 使用者則直白評價 K2.6 在原始能力上不如 Sonnet 與 Opus 4.0。

🎯 **實務啟示**

如果你的團隊已經在用 OpenAI SDK，Kimi K3 的接入成本幾乎為零，值得先用免費層測試長上下文文件分析這類場景。但若你真正想用的是 Agent Swarm 的大規模平行子代理能力，記得免費層一次只能跑一個並行任務，這幾乎等於拿不到這個架構真正的優勢，得先評估每月 39 美元的方案是否划算，並留意 reasoning_effort 目前僅支援 "max" 這個過渡期限制。

🔗 **來源**
- 標題：I Tried Kimi Agent and Here's What I Found
- 作者／機構：Shittu Olumide，KDnuggets
- 連結：https://www.kdnuggets.com/i-tried-kimi-agent-and-heres-what-i-found

#KimiAgent #MoonshotAI #AgentSwarm #LLM #MixtureOfExperts #AIAgents #OpenAICompatible #LongContext #DeveloperTools #LLMPricing
