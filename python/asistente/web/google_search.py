import wikipedia
from config import DEBUG

wikipedia.set_lang("pt")

def pesquisar_wikipedia(termo):
    try:
        if DEBUG:
            print(f"[DEBUG] Buscando na Wikipedia: {termo}")

        resumo = wikipedia.summary(termo, sentences=3)
        return resumo

    except wikipedia.exceptions.DisambiguationError as e:
        return f"O termo {termo} pode se referir a várias coisas. Seja mais específico."

    except wikipedia.exceptions.PageError:
        return None
