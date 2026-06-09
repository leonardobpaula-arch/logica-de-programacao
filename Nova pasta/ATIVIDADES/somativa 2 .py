# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# import tkinter as tk
# from tkinter import messagebox, ttk


# def janela_bemvindo():
#     nome = nome_usuario.get()
#     turno = turno_usuario.get()



#     if nome == "" and turno == "":
#         messagebox.showwarning("Aviso", f"Digite seu nome e seu turno ")
#     else:
#         messagebox.showinfo("Bem-Vindo ", f"Operador, {nome} registrado no turno {turno} - boa jornada")


# janela = tk.Tk()
# janela.title("Exemplo 2")
# janela.geometry("500x300")
# janela.configure(bg="green")


# lbl_mensagem = tk.Label(janela, text="Digite seu nome ")
# lbl_mensagem.grid(row=0, column=0, pady=11, padx=11)
# lbl_idade = tk.Label(janela, text="Digite seu turno ")
# lbl_idade.grid(row=1, column=0, pady=11, padx=11)


# nome_usuario = tk.Entry(janela, font=("Arial", 12))
# nome_usuario.grid(row=0, column=1, pady=11, padx=11)
# turno_usuario = tk.Entry(janela, font=("Arial", 12))
# turno_usuario.grid(row=1, column=1, pady=11, padx=11)

# btn_mensagem = tk.Button(janela, text="registrar", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=11, padx=11)

# janela.mainloop()


# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.


# import tkinter as tk
# from tkinter import messagebox, ttk


# def janela_bemvindo():
#     horas = int(quantidade_horas.get())
#     peças = int(quantidade_peças.get())


#     if horas == "" and peças == "":
#         messagebox.showwarning("Aviso", f"Digite quantidade de horas e de peças! ")
#     else:
#         messagebox.showinfo("Informação", f"foram feitas,{horas * peças} peças em {horas} horas")


# janela = tk.Tk()
# janela.title("Exemplo 2")
# janela.geometry("500x300")
# janela.configure(bg="green")


# lbl_mensagem = tk.Label(janela, text="Digite quantas horas de produção ")
# lbl_mensagem.grid(row=0, column=0, pady=15, padx=15)
# lbl_idade = tk.Label(janela, text="Digite quantas peças foram produzidas por 1 hora ")
# lbl_idade.grid(row=1, column=0, pady=15, padx=15)


# quantidade_horas = tk.Entry(janela, font=("Arial", 12))
# quantidade_horas.grid(row=0, column=1, pady=15, padx=15)
# quantidade_peças = tk.Entry(janela, font=("Arial", 12))
# quantidade_peças.grid(row=1, column=1, pady=15, padx=15)

# btn_mensagem = tk.Button(janela, text="registrar", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=15, padx=15)

# janela.mainloop()


# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.


# import tkinter as tk
# from tkinter import messagebox, ttk


# def janela_bemvindo():
#     psi = 14.5
#     bar = float(valor_bar.get())


#     if bar == "" and psi == "":
#         messagebox.showwarning("Aviso", f"Digite o valor de Bar! ")
#     else:
#         messagebox.showinfo("informação", f"A conversão resultou em {bar * psi} PSI ")


# janela = tk.Tk()
# janela.title("Exemplo 2")
# janela.geometry("500x300")
# janela.configure(bg="green")


# lbl_idade = tk.Label(janela, text="Digite qual o valor de Bar ")
# lbl_idade.grid(row=1, column=0, pady=15, padx=15)


# valor_bar = tk.Entry(janela, font=("Arial", 12))
# valor_bar.grid(row=1, column=1, pady=15, padx=15)

# btn_mensagem = tk.Button(janela, text="registrar", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=15, padx=15)

# janela.mainloop()


# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.


import tkinter as tk
from tkinter import messagebox, ttk


def janela_bemvindo():
    peça1 = int(qualidade_peça1.get())
    peça2 = int(qualidade_peça2.get())
    peça3 = int(qualidade_peça3.get())


    if peça1 == "" and peça2 == "" and peça3 == "":
        messagebox.showwarning("Aviso", f"Digite a qualidade das peças! ")
    else:
        messagebox.showinfo("Informação", f"A média de qualidade foi de {peça1 + peça2 + peça3 / 3} ")


janela = tk.Tk()
janela.title("Exemplo 2")
janela.geometry("500x300")
janela.configure(bg="green")


lbl_peça1= tk.Label(janela, text="Digite a qualidade da peça um (de 0 a 10) ")
lbl_peça1.grid(row=0, column=0, pady=15, padx=15)
lbl_peça2 = tk.Label(janela, text="Digite a qualidade da peça dois (de 0 a 10) ")
lbl_peça2.grid(row=1, column=0, pady=15, padx=15)
lbl_peça3 = tk.Label(janela, text="Digite a qualidade da peça três (de 0 a 10)")
lbl_peça3.grid(row=2, column=0, pady=15, padx=15)


qualidade_peça1 = tk.Entry(janela, font=("Arial", 12))
qualidade_peça1.grid(row=0, column=1, pady=15, padx=15)
qualidade_peça2 = tk.Entry(janela, font=("Arial", 12))
qualidade_peça2.grid(row=1, column=1, pady=15, padx=15)
qualidade_peça3 = tk.Entry(janela, font=("Arial", 12))
qualidade_peça3.grid(row=2, column=1, pady=15, padx=15)


btn_mensagem = tk.Button(janela, text="registrar", command=janela_bemvindo)
btn_mensagem.grid(row=3, column=0, pady=15, padx=15)

janela.mainloop()