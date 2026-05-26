#Tratamento de erros

# organizar de forma adequada o código é essencial para evitar erros e garantir que o programa funcione corretamente.
# O tratamento de erros é uma prática importante para lidar com situações inesperadas que podem ocorrer durante
# a execução do programa.

# "try" e "except" são estruturas usadas para capturar e lidar com erros de forma controlada. O código dentro do bloco
#  try é executado normalmente, mas se ocorrer um erro, o programa pula para o bloco except, onde você pode definir como
# lidar com o erro

# while True:
# try:
#     # Código que pode gerar um erro
#     numero = int(input("Digite um número: "))
#     resultado = 10 / numero
#     print(f"Erro: você deve digitar um número válido.")

# except ValueError:
#     print("Erro: você deve digitar um número válido.")

# except ZeroDivisionError:
#     print("Erro: não foi possivel dividir por zero.")

# except Exception as erro:
#     print(f"Ocorreu um erro inesperado: {erro}")
#     break

# print("Programa encerrado")




# Exercicio 1

# crie um algoritmo para calcular a média e trate o erro ao inserir valores errados.

# while 
# try:
#     numero1 = int(input("Digite um dos valores para calcular a sua média: "))
#     numero2 = int(input("Digite seu segundo valor: "))
#     resultado = numero1 + numero2 / 2
#     print(f"Erro: você deve digitar um numero válido")

# except ValueError:
#     print("Erro: ")
 
# #Erros comuns: 

# ZeroDivisionError? divisão por zero 
# ValueError: conversao de tipo inválido
# InterruptedError: acesso a índice fora do limite
# KeyboardInterrupt: acesso a chave inexistente em dicionário


# Escreva um programa que solicite ao usuário um número inteiro e calcule a media de uma
# lista de números. O programa deve tratar os seguintes erros:

# - ValueError: se o usuário digitar um valor que não seja um número inteiro.

# - ZeroDivisionError: se a lista de números estiver vazia.

# Len: retorna o numero de itens de um objeto. pode ser usado para obter o comprimento de uma string, lista, dicionário, etc.

# append: Adiciona  um item ao final de uma lista 

# while True:
# try:
#     print("Calculadora de Média em lista")
#     numero = int(input("Digite um número inteiro para definir o tamanho da lista: "))
#     lista = []

# for listagem in range (numero):
#     numero_lista = float(input(f"Digite o número {listagem + 1}: "))
#     lista.append(numero_lista)

# media = sum(lista) / len(lista)
# print(f"A média dos numeros é: {média}")

# except ValueError:
# print("Erro: você deve digitar um número inteiro")
# break

# except ZeroDivisionError:
# print("Erro: A lista de números está vazia. Não é possível calcular a média. ")
# break

# print("Programa encerrado.")



# Exercicio 3
# Escreva um programa que solicite ao usuário uma lista de palavras e conte quantas vezes cada palavra aparece na lista.
# O programa deve tratar os seguintes erros

# - ValueError: se o usuário digitar um valor que não seja uma string.

try:
    palavra - input("Digite uma lista de palavras separadas por espaço").split()
    contagem = {}

    for palavra in palavra:
        if palavra in contagem:
            contagem[lista] += 1

        else:
            contagem[lista] = 1
            print("Contagem de palavras: ")
            for palavra,  contagem in contagem, itens():
                print(f"{palavra}: {contagem}")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite uma lista de espaço.")