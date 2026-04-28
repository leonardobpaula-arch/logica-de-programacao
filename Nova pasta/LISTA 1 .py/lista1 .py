# 1. Perfil de Gamer: Peça o nick (nome) do jogador e o nível atual. Exiba: "O
# jogador [nick] está no nível [nível] e pronto para a partida!"

print("Bem vindo senai Batle royal")
print("Digite seu nome e seu nível")
nome = input("Qual o seu nome?")
nivel = input("Qual é o seu nivel?")
print("O jogador" , nome , "está no nível" , nivel , "e pronto para a partida!")

# 2. Calculadora de Mesada: Peça o valor que o aluno ganha por semana e
# multiplique por 4 para mostrar quanto ele terá no final do mês.

valor = float(input("Quanto você ganha de mesada toda semana?"))
print("No fim do mês você terá" , valor * 4 , "reais")

# 3. Conversor de Internet: Peça um valor em Gigabytes (GB) e converta para
# Megabytes (MB) (multiplique por 1024).

print("Digite um valor de Gigabytes para a conversão em Megabytes")
valor = int(input("Porfavor digite o valor"))
print("Os" , valor , "Gigabytes foram convertidos em" , valor * 1024 , "Megabytes")

# 4. Média de Notas: Peça as notas de Matemática e Português. Calcule e mostre a
# média final.

print("Quais foram suas notas de português e matemática?")
notap = float(input("Qual foi sua nota de português?"))
notam = float(input("Qual foi sua nota de matemática?"))

resultado = int(notap + notam / 2)

print("Sua média foi" , resultado ,)

# 5. Seguidores: Peça a quantidade de seguidores atuais e quantos novos seguidores
# o aluno ganhou hoje. Exiba o total atualizado.

print("Quantos seguidores você tem?")
atual = int(input("Digite a quantidade de seguidores que você tem"))

print("Quantos seguidores você conseguiu hoje?")
depois = int(input("Digite a quantidade de seguidores que você conseguiu hoje"))

print("O total de seguidores atuais é" , atual + depois ,)

# 6. Idade em Dias: Peça a idade do aluno e calcule aproximadamente quantos dias
# ele já viveu (idade * 365).

print("Quantos anos você tem")

anos = int(input("Digite quantos anos você tem"))

print("você tem aproximadamente" , anos * 365 , "dias de idade")

# 7. Consumo de Lanche: Peça o preço do salgado e o preço do suco. Exiba o valor
# total da conta.

print("Quanto foi o valor dos alimentos que você comeu?")

salgado = float(input("Quanto custou o seu salgado?"))

suco = float(input("E seu suco? Quanto ficou?"))

print("Seu lanche custou" , salgado + suco , "reais no total")

# 8. Ano de Nascimento: Peça o ano atual e a idade do aluno. Calcule e exiba o ano
# em que ele nasceu.

print("Em que ano estamos?")

ano = int(input("Digite qual o ano atual"))

print("Qual sua idade?")

idade = int(input("Digite quantos anos você tem"))

print("Você nasceu no ano de" , ano - idade)

# 9. Filtro de Idade (TikTok): Peça a idade do usuário. Se for menor que 13, exiba
# "Acesso restrito". Se tiver entre 13 e 17, "Acesso moderado". Se for 18 ou
# mais, "Acesso liberado".

print("Necessitamos sua idade para prosseguir com o conteúdo")

idade = int(input("Digite sua idade"))

if 12 >= idade:
    print("Acesso restrito")

elif 13 <= idade <= 17:
    print("Acesso moderado")

else:
    print("Acesso liberado")

#     10.Bateria do Celular: Crie um while que começa com a bateria em 100. A cada
# repetição, subtraia 10 e mostre: "Bateria em [valor]%". O loop para quando
# chegar em 10 e exibe: "Por favor, conecte o carregador!".

bateria = 100

while bateria > 10:
    print(f"bateria em {bateria}%")
    bateria -=10

print(f"bateria em {bateria}%")
print("Por favor, conecte ao carregador!")

# 11. Contagem de Curtidas: Use um for para simular a contagem de curtidas em uma
# foto. Peça ao usuário o limite de curtidas (ex: 5). O programa deve contar de 1 até
# esse número, printando: "Curtida no [i] recebida!".


limite = int(input("Digite o limite de curtidas"))

for i in range(1, limite + 1):
    print(f"Curtida n° {i} recebida")
    
# 12.Carrinho de Compras Online: Use um while para pedir nomes de produtos que o
# aluno quer comprar. O loop só para quando ele digitar "sair". No final, mostre
# quantas vezes ele adiciona itens ao carrinho (use um contador).

conntador = 0
produto = ""

print("bem vindo ao carrinho de compras")
print("Digite sair para finalizar a compra")

while produto.lower() != "sair":
    produto = input("Digite o nome do produto:")
    contador += 1
    if produto.lower() != "sair":
        print(f"produto '{produto}' adicionado ao carrinho!")

print(f"Compra finalizada! Você adicionou {contador} itens ao seu carrinho.")