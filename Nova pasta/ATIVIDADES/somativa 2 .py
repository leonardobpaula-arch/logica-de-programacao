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


# import tkinter as tk
# from tkinter import messagebox, ttk


# def janela_bemvindo():
#     peça1 = int(qualidade_peça1.get())
#     peça2 = int(qualidade_peça2.get())
#     peça3 = int(qualidade_peça3.get())
#     resultado = peça1 + peça2 + peça3


#     if peça1 == "" and peça2 == "" and peça3 == "":
#         messagebox.showwarning("Aviso", f"Digite a qualidade das peças! ")
#     else:
#         messagebox.showinfo("Informação", f"A média de qualidade foi de {resultado /3} ")


# janela = tk.Tk()
# janela.title("Exemplo 2")
# janela.geometry("500x300")
# janela.configure(bg="green")


# lbl_peça1= tk.Label(janela, text="Digite a qualidade da peça um (de 0 a 10) ")
# lbl_peça1.grid(row=0, column=0, pady=15, padx=15)
# lbl_peça2 = tk.Label(janela, text="Digite a qualidade da peça dois (de 0 a 10) ")
# lbl_peça2.grid(row=1, column=0, pady=15, padx=15)
# lbl_peça3 = tk.Label(janela, text="Digite a qualidade da peça três (de 0 a 10)")
# lbl_peça3.grid(row=2, column=0, pady=15, padx=15)


# qualidade_peça1 = tk.Entry(janela, font=("Arial", 12))
# qualidade_peça1.grid(row=0, column=1, pady=15, padx=15)
# qualidade_peça2 = tk.Entry(janela, font=("Arial", 12))
# qualidade_peça2.grid(row=1, column=1, pady=15, padx=15)
# qualidade_peça3 = tk.Entry(janela, font=("Arial", 12))
# qualidade_peça3.grid(row=2, column=1, pady=15, padx=15)


# btn_mensagem = tk.Button(janela, text="registrar", command=janela_bemvindo)
# btn_mensagem.grid(row=3, column=0, pady=15, padx=15)

# janela.mainloop()


# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".


# import tkinter as tk
# from tkinter import messagebox, ttk


# def janela_bemvindo():
    
#     temperatura = int(valor_temperatura.get())


#     if temperatura == "":
#         messagebox.showwarning("Aviso", f"Digite o valor da temperatura! ")
#     elif temperatura < 40:
#         messagebox.showwarning("Atenção", f"O motor está com carga baixa ")
#     elif 40 >= temperatura <= 70:
#         messagebox.showinfo("informação", f"O motor está funcionando normalmente")
#     elif temperatura >= 70:
#         messagebox.showwarning("Atenção", f"Resfriamento ativado excesso de calor")
#     else:
#         messagebox.showwarning("Erro")


# janela = tk.Tk()
# janela.title("Exemplo 2")
# janela.geometry("500x300")
# janela.configure(bg="green")


# lbl_idade = tk.Label(janela, text="Digite qual a temperatura ")
# lbl_idade.grid(row=1, column=0, pady=15, padx=15)


# valor_temperatura = tk.Entry(janela, font=("Arial", 12))
# valor_temperatura.grid(row=1, column=1, pady=15, padx=15)

# btn_mensagem = tk.Button(janela, text="registrar", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=15, padx=15)

# janela.mainloop()


# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".


# import tkinter as tk
# from tkinter import messagebox, ttk


# def janela_bemvindo():
    
#     lote = tipo_lote.get()

#     if lote == "":
#         messagebox.showwarning("Aviso", f"Digite o lote! ")
#     elif lote == "a":
#         messagebox.showinfo("informação", f"Lote de alimentos selecionado")
#     elif lote == "b":
#         messagebox.showinfo("informação", f"Lote de eletrônicos selecionado")
#     else:
#         messagebox.showwarning("atenção", f"Desconhecido")

     

# janela = tk.Tk()
# janela.title("Exemplo 2")
# janela.geometry("500x300")
# janela.configure(bg="green")


# lbl_idade = tk.Label(janela, text="Digite qual lote você deseja")
# lbl_idade(row=1, column=0, pady=15, padx=15)


# tipo_lote = tk.Entry(janela, font=("Arial", 12))
# tipo_lote.grid(row=1, column=1, pady=15, padx=15)

# btn_mensagem = tk.Button(janela, text="registrar", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=15, padx=15)

# janela.mainloop()


# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.

# import tkinter as tk
# from tkinter import messagebox, ttk


# def janela_bemvindo():
    
#     porta = sensor_porta.get()
#     botao = sensor_botao.get() 


#     if porta == "" and botao == "":
#         messagebox.showwarning("Aviso", f"Defina o estado atual da porta e do botão ")
#     elif porta == "aberta" and botao == "ligado":
#         messagebox.showwarning("Aviso", f"Impossivel prosseguir a porta está aberta e o botão de emergência está ativado! ")
#     elif porta == "aberta" and botao == "desligado":
#         messagebox.showwarning("atenção", f"A porta está aberta")
#     elif porta == "fechada" and botao == "ligado":
#         messagebox.showwarning("atenção", f"O botão de emergência está ligado")
#     elif porta == "fechada" and botao == "desligado":
#         messagebox.showinfo("informação", f"Prociga com a operação")    
#     else:
#         messagebox.showwarning("Aviso", f"Erro")

     

# janela = tk.Tk()
# janela.title("Exemplo 2")
# janela.geometry("500x300")
# janela.configure(bg="green")


# lbl_porta = tk.Label(janela, text="A porta está fechada ou aberta?")
# lbl_porta.grid(row=1, column=1, pady=15, padx=15)
# lbl_botao = tk.Label(janela, text="O botão está ligado ou desligado?")
# lbl_botao.grid(row=2, column=1, pady=15, padx=15)


# sensor_porta = tk.Entry(janela, font=("Arial", 12))
# sensor_porta.grid(row=1, column=0, pady=15, padx=15)
# sensor_botao = tk.Entry(janela, font=("Arial", 12))
# sensor_botao.grid(row=2, column=0, pady=15, padx=15)


# btn_mensagem = tk.Button(janela, text="registrar", command=janela_bemvindo)
# btn_mensagem.grid(row=3, column=0, pady=15, padx=15)

# janela.mainloop()


# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".



# 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.


# import tkinter as tk
# from tkinter import messagebox

# def validacao_dados():
#     # try:
#         entrada_medida_dados = float(ent_medida_peca.get())
#     # except ValueError:
#         if entrada_medida_dados == "":
#             messagebox.showwarning("Aviso!", "Verificar Dados!")
#         elif entrada_medida_dados >= 9.8 and entrada_medida_dados < 10.2:
#             messagebox.showinfo("Resultado", f"O calculo da medida foi {entrada_medida_dados}")
#         else:
#             messagebox.showerror("Erro", "Calculo aguardado")


# janela = tk.Tk()
# janela.title("Exercício 9")
# janela.geometry("500x500")

# lbl_medida_peca = tk.Label(janela, text="Validação de Peças")
# lbl_medida_peca.pack()

# ent_medida_peca = tk.Entry(janela)
# ent_medida_peca.pack()

# btn_enviar_validacao = tk.Button(janela, text="Calcular Valores", command=validacao_dados)
# btn_enviar_validacao.pack()

# janela.mainloop()