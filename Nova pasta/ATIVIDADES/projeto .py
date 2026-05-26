# Sistema de Elevador de Prédio

# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo,
# e tem a capacidade de transportar até 5 pessoas.

# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador,
# e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.

while True:
    print("Aperte o botão para chamar o elevador")

    pessoa = int(input("Quantas pessoas tem no elevador "))

    if pessoa >= 5:
        print("Sinto muito, mas o elevador esta cheio! espere um momento")
        break

    elif 0 >= pessoa <= 4:
        print("Bem vindo. Qual andar você deseja ir?")

    andar = int(input("Aperte o botão com o número do andar desejado entre 0 a 10 "))

    if andar == 0:
        print("A caminho do andar térreo ")
        print("Descendo")
        
    elif 10 >= andar >= 1:
        print("A caminho do seu andar ")
        print("Subindo")

    else:
        print("Esse andar não existe")