---
title: "Making Every Verified Token Count: Adaptive Verification for MoE Speculative Decoding"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.00342
score: 104
model: tencent/hy3-preview:free
generated_at: 2026-05-04T20:40:32.101956
---

📌 MoE 推理加速 2.35 倍：只驗證「值得」的 Token

MoE 模型在長文本與 Agent 場景越來越普及，但 tree-based speculative decoding 的加速優勢，隨著草案樹擴張反而逐漸流失。分支越多、啟動專家聯集越大，驗證成本急遽攀高，加速比不升反降。我們真的只能忍受這種「加速天花板」嗎？

🤔 **越寬的草案樹，越昂貴的驗證代價**

針對稀疏 MoE 模型，傳統草案樹驗證會同時激活不同分支的專家集合，導致目標端驗證成本大幅增加。儘管 draft 階段看似產出更多候選，實際上卻帶來大量低效益的專家激活，拖慢整體生成。

🧪 **訓練免、超參免、無損的 EVICT 機制**

研究團隊提出 EVICT，一種兼容於 SGLang 等圖式高效服務框架的適應性驗證方法。EVICT 在目標驗證前動態截斷草案樹，只保留成本效益最高的前綴進行驗證：

- 依據細粒度 drafter 信號評估候選價值  
- 結合離線 profiling 的驗證成本資訊  
- 無需重新訓練、不引入額外超參、理論與實務皆無損  

這使得驗證階段的專家啟動被壓製在必要範圍內，加速效益不再被無效分支吞噬。

📈 **相較基線平均提速 1.21 倍，最高達 2.35 倍**

在多種 MoE 主幹與 benchmark 上的實驗顯示：

- 相比純 autoregressive 解碼：最高達 2.35 倍速度提升  
- 相比當前 SOTA 基線 EAGLE-3：平均提升 1.21 倍  
- 驗證階段不必要的專家激活顯著降低  

這不僅是吞吐量的提升，更讓 MoE 在長序列與 Agent 推理場景中更穩定可控。

🔍 **用「成本—效益」動態取代「越多越好」的啟發式**

EVICT 的關鍵在於跳脫「草案愈多愈好」的直覺思維，改以細粒度信號與離線成本模型協同決策。這使草案樹不再盲目擴張，而是在驗證前即被修剪至最具回報的範圍，從而兼顧速度與資源效率。

⚠️ **限於 tree-based MoE 設定，長期穩定性待探討**

EVICT 聚焦於當前主流的草案樹驗證框架，並依賴離線 profiling 提供的成本參考；雖然實驗階段表現穩定，但在更動態或異質部署環境下的泛化表現，以及極長序列下的穩定性，仍需進一步驗證。

⚙️ **高度兼容 SGLang，工程落地門檻低**

由於不修改訓練流程、不引入額外超參，EVICT 可直接接入現有高階服務框架。對於已採用 SGLang 的推理服務而言，部署成本與風險皆低，適合快速導入至長文本生成與 Agent 執行環境。

🔗 **論文連結**  
📝 Making Every Verified Token Count: Adaptive Verification for MoE Speculative Decoding  
👤 Lehan Pan, Ziyang Tao, Ruoyu Pang, Xiao Wang, Jianjun Zhao  
🏫 University of Science and Technology of China; Tianyijiaotong Technology Ltd.  
🔗 https://arxiv.org/abs/2605.00342  

你的 MoE 推理服務目前如何管理草案樹的驗證成本？是否有類似的動態修剪經驗？歡迎交流 👇  

#MoE #SpeculativeDecoding #LLMInference #SGLang #AIEngineering
