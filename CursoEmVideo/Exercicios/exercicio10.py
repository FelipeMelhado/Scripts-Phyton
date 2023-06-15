n = float(input('Para converter os valores de R$ para US$, digite um valor em reais: '))
cnvtd = float(n/3.27)
print ('Considerando a cotação atual do dolar em R$ 3,27.\n(US$1.00 = R$3,27)\nA conversão do valor digitado é: US${:.2f}'.format(cnvtd))
