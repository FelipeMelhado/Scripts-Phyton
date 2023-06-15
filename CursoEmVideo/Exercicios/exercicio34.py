salario = float(input('Qual o salário do funcionario? '))
if  salario<=1250:
    aumento = salario*0.15
    novo = salario+aumento
else:
    aumento = salario*0.10
    novo = salario+aumento
print('O aumento é de {} e seu novo salário é de {}'.format(aumento, novo))
