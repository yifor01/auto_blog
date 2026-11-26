---
title: Hill-climbing Inkling 2 Mini inference on one RTX PRO 6000
source: HuggingFace Blog
url: https://huggingface.co/blog/inkling-2-mini-inference-hillclimb
model: claude-code/sonnet
generated_at: '2026-11-26T01:07:40.154202'
score: 100
---

📌 一張RTX PRO 6000，把Inkling 2 Mini推理衝到頻寬上限的95%

TL;DR：HuggingFace讓一個coding agent自己跑一下午基準測試，把Inkling 2 Mini在單張工作站GPU上的解碼速度拉升四成。

官方serving recipe只針對資料中心等級的B200與GB300調過，你手上那張RTX PRO 6000該怎麼辦？HuggingFace的做法是：把優化這件事直接交給agent自己去試。

🤔 **一顆looped MoE模型，官方recipe卻沒涵蓋你的卡**

Inkling 2 Mini上週發布，約26B總參數（每個token僅啟用3B），支援multimodal輸入與1M token的context window，在Artificial Analysis Intelligence Index v5上同量級稱霸，並在48項基準測試中有32項贏過Gemma 4 31B與Qwen3.8-27B。它能有這種表現，架構上一個可能的原因是：這是一個looped的Mixture-of-Experts模型，24個實體層，中間12層會重複執行三次，於是每個token實際上要走過48層。Checkpoint以混合NVFP4與MXFP8格式發佈，並內建DSpark drafter做投機解碼（speculative decoding）。vLLM與SGLang的nightly版本都已支援它，但官方公佈的serving recipe只針對NVIDIA B200、GB300這類sm100架構，像RTX PRO 6000這種sm120工作站卡的kernel相容性沒有被涵蓋。

🧩 **給agent一個下午、一套實驗協定和一張GPU**

HuggingFace沒有手動調flag，而是給一個coding agent裝上「inference-optimisation」skill、hf CLI，以及Hugging Face Jobs的存取權限，讓它自己跑實驗。協定很硬性：先量測硬體並估算理論頻寬上限，再一次只改一個變數，每個候選配置都要前後各夾一次control run（control→candidate→control），只有同時贏過兩次control、且沒有讓其他指標變差時才保留這個改動，所有結果（包括失敗與死路）都記錄在PLAN.md，最後還要通過長文本、併發與greedy-equivalence三項檢查，才能宣布贏家配置。bench.py負責量測單用戶解碼速度、N人併發下的聚合解碼速度、不同長度的cold prefill，以及首token延遲（TTFT），token數直接取自伺服器回傳的usage response。所有測試固定用六則prompt（程式碼、說明文、故事、比較表格、bash腳本、歷史摘要），溫度1.0（模型預設值），思考模式開啟，輸出512 token，啟用投機解碼時每組重複12次。

基礎設施上，HF Jobs的rtx-pro-6000規格與對外販售的nvidia-rtx-pro-6000 Inference Endpoint用的是同一張卡（都是每小時2.75美元），所以Job上量到的數字可以直接拿來當endpoint的參考。agent因此能把SGLang（lmsysorg/sglang:inkling-2-mini）與vLLM nightly（vllm/vllm-openai:nightly）平行掃過一遍。遇到沒有文件說明的flag，就開一個便宜的CPU Job，直接到容器裡grep已安裝的Python套件原始碼——SGLang的SGLANG_OPT_*環境變數與vLLM的speculative-config欄位就是這樣找出來的。最後透過hf endpoints deploy，用通過驗證的image digest與flag組合，把贏家配置部署成正式的Inference Endpoint。

📊 **從136到190.6 tok/s的落地數字**

