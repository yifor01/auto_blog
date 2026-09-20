---
title: 'GGUF vs GPTQ vs AWQ vs EXL2: LLM Model Formats Explained (2026)'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/18/gguf-vs-gptq-vs-awq-vs-exl2-llm-model-formats-explained-2026/
model: claude-code/sonnet
generated_at: '2026-09-20T19:35:32.832304'
score: 81
---

📌 GGUF、GPTQ、AWQ、EXL2怎麼選?量化格式一次搞懂

TL;DR:容器格式與量化方法是兩層不同概念,搞懂這點才能對症選對LLM部署方案。

模型檔名裡的Q4_K_M、4.65bpw、AWQ這些後綴,常讓人一頭霧水。其實大部分的混淆,來自把兩層完全不同的東西混在一起看。

🤔 **容器格式與量化方法,是兩回事**

一個容器定義的是tensor如何存在磁碟上;一個量化方法定義的是權重如何被壓進更少的位元。權重記憶體用量約略等於「參數量 × 每權重位元數 ÷ 8」,這只是算術,不是廠商跑分,而且僅涵蓋權重本身,KV cache與執行期額外開銷還要另外疊加。

未量化模型通常以16位元權重形式發佈,存成pytorch_model.bin或model.safetensors。較舊的.bin/.pt檔案使用Python pickle格式,載入pickle檔案可能執行任意程式碼,對不受信任的checkpoint是安全風險。Hugging Face推出的safetensors則移除了這個風險:檔案只是一小段JSON標頭加上原始tensor緩衝區,內部沒有任何可執行內容,tensor可以被記憶體映射(mmap)並逐一載入,無需讀取整個檔案。值得注意的是,多數GPTQ、AWQ、EXL2、EXL3與MLX模型其實也都儲存在.safetensors檔案裡,量化資訊是放在tensor內容與設定檔中,而不是換了新容器。

🧩 **GGUF:llama.cpp生態系的原生格式**

GGUF由llama.cpp的創建者Georgi Gerganov提出,於2023年8月21日發布,取代舊有的GGML格式。舊格式(GGML、GGMF、GGJT)無法標示模型屬於哪個架構,新增一個超參數就會破壞所有既有檔案;GGUF改用具型別的鍵值(key-value)中繼資料,可以在不破壞舊檔案的前提下新增欄位。規格列出五個目標:單檔部署、可擴展性、mmap相容、易於載入、資訊完整內含於檔案中。與只存tensor的格式不同,GGUF可以在同一個檔案內連帶存放tokenizer、特殊token與Jinja聊天樣板。

檔名中的Q4_K_M之類後綴代表量化方案。以Q4_K為例:一個super-block容納256個權重,256×4bit=1024bit,再加上8組scale/minimum各12bit(共96bit),以及一個16bit的super-scale和16bit的super-minimum(共32bit),總計1152bit÷256=每權重4.5bit。而_S、_M、_L代表的是混合精度組合而非全新型態,例如llama.cpp文件說明Q4_K_M會對一半的attention.wv與feed_forward.w2張量使用Q6_K、其餘用Q4_K,這也是為什麼Q4_K_M實際檔案平均位元數會高於4.5bit。GGUF量化還可以使用校正資料:llama.cpp的llama-imatrix能從文字檔算出重要性矩陣,llama-quantize --imatrix再用它提升量化品質,對1bit、2bit的混合方案,若沒有提供imatrix,llama-quantize會提出警告。GGUF目前原生支援llama.cpp、LM Studio、GPT4All與Ollama等生態,vLLM雖然存在支援,但官方形容為「高度實驗性且未充分最佳化」,且現在需要額外的vllm-gguf-plugin。

🧩 **GPTQ、AWQ、EXL2/EXL3、bitsandbytes、MLX 各有側重**

