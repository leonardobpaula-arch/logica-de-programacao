#Atividade 1: Mensagem de Boas-Vindas
#Crie um script que use a função print() para exibir a mensagem "Bem-vindo ao mundo da
#programação em Python!".

#print("Bem vindo ao mundo da programação em python!")

# #Atividade 2: Informações Pessoais
# #Escreva um programa que imprima seu nome completo em uma linha e sua idade em outra linha.
# #Exemplo de saída:
# #Fulano de Tal
# #30

# pergunta1 = input("Digite seu nome")
# pergunta2 = int(input("Digite sua idade"))

# print("Seu nome é:" ,pergunta1)

# print("sua ideda é" ,pergunta2 )

# #Atividade 3: Calculadora de Soma e Subtração
# #Crie um script que exiba o resultado da soma de 135 com 246 e o resultado da subtração de 512
# #por 128. Cada resultado deve ser exibido em uma linha separada.
# #● Dica: Use o print() diretamente com os operadores (print(135 + 246)).
# #● Obs: Realize também a mesma situação com variáveis

# soma1 = int(input("Digite o primeiro valor"))
# soma2 = int(input("Digite o segundo valor"))

# formula = input("Digite + para soma ou - para subtração")

# if formula == "+":
#     print("seu resultado é" ,soma1 + soma2)

# elif formula == "-":
    # print("Seu resultado é" ,soma1 - soma2)

#Atividade 4: Multiplicação e Divisão
#Escreva um programa que mostre o resultado da multiplicação de 15 por 8 e o resultado da
#divisão de 78 por 3.

#soma1 = float(input("Digite o primeiro valor"))
# soma2 = float(input("Digite o segundo valor"))

# formula = input("Digite * para multiplicação ou / para divisão")

# if formula == "*":
#     print("seu resultado é" ,soma1 * soma2)

# elif formula == "/":
#     print("Seu resultado é" ,soma1 / soma2)

# Atividade 5: Potenciação
# Calcule e exiba o resultado de "5 elevado à 3a potência" (53).
# ● Dica: O operador de potenciação em Python é **.

#soma = float(input("Digite o primeiro valor"))
# potência = float(input("Digite o valor do expoente"))

# print("seu resultado é:" , soma ** potência)

# Atividade 6: Concatenando Palavras
# Crie um script que declare o seu primeiro nome em uma string e seu sobrenome em outra. Use
# o operador + para concatenar (juntar) as duas strings e exibir seu nome completo.
# ● Exemplo: print("Maria" + " " + "Silva")

# nome = input("Digite seu nome")
# sobrenome = input("Digite seu sobrenome")

# print(nome + sobrenome)

# Atividade 7: Cálculo de Eficiência (OEE)
# ● Peça a quantidade de peças produzidas e a quantidade de peças defeituosas. Calcule
# e exiba a taxa de aproveitamento (peças boas / total).

# peçaboa = int(input("Quantas peças possuem a qualide esperada?"))

# peçaruim = int(input("Quantas peças ruins foram descartadas feitas?"))

# print("A eficiência foi de" , peçaboa - peçaruim , "peças")

# Atividade 8: Descrição com Cálculos
# Crie um script que exiba a seguinte frase, substituindo os cálculos pelos seus resultados:
# "Eu tenho 25 anos e, em 10 anos, terei 35 anos."
# ● Dica: Use a vírgula dentro do print() para combinar strings e cálculos.
# ● Ex: print("Texto", 25 + 10).

# print("Eu tenho 16 anos e em 10 anos terei" , 16 + 10 , "anos")

# Atividade 9: Orçamento de Viagem (Cálculo com float)
# Imagine que você está planejando uma viagem. O custo do hotel é de R$ 250.50 por noite e
# o custo da passagem é R$ 412.00. Calcule e exiba o custo total para uma viagem por noites.
# ● Ex: Fórmula: (custo_hotel * 3) + custo_passagem

# passagem = float(input("Digite o valor da passagem"))
# noites = float(input("Digite quantas noites vai passar"))

# print("O valor total será de" , 250.50 * noites + passagem)

# Atividade 10: Desafio - Mini Relatório
# Crie um script que imprima um pequeno relatório. Use print() várias vezes para formatar a
# saída de forma organizada.
# ● Exemplo de saída:

# ==========================
# Relatório de Vendas
# ==========================
# Produto: Notebook Gamer
# Quantidade vendida: 15
# Preço unitário: R$ 5499.50
# Total de vendas: R$ 82492.50
# ==========================

# produto = input("Digite qual o produto?")
# quantidade = int(input("Quantas quantidades desse produto foram vendidas?"))
# preço = float(input("Qual o valor do produto?"))


# print(" ==========================")
# print(" RELATÓRIO DE VENDAS")
# print(" ==========================")
# print(" Produto:" , produto)
# print(" Quantidade vendida:" , quantidade)
# print("Preço unitário: R$" , preço)
# print("total de vendas: R$" , preço * quantidade)
