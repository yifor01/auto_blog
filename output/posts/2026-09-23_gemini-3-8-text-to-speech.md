---
title: Gemini 3.8 text-to-speech
source: Hacker News
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/
model: claude-code/sonnet
generated_at: '2026-09-23T20:36:24.431967'
score: 89
---

📌 Gemini 3.8 TTS：從固定語音庫變成可導演的配音工作室

TL;DR：Google 推出 Gemini 3.8 Flash TTS 與 Flash-Lite TTS，可用自然語言從零打造角色語音並逐句導演表演。

過去要做出一個有個性的角色聲音，得從固定語音預設中挑一個將就用；現在 Google 讓你直接用一句話描述「一個來自墨爾本、充滿活力的 DJ」，模型就能生成對應的聲音。

🤔 語音生成從「選一個」變成「做一個」

Google 這次在 Gemini 家族中新增兩個文字轉語音模型：Gemini 3.8 Flash TTS 專為深度創意導演與角色設計打造，適用遊戲、沉浸式有聲書、Podcast 與互動媒體；Gemini 3.8 Flash-Lite TTS 則針對大量、低成本的場景最佳化，適合大規模配音、音訊內容生成與具表現力的語音代理。兩者都已開放在 Google AI Studio、Gemini API、Gemini Enterprise、Gemini Notebook 與 Google Vids 使用，是繼 3.5 Live Translate、3.5 Transcribe、3.8 Live、3.8 Live Extended Thinking 之後，Gemini Audio 家族的最新成員。

🧩 從語音設計到逐句導演

- 生成式語音設計：用超過 100 種語言與方言的自然語言提示，從零打造角色語音，包括口音、性格特徵等細節。
- 龐大語音庫：提供超過 2,000 個可直接投入生產的語音，涵蓋墨西哥西班牙語、魁北克法語、蘇格蘭英語等地區變體。
- 語音複製：僅需 30 秒的音訊樣本即可還原一致的聲音特質，並內建同意驗證機制——語音複製前，使用者必須提供與參考講者相符的口頭同意錄音。
- 儲存與擴充：可儲存並管理自訂語音，維持長期專案的一致表現與最小漂移。
- 語音混合（即將推出）：可從既有語音庫挑選語音後，再用提示微調音色、音高、語速與口音。
- 逐句表演導演：可自行撰寫舞臺指示，或讓 Gemini 依腳本線索自動調整語氣，從平靜的客服語氣到低語懸疑場景皆可控制。
- 長篇生成：可在數小時的連續音訊中維持語音品質、自然節奏與角色音色一致，適合 Podcast 與有聲書。
- 雙講者場景搭建：能從單一腳本直接導演多輪對話，保持兩個聲音清楚分離且自然輪替。
- 腳本化語氣與插話詞：支援非語言提示（如 `<laughs>`、`<sigh>`、`<gasp>`）與主動聆聽插話（如 `|mhm|`、`|yeah|`），用於精準的喜劇節奏與反應時機。

📊 在 Hume AI 與 Voice Arena 評測中的排名

根據 Google 公布的數據，Gemini 3.8 Flash TTS 在 Hume AI 的 Voice Design Benchmark 拿下整體第一（71.4 分），並在口音建模上同樣領先（60.8 分）；在 Hume AI 的 Overall Quality Index 上，Flash TTS 與 Flash-Lite TTS 分別拿下第一與第二名。在 Voice Arena 的盲測人類偏好評測中，兩個模型在日語、巴西葡萄牙語、越南語、現代標準阿拉伯語（MSA）、墨西哥西班牙語與印地語等多個主要語言上都位居前段。

⚠️ 安全機制內建在生成流程中

每一段由 Gemini Audio 模型生成的音訊都會嵌入 SynthID 浮水印，且該浮水印是不可感知地織入音訊輸出中，用於協助辨識 AI 生成內容、防止誤導資訊；語音複製功能則要求提供驗證用的口頭同意錄音，並搭配 C2PA 內容憑證，用以保護開發者與聲音本人的權益。

🎯 實務啟示

對需要大量客製化語音的團隊來說，重點在於這次更新把「語音設計」與「表演導演」拆成兩層可分別控制的能力：想要角色語音就用 Flash TTS 從零設計或複製既有聲音，想要大規模穩定輸出就用 Flash-Lite TTS。腳本層面的細粒度控制（停頓、插話詞、雙講者場景）代表這套工具已經能直接產出接近成品的 Podcast 或有聲書素材，而非僅是單句朗讀。開發者今天起即可在 Google AI Studio 的 audio playground 中直接體驗。

🔗 來源
- 標題：Gemini 3.8 text-to-speech
- 作者／機構：Leland Rechis (Group Product Manager), Alan Cowen (Director, Research Science), Gemini Audio Team, Google
- 連結：https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/

#Gemini #TextToSpeech #VoiceAI #GoogleAI #AudioGeneration #SynthID #VoiceCloning #GenerativeAudio #Podcasting #AIStudio
