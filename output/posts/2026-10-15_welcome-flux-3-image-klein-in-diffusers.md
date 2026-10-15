---
title: Welcome FLUX.3 Image Klein in Diffusers
source: HuggingFace Blog
url: https://huggingface.co/blog/flux-3
model: claude-code/sonnet
generated_at: '2026-10-15T20:30:53.900233'
score: 111
---

📌 FLUX.3 Image Klein 開源發布，Diffusers 當天就能跑

TL;DR：Black Forest Labs 開源新一代影像模型 FLUX.3 Image Klein，一個模型同時處理文生圖、多參考圖編輯與版面控制，程式碼、量化權重與 LoRA 訓練腳本一次到位。

多數開源影像模型發布時只丟出一份模型權重，剩下的自己摸索。這次 Black Forest Labs 連「用 bounding box 指定物件要畫在哪裡」的 prompt 語法都寫進了官方文件，而且 Hugging Face 的 Diffusers 團隊在發布當天就把它接進 `ModularPipeline`，複製貼上就能跑。

🤔 **一個模型，三種任務**

FLUX.3 Image Klein 把文字生圖（text-to-image）、多張參考圖的圖生圖（multi-reference image-to-image），以及這次新加入的「版面控制」（layout control）整合進同一個模型。版面控制讓你在 prompt 裡寫入 JSON 格式的區域列表，指定畫面中每個部分要出現在哪個位置，或是指定參考圖裡的某個元素該移動到新畫面的哪裡。

官方開放的兩個 checkpoint 列在 FLUX.3 Image Klein collection 中：

| Checkpoint | 說明 | 預設設定 |
|---|---|---|
| `black-forest-labs/flux-3-image-klein` | 時間步蒸餾（time step distilled）版本，推論快 | 16 步，不使用 CFG |
| `black-forest-labs/flux-3-image-klein-base` | 基礎模型 | 50 步，使用 CFG |

🧩 **怎麼用：從安裝到版面控制**

安裝最新版 `diffusers` 與 `transformers`（因為文字編碼器用的是 Qwen3-VL），接著載入蒸餾版 checkpoint：

```python
import torch
from diffusers import ModularPipeline

pipe = ModularPipeline.from_pretrained("black-forest-labs/flux-3-image-klein")
pipe.load_components(dtype=torch.bfloat16)
pipe.to("cuda")

pipe(prompt="a red fox", output="images")[0].save("fox.png")
```

文生圖時，官方提示指南建議把主體、場景、光線、構圖與風格都寫進完整的場景描述裡，效果會比短句子更好。蒸餾版預設 16 步產生 1024×1024 影像，可透過 `height`、`width`、`num_inference_steps` 調整。

圖生圖則是把參考圖傳入 `image` 參數，prompt 寫成「你想要的結果圖的描述」，並包含要做的改動。若傳入多張參考圖，可在 prompt 中用 `<ref_image_0>`、`<ref_image_1>` 依序指稱它們，例如把一張狐狸的圖和一張木椅的圖合成「狐狸坐在木椅上」的新畫面。

版面控制則是在 caption 後面接一段 JSON 區域列表，每個區域有 `id`、`bbox`（格式為 `[y_min, x_min, y_max, x_max]`，y 在前，採 0 到 1000 的正規化座標）與 `desc`，caption 裡用 `<id>` 指稱該區域。因為座標是正規化的，同一組 bbox 在任何輸出尺寸下都通用。如果是編輯既有參考圖，每個區域還要多給 `src_bbox`（來源位置）與 `tgt_bbox`（目標位置），兩者相同就代表該元素原地不動，不同則代表要把它搬過去，其餘區域維持原狀。

📊 **跑起來多快、多重**

蒸餾版 checkpoint 在 H100 上產生一張 1024×1024 影像約需 2 秒。對於記憶體較小的 GPU，官方也提供 NVFP4 與 FP8 量化權重，可透過 `from_single_file` 直接載入。基礎模型則需要 50 步並搭配 CFG，速度較慢，但它才是用來做 LoRA 微調的對象。

⚠️ **微調與部署的限制**

要做 LoRA 微調，官方建議使用基礎模型而非蒸餾版；蒸餾版本身已經針對快速推論做過最佳化，直接拿去微調不是官方建議的路徑。此外，完整的多參考圖與版面控制功能仍仰賴正確撰寫 JSON 區域描述，格式稍有出錯就可能影響生成結果。

🎯 **實務啟示**

對工程師來說，這次發布的價值不只是模型本身，而是「Modular Diffusers pipeline」這個設計：可以把管線裡的區塊拆開或替換成自訂模組。再加上官方同步給出 LoRA 訓練腳本與量化權重，想要在特定風格或任務上做客製化、或是把模型塞進較小的 GPU，都有現成的路徑可以直接試，不用自己從零拼湊推論與訓練流程。

🔗 **來源**
- 標題：Welcome FLUX.3 Image Klein in Diffusers
- 作者／機構：Hugging Face（Black Forest Labs 模型）
- 連結：https://huggingface.co/blog/flux-3

#FLUX3 #BlackForestLabs #Diffusers #ImageGeneration #OpenSource #LoRA #TextToImage #ImageToImage #HuggingFace #GenerativeAI
