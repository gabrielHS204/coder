import tkinter as tk

# Função para processar os cliques nos botões


def click(botao, entrada):
    if botao == "=":
        try:
            resultado = eval(entrada.get())  # Avalia a expressão digitada
            entrada.delete(0, tk.END)  # Limpa o campo de entrada
            entrada.insert(tk.END, str(resultado))  # Exibe o resultado
        except Exception:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "Erro")  # Exibe mensagem de erro
    elif botao == "C":
        entrada.delete(0, tk.END)  # Limpa o campo de entrada
    else:
        entrada.insert(tk.END, botao)  # Adiciona número ou operador

# Função para criar os botões e adicionar à interface


def make_buttons(root, entrada):
    buttons = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ]

    for (text, row, col) in buttons:
        btn = tk.Button(
            root,
            text=text,
            padx=20,
            pady=20,
            font=("Arial", 14),
            # Vincula cada botão à função click
            command=lambda t=text: click(t, entrada)
        )
        # Posiciona o botão na grade
        btn.grid(row=row, column=col, sticky="nsew")

# Função para criar a janela principal


def make_root():
    root = tk.Tk()
    root.title("Calculadora")  # Título da janela
    root.geometry("300x400")  # Tamanho fixo da janela
    # Margens e cor de fundo
    root.config(padx=10, pady=10, background="#f5f5f5")
    root.resizable(False, False)  # Desabilita o redimensionamento da janela

    # Campo de entrada
    entrada = tk.Entry(root, font=("Arial", 18), width=16, justify="right")
    # Posiciona o campo no topo
    entrada.grid(row=0, column=0, columnspan=4, pady=10)

    # Adicionar botões
    make_buttons(root, entrada)
    return root
