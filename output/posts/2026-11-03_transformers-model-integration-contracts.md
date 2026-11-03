---
title: Transformers Model Integration Contracts
source: HuggingFace Blog
url: https://huggingface.co/blog/transformers-mic
model: claude-code/sonnet
generated_at: '2026-11-03T22:38:09.469566'
score: 85
---

📌 一個 UMT5 小模型，抓到了潛伏兩個月的 attention bug

TL;DR：Hugging Face 用「縮小版模型」做快速整合測試,成功在 PR 階段抓出可能漏進 main 的模型 bug。

2026 年 7 月 30 日,Transformers 為 T5 系列啟用了 PyTorch 的 SDPA（scaled dot-product attention）,結果副作用是 UMT5 的 decoder 可以偷看到未來的 token——訓練時,模型其實看得到它該要預測的答案。沒有任何東西崩潰,這個 bug 就這樣在 main 待了快兩個月才被修掉。等團隊事後重放那段時間的 commit 歷史,一個小型的 UMT5 模型,在每一次 commit 上都抓到了它。

🤔 **750 多種模型,測試跑不完怎麼辦**

Transformers 目前支援超過 750 種模型類型,CPU 測試超過 8.8 萬筆,每日 GPU 測試更超過 20 萬筆,涵蓋 pipeline、訓練、分散式執行、量化與 attention kernel。真正能抓到 regression 的整合測試,需要載入真實 checkpoint 並在真實硬體上跑模型 API,但每個 PR 都跑一輪,等於要讓大量 GPU 整天保持忙碌,並不現實。等到排程跑出結果,bug 往往已經進了 main——UMT5 那個 bug 就是這樣。

🧩 **Model Integration Contract：把模型縮小,但保留每種層**

Hugging Face 的解法是「縮小模型」,並把這套縮小+測試的流程標準化成 Model Integration Contract（MIC),包含三個部分：

- **fixture**：用真實 checkpoint 的設定,做出一個層數更少、維度更窄,但保留每一種層類型的小模型,一次建置、重複使用。
- **usage path**：一份可執行的 Markdown 範例,示範使用者實際會做的事,例如生成文字或跑一個訓練步驟。
- **baselines**：跑過這個範例後記錄下來、經人工審核過的輸出結果。

只要在 fixture 上跑 usage path,結果仍與 baseline 一致,contract 就算成立。一個 contract 對應的是「架構 + 使用路徑」,不是單一 checkpoint——相容的 checkpoint 可以共用同一個 fixture,各自保留自己的預期結果。

縮小模型的具體作法有四步：先縮小設定（保留不同種類的層,例如 sliding attention 和 full attention 混合,或 dense 與 MoE 混合層,必要時參考模型自己的 ModelTester 挑選的小尺寸);接著保持前處理不變（詞彙表、特殊 token、輸入維度不動,tokenizer 與 processor 檔案逐位元複製);然後建置並驗證權重（先試隨機種子權重,改變輸入檢查模型是否有反應,沒反應就在 contract 的小批量範例上訓練它,失敗就打掉重練);最後凍結並記錄基準輸出,人工審核過不同平臺與精度下的結果後才發布。

以 UMT5 為例,實驗用的 fixture 只有 66 MB 權重,相較原始 checkpoint 的 1,227 MB。更極端的案例是 Llama 4 Scout：1,086 億參數縮成 4,470 萬,視覺層從 34 層減到 2 層,語言層從 48 層減到 4 層,但保留了所有被檢查的層類型與 MoE 路由方式。

📊 **重放歷史,13.4 秒就抓到 bug**

團隊把凍結的 MIC 重放過去五個月的 Transformers commit 歷史,UMT5 的小型 fixture 從 7 月 30 日 bug 引入的那一刻起,到 9 月 28 日修復為止,每一次 commit 都能抓到異常：標籤的 log 機率與人工審核過的 baseline 相差 1.22,訓練 loss 相差約 0.20。團隊接著在一個驗證用的 proof branch 上還原這個修復,檢查果然再次失敗,且差異數字相同,對應 T5 contract 的 runner 步驟在 CPU 上只花了 13.4 秒（不含環境設定時間）。值得注意的細節是：這個 contract 用的是 SDPA（預設的 attention 路徑),如果只跑 eager attention 版本,反而會漏掉這個 bug——fixture 必須走與真實 checkpoint 相同的程式路徑,否則測試毫無意義。

🧩 **怎麼用：CLI 工具 tmic**

團隊提供 CLI 工具 tmic 來建立 contract 與 fixture。針對新模型,流程是讓 LLM 起草 usage code 與 manifest,再用 CPU 與 GPU 跑出候選 baseline——但 LLM 只負責起草,不負責核准,任何預期結果的變動都需要人工審核。本機試跑指令大致如下：

```
pip install "transformers-mic[runtime]" "hf-doc-builder @ git+https://github.com/huggingface/doc-builder.git"
hf auth login
tmic run org/model --local-only --fixtures-only --no-history --bill-to ''
```

這會在本機起草 contract、建置 fixture 並記錄基準,每一步都會要求人工確認,且在上傳任何東西之前就停下來。

⚠️ **不是萬能解法**

文章也坦承,fixture 無法取代完整的整合測試,它的價值在於讓 PR 階段「有機會」在 bug 進 main 之前抓到問題。另外像 Whisper 這類模型,隨機權重幾乎對音訊變化沒反應,團隊只好改用幾個對應到「red」「green」等單字的簡單音調去訓練它——目的不是教模型做語音辨識,而是讓音訊路徑上的變化能在輸出上被看見。

🎯 **實務啟示**

如果你維護的也是一個支援大量模型架構的函式庫,這套「縮小但保留層多樣性 + 凍結基準 + 走真實程式碼路徑」的做法,值得參考。相較於單純做 tiny-random checkpoint 的 forward pass 測試（UMT5 bug 就是這種測試會放過的那種),MIC 的關鍵差異在於它比對的是具體數值（loss、log 機率、梯度是否有限),而不只是「有沒有跑起來」。

🔗 **來源**
- 標題：Transformers Model Integration Contracts
- 作者／機構：Tarek Ziadé, Hugging Face
- 連結：https://huggingface.co/blog/transformers-mic

#HuggingFace #Transformers #CICD #SoftwareTesting #MachineLearning #ModelIntegration #UMT5 #AttentionMechanism #MLOps #OpenSource
