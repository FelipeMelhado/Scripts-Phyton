name = str(input('Digite seu nome completo: '))
n = name.split()[0]
un = name.rsplit()
print('Seu primeiro nome é {} e seu ultimo nome é {}'.format(n, un))