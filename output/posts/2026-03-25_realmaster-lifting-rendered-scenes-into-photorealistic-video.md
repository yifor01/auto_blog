---
title: "RealMaster: Lifting Rendered Scenes into Photorealistic Video"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.23462
score: 113
model: gpt-4o-free
generated_at: 2026-03-25T19:34:25.192756
---

📌 【Tel Aviv University + Meta Reality Labs】RealMaster：讓 3D 渲染影片直接變寫實，幾何不變  

你有沒想過，遊戲引擎產出的影片雖精準卻總欠點真實感？而純 AI 生成影片又失去對場景的精準控制？RealMaster 試圖用一種「錨點傳播」+ IC‑LoRA 的方式，把兩者的優點結合起來。  🤔 **當 AI 生成失控，3D 引擎陷入 uncanny valley**  
現有的視訊生成模型能產出高度寫實的畫面，但缺乏對場景幾何與動態的精準控制；相反，3D 引擎可以逐個調整每個元素並保證天然的 3D 一致性，然而其輸出常停留在「不可思議的山谷」，缺乏照片級的材質、光線與紋理。這個同時需要結構精準與全域語意轉換的缺口，正是 RealMaster 要填補的目標。  

🧪 **以錨點傳播建立訓練對，IC‑LoRA 蒸餾模型**  
研究團隊首先透過錨點傳播策略建立配對資料集：讓影片的第一幀與最後幀經過寫實增強，再利用幾何條件引導將這種寫實傳播到中間幀。接著，他們在這些配對影片上訓練 IC-LoRA，將管線的高品質輸出蒸餾成一個能在沒有錨點幀的情況下泛化的模型，因而能處理中途出現的物體與角色。  

💡 **在 GTA‑V 複雜序列上，RealMaster 優於現有編輯基線，同時保持幾何與動態**  在複雜的 GTA‑V 視訊上進行評估，RealMaster 明顯勝過既有的視訊編輯基線，在提升寫實感的同時，完整保留了原始 3D 控制所指定的幾何結構、動態軌跡與物體身份。  

🔍 **錨點傳播如何實現幾何對齊與全域語意轉換**  
透過將寫實增強限制在序列的兩端，並以幾何條件作為橋樑，模型學會在不破壞底層幾何的前提下，對材質、光線與紋理進行全域的語意轉換。這種設計讓輸出既符合 3D 引擎的精準控制，又獲得視訊擴散模型的寫實表現。  

⚠️ **僅在 GTA‑V 上驗證，訓練仍需錨點幀，泛化能力待進一步探討**  
目前的實驗僅針對 GTA‑V 的複雜場景進行，訓練階段仍依賴錨點幀的寫實增強，模型在完全不同的場景或更長時間序列上的表現尚未被探討。此外，管線的資料集生成過程依賴特定的幾何條件引導，可能在缺乏精準幾何資訊的環境下受限。  🎯 **可直接用於遊戲、虛擬製作與機器人模擬的可控視訊生成**  
由於 RealMaster 能在保持原始 3D 場景幾何與動態的同時提升寫實感，它在遊戲內容製作、虛擬製作前視覺化以及機器人仿真中的視訊生成都具備直接應用潛力。研究團隊亦釋放了所使用的配對資料集，供後續研究與工程參考。  

🔗 **論文連結**  
📝 RealMaster: Lifting Rendered Scenes into Photorealistic Video  
👤 Dana Cohen‑Bar, Ido Sobol, Raphael Bensadoun, Shelly Sheynin, Oran Gafni (Tel Aviv University; Reality Labs, Meta; Technion)  🔗 https://arxiv.org/abs/2603.23462  

你認為這種「渲染→寫實」的管線在未來的互動媒體中會扮演什麼角色？歡迎在留言區分享你的看法 👇  

#AI #VideoGeneration #ComputerVision #GTA5 #VirtualProduction #Meta #TelAvivUniversity #Technion #RealMaster
