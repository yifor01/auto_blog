---
title: "The Memory Curse: How Expanded Recall Erodes Cooperative Intent in LLM Agents"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.08060
score: 101
model: tencent/hy3-preview:free
generated_at: 2026-05-11T20:44:37.145715
---

📌 【CMU 最新研究】記憶視窗變長，合作意願卻下降？

你以為讓 AI 能記得更多對話會讓它更合作？研究顯示，相反的情況發生在多代理社會困境中。

🤔 **記憶變長，卻讓合作更難維持**

隨著語言模型的上下文視窗不斷擴大，人們常認為這是單純的能力提升。但在多代理互動的情境下，更長的歷史紀錄真的會幫助合作嗎？這篇論文提出了一個反直覺的現象——**記憶詛咒**（memory curse）。

🧪 **七種模型、四種博弈、五百輪對抗實驗**

研究團隊在七種不同的大型語言模型與四種社會困境博弈中，各進行了五百輪互動。他們比較了限制歷史長度與擴充歷史長度兩種條件下的合作率，並蒐集了超過三十七萬條推理追蹤（reasoning trace）進行詞彙層面分析。

📉 **擴充記憶在十八種模型‑博弈組合中降低合作**

在二十八種模型‑博弈組合中，有十八種顯示當可見歷史變長時，合作意願明顯下降。研究團隊將此現象命名為「記憶詛咒」。進一步的詞彙分析顯示，合作的衰落與**前瞻意圖（forward‑looking intent）的侵蝕**相關，而非單純的猜疑或不信任增加。

💡 **前瞻意圖是關鍵，LoRA 適配器可部分修復**

為驗證機制，團隊針對那些帶有前瞻意圖的推理追蹤進行專門的 LoRA 適配器微調。此適配器在未見過的博弈中也能零射擊地提升合作率，表明前瞻性的推理模式是維持合作的重要因素。

🧹 **記憶內容而非長度才是罪魁禍首**

在另一組實驗中，他們將可見歷史的長度固定，但用合成的合作記錄取代真實對話歷史（記憶潔淨化，memory sanitization）。結果顯示合作率顯著回升，證明問題出在**記憶的內容**，而不僅是記憶長度本身。

⚙️ **鏈式思考（CoT）會放大記憶詛咒**

當研究團隊移除明確的鏈式思考（Chain‑of‑Thought）提示時，記憶導致的合作崩潰幅度往往會變小。這意味著，深度的 deliberation 反而會把負面的歷史資訊放大，進一步削弱前瞻意圖。

⚠️ **僅涵蓋特定模型與博弈，長效及其他任務有待驗證**

此研究的結論基於七種語言模型與四種社會困境博弈。是否在更大規模的模型、不同類型的任務或長期互動中仍然成立，尚需進一步驗證。

🎯 **實務啟示：設計記憶時要關注「前瞻性」**

- 在多代理或對話系統中，單純加長上下文未必帶來更好合作，需審視歷史內容是否鼓勵前瞻性思考。  
- 可嘗試使用導向前瞻意圖的資料進行少量微調（如 LoRA 適配器）來抵負面歷史的影響。  
- 記憶潔淨化或合成正向歷史的方法，在提升合作率方面具有潛力。  
- 若系統依賴鏈式思考推理，應該評估其是否無意中放大了不利的歷史資訊。

🔗 **論文連結**  
📝 The Memory Curse: How Expanded Recall Erodes Cooperative Intent in LLM Agents  
👤 Jiayuan Liu, Tianqin Li, Shiyi Du, Xin Luo, Haoxuan Zeng  
🏫 Carnegie Mellon University; Foundations of Cooperative AI Lab; University of Michigan; Harvard University  
🔗 https://arxiv.org/abs/2605.08060  

你在設計多代理 AI 時，是否曾注意到「記得越多，合作越少」的現象？歡迎在留言區分享你的經驗與想法 👇

#AI #LLM #多代理系統 #記憶效應 #合作博弈 #CMU #研究解讀
