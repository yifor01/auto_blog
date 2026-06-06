---
title: 'Five labs, five minds: building a multi-model finance drama on small models'
source: HuggingFace Blog
url: https://huggingface.co/blog/build-small-hackathon/thousand-token-wood-sim-v2
score: 98
model: google/gemma-4-31b-it:free
generated_at: '2026-06-06T19:55:12.463641'
---

📌 【HuggingFace 技術分享】用 4 家不同實驗室的小模型，打造一個會「內鬥」的金融模擬社會

如果一個 AI 模擬社會的所有 Agent 都使用同一個模型，那這只是在跟一個人的不同分身對話。真正的市場動態，來自於參與者之間「認知」的差異。

當我們把 OpenAI、NVIDIA、OpenBMB 和 Qwen 的小模型全部塞進同一個生態系，會發生什麼事？

🤔 **同質化模型是模擬的敵人，異構性才是產品核心**

在第一版 Thousand Token Wood 中，所有森林生物都跑在同一個微調過的 0.5B 模型上。雖然能觀察到經濟泡沫與崩潰，但那更像是一個「觀察箱」而非真正的遊戲。

作者在 v2 版本中提出了一個核心洞察：一個有趣的市場，必須讓參與者「真正地不同」。如果所有 Agent 的思考邏輯一致，對話會變成劇本；但如果他們來自不同實驗室、使用不同訓練數據與後訓練（post-training）策略，他們對風險的感知、囤貨的習慣以及投機的邏輯將截然不同。

🧪 **將 4 家實驗室的小模型部署在單一平台**

為了實現這種「認知差異」，v2 版本不再使用「單一模型 + 多個 Prompt」的傳統做法，而是直接部署了四個不同的模型：
- **gpt-oss-20b** (OpenAI)
- **MiniCPM3-4B** (OpenBMB)
- **Nemotron-Mini-4B** (NVIDIA)
- **Qwen 0.5B** (作者自行微調版本)

這種設計讓森林裡的「貓頭鷹」囤貨方式與「狐狸」投機方式完全不同，讓 Agent 之間的議會討論變成一場真實的爭論，而非預設的腳本。

💡 **工程痛點不在於模型，而是在於服務層 (Serving Layer)**

這次實驗揭示了一個對 AI 工程師至關重要的實務經驗：在單一平台上運行多個異構模型，最大的摩擦力幾乎全部來自於「服務層」，而非模型本身。

作者在部署過程中發現，目前的 vLLM (0.22.1) 在加載時會進行內核的 JIT 編譯，這要求環境中必須安裝 CUDA toolkit (nvcc)。然而，許多精簡的基礎鏡像 (lean base image) 並未包含這些工具，這導致在部署多模型環境時，環境配置成了最主要的技術阻礙。

⚠️ **目前仍處於工程實作階段，複雜度隨模型數增加**

雖然異構模型帶來了豐富的行為多樣性，但這也意味著維護成本增加。每個模型需要不同的資源管理與服務配置，且在單一平台上同時運行多個不同架構的模型，對底層環境的依賴管理要求極高。

🎯 **構建 Multi-Agent 系統：嘗試引入「認知異構性」**

對於想要開發多代理系統 (Multi-Agent Systems) 的開發者，這篇報告提供了一個新視角：
- **不要只依賴 Prompt 工程**：若要創造真實的衝突與協作，嘗試混合不同實驗室的小模型。
- **關注 Serving 層的依賴**：在部署 vLLM 等推理框架時，務必確認基礎鏡像是否包含 CUDA toolkit 等編譯工具，以避免 JIT 編譯失敗。
- **小模型也能創造複雜行為**：即便模型參數規模小，只要數據分佈不同，就能產生足以支撐金融模擬的行為差異。

🔗 **文章連結**
📝 Five labs, five minds: building a multi-model finance drama on small models
👤 Lester Leong & AdmiralTaco
🔗 閱讀全文：https://huggingface.co/blog/build-small-hackathon/thousand-token-wood-sim-v2

如果你在構建 Multi-Agent 系統，你會選擇單一強大模型，還是多個異構小模型？歡迎在下方討論 👇

#AI #MultiAgent #LLM #vLLM #HuggingFace #SmallModels #AI工程
