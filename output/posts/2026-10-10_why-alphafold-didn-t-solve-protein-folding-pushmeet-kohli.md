---
title: Why AlphaFold Didn't Solve Protein Folding — Pushmeet Kohli, Google DeepMind
  & Sal Candido, Biohub
source: Latent Space
url: https://www.latent.space/p/biohub-deepmind
model: claude-code/sonnet
generated_at: '2026-10-10T20:47:30.117938'
score: 78
---

📌 Google DeepMind × Biohub 對談：AlphaFold 其實沒解決蛋白質摺疊問題

TL;DR：DeepMind 的 Pushmeet Kohli 與 Biohub 的 Sal Candido 在 Latent Space 專題對談中指出，AlphaFold 只解開了靜態結構預測，蛋白質動態、設計與全細胞建模仍是未竟之業。

AlphaFold 拿下諾貝爾化學獎、被譽為結構生物學的里程碑，但如果你問兩位真正在第一線做蛋白質 AI 的研究者「蛋白質摺疊問題解決了嗎？」，得到的答案居然是「還沒」。這場由 Brandon Anderson 主持的對談，把這個反直覺的結論拆解得相當細。

🤔 **資料界也有「苦澀的教訓」嗎？**

主持人開場就拋出一個改寫版的 Bitter Lesson：如果 Rich Sutton 說「能夠規模化的方法終將勝出」，那麼資料是否也存在同樣的規律？Sal Candido 的回答很務實：scaling law 不是處處都有，真正的工作是先找出「放更多運算、更多資料進去,就能得到更好結果」的那個情境,一旦找到,問題就變成工程問題,可以「轉動把手」持續優化。但前提是資料本身要帶有解決目標問題所需的資訊與統計特性，否則模型終究無法超越資料本身去泛化。

🧩 **低品質的 metagenomic 資料,反而讓蛋白質語言模型更強**

Sal 坦承自己做研究傾向「挑現成資料來用」,這有好有壞。壞處是容易導向「什麼資料好生成就規模化什麼資料」的懶惰路線;好處則是常有意外收穫——他舉例,用 metagenomic 序列(很多甚至不是完整、真實的蛋白質)訓練蛋白質語言模型,結果卻提升了模型在設計真實可用蛋白質、理解已知蛋白質上的表現。他認為真正該問的問題不是「有什麼資料」,而是「解決這個問題到底需要什麼資料」,這也是 Biohub 強調社群開放協作的原因:只有建模者、資料生成者和科學社群一起工作,才能真正定義出需要的資料,進而找到對的 scaling law。

Pushmeet Kohli 則從 DeepMind 內部視角回應:他當年在 DeepMind 聽 Rich Sutton 親自講這堂課時,體會到的重點並非「資料是否有用」這種具體層面的問題,而是更概念性、更根本的東西。

💡 **AlphaFold 到底還沒解決什麼**

根據節目議程,兩人進一步談到 AlphaFold 手工設計的架構與科學直覺在其中的角色,以及「好資料勝過單純堆資料量」的設計哲學。更關鍵的是,對談明確點出 AlphaFold 並未真正解決整個蛋白質摺疊問題——靜態結構預測只是故事的一部分,蛋白質的動態行為(dynamics)、無序區域(disorder)都還在靜態結構預測的能力範圍之外。節目也提到 cryo-EM 顯微影像可能是解鎖更豐富生物表徵的下一個入口,以及建模視角需要從「單一蛋白質」擴展到「完整生物系統」,這正是打造 virtual cell(虛擬細胞)的核心挑戰。

此外議程也涵蓋了蛋白質語言模型中可能藏有尚未被解鎖的科學知識、可信度與不確定性校準為何比完全可解釋性更重要,以及未來前沿模型是否可能比人類更擅長理解其他 AI 系統等議題。

🎯 **對 AI 研究者的啟示**

這場對談給做生物 AI 的工程師一個提醒:盲目堆大模型、堆算力不是終點,找到「對的 scaling law」與「對的資料」才是真正的工程槓桿。而像 Biohub 這樣強調「以社群協作定義需求、而非被現有資料牽著走」的做法,也值得其他領域的 AI 團隊借鏡。

🔗 **來源**
- 標題：Why AlphaFold Didn't Solve Protein Folding — Pushmeet Kohli, Google DeepMind & Sal Candido, Biohub
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/biohub-deepmind

#AlphaFold #ProteinFolding #GoogleDeepMind #Biohub #ScalingLaws #BitterLesson #ProteinLanguageModel #VirtualCell #AIforScience #DrugDiscovery
