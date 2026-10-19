---
title: 'TorchNeuron: running HF models on AWS Trainium is easier than ever'
source: HuggingFace Blog
url: https://huggingface.co/blog/hf-torchneuron
model: claude-code/sonnet
generated_at: '2026-10-19T21:46:44.900794'
score: 79
---

📌 Hugging Face新backend讓Trainium不用再當編譯器思維寫程式碼

TL;DR:TorchNeuron把AWS Trainium變成PyTorch原生裝置，Transformers、Diffusers可直接跑，不再需要專用fork。

如果你曾經想在AWS Trainium上跑Hugging Face模型，大概都經歷過這個痛點:得先學會用編譯器的腦袋思考——lazy tensor、固定shape、graph一斷就重新編譯。10月20日起，這個痛點有了新解法。

🤔 **過去optimum-neuron背後的代價:維護一整套專用程式碼**

根據Hugging Face官方部落格，過去在AWS Trainium與Inferentia（分別為訓練與推論設計的AI晶片）上的使用體驗，是透過optimum-neuron函式庫實現的。這套函式庫基於torch-neuronx，而torch-neuronx建立在PyTorch XLA之上——這在當時是自然的選擇，但也意味著開發者得用「編譯器思維」寫程式:lazy tensor取代即時執行、只能用固定shape、每次graph break都要重新編譯。為了隱藏這些複雜度，optimum-neuron得維護自己的一套modeling class、trainer等客製化程式碼。

🧩 **TorchNeuron:讓Neuron變成和其他裝置一樣的原生device**

TorchNeuron改變了這個現況。它是直接整合進PyTorch的plugin，把Neuron作為原生裝置暴露出來，支援即時執行（eager mode）、PyTorch自己的分散式原語（DTensor、FSDP2）以及torch.compile。對Hugging Face的函式庫而言，Trainium從此變成和其他加速器一樣的裝置——Transformers、Diffusers、Accelerate、PEFT與TRL都能直接在上面跑，用的是和其他加速器上完全相同的class與script。官方也建議Neuron使用者從今以後直接用這些函式庫，不用再透過optimum-neuron。

文章提供的數字相當具體:採用TorchNeuron後，前100個最常用的文字生成模型架構中，有89%可以直接開箱支援；相比之下，optimum-neuron v0.4.5只支援46%。

🧩 **怎麼用:推論只需多傳一個device_map參數**

推論端的用法非常直接，只要在程式碼中傳入`device_map="neuron"`，模型就會被搬到Neuron裝置上。文章給出的範例是搭配tensor parallelism做文字生成，並使用static cache以避免頻繁重新編譯（官方強調在Neuron上這是「強烈建議」的做法）：

```python
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    dtype=torch.bfloat16,
    distributed_config=DistributedConfig(tp_size=world_size),
    device_mesh=DeviceMesh("neuron", list(range(world_size))),
).eval()
```

訓練端則是用標準的TRL `SFTTrainer`微調流程，和在GPU上寫的script幾乎一模一樣。把`DistributedConfig`的tensor-parallel與FSDP尺寸放進`model_init_kwargs`，`SFTTrainer`會把它傳給`from_pretrained`，模型在載入權重的同時就會被切分——不需要`--fsdp`參數，也不需要Accelerate的FSDP設定檔。

🧩 **在Trainium上跑,仍有幾個小地方要注意**

官方文件列出幾個實務細節:一是固定shape——範例中關閉了torch.compile的自動動態shape功能，並用wrapped packing把序列長度補到最多2048 tokens，TRL 1.16以上版本會把Neuron上的batch補到128 tokens的倍數，限制輸入shape的種類，讓編譯過的graph可以在後續相同shape的步驟中重複使用；二是只要傳入`--torch_compile true`，torch.compile會自動偵測裝置並選擇Neuron backend，不需要額外設定；三是目前Neuron backend還無法編譯Dynamo的自動動態shape功能（文章引用了TRL的相關issue），因此非同步權重載入功能目前在Neuron上暫不支援，需要用`HF_DEACTIVATE_ASYNC_LOAD=1`關閉。

🎯 **實務啟示**

對正在評估或已經在用AWS Trainium的團隊來說，這代表可以把原本針對optimum-neuron寫的客製化訓練/推論程式碼，逐步換成和GPU上一樣的標準Transformers/TRL/PEFT流程，減少維護兩套程式碼的負擔。TorchNeuron將從10月20日起以public beta形式提供，可用`pip install torch-neuronx`安裝，值得在遷移前先確認你用到的模型架構是否在那89%的開箱支援清單內。

🔗 **來源**
- 標題：TorchNeuron: running HF models on AWS Trainium is easier than ever
- 作者／機構：Régis Pierrard、Simon Pagezy、Michael Benayoun、Jingya Huang、Alvaro Moran、David Corvoysier、Jeff Boudier（Hugging Face）
- 連結：https://huggingface.co/blog/hf-torchneuron

#AWSTrainium #PyTorch #HuggingFace #Transformers #MachineLearning #DeepLearning #MLOps #ModelTraining #Inference #TorchCompile
