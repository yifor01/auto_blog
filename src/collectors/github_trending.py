"""GitHub Trending collector for AI repos."""

from __future__ import annotations

from datetime import date

from bs4 import BeautifulSoup

from src.collectors.base import BaseCollector
from src.models import ContentItem, SourceType
from src.logger import get_logger
from src.utils import get_http_client, load_config

_logger = get_logger("collectors.github")


class GitHubTrendingCollector(BaseCollector):
    name = "github"

    # AI 相關的關鍵字，用來過濾 trending repos
    AI_KEYWORDS = {
        # 核心 GenAI
        "llm", "gpt", "transformer", "diffusion", "agent", "rag",
        "langchain", "embedding", "fine-tune", "finetune", "lora",
        "rlhf", "dpo", "grpo", "multimodal", "nlp",
        "machine-learning", "deep-learning", "neural", "ai",
        "inference", "tokenizer", "benchmark",
        # 模型與框架
        "ollama", "vllm", "sglang", "mlx", "gguf", "onnx",
        "deepseek", "qwen", "gemma", "mistral", "llama",
        # 2025-2026 熱門
        "mcp", "reasoning", "agentic", "text-to-video",
        "speculative-decoding", "quantiz", "reward-model",
        "tts", "whisper", "speech", "vision-language",
        "flow-matching", "moe", "alignment", "safety",
    }

    def collect(self, target_date: date | None = None) -> list[ContentItem]:
        config = load_config()
        cfg = config["collectors"]["github"]
        if not cfg.get("enabled", True):
            return []

        target_date = target_date or date.today()
        languages = cfg.get("languages", ["python"])
        items: list[ContentItem] = []

        client = get_http_client()
        try:
            for lang in languages:
                try:
                    url = f"https://github.com/trending/{lang}?since=daily"
                    resp = client.get(url)
                    resp.raise_for_status()
                    soup = BeautifulSoup(resp.text, "html.parser")

                    for row in soup.select("article.Box-row"):
                        repo_link = row.select_one("h2 a")
                        if not repo_link:
                            continue

                        repo_path = repo_link.get("href", "").strip("/")
                        repo_name = repo_path.split("/")[-1] if "/" in repo_path else repo_path

                        # 描述
                        desc_el = row.select_one("p.color-fg-muted")
                        description = desc_el.get_text(strip=True) if desc_el else ""
                        if not description:
                            desc_el = row.select_one("p")
                            description = desc_el.get_text(strip=True) if desc_el else "GitHub Project: " + repo_name

                        # Stars today
                        stars_today = 0
                        star_el = row.select_one("span.d-inline-block.float-sm-right")
                        if star_el:
                            try:
                                stars_text = star_el.get_text(strip=True).replace(",", "")
                                stars_today = int(
                                    "".join(c for c in stars_text if c.isdigit()) or "0"
                                )
                            except ValueError:
                                pass

                        # 用關鍵字 + 描述判斷是否 AI 相關
                        combined = f"{repo_name} {description}".lower()
                        is_ai = any(kw in combined for kw in self.AI_KEYWORDS)
                        if not is_ai:
                            continue

                        # language tag
                        lang_el = row.select_one("[itemprop='programmingLanguage']")
                        language = lang_el.get_text(strip=True) if lang_el else lang

                        # 追加抓取 README 作為長篇摘要
                        readme_text = ""
                        try:
                            import time
                            time.sleep(0.5)
                            repo_url = f"https://github.com/{repo_path}"
                            r_resp = client.get(repo_url)
                            if r_resp.status_code == 200:
                                r_soup = BeautifulSoup(r_resp.text, "html.parser")
                                readme_el = r_soup.select_one("article.markdown-body")
                                if readme_el:
                                    readme_text = readme_el.get_text(separator=" ", strip=True)
                        except Exception as e:
                            _logger.warning("Could not fetch README", extra={"repo": repo_name, "error": str(e)})

                        final_abstract = readme_text[:1500] if readme_text else description

                        items.append(
                            ContentItem(
                                source=SourceType.GITHUB,
                                source_name="GitHub Trending",
                                title=repo_path,
                                url=f"https://github.com/{repo_path}",
                                authors=[repo_path.split("/")[0]] if "/" in repo_path else [],
                                abstract=final_abstract,
                                published_date=target_date,
                                tags=[language, "github", "trending"],
                                raw_metadata={
                                    "stars_today": stars_today,
                                    "language": language,
                                    "repo_name": repo_name,
                                },
                            )
                        )
                except Exception as e:
                    _logger.error("GitHub Trending error", extra={"language": lang, "error": str(e)})
        finally:
            client.close()

        _logger.info("GitHub Trending complete", extra={"count": len(items)})
        return items
