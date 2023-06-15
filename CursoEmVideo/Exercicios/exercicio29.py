import emoji
velocity = int(input('Qual a velocidade de seu carro? '))
if  velocity>80:
    print('Você foi multado!\nA multa vai custar R$ {}'.format((velocity-80)*7))