**GPTQ**由IST Austria的Elias Frantar、ETH Zurich的Saleh Ashkboos與Torsten Hoefler,以及IST Austria／Neural Magic的Dan Alistarh共同提出,2022年10月31日發表於arXiv,後刊登於ICLR 2023。它是一種one-shot、訓練後(post-training)的權重量化方法,利用近似二階(Hessian)資訊決定如何捨入權重,某一欄的捨入誤差會透過調整尚未量化的權重來補償,需要少量校正資料集,但不需要重新訓練。原始的AutoGPTQ函式庫目前已不再維護。

**AWQ**(Activation-aware Weight Quantization)來自MIT Song Han團隊,2023年6月1日發表於arXiv,獲得MLSys 2024最佳論文獎。其核心觀察是並非所有權重都同等重要,保護約1%的「顯著」權重就能大幅降低量化誤差;巧妙之處在於AWQ透過觀察activation幅度、而非權重本身來找出這些顯著channel,且不將它們以更高精度另外儲存,而是透過數學上等價的變換將其縮放,維持統一、對硬體友善的格式。AWQ不使用反向傳播或重建,因此較不容易對校正資料集過擬合。

**EXL2**是turboderp開發的推理函式庫ExLlamaV2的原生格式,主打消費級GPU,採用與GPTQ相同的最佳化方法,支援2、3、4、5、6、8bit量化,因此檔名常標示如4.65bpw而非固定的「4-bit」。官方推薦的伺服器是提供OpenAI相容API的TabbyAPI。EXL2會重新命名部分tensor,讓每個模型在內部看起來都像Llama變體,這使得它較難被其他框架重用。

**EXL3**是後繼格式,建構於Cornell RelaxML提出、發表於NeurIPS 2024的QTIP之上,採用trellis編碼量化搭配incoherence processing,EXL3延續了QTIP的程序化codebook與trellis編碼方式,調整的是tensor的正規化與打包方式。ExLlamaV3在此基礎上新增2至8bit的KV cache量化、張量與專家並行推理、推測解碼、多模態支援,以及Transformers外掛,近期版本也加入了大型MoE模型的CPU卸載功能。硬體上,ExLlamaV3要求CUDA 12.4以上,其README中ROCm支援仍列為待辦事項。

**bitsandbytes**通常不是預先量化好下載,而是載入16bit模型後即時量化,其4bit模式源自QLoRA。**MLX-LM**則是Apple Machine Learning Research推出、用於在Apple Silicon上執行與微調LLM的Python套件,MLX模型是帶有MLX專屬量化權重的safetensors,可用mlx_lm.convert加上-q參數將Hugging Face模型量化並上傳至mlx-community組織。在Mac上,透過llama.cpp使用GGUF與使用MLX都是不錯的選擇。

⚠️ **數字僅供參考**

文中引用Hugging Face針對Llama-2-7B級模型的量化位元/品質對照表僅為示意,數字來自2023年的7B模型,較新的模型在量化下的表現可能不同。

🎯 **實務啟示**

選格式前先分清楚自己要解決的是「容器」還是「量化」問題:若在llama.cpp/Ollama生態內部署,GGUF是預設選擇,且Q4_K_M搭配imatrix校正通常是品質與體積的均衡點;若鎖定消費級GPU且想要非整數位元的精細權衡,EXL2/EXL3更合適;若追求無需大量校正資料、對過擬合風險敏感的量化方案,AWQ值得考慮;若需要一次性、免重新訓練的post-training量化,GPTQ仍是成熟選項;在Apple Silicon上,GGUF與MLX都是可行路線。

🔗 **來源**
- 標題:GGUF vs GPTQ vs AWQ vs EXL2: LLM Model Formats Explained (2026)
- 作者／機構:Asif Razzaq／MarkTechPost
- 連結:https://www.marktechpost.com/2026/09/18/gguf-vs-gptq-vs-awq-vs-exl2-llm-model-formats-explained-2026/

#LLM #Quantization #GGUF #GPTQ #AWQ #EXL2 #LlamaCpp #ModelDeployment #MachineLearning #EdgeAI
