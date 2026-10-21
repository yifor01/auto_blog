---
title: 'Beyond the KV cache: Training and serving i14’s Laplace 3B linear attention
  model on AWS Trainium2 with native PyTorch'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/beyond-the-kv-cache-training-and-serving-i14s-laplace-3b-linear-attention-model-on-aws-trainium2-with-native-pytorch/
model: claude-code/sonnet
generated_at: '2026-10-21T20:50:49.003749'
score: 111
---

📌 i14把線性注意力模型Laplace 3B搬上AWS Trainium2

TL;DR：i14用原生PyTorch把固定狀態的線性注意力模型搬上Trainium2，繞過KV快取隨對話成長的問題。

多數大型語言模型靠softmax attention撐起上下文理解，但也因此背上了一個隨對話長度線性增長的包袱：KV快取。i14的答案是讓模型的狀態完全不隨上下文變長而變大。

🤔 上下文越長，KV cache越肥，併發就越少

Transformer的softmax attention在推理時需要持續累積KV快取，上下文越長，快取越大，結果是併發能力下降、服務成本上升，agent類應用甚至必須主動丟棄有用的歷史紀錄來控制成本。i14設計的Laplace 3B選擇了一條不同的路：用Gated Linear Attention（GLA）把歷史壓縮進一個固定大小的遞迴狀態，讓每個序列的狀態大小固定在29.5MB，不論上下文多長都不變。

i14是一家開發模型架構、元件與執行環境的AI研究與技術公司，其設計思路來自AI、計算認知科學，以及生物系統如何隨時間學習的研究。i14與AWS合作，透過TorchNeuron Native的原生PyTorch支援，把這個客製架構搬上Trainium2，同時保留了原本的GLA設計與Muon optimizer。

🧩 24層解碼器，用固定大小的矩陣狀態取代KV cache

Laplace 3B是一個24層的i14解碼器，每一層都用Simple GLA取代了softmax attention。資料流大致如下：每個token的殘差向量（維度D=3072）先經過LayerNorm，再通過寬度k=4、帶SiLU的深度可分離因果Conv1d，取得一個4-gram摘要；接著進入一個融合矩陣投影Wqkvg（維度9216×3072，其中9216=H×（2dk+2dv）），切出queries、keys、values與一個稍後在mixer之後使用的gate（H=16個頭，dk=96，dv=192）。

GLA mixer是核心：每個頭維護一個dk×dv（96×192）的矩陣狀態，用來存放過去key-value配對的壓縮、衰減記錄，並對整段歷史做基於內容的檢索。每個頭的衰減速率在初始化時就固定（並非學習得來），由一個幾何排程設定，讓16個頭擁有不同長度的記憶跨度。注意力區塊與殘差之後，接著第二個LayerNorm與一個內部維度8192的GLU（SiLU）FFN，由兩個升維矩陣與一個降維矩陣組成，再接第二個殘差。因為每個頭的狀態大小固定在96×192，不會隨序列長度增加，推理時每個token的運算量是O(1)，訓練的運算量則是O(T)而不是softmax attention的O(T²)。

🧩 搬上Trainium2要過的三道關

Laplace 3B原本用GPU最佳化的Triton kernel，即flash-linear-attention函式庫中的fused_chunk_simple_gla。AWS Generative AI Innovation Center（GenAIIC）團隊先用標準PyTorch運算子重寫了GLA kernel，並在比較後選擇了TorchNeuron Native這個Trainium原生PyTorch backend的beta版本，因為它表現更好。

Trainium2的三個特性決定了實作方式：軟體管理的晶片內記憶體、晶片間高速互連，以及一個會把GLA遞迴追蹤成固定計算圖的靜態編譯器。trn2.48xlarge這款實例由16顆Trainium2晶片、64個邏輯NeuronCore、高頻寬記憶體與NeuronLink-v3互連組成；每個NeuronCore有一個128分區的28MiB SBUF與一個2MiB的PSUM，PSUM連接到一個128×128的systolic Tensor Engine，SBUF不是快取，而是由編譯器提前排好每一次HBM到SBUF的資料搬移，不存在cache miss或eviction。

具體改動包含兩項：第一，GLA kernel重寫成固定chunk的顯式迴圈，chunk數量在編譯時固定，決定了反向傳播展開的深度，設定為fla_num_chunks=16，每個chunk涵蓋C=128個token，chunk內部的運算是平行的masked linear attention，只有跨chunk的狀態更新是序列執行的。由於SBUF剛好有128個分區，128-token的chunk可以一個token對應一個分區，完全不需要補零或跨分區搬移資料，這個對齊讓實測吞吐量提升了14%。

第二，Muon optimizer的分散式重寫：Muon會在更新前對每個梯度做正交化，針對96個二維權重矩陣（共27.18億參數）各跑五次Newton–Schulz迭代。在FSDP2下，64個rank各自只持有矩陣的1/64，單一rank本地算出的Gram矩陣只是一個對角區塊，會丟失所有跨rank的項。naive做法是讓每個rank收集完整梯度（5.44GB）、由一個rank跑Newton–Schulz再廣播結果，每一步要搬動10.87GB，且其他63個rank全程等待；最終採用的生產做法則是用all_to_all轉置（MuonFSDP2）：先用一次all_to_all讓每個rank拿到幾個完整的矩陣，64個rank平行跑Newton–Schulz，再用第二次all_to_all把結果送回。

📊 單機12萬token/秒訓練，逾萬token/秒服務

在單臺trn2.48xlarge實例上，Laplace 3B的訓練吞吐量約為每秒12萬個token；在服務端，模型在1,280個併發序列下，達到每秒11,544個輸出token。

⚠️ 壓縮歷史不是免費的，檢索品質要自己驗

GLA用壓縮取代了保留每一組key和value，這代表檢索品質不是免費的，原文指出使用者必須針對自己的工作負載評估檢索品質是否足夠。固定狀態帶來的好處比較適合長時間運行的agent、大型文件分析，以及需要可預期服務資源、長期記憶的應用場景。

🎯 長上下文agent的KV cache困境，這是一條可評估的替代路線

如果你的應用場景是長上下文agent或需要持續對話記憶，但又被KV快取的記憶體成長壓得喘不過氣，Laplace 3B展示的固定大小遞迴狀態加原生PyTorch搬上Trainium2的路線值得納入評估清單；但在導入前，務必先驗證線性注意力的檢索能力是否滿足實際任務需求，而不是只看吞吐量數字。

🔗 來源
- 標題：Beyond the KV cache: Training and serving i14's Laplace 3B linear attention model on AWS Trainium2 with native PyTorch
- 作者／機構：Kevin Shabahang（AWS ML）
- 連結：https://aws.amazon.com/blogs/machine-learning/beyond-the-kv-cache-training-and-serving-i14s-laplace-3b-linear-attention-model-on-aws-trainium2-with-native-pytorch/

#LinearAttention #GLA #AWSTrainium2 #PyTorch #LLM #KVCache #ModelArchitecture #MuonOptimizer #FSDP #AIInfrastructure
