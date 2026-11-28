---
title: 'XNU Linux: Full OS X GUI Userspace on Linux'
source: Hacker News
url: https://github.com/AFK-surf/xnulinux
model: gpt-6.1-terra
generated_at: '2026-11-28T05:51:07.282842'
score: 89
---

📌 用 Linux 核心模組託管 macOS

TL;DR：xnulinux 在 Linux 中載入 XNU，讓 macOS 使用者空間與 Linux 程序並行。

在 Linux 上執行 macOS，未必需要在兩者之間放入 Hypervisor（虛擬機監控器）。xnulinux 的做法是將 XNU 編譯成 Linux 可載入的核心模組，再借用 Linux 提供的硬體與系統資源。

專案 README 指出，這套架構已能啟動 macOS 桌面，並執行 Finder、Safari 等應用程式。不過，它仍有安全機制調整與效能方面的限制。

🧩 **XNU 與 Linux 共用 CPU，由介面模組銜接資源**

xnulinux 從 Apple 公開的原始碼編譯 XNU，將它作為 `xnu.ko` 載入未修改的 arm64 Linux 核心。macOS 程序與 Linux 程序在同一批 CPU 上原生執行，兩者之間沒有 Hypervisor。

其資源銜接方式包括：

- **CPU**：每個受託管的 CPU 對應一條固定在 Linux CPU 上的核心執行緒。XNU 執行至閒置、I/O 或計時器等需要呼叫主機的時機，才交還 Linux。
- **例外處理**：Linux 保留自己的例外向量，由 `fki.ko` 將 XNU 程式碼的錯誤與使用者例外轉交給 XNU 處理。
- **記憶體**：Linux 透過 CMA 提供一塊實體連續記憶體，再由 XNU 自己管理。
- **裝置**：專案提供核心擴充（kext），讓 macOS 使用由 Linux 端提供的磁碟檔案、顯示畫面、輸入裝置、網路及 GPU 等資源。

Linux 端與 XNU 端透過外部核心介面（Foreign Kernel Interface，FKI）銜接，專案也以此分隔兩側的授權。

🧩 **GPU 橋接把 Metal 呼叫導向 Linux 繪圖裝置**

README 描述的圖形路徑是：受託管 macOS 中的 Metal 經由 metal2vulkan 轉成 Vulkan，再透過 DRM 橋接連接 Linux 主機的 GPU。若沒有支援的 DRM 橋接後端，則回退至 Mesa lavapipe，在 CPU 上繪製。

專案狀態列出兩種 arm64 測試環境：Apple Silicon Mac 上的 Linux 虛擬機，以及直接執行 Linux 的 NVIDIA DGX Spark。需注意，前者的 Linux 本身仍執行在虛擬機中；「兩者之間沒有 Hypervisor」指的是受託管的 XNU 與 Linux 之間。

📊 **README 回報可啟動桌面並完成 30 分鐘壓力測試**

在 Apple Silicon Mac 的 arm64 Linux 虛擬機中，README 回報 macOS 27.2.1 自動登入至桌面需時 31–48 秒；同一臺 Mac 上的 Apple Virtualization macOS 虛擬機則為 49 秒。這是專案提供的特定環境測試，不代表所有配置的表現。

README 也指出，一次 30 分鐘壓力測試涵蓋 Safari、Notes、Calculator、TextEdit、System Settings、Spotlight 和磁碟走訪，共執行 40 輪，未出現核心 panic 或當機報告。

🎯 **部署前先準備 macOS 安裝來源與保留記憶體**

專案要求支援 PAC 的 arm64 Linux 主機、4K 記憶體頁面，以及至少 16 GB 記憶體，其中 8 GB 保留給受託管核心。建置系統磁碟與 GPU 元件還需要一臺安裝 Xcode 的 Mac。

儲存庫不包含 Apple 二進位檔；使用者必須自行提供 macOS 安裝、Apple 的 kext、系統磁碟與信任快取。README 列出的主要流程為：

1. 在 Linux 主機執行 `scripts/vm-xnu-build.sh`，建立工具鏈並編譯 XNU。
2. 執行 `scripts/vm-xnu-rebuild.sh`，套用修補並建置核心與 kext；連結核心集合需要指定的 Apple kernelcache。
3. 在 Mac 上執行 `scripts/mk-macvm-disk.sh`，將自己的 macOS VM 磁碟轉換為受託管系統使用的磁碟。
4. 在 Linux 主機執行 `scripts/vm-install-fki-service.sh` 並重新開機，設定記憶體保留區及開機載入 `fki.ko`。
5. 執行 `scripts/xnulinux-boot.sh`，建置模組、設定網路並啟動系統。

專案另提供 `scripts/install-service.sh`，可將系統設定為 systemd 服務。

⚠️ **安全機制已調整，記憶體存取也有代價**

README 列出的權宜措施包括：將 OS cryptex 合併至系統卷宗、修補 AMFI，以及放寬 SIP。此外，作者指出，由於使用 4K 而非 16K 頁面，記憶體存取比原生虛擬機慢。評估部署時，應先確認這些限制是否符合自己的需求。

🔗 **來源**
- 標題：XNU Linux: Full OS X GUI Userspace on Linux
- 作者／機構：mmastrac
- 連結：https://github.com/AFK-surf/xnulinux

#XNU #Linux #macOS #Kernel #ARM64 #KernelModules #GPU #Vulkan #OperatingSystems #OpenSource
