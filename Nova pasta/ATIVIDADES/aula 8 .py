# Exercícios de Programação Python: "O Caça-Erros"

# 1. O Problema da Idade

# idade = input("Digite sua idade:")

# if idade >= 18:
#     print("Você é maior de idade.")


# correção


# idade = int(input("Digite sua idade"))

# if idade >= 18:
#     print("Você é maior de idade")


# melhorado


# idade = int(input("Digite sua idade"))

# if idade >= 18:
#     print("Você é maior de idade")

# else:
#     print("Você é menor de idade")


# 2. A Escrita Fiel

# nome = "Mariana"
# print("Seja bem vinda, nome!")

# correção

# nome = "Mariana"

# print("Seja bem vinda", nome, "!")

# 3 melharado

# nome = input("Digite seu nome")

# print("Seja bem vinda", nome, "!")


# 3. Falta de Espaço

# numero = 10

# if numero > 5:
#     print("O número é maior que cinco.")

# else:
#     print("O número é menor que ou igual a cinco.")

# correção 

# numero = int(input("Digite um numero entre 0 a 10"))

# if numero >= 6:
#     print("O número é maior que cinco.")

# else:
#     print("O número é menor ou igual a cinco.")

# melhorado












# 4. Esquecimento Fatal


# usuario = "aluno123"
# if usuario == "aluno123"
# print("Login realizado com sucesso")


# correção


# usuario = "aluno123"

# if usuario == "aluno123":
#     print("Login realizado com sucesso")


# melhorado


# usuario = input("Digite sua senha")

# if usuario == "aluno123":
#     print("Login realizado com sucesso")

# else:
#     print("Senha incorreta tente novamente")


# 5. Atribuição vs. Comparação


# clima = "ensolarado"
# if clima = "chuvoso":
# print("Leve um guarda-chuva!")


# correção


# clima = "ensolarado"

# if clima == "chuvoso":
#     print("Leve um guarda chuva!")


# melhorado


# clima = input("Como está o clima?")

# if clima == "Chuvoso":
#     print("Leve um guarda chuva")

# elif clima == "Ensolarado":
#     print("Leve um óculos de sol")

# else:
#     print("Aproveite o dia")


# 6. Misturando Alhos com Bugalhos


# pontos = 50
# print("Parabéns! Você fez" + pontos+"pontos.")


#correção


# pontos = 50
# print("Parabéns! Você fez", pontos,"pontos")


#melhorado


# pontos = input("Digite quantos pontos você ganhou")
# print("Parabéns! Você fez", pontos,"pontos")



# 7. A Ordem dos Fatores
# O sistema deve dar "exelente" para notas 9 ou 10.


# nota = 9.5

# if nota >=7:
#     print("Aprovado")

# elif nota >=9:
#     print("Excelente!")


#correção


# nota = 9.5

# if 7 >= nota <=9:
#     print("Aprovado")

# elif nota >=9:
#     print("Excelente!")


# melhorado


# nota = float(input("Digite sua nota de 0 a 10"))

# if nota <= 4.5:
#     print("Recuperção")

# elif 5 >= nota <=7:
#     print("Na média")

# elif 7.5 >= nota <=9:
#     print("Aprovado")

# elif nota >=9:
#     print("Excelente")

# else:
#     print("algo deu errado! insira outro valor")



# 8. O Contador de 1 a 5

# for i in range(5):
#     print(i)

#correção


# for i in range(1,6):
#     print(i)


#melhorado

# for i in range(1,6):
#     print("número", (i), "...")


# 9. O Loop Eterno

# tentativas = 1
# while tentativas <= 3:
#     print("Tentando conectar...")


#correção


# tentativas = 1
# while tentativas <= 3:
#     print("Tentando conectar...")
#     tentativas += 1


#melhorado









# 10. A Senha Teimosa
# O programa deve pedir a senha até que o usuário digite "python123"


# senha = ""

# while senha == "phyton123":
#     print("Acesso concedido!")


# correção


senha = input("Digite sua senha")

while senha == "phyton123":
    print("Acesso concedido")

    break

print("Acesso negado")


#melhorado

# print("")
# senha = ("Digite sua senha")


