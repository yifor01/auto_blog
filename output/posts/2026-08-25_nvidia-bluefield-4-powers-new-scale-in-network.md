---
title: NVIDIA BlueField-4 Powers New Scale-In Network Infrastructure for Agentic AI
  Factories
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/nvidia-bluefield-4-powers-new-scale-in-network-infrastructure-for-agentic-ai-factories/
model: claude-code/sonnet
generated_at: '2026-08-25T06:23:14.516266'
score: 95
---

📌 【NVIDIA 最新架構】BlueField-4 領軍 Scale-In，AI 工廠多了第五道網路支柱

TL;DR：BlueField-4 打造 Scale-In 網路，把安全與資料存取從主機 CPU 卸載出來，撐住 agentic AI 工廠的規模化需求。

當 GPU 算力以指數速度堆疊，如果安全檢查、租戶隔離與資料存取還得靠通用主機 CPU 硬撐，這些看似「配角」的基礎設施，很可能才是拖垮整座 AI 工廠效能的隱形瓶頸。

🤔 **傳統雲端網路，撐不住 agentic AI 的規模**

傳統雲端資料中心的 north-south network（連接使用者、應用程式、資料來源、儲存系統到單一系統的存取路徑）是圍繞「軟體定義、可組合、可彈性擴展」的設計理念打造的。但 agentic AI 工廠把大量加速運算，與持續成長的使用者、agent、應用程式、企業資料來源、儲存系統綁在一起，並要求它們不斷互動。軟體定義網路依然必要，但已經不足夠：安全性、多租戶網路、資料與儲存存取、維運，不能再各自獨立運作或單靠主機 CPU 上的軟體處理，必須整合成統一的基礎設施網域。

🧩 **AI networking 的第五支柱**

NVIDIA 將 AI 網路架構分成五個支柱：Scale-Up（NVLink 統一 GPU 為單一加速器）、Scale-Out（Spectrum-X Ethernet 與 Quantum InfiniBand 跨伺服器連接）、Scale-Across（Spectrum-XGS Ethernet 連接分散式 AI 工廠）、Context Memory（CMX，提供工廠內共享的 KV-cache 儲存）,以及新加入的 Scale-In。Scale-In 由 BlueField-4、DOCA、Spectrum-X Ethernet 組成，負責加速圍繞運算周邊的存取、安全、資料搬移與基礎設施維運。

在 NVIDIA Vera Rubin NVL72 中，ConnectX-9 SuperNIC 負責在 Scale-Out 網路上傳輸租戶工作負載流量，而 BlueField-4 則獨立於主機之外，執行並加速連接、安全、管理每臺伺服器所需的基礎設施服務，讓維運者能在不佔用主機 CPU 資源的情況下管理安全政策、服務狀態與遙測。NVIDIA BlueField Astra 進一步把這種可信任的控制延伸到 east-west 的 Scale-Out fabric：BlueField-4 負責安裝與更新政策、監控遙測，ConnectX-9 則直接在資料路徑上落地執行這些政策，形成一個不依賴租戶主機的閉環控制。

🧩 **控制平面與資料平面分工**

BlueField-4 將可程式化的控制平面處理與加速資料平面處理結合：軟體負責決策，內建的加速引擎則就地執行，不需把工作交回主機 CPU。根據素材提供的元件表：64 核心 NVIDIA Grace CPU 負責政策、佈建、遙測與基礎設施協調軟體，相比前代提供 6 倍運算力；內建加速引擎處理封包、RDMA、儲存協定、加密、防火牆規則與政策執行，最高可達 800 Gb/s；LPDDR5X 記憶體子系統提供資料與服務狀態存取所需的高頻寬；PCIe Gen6 連接主機伺服器；800 Gb/s 網路介面則連接 Scale-In fabric。

📊 **對比前代：頻寬全面提升**

相較 BlueField-3，BlueField-4 提供 4 倍記憶體頻寬與 2 倍網路頻寬。

🎯 **實務啟示**

對正在建置或營運多租戶 AI 基礎設施的工程團隊而言，Scale-In 傳達的核心訊息是：擴充 GPU、機櫃、資料中心只有在資料存取、儲存、資安與維運能同步擴展時才有價值。若團隊已在規劃大規模 agentic AI 部署，值得評估將安全與基礎設施服務從主機 CPU 卸載到獨立處理網域，是否能減少維運與資安在算力擴張時成為瓶頸的風險。

🔗 **來源**
- 標題：NVIDIA BlueField-4 Powers New Scale-In Network Infrastructure for Agentic AI Factories
- 作者／機構：Michelle Horton（NVIDIA Developer）
- 連結：https://developer.nvidia.com/blog/nvidia-bluefield-4-powers-new-scale-in-network-infrastructure-for-agentic-ai-factories/

#NVIDIA #BlueField #AgenticAI #DataCenterNetworking #DPU #SpectrumX #AIInfrastructure #Ethernet #ScaleIn #AIFactory
