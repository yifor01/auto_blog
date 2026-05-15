---
title: "XDomainBench: Diagnosing Reasoning Collapse in High-Dimensional Scientific Knowledge Composition"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.14754
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-05-15T20:42:49.485176
---

📌 **XDomainBench: 揭露高維科學知識組合中的推理崩潰**  

🎣 **你以為讓 LLM 跨領域寫論文只是提個 prompt 就好？實際測試顯示，當知識需要跨越多個科學領域時，模型的推理會快速崩解。**  

🤔 **科學知識組合的真實挑戰**  
現有基準多聚焦於單步、封閉場景，無法反映真正的跨學科科研工作流。為了檢驗 LLM 在真實 AI4S 情境中的組合推理能力，研究團隊設計了互動式基準。  

🧪 **8,598 次互動會話的壓力測試**  
XDomainBench 包含 20 個科學領域、4 種任務類型、8 種真實軌跡模式，共產生 8,598 次互動會話，從單學科逐步提升至跨學科組合，系統地檢測不同組合順序下的表現。  

📉 **組合順序升高時，推理會系統性崩解**  
大規模評估顯示，隨著需要組合的領域數增加，模型的正確率顯著下降。這種崩解主要源於兩個因素：(i) 領域組合本身帶來的直接難度提升；(ii) 軌跡模式觸發的間接效應，導致錯誤累積、推理中斷以及領域混淆，最終造成整個會話失效。  

💡 **間接失誤如何放大錯誤**  
當特定的互動軌跡（例如頻繁切換任務或需要回溯）出現時，早期的小錯誤會被放大，使模型在後續步驟中更容易產生領域混淆，進而導致推理鏈斷裂。這指出，僅提升單步準確度不足以防止複雜工作流中的連鎖失誤。  

⚠️ **基準設計的限制**  
XDomainBench 目前聚焦於文字 기반 的互動場景，未涵蓋多模態輸入或真實的實驗室儀器操作。此外，基準使用的軌跡模式雖然模擬了真實工作流，但可能無法涵蓋所有可能的科研情節。  

🎯 **實務啟示：評估與改進方向**  
對於 AI4S 系統的開發者，這個基準提供了一種可量化的方式來檢測模型在跨領域組合任務中的脆弱點。改進方向可著重於錯誤檢測與回溯機制，或在訓練階段引入更多樣化的跨域互動軌跡，以減少間接失誤的放大效應。  

🔗 **論文連結**  
📝 XDomainBench: Diagnosing Reasoning Collapse in High-Dimensional Scientific Knowledge Composition  
👤 Gong Zhiren, Tiantong Wu, Jiaming Zhang, Fuyao Zhang, Che Wang (Nanyang Technological University; Umeå University; Alibaba Group; School of Electrical and Electronic Engineering)  
🔗 https://arxiv.org/abs/2605.14754  

#AI #LLM #AI4S #Reasoning #Benchmark #NanyangTechnologicalUniversity #UmeåUniversity #AlibabaGroup
