from rapidfuzz import fuzz
from config import DEBUG

INTENCOES = {
    "abrir_programa": ["abrir", "executar", "iniciar"],
    "pesquisar": ["pesquisar", "procurar", "buscar", "pesquisa"]
}

PROGRAMAS = {
    "chrome": ["chrome", "google", "navegador"],
    "vscode": ["vscode", "visual studio code", "code"],
    "explorer": ["explorador", "arquivos", "pasta"],
    "musica": ["spotify", "musica", "tocar", "ouvir"],
}


def interpretar(texto):
    if DEBUG:
        print(f"[DEBUG] Interpretando texto: {texto}")

    for intencao, palavras in INTENCOES.items():
        for palavra in palavras:
            if palavra in texto:
                if DEBUG:
                    print(f"[DEBUG] Intenção detectada: {intencao}")
                return intencao, texto

    return None, texto


def extrair_termo_pesquisa(texto):
    removidos = [
        "pesquisar", "buscar", "procurar",
        "no google", "na internet", "sobre"
    ]
    termo = texto.lower()
    for r in removidos:
        termo = termo.replace(r, "")
        return termo.strip()


def identificar_programa(texto):
    melhor_match = None
    melhor_score = 0

    for programa, aliases in PROGRAMAS.items():
        for alias in aliases:
            score = fuzz.partial_ratio(alias, texto)

            if DEBUG:
                print(
                    f"[DEBUG] Comparando '{alias}' com texto → score: {score}")

            if score > melhor_score and score > 80:
                melhor_score = score
                melhor_match = programa

    if DEBUG:
        print(f"[DEBUG] Programa identificado: {melhor_match}")

    return melhor_match
