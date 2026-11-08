---
title: Goodbye Claude, hello Pi
source: Hacker News
url: https://caleb.software/posts/claude-to-pi.html
model: claude-code/sonnet
generated_at: '2026-11-08T21:19:20.640873'
score: 66
---

📌 用戶出走:一篇對Claude Code的「告別文」在說什麼

TL;DR:一名長期Claude Code用戶列出一連串痛點後,改用開源coding harness Pi。

Claude Code剛宣布終於要支援AGENTS.md檔案的隔天,一位用了超過一年的重度用戶就公開宣布:要走了。這篇在Hacker News拿下628點、405則留言的文章,與其說是產品負評,更像是一份寫給coding agent harness設計者的使用者心聲清單。

🤔 **一年的用戶,為什麼在這個時間點離開**

作者自稱是Claude Code的長期使用者,從它進入Claude Pro訂閱方案就開始用,還形容第一次看到它從一句提示就吐出(雖然雜亂但可用的)Python程式碼時「興奮到發抖」,也認為幾年後回頭看,Claude Code會被視為推動這波軟體開發新時代的重要推手之一。儘管如此,他還是決定把主力開發環境換成開源的Pi,理由是一連串累積起來的小摩擦。

🧩 **摩擦點一:格式與IDE整合的拉扯**

作者認為Claude Code一路要求使用者在CLAUDE.md與後來業界漸漸收斂的AGENTS.md之間複製或建symlink,對散落在各個GitHub專案裡的使用者來說很不方便。他在VSCode裡使用Claude Code,原本很喜歡「框選文字自動帶入context」這個功能,但這功能只能綁在單一session上:如果開第二個分頁啟動另一項任務,第一個分頁就完全收不到文字選取事件。文章提到這個問題至少從2025年12月就有人回報過,卻被官方標記為另一個不相關bug的重複問題而關閉。改用官方的VSCode GUI擴展雖然能支援多分頁,但作者說這個擴展本身問題也不少:內建的slash指令有一半完全無法使用,不支援自訂status line,多個subagent的輸出會依時間順序混雜堆在同一個對話串裡,難以閱讀。

💡 **摩擦點二:功能擴張速度與系統提示的膨脹**

作者列出dynamic workflows、agent teams、ultrareviews等新功能,認為這些更適合用來讓企業客戶消耗更多token,而不是他真正需要的東西。他提到,光是今年Claude Code就已經發布了244次更新,其中超過四分之三改動了系統提示(system prompt)或工具描述——這類改動足以明顯影響模型表現,尤其當新指令和使用者自己的提示或倉庫慣例衝突時。作者也指出,儘管官方曾經把系統提示砍掉80%,Claude Code整體的額外負擔(overhead)仍然比Pi高出不少;舉例來說,預設Bash工具的描述文字就將近3000個token,其中大部分是關於git操作與開PR的說明,而作者認為這些模型本來就已經會做,不需要特別教。他並做了一個假設性的估算:如果以百萬日活用戶、每天一億次請求來算,光是從這段描述裡省下1000個token,理論上每年就能省下可觀的推論成本。

⚠️ **作者自己也承認的侷限**

文章作者也坦承自己這篇寫得「滿是抱怨」,並不是常態寫作風格;他承認Anthropic做出了一款很酷的產品,也不認為自己從頭接手會做得更好,畢竟LLM coding harness還是一個很新的領域,先行者要在創新與穩定之間找平衡本來就很難。他認為真正的問題在於Claude Code像是一群工程師與PM各自把自己想要的功能快速塞進去,卻沒有一個角色專門負責在產品方向上說「不」。

🎯 **對工程師的意義**

這篇文章提醒的重點不是「該不該換工具」,而是coding agent harness本身的系統提示大小、工具描述長度與更新頻率,都會實際影響推論成本與行為穩定性,值得在選型時納入考量。作者也提到,換成Pi之後自己花了20分鐘就寫出一個擴展,解決了原本VSCode多分頁無法同時接收文字選取事件的問題,這說明這類整合問題未必有技術門檻,更多是產品取捨的問題。如果你也被類似的小摩擦困擾,不妨評估一下開源的coding harness作為替代方案。

🔗 **來源**
- 標題:Goodbye Claude, hello Pi
- 作者/機構:karagenit(caleb.software)
- 連結:https://caleb.software/posts/claude-to-pi.html

#ClaudeCode #AIcoding #DeveloperTools #CodingAgent #AGENTSmd #OpenSource #VSCode #LLMTooling #DeveloperExperience #AIWorkflow
