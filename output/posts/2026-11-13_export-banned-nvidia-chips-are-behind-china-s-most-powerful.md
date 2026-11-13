---
title: Export-banned Nvidia chips are behind China’s most powerful AI models — uh-oh,
  Jensen!
source: TechCrunch AI
url: https://techcrunch.com/2026/11/13/export-banned-nvidia-chips-are-behind-chinas-most-powerful-ai-models-uh-oh-jensen/
model: claude-code/sonnet
generated_at: '2026-11-13T22:54:45.735463'
score: 82
---

📌 晶片禁運擋不住：中國前沿 AI 模型權重現身 Blackwell 指紋

TL;DR：研究者指出 DeepSeek、Moonshot 等中國開源旗艦模型的權重帶有禁運 Blackwell GPU 的訓練痕跡。

美國對中國實施晶片出口管制，目的是阻止對手拿到最先進的 Nvidia AI 加速晶片，但一份新研究卻聲稱：中國目前最受矚目的開放權重模型，背後訓練用的晶片痕跡恰好吻合被禁運的 Blackwell GPU。

🤔 **出口管制想擋的是晶片，但擋得住流向嗎**

Blackwell GPU 被明令禁止出口到中國或中資企業，而川普政府僅允許較弱的 H200 透過繞道航線出口（並藉此徵收 25% 關稅）。問題在於：晶片一旦離開美國監管視線，要如何確認它最終被誰、在哪裡實際拿來訓練模型？

🧩 **從模型權重結構回推訓練晶片**

前 OpenAI 研究員 Will DePue、現為非營利研究組織 Unemployment Labs 負責人，分析了 DeepSeek、Moonshot AI、MiniMax、Ant Group 公開發布的大型語言模型權重結構，聲稱模型權重仍會反映訓練時所用晶片的配置特徵。他在 Moonshot 的 Kimi K3 系列與 DeepSeek 的 V4 系列模型中找到了與 Blackwell 訓練吻合的「指紋」證據。此前，白宮科技顧問 Michael Kratsios 也曾引述美國情報來源，指稱 Moonshot 使用了被禁運的 Nvidia 晶片。

📊 **兩百萬片晶片，暗渡陳倉**

非營利研究機構 Epoch AI 估計，2024 到 2025 年間，約有兩百萬片先進晶片透過隱藏最終流向的手法進入中國；其中，約 275,000 片 Nvidia AI 加速器在同期間經由馬來西亞進口，使當地成為繞過管制的熱點，也帶動了一波資料中心建設潮。另外，據報約有 60 萬片 H200 晶片目前囤積在香港，等待進入中國市場。

💡 **晶片在境外資料中心合法使用，算不算違規？**

這些晶片是否被用於違反出口管制的直接訓練，目前並無定論——它們也可能是透過境外資料中心（如馬來西亞）合法取得使用權。但這恰恰是出口管制設計上的灰色地帶：管制聚焦在晶片的「所有權」與「所在地」，而非「實際使用者」。長期關注中美科技政策的研究者因此主張，只要人能繞到境外去用，單純限制晶片進入中國境內並無實質意義。這起事件也與 Nvidia CEO Jensen Huang 本週因與 Megaspeed 高層 Alice Huang 的私人關係而離職有關——Alice Huang 所涉及的公司被指控協助晶片走私，且被指為中國情報人員，Nvidia 因而面臨潛在的出口管制合規責任追究，美國商務部長 Howard Lutnick 的監管失察也同時受到檢視。

⚠️ **鑑識方法本身細節有限，不宜過度解讀**

本篇報導混雜了企業人事與地緣政治爭議，對「權重指紋鑑識」方法的技術細節說明有限，也未能確認這些模型是否完全在禁運晶片上訓練，或是否確實違反出口法規，相關指控目前仍待政府調查證實。

🎯 **對模型選型與供應鏈評估的提醒**

對需要評估開源模型來源與合規風險的工程團隊而言，這提醒了一件事：模型能力的審查正在延伸到訓練基礎設施層級的鑑識分析。未來可能出現更多類似的「weight fingerprinting」工具，用來推斷訓練所用的硬體與供應鏈，這是在評估開源模型時可以留意的新維度。

🔗 來源
- 標題：Export-banned Nvidia chips are behind China's most powerful AI models — uh-oh, Jensen!
- 作者／機構：Tim Fernholz, TechCrunch
- 連結：https://techcrunch.com/2026/11/13/export-banned-nvidia-chips-are-behind-chinas-most-powerful-ai-models-uh-oh-jensen/

#Nvidia #AIChips #ExportControls #China #DeepSeek #MoonshotAI #Blackwell #GPU #Geopolitics #AIHardware
