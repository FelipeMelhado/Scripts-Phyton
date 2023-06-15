import math
ang = float(input('Digite um angulo: '))
rad = math.radians(ang)
coss = math.cos(rad)
seno = math.sin(rad)
tang = math.tan(rad)
print('De acordo com o angulo {}\nO seu cosseno é {:.2f}\nO seu seno é {:.2f}\nE a sua tangente é {:.2f}'.format(ang, coss, seno, tang))
