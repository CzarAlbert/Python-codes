velocidade = 61
local_carro = 90
# barra invertida dignifica que posso continuar o codigo na linha de baixo
# Letra maiscula é 
RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1 

if velocidade > RADAR_1 :
    print('Velocidade do carro passou do Radar 1 ')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro<= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1 :
    print('Carro multado no radar 1')