import math
cato = float(input('Qual o cateto oposto? :'))
cata = float(input('Qual o cateto adjacente? :'))
soma = (cato**2+cata**2)
hptns = (math.sqrt(soma))
print('A hipotenusa é {}'.format(hptns))

