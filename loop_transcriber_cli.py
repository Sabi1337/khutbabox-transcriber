import os
import time
import subprocess
from datetime import datetime

DEVICE = "hw:2,0"  # dein Mikrofon-Gerät
DURATION = 5       # Sekunden pro Aufnahme
MODEL_PATH = "../models/ggml-tiny.bin"  # oder ggml-tiny.en.bin je nach Sprache
LANG = "de"        # Sprache manuell festlegen
SAVE_FOLDER = "recordings"

os.makedirs(SAVE_FOLDER, exist_ok=True)

print("🎙️ Starte Transkriptionsschleife. STRG+C zum Beenden.\n")

try:
    while True:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        wav_path = os.path.join(SAVE_FOLDER, f"recording_{timestamp}.wav")
        txt_path = wav_path + ".txt"

        print(f"🎧 Nehme {DURATION}s auf → {wav_path}")
        subprocess.run(["arecord", "--device=" + DEVICE, "-f", "cd", "-d", str(DURATION), wav_path])

        print("🧠 Transkribiere Audio …")
        subprocess.run([
            "./bin/whisper-cli",
            "-m", MODEL_PATH,
            "-f", wav_path,
            "-otxt",
            "-l", LANG
        ])

        print(f"📄 Ausgabe gespeichert in: {txt_path}")
        print("⏳ Warte kurz...\n")
        time.sleep(2)  # kleine Pause vor nächster Runde

except KeyboardInterrupt:
    print("\n👋 Aufnahme beendet.")
