print("Bem vindo")
print("Por favor digite as informações requisitadas")

carro = input("Por favor digite o modelo do seu veículo")

placa = input("por favor digite a placa do seu veículo")

print("O veículo" , carro, "de placa ", placa, "foi registrado no sistema. Boa viagem")


print("Necessitamos a capacidade total do tanque do seu veículo e a taxa de consumo média")

capacidade = input("Digite a capacidade total do tanque")

consumo = input("Digite a taxa de consumo em (KM/L)")

distancia_total = capacidade / consumo

print("Seu veículo pode percorrer no máximo" , distancia_total, "(KM/L)")