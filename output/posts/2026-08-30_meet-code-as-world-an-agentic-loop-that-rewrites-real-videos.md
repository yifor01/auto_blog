---
title: 'Meet ‘Code-as-World’: An Agentic Loop That Rewrites Real Videos Into Executable
  MuJoCo Physics Programs'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/29/mirros-code-as-world-executable-world-representations/
model: claude-code/sonnet
generated_at: '2026-08-30T10:53:35.594366'
score: 113
---

📌 MirroS Code-as-World：讓影片變成可執行的物理程式

TL;DR：用代理迴圈把真實影片重建成可驗證、可編輯的 MuJoCo 物理程式，而非停留在像素預測。

影片生成模型能畫出下一幀逼真的畫面，卻從來不知道畫面裡的箱子有多重、會不會被撞飛、受不受重力影響——因為它學到的是像素分佈，不是物理法則。

🤔 像素只是證據，不是本體

MirroS 提出的論點很直接：像素是物理場景存在的證據，不是場景的本體(ontology)。影片模型可以預測出合理的畫面，卻從未表徵質量、接觸、重力這些東西。影片模型、3D 重建、字幕描述各自能還原場景的一部分，但沒有一種方法能還原場景背後真正的運作機制。Code-as-World 因此選擇用可執行程式碼取代像素、latent 或字幕，作為場景的表示方式——一份 MuJoCo 可以直接執行、Agent 可以拿去對照原始影片驗證、任何人都能編輯再重新模擬的 scene.json。

🧩 用「假設—驗證」迴圈從影片反推物理程式

MirroS 把場景定義為 Executable World Representation（EWR），一個三元組 p = (C, E, A)，在目前釋出的實作中會被編譯成一份 scene.json，交給 MuJoCo 執行，並提供兩套可互換的引擎：動畫引擎（處理運動姿態）與物理引擎（處理力與接觸）。

從影片反推 EWR 是一個反問題，MirroS 把它當成溯因搜尋（abductive search）來處理：一個 Agent 反覆執行 propose → instantiate → execute → render → verify，最多跑 5 輪。輸入端由 SAM 3 提供物件遮罩與影像平面軌跡、VGGT-Omega 估計深度與相機幾何、SAM 3D 生成每個物件的網格。候選的模擬結果會被投影回原始視角，在關鍵幀上比對 RGB、深度、遮罩與軌跡，逐幀的落差彙整成結構化回饋 Δ，指導下一輪修正；如果到預算用盡仍未通過驗證，這個假設就被拒絕。在相同的五次評估預算下，這套迴圈在 Visual Alignment、Object IoU、Traj-ADE、Accuracy@2%D 上都贏過 Best-of-5 的獨立取樣，換成物理引擎重跑一次結果依然成立。

📊 9B 模型打贏 Gemini 3.1 Flash，關鍵在世界空間監督

訓練資料先用動作篩選過的 WISA-80K 影片，再用 Wan2.2-VACE 加上內部影片模型做 sim-to-real 重新渲染。訓練分兩階段：第一階段是監督式微調，用 RefCOCO/+/g、RefCLEF、GOT-10K 建構出的 73,335 筆影像空間 QA，涵蓋像素座標中的範圍、位置、位移、速度、加速度；第二階段用 GRPO 在 1,585 筆文字驅動與 988 筆影片驅動的可執行世界上做世界空間 VQA 強化學習，獎勵訊號結合尺度標準化的數值準確度、單位與格式正確性，訓練用了 8 張 NVIDIA H100。

在 QuantiPhy-validation（159 題，跨 2S/2D/3S/3D 取 MRA 巨集平均）上，4B 模型拿到 50.6 分，9B 模型 55.4 分，一個 27B 的推理版本拿到 58.6 分；對照組 Gemini-3.1 Flash 是 54.8 分，ChatGPT-5.1 是 48.4 分，最強的開權重基準 Qwen3-VL-32B-Instruct 只有 40.2 分。消融實驗更能說明問題：只用影像空間 QA 訓練，4B/9B 分別只有 44.2/50.9 分，加入世界空間監督後才拉到 50.6/55.4。連原本沒特別針對的像素級定位任務也跟著進步，9B 模型在 RefCOCO 上從 63.7 分提升到 68.3 分，在 GOT-10K 上從 20.1 分提升到 26.6 分。

💡 世界空間監督帶來的是真實影片給不了的精確標籤

這個消融結果的意義在於：影像空間 QA 只能教模型讀懂像素座標，而可執行世界表示能提供真實影片本身沒有的精確物理標籤（質量、速度、加速度的真值），這種監督訊號連帶把模型在純像素定位任務上的表現一起拉高，說明「理解機制」和「理解像素」並不是互斥的兩件事。

🎯 已開源兩個 checkpoint，可直接接進 vLLM 服務

MirroS 以 Apache 2.0 釋出 GitHub 原始碼與兩個 checkpoint——Code-as-World-VL-4B 與 Code-as-World-VL-9B，分別從 Qwen3.5-4B、Qwen3.5-9B 微調而來，皆為 BF16 safetensors，可用 vLLM 起一個相容 OpenAI 格式的 /v1 端點服務，每支影片取樣 16 幀、--max-model-len 設為 4608。對做具身智能、機器人模擬或需要精確物理標籤訓練資料的團隊，這套流程提供了一個把任意影片轉成可編輯、可重新模擬場景的現成起點。

🔗 來源
- 標題：Meet 'Code-as-World': An Agentic Loop That Rewrites Real Videos Into Executable MuJoCo Physics Programs
- 作者／機構：Michal Sutter，MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/29/mirros-code-as-world-executable-world-representations/

#WorldModels #MuJoCo #PhysicsSimulation #VideoUnderstanding #EmbodiedAI #OpenSource #VLM #Robotics #ComputerVision #AgenticAI
