---
title: '[AINews] Math Proofs Are Landing Faster Than We Can Read Them'
source: Latent Space
url: https://latent.space/p/ainews-math-proofs-are-landing-faster-than-we-can-read-them/
model: claude-code/sonnet
generated_at: '2026-11-26T01:07:40.154048'
score: 102
---

📌 數學證明掉落的速度，已經快過人類閱讀的速度

TL;DR：一週內多個AI系統接連宣稱解出矩陣乘法指數、量子互動證明等重量級難題，但其中不少仍待驗證。

Scott Aaronson晚餐時還在消化兩篇關於VP≠VNP的證明，甜點都還沒上桌，OpenAI的一篇論文已經宣稱方陣乘法指數ω恰好等於9/4；吃甜點的時候，另一篇論文又宣稱找到有限傅立葉轉換的匹配上下界。

🤔 **一個月內冒出的20個「AI輔助證明」**

Latent Space整理了今年以來64個精選的AI輔助研究進展，光是11月就佔了20個，其中6篇來自Google Cogentic的預印本。文章特別指出，這條曲線其實跟著公開發布的節奏走，裡頭也包含仍在審查中的證明——換句話說，數量本身可能掩蓋了尚未經過同儕驗證這個事實。文中還提到，OpenAI自己的目錄就列出730份手稿、分屬375個結果家族（含後續與同伴論述），而10月才因為一篇論文的符號錯誤，連帶撤回了另外兩篇——這說明AI產出證明的速度雖快，品質把關仍在路上。

🧩 **ω=9/4：多數專家原本預期的答案是2**

最受矚目的是矩陣乘法指數ω的進展：10月OpenAI的模型找到ω的上界至多9/4，這次則宣稱找到匹配的下界，兩者相符意味著ω的值被鎖定在9/4，在此之前沒有任何非平凡的下界被找到過。據文中引述，這個下界是透過一個顯式的超線性電路下界得出。Omri Weinstein表示，如果屬實，這「真的很超現實」，因為多數專家原本預期ω應該等於2。Sebastien Bubeck也指出，先前Lee等人的結果意味著線性規劃（LP）現在可以在n^9/4內求解，他並表示LP甚至能以強多項式時間求解，這是Smale提出的著名問題之一。同一批進展還包括：有限傅立葉轉換複雜度為n√log n；整數乘法同樣達到n√log n，且在弱指數時間假設（ETH）下是緊界。

💡 **沒有公告、直接丟上GitHub的6篇論文**

文中提到一個值得留意的現象：Google Cogentic的6篇論文沒有經過正式公告，就由一個基於未命名Gemini 4模型的agent harness直接貼上GitHub，內容包括一個優於1992年紀錄的NFS級別因數分解界、聲稱的確定性次指數因數分解、更快的小特徵離散對數算法，以及log-rank問題在平方根障礙以下的進展——這些都是「聲稱」的結果，素材並未說明是否已通過獨立驗證。同一天，Anthropic也貼出了自己對VP≠VNP的解答。另外，Yupan Liu展示了兩則訊息就足以完成量子互動證明，Aaronson表示他必須提醒自己這件事真的發生了。OpenHuman則說他們的agent利用先前那篇Lean版黎曼猜想（RH）證明（文中歸功於Levent Alpöge與Claude），在三天內證出了17個結果，包括Lindelöf猜想與Erdős第985號問題。

⚠️ **密碼學傳言：有，但未經證實**

加密安全是這波進展裡最敏感的一環。文中提到一份由Claude產生的分析認為RSA與ECC不受影響；但同時也記錄了Scott Aaronson轉述的說法——他聽到「許多許多」關於OpenAI或Anthropic能在多項式時間內做因數分解的傳言，文章明確標註這一點「未經證實」。Igor Babuschkin則提出另一個角度：比起量子電腦的Shor演算法，LLM找到的古典演算法可能才是對RSA更迫近的風險。

🎯 **實務啟示**

對工程師而言，這篇文章最大的提醒不是「數學要被AI解決了」，而是驗證速度已經追不上生成速度——10月那起符號錯誤撤稿案就是明證。在把任何「AI宣稱證明」的結果（尤其是涉及密碼學安全假設的部分）當成既定事實、進而影響系統設計決策之前，務必確認它是否已經過同儕審查或獨立複現，而不是只看到一則推文或一篇預印本就下定論。

🔗 **來源**
- 標題：[AINews] Math Proofs Are Landing Faster Than We Can Read Them
- 作者／機構：Latent Space
- 連結：https://latent.space/p/ainews-math-proofs-are-landing-faster-than-we-can-read-them/

#AIResearch #MathProofs #TheoreticalComputerScience #OpenAI #Anthropic #ComplexityTheory #MatrixMultiplication #AIForMath #LeanProver #Cryptography
