---
title: "OmniLiDAR: A Unified Diffusion Framework for Multi-Domain 3D LiDAR Generation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.13815
score: 118
model: tencent/hy3-preview:free
generated_at: 2026-05-14T20:27:53.053698
---

📌 **OmniLiDAR：統一擴散生成多域 LiDAR 掃描**  

你以為 LiDAR 資料只能靠真實採集？一個模型竟能跨天氣、感測器與平台生成高品質掃描。  

🤔 **多域 LiDAR 資料稀缺，單一模型難以應對天氣與感測器變化**  
在擴展模擬與合成資料時，不同惡劣天氣、感測器束數減少或載具類型（車輛、無人機、四足機械）會導致資料分布顯著偏移。傳統擴散模型往往只在單一域上訓練，需要為每種條件維護獨立模型，難以實現統一、可控的合成。  

🧪 **八個域混合訓練的跨域擴散框架**  
OmniLiDAR 採用共享的範圍影像表示，將八個代表性域（三類偏移：惡劣天氣、感測器配置變化、跨平台採樣）納入同一訓練流程。Cross‑Domain Training Strategy (CDTS) 在每個 mini‑batch 中混合不同域的樣本，並利用文字條件引導生成。為了捕捉範圍影像在方位角與仰角上的各向異性結構，提出 Cross‑Domain Feature Modeling (CDFM)；同時設計 Domain‑Adaptive Feature Scaling (DAFS) 作為輕量調制，以在去噪過程中補償域依賴的特徵偏移。  

📊 **統一模型在多域生成與下游任務上皆顯著提升**  
在自建的 8 個域資料集（結合真實掃描、基於物理的天氣模擬與系統性束數減少）上的實驗顯示，OmniLiDAR 能產生高保真度的 LiDAR 掃描。進一步的下游評估表明，使用其生成資料進行資料增強可提升 LiDAR 語意分割與 3D 物體偵測的表現，尤其在標籤有限的情況下獲得明顯好處；同時在腐敗 robustness 測試中也展現穩定的改善。  

💡 **跨域特徵建模與自適應縮放如何捕捉掃描各向異性**  
CDFM 明確建模了方位角與仰角方向上的特徵依賴，使模型能夠學習到 LiDAR 掃描固有的非各向同性結構。DAFS 則在每個去噪步驟上根據當前域的統計特性進行微調，避免因域間特徵漂移導致生成品質下降。兩者的結合使單一模型在面對異質分布偏移時仍能保持一致的生成品質。  

⚠️ **僅合成資料基準，真實極端條件尚未驗證**  
研究所使用的 8 個域資料集包含真實掃描與模擬天氣/束數變化，但未在實際極端惡劣環境或未見過的感測器配置上進行驗證。長期穩定性與真實世界部署的適用性仍需後續工作補充。  

🎯 **可用於標籤稀少的 LiDAR 任務資料增強**  
OmniLiDAR 提供了一種在多種感測條件下統一合成 LiDAR 數據的途徑，適合資料標記成本高、標籤稀少的場景。研究團隊已發布資料集與程式碼，供 CV 與機器人領域研究者直接用於可控 3D 生成與模擬資料管線。  

🔗 **論文連結**  
📝 OmniLiDAR: A Unified Diffusion Framework for Multi-Domain 3D LiDAR Generation  
👤 Youquan Liu, Weidong Yang, Ao Liang, Xiang Xu, Lingdong Kong (Fudan University; National University of Singapore; Nanjing University of Aeronautics and Astronautics; Technical University of Munich; Nanjing University of Science and Technology; Shanghai AI Laboratory; University of Sydney; The Chinese University of Hong Kong)  
🔗 https://arxiv.org/abs/2605.13815  

#OmniLiDAR #LiDAR #DiffusionModel #3DGeneration #CVPR2025 #Fudan #NUS #NUAA #TUM #SAIL #USYD #CUHK #資料增強 #自動駕駛 #機器人視覺
