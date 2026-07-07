---
title: Bridging Interleaved Multi-Modal Reasoning as a Unified Decision Process
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.03748
score: 96
model: google/gemma-4-31b-it:free
generated_at: '2026-07-07T21:12:57.206958'
---

Bridging Interleaved Multi-Modal Reasoning as a Unified Decision Process  

🔹 **TL;DR**  
- BRAID 框架將文字‑影像互動建模為馬可夫決策過程 (MDP)，以實現統一的多模態推理。  
- 透過視覺‑語言模型 (VLM) 的引導，採用強化學習進行文字與影像的聯合最佳化。  
- 框架設計為模態無關，理論上可擴充套件至其他模態組合，本文僅以文字‑影像為示範。  

## 🔍 框架核心概念  
- 將文字與影像的互動視為一個馬可夫決策過程：狀態對應多模態表示、動作對應推理決策、獎勵對應任務回饋。  
- 此建模方式使得多模態推理能在單一決策框架下進行聯合最佳化，避免分階段處理所帶來的資訊損失。  

## 🔧 方法概述  
- 使用視覺‑語言模型作為導引（guidance），提供狀態價值或動作建議，以強化學習的方式更新策略。  
- 強化學習目標為最大化預期回報，使得文字與影像的推理過程能夠協同最佳化。  
- 框架本身具有模態無關性，理論上可適用於其他模態組合（如聲音、影片），但本文僅展示文字‑影像的應用案例。  

## 📚 來源與參考  
- 論文標題：Bridging Interleaved Multi-Modal Reasoning as a Unified Decision Process  
- 來源：HuggingFace Daily Papers  
- 連結：[HuggingFace Daily Papers](https://huggingface.co/papers/2607.03748)
