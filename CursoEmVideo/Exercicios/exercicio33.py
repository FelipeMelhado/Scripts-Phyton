#Verificar o maior e menor numero!

a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))
c = int(input('Digite um numero: '))

#Verificando o menor numero
menor = a
if  b<a and b<c:
    menor = b
if  c<a and c<b:
    menor = c
print('Menor Numero',menor)

#Verificando o maior numero
maior = a
if  b>a and b>c:
    maior = b
if c>b and c>a:
    maior= c
    print('Maior Numero',maior)