---
title: Rebuilding AUTOMATIC1111 with Gradio Workflow
source: HuggingFace Blog
url: https://huggingface.co/blog/gradio-workflow-1111
model: claude-code/sonnet
generated_at: '2026-09-10T20:05:31.492102'
score: 90
---

📌 73 個節點、11 條媒體管線：Gradio 畫布重建 AUTOMATIC1111

TL;DR：HuggingFace 用 gr.Workflow 節點式畫布重現了 AUTOMATIC1111 幾乎全部功能，每個輸出節點還會自動變成 REST API。

熟悉 stable-diffusion-webui 的人都知道，AUTOMATIC1111（A1111）的功能繁雜到令人卻步：txt2img、img2img、hi-res fix、ControlNet 標註器、Extras 放大、PNG 資訊回讀⋯⋯要在一張畫布上重現這些功能，得拆解成多少個零件？HuggingFace 團隊給出的答案是：73 個節點、11 條管線。

🧩 四種算子，拼出十一條管線

Workflow1111 建立在四種固定的算子（operator）之上：fn（一般 Python 函式）、model（透過 InferenceClient 呼叫的模型）、space（呼叫另一個 Hugging Face Space）、dataset（讀取 Hub 資料集的一列資料）。每個節點包一個算子，算子的輸入輸出就是畫布上可連接的埠。

以核心的文字轉圖片管線為例：prompt 先經過一個 fn 節點（prompt-builder）附加風格預設並清理文字，再進入呼叫 checkpoint 的 model 節點生成圖片，最後由一個 post-process fn 節點把生成參數寫進 PNG 的 metadata，供之後的 PNG Info 管線讀回。

其他管線也各有巧思：
- Hi-res fix 與 img2img 共用同一個 FLUX.1-Kontext 節點，前者下達「加強細節、保持構圖不變」的指令，後者則直接依使用者描述做編輯。
- 用 LLM 寫 prompt：把「A lighthouse in a storm」丟給 Qwen3-4B，一個 fn 節點把回覆整理成最多 40 個標籤，再接上任意 diffusion 模型節點成像。文章特別點出，這裡沒有像 ComfyUI 那樣的自訂節點，LLM 和 diffusion 模型在 gr.Workflow 上就是同層級的兩個 model 算子。
- VLM interrogate：Qwen2.5-VL 看夜市照片寫出還原用的 prompt，同時一個 ViT 分類器讀同一張圖給出標籤（如 restaurant 51.9%、tobacco shop 15.6%）。兩個節點吃同一張圖，gr.Workflow 會自動平行執行，耗時約等於跑一次。
- 偵測轉 inpaint 遮罩：DETR 偵測街景中的物件（三人、一狗、一自行車、一汽車），再分岔成兩條分支，一條用 Pillow／NumPy 在本機畫出偵測框，一條在本機產生遮罩，只有偵測呼叫本身離開機器。
- Prompt matrix：基礎 prompt「a lone oak tree」與四個後綴（日出、雷雨、銀河下、秋霧）組合，各自送進獨立的文字轉圖片節點。由於 gr.Workflow 沒有迴圈算子，四個節點只能並排放在畫布上，但正因為深度相同，它們會同時平行生成。
- Extras 對應的放大與去背：Lanczos 重採樣是純本機 fn 節點，不需網路；AuraSR ×4 放大與 BRIA RMBG-2.0 去背則是呼叫 Hub 上另一個 Space 的 space 節點。
- ControlNet 風格標註器（Canny、line art、sketch、luma-depth、posterize）全部是純 NumPy 寫成的 fn 節點，在 CPU 上對一張建築外牆範例圖約各耗時半秒。
- Image-to-video：PNG Info 讀取的同一張圖也會餵給 Wan 2.2 I2V A14B 節點生成動畫，示範案例是一隻沉睡狐狸甦醒動起來；因為一個參考節點可以同時餵給多條下游管線，所以只需一次上傳。

📊 三分之二的畫布離線也能跑

文章統計，畫布上共有 36 個算子節點，其中 32 個是 fn 節點，22 個完全在本機執行、不發出任何網路呼叫，這代表整個應用有約三分之二的部分在斷網時仍可運作。由於這些節點就是普通的 Python 函式，也能脫離畫布、伺服器與 GPU 直接單獨測試。

💡 用自己的 GPU 跑，甚至自動變成 API

目前為止所有模型呼叫都送到別人的硬體上（透過 Inference Providers 或 Space），這也是為什麼不需要自備 GPU 就能建置這類畫布。但 fn 節點本質就是 Python，同樣可以載入本地模型、跑在自己的 GPU 上。文中舉的例子是 FastVideo/fastvideo-fasth3-preview，它跑的是 MiniMax-H3 的四步蒸餾版本 FastH3，透過 ZeroGPU 生成帶配樂的影片，核心只是一個綁定函式：

```python
@spaces.GPU(duration=get_duration, size=GPU_SIZE)
def _generate(prompt_embeds, text_token_tags, height, width, num_frames, seed):
    ...

gr.Workflow(bind={"generate": generate, "status": status}).launch()
```

ZeroGPU 負責在函式需要時配置 GPU、用完釋放，gr.Workflow 本身完全不需要知道這件事。這個模式也不限於 Spaces：把 bind= 指向載入本地 checkpoint 的函式，在自己的機器上執行 .launch()，Workflow1111 的畫布就能驅動自家 GPU。此外，畫布上每個輸出節點都會自動變成一個 REST API 端點，不需要額外手寫路由。

🎯 實務啟示

想快速拼裝一套涵蓋文生圖、圖生圖、放大、去背、影片生成的完整 pipeline，Workflow1111 提供了一個現成的節點式範本；更重要的是它示範了 fn／model／space／dataset 四種算子如何混搭，讓 LLM 寫 prompt、VLM 讀圖、diffusion 模型出圖可以在同一張畫布上並行運作，並且每個節點都能單獨測試、單獨換成自己的模型或 GPU。對已經在用 ComfyUI 之類節點式工具的團隊來說，這是一個值得比較的替代架構。

🔗 來源
- 標題：Rebuilding AUTOMATIC1111 with Gradio Workflow
- 作者／機構：Yuvraj Sharma、Abubakar Abid（Hugging Face）
- 連結：https://huggingface.co/blog/gradio-workflow-1111

#Gradio #HuggingFace #StableDiffusion #AUTOMATIC1111 #AIWorkflow #OpenSource #ZeroGPU #DiffusionModels #MLOps #GenerativeAI
