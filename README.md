# 🕌 KhutbaBox – Live Transcription & Translation for Mosques or Events (Offline)

A simple tool for Raspberry Pi & co. that **records speech live**, **transcribes it**, and **translates it if needed** – e.g. from Arabic to German.  
The idea came to me during Friday prayer, hence the name.

**Perfect for use in mosques** with a projector or display.  
Completely **offline-capable** – no cloud, no internet connection required.

---

⚠️ **Note:** This project is still under development.  
Processing – especially with larger Whisper models – is **not in real time** and may have a delay of 10–30 seconds.  
But everything runs locally, privacy-friendly, and without any internet.

---

## 🛠️ Requirements

- 🐍 Python 3.11+
- 🎤 `arecord` for audio recording (e.g. with a USB microphone)
- 🧠 [`whisper.cpp`](https://github.com/ggerganov/whisper.cpp) (local speech-to-text model)
- 🔤 A model file like `ggml-small.bin` or `ggml-medium.bin`

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/khutbabox-transcriber.git
cd khutbabox-transcriber
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
2. Clone & build whisper.cpp
bash
Kopieren
Bearbeiten
git clone https://github.com/ggerganov/whisper.cpp.git
cd whisper.cpp
mkdir build && cd build
cmake ..
make
3. Place your desired model file
bash
Kopieren
Bearbeiten
mkdir -p ~/whisper.cpp/models
mv /path/to/ggml-small.bin ~/whisper.cpp/models/
Recommended: ggml-small.bin (smaller and faster)
```
## 🚀 Running the Application
```bash
python3 main.py
```
This will automatically start:

🎧 Audio recording + transcription loop

🌐 Flask web server on port 5050

🖥️ Beamer mode (display output)

Open the beamer view in your browser (on a second device or projector PC):

```bash
http://<IP-of-your-RaspberryPi>:5050/beamer
Or directly on the Pi:
```
```bash
http://localhost:5050/beamer
```
📺 The HTML template displays the latest translated statement, updating every 5 seconds.

🧠 Example Flow
---
You speak Arabic into the microphone
→ Whisper detects it and translates it into German
→ The translation is displayed on the projector

##Fully offline
Perfect for khutbas, talks, visitors, and non-Arabic speakers

⚠️ Known Limitations
---
❗ Delay: Especially with larger models, transcription takes more time

❗ --translate is not always accurate (expect imperfect grammar)

❗ Not true "live" – more like near-real-time processing

❗ No automatic language switching – Arabic must be set beforehand

🤝 Contribute & Support
---
If you use this project:

⭐️ Give it a star on GitHub

💬 Share your feedback
