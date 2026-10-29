---
title: Build a repeatable PHP-to-Java migration engine with Kiro
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-a-repeatable-php-to-java-migration-engine-with-kiro/
model: claude-code/sonnet
generated_at: '2026-10-29T22:11:05.307234'
score: 80
---

📌 用Kiro打造可重複驗證的PHP轉Java遷移引擎

TL;DR：AWS示範如何用skill files加parity harness,把PHP轉Java遷移變成可重複、可驗證的流程。

把一套用了多年的PHP應用機械轉譯成結構相似的Java程式碼,編譯通過不代表行為一致——業務規則往往藏在Eloquent traits、XML mapping檔案這類不顯眼的地方。這正是AWS這篇文章要解決的痛點。

🤔 為什麼PHP轉Java這麼容易「看起來對,其實錯」

用Laravel、Symfony或Doctrine搭建多年的PHP專案,業務規則散落在框架的各種慣例裡。文章提出的解法是把原始PHP應用當成「規格」本身,直到有一套parity harness驗證通過之前,絕不宣稱Java版本正確。這套方法透過Kiro(一個把AI agent與你的程式碼庫配對、由人在環中逐步執行多步驟工程任務的IDE)來落地。

🧩 一套共享大腦,多個專案

整套知識封裝成版本化的Markdown skill files：php-to-java-migration(八階段遷移方法論)與php-model-discovery(掃描器工作流程),再加上一份core-workflow.md的steering檔案。這些檔案放在全域的`.kiro/`層,每個專案資料夾各自保有自己的PHP原始碼、Java輸出與`.kiro/specs/`規格子資料夾,方法論改進一次,所有專案都能受益。

掃描器本體是discover-models.php,一個單檔、無依賴的PHP命令列工具,不會真的執行目標程式碼,只讀取原始碼文字當作token。它會跑三種探索策略：沿著class繼承鏈找到`Illuminate\Database\Eloquent\Model`的Eloquent model、偵測`#[ORM\Entity]`這類Doctrine attribute,以及解析外部的`*.orm.xml`映射檔。輸出是單一JSON manifest,裡面的`models[]`陣列記錄每個欄位、cast、關聯與可見性規則,`flags[]`陣列則標記任何模糊之處(例如由執行期運算式組成的`$fillable`清單)交給人工審核,而不是讓AI自己猜。

八階段工作流程中,前四個階段集中人力判斷：Phase 0執行掃描器並整理盤點清單;Phase 1在寫任何Java程式碼之前先建立parity harness,用request/response配對同時打PHP原版與Java port,且這套harness必須能在人為故意注入bug時「失敗」才算可信;Phase 2建立RULEBOOK.md與GAP_INVENTORY.md;Phase 3用具代表性的檔案做壓力測試後才推廣到整個應用。Phase 4到8則大多是自驅動的迴圈：Phase 4搭建專案骨架,Phase 5依manifest翻譯資料模型,Phase 6翻譯I/O層(routes變成controllers、middleware變成filters、驗證邏輯變成annotated DTO),Phase 7分批轉換業務邏輯,Phase 8用harness證明parity並完成切換。

整個流程遵循兩條原則：PHP程式碼是規格,只有裁判(parity harness)點頭或每個不一致都被記錄為已核准的變更,才算完工;出問題時「修正迴圈,而不是修正程式碼」,也就是修改rulebook後重新產生,而不是手動補丁。同一套skill files還能有兩種跑法：在Kiro裡互動式驅動,每個階段都有明確的核準關卡;或是交給AWS Transform(AWS的大規模遷移agentic服務)自動化、以portfolio規模執行,兩者走的是完全相同的八階段流程。

🧩 怎麼用

從開放的repository開始,clone下來後用Kiro開啟repository根目錄(需包含`.kiro/`),skills與steering檔案會自動載入。範例專案laravel-eloquent-sample是一個bounded的示範：取一個開源Laravel應用的read-only切片,把Book、Chapter、Page、User四個model遷移成Spring Boot 3.4.1、Java 21、Maven搭配記憶體內的H2資料庫,manifest裡的每一筆項目都能機械式地對應到Java端的對應結構。

⚠️ 適用場景

目前公開的示範是一個範圍受限的read-only切片,文章沒有提供在大型正式應用上實際花費的時間或成本數字,這部分留白。

🎯 實務啟示

把遷移方法論封裝成版本化的skill files,而不是寫成一次性的轉換腳本,讓同一套邏輯能在「人工逐步審核」與「自動化、大規模」兩種模式間切換而不走樣;更重要的是,用一個「失敗測試都要能失敗」的parity harness當裁判,比起單純「看起來編譯過、跑得動」,更能抓出遷移中悄悄變質的業務邏輯。

🔗 來源
- 標題：Build a repeatable PHP-to-Java migration engine with Kiro
- 作者／機構：Sarat Guttikonda（AWS）
- 連結：https://aws.amazon.com/blogs/machine-learning/build-a-repeatable-php-to-java-migration-engine-with-kiro/

#AWS #Kiro #PHP #Java #SpringBoot #CodeMigration #AIAgent #LegacyModernization #SoftwareEngineering #DeveloperTools
