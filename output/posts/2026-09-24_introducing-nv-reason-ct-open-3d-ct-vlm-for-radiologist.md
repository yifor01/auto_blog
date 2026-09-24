---
title: Introducing NV-Reason-CT Open 3D CT VLM for Radiologist Chain-of-Thought Reasoning
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/introducing-nv-reason-ct-open-3d-ct-vlm-for-radiologist-chain-of-thought-reasoning/
model: claude-code/sonnet
generated_at: '2026-09-24T20:38:55.116479'
score: 97
---

📌 NVIDIA 開源 NV-Reason-CT：3D CT 也能思維鏈推理

TL;DR：NVIDIA 釋出開源 3D CT 視覺語言模型，模仿放射科醫師逐步推理，支援多輪追問。

放射科 AI 在胸部 X 光、病理切片、2D 影像上早已進展神速，但臨床資訊量最大、也最複雜的模態——3D 電腦斷層（CT）——長期以來卻是現有視覺語言模型（VLM）的弱項。NVIDIA 這次推出的 NV-Reason-CT，正是要補上這塊拼圖。

🤔 為什麼 3D CT 需要不一樣的做法

一份腹部 CT 檢查可能包含 300 到 600 張軸位切片，橫跨三個空間維度編碼解剖結構資訊；標準的 2D 編碼器如果把 CT 當成一疊獨立 2D 影像逐張處理，就會丟失切片之間的空間關係，而腫塊、積液、浸潤這類結構的形狀、範圍與密度，恰恰只有在三維空間中才有臨床意義。這帶來三重複合挑戰：

- 感知層面：通用 VLM 把輸入當成 2D token 網格，無法從獨立切片重建 3D 空間關係。
- 推理層面：即使模型正確感知到異常，也常常只輸出一個診斷標籤而不說明理由。放射科醫師思考時不是靠標籤，而是系統性的解剖回顧、鑑別診斷與信心程度判斷；無法重現這個推理過程的 AI，難以被稽核、難以作為教學工具，也難以安全整合進臨床流程。
- 對話深度層面：放射科醫師看到可疑發現時不會就此結案，而是會追問、重新考慮鑑別診斷、跨解剖區域交叉比對。多數現有模型缺乏支援這種迭代式臨床推理的多輪對話能力。

NV-Reason-CT 延續了 NV-Reason-CXR 所開創的推理方法論——後者已在一項獲 RSNA 2026 接受的多讀者臨床研究中，驗證了能節省放射科醫師閱片時間，同時維持診斷準確度。需要強調的是，官方明確定位 NV-Reason-CT 是開放的研究與開發基礎模型，並非自主診斷系統或已通過認證的臨床產品，目標使用者是要在此基礎上做後訓練、打造專屬 CT 分析應用的研究者與開發者。

🧩 全 3D ViT 編碼器 + 3D MRoPE

NV-Reason-CT 結合一個專為 3D CT 打造的全 3D vision transformer（ViT）編碼器，以及一個經過訓練、能模仿放射科醫師系統性分析流程產生思維鏈（chain-of-thought）的語言模型。與把切片各自獨立處理再拼接的做法不同，NV-Reason-CT 把整個 CT volume 當作真正的 3D 輸入處理，保留切片之間的解剖連續性，讓模型能像醫師逐張捲動閱片一樣，整體性地推理結構。

核心能力包括：
- 結構化報告生成：NVIDIA 團隊整理了一套涵蓋 30 種胸部異常與 29 種腹部異常的 CT ontology（如肺結節、氣胸、肝臟病灶、腎囊腫等），用來引導與評估模型輸出，格式貼近臨床文件流程。
- 模仿放射科醫師的思維鏈：模型會產生逐步的內部思考過程，系統性檢視各解剖區域、浮現相關發現、考慮鑑別診斷，並表達不確定性，風格類似資深放射科醫師的閱片過程。
- 多步驟對話追問：使用者可以針對特定發現追問、要求釐清鑑別診斷，或在任何階段追問模型的推理依據，讓模型從單純的報告產生器變成互動式診斷夥伴。

架構上，NV-Reason-CT 把 Qwen3.5-4B 語言模型與 3D ViT（架構基於 Primus，並以 Colipri 權重初始化）結合，所有權重都在大規模 CT 資料上端到端重新訓練，資料含結構化報告、推理軌跡與多步驟 VQA。CT volume 會先被重採樣到 192³ 體素、2mm 等向解析度，切成不重疊的 8x8x8 patch token，產生 24x24x24 = 13,824 個視覺 token；這些視覺 token 不經過合併或降維，連同各自的 3D 網格座標一起完整送進語言模型，模型內建 3D MRoPE 來處理視覺 token 之間的三維空間關係。語言模型被訓練成「像老師一樣解釋問題」，而非單純輸出分類結果：系統性檢視各解剖區域、同時記錄正常與異常發現、表達校準過的不確定性，最後給出結構化結論。

🧩 兩階段訓練：SFT 打底、GRPO 精修

訓練沿用 NV-Reason-CXR 建立的兩階段流程：

第一階段（監督式微調）：訓練資料混合了結構化報告、專家放射科醫師的推理標註，以及一般 VQA。放射科醫師提供了詳細的思維鏈口述，捕捉他們檢視每個解剖區域時的實際思考過程——看什麼、認為哪些發現重要、權衡哪些鑑別診斷、如何得出最終結論。整體訓練資料集涵蓋約 55 萬筆結構化 QA 範例，橫跨胸部與腹部區域，包含解剖分區層級 QA、側邊與局部發現 QA、嚴重程度 QA，以及二元異常判定 QA，並加入針對無效提示與圖文不匹配情境的拒答範例以提升穩健性。訓練資料來源包括 CT-RATE、NIH CT 資料集與 CancerVerse，並輔以從大型語言模型蒸餾、以專家標註為基準的高品質合成推理資料。

第二階段（強化學習）：使用 Group Relative Policy Optimization（GRPO）進一步精修推理品質。

🎯 實務啟示

對於想投入醫學影像 AI 的團隊，NV-Reason-CT 提供了一個少見的開放起點：不只是分類器，而是帶有完整思維鏈與多輪對話能力的 3D CT 基礎模型，且明確定位為可後訓練的研究基礎，而非可直接上線的臨床產品。若你的應用場景需要「可被稽核的推理過程」而不只是一個診斷標籤，這類架構思路（3D 原生編碼、思維鏈監督資料、SFT+RL 兩階段訓練）值得參考；但落地前務必留意，官方尚未在文中提供 NV-Reason-CT 本身於 3D CT 任務上的量化評估數據，RSNA 2026 的臨床驗證是針對前作 NV-Reason-CXR（胸部 X 光），不能直接等同於 CT 版本的臨床表現。

🔗 來源
- 標題：Introducing NV-Reason-CT Open 3D CT VLM for Radiologist Chain-of-Thought Reasoning
- 作者／機構：Tanya Lenz，NVIDIA
- 連結：https://developer.nvidia.com/blog/introducing-nv-reason-ct-open-3d-ct-vlm-for-radiologist-chain-of-thought-reasoning/

#MedicalAI #VLM #ChainOfThought #NVIDIA #Radiology #3DImaging #GRPO #OpenSourceAI #HealthcareAI #FoundationModel
