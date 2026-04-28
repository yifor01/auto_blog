---
title: "TextGround4M: A Prompt-Aligned Dataset for Layout-Aware Text Rendering"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2604.24459
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-04-28T20:39:24.387549
---

📌 【Microsoft Research 等】TextGround4M：4M 規模的 prompt-aligned layout-grounded 資料集，解決文生圖文字排版難題  

你有試過讓 AI 生成海報、廣告或 UI 時，文字總是跑版、重疊或與提示詞不符嗎？這不只是視覺上的瑕疵，更影響設計的可用性與品牌一致性。  

🤔 **現有文生圖模型難以精準呈現提示詞中的文字排版**  
儘管近年文字到圖像（T2I）模型在生成逼真圖像方面取得長足進步，但在需要精確控制多段文字、表格或結構化排版的場景中，模型仍常忽略提示詞中指定的文字位置與大小。問題的根源在於缺乏能將提示詞內容與圖像中文字逐個標註的大規模資料集，亦缺少專門衡量空間排版的評估指標。  

🧪 **建構 4M 筆 span-level 文字標註資料集與輕量訓練策略**  
研究團隊從 Central South University、Zhejiang University 與 Microsoft Research 合作，針對以上兩個缺口提出 TextGround4M。該資料集包含超過 400 萬個 prompt‑image 配對，每筆資料均以 span 為單位標註提示詞中的文字，並給出對應的 bounding box，實現文字與位置的細粒度對齊。在此基礎上，他們設計了一種輕量訓練方式：在自回歸 T2I 模型的訓練過程中，只需將 layout‑aware span token 附加在輸入序列末尾，不改變模型結構也不影響推論行為。為了評估不同模型在零射擊情境下的表現，團隊進一步建立了一個依照 layout 複雜度分層的基準，並提出兩個新的 layout‑aware 評估指標來量測空間排版的品質。  

💡 **使用 TextGround4M 訓練的模型在文字忠誠度與空間準確度上顯著優於基線**  
實驗結果顯示，採用該資料集進行訓練的開源與專有模型，在文字忠誠度（文字內容是否與提示詞一致）、空間準確度（文字位置與尺寸是否符合標註）以及提示詞一致性方面，均顯著超越未使用細粒度 layout 監督的強基線。特別是在多跨度、結構化排版的測試樣本中，改善幅度最為明顯，證實了精細 layout 監督對提升可控文字渲染的關鍵作用。  

💡 **細粒度 layout 監督讓模型學會遵循提示詞中的文字位置與格式**  
進一步分析發現，模型在訓練時接收到的 layout‑aware span token 提供了明確的空間約束，使其在生成過程中能更好地將文字放置於提示詞所指定的區域，而不僅僅是生成文字內容。這種「先理解位置，再渲染文字」的機制，降低了模型對文字與布局之間衝突的依賴，從而在複雜排版場景中保持更高的準確度。  

⚠️ **資料集主要來源於合成圖像，真實設計場景的泛化能力尚待驗證**  
目前 TextGround4M 的圖像多由合成引擎生成，雖然標註精細，但其在真實海報、品牌手冊或 UI 截圖等實際設計資料上的表現仍需進一步驗證。此外，資料集的標註集中在英文與少數常見語言，其他語系的覆蓋度有待擴充。  

🎯 **工程團隊可直接使用此資料集與評估指標提升 UI、廣告等場景的文字排版控制**  
對於需要精準文字排版的產品團隊，TextGround4M 提供了可立即下訓練的大規模資料集與兩個 layout‑aware 評估指標，可用於快速檢驗模型在特定排版任務上的表現。輕量的訓練策略亦意味著無需重新設計模型架構，即可在現有 T2I 系統上獲得顯著的排版品質提升，適合用於廣告素材自動生成、介面原型製作以及文件排版自動化等應用。  

🔗 **論文連結**  
📝 TextGround4M: A Prompt-Aligned Dataset for Layout-Aware Text Rendering  
👤 Dongxing Mao, Yilin Wang, Linjie Li, Zhengyuan Yang, Alex Jinpeng Wang (Central South University; Zhejiang University; Microsoft Research)  
🔗 論文：https://arxiv.org/abs/2604.24459  

如果你正在開發需要精準文字排版的生成式 AI 功能，這份資料集與評估方法或許能讓你的模型在實際設計場景中更加得心應手。歡迎在留言區分享你的經驗或想法！  

#AI #TextToImage #LayoutAware #MicrosoftResearch #CVPR #生成式模型 #UI設計 #廣告生成