| 配置（1張RTX PRO 6000） | 單用戶解碼 (tok/s) | 8用戶聚合 (tok/s) | Prefill 4K/32K (tok/s) | TTFT |
|---|---|---|---|---|
| SGLang，無投機解碼（基準） | 134–139 | 543–598 | 18.7–19.1K / 16.9–19.1K | 41–114 ms |
| vLLM，無投機解碼 | 157.0 | 638 | 20.7K / 20.7K | 33 ms |
| SGLang + DSpark（8 drafts） | 166.6 | — | 18.0–19.5K / 18.9–19.1K | 38–51 ms |
| vLLM + DSpark（7 drafts） | 190.6 | 716 | 20.7K / 20.6K | 40 ms |
| 正式部署的Endpoint（走網路） | 194.9 | 673 | 11.7K / 19.2K | 198 ms |

最終單用戶解碼從136提升到190.6 tok/s（+40%），優於同一張卡上社群公布的SGLang + DSpark基準（167.7 tok/s）；8用戶聚合吞吐量從約570提升到716 tok/s（+26%）。文中強調，加了投機解碼後greedy輸出與未加投機解碼時逐byte相同，長文本needle檢索測試在250K token內也是3/3全過。所有加速都來自：切換到vLLM nightly（136→157 tok/s，+15%）、啟用7個draft並改用機率式draft取樣的DSpark（157→190.6 tok/s，+21%），以及兩個讓vLLM的DSpark設定能在96GB顯存上啟動的記憶體flag。

💡 **為什麼卡在190 tok/s附近**

agent在開跑前先在一個Job裡量到這張卡的硬體規格：1,469 GB/s的拷貝頻寬、416 TFLOPS的BF16與792 TFLOPS的FP8算力，再從safetensors檔頭讀出張量大小。因為每個token要走48次layer visit，單純解碼一次要重新讀取約2.7GB的attention與dense權重、2GB的routed experts（每層128取8），以及0.9GB的LM head——在1,469 GB/s頻寬下，單用戶的理論頻寬上限約為256 tok/s。沒有投機解碼時，vLLM的157 tok/s只達到這個上限的61%，主要被48次layer visit帶來的kernel啟動延遲卡住。投機解碼則改變了MoE的記憶體算法：一次驗證8個位置會啟動這些位置路由到的experts聯集，讀取量從單一token的約6%暴增到約40%；在溫度1.0下實測的接受率約每步2.3個token（逐位置接受率從第一個draft的0.6，掉到第二個的0.33、第三個的0.19），頻寬上限因此降到約201 tok/s。實測190.6 tok/s已經是硬體頻寬的95%，代表再怎麼調flag，空間也所剩無幾。

⚠️ **哪些嘗試沒有用**

較短的draft長度（3到6）在啟動時就被拒絕，因為checkpoint的區塊大小固定要求num_speculative_tokens必須是7；把draft_sample_method改成greedy，在溫度1.0下反而讓解碼速度掉了11%；rejection_sample_method改成block幾乎沒有影響；enable_adaptive_verification在Inkling 2的drafter上會直接觸發assertion error；draft_lm_head_quantization設成fp8則只支援DeepSeek的DSpark drafter，Inkling 2用不到。

🎯 **實務啟示**

如果你要在消費級或工作站GPU上部署這類looped MoE模型，官方serving recipe很可能沒有照顧到你的硬體；文中這套「control→candidate→control」的實驗協定，搭配讓agent用Jobs大量平行跑配置，是一套可複製的調參方法論。另外也值得記住：在MoE模型上做投機解碼，驗證多個位置會讓啟用的expert集合變大，記憶體頻寬的代價要一併算進去，不是單純「加了投機解碼就一定更快」。

🔗 **來源**
- 標題：Hill-climbing Inkling 2 Mini inference on one RTX PRO 6000
- 作者／機構：Niels Rogge／Hugging Face
- 連結：https://huggingface.co/blog/inkling-2-mini-inference-hillclimb

#Inkling2Mini #LLMInference #vLLM #SGLang #SpeculativeDecoding #MixtureOfExperts #HuggingFace #GPUOptimization #EdgeAI #NVFP4
