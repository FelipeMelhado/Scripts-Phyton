distancia = float(input('Qual a quantidade de km/s percorridos? '))
diaria = int(input('Qual a quantidade de diárias utilizadas? '))
calc = diaria*60+distancia*0.15
print('O preço a pagar pelo carro alugado é R${:.2f}'.format(calc))


