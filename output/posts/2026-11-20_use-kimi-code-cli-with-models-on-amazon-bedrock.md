---
title: Use Kimi Code CLI with models on Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/use-kimi-code-cli-with-models-on-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-11-20T23:25:57.136565'
score: 71
---

📌 Kimi Code CLI v2.7.0：免管理額外金鑰，直接用 AWS 憑證串接 Bedrock

TL;DR：Kimi Code CLI 新增原生 Bedrock provider，改用既有 AWS 憑證鏈認證，不用再多管一組 API Key。

多一組要額外保護的憑證，就多一個可能被洩漏的缺口。Moonshot AI 這次直接把這個麻煩從設定流程裡拿掉。

🤔 **問題：一個 agent CLI，兩套認證邏輯**

Kimi Code CLI 是 Moonshot AI（Kimi 系列開放權重模型的開發者）推出的開源 coding agent。在舊版本裡，要連到 Amazon Bedrock 上的模型，得把 provider 設成 `type = "openai"` 或 `type = "openai_responses"`，透過 OpenAI 相容的 Chat Completions 或 Responses API，並額外申請、設定一組 Amazon Bedrock API key。這組 key 可以是短期或長期憑證，但終究是一個獨立於 AWS 帳號體系之外、需要自己管理的秘密。對已經有一套 AWS 憑證鏈（named profile、SSO）在用的團隊而言，這等於多了一條平行的憑證管理路徑。

🧩 **原生 provider：直接借用你的 AWS 身分**

v2.7.0 加入的原生 `bedrock` provider 改變了這件事：設定時可以不填 `api_key`、`api_key_env`、`AWS_BEARER_TOKEN_BEDROCK`，讓 provider 直接沿用當前環境裡的 AWS 憑證（named profile 或 SSO 都算），由它解析出的 IAM 身分去請求 Amazon Bedrock。官方文件指出，整個流程會自動完成認證與路由，背後產生的是有效期最多 12 小時（或等於 AWS session 長度，取較短者）的臨時 API key，之後 CLI 再以串流方式接收模型回應，並能在編碼任務中使用 client-side tool calling。文中示範以 Kimi K3.1 Pro Highspeed 為例，該模型支援串流、可調整的 reasoning、圖片輸入與 client-side tool calling，並建議透過 global 跨 Region inference profile 存取，取得最廣的可用性與較低成本（官方文件提到此類全域 profile 定價比地理對應 profile 低 10%）。

需要留意的是，這只是把「哪組憑證在用」換成 AWS 原生身分，並不會改變使用者本來就該承擔的責任：IAM 權限仍要按最小權限原則授予，文中建議為 Kimi Code CLI 準備一個獨立的 IAM role，和日常 AWS 操作分開。

🧩 **實際設定要手動碰 config.toml**

目前 Kimi Code 的桌面版與網頁版介面還沒有把這套憑證鏈設定需要的所有欄位開放出來，官方建議直接編輯 `config.toml`。設定重點包括：在別名下填入 Amazon Bedrock 的全域 inference-profile ID 當作 `model` 值，並明確宣告該模型支援的能力（例如 Kimi K3.1 Pro Highspeed 支援 `always_thinking`、`thinking`、`image_in`、`tool_use`，但不支援 `audio_in`、`video_in`）。設好 `default_model` 後，啟動 session 就會自動選用對應模型。

⚠️ **幾個容易踩的雷**

- Kimi Code 不會自動偵測 Bedrock 上多數模型（包含 Kimi 系列）的能力，必須對照各模型的 Amazon Bedrock model card，自己在設定裡逐一宣告，且應只實際驗證過的能力才填，不能只信標籤。
- `bedrock` provider 必須在 `config.toml` 或 shell 環境變數裡明確指定 `AWS_REGION` 或 `AWS_DEFAULT_REGION`，無法從 `~/.aws/config` 或 `aws configure` 推斷；若用的是帶 `global.`、`us.`、`in.` 前綴的跨 Region inference profile，這個 Region 設定會決定請求實際送往哪個來源 Region。
- 若要透過 VPC endpoint 或其他端點連線，需要自行覆寫 API 協定與目標 URL，不能全靠自動偵測。
- 桌面版或網頁版介面顯示 provider 狀態「connected」，不代表 AWS 憑證、IAM 權限、Region 設定與網路路徑真的全部正確；務必用非互動模式送一次完整請求來驗證，出錯時再逐項排查。

🎯 **實務啟示**

對已經用 AWS SSO 或 named profile 管理團隊存取的組織，這個改動直接省掉一條平行的金鑰管理流程。測試完畢後記得清掉臨時建立的 IAM 身分或權限，並視需要還原本機的 provider 設定，避免留下多餘的存取路徑。

🔗 **來源**
- 標題：Use Kimi Code CLI with models on Amazon Bedrock
- 作者／機構：Alex Thewsey（AWS）
- 連結：https://aws.amazon.com/blogs/machine-learning/use-kimi-code-cli-with-models-on-amazon-bedrock/

#AWS #AmazonBedrock #KimiCode #MoonshotAI #LLM #CLI #IAM #CloudSecurity #AIAgent #DevOps
