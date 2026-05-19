# Projeto cancela automática

#variaveis

# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código

print("Bem vindo")
print("Qual é o modelo do veiculo e a placa do carro?")

modelo = input("Insira o modelo do veículo ")

placa = input("Insira a placa do carro ")

print("Como deseja entrar?")

entrada = input("Opção 1: Ticket/Opção 2: TAG/Opção 3: interfone ")

if entrada == "ticket":
    print("Acesso liberado")
    
    hora_entrada = float(input("Digite a hora de entrada "))
    estacionamento = float(input("Qual o custo do estacionamento? "))
    hora_saida = float(input("Quando você deixou o estacionamento "))

    permanencia = hora_saida - hora_entrada

    print(f"Seu tempo de permanência foi de {permanencia}")

    total_pagar = permanencia * estacionamento

    print(f"O valor da estadia será R${total_pagar:.2f}")
    print("Por favor devolva o ticket")


elif entrada == "TAG":
    print("Acesso liberado")
    print("A cobrança será realizada diretamente à sua fatura")


elif entrada == "interfone":
    print("Liberando acesso pelo interfone")
    print("Ao sair, use o interfone novamente")

else:
    print("Obrigado pela visita. Volte sempre")

