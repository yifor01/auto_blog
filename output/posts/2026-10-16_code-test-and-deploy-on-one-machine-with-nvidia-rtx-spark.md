---
title: Code, Test, and Deploy on One Machine with NVIDIA RTX Spark
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/code-test-and-deploy-on-one-machine-with-nvidia-rtx-spark/
model: claude-code/sonnet
generated_at: '2026-10-16T20:15:08.413097'
score: 74
---

📌 NVIDIA RTX Spark：寫程式、測試、部署三合一主機

TL;DR：NVIDIA RTX Spark主打用一臺GB10晶片主機完成本地agent開發、測試與部署，官方宣稱coding agent效能是Intel Panther Lake的4.6倍。

過去開發者寫程式碼，現在開發者指揮AI agent寫程式碼。但這個轉變也讓工作流變得破碎：筆電寫程式、雲端模型API做推論、雲端VM做部署，三個環境各自獨立。NVIDIA RTX Spark想解決的，正是這種「一份工作、三個地方」的割裂狀態。

🤔 **從CPU-bound到GPU-bound的開發工作**

文章指出，開發工作的性質已經從過去由CPU決定效能的工作，變成由GPU決定效能的工作：今天的AI開發者需要跑推論來驅動coding agent並測試應用，需要做fine-tuning與訓練，也還有少量編譯需求。RTX Spark搭載NVIDIA Grace CPU與Blackwell GPU，希望同時涵蓋推論、fine-tuning與編譯所需的運算力。

🧩 **GB10晶片、128GB統一記憶體，一臺打通本地與雲端**

RTX Spark的核心是NVIDIA GB10系統單晶片，搭配最高128GB統一記憶體與1 petaflop的FP4 AI運算能力。開發者可以用Windows（包含與微軟共同開發的Windows Developer Config，會安裝主流開發框架、靜音通知、強化終端機、並能把工作列移到側邊），也可以用Windows Subsystem for Linux，取得與雲端部署環境相同的依賴與設定，不需要跨環境搬移程式碼。由於機身內建NVIDIA GPU，開發者可以直接測試並部署到官方所稱的1.5億臺RTX PC安裝基礎，以及幾乎所有採用NVIDIA GPU的雲端平臺。

官方公布的效能比較（以Intel Core Ultra X9 388H／Panther Lake 12Xe為基準1.0）顯示：coding agent效能為4.6倍、fine-tuning效能為2.7倍、程式碼編譯效能為1.8倍，測試分別使用AA-AgentPerf-local搭配Qwen3.8-27B、Unsloth LoRA搭配Llama-3.1-8B，以及Phoronix Test Suite的Linux kernel編譯。

在軟體生態方面，NVIDIA與微軟合作推進Windows on Arm開發者生態，隨RTX Spark釋出的新工具包括首個PyTorch-CUDA build、預設原生支援的Python 3.15版本、超過2,000個可直接使用的Conda套件，以及前15,000大Python套件中97%以上提供Arm相容版本。

📊 **本地coding agent生態與新款Nemotron模型**

NVIDIA與GitHub Copilot、Pi、Hermes、OpenClaw等主流coding agent合作，重點改進包括：以最佳化recipe無縫部署本地模型、透過NVIDIA OpenShell與／或Microsoft Execution Containers提供OS層級沙盒強化安全性，以及在本地與雲端模型之間做混合式prompt路由，讓prompt在本地模型已經足夠時留在本地，必要時才升級到雲端，藉此降低token消耗。

具體而言，GitHub Copilot透過Windows ML搭配llama.cpp後端支援無縫本地AI，其prompt路由器HydraFusion升級後也支援本地模型，新款MAI 1.1 Coding Flash模型可在RTX Spark上本地執行；開源coding agent Pi則透過擴充功能、skills與prompt模板讓開發者掌控模型選擇與可用工具；JetBrains也推出Junie Local的原生支援，模型與程式碼都留在本機，其context window大小會依GPU可用記憶體自動調整，因此RTX Spark的統一記憶體能讓它保留更多程式碼、工具輸出與對話紀錄。

此外，NVIDIA推出專為RTX Spark本地agent設計的新模型Nemotron 3.5 Bolt 74B-A9B 24GB：74B參數、9B啟用參數的MoE模型，透過2-bit量化與進階quantization-aware training技術壓縮進24GB記憶體，目標是在速度與智慧程度之間取得平衡，號稱比多數主流dense模型更快、比記憶體相當的主流MoE模型更聰明。該模型可透過llama.cpp、vLLM、Ollama、Unsloth、LM Studio運行，也能直接透過Hermes、OpenClaw等agent存取，並和其他Nemotron模型一樣完全開源（含訓練資料、權重與recipe）。文章也提到decision model這類新技術，宣稱能讓agent跳過冗長推理迴圈、最快200倍速度做出下一步決策，目前llama.cpp與Unsloth已在RTX Spark與GeForce RTX GPU上支援。另外，NVIDIA AI for Media SDK也已上架RTX Spark，提供影片超解析度、幀生成與TrueHDR功能的Python wheel（PyPI）與C++ SDK（NGC）。

💡 **一臺主機想打通的，其實是工作流的割裂**

這篇文章的重點與其說是單一技術突破，不如說是一次生態系整合：把GPU運算、本地coding agent、量化模型與Windows on Arm套件生態湊在一起，讓開發者少做「筆電寫、雲端跑、VM部署」之間的環境搬遷。它的說服力建立在NVIDIA自己公布的效能比較基準上，實際表現仍需個別開發者在自己的工作負載上驗證。

🎯 **實務啟示**

如果團隊的痛點正是本地開發環境與雲端部署環境不一致、或是coding agent的雲端token費用偏高，RTX Spark提供的「本地跑模型、必要時才升級雲端」路由機制值得關注；但導入前應留意這仍是全新的Windows on Arm生態，既有應用需先評估Arm64相容性，再決定走原生build還是Arm64EC漸進遷移。

🔗 **來源**
- 標題：Code, Test, and Deploy on One Machine with NVIDIA RTX Spark
- 作者／機構：Elizabeth Goodman
- 連結：https://developer.nvidia.com/blog/code-test-and-deploy-on-one-machine-with-nvidia-rtx-spark/

#NVIDIA #RTXSpark #GB10 #LocalAI #CodingAgent #Nemotron #WindowsOnArm #EdgeAI #MixtureOfExperts #AIDevTools
