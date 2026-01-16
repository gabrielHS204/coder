import speech_recognition as sr
import keyboard
from config import DEBUG

recognizer = sr.Recognizer()

def ouvir_push_to_talk():
    if DEBUG:
        print("[DEBUG] Segure ESPAÇO para falar")

    # Espera apertar espaço
    keyboard.wait("space")

    if DEBUG:
        print("[DEBUG] ESPAÇO pressionado → ouvindo")

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        audio = recognizer.listen(source)

    # Espera soltar espaço
    keyboard.wait("space", suppress=False)

    if DEBUG:
        print("[DEBUG] ESPAÇO solto → processando")

    try:
        texto = recognizer.recognize_google(audio, language="pt-BR")

        if DEBUG:
            print(f"[DEBUG] Texto reconhecido: '{texto}'")

        return texto.lower()

    except:
        if DEBUG:
            print("[DEBUG] Não foi possível reconhecer a fala")
        return ""
