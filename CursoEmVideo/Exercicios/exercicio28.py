import random
x = random.randint (1, 5)
esc = int(input('Descubra qual numero a maquina pensou entre 1 e 5: '))
if x == esc:
    print('===== Parabéns, você acertou! =====')
else:
    print('Você errou!')
print('A maquina pensou no numero: {}'.format(x))
