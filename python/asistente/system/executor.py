import subprocess
from config import DEBUG
import webbrowser

def pesquisar_no_google(termo):
    url = f"https://www.google.com/search?q={termo.replace(' ', '+')}"

    if DEBUG:
        print(f"[DEBUG] Abrindo navegador com URL: {url}")

    webbrowser.open(url)


def abrir_programa(nome):
    programas = {
        "chrome": r"c:\Users\guisa\AppData\Local\Programs\Opera GX\opera.exe",
        "vscode": r"c:\Users\guisa\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk",
        "explorer": "explorer",
        "musica": r"c:\Users\guisa\AppData\Roaming\Spotify\Spotify.exe"
    }

    if nome in programas:
        if DEBUG:
            print(f"[DEBUG] Executando programa: {programas[nome]}")

        subprocess.Popen(programas[nome])
        return True

    if DEBUG:
        print("[DEBUG] Programa não encontrado na lista segura")

    return False
