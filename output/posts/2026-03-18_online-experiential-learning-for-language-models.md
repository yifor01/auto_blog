---
title: "Online Experiential Learning for Language Models"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2603.16856
score: 115
model: gpt-4o-free
generated_at: 2026-03-18T21:12:02.443824
---

📌 **OEL: 模型邊學**  

傳統語言模型只能靠離線資料進步，但真實部署中的經驗卻被浪費。  
若模型能從自己的使用紀錄中學習，會不會變得更聰明又更省 token？  
Microsoft Research 提出的 OEL 框架試圖讓這成為可能。  

🤔 **離線訓練浪費了真實部署的寶貴經驗**  
現有的改進方式多依賴人工標註或模擬環境的離線訓練，無法利用模型在實際使用中累積的互動軌跡。這意味著寶貴的「體驗知識」被完全忽略。  

🧪 **兩階段迴圈：從使用紀錄萃取經驗，再經 on-policy 條件蒸餾融入模型**  
OEL 包含兩個步驟：首先，從使用者端收到的互動軌跡中抽取可遷移的體驗知識並予以累積；其次，透過 on-policy 條件蒸餾將這些知識編入模型參數，過程不需要再次存取使用者端環境。兩個步驟反覆迭代，形成線上學習迴圈，使改進後的模型能產出更高品質的軌跡，進一步豐富知識庫。  

🚀 **OEL 能在多次迭代中持續提升任務準確度與 token 效率，且不損害分布外表現**  
在多種模型規模以及思考與非思考變體的文字遊戲環境中，OEL 在 successive iterations 中表現出持續的改進：任務準確度提升、所需 token 數降低，同時在分布外（OOD）基準上保持原有水準。  💡 **萃取的經驗知識勝過原始軌跡，且知識來源與模型策略必須保持 on-policy 一致**  
分析顯示，經過萃取的體驗知識對學習的貢獻顯著高於直接使用原始軌跡；此外，知識來源（即產生軌跡的政策）與被更新的模型必須維持 on-policy 一致，這是有效學習的關鍵條件。  

⚠️ **僅在文字遊戲環境驗證，未涉及真實複雜任務或長期部署效果**  
實驗僅基於文字遊戲環境，未覆盤更開放或多模態的真實場景；長期部署後的穩定性與潛在偏差積累仍需後續研究檢視。  

🎯 **工程師可考慮在服務中收集使用軌跡，萃取經驗知識以持續微調模型，但需注意 on-policy 一致性**  
若系統具備記錄使用者互動的能力，可嘗試先抽取高層次的經驗知識（例如成功策略、常見錯誤模式），再以 on-policy 蒸餾方式更新模型。這樣的做法能讓模型隨服務使用而自我改進，同時減少對大規模離線標註的依賴。  

🔗 **論文連結**  
📝 Online Experiential Learning for Language Models  
👤 Tianzhu Ye, Li Dong, Qingxiu Dong, Xun Wu, Shaohan Huang @ Microsoft Research  
🔗 https://arxiv.org/abs/2603.16856  #OEL #LanguageModel #OnlineLearning #MicrosoftResearch #AI #MachineLearning #LLM #ExperientialLearning
