---
title: OpenAI, Google pushing new AI models easily tricked into making nudes, researchers
  say
source: Ars Technica AI
url: https://arstechnica.com/tech-policy/2026/10/openai-google-pushing-new-ai-models-easily-tricked-into-making-nudes-researchers-say/
model: claude-code/sonnet
generated_at: '2026-10-14T21:09:34.704064'
score: 76
---

📌 紅隊測試：OpenAI、Google新一代生圖模型，防護仍可被簡單繞過

TL;DR：White Circle紅隊測試顯示，DALL·E 3、Nano Banana 2、GPT-Image-2的安全過濾器仍可被現成工具繞過，產生情色圖像。

模型愈強大，防護理應愈周全才合理。但多位安全研究者的最新紅隊測試卻指出，Google與OpenAI最新一代的圖像生成模型，在阻擋情色輸出這件事上，可能反而不比舊版本可靠。

🤔 **色情深偽內容持續擴散，源頭工具才是關鍵防線**

Google共同撰寫的一份研究，在今年7月調查了美國、澳洲、英國的網路使用者,發現未經同意的AI生成情色內容，常透過文字訊息、私訊分享,或存放在私人雲端空間,因此較不容易被偵測或舉報。Google研究人員因此得出結論：「最關鍵的干預點」仍是源頭——也就是被用來製作這類假色情圖像的AI工具本身。

🧩 **White Circle如何繞過三大生圖模型的安全防護**

出面示警的是White Circle，一家由Anthropic、DeepMind、Hugging Face、OpenAI的資深領導者與研究人員背書的公益公司。該公司由Denis Shilov創辦,他在2024年10月曾發布一個備受關注的通用型模型越獄（jailbreak）手法。White Circle長期投入文生圖模型是否會擋下禁止內容類別的測試，而他們上個月發布的一篇preprint，揭露了DALL·E 3、Google的Nano Banana 2，以及GPT-Image-2在安全防護上的漏洞。研究團隊表示，他們僅用「網路上任何人都能下載的現成工具」，搭配API呼叫，以一種新穎的攻擊手法就繞過了安全過濾器。

📊 **DALL·E 3防護破功機率13%，新模型不代表更安全**

測試結果顯示：在DALL·E 3上，約13%的攻擊prompt產出的圖像經人工審核確認為情色內容；Nano Banana 2的比例低於10%；GPT-Image-2約為3%。

💡 **模型愈強，過濾卻可能愈弱？**

值得注意的是,文章指出近幾個月的紅隊測試顯示，隨著Google與OpenAI的主力圖像生成模型變得更強大,它們在阻擋情色輸出上反而可能表現得更差。這與「模型進步理應連帶提升安全防護」的直覺相反。

⚠️ **一份剛發布的preprint，仍待更大規模驗證**

這份研究目前仍是「鮮少被注意到的preprint」，尚未經過更廣泛的同行檢視，測試範圍也僅涵蓋這三款模型，結論的普遍性仍有待觀察。

🎯 **整合生圖API前，別把guardrails當成唯一防線**

對於正在呼叫這些圖像生成API來建置產品的工程團隊，這項測試結果提醒：供應商內建的安全過濾器並非萬無一失，若應用場景涉及使用者上傳內容或開放式prompt,仍需在自己的系統層再疊加一層內容審核與濫用偵測機制。

🔗 **來源**
- 標題：OpenAI, Google pushing new AI models easily tricked into making nudes, researchers say
- 作者／機構：Ashley Belanger（Ars Technica）
- 連結：https://arstechnica.com/tech-policy/2026/10/openai-google-pushing-new-ai-models-easily-tricked-into-making-nudes-researchers-say/

#AISafety #RedTeaming #OpenAI #Google #DeepfakeDetection #ContentModeration #TextToImage #AIGovernance #Jailbreak #ResponsibleAI
