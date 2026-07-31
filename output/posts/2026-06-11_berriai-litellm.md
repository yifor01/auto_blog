---
title: BerriAI/litellm
source: GitHub Trending
url: https://github.com/BerriAI/litellm
score: 87
model: google/gemma-4-31b-it:free
generated_at: '2026-06-11T00:49:10.024332'
---

📌 **【BerriAI 開源】LiteLLM：一把鑰匙搞定 100+ 大模型呼叫！**

在多雲環境裡，你是否還在為不同 LLM 的 SDK、認證方式與錯誤格式頭疼？  
想換模型卻怕要重寫整套程式碼？  
LiteLLM 讓這些「切換成本」瞬間消失，直接以 OpenAI 標準介面玩遍 OpenAI、Anthropic、Gemini、Bedrock、Azure…等百餘家供應商。

---

🤔 **跨供應商的繁雜度，真的只能靠手動腳本解決嗎？**  

傳統上每家雲服務都有自己的 API、金鑰管理方式，甚至回傳的錯誤結構都不統一。開發團隊常因為「換一家」而陷入「重新寫 SDK、重新測試」的惡性循環。LiteLLM 把這層整合工作抽象成一個 **AI Gateway**，讓你只需要改變環境變數，就能即時切換後端模型。

---

🧪 **LiteLLM 的核心設計：單一 OpenAI 格式 + 多端點支援**  

- **Unified API**：一次呼叫 `/chat/completions`、`/embeddings`、`/images`…等所有常見端點，後端自動路由到對應的 LLM 供應商。  
- **Python SDK**：`pip install litellm` 後即可在程式碼中直接 `from litellm import completion`，不需要額外安裝每家廠商的套件。  
- **Proxy Server（AI Gateway）**：部署為公司內部的 Proxy，提供 **virtual keys、消費追蹤、守護規則、負載平衡**，甚至內建管理儀表板。  
- **效能基準**：在 1k RPS（每秒千次請求）下的 95% 延遲僅 8 ms，足以支撐高頻率的生成任務。  

> **範例程式**  
> ```python
> from litellm import completion
> import os
> 
> os.environ["OPENAI_API_KEY"] = "your-openai-key"
> os.environ["ANTHROPIC_API_KEY"] = "your-anthropic-key"
> 
> response = completion(
>     model="anthropic.claude-v2",
>     messages=[{"role":"user","content":"Explain LiteLLM in 30 seconds"}],
> )
> print(response)
> ```

---

⚡ **為什麼現在的團隊都在採用 LiteLLM？**  

- **即插即用**：只要改變環境變數，即可在不同雲供應商之間切換，無需重寫業務邏輯。  
- **成本治理**：虛擬金鑰與消費追蹤讓財務與工程團隊同步掌握每個模型的使用費用，避免「雲端帳單失控」。  
- **企業級防護**：內建 Guardrails（內容過濾、速率限制）以及 Dashboard，滿足合規與監控需求。  
- **開源與社群**：已被 Netflix 等大企業採用，GitHub Trending 高星標，持續有社群貢獻與功能擴充。

---

⚠️ **限制與考量**  

- **不是新模型**：LiteLLM 本身不提供任何生成能力，僅是統一介面層，模型品質仍取決於底層供應商。  
- **部署與維運成本**：自行托管 Proxy 需要額外的基礎設施與運維，對小型團隊而言可能仍有門檻。  
- **功能覆蓋度**：雖支援 100+ 供應商，但部分新發布的專屬功能（如特定的工具呼叫）仍需供應商原生 SDK 才能使用。

---

🎯 **實務建議：如何把 LiteLLM 融入你的開發流程**  

1. **先行測試**：在本機環境安裝 `litellm`，用最常用的模型跑一次基準測試，確認延遲與回傳格式符合預期。  
2. **設定虛擬金鑰**：為每個部門或專案建立獨立的 virtual key，配合支出追蹤儀表板，避免成本失控。  
3. **部署 Proxy**：在 Kubernetes 或 Docker 中以 Helm chart 部署 LiteLLM Proxy，並啟用 Guardrails 以滿足合規需求。  
4. **漸進式切換**：先將非關鍵服務（如測試環境）切換至 LiteLLM，確保監控與錯誤處理正常後，再逐步遷移核心服務。  

---

🔗 **論文/專案連結**  
📝 **專案名稱**：LiteLLM – Open Source AI Gateway for 100+ LLMs  
👤 **作者**：BerriAI (GitHub: BerriAI/litellm)  
🔗 **GitHub**：https://github.com/BerriAI/litellm  

---

💬 你在多雲 LLM 部署上遇過哪些痛點？有沒有嘗試過類似的統一 Gateway？歡迎在下方分享你的經驗與觀察 👇

#AI #LLM #OpenSource #DevOps #EnterpriseAI #BerriAI #LiteLLM #MachineLearning #MultiCloud #API #GitHubTrending
