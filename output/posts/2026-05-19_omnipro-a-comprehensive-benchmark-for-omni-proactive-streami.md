---
title: "OmniPro: A Comprehensive Benchmark for Omni-Proactive Streaming Video Understanding"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.18577
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-05-19T20:59:39.707380
---

📌 **OmniPro 基準：全模態主動影片理解**

你以為 AI 已經能看懂長影片？實際上，它可能只聽見一半的聲音，且隨時間越來越笨。

🤔 **現有基準只看畫面，忽略聲音與主動性**  
既有評測多依賴視覺訊息、採用輪詢或固定時間點，無法真正衡量模型在連續音訊‑影像流中何時該發聲、該說什麼。

🧪 **2,700 人工標註樣本，涵蓋 9 子任務與 3 認知層次**  
OmniPro 提供 2,700 經人工驗證的樣本，橫跨 9 個子任務、3 個認知難度，涵蓋 6 種基本影片理解能力；84% 的樣本需要音訊（語音或非語音），每筆資料都標註了模態隔離標籤，以便細部多模態分析。

🔬 **雙模式評估：Probe 與 Online**  
- **Probe mode**：在每個真實觸發點前後查詢模型，測量對內容的理解程度。  
- **Online mode**：要求模型在串流輸入中自主決定何時回應，完整評估主動反應能力。

📊 **音訊帶來提升但利用不穩，隨時間衰退，非語聲音最弱**  
評測 11 種代表模型後發現：  
1. 音訊對性能有正面貢獻，但各模型利用程度差異極大。  
2. 隨著串流時間增加，顯著下降，顯示長時域穩健性不足。  
3. 對非語音音訊的感知是所有維度中最薄弱的環節。

💡 **模型對聲音的依賴度不一，顯示主動理解仍缺乏長期穩健性**  
結果說明，即使模型能從音訊中獲益，卻缺乏一致且持久的利用機制；尤其在需要辨識背景聲音或環境音時，表現尤為不足。

⚠️ **僅評估有限數量模型，且未探索不同架構對音訊利用的具體機制**  
基準目前僅涵蓋 11 個代表模型，未深入分析導致音訊利用差異的架構或訓練差異；此外，評估基於靜態樣本，無法直接反映真實串流中的延遲與計算成本。

🎯 **開發主動式影片 AI 應該平衡聲音利用與長期穩定性**  
- 在模型設計時，應該顯式訓練對語音與非語音音訊的敏感度。  
- 評估時納入長時域序列，觀察性能衰退趨勢，以改善穩健性。  
- 考慮在訓練目標中加入主動決策的成本函數，鼓勵模型在適當時機發聲而非過度依賴輪詢查詢。

🔗 **論文連結**  
📝 OmniPro: A Comprehensive Benchmark for Omni-Proactive Streaming Video Understanding  
👤 Ruixiang Zhao, Jie Yang, Zijie Xin, Tianyi Wang, Fengyun Rao (Renmin University of China; WeChat Vision, Tencent Inc.)  
🔗 https://arxiv.org/abs/2605.18577  

你認為在開發主動式影片助手時，哪一方面最值得優先改進？歡迎在留言區分享你的見解 👇  

#OmniPro #多模態AI #影片理解 #基準評估 #Tencent #RenminUniversity #AI研究
