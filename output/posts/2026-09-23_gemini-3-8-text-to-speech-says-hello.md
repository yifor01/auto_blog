---
title: Gemini 3.8 text-to-speech says hello
source: Google DeepMind
url: https://deepmind.google/blog/say-hello-to-gemini-38-text-to-speech/
model: claude-code/sonnet
generated_at: '2026-09-23T20:30:34.043844'
score: 119
---

📌 【Google DeepMind】Gemini 3.8 新 TTS 模型，逐行導演 AI 語音演出

TL;DR：Gemini 3.8 推出兩款新 TTS 模型，讓開發者能用自然語言打造客製化角色聲音並逐行導演臺詞情緒。

如果一個 AI 不只能唸稿，還能被你「說戲」，要求它在第三句嘆氣、第七句壓低聲音、句尾加一句自然的「嗯」，那語音生成離真正的配音演出還有多遠？Google DeepMind 今天用 Gemini 3.8 給出了答案。

🤔 背景：從固定語音庫到動態創作工具

Google 在 Gemini 家族中推出兩款新的文字轉語音模型：Gemini 3.8 Flash TTS 與 Gemini 3.8 Flash-Lite TTS。團隊將此定位為把語音生成「從靜態預設聲音，轉變為動態的創作工作室」，目標是讓創作者、開發者與企業打造更豐富、更具表現力的音訊體驗，同時強化 Gemini Notebook、Google Vids 等產品的使用體驗。兩款模型已可在 Google AI Studio、Gemini API、Gemini Enterprise、Gemini Notebook 與 Google Vids 中使用，並延續先前 3.5 Live Translate、3.5 Transcribe、3.8 Live、3.8 Live Extended Thinking 等 Gemini Audio 產品線。

🧩 兩款模型的分工：創意導演 vs 大規模量產

Gemini 3.8 Flash TTS 主打深度創意導演與角色設計，可用自然語言 prompt 從零打造全新聲音，應用在遊戲、沉浸式有聲書、Podcast 與互動媒體上，並能逐行控制表演細節，包括表演指示、節奏、口音轉換與應答式插話（backchanneling）。Gemini 3.8 Flash-Lite TTS 則針對高流量、需要成本效益的場景最佳化，適合大量配音、音訊內容製作與具表現力的語音 agent，同樣能細緻控制語氣、節奏與情緒層次。

聲音打造方面，開發者可用自然語言 prompt 跨越 100 多種語言與方言，從零設計聲音的角色、口音與特質，官方舉例包括墨爾本 DJ 的高能量聲線、單調的機器人聲，以及日本龍的聲音演出。語音庫也擴充到超過 2,000 個可直接上線使用的聲音，涵蓋墨西哥西班牙語、魁北克法語、蘇格蘭英語等地區變體。語音複製功能能透過 30 秒的音訊樣本重現一致的聲音特徵，並內建同意驗證機制：必須提供與參考聲音相符的口頭同意錄音才能建立複製聲音。官方也預告即將推出「語音混音」功能，讓使用者從既有語音庫挑選聲音後微調音色、音高、節奏與口音。

導演臺詞方面，開發者可自行撰寫舞臺指示，或讓 Gemini 依自然的劇本線索掌控表演節奏，例如冷靜的客服語氣或耳語式的懸疑場景。長篇生成能在數小時的連續音訊中維持穩定的音質、節奏與角色音色，適合 Podcast 與有聲書；原生雙人對話場景則能從單一劇本同時導演兩個角色的對話，保持聲音區隔與自然的輪流節奏。此外還支援腳本化的擬真聲效與應答插話，例如 <laughs>、<sigh>、<gasp> 等非語言標記，以及 |mhm|、|yeah| 等主動聆聽用語，用於掌握喜劇節奏與反應點。

📊 數據：Hume AI 基準測試中的表現

官方公布的評測數據顯示，Gemini 3.8 Flash TTS 在 Hume AI 的 Voice Design Benchmark 中拿下整體第一（71.4 分），並在口音建模項目中同樣領先（60.8 分）。在 Hume AI 的 Overall Quality Index 中，Flash TTS 與 Flash-Lite TTS 分別拿下第一與第二名。相較於前代 Gemini 3.1 Flash TTS，兩款新模型在長篇內容生成與雙人劇本對話控制上有明顯進步。在 Voice Arena 的盲測人類偏好評比中，兩款模型在日語、巴西葡萄牙語、越南語、現代標準阿拉伯語、墨西哥西班牙語與印地語等多國語言中都取得領先地位。

⚠️ 限制與信任機制

語音生成能力越強，被濫用來假冒他人聲音的風險也越高。Google 在語音複製功能中加入同意驗證機制作為防線，並為所有 Gemini Audio 模型生成的音訊加上 SynthID 浮水印，這是一種嵌入音訊訊號中的不可感知標記，用來協助偵測 AI 生成內容以防範不實資訊。語音複製也附帶 C2PA 內容憑證，用來保護開發者與聲音提供者的權益。

🎯 實務啟示

這次更新的重點不只是「聲音更逼真」，而是把語音生成從單一段落的合成，變成可逐行導演、可長篇維持一致性的創作工具。如果產品需要角色化的語音 agent 或大量配音場景，值得評估 Flash-Lite 的成本效益；若需要精緻的角色演出與情緒控制，Flash TTS 的逐行導演能力可能是更合適的起點。

🔗 來源
- 標題：Gemini 3.8 text-to-speech says hello
- 作者／機構：Google DeepMind
- 連結：https://deepmind.google/blog/say-hello-to-gemini-38-text-to-speech/

#Gemini #TextToSpeech #GoogleDeepMind #VoiceAI #GenerativeAI #VoiceCloning #SynthID #ConversationalAI #AIStudio #AIAudio
