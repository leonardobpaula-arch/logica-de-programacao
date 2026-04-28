#O laço while (repetições indeterminadas)
#Use o while quando você não sabe quando vai parar. Ele depende de uma condição (como um sensor de segurança ou um botão de emergencia)
#Exemplo: Monitor de temperatura estiver segura

# import time
# temperatura = 30
# while temperatura < 80:
#     print(f"Temperatura atual: {temperatura} °C. Sistema operando...")
#     #time.sleep(1)
#     temperatura += 3 #simulando o aquecimento da máquina
#     print("ALERTA! Temperatura atingiu o limite. Desligando motor...")

    # Exemplo 2: monitoramento de teperatura com lista de leituras
    # Lista de temperaturas lidas pelo sensor por minuto

#     leituras = [70, 75, 82, 98, 110, 85, 80]
#     for temp in leituras:
#         if temp > 100:
#             print(f"CRITICO: {temp} °C detectado! Acionando parada de emergência.")
#             break # O loop para aqui e NÃO lê os próximos valores (85 e 80)
#         print(f"Temperatura está em {temp} °C. Operação normal")
#         print("Sistema desligado. Aguardando manutenção.")

# print("Sistema desligado. aguardando manutenção")

# materiais = ["metal", "metal", "plastico", "matal", "vidro", "metal"]
# for peça in materiais:
#     if peça = "metal":
# print(f"Aviso: peça de {peça} detectada. desviando para descarte...")
# continue

# print(f"processando peça de {peça}. furando e polindo...")

# print("Fim do lote de produção.")

#Exercicio 1 tente criar um código que conte de 1 a 10, mas use o 
# continue para não imprimir o numero 5 (simulando falha de sensor especifica no item 5)

# for sensor in range(1, 11):
#     print(f"Sensor nº {sensor}com falha")
#     print (f"sensor {sensor} sem falha")
#     print("Fim! :)")

#Exercicio 2
#Simule um semáforo com parada para cada cor. 
#Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa para cada cor
#Use o continue para pular a cor amarela (simulando um semáforo com defeito que não acende a luz amarela)

# import time
# leituras = ["verde", "amarelo", "vermelho"]
# for cor in leituras:
#     if cor == "amarelo":
#         print(f"Semáforo com defeito, pulando a cor {cor}...")
#         continue
#     print(f"semáforo na cor {cor}. Parando por 3 segundos...")
#     time.sleep(3)
#     print("Fim do ciclo do semáforo.")

#Exercicio 3
#Soma de cargas de energia (for)
#Uma fábrica tem 5 maquinas. Peça ao usuário (via input dentro do loop)
#o consumo em KWH de cada uma das máquinas.
#Ao final do loop, o programa deve exibir o consumo total da fábrica

# total_consumo = 0
# for maquina in range(1, 6):
#     consumo = float(input(f"Digite o consumo em KWH da máquina {maquina}:"))
#     total_consumo += consumo # Acumula o consumo total
#     print(f"O consumo total da fábrica é de {total_consumo}KWH.")

#Exercicio 4 - Identificador de peças defeituosas (for + if)
#Percorra uma lista de medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
#o padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
#Use um for para ler a lista e, para cada peça, diga se ela está "aprovada" ou "rejeitada"

#peças = [50.1, 49.8, 52.0, 50.0, 48.5]

#for medida in peças:
#     if medida >= 50.0:
#         print(f"Peça com medida {medida}mm: Aprovada")
# else:
#     print(f"peça com medida {medida}mm: Rejeitada")
#     print("Fim da avaliação de peças")

#Exercicio 5 - Uma balança industrial está pesando um lote de 6 sacos de insumos.
#O peso ideal de cada saco é 50kg, mas o sistema aceita variações.
#Crie um programa que peça ao usuário o peso de cada saco (via input dentro do loop) e, para cada um,
#informe se ele está "Dentro do limite" (entre 48kg e 52kg) ou "Fora do limite".No final, exiba quantos sacos
#estão dentro do limite

# sacos_dl = 0
# for saco in range(1,7):
#     peso = float(input(f"digite o peso do saco {saco} em kg: "))
#     if 48 <= peso <= 52:
#         print(f"saco {saco} com peso {peso}kg: dentro do limite")
#         sacos_dl += 1 
#     else:
#         print(f"saco {saco} com peso {peso}kg: fora do limite")
#         print(f"Quantidade de sacos dentro do limite: {sacos_dl}")

# ciclo = 0
# while ciclo < 5:
#     temperatura = float(input(f"Digite a temperatura da peça {ciclo + 1} em °C:"))

#     if temperatura < 0:
#         print("Erro de leitura no sensor. Por favor, digite uma temperatura válida.")
#         continue

#     if temperatura > 150:
#         print(f"Peça {ciclo + 1} processada com temperatura {temperatura}°C.")
#         ciclo += 1

#         print(f"Peça {ciclo} processada com sucesso. temperatura dentro do limite.")
        
#         print(f"Fim do monitoramento de temperatura.")

#Exercicio 6 - Contador de peças com falha (while + if + continue)
#Uma linha de produção tem um sensor que detecta falhas em peças.
#O programa deve contar quantas peças com falha foram detectadas.
#O usuário deve digitar "sim" para indicar que uma peça tem falha e "não" para indicar que está boa.
#O programa deve continuar pedindo a condição da peça até que o usuário digite "fim".
#No final, exiba o total de peças com falha detectadas.