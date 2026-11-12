---
title: Detecting and recovering from silent data corruption on Amazon SageMaker HyperPod
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/detecting-and-recovering-from-silent-data-corruption-on-amazon-sagemaker-hyperpod/
model: claude-code/sonnet
generated_at: '2026-11-12T23:01:44.264501'
score: 89
---

📌 Meta 訓練 Llama 3 405B 時踩過的坑:靜默資料損壞怎麼抓?

TL;DR:AWS 在 SageMaker HyperPod 上加了三個檢查,專門抓硬體不報錯卻算錯數字的靜默資料損壞(SDC)。

訓練 loss 曲線看起來完全正常,跑了好幾個小時,直到有人發現模型莫名其妙變弱或出現無法解釋的發散——這時候算力早就燒掉了。問題可能不是資料、不是超參數,而是某顆 GPU 一直在悄悄算錯數字,卻從來沒報過任何錯誤。

🤔 問題:硬體什麼都沒報錯,錯誤卻一路傳進每個模型副本

靜默資料損壞(silent data corruption, SDC)發生在硬體(例如 GPU)回傳一個錯誤但看起來合理的數字,卻不觸發任何錯誤訊號。在分散式訓練裡,這個錯誤數字會流進每個副本的梯度與權重。文章引用一個真實規模的案例:Meta 在 Llama 3 405B 預訓練的 54 天期間,用到多達 16K 張 H100 GPU,419 次未預期的任務中斷裡有 6 次被歸因於 SDC——而且這只是那些真的中斷了任務、又被追查出來是 SDC 的案例。

SageMaker HyperPod 本來就會替換回報故障的節點:健康監控 agent 監看 GPU 錯誤、深度健康檢查對節點做壓力測試、自動節點復原會換掉壞硬體。但 SDC 繞過了這一切,因為硬體從頭到尾什麼都沒回報,偵測只能從訓練任務本身下手。

🧩 三個檢查,嵌進 PyTorch DDP 的訓練迴圈

SDC 來自製造缺陷或矽老化,最常發生在張量核心裡的乘加運算單元——也就是模型訓練最密集使用的部位。那個有問題的電路大多數時候算得對,只有在高溫、電壓驟降或特定運算元組合的壓力下才會算錯,而且運算路徑本身沒有像記憶體那樣的 ECC 或 parity 保護,錯誤(例如該是 4.0000 卻算出 4.0001)永遠不會被標記,就這樣流進 activation 和梯度,再寫進每個副本的權重。

AWS 的做法是直接檢查運算結果本身,整套偵測迴圈分四步:
1. 偵測:訓練迴圈裡的三個檢查,透過比較資料平行(data-parallel)副本之間的差異,指出可疑的 GPU。
2. 定位:在用 Amazon EKS 編排的 SageMaker HyperPod 叢集上,Kubernetes 節點名稱本身就包含 instance ID,把可疑的 rank 對應到節點只是一次查詢。
3. 隔離與比對:停止任務、cordon 該節點,到 SageMaker HyperPod 可觀測性儀表板上查看它的 GPU 指標。
4. 確認與復原:在警報不明確時進行確認,審查後更換節點,再從可疑時間窗之前存的 checkpoint 恢復訓練。

三個檢查依固定順序排在每個訓練步驟裡:檢查一在 all-reduce 前後都檢查梯度是否有 NaN/Inf,一旦觸發就中止該步驟;檢查二是在固定的「稽核步驟」上做 ring replay,比較各副本的梯度指紋;檢查三在 optimizer 更新後比對權重指紋,若不一致就擋下 checkpoint 的儲存。這三個檢查只在資料平行副本數量足夠時才有意義——文章的測試在 4 臺 ml.p5.48xlarge 執行個體(32 張 H100 GPU)上進行,每個測試都在三臺執行個體上重複,這是檢查機制運作所需的最小數量。

💡 為什麼不能只看梯度範數,而要靠「指紋」比對

AWS 一開始嘗試的直覺做法,是標記本地梯度範數偏離當步中位數超過 k 個中位絕對差(MAD)的那個 rank。他們在 4 臺執行個體上跑了三次無故障訓練(一個 9.53 億參數模型,32 張 H100),記錄了 22,800 個步驟裡每個 rank 的本地梯度範數,結果這個方法行不通——單純比較梯度範數只能抓到 NaN 和 Inf,抓不到「有限但錯誤」的數值,這類錯誤必須靠重新運算才能發現。

真正有效的做法是把整個張量壓縮成「指紋」:每個張量生成兩個 64 位元的總和,一個是原始位元模式的單純加總,另一個是依位置加權的加總。只要張量裡有一兩個元素變了,指紋就會變(適用於元素數少於 2 的 32 次方、每個最多 4 bytes 的張量)。測試中發現,交換兩個權重值再補償性修改另外兩個值,單純加總完全看不出來,只有加權加總能抓到這種情況。

這套檢查之所以能分層運作,關鍵在於錯誤「落在哪裡」決定了哪個檢查能看到它:如果錯誤發生在 all-reduce 之前(某個副本的本地梯度算錯),all-reduce 會把這個錯誤值平均散布給所有副本,之後大家的權重又會一致——只有 all-reduce 之前的本地梯度看起來不一樣,這正是檢查一、二要抓的窗口。如果錯誤發生在 optimizer 更新中或更新之後,該副本的權重會從此跟其他副本不一致,這由檢查三的權重指紋負責。NaN 或 Inf 則是例外,它們會透過下一次 all-reduce 傳播到每個副本,之後大家又會「一致地錯」。

⚠️ 這套方法抓不到的情況

如果錯誤發生在 all-reduce 這個運算本身裡面(例如某張 GPU 把部分總和算錯),錯誤會同樣地傳給每個副本,權重依然彼此一致,三個檢查都會放過它。另外,若用 fp16 搭配 gradient scaler 訓練,需要把 scaler 本來就會跳過的 overflow 步驟排除在檢查之外,bf16 則沒有這個問題。這套方案是針對 PyTorch DDP 設計,張量平行、管線平行或 context 平行需要不同的處理方式。

🎯 實務啟示

這套方法的核心價值在於成本很低:兩個 64 位元加總的指紋運算,換來的是能在數萬步訓練裡抓出硬體悄悄算錯卻不報錯的罕見故障,並且跟 HyperPod 既有的節點替換與 checkpoint 機制直接串接。對任何跑大規模分散式訓練的團隊,在可疑時間窗之前有乾淨的 checkpoint 可回溯,是這整套偵測與復原流程能真正發揮作用的前提。完整程式碼已公開在對應的 GitHub repository。

🔗 來源
- 標題:Detecting and recovering from silent data corruption on Amazon SageMaker HyperPod
- 作者/機構:Siddharth Senger(AWS ML Blog)
- 連結:https://aws.amazon.com/blogs/machine-learning/detecting-and-recovering-from-silent-data-corruption-on-amazon-sagemaker-hyperpod/

#SageMakerHyperPod #SilentDataCorruption #DistributedTraining #PyTorchDDP #GPUReliability #LLMTraining #AWS #MLInfra #FaultTolerance #H100
