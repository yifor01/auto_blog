---
title: "Persistent Visual Memory: Sustaining Perception for Deep Generation in LVLMs"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.00814
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-04T20:34:09.274367
---

📌 【上海AI Lab首創】視覺記憶不會被文字淹沒，長序列生成終於穩了

多模態助理越來越會「說話」，卻越來越「看不清圖」。  
當對話拉長、歷史堆疊，LVLMs 的視覺注意力會被文字序列長度「稀釋」；你以為它還在盯著圖片思考，其實視覺信號已經悄悄崩解。

🤔 **長序列生成正在吃掉視覺注意力**

Autoregressive LVLMs 在多輪對話與長文本生成中表現亮眼，但伴隨文本歷史不斷累積，注意力空間被大幅擴張，視覺訊號的權重會隨生成長度反比衰減。這不僅削弱感知精度，更直接傷害需要持續視覺參考的複雜推理。

問題是：在不犧牲生成效率的前提下，如何讓模型「長時間都看得清楚」？

🧪 **距離無關的視覺取回路徑，嵌入為平行分支**

團隊提出 Persistent Visual Memory（PVM），一個輕量、可學習的模組，並行於前饋神經網路（FFN）分支。  
PVM 構建距離無關的取回機制，直接輸出視覺嵌入，繞過注意力稀釋效應，為模型提供隨時可用、穩定精確的視覺感知。

实驗以 Qwen3-VL 為基座，在 4B 與 8B 規模下驗證，參數開銷幾可忽略。

📉 **視覺信號不再稀釋，複雜推理穩定提升**

- PVM 有效抵銷長度導致的視覺衰減
- 內部預測收斂速度加快
- 平均準確率在雙規模下穩定提升，尤其在需要持續視覺推理的任務中增益明顯

💡 **結構補償取代注意力擴張，把感知與生成解耦**

傳統做法常透過擴大注意力視野或重計算來緩解稀釋；PVM 選擇另一條路：  
把「持續感知」從生成主幹中解耦，以輕量外掛維護視覺狀態。這不僅壓制訊號抑制，還讓模型在長上下文與深層生成中保持穩定的視覺參考。

⚠️ **研究以 Qwen3-VL 為主，長期部署與跨模型泛化仍待驗證**

目前驗證集中於特定 LVLM 家族與中短訓練週期；更長序列、更大規模與不同架構上的穩定性，以及開放環境下的部署成本，仍需進一步探討。

🎯 **把 PVM 當作「視覺緩存」設計，長上下文多模態助理值得內建**

- 視覺感知不應依賴注意力分配的殘餘餘量
- 平行分支設計兼容現有 LVLM 架構，遷移成本低
- 對需要長期盯圖與多輪推理的應用（醫療、工程、教育）具直接啟發

🔗 **論文連結**  
📝 Persistent Visual Memory: Sustaining Perception for Deep Generation in LVLMs  
👤 Siyuan Huang, Xiaoye Qu, Yafu Li, Tong Zhu, Zefeng He  
🏢 Shanghai AI Laboratory; Shanghai Jiao Tong University; CUHK; Nanjing Univ.; Tongji Univ.; Wuhan Univ.  
🔗 https://arxiv.org/abs/2605.00814

你在開發或部署長上下文多模態助理時，是否也看見「越聊圖越盲」的現象？歡迎分享你的觀察與解法 👇

#AI #多模態 #長上下文 #視覺語言模型 #LVLM #上海AI Lab #Qwen3 #模型架構 #PersistentVisualMemory
