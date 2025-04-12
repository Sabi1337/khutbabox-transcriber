import sounddevice as sd
import soundfile as sf
import whisper
import time
from translate_local import übersetze_offline

model = whisper.load_model("tiny")

def aufnehmen(dateiname="loop.wav", dauer=15):
    fs = 16000
    print("🎙 Aufnahme...")
    aufnahme = sd.rec(int(dauer * fs), samplerate=fs, channels=1)
    sd.wait()
    sf.write(dateiname, aufnahme, fs)

def transkribieren(dateiname="loop.wav", sprache="tr"):
    print("🧠 Transkription läuft...")
    result = model.transcribe(dateiname, language=sprache)
    return result["text"]

def schreibe_in_buffer(original, übersetzung):
    with open("textbuffer.txt", "w") as f:
        f.write("###ORIGINAL###\n")
        f.write(original.strip() + "\n")
        f.write("###UEBERSETZT###\n")
        f.write(übersetzung.strip())

def main_loop():
    while True:
        aufnehmen()
        original = transkribieren()
        übersetzt = übersetze_offline(original)
        schreibe_in_buffer(original, übersetzt)
        print("🔁 Warte auf nächsten Zyklus...\n")
        time.sleep(1)  # Mini-Pause bevor nächste Runde

if __name__ == "__main__":
    main_loop()
