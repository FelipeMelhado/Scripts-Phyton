distance = int(input('Qual a distancia da viagem em Km/h? '))
if  distance<=200:
    print('O valor desta viagem será de R$ {}'.format(distance*0.50))
else:
    print('O valor desta viagem será de R$ {}'.format(distance*0.45))