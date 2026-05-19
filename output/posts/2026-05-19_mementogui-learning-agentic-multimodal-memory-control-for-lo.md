---
title: "MementoGUI: Learning Agentic Multimodal Memory Control for Long-Horizon GUI Agents"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.18652
score: 124
model: tencent/hy3-preview:free
generated_at: 2026-05-19T20:21:54.923665
---

📌 【University of Rochester 等】MementoGUI：讓 GUI 代理在長序列任務中記得更好  

你以為讓 AI 把每一步螢幕畫面全記住就能玩轉複雜介面？事實上，這樣做會讓模型被大量無關資訊淹沒，反而傷害決策品質。  

🤔 **長 horizon GUI 任務需要可控的記憶機制**  
現有的 GUI 代理多依賴 raw history replay 或純文字記憶。前者會用大量截圖添加冗餘資訊，後者則捨棄了未來決策所需的局部視覺線索。兩種方式都無法在需要跨多介面切換的長序列任務中穩穩保持任務狀態。  

🧪 **MementoCore：可插拔的多模記憶控制器**  
論文提出 MementoGUI 框架，其核心是 MementoCore —— 一個學習得到的線上記憶選擇、壓縮與檢索控制器。它把長 horizon GUI 控制視為一個記憶控制問題：工作記憶選擇性保留具任務相關性的介面事件，同時附上文字摘要與 ROI 級的視覺證據；情節記憶則透過學習得到的相關性選擇，檢索可重用的過去軌跡。MementoCore 將記憶控制模組化為四種運算子（步驟處理、記憶壓縮、情節寫入、情節選擇），使其能以 plug‑in 方式直接加入既有的 MLLM GUI 代理骨幹，無需額外微調。  

📈 **實驗顯示一致的效能提升**  
作者進一步設計了可擴展的資料蒐集管線，將電腦使用軌跡轉換為記憶控制器的訓練資料，並提出新基準 MementoGUI‑Bench 以及基於 MLLM 的評估指標（語義動作匹配、任務進度、記憶一致性）。在 GUI‑Odyssey、MM‑Mind2Web 與 MementoGUI‑Bench 三個基準上，MementoGUI 在無歷史、歷史回放、純文字記憶等基線上都表現出提升；同時，更大的 MementoCore 骨幹會進一步強化記憶增強的 GUI 控制能力。  

🔍 **關鍵洞察：選擇性保留視覺與文字線索才是關鍵**  
與其讓模型被動重播所有畫面，MementoGUI 教會代理在線上判斷哪些片段對當前任務真正有用，僅保留那些具備文字摘要與局部視覺證據的事件。這樣的選擇性記憶既避免了資訊過載，又保留了未來決策所需的細節，從而在長序列情境中維持更穩定的任務狀態。  

⚠️ **實驗範圍與評估指標仍有待擴充**  
目前的結果僅在 GUI‑Odyssey、MM‑Mind2Web 與新提出的 MementoGUI‑Bench 三個基準上獲得；論文未報告在更長或更複雜真實應用場景中的表現，亦未詳細說明 MementoCore 在極端歷史長度下的運算開銷。  

🎯 **對工程師的實務建議**  
- 若你正在構建基於 MLLM 的 GUI 代理，可直接將 MementoGUI 作為記憶增強的 plug‑in 加入，無需重新訓練代理骨幹。  
- 透過提供的資料蒐集管線，可將自身的電腦使用軌跡轉換為訓練 MementoCore 的素材，以適配特定領域的 GUI 任務。  
- 在評估時，參考論文提出的 MLLM 基準指標（語義動作匹配、任務進度、記憶一致性）來全面檢視代理的長序列決策品質。  

🔗 **論文連結**  
📝 MementoGUI: Learning Agentic Multimodal Memory Control for Long-Horizon GUI Agents  
👤 Ziyun Zeng, Hang Hua, Bocheng Zou, Mu Cai, Rogerio Feris  
🏫 University of Rochester; MIT-IBM Watson AI Lab; University of Wisconsin-Madison  
🔗 https://arxiv.org/abs/2605.18652  

你是否曾因 GUI 代理在長序列任務中「忘記」關鍵步驟而感到困擾？歡迎在留言區分享你的經驗或對記憶控制的看法 👇  

#AI #GUIAgent #MultimodalMemory #MLLM #ComputerVision #HumanComputerInteraction #UniversityOfRochester #MITIBMWatson #UWMadison #MementoGUI
