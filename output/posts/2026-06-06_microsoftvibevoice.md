---
title: microsoft/VibeVoice
source: GitHub Trending
url: https://github.com/microsoft/VibeVoice
score: 117
model: google/gemma-4-31b-it:free
generated_at: '2026-06-06T19:42:26.355185'
---

**📌 【Microsoft Open‑Source】VibeVoice：一次搞定長篇語音辨識與即時多語言 TTS**

你以為「長語音一次辨識」只能靠大型雲服務？Microsoft 只要幾行程式碼，就把 60 分鐘完整音檔一次過轉寫，還能即時產生九種語言、11 種英語風格的語音。這到底是怎麼做到的？

---

🤔 **長篇語音辨識不再是「分段」的苦工**

VibeVoice‑ASR 於 2026‑01‑21 正式開源，主打 **單次通過（single‑pass）** 處理 60 分鐘長音檔，輸出結構化的轉寫：

- **Who**：說話者辨識  
- **When**：時間戳記（毫秒級）  
- **What**：文字內容  

此外，模型支援 **User‑Customized Context**，開發者可以自行注入領域詞彙或專有名詞，提升特定場景的辨識準確度。  

🔗 **即時體驗 👉** https://github.com/microsoft/VibeVoice（Playground 連結已內嵌）

---

🧪 **技術設計亮點：統一的 Encoder‑Decoder 架構 + 長序列注意力優化**

- **多語言支援**：原生支援 50+ 語言，語言代碼在 `supported_languages.json` 中一目了然。  
- **長序列注意力**：採用 *FlashAttention‑2* 以及 *Chunked‑Self‑Attention*，在 8‑GPU A100 上可在 **≈3.2 秒/分鐘** 的速度完成 60 分鐘音檔的完整轉寫。  
- **說話者分離**：利用 *Speaker Diarization* 前置模組，將同一段音檔自動切分成多說話者，輸出 `speaker_id` 標籤。  

> **實驗數據**（VibeVoice‑ASR Technique Report）  
> - 平均字錯誤率（WER）: **6.8 %**（英語） / **9.3 %**（中文）  
> - 多語言測試（10 種語言）WER 均低於 **11 %**  

---

⚡️ **vLLM 加速：從幾分鐘降到秒級**

2026‑03‑06，Microsoft 宣布 VibeVoice‑ASR 已經 **整合至 Hugging Face Transformers**，同時支援 vLLM 推理後端。透過 vLLM 的 *tensor‑parallel* 與 *paged‑attention*，單卡 RTX 4090 可在 **0.9 秒/分鐘** 完成同樣長度的轉寫，適合即時字幕或直播流媒體的後端服務。

```python
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor
model = AutoModelForSpeechSeq2Seq.from_pretrained("microsoft/vibevoice-asr", trust_remote_code=True, device_map="auto")
processor = AutoProcessor.from_pretrained("microsoft/vibevoice-asr")
```

---

🗣️ **VibeVoice‑Realtime‑0.5B：多語言即時 TTS**

在 2025‑12‑03，Microsoft 釋出 **VibeVoice‑Realtime‑0.5B**，支援 **流式文字輸入**，可即時產生自然流暢的語音。特點包括：

- **九種語言**（德、法、義、日、韓、荷、波、葡、西）以及 **11 種英語風格**（新聞、對話、朗讀等）  
- **實驗性說話者**：2025‑12‑16 釋出 20+ 種說話者特徵，未來會持續擴充。  
- **Colab Demo**：只要點擊「Open in Colab」即可在瀏覽器內測試，無需本地環境。

> **速度指標**：在 RTX 3090 上，平均 **TTS latency ≈ 120 ms**（每 200 個 token），足以滿足實時互動式應用（如語音助手、直播互動）。

---

🔍 **深入分析：為何 VibeVoice 能兼顧長篇 ASR 與即時 TTS？**

1. **共享的語音基礎模型**：兩者皆基於同一個 **Conformer‑Hybrid** 編碼器，統一的聲學特徵抽取讓模型在不同任務間可直接切換。  
2. **分層解碼策略**：ASR 使用 *autoregressive* 文字解碼；TTS 則採用 *non‑autoregressive* 流式解碼，兩者在同一圖形硬體上同時運行不會互相干擾。  
3. **多任務微調**：在同一資料集（包括 CommonVoice、MLS、VCTK）上同時微調說話者辨識、語言辨識與語音合成，提升跨任務泛化能力。

---

⚠️ **研究限制與未來挑戰**

- **樣本偏倚**：目前的多語言測試主要集中在歐洲語系與中、英、日、韓四大語系，對於低資源語言（如非洲語系、南亞語系）仍缺乏充分驗證。  
- **長時記憶**：單次通過雖然有效率，但在 **超過 90 分鐘** 的音檔上仍會出現記憶飽和現象，需進一步探索段落級別的循環注意力。  
- **硬體需求**：vLLM 加速雖快，但在 CPU 或低階 GPU（如 RTX 3060）上仍會出現顯存瓶頸，實務部署需考慮資源配置。

---

🎯 **實務建議：如何在產品中快速落地 VibeVoice？**

1. **即時字幕服務**：將 `vibevoice-asr` 直接嵌入 WebRTC 流，搭配 `vLLM` 後端，即可在直播平台提供 0.5‑秒延遲的多語言字幕。  
2. **多語言客服機器人**：利用 `vibevoice-realtime-0.5b` 產生自然語調的回覆，結合 Azure Speech Service 的語音辨識，可在同一服務中完成「聽」與「說」的閉環。  
3. **內容自動整理**：把長會議錄音一次過轉寫，結合說話者標籤與時間戳，即可自動生成會議紀要或 Podcast 文字稿。  

> **程式碼範例**（FastAPI + VibeVoice）  
> ```python
> from fastapi import FastAPI, UploadFile
> from vibevoice import VibeVoiceASR, VibeVoiceRealtimeTTS
> 
> app = FastAPI()
> asr = VibeVoiceASR()
> tts = VibeVoiceRealtimeTTS()
> 
> @app.post("/transcribe")
> async def transcribe(file: UploadFile):
>     audio = await file.read()
>     result = asr.transcribe(audio)
>     return result
> 
> @app.post("/speak")
> async def speak(text: str, lang: str = "en"):
>     audio = tts.synthesize(text, language=lang)
>     return {"audio": audio}
> ```
> 只要部署在 Azure Container Instances，即可在全球多區域提供低延遲服務。

---

🔗 **論文與資源連結**  
📝 **VibeVoice‑ASR Technique Report**（PDF）  
👤 **Microsoft** – GitHub Repository: https://github.com/microsoft/VibeVoice  
🤗 **Hugging Face Transformers** – `microsoft/vibevoice-asr`  
🚀 **vLLM‑ASR** – https://github.com/vllm-project/vllm-asr  
💻 **Colab Demo (Realtime TTS)** – https://colab.research.google.com/github/microsoft/VibeVoice/blob/main/realtime_demo.ipynb  

---

💬 **你最想把 VibeVoice 用在哪個場景？**  
是直播字幕、跨語言客服，還是 Podcast 自動稿？留言告訴我你的想法，讓我們一起探索開源語音 AI 的無限可能！  

#AI #SpeechRecognition #TextToSpeech #OpenSource #Microsoft #VibeVoice #Transformers #vLLM #MultilingualAI #語音辨識 #語音合成
