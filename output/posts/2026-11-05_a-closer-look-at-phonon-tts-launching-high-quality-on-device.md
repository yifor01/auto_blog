---
title: A Closer Look at Phonon TTS. Launching High-Quality On-Device Speech That Tops
  the Benchmarks.
source: HuggingFace Blog
url: https://huggingface.co/blog/phonon-tts
model: claude-code/sonnet
generated_at: '2026-11-05T23:00:10.522386'
score: 95
---

📌 65MB模型如何在離線裝置上念出自然人聲

TL;DR:Gradium開源的Phonon TTS能在手機、瀏覽器離線運行,還在Hugging Face Open TTS Leaderboard多語言拿下前三。

大多數語音AI的運作方式是:你打的每一句話都要繞去伺服器一趟才能變成聲音。Phonon把這段來回直接砍掉,文字留在裝置上,語音生成也不需要網路連線。兩週前Phonon剛開源釋出,團隊這次把開發脈絡、效能測試結果與推理框架一次說清楚。

🤔 **小模型和好聲音,過去很難兩者兼得**

讓語音AI能在小裝置上跑,一直是個兩難:要把模型做小,聲音品質往往跟著打折;要讓聲音好聽,模型通常就小不下來。Phonon團隊從4月發布最初版本後,花了六個月和早期使用者、合作夥伴一起打磨,把模型做得更小,同時擴充語言數與自訂語音(voice cloning、voice design)的能力。

🧩 **技術核心:flow matching,而非常見的TTS做法**

Phonon延續Pocket TTS系列的做法,用flow matching生成音訊,這和其他TTS系統常用的建模技巧相當不同,也是能把這種品質塞進如此小模型的關鍵。不過團隊也坦言,訓練初期數值不穩定,得靠多個技巧才能讓五種語言都產出穩定品質的結果。Phonon目前有兩個尺寸,分別約65MB與75MB,合計支援英文、法文、德文、西班牙文與葡萄牙文,並內建超過100種語音,也可以透過Gradium Studio自行打造專屬語音。它還能處理電話號碼、日期、代碼這類多數TTS系統容易出錯的細節。授權上,Phonon 31m(對應65MB版本)採Apache 2.0,可免費用於商業產品;Phonon 40m(涵蓋全部五種語言)採CC BY-NC,僅限非商業用途,若要商用則依使用者數量計價,而不是依生成的語音量計價。

🧩 **推理怎麼跑:ptts與🤗Transformers分工**

團隊為Phonon打造了專屬推理框架ptts,目標是在各種裝置上都拿到最佳效能,支援超過10種後端,包括CPU(Intel、Arm、WebAssembly)、GPU(CUDA、Vulkan、Metal、WebGPU)與NPU(Apple Core ML、Snapdragon)。Phonon同時從Transformers v5.21起作為官方參考的PyTorch實作,目標則不同:它面向GPU吞吐量,支援batched generation與完整圖的torch.compile,適合大規模合成語音資料集,也方便研究者直接拿原生PyTorch程式碼去研究或改造模型。因為Phonon建立在Pocket TTS系列之上,團隊先把Pocket TTS加進Transformers,Phonon再以模組化模型的形式疊上去,只需約200行程式碼描述差異之處。Phonon是自回歸(autoregressive)生成音訊latent:每一步輸出一個latent,再餵回去當下一步的輸入,訓練loss也算在這些latent上,而負責在音訊與latent之間轉換的codec,扮演的角色就相當於語言模型裡的tokenizer。在Transformers裡,它確實被包裝成一個audio tokenizer,由processor和文字tokenizer並列持有。一段語音不是錄音,而是一個speaker latent張量,voice是預先算好的,Phonon本身的audio tokenizer只能decode、不會直接編碼音訊。prompt的排列方式(語音位置、文字、再加上開啟音訊的token)會隨checkpoint一起以chat template的形式提供,寫法和其他Transformers裡的多模態模型一致。

📊 **在Open TTS Leaderboard上的成績**

Hugging Face的Open TTS Leaderboard是個很新的專案,目前Hub上有超過9,000個TTS模型,這個排行榜讓開發者能在同一個地方比較開放模型並直接聽聲音。評測涵蓋23種語言,指標包括intelligibility(輸出的word error rate)、速度(inverse real-time factor與time-to-first audio)與自然度(英文用UTMOS、韓文用KOMOS),同時評估固定語音與voice cloning,voice cloning還多了一項speaker similarity指標。在intelligibility上,Phonon在德文與西班牙文排名第一,在所評測的每種語言都進到前三,對手裡不乏體積比它大上百倍的模型;在速度上,Phonon在CPU串流基準的time-to-first audio上排名第一,是它表現最突出的地方。上線兩週,Phonon下載量已超過20萬次,目前仍在Hugging Face上維持熱門。文章也提到幾個第三方示範:在關掉Wi-Fi的Apple Watch上逐步講解咖啡沖泡步驟、在沒訊號的iPhone上計算運動次數、一個叫Lamp的機器人用角色語氣講話、瀏覽器裡離線的恐龍跑酷遊戲變成電臺節目,以及逐頁念出的《追憶似水年華》。

🎯 **實務啟示**

如果你要做的是裝置端、不依賴網路、又在意隱私的語音功能,Phonon 31m的Apache 2.0授權讓你可以直接商用;若需要多語言或客製語音,要留意40m版本是CC BY-NC,商用需另外談Gradium的按使用者數計價方案。想整合進既有PyTorch pipeline或拿來做大規模語音資料集合成的,可以從🤗Transformers v5.21的實作入手；要做純裝置端單一串流的即時應用,則該看ptts這套多後端推理框架。

🔗 **來源**
- 標題:A Closer Look at Phonon TTS. Launching High-Quality On-Device Speech That Tops the Benchmarks.
- 作者/機構:Olesia Krizhevich、Laurent Mazare、Eric Bezzam、Eustache Le Bihan(Gradium)
- 連結:https://huggingface.co/blog/phonon-tts

#TTS #OnDeviceAI #OpenSource #Gradium #HuggingFace #FlowMatching #SpeechAI #EdgeAI #VoiceCloning #Transformers
