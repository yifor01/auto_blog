---
title: The work by Valve's Timur Kristóf on improving old AMD GPUs on Linux
source: Hacker News
url: https://www.phoronix.com/news/XDC-2026-Valve-Timur-AMDGPU
model: claude-code/sonnet
generated_at: '2026-10-04T20:30:03.518883'
score: 41
---

📌 Valve工程師一人之力,讓十年前的AMD顯卡在Linux重獲新生

TL;DR：Valve的Timur Kristóf靠單人之力把老AMD顯卡從legacy驅動搬上AMDGPU。

當顯卡廠商自己都不想再花資源維護十年前的硬體,一位Valve工程師卻靠著業餘般的熱情,讓這些老卡在2026年依然能跑出不錯的Linux遊戲體驗。

🤔 **被原廠放棄的GCN 1.0/1.1世代顯卡**

根據Phoronix報導,過去一年Valve Linux繪圖驅動團隊的Timur Kristóf對AMDGPU核心驅動程式做出多項重大改進,目標是加強對GCN 1.0/1.1世代(約十年前)AMD顯卡與APU的支援,讓它們能更好地處理Linux遊戲與其他工作負載。這週他在多倫多舉行的XDC2026大會上發表了這項工作的完整歷程。報導指出,AMD本身這些年並未投入太多資源維護這批老舊顯卡的驅動程式,而Kristóf幾乎是一個人扛起了這塊工作。

🧩 **從legacy Radeon驅動遷移到AMDGPU,打開了什麼**

Kristóf原本多年專注於使用者空間的Mesa 3D驅動程式開發,這次則是以核心驅動開發作為新的練習方向。他協助這些老顯卡從舊版的Radeon驅動程式轉移到現代的AMDGPU核心驅動程式,而這個轉移正是能使用RADV Vulkan驅動程式、取得更好效能與更完整功能的關鍵前提。在過程中,他修復了這些老卡在AMDGPU顯示程式碼中的缺陷,處理了多項電源管理問題,並進一步加入軟重置(soft reset)支援等增強功能,讓這些顯卡在2026年及之後都能維持較高的可用性。

📊 **過去改進成果的參考點**

報導提及,去年Linux 6.19曾為這批老AMD Radeon顯卡帶來約30%的效能提升,這正是legacy Radeon驅動轉換到AMDGPU驅動後所帶來效益的一個具體例證。

⚠️ **這項工作的侷限**

文中並未提及這些改進是否會回饋到官方發行版的預設設定,也沒有說明哪些具體型號的APU或顯卡尚未完成轉移,相關細節可參考他在XDC2026上公開的簡報錄影與PDF投影片。

🎯 **對工程師的啟示**

如果你手邊還有GCN 1.0/1.1世代的AMD顯卡(例如用作測試機、二手工作站或低成本的邊緣裝置),這條「legacy Radeon驅動 → AMDGPU → RADV Vulkan」的升級路徑值得留意,可能是延長老舊硬體壽命最務實的方式。這也是開源社群價值的一個範例:當原廠停止投入資源,個別貢獻者仍能靠著長期專注的核心驅動開發,持續把舊硬體的使用體驗往前推進。

🔗 **來源**
- 標題：The work by Valve's Timur Kristóf on improving old AMD GPUs on Linux
- 作者／機構：Michael Larabel, Phoronix
- 連結：https://www.phoronix.com/news/XDC-2026-Valve-Timur-AMDGPU

#Linux #AMDGPU #OpenSource #GPUDriver #Vulkan #RADV #Valve #LinuxGaming #Mesa3D #KernelDevelopment
