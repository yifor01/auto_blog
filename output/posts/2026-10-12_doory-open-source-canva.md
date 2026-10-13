---
title: Doory – Open-Source Canva
source: Hacker News
url: https://github.com/shaongitbd/doory
model: claude-code/sonnet
generated_at: '2026-10-13T00:02:06.040218'
score: 71
---

📌 Doory:能自架的開源 Canva,設計檔案留在自己的伺服器

TL;DR:Doory 是一套可自行架設的開源設計編輯器,功能全免費,三個指令就能跑起整套服務。

付費解鎖模板、浮水印、帳號綁定,是許多線上設計工具的標準套路。Doory 反過來打一張牌:所有功能免費開放,而且你可以把整套系統架在自己的伺服器上,設計檔案完全不離開你的基礎設施。

🤔 解決什麼問題,為誰而做

Doory 是一個跑在瀏覽器裡的完整設計編輯器,可以做海報、社群貼文、限時動態、投影片、邀請卡、履歷、縮圖與名片,支援從範本或空白頁面開始編輯,並匯出成 PNG、JPG、SVG、PDF、MP4 或 GIF。它的定位很明確:給想要「Canva 等級的工具,但開源、免費、自己掌控」的使用者,訪客不需要註冊帳號就能直接開始設計,作品先存在瀏覽器裡,要存雲端再建帳號,一步就能把訪客作品轉移過去。

🧩 架構:前端 React 生態系 + Django 後端 + Docker Compose 一鍵部署

技術棧方面,前端用 React 19、TypeScript、Vite、Fabric.js、Yjs(即時協作用)與 Zustand;後端是 Django 5、Django REST Framework、Channels 與 PostgreSQL;部署則靠 Docker Compose,搭配 nginx、可選的 Redis,以及 S3 相容儲存服務。功能面包含圖層、群組、遮罩、濾鏡、曲線文字、對齊吸附、多頁面設計、27 種進出場動畫、12 種強調動畫、16 種頁面轉場,以及內建 24 首音樂迴圈與 88 個音效素材;協作部分支援可設密碼的分享連結(檢視/留言/編輯權限)、釘選留言、版本歷史與即時多人遊標協作。

🧩 怎麼用:三個指令自架,再用管理指令灌入素材內容

自架流程相當精簡:複製 `.env.example` 為 `.env` 並設定 `DJANGO_SECRET_KEY`、`POSTGRES_PASSWORD`,接著執行 `docker compose up -d --build`,再用 `docker compose exec api python manage.py createsuperuser` 建立管理員帳號,打開 `http://localhost:8080` 就能開始設計。由於是全新站點,素材(範本分類、字型、範本、圖形元素、圖示包、去背模型、音效庫)需要額外用對應的管理指令(如 `seed_gallery`、`sync_fonts`、`seed_templates`、`seed_elements`、`sync_element_packs`、`sync_models`、`sync_audio`)灌入。常見設定項目包括 `SITE_URL`、`DJANGO_ALLOWED_HOSTS`、`SECURE_SSL_REDIRECT`、SMTP 設定、`WEB_PORT`,以及是否啟用 Google 登入或 Unsplash/Pexels 圖庫搜尋的金鑰。

📊 與 Canva 的對照

README 提供的對照表顯示,Doory 和 Canva 都支援即時協作、留言,以及動畫、影片與 GIF 匯出,去背功能 Doory 是在瀏覽器本機端執行模型。差異主要在於:Canva 是免費方案搭配付費 Pro/Teams 方案,Doory 全功能免費;Canva 非開源、不可自架,Doory 兩者都支援;Canva 需要帳號才能設計,Doory 不需要;範本庫方面,Canva 庫更大,Doory 目前隨附 10 個起始範本,可自行在後臺新增。

⚠️ 授權條款需要留意

Doory 採用 Attribution Assurance License,允許使用、修改、再散布甚至商用,但要求保留授權與 NOTICE,並在執行中的應用程式裡明顯標示作者具名,這點在評估是否要用於商業產品前值得先確認清楚。

🎯 實務啟示

如果團隊需要內部設計工具但不想把素材與使用者資料交給第三方 SaaS,Doory 的自架路線和技術棧(Django + React + Docker Compose)對熟悉這套組合的團隊來說上手成本不高;但要注意範本與素材庫是空的,上線前得規劃好內容灌入流程,另外商用時務必遵守具名標示的授權要求。

🔗 來源
- 標題:Doory – Open-Source Canva
- 作者／機構:acley(Hacker News)
- 連結:https://github.com/shaongitbd/doory

#OpenSource #DesignTools #SelfHosted #Canva #React #Django #Docker #WebDev #GraphicDesign #FOSS
