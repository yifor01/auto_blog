---
title: 'How to Run NVIDIA Dory 4B with llama.cpp: Loop by Loop Guide'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/07/coding-guide-nvidia-dory-4b-llama-cpp/
model: claude-code/sonnet
generated_at: '2026-11-08T21:15:03.109622'
score: 99
---

📌 同一顆checkpoint，四種算力：Dory 4B的loop玄機

TL;DR：NVIDIA Nemotron Labs的Dory 1.0 4B靠重複執行同一層block調節推理算力，這篇教學逐項實測驗證其設計宣稱。

多跑一次同一段網路層，居然能讓同一個checkpoint變成四種不同運算預算的模型，聽起來像在鑽漏洞，但NVIDIA Nemotron Labs的Dory確實是這樣設計的：中間層組成一個共享block，每個token可以套用一次、兩次、三次或四次，每多跑一次loop就多花運算，卻不增加一個參數，一顆checkpoint不需要重新訓練就能在四種compute budget下運作。

🤔 從GGUF header讀出的架構

因為Dory在llama.cpp的支援還是一個未審核通過的draft PR，沒有任何官方發行的binary能載入它，必須照NVIDIA model card指定的commit自己編譯。GGUF header顯示整個模型72個layer entry分成三組：輸入層16層、共享的recurrent block 40層、輸出層16層，attention與MLP交替排列，每3個sliding-window layer搭配1個full-attention layer。把各組的張量大小加總，recurrent block就佔了全模型3.98B參數中的1.84B。header裡還藏著一個陷阱：內建的loop count預設是4，但model card建議用2，如果啟動伺服器時沒有手動override，就會悄悄用上最貴的設定。

🧩 下載與驗證：檔名對不上、要靠SHA-256抓包

3.7GB的Q5_K_M GGUF檔案來自Hugging Face的固定版本，下載後先做雜湊比對。model card裡的指令把檔案稱作`dory-q5_k_m.gguf`，但實際的repository裡檔名是`NVIDIA-Nemotron-Labs-Dory1.0-4B-Q5_K_M.gguf`，直接照抄官方指令會失敗；把真實檔名、大小與SHA-256一起pin住，可以同時抓到「檔名錯誤」與「下載損毀」兩種問題。

📊 loop次數對記憶體與速度的影響

從架構推算，4個loop會套用1個loop的2.51倍參數量，讀取2.28倍的權重位元組（對memory-bound的decoder來說，位元組數才是更準的指標）。KV cache則依照fork的分配規則有兩種模式：`per_loop`為每個loop的每個recurrent attention layer各存一份獨立cache，在4096 token context下從1個loop的306MiB一路長到4個loop的816MiB；`last_loop`模式則固定維持306MiB不變。教學實際起了七組伺服器設定（1到4個loop、兩種cache模式）做驗證，比對解析出的層數與理論推算是否一致，再用同一個prompt生成192個token（greedy解碼、取3次中位數）量出各設定的decode速度，除以1-loop的速度得到實測減速比，拿去和理論預測的比例互相印證，藉此判斷解碼行為更接近compute-bound還是memory-bound。

💡 配對GSM8K實驗：loop到底改變了什麼

先用50題GSM8K題目當prompt，在每種設定下取top-20的next-token候選，比較top-1一致性與total variation distance，驗證`last_loop`是否真的等同`per_loop`——理論上兩者只有在prompt被切成多個micro-batch時才會出現差異，整段prompt一次處理時不會有差別；教學接著用16-token的micro-batch重跑一次這個探針，正好驗證了這個預測。再用30題配對樣本在五種設定下讓模型帶推理作答，記錄正確率（Wilson信賴區間、McNemar精確檢定）、生成token數（含推理過程，和1-loop比較的中位數比例，附bootstrap區間）、是否撞到2048 token上限，以及每題花的時間，最終把速度、長度與正確率合併成「每道解出的題目實際要付出多少時間成本」這個指標。

⚠️ 樣本量與未驗證的宣稱

作者明確指出，30題配對樣本不足以判定小幅度的正確率差異。model card裡有些宣稱這次教學完全沒測到，例如官方benchmark表格、256K context、NVFP4預訓練，文章把這些標記為「未測試」而不是直接當作已驗證或已推翻。另外CPU-only與GPU/Metal伺服器在next-token分佈上的一致性檢查，也只拿5個prompt做抽樣比對，因為Dory在每個backend上的支援都還沒經過上游完整審查。

🎯 實務啟示

部署looped transformer類模型時，務必顯式指定loop count，別信任GGUF內建的預設值；同時要pin住fork的commit，因為上游支援還停在draft PR階段，行為可能隨時改變。如果記憶體是瓶頸，`last_loop`的cache模式能省下大量KV memory，但要先驗證輸出分佈跟`per_loop`在你實際的批次處理方式下是否真的一致。

🔗 來源
- 標題：How to Run NVIDIA Dory 4B with llama.cpp: Loop by Loop Guide
- 作者／機構：Sana Hassan（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/11/07/coding-guide-nvidia-dory-4b-llama-cpp/

#NVIDIA #Dory #LoopedTransformer #llamacpp #LLM #GSM8K #Inference #TestTimeCompute #OpenSource #MachineLearning
