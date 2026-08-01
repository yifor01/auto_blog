---
title: 'JetBrains Open-Sources KotlinLLM: Smart Macros That Generate Kotlin Source
  Code at Runtime and Hot-Reload It Through JDI'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/31/jetbrains-research-open-sources-kotlinllm-intellij-plugin-kotlin-runtime-llm/
model: tencent/hy3:free
generated_at: '2026-08-01T08:08:47.861237'
score: 91
---

📌 【JetBrains Research 開源】KotlinLLM：透過 Smart Macros 與 JDI 實現程式碼即時生成與熱重載

TL;DR：KotlinLLM 是一個實驗性 IntelliJ IDEA 插件，利用 Smart macros 在執行期生成 Kotlin 程式碼並透過 JDI 進行熱重載。

JetBrains Research 近期開源了 KotlinLLM，這是一個針對 Kotlin/JVM 專案開發的實驗性研究原型（Research Prototype）。它引入了一種稱為「Smart macros」的新語言特性，讓開發者能在執行期生成程式碼，並在邏輯不符時自動修正。

🧩 **Smart macros：將函式呼叫轉化為生成的程式碼**

KotlinLLM 的核心概念是 Smart macro，它本質上是一個普通的 Kotlin 函式呼叫，但其函式體是由 LLM 生成的程式碼。目前提供的公開 API 非常精簡：

* `asLlm<F, T>(from, hint)`：將輸入類型 F 轉換為目標類型 T（例如 data class、enum、list 或基本型別）。
* `mockLlm<T>()`：為介面 T 生成一個具備狀態的實作，其行為會根據被呼叫的方法而變化。

🚀 **九步執行迴圈：如何實現自動修正與熱重載**

當專案透過 KotlinLLM 的執行設定啟動時，插件會執行以下流程：

1. 掃描專案中的 `asLlm` 與 `mockLlm` 呼叫。
2. 更新生成的 bootstrap/provider/parser/mock 檔案。
3. 在 JDI（Java Debug Interface）環境下啟動執行設定。
4. 在生成的 regenerate hooks 上註冊斷點。
5. 若生成的邏輯與執行期場景不符，執行流程會觸發 hook。
6. 插件從暫停的 frame 中擷取執行期數值與型別資訊。
7. LLM Agent 根據資訊提交程式碼更新。
8. 插件編譯新程式碼並透過 JDI 重新定義（redefine）已載入的類別。
9. 重新嘗試原始呼叫。

📊 **實驗數據：高成功率與極低的執行開銷**

在一個適配過的 Spring Petclinic Kotlin 專案測試中（包含 18 個 `asLlm` 呼叫點）：

* **成功率**：24 個應用場景皆在 Smart macro 演化後成功完成，熱重載成功率達 100%。
* **效能影響**：編譯與重新定義過程僅增加約 1% 的總執行時間開銷。
* **其他應用**：在一個名為「GitHub Beginner Issue Radar」的合成實驗中，透過解析 20 個儲存庫與 3 萬多個 issue，在初學者標籤的檢索上達到了約 0.89 的召回率（recall）。

💡 **並非生產環境工具，但輸出結果可部署**

儘管 JetBrains 將其標記為實驗性插件，但其產出的行為（behavior）是可部署的。一旦行為生成完成，目標專案可以編譯並執行該行為，而不需要針對相同場景再次請求 LLM。開發者交付的是純粹的 Kotlin 程式碼，而非模型依賴。

⚠️ **使用限制與環境需求**

* 需要 IntelliJ IDEA 2025.2.x 版本。
* 需要 JDK 21。
* 需要在目標專案的 `.kotlinllm` 檔案中設定 OpenAI API key。

🎯 **實務啟示**

對於開發者而言，這提供了一種在開發早期快速模擬複雜邏輯或處理未知輸入的方式。透過將 LLM 的生成能力與 JVM 的動態特性結合，開發者可以在不重啟應用程式的情況下，直接在執行期「修復」生成的邏輯。

🔗 **來源**
- 標題：JetBrains Open-Sources KotlinLLM: Smart Macros That Generate Kotlin Source Code at Runtime and Hot-Reload It Through JDI
- 作者／機構：Michal Sutter @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/31/jetbrains-research-open-sources-kotlinllm-intellij-plugin-kotlin-runtime-llm/

#Kotlin #JetBrains #LLM #IntelliJ #JVM #SmartMacros #OpenSource #SoftwareEngineering #HotReload #MachineLearning
