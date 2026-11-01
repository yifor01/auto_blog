---
title: 'Nace AI Open-Sources Drex Max v1: A 27B Decision Model That Runs Locally on
  Apple Silicon'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/01/nace-ai-open-sources-drex-max-v1-local-inference/
model: claude-code/sonnet
generated_at: '2026-11-01T21:17:19.181697'
score: 92
---

📌 Nace AI 開源 Drex Max v1,27B 決策模型可在 Mac 本地跑

TL;DR：Drex Max 不生成文字,只替每個選項打機率分數,開源權重讓路由、分類、政策檢查能完全留在本機跑。

多數開源釋出都在比「生成能力」,Nace AI 這次開源的 Drex Max v1,目標卻是完全不生成任何文字,只回答「這個選項的機率是多少」。

🤔 **它回答的不是文字,是機率**

Drex Max 是 Nace.AI 的決策模型,針對給定的 context 回答帶類型的問題。你傳入一個 state(文字、JSON 或影像),加上一組命名好的問題,模型在一次前向傳播中,為每個選項回傳一個機率,不生成任何內容。問題分三種類型:在命名選項中做選擇、是／否判斷,以及順序分數。這讓它適合用在 agent 路由、工單分類與護欄檢查上;Nace 官方也把託管版本定位在路由、分類與政策檢查這三類場景。

🧩 **48 層線性注意力加 16 層全注意力的混合架構**

模型卡顯示,Drex Max 是一個 64 層的稠密 27B 骨幹網路。其中 48 層是 Gated DeltaNet 線性注意力層,從左到右依序運作;另外 16 層是全注意力層,每隔四層放一層,而且是非因果(non-causal)的,也就是每個 token 都能看到整個序列。影像會經過原生的視覺塔(vision tower)處理,對請求中的每個問題都可見。最後,一個 255 選項的讀出頭(readout head)把最後的隱藏狀態轉換成選項機率。設定檔標示模型類型為 qwen3_5,視窗長度為 262,144 個位置。

👷 **五種跑法,從 bf16 到量化 GGUF**

這次釋出附帶 bf16 權重、Q8_0 GGUF、一個 affine Q4 量化檔案,以及 llama.cpp 與 Ollama 的分支版本。Nace 文件列出 5 種執行環境,全部對外提供同一個 POST /v1/systemone API。affine Q4 量化檔案的目標是記憶體 24GB 以上的 Mac;Q8_0 GGUF 則需要 48GB。在 48GB 的 Mac 上,Nace 建議針對 Kapitsa 使用 --context 2048;Ollama 使用者可以設定 num_gpu 40,把 40 層卸載到 Metal,設成 num_gpu 0 則整個跑在 CPU 上。Ollama 分支版本需要在 Modelfile 裡加上一行 CAPABILITY decision 設定。

📊 **量化後機率誤差在 0.02 到 0.03 之間**

結果資料集涵蓋 140,620 筆請求,未回答的請求一律算錯。在 48GB 的 Apple M5 Pro 上,Q8_0 GGUF 與 H100 的 bf16 相比,每個機率的誤差落在 0.02 以內;affine Q4 與 Q8_0 相比,誤差落在 0.0329 以內,且沒有出現選項判斷翻轉的情況。Nace AI 團隊表示,Decision Index 0.4 沿用了與 0.3.1 相同的公開測試集。

⚠️ **數字為廠商自報,且為贊助文章**

以上所有數據均由 Nace AI 自行提供,文章本身也標明是 Nace AI 贊助的內容,這些量化誤差與匹配度數字尚未見獨立第三方的覆核,工程團隊在評估導入前,建議用自己的場景資料再做一次驗證。

🎯 **實務啟示**

對需要在 agent pipeline 裡做路由、工單分類或政策護欄檢查的工程師而言,一次前向傳播直接吐機率、不用等生成完成再解析文字,本身就能省掉不少後處理邏輯;加上權重開放、能在 Mac 本機跑,對重視資料不外流或延遲敏感的場景,是值得納入評估清單的選項。

🔗 **來源**
- 標題：Nace AI Open-Sources Drex Max v1: A 27B Decision Model That Runs Locally on Apple Silicon
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/01/nace-ai-open-sources-drex-max-v1-local-inference/

#AI #OpenSource #DecisionModel #LocalInference #AppleSilicon #LLM #EdgeAI #Routing #MachineLearning #ModelRelease
