import pyttsx3
from config import DEBUG

engine = pyttsx3.init(driverName="sapi5")

engine.setProperty("rate", 180)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # voz padrão PT-BR se existir

def falar(texto):
    if not texto:
        if DEBUG:
            print("[DEBUG] Nenhum texto para falar")
        return

    if DEBUG:
        print(f"[DEBUG] Falando texto: {texto[:60]}...")

    engine.say(texto)
    engine.runAndWait()
