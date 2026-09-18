---
title: A heap overflow and SSO misconfiguration to compromise OpenAI internal repos
source: Hacker News
url: https://www.hacktron.ai/blog/hacking-openai
model: claude-code/sonnet
generated_at: '2026-09-18T19:52:25.439325'
score: 94
---

📌 一支論壇圖片上傳漏洞，如何鏈成OpenAI內部程式碼庫的存取權

TL;DR：研究團隊串連libheif堆疊溢位與OpenAI SSO設定錯誤，72小時內從論壇RCE走到員工Codex帳號。

一張看似無害的HEIC圖片上傳，最後能讓外部研究者用OpenAI員工的Codex帳號，在OpenAI內部monorepo裡開一個PR。這不是想像，而是安全研究團隊Hacktron在2026年7月25日實際完成的攻擊鏈，而整段過程從發現漏洞到取得內部倉庫存取,只花了不到72小時。

🤔 **論壇的「Sign in with OpenAI」，成了跳板的關鍵假設**

OpenAI的官方論壇community.openai.com使用Discourse架設，並支援透過auth.openai.com的「Sign in with OpenAI」SSO登入。Hacktron團隊在摸清OpenAI服務與基礎架構後推測：只要能攻陷這個論壇，就有機會透過這條身分驗證流程,滲透進OpenAI更廣泛的服務。由於使用者能把GitHub、Slack、Email等多種服務連接到ChatGPT與Codex帳號,理論上暴露的攻擊面相當可觀。要驗證這個假設,第一步是先在Discourse論壇上拿到RCE。

🧩 **從HEIC圖片到heap overflow：libheif的未回補安全修復**

Discourse本身並不是容易的攻擊目標，團隊過去也曾研究過，於是轉向其依賴套件。他們在檢視Discourse圖片上傳流程時發現，Discourse原本用FastImage做圖片檢查，但FastImage不支援HEIF格式，因此HEIC/HEIF檔案會被轉交給ImageMagick的magick指令做轉換，這使得底層的libheif解析器直接暴露在攻擊者可控的檔案面前。

團隊用Claude Opus 4.8檢查Discourse Docker映像中安裝的libheif套件，發現某些安全修復並未被回補（backport）到該版本，導致HEIC解碼過程中出現heap buffer overflow，可產生越界讀寫（OOB R/W）原語。值得注意的是，這段有問題的程式碼在上游其實已於前一年修改過，但當時的commit並未被標記為安全修復,也沒有拿到CVE編號——這很可能正是Debian 12與13遲遲沒有跟進回補的原因。Discourse的Docker映像基於Debian 12，安裝的是有漏洞的libheif 1.19.7版；即使是Debian 13，在事發當時裝的1.19.8版同樣受影響。Debian直到8月8日才發布Debian 13的對應安全更新。

🧩 **Opus 5上線當晚，exploit從ARM64搬到x86-64/jemalloc**

7月24日，團隊先用Opus 4.8在關閉ASLR的情況下做出可用的ImageMagick/libheif程式碼執行exploit，但要在ASLR開啟、貼近Discourse預設設定的環境下做到穩定利用，多次嘗試並不順利。就在當天晚上，Anthropic發布了Claude Opus 5。團隊用新模型重新開始，三小時內先在本地Mac上做出可用的ARM64 exploit，再要求它移植到Discourse實際使用的x86-64與jemalloc記憶體配置環境。到7月25日清晨6點，他們已透過圖片上傳確認了本地RCE。

接著團隊把Claude放進自主的/goal迴圈，讓它攻擊自己架設的Discourse Cloud instance，並用rce.ee/ctf-forum做代理讓目標看起來像CTF題目——原因是Opus本身會拒絕針對真實遠端目標撰寫exploit。上午10點再檢查時，agent已經在Discourse Cloud上拿到RCE，並透過讀取/etc/hosts證明存取。團隊用產生出的exploit腳本，最終在OpenAI自己的Discourse實例上取得RCE，驗證了論壇會員可被零互動（no interaction）方式接管ChatGPT/Codex帳號的假設,隨即通報OpenAI。之後他們接管了一名OpenAI員工的帳號，其Codex恰好連結到OpenAI的GitHub組織。為了證明影響力但不實際窺探任何內部程式碼，團隊向這名員工的Codex送出一則prompt，請它在OpenAI內部monorepo中開了PR #1186742。

📊 **72小時時間線與後續處理**

| 時間 | 事件 |
|---|---|
| 7/25 05:00–06:00 UTC | 取得Discourse社群環境的RCE與管理員權限 |
| 7/25 08:00–10:00 UTC | 向OpenAI Bugcrowd計畫提交報告 |
| 7/25 13:30–15:30 UTC | 建立內部monorepo的無害PoC PR，並停止一切測試 |
| 7/25 22:49 UTC | OpenAI確認修復完成 |
| 7/25 | 向Discourse HackerOne計畫提交報告 |
| 7/27 | Discourse完成修復並加入圖片處理沙箱作為深度防禦 |
| 7/28 | Discourse發布安全公告GHSA-vhm9-85gw-x335 |
| 9/1 | OpenAI核發6,500美元賞金並結案 |

⚠️ **一個容易被忽略的細節：賞金範圍不含對Discourse本身的測試**

OpenAI在結案留言中特別澄清：針對Discourse託管的community.openai.com本身的測試，其實明確排除在OpenAI漏洞賞金計畫範圍之外；這筆6,500美元獎金認可的是OpenAI端的問題（即SSO身分驗證流程被利用的部分），而非團隊對Discourse所做的操作。若你自架Discourse，也要留意：僅更新網頁介面並不會替換底層映像檔，官方建議在/var/discourse下執行git pull後接著./launcher rebuild app才能真正套用修復。

🎯 **實務啟示**

這個案例提醒工程團隊幾件事：第三方圖片處理函式庫（尤其是HEIC/HEIF/AVIF解碼路徑）是容易被忽視的攻擊面，且作業系統套件的安全回補未必即時；SSO與帳號連接的第三方服務（GitHub、Slack、Email）會放大單點漏洞的影響範圍；而AI模型被用於加速exploit開發本身也是值得關注的雙面刃趨勢。Hacktron團隊表示後續已將研究延伸為「HEIF Heist」，追蹤libheif在Slack、Meta、GitHub Enterprise、Ruby on Rails，以及Next.js、Astro、Gatsby等Node.js框架中的影響面，若你的應用程式會接受使用者上傳的.heic/.heif/.avif檔案，很可能也在受影響範圍內。

🔗 **來源**
- 標題：A heap overflow and SSO misconfiguration to compromise OpenAI internal repos
- 作者／機構：Hacktron（Harsh Jaiswal、Mohan Pedhapati、Rahul Maini）
- 連結：https://www.hacktron.ai/blog/hacking-openai

#OpenAI #SecurityResearch #BugBounty #libheif #Discourse #SSO #HeapOverflow #ResponsibleDisclosure #ExploitDev #InfoSec
