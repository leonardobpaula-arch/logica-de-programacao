# clean code - aula 6
# para que usar?
# como usar
# print("Clean code - Aula 6")
# aula = 6
# print(f"Estamos na aula {aula} de clean code")

# texto = " Python é muito legal! "
# print(texto.strip().upper())
# print(texto.strip().lower())
# print(texto.strip().capitalize())
# print(texto.strip().title())
# print(texto.strip().replace(" ", "-"))
# print(texto.strip().split())

#escrevendo

# with open("notas.txt", "w") as arquivo:
#     arquivo.write("Estudar Python hoje!")
#     arquivo.write("\nler sobre Clean code.")

# #ler

# with open("notas.txt", "r")as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# Exercicio 1:

# Crie um programa que peça ao ausuário para inserir uma frase e, em seguida, exiba a frase com as seguintes transformações:
# - remova os espaços extras no inicio e no final da frase.

# frase = input("Escreva uma frase")

# print(frase.strip().replace(" ", ""))

# Exemplo 1

# Crie um programa que leia o conteúdo de um arquivo de texto e conte quantas vezes a palavra "Python" aparece no arquivo.
# Exiba o resultado para o usuário.

# print("Contagem de palavras em arquivo")
# with open("notas.txt", "r")as arquivo:
#     conteudo = arquivo.read()
#     contagem = conteudo.count("Python")
#     print(f"A contagem de palavras {contagem} é de ...")


# import os
# print(os.getcwd())

# print(os.listdir())
# print(os.listdir(".."))
# print(os.listdir("..\\.."))
# print(os.listdir("C:\\"))
# print(os.listdir("C:\\Users"))
# print(os.listdir("C:\\Users\\Public"))

# os.mkdir("nova_pasta")

# os.rename("nova_pasta", "pasta_renomeada")

# os.rmdir("pasta_renomeada")

# Exercicio 2

# crie um script que mostre o caminho da pasta atual.

# import os
# print(os.getcwd)

# Exercicio 3

# liste os arquivos da pasta atual.

# print(os.listdir())

# Exercicio 4

# Crie uma pasta chamada "projetos" e depois renomeie para "meus_projetos". Por fim, exclua a pasta

# os.mkdir("nova_pasta")

# os.rename("nova_pasta", "si")

# os.rmdir("si")

# Exercicio 5

# Crie um arquivo chamado "log.txt" e escreva a mensagem "log de atividades".
# Depois, leia o conteúdo do arquivo e exiba na tela

# with open("log.txt", "w") as arquivo:
#     arquivo.write("log de atividades")

# with open("log.txt", "r")as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# Exemplo de dicionário:

# pessoa = {
#     "nome": "Alice",
#     "idade": 30,
#     "cidade": "São Paulo",
#     "profissão": "Engenheira"
# }
# pessoa2 = {
#     "nome": "Bruno",
#     "idade": 25,
#     "cidade": "SP",
#     "profissão": "Designer"

# }
# print(pessoa ["profissão"])
# print(pessoa2 ["nome"], pessoa["idade"])



# comida = {
#     "nome": "frango frito",
#     "ingredientes": "frango, frito",
#     "sabor": "frango e fritura",
# }

# comida2 = {
#     "nome": "bife",
#     "ingredientes": "carne, panela",
#     "sabor": "delicia"
# }
# print


# Exemplo 2: Desligar o PC (comando para windows)
with open("desliga.bat", "w") as desligar:
    desligar.write("shutdown -s -t 60 -c \"Desligamento programado para daqui a 1 hora. salve seu trabalho!\"")

    # -s comando pra desligar
    # -t tempo definir
    # -a cancelar desligamento