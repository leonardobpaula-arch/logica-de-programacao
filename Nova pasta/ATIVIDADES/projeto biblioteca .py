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


def janela_bemvindo():

    
    janela = tk.Tk()
    janela.title("Exemplo 2")
    janela.geometry("300x300")
    janela.configure(bg="light green")

    
    
    lbl_mensagem = tk.Label(janela, text="digite sua categoria")
    lbl_mensagem.grid(row=0, column=0, pady=50, padx=50)

    categoria_usuario = tk.Entry(janela, font=("Arial", 12))
    categoria_usuario.grid(row=0, column=1, pady=50, padx=50)

    btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
    btn_mensagem.grid(row=2, column=0, pady=10, padx=10)





    categoria = categoria_usuario.get()

    if categoria == "aluno":
        messagebox.showinfo("Você está logado como aluno")

    elif categoria == "comunidade geral":
        messagebox.showinfo("Você está logado como comunidade geral")
    else:
        messagebox.showwarning("aviso", "digite sua categoria")



    janela.mainloop()