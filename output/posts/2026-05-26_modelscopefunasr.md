---
title: "modelscope/FunASR"
source: GitHub Trending
url: https://github.com/modelscope/FunASR
score: 89
model: tencent/hy3-preview:free
generated_at: 2026-05-26T21:17:42.214225
---

📌 【ModelScope FunASR】語音識別速度提升 170 倍，一行程式碼即可完成 VAD、ASR、說話人分離與情感偵測  

你以為 Whisper 已經是開源語音識別的天花板？FunASR 聲稱在同樣硬體上跑快 170 倍，且內建說話人與情感偵測，免去額外套件。  

🤔 **工具背景：為何需要一站式語音處理？**  
傳統語音 pipeline 常需要分別安裝 VAD、ASR、標點、說話人分離（pyannote）以及情感模型，每個步驟都有獨立的依賴與成本。FunASR 將這些功能整合到單一模型與一個 API 呼叫中，降低開發與維護複雜度。  

🧪 **核心功能與使用方式**  
- 支援 50+ 語言，內建說話人分離與情感偵測（Happy / Sad / Angry）。  
- 提供即時串流（WebSocket）與批次處理兩種模式。  
- 一行程式碼即可完成端到端識別：  

```bash
pip install funasr
```

```python
from funasr import AutoModel
model = AutoModel(
    model="iic/SenseVoiceSmall",
    vad_model="fsmn-vad",
    spk_model="cam++",
    device="cuda"
)
result = model.generate(input="meeting.wav")
```

- 輸出為結構化文字，包含時間戳、說話人標籤與標點。  
- 可透過 `funasr-server --device cuda` 啟動 OpenAI‑相容的 HTTP 端點（localhost:8000），直接被 LangChain、Dify、AutoGen 或 MCP Server（Claude/Cursor）調用。  

💡 **效能與比較**  
根據專案基準表：  
- FunASR：170× realtime（在 GPU 上）  
- Whisper（開源）：13× realtime  
- 雲端 API：約 1× realtime  
此外，FunASR 內建說話人 ID（無需額外 pyannote）、情感偵測，並支援 vLLM 加速，可再提升 2–3 倍吞吐。  

⚠️ **使用限制與注意事項**  
- 速度數據基於特定硬體與模組（SenseVoiceSmall、fs mn‑vad、cam++）測得，實際表現會隨設備與語言而異。  
- 情感偵測目前僅區分三種極性，細緻情感辨識尚未涵蓋。  
- 儘管工具鏈非常完整，核心模型本身並非全新創新，其價值主要在於打包、部署與 OpenAI 相容性。  

🎯 **實務啟示：如何快速落地語音應用？**  
- 會議紀要、客服錄音分析：直接呼叫 API 取得帶說話人與情感的逐字稿。  
- 語音代理或 Agent：利用 OpenAI‑相容端點，將 FunASR 作為前端語音理解層，簡化與 LLM 的串接。  
- 資料隱私敏感場景：選擇自行部署（Docker 或裸機），避免將語音上傳至第三方雲端。  

🔗 **資源連結**  
📂 GitHub：https://github.com/modelscope/FunASR  
📖 快速開始 Colab（見專案 README）  
📚 文件與模型選擇指南：專案內 Docs 目錄  

你是否已在專案中嘗試過一站式語音處理？歡迎在留言區分享你的使用經驗或遇到的挑戰 👇  

#FunASR #ModelScope #語音識別 #ASR #說話人分離 #情感偵測 #OpenAI相容 #AI工具 #GitHubTrending
