# Regras de Negócio (O que o sistema deve fazer):

# 1. Classificação do Usuário: A biblioteca atende [1] Alunos e [2] Comunidade
# Geral.
# 2. Limite de Dias: * Alunos podem ficar com o livro por até 14 dias de graça.
# A Comunidade Geral pode ficar por até 7 dias de graça.
# 3. Taxa de Renovação: Se o usuário quiser ficar mais tempo do que o limite do seu
# perfil, será cobrada uma taxa fixa de R$ 5,00 por dia adicional.
# 4. Restrição de Categoria: Livros da categoria "Raros" não podem ser emprestados
# para a Comunidade Geral, apenas para Alunos.


import tkinter as tk
from tkinter import messagebox

def validar_emprestimo():
    tipo_usuario = usuario_var.get()
    categoria = categoria_var.get()
    
    try:
        dias = int(entry_dias.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido de dias.")
        return

    if categoria == "Raro" and tipo_usuario == "Comunidade Geral":
        resultado.set("Empréstimo negado.\nLivros raros são exclusivos para alunos.")
        return

    if tipo_usuario == "Aluno":
        limite = 14
    else:
        limite = 7

    if dias <= limite:
        resultado.set("Empréstimo aprovado sem taxa.")
    else:
        taxa = (dias - limite) * 5
        resultado.set(
            f"Empréstimo aprovado com taxa.\n"
            f"Valor da taxa: R$ {taxa:.2f}"
        )
janela = tk.Tk()
janela.title("Biblioteca Comunitária")
janela.geometry("500x500")


tk.Label(janela, text="Tipo de Usuário").pack(pady=5)

usuario_var = tk.StringVar(value="Aluno")

tk.Radiobutton(
    janela, text="Aluno",
    variable=usuario_var, value="Aluno"
).pack()

tk.Radiobutton(
    janela, text="Comunidade Geral",
    variable=usuario_var, value="Comunidade Geral"
).pack()

tk.Label(janela, text="Categoria do Livro").pack(pady=5)

categoria_var = tk.StringVar(value="Comum")

tk.OptionMenu(
    janela,
    categoria_var,
    "Comum",
    "Raro"
).pack()

tk.Label(janela, text="Quantidade de Dias").pack(pady=5)

entry_dias = tk.Entry(janela)
entry_dias.pack()

tk.Button(
    janela,
    text="Validar Empréstimo",
    command=validar_emprestimo
).pack(pady=10)

resultado = tk.StringVar()
tk.Label(
    janela,
    textvariable=resultado,
    fg="blue",
    justify="center").pack(pady=10)

janela.mainloop()
