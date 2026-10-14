---
title: Google DeepMind and Singapore Government collaborate to build fine-tuned AI
  model for scam detection
source: Google DeepMind
url: https://deepmind.google/blog/on-device-ai-scam-detection-mddi/
model: claude-code/sonnet
generated_at: '2026-10-14T20:50:10.157930'
pinned: true
---

📌 【Google DeepMind】新加坡打造裝置端詐騙偵測 AI

TL;DR：DeepMind 與新加坡政府微調 Gemma 模型,在手機上即時偵測詐騙且不上雲。

🎣 詐騙已佔新加坡所有報案犯罪的一半以上,而且越來越難防：攻擊者不再靠粗糙的釣魚訊息,而是先用一段看似正常的對話建立信任,再伺機要錢。Google DeepMind 選擇用一個反直覺的方式應對——讓 AI 偵測模型完全跑在手機裡,連政府和 Google 自己都看不到對話內容。

🤔 詐騙手法已經進化成社會工程

根據 Google DeepMind 的部落格,投資詐騙、假工作邀約、冒充公職人員等詐騙類型,佔新加坡報案犯罪的一半以上,自 2019 年以來造成超過新加坡幣 40 億元的損失。這類利用對話逐步操控受害者的社會工程手法,如今佔所有詐騙損失的比例最高達 80%。作為 Google DeepMind 與新加坡政府「National AI Partnership」的一環,DeepMind 與新加坡政府科技局（GovTech Singapore）合作,微調出一套具隱私保護特性、可在裝置端運行的詐騙偵測模型。

🧩 為什麼要搬到裝置端

通用型模型往往難以辨識在地化的詐騙話術,這是促使團隊微調模型的原因。團隊以 Google 的輕量模型 Gemma 為基礎,用在地詐騙對話進行微調,涵蓋冒充公家機構、銀行、地方人物,以及當下流行的區域詐騙手法,讓模型能分辨「一般閒聊」與「真正的操控意圖」。與傳統依賴伺服器端雲端掃描訊息的威脅偵測方式不同,這套模型直接在裝置上處理對話資料,能更快分析對話模式、在使用者金錢或帳密曝險之前發出警示。導入會與新加坡政府分階段合作推行,且模型只會在使用者同意、並依照所屬應用程式使用條款的前提下,存取裝置端的對話內容；由於模型完全在裝置上運行,新加坡政府與 Google 都無法透過此部署存取使用者的對話。GovTech Singapore 信任與安全總監 Mark Chen 表示,打擊詐騙不該以犧牲個人隱私為代價,與 Google DeepMind 合作把進階 AI 防護直接帶到公民的裝置上,讓團隊能即時攔截高度針對性的在地詐騙嘗試,同時保持個人通訊的私密性。

📊 兩階段的運算管線

在現代智慧型手機上跑一個複雜的詐騙分類模型並不容易,電池續航是主要考量。團隊因此設計了兩階段管線：第一階段由一個輕量、低耗能的分類器篩選收到的訊息,專注於抓出潛在威脅；第二階段則由微調後的 Gemma 模型對更大範圍的對話片段做情境分析,確認是真正的威脅還是誤判。當模型偵測到帶有操控性的對話模式時,會直接在使用者裝置上觸發即時警示,提醒使用者在分享敏感資訊或資金前先暫停並保持警覺。

⚠️ 開發過程的治理機制

這項合作在新加坡國際網路週（SICW 2026）上公開,團隊強調整個開發過程遵循嚴格治理：微調作業在 GovTech Singapore 自行管理維護的 GCP 環境（「Sovereign Sandbox」）中進行,訓練資料保持隔離；訓練資料嚴格排除任何私人或可識別個人身分的資訊,僅使用源自詐騙報告與情資來源的匿名化資料集；模型也針對合成對話與在地語料做壓力測試,以涵蓋多樣的詐騙類型與不斷演變的冒充手法。

🎯 實務啟示

這個案例示範了一種「模型能力下放到終端」的務實路線：當隱私與安全防護看起來互斥時,用小型微調模型 + 裝置端推論的架構,是個值得參考的折衷方案,尤其適合做端對端加密通訊平臺上的風險偵測。對正在評估輕量模型微調專案的團隊,這也是一個 Gemma 這類開源權重模型在真實政府級場景落地的具體範例。Google DeepMind 表示未來會分享更多合作細節,並評估將類似技術部署到其他國家的可能性。

🔗 來源
- 標題：Google DeepMind and Singapore Government collaborate to build fine-tuned AI model for scam detection
- 作者／機構：Google DeepMind
- 連結：https://deepmind.google/blog/on-device-ai-scam-detection-mddi/

#GoogleDeepMind #Gemma #OnDeviceAI #ScamDetection #AISafety #Privacy #Singapore #GovTech #EdgeAI #ResponsibleAI
