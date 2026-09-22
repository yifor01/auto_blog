---
title: Right-size generative AI endpoints with concurrency sweeps on Amazon SageMaker
  AI
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/right-size-generative-ai-endpoints-with-concurrency-sweeps-on-amazon-sagemaker-ai/
model: claude-code/sonnet
generated_at: '2026-09-22T20:33:41.546316'
score: 85
---

📌 併發掃描一次掃出，GPU端點該租幾臺

TL;DR：SageMaker內建併發掃描，自動找出推理端點的最佳實例與併發規格。

多租一臺ml.g7e.2xlarge，就是白燒一顆閒置GPU的錢；租少一臺，請求開始排隊，延遲飆高，使用者體驗直接崩壞。過去要抓對這個平衡點，只能手動部署、手動壓測、手動調整，一輪一輪試到數字看起來還行為止。

🤔 右調規格的老問題

生成式AI端點的容量規劃向來是個反覆試錯的過程：沒有系統化方法時，團隊只能靠「部署→壓測→調整→再部署」的循環摸索，既耗時間也耗預算。Amazon SageMaker AI Inference Recommendations內建的併發掃描（concurrency sweep），要把這個過程變成一套可重複執行的自動化基準測試。

🧩 四步驟工作流程

併發掃描的做法，是對SageMaker AI端點送出受控且遞增的併發流量，並在每個併發等級量測吞吐量與延遲，藉此描繪出端點的效能曲線。整套流程分四步：

1. **部署模型**：文章以NVIDIA Nemotron-3 Nano 30B（Mixture-of-Experts架構，僅3B個啟用參數）為例，部署到搭載NVIDIA Blackwell GPU的ml.g7e.2xlarge實例，使用SageMaker AI的vLLM Deep Learning Container，透過`SM_VLLM_*`環境變數設定。其中`SM_VLLM_ENFORCE_EAGER`是必要設定，因為Nemotron-3 Nano採用Mamba-Transformer混合架構，需要eager執行模式；GPU記憶體使用率設為0.85，為高併發下的KV cache成長預留空間；並開啟prefix caching，讓重複出現的system prompt能重複使用快取的key-value配對。
2. **定義工作負載設定檔**：透過`CreateAIWorkloadConfig`定義要模擬的流量型態，範例採用1,024個輸入token、256個輸出token，代表典型的RAG（檢索增強生成）或摘要類工作負載；若應用場景是短prompt、長輸出（例如程式碼生成），則需相應調整。設定同時開啟streaming，以量測time to first token（TTFT）。
3. **啟動掃描**：透過`CreateAIBenchmarkJob` API發起基準測試工作，由基準測試引擎AIPerf在單一工作內依序執行各個併發等級（例如64、256、1,024），並在每個等級送出設定的請求總數。依序而非平行執行各等級，能確保每次量測反映的是乾淨、獨立的負載狀態，同時控制測試成本。
4. **分析結果**：工作完成後，結果會以JSON格式的每等級指標寫入指定的Amazon S3路徑，供下載分析。

📊 飽和點在哪裡：256併發是分水嶺

把吞吐量對延遲畫成曲線，飽和點會呈現一個明顯的「拐點」：吞吐量趨於平緩，而p99延遲則急遽上揚。在文章的測試情境中，這個拐點出現在256個併發請求：拐點以下是安全操作區間，超過拐點，端點已經過載，使用者會開始等待。

如果不想手動挑選要測試的併發等級，可以改用`max-concurrency-under-sla`搜尋方案，直接指定一項或多項SLA門檻，讓最佳化規劃器自動搜尋滿足所有門檻的最高併發數。範例中，規劃器從併發16開始逐輪倍增，在併發512時首次觸發SLA違規（p99端到端延遲超標或請求失敗），接著把搜尋範圍縮小到256至512之間，最終找到併發320能在滿足p99端到端延遲低於50秒的同時，達到每秒2,782個token的吞吐量。而當同時對端到端延遲與TTFT設下SLA門檻時，該情境下端點能支撐的最高併發數則降為80。

💡 用最佳化規劃器省下反覆試探的成本

比起固定併發清單的線性掃描，搜尋方案的規劃器會從較寬的範圍開始，逐步收斂，只評估找出邊界所需的併發等級，因此能用更少的迭代次數與更低的測試成本逼近答案，迭代次數上限則由`search_max_iterations`控制。

🎯 實務啟示

併發掃描把容量規劃從「憑感覺調整」變成「看資料決策」：先用單一SLA門檻（例如p99延遲）找出基準，再視場景疊加TTFT等互動體驗指標，往往會發現實際可承受的併發數比單一指標算出來的更保守。另外別忘了，SageMaker端點是按小時計費，不論有沒有流量進來，測試完務必刪除端點、端點設定與模型，避免持續產生費用。

🔗 來源
- 標題：Right-size generative AI endpoints with concurrency sweeps on Amazon SageMaker AI
- 作者／機構：Mona Mona，AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/right-size-generative-ai-endpoints-with-concurrency-sweeps-on-amazon-sagemaker-ai/

#AWS #SageMaker #LLMInference #vLLM #MoE #NemotronNano #MLOps #CapacityPlanning #GenerativeAI #Blackwell
