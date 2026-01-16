from voice.listen import ouvir_push_to_talk
from voice.speak import falar
from nlp.interpreter import interpretar, extrair_termo_pesquisa, identificar_programa
from system.executor import pesquisar_no_google, abrir_programa
from web.google_search import pesquisar_wikipedia
from config import DEBUG

if DEBUG:
    print("[DEBUG] Assistente iniciado em modo Push-to-Talk")

falar("Assistente iniciado. Segure espaço para falar.")

while True:
    texto = ouvir_push_to_talk()

    if not texto:
        continue

    if "sair" in texto:
        falar("Até logo.")
        break

    intencao, conteudo = interpretar(texto)

    if intencao == "pesquisar":
        termo = extrair_termo_pesquisa(conteudo)

        if DEBUG:
            print(f"[DEBUG] Termo final: {termo}")

        falar(f"Pesquisando por {termo}")
        pesquisar_no_google(termo)
        resposta = pesquisar_wikipedia(termo)

        if resposta:
            falar(resposta)
        else:
            falar("Não encontrei um resumo confiável.")

    elif intencao == "abrir_programa":
        programa = identificar_programa(texto)

        if programa:
            if programa == "musica":
                falar("Abrindo Spotify para tocar música.")
            elif programa == "chrome":
                falar("Abrindo navegador.")
            elif programa == "vscode":
                falar("Abrindo Visual Studio Code.")
            elif programa == "explorer":
                falar("Abrindo explorador de arquivos.")
            else:
                falar(f"Abrindo {programa}.")

            abrir_programa(programa)
        else:
            falar("Programa não reconhecido.")
