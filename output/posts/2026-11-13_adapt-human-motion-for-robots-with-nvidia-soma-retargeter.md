---
title: Adapt Human Motion for Robots with NVIDIA SOMA Retargeter
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/adapt-human-motion-for-robots-with-nvidia-soma-retargeter/
model: claude-code/sonnet
generated_at: '2026-11-13T22:56:40.925221'
score: 80
---

📌 NVIDIA SOMA Retargeter：把人類動作轉成機器人能走的路

TL;DR：開源工具把動作捕捉或生成的人類動作,轉換成人形機器人可執行的關節軌跡。

教人形機器人走路、揮手,最直覺的方式是「給它看人怎麼動」。但人跟機器人的身體比例、關節結構、活動範圍完全不同,直接複製關節角度只會得到一堆怪異的姿勢。NVIDIA 開源的 SOMA Retargeter,就是專門解決這個「動作重定向」（motion retargeting）問題的工具。

🤔 **人類動作不能直接套用到機器人身上**

人類示範動作捕捉了自然動作背後的協調性與時序,從日常行為到複雜任務都適用。但機器人無法單純複製相同的關節運動,因為機器人的比例、關節結構與活動範圍都不一樣,動作必須經過調整才能套用到機器人身上。SOMA Retargeter 建立在 NVIDIA SOMA-X 共享的人體動作表示法之上,提供設定機器人、修正重定向結果,以及為後續訓練處理動作資料的工具。

🧩 **從 BVH 動作檔到機器人關節軌跡**

人類動作可以來自多種來源：動作捕捉 session、影片、線上資料集,或生成式模型。這些來源輸出的骨架與檔案格式各不相同,因此 SOMA Retargeter 統一以 SOMA 基礎骨架上相容的人類動作作為輸入。

重定向流程讀取基於 SOMA 基礎骨架的 Biovision Hierarchy（BVH）動作檔,將動作目標縮放到機器人的比例,求解關節姿勢,再套用設定好的修正。輸出是一個 CSV 檔,包含機器人在每一幀的根部位置、方向與各關節角度,這些軌跡描述了後續學習或控制系統所需的目標動作。

動作來源方面,素材提到三類：動作捕捉資料（如 BONES-SEED 資料集）、從單一影片重建全身 3D 人類動作（GEM-X,透過 SOMA 身體模型）,以及從文字與姿勢限制生成動作（Kimodo 支援從文字描述生成動作序列,ARDY 則加入互動式引導功能）,兩者皆可在 SOMA 骨架上生成動作。

重定向的求解器使用基於 NVIDIA Warp 建構的 Newton 做反向動力學（inverse kinematics, IK）求解,讓機器人追蹤縮放後的人類動作目標。當機器人無法同時滿足所有目標時,IK 權重決定哪些身體部位優先。實驗性的 IK 權重最佳化工具,可以用一小組具代表性的動作,自動調整這些權重。

SOMA Retargeter v0.2 版本提供了 BONES-SEED 資料集中的範例動作,以及五款人形機器人的參考重定向結果與設定檔：Unitree G1、Unitree H2、Booster T1、AgiBot X2 Ultra 與 AgiBot A3T3,展示了不同機器人因比例與活動範圍差異,呈現出不同的關節角度與落腳位置。

🛠️ **實際怎麼跑：從 BVH 載入到存成 CSV**

安裝好 SOMA Retargeter 後,在 repository 根目錄開啟終端機,執行：
`uv run python app/bvh_to_csv_converter.py --config assets/default_bvh_to_csv_converter_config.json --viewer gl`

這會開啟 BVH to CSV Converter,預設選取 unitree_g1。在 Scene Options 的 Motion 區塊載入 BVH 動作檔後,人類動作會顯示在檢視器中;選擇 Retarget,重定向器就會把來源目標縮放到 G1,針對每一幀求解設定好的 IK 目標,並套用後處理。結果可以用播放控制檢視,最後透過 CSV Motion 的 Save 功能存檔,存檔內容包含機器人在整段動作中的根部姿勢與關節數值。

🧪 **修正細節：參考姿勢對齊與腳步滑動**

文中舉了一個例子：來源動作是單手揮手,但若機器人的參考姿勢沒有對齊,Booster T1 會呈現兩隻手都往外伸的怪異姿態;對齊人類與機器人的參考姿勢後,才會呈現一手揮手、另一手自然垂放的正常動作。這說明參考姿勢對齊對結果的影響很大。

另一個常見問題是腳步滑動：參考動作中腳在移動,但實際動作需要的是腳踩穩不動,這會對下游的動作追蹤策略造成衝突的目標。Foot-plant correction 功能會在偵測到的接觸區間內調整腳部動作,減少這類滑動問題,也可以透過 headless 批次重定向,把調整好的設定重複套用到更大量的動作資料上。

🎯 **重定向之後,還要接上策略訓練**

重定向完成後,動作追蹤策略（motion-tracking policy）會學習如何把這些參考動作轉換成實際的控制動作,同時考慮機器人當下的狀態。SONIC 訓練流程提供了針對 G1 的 SOMA CSV 轉換器,可以把重定向後的軌跡轉成 SONIC 的動作庫格式進行訓練;ProtoMotions 則是另一個基於物理的動作追蹤訓練框架。對 Physical AI 開發者來說,SOMA Retargeter 補上了「人類示範→機器人可用的訓練資料」這段關鍵且常被低估的 pipeline。

🔗 **來源**
- 標題：Adapt Human Motion for Robots with NVIDIA SOMA Retargeter
- 作者／機構：John Malaska @ NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/adapt-human-motion-for-robots-with-nvidia-soma-retargeter/

#NVIDIA #Robotics #HumanoidRobot #MotionRetargeting #PhysicalAI #InverseKinematics #OpenSource #RobotLearning #MotionCapture #Isaac
