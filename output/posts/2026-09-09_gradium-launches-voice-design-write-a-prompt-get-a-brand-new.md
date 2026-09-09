---
title: 'Gradium Launches Voice Design: Write a Prompt, Get a Brand New Synthetic Voice
  in Seconds'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/09/gradium-launches-voice-design-write-a-prompt-get-a-brand-new-synthetic-voice-in-seconds/
model: claude-code/sonnet
generated_at: '2026-09-09T20:09:09.860940'
score: 78
---

📌 TorchServe 停止維護，AWS 推出 Ray Serve DLC 補位

TL;DR：TorchServe 官方公告不再更新，AWS 用 Ray Serve Deep Learning Container 接手推論部署，省下自組 GPU 環境的苦工。

如果你的推論服務還跑在 TorchServe 上，現在該注意了：官方公告明確寫著「沒有規劃中的更新、沒有 bug 修復、沒有新功能、沒有安全性修補」，甚至連已知漏洞都可能不會處理。對還在用它的團隊來說，這代表兩件事同時發生：安全性修補停止，與新版 PyTorch、CUDA 的相容性更新也停止。剩下的工作全部落到工程師頭上，自己挑選 GPU stack 各層的相容版本、自己修每一層的漏洞、自己 debug 元件版本漂移造成的詭異錯誤。這些都是不會替產品加分、卻會拖慢模型上線速度的「無差異化工作」。

🤔 **停維護留下的坑，誰來填？**

AWS Deep Learning Containers（DLC）這套思路早就用在訓練工作負載上：把框架、依賴套件、GPU stack 打包成一個經過測試、修補過的 Docker 映像檔，拉下來就能用。這次隨著 Ray Serve DLC 推出，同樣的做法延伸到推論端。你拿到的是一個為「模型上線變成 HTTP endpoint」量身打造的容器，由 AWS 維護與測試，整套推論 stack 已經組好。

🧩 **容器裡裝了什麼，換掉 TorchServe 要改哪裡**

Ray Serve DLC 的 CPU 版本建構在 Amazon Linux 2023 基礎映像檔上；GPU 版本則建構在官方 NVIDIA Amazon Linux 2023 映像檔上，包含 OS 層與 CUDA runtime。在這個基礎之上疊加 PyTorch、搭配 FastAPI 與 Uvicorn 的 Ray Serve 服務層，以及涵蓋 vision、audio、多模態工作負載的常用工具，包括為影片前處理編譯了 NVIDIA 硬體加速的 FFmpeg。所有元件都在每次發版前一起驗證測試過，因此 CUDA runtime、框架與服務層之間不會有版本漂移，安全性修補在建構時就已套用。這個 DLC 分別發布給 Amazon EKS／EC2 與 Amazon SageMaker 兩種環境，各自搭配對應的 entrypoint，但共用同一套底層 stack。

因為 DLC 已經內建常見的推論 stack，像 Qwen3-VL 這類模型不需要客製映像檔就能跑；需要額外函式庫的模型，也可以在同一個經測試的基礎上疊加。

從 TorchServe 遷移過來，最大的改變是服務端點的寫法。在 Ray Serve 裡，一個模型端點就是一個用 `@serve.deployment` 裝飾的 Python class，實作 `__call__` 處理 HTTP 請求，呼叫 `.bind()` 註冊即可，不需要 model archiver、不需要 handler class 繼承體系、也不需要 config.properties 設定檔。文章示範用 GPU 版 Ray Serve DLC 部署 Qwen3-VL-2B 這個 vision-language 模型，服務程式碼透過 ConfigMap 注入容器，換程式碼不必重建映像檔。範例中 `@serve.deployment` 搭配 `ray_actor_options={"num_gpus": 1}` 告訴 Ray 把這個部署排程到有一張可用 GPU 的 worker 上，模型以 float16 載入，以符合 A10G GPU 24GB VRAM 的容量限制。

🎯 **單節點先跑起來，多節點再談 KubeRay**

文中的部署架構是單一 g5.xlarge 執行個體（一張 NVIDIA A10G GPU、24GB VRAM），單節點設定：一個 pod、一張 GPU、一臺機器，透過 8000 port 對外提供 HTTP 服務。如果之後需要跨機器的模型平行化，或是多副本的水平擴展，可以在這個基礎上用 KubeRay 來調度跨節點的 Ray worker。

對現在還在用 TorchServe 的團隊來說，這是一條務實的遷移路徑：不用再自己維護 CUDA 相容性，升級版本變成換個映像檔標籤，安全性修補則交給 AWS 定期處理。省下的自組 Dockerfile、寫 handler boilerplate 的時間，可以拿去處理真正影響產品的模型邏輯。

🔗 **來源**
- 標題：Simplify and support your TorchServe workloads using Ray Serve Deep Learning Containers
- 作者／機構：Ananth Raghavendra, AWS ML Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/simplify-and-support-your-torchserve-workloads-using-ray-serve-deep-learning-containers/

#TorchServe #RayServe #AWS #DeepLearningContainers #MLOps #ModelServing #Kubernetes #EKS #PyTorch #Inference
