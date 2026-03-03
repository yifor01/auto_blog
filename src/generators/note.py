"""Personal AI note generator."""

from __future__ import annotations

from datetime import date

from src.models import GeneratedContent, ScoredItem
from src.logger import get_logger
from src.utils import (
    NOTES_DIR,
    llm_chat,
    load_config,
    slugify,
    today_str,
)

_logger = get_logger("generators.note")

NOTE_SYSTEM_PROMPT = """你是一位 AI 研究者的個人筆記助理。請將以下 AI 論文/新聞整理為精簡的個人筆記。

## 筆記格式

# [標題]

**TL;DR**: 一句話總結

**來源**: [連結]
**機構**: [機構名]
**日期**: [日期]

## 核心要點
- 要點 1
- 要點 2
- 要點 3

## 技術細節
- 方法/架構的關鍵創新
- 與現有方法的差異

## 實驗結果
- 主要數據 / benchmark 表現

## 個人標註
- 這篇對我的工作/研究有什麼啟發？
- 有沒有可以直接應用的地方？
- 需要再深入閱讀的部分？

## 相關連結
- 論文 / GitHub / Demo

---

注意：語言使用繁體中文。保持精簡，重點突出。"""


def generate_note(item: ScoredItem) -> GeneratedContent:
    """為單一高分 item 生成個人 AI 筆記。"""
    config = load_config()
    model = config["llm"]["model"]

    user_msg = f"""請幫我整理以下內容為個人 AI 筆記：

**標題**: {item.item.title}
**來源**: {item.item.source_name}
**機構**: {item.item.organization}
**作者**: {', '.join(item.item.authors[:5])}
**連結**: {item.item.url}
**摘要**:
{item.item.abstract}

**評分理由**: {item.llm_reason}"""

    full_prompt = f"[SYSTEM]\n{NOTE_SYSTEM_PROMPT}\n\n[USER]\n{user_msg}"

    _logger.debug("LLM note generation started", extra={"title": item.item.title[:80]})
    content = llm_chat(
        messages=[
            {"role": "system", "content": NOTE_SYSTEM_PROMPT},
            {"role": "user", "content": user_msg},
        ],
        model=model,
        temperature=0.5,
    )

    return GeneratedContent(
        source_item=item,
        content=content,
        prompt_used=full_prompt,
        model_used=model,
        content_type="note",
    )


def save_note(gen: GeneratedContent, target_date: date | None = None) -> str:
    """儲存筆記（含 YAML frontmatter，便於後續查詢篩選）。"""
    date_str = target_date.isoformat() if target_date else today_str()
    slug = slugify(gen.source_item.item.title)
    filename = f"{date_str}_{slug}.md"

    note_path = NOTES_DIR / filename
    note_content = f"""---
title: "{gen.source_item.item.title}"
source: {gen.source_item.item.source_name}
url: {gen.source_item.item.url}
score: {gen.source_item.total_score:.0f}
model: {gen.model_used}
generated_at: {gen.generated_at.isoformat()}
---

{gen.content}
"""
    note_path.write_text(note_content, encoding="utf-8")

    _logger.debug("Note file written", extra={"output_file": note_path.name})
    return str(note_path)


def generate_and_save_notes(items: list[ScoredItem], target_date: date | None = None) -> list[str]:
    """批量生成並儲存筆記。"""
    import time

    config = load_config()
    delay = config.get("llm", {}).get("request_delay_seconds", 10)

    _logger.info(f"Note generation started ({len(items)} 篇)", extra={"count": len(items)})
    paths: list[str] = []
    for i, item in enumerate(items):
        try:
            gen = generate_note(item)
            path = save_note(gen, target_date)
            paths.append(path)
            _logger.info(
                f"({i+1}/{len(items)}) [{item.item.source.value}] "
                f"{item.item.title[:50]} → Note 已儲存",
                extra={
                    "title": item.item.title[:80],
                    "source": item.item.source.value,
                    "total_score": round(item.total_score),
                    "output_file": path.rsplit("/", 1)[-1],
                },
            )
        except Exception as e:
            _logger.error(
                f"({i+1}/{len(items)}) [{item.item.source.value}] "
                f"{item.item.title[:50]} → Note 生成失敗: {str(e)[:80]}",
                extra={"title": item.item.title[:80], "source": item.item.source.value, "error": str(e)},
            )
        if i < len(items) - 1:
            time.sleep(delay)
    return paths

