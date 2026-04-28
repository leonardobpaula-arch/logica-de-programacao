# 1. O laço 'for' (repetições determinadas)
# Use p 'for' quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças)
# exemplo: Relatório de produção diária
# imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# Exemplo 1

# for lote in range(1, 6):
#     print(f"Processando lote número {lote}...")
#     print("Qualidade verificada. [OK]")
#     print("Produção do dia finalizada!")

# # Exemplo 2

# for b in range(10):
#     print(f"quantidade total {b} foi...")

# Exemplo 3

# for disco in range(1, 20):
#     print(f"Processando disco de vinil número {disco}...")
#     print("Qualidade verificada. [OK]")
# print("Produção do dia finalizada!")

# Exemplo 4

# peças = ["Engrenagens", "Eixo", "Rolamento", "Parafuso", "Martelo", "Prego", "Chave de fenda"]

# itempeças = ["Cilindricas", "Eixo cônico", "Radiais", "Madeira", "Bola", "Cabeça chata", "Chave metalica verde"]

# for item in peças:
#     print(f"Item em estoque: {item} e {itempeças}")

# Exemplo 5
# imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opção voçê deseja e a 
# partir da seleção ele listar os produtos

# print("Loja de ferramenta")
# print("Opção 1- peças")
# print("Opção 2- itempeças")

# menu = int(input("escolha uma opção"))

# peças = ["Engrenagens", "Eixo", "Rolamento", "Parafuso", "Martelo", "Prego", "Chave de fenda"]

# itempeças = ["Cilindricas", "Eixo cônico", "Radiais", "Madeira", "Bola", "Cabeça chata", "Chave metalica verde"]

# if menu == 1:
#         print(f"Sua lista de peças {peças} são...")
# elif menu == 2:
#     print(f"Sua lista de itens de peças {itempeças} são...")
# else:
#     print("opção inválida: Encerrando o sistema")

# Exercício 1 

# 1. Contador de produção (for)
# Uma esteira processa 10 peças por ciclo. Crie um programa que use um for para contar 
# de 1 a 10 e, para cada número, imprima:


# for lote in range(1, 10):
#     print(f"Processando lote número {lote}...")
#     print(f"lote {lote} Processado com sucesso...")
#     print("Ciclo de produção concluído")

# Execicio 2

# Imagine a produção de frutas em uma feira. Desejo apresentar as frutas banana, manga, melancia, abacaxi.
# com uma quantidade de 10 bananas, 5 mangas, 10 melancias e 13 abacaxi

# print("Frutas fresca da feira")
# print("Opção 1- banana")
# print("Opção 2- manga")
# print("Opção 3- melancia")
# print("Opção 4- abacaxi")

# menu = int(input("escolha uma opção"))

# banana = 10

# manga = 5

# melancia = 10

# abacaxi = 13

# if menu == 1:
#         print(f"temos {banana} bananas")
# elif menu == 2:
#     print(f"temos {manga} mangas")
# elif menu == 3:
#         print(f"temos {melancia} melancias")
# elif menu == 4:
#     print(f"temos {abacaxi} abacaxis")
# else:
#     print("Isso não é uma opção")

# print("No total temos", banana + manga + melancia + abacaxi, "frutas")

# Exercicio 3

# montar uma tabuada inicialmente pode ser usado por um valor fixo e depois usar pergunta

print("Digite a tabuada que deseja")

primeiro = float(input("Primeiro número"))

for primeiro in range(primeiro * 1, 10):
    print(f"{primeiro} vezes...")
    print(f" {primeiro} Processado com sucesso...")






