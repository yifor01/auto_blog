---
title: Uplifting conversion across the acquisition funnel with personalization using
  contextual bandits on AWS
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/uplifting-conversion-across-the-acquisition-funnel-with-personalization-using-contextual-bandits-on-aws/
model: claude-code/sonnet
generated_at: '2026-10-01T22:08:56.162158'
score: 85
---

📌 情境式 Bandit 優化獲客漏斗，而非單一轉換率

TL;DR：Amazon Payments 用多目標 LinUCB bandit 跑過整個獲客漏斗，七週 A/B 測試顯示關鍵在內容而非模型。

生成式 AI 讓產生大量個人化內容變得又快又便宜，但這也製造了新問題：面對一堆可選內容，該給哪個使用者看哪一版，又要花多久才能知道答案？AWS 這篇文章接續先前討論 Bedrock 生成個人化內容的文章，聚焦在「選擇」這一關，分享 Amazon Payments 如何用多目標情境式多臂拉霸機（contextual multi-armed bandit，MAB）在 Amazon SageMaker AI 上解決這個問題。

🤔 **從單一指標到整條漏斗**

多臂拉霸機是一種強化學習方法，適用於選項多、流量有限的場景：把每種內容變化視為一支「arm」，用真實流量去試，並逐步把曝光導向表現好的 arm，同時保留一部分流量繼續測試其他 arm，這就是探索（exploration）與利用（exploitation）之間的經典取捨。文章提到選用 UCB（Upper Confidence Bound）策略：選擇「預估報酬＋不確定性加成」最高的 arm，這個決策規則是確定性的，代表每一次曝光的決策都可以被稽核與重現。但標準 bandit 只會為全體受眾學出一個最佳 arm，真正的個人化需要依據「這個人是誰」來決策，這正是情境式 bandit（contextual bandit）要解決的問題：不再問「哪個內容整體最好」，而是把造訪者的行為訊號（例如付款行為、交易組合等）表示成一個特徵向量，讓模型學到的模式能遷移到從未見過的相似造訪者身上，而不需要像分段式 bandit 那樣為每個人工切分的群組單獨累積流量。

🧩 **LinUCB 與三階段的「蹺蹺板問題」**

團隊選用 LinUCB（Li et al., 2010）作為情境式方法，理由是它計算效率高、決策可稽核，且在 arm 數量多、冷啟動資料有限時仍能運作，核心假設是每個 arm 的預期報酬是情境向量的線性函數。每個 arm 在每次曝光後都會更新兩組累積統計量，報酬除以累積經驗即可得到估計值（θ = A 的反矩陣 乘以 b），隨著證據增加，探索加成（exploration bonus）也會跟著收斂；這個加成同時是情境相關的，對模型很少見過的造訪者類型給予較大加成，對常見的類型則給予較小加成。

這次的使用者旅程分成三個階段：申請開始、送出申請、核准，是一個多階段的結果，而非單一指標。文章稱此為「蹺蹺板問題」：針對「開始申請」最佳化的內容容易吸引廣泛受眾，但核准與否取決於優惠是否真的適合申請人；只最佳化某一階段可能讓另一階段變差，但若只針對核准（approval）最佳化，又會因為核准案例稀少且延遲出現而讓模型缺乏訊號。解法是為每個階段（開始、送出、核准）各跑一個獨立的 LinUCB 模型，再用線性組合把三個 UCB 分數加總，權重可以依業務優先順序指定，也可以透過額外的校準步驟學出來；團隊實際採用大致相等的權重，但也提到之後可以等模型「熱身」完成後再提高核准階段的權重，或者在真的存在取捨時改用 Pareto frontier。

📊 **七週 A/B 測試：問題出在內容，不在模型**

線上 A/B 測試跑了七週，其中一個客群在最終轉換率上出現高個位數百分比的相對提升，但另一個客群完全沒有改善。文章直言：「問題出在內容，不在模型」，也就是說 bandit 架構本身運作正常，真正限制效果的是 arm 池（可供選擇的內容變化）的品質與多樣性。

💡 **兩個實務細節：alpha 怎麼調、延遲回饋怎麼處理**

控制探索與利用平衡的 α 參數，數值越高越傾向探索未充分測試的 arm，Li et al.（2010）建議的合理預設值是 1.0；實務上建議在 arm 空間大、歷史資料少時先設高一點，隨證據累積再調低，常見範圍落在 0.1 到 2.0 之間，由於 α 只是單一純量，用網格搜尋（grid search）調整相當直接。另一個挑戰是核准決策通常要延遲數天才會出現，團隊用一個歸因窗口（attribution window）處理：開始與送出申請立即更新模型，核准結果則保留到下一次批次處理週期才納入，避免因為申請案仍在審核中而產生向下偏誤，這個設計也剛好契合團隊原本每週一次的批次處理節奏。arm 池本身則是由一小組經過審核的素材組合而成，例如產業主題圖片與利益導向的標語，arm 空間是這些素材的笛卡兒積（Cartesian product），文章強調審核的對象是「素材本身」而不是「所有組合」，這讓做法在 arm 池不斷擴大時仍然維持可擴展性與內容把關。

⚠️ **效果因客群而異**

文章坦言其中一個客群完全沒有看到改善，顯示 bandit 架構雖然能自動找到表現最好的內容，但無法彌補 arm 池內容本身對該客群缺乏吸引力的問題，這也是在導入前需要正視的限制。

🎯 **實務啟示**

如果你的團隊已經有能力用生成式 AI 快速產出大量內容變體，contextual bandit 提供了一個比傳統 A/B/n 測試更有效率的方式持續收斂到最佳內容，而且不需要等測試跑完才能做決策。更重要的是這篇文章示範的多階段漏斗作法：與其只盯著最終轉換率，不如把漏斗拆成幾個階段分別建模，再用加權組合避免「蹺蹺板問題」讓某一階段的最佳化犧牲另一階段的表現。

🔗 **來源**
- 標題：Uplifting conversion across the acquisition funnel with personalization using contextual bandits on AWS
- 作者／機構：Chidi Prince John（AWS）
- 連結：https://aws.amazon.com/blogs/machine-learning/uplifting-conversion-across-the-acquisition-funnel-with-personalization-using-contextual-bandits-on-aws/

#ContextualBandits #MachineLearning #Personalization #LinUCB #AWS #SageMaker #ReinforcementLearning #ABTesting #ConversionOptimization #AmazonPayments
