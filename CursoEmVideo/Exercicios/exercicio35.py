print('-='*15)
print('Analisador de triângulos')
print('-='*15)

la = float(input('Digite o tamanho do lado a: '))
lb = float(input('Digite o tamanho do lado b: '))
lc = float(input('Digite o tamanho do lado c: '))
if  la+lb>lc and lb+lc>la and la+lc>lb:
    print('Pode formar um triangulo')
else:
    print('Não pode formar um triangulo')

