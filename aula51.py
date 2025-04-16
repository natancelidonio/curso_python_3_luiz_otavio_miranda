velocidade = 61    # Velocidade atual do carro
local_carro = 102    # local em que o carro está na estrada

RADAR_1 = 60    # Velocidade máxima do radar 1
LOCAL_1 = 100    # local onde o radar 1 está
RADAR_RANGE = 1    # A distância onde o radar pega

if velocidade > RADAR_1:
    print('A velocidade do carro passou do limite do radar 1 em algum momento.')

if (local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)) and (velocidade > RADAR_1):
    print('O carro estava acima do limite no radar e foi multado.')