---
title: A/B test models in production
source: Together AI
url: https://www.together.ai/blog/a-b-test-models-in-production
model: claude-code/sonnet
generated_at: '2026-08-18T06:35:27.477282'
score: 81
---

📌 Together AI 讓 A/B 測試變成 Endpoint 內建功能

TL;DR:Together AI 平臺把模型 A/B 測試邏輯下沉到 endpoint 層,不必再自己刻分流程式碼。

模型在 benchmark 上分數更高,不代表使用者真的比較喜歡它。想知道答案,唯一辦法是讓真實流量對照著跑。

🤔 為什麼 Shadow Traffic 不夠用

每個團隊遲早都要回答同一個問題:新模型對使用者來說是不是真的比較好?不是在 benchmark 上更好,而是在留存率、按讚率、任務完成率這些產品實際在意的指標上更好。Shadow traffic 只能驗證候選模型在延遲、錯誤率、吞吐量上運作正常,它的回應會被丟棄,沒有使用者會依照它行動,回答不了品質問題。

多數團隊的做法是自己在應用層刻:用 feature flag 或對 user ID 做 hash-mod-100,維護兩個 endpoint 讓客戶端切換,再用一份文件記錄 A/B 兩組代表什麼。這樣做的問題是實驗邏輯和基礎設施糾纏在一起——分流程式碼跟著應用一起上線,cohort 分配可能因客戶端快取決策而漂移,實驗「結束」後那段分支程式碼往往因為沒人敢確定安全而長期留在程式庫裡。

🧩 Endpoint 層的 A/B 實驗怎麼設計

Together AI 把 A/B 實驗直接掛在 endpoint 上:一個實驗恰好有一個 control 與最多 20 個 variant 成員,每個成員指向一個 deployment 並帶有百分比設定,所有百分比加總須為 100。運作機制是,當基礎流量分配把請求路由到 control 時,實驗會在其成員之間重新取樣,依百分比重新分配流量——換句話說,實驗是在 subdivide control 原本分到的那份流量。

有兩個關鍵限制要注意:variant deployment 不能出現在 endpoint 原本的 traffic split 裡,平臺要求 variant 的權重必須是零,只有 control 留在基礎分配中,實驗會完全接管路由到 variant 的流量;另外 A/B 的百分比是固定的絕對流量佔比,獨立於 replica 數量,這點刻意設計得和「跟著 ready replica 數量走」的 traffic-split 權重不同,目的是讓量測期間的分流比例不會隨著自動擴縮而漂移。

建立一個 95/5 實驗只需要一行 CLI 指令:

```
tg beta endpoints ab my-org/candidate-model --control $CONTROL_DEPLOYMENT --percent 5
```

客戶端完全感受不到變化,同一個 endpoint 名稱、API、金鑰照舊,後端則有 5% 的請求交給 variant 處理。

升溫(ramp)的做法是重新送出完整的成員清單,而不是呼叫另一個「ramp」API,這讓心智模型維持簡單:實驗永遠等於成員清單本身。更新請求會帶上 etag,若隊友同時在調整同一個實驗,後送出的更新會被拒絕而不是悄悄覆蓋掉對方的設定。

流量佔比怎麼選,素材給出了一份對照:

| 分配比例 | 訊號速度 | 風險 | 適用時機 |
|---|---|---|---|
| 95/5 | 慢(需要量與時間) | 最小 | 新模型第一次真實曝光 |
| 80/20 | 中等 | 可控 | 已挺過 5% 測試,想要更顯著的讀數 |
| 50/50 | 最快 | 影響一半使用者 | 兩個已知不錯的方案做最終確認 |

📊 量測與收尾

平臺側的指標(延遲、錯誤率、吞吐量)本來就是每個 deployment 各自可查,量測的重點在產品側:把每筆回應對應的 deployment ID 連同評分、重試、任務完成率等品質訊號一起記錄下來,join key 就是 deployment ID。平臺刻意不替你猜品質指標是什麼,只確保歸因這件事本身是簡單的。

若 variant 勝出,收尾分兩步:先用 blue-green rollout 把流量從 control 正式切到 variant deployment(健康檢查、傳播等待、回滾安全機制照常適用),再刪除實驗本身,所有實驗路由消失,100% 流量回到 endpoint 的基礎分配——此時它已經指向贏家。若 variant 輸了,直接刪除實驗即可,流量會完全回到 control。

⚠️ 邊界情況

如果 variant 在實驗過程中表現變差,受影響的只有它自己那個 cohort——deployment 各自獨立監控、獨立自動擴縮,不會拖累 control。要修正只需重新送出不含該 variant 的成員清單,使用者會在一定的傳播時間內回到 control,這也是為什麼從 5% 起步是穩妥做法。

🎯 實務啟示

比起自己在應用層維護 hash-mod-100 邏輯與一堆分流分支程式碼,把 A/B 實驗當成 endpoint 的原生能力來用,好處是實驗結束後不會留下技術債:刪除實驗就等於完全撤回分流邏輯,不需要額外清理客戶端程式碼。

🔗 來源
- 標題:A/B test models in production
- 作者/機構:Together AI
- 連結:https://www.together.ai/blog/a-b-test-models-in-production

#LLMOps #ABTesting #ModelDeployment #TogetherAI #MLInfrastructure #ProductionML #BlueGreenDeployment #Experimentation #LLM #DevOps
