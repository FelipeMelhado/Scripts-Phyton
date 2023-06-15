import random
al1 = str(input('Digite o nome do primeiro aluno: '))
al2 = str(input('Digite o nome do segundo aluno:'))
al3 = str(input('Digite o nome do terceiro aluno: '))
al4 = str(input('Digite o nome do quarto aluno: '))
print('O aluno escolhido foi {}'. format(random.choice([al1, al2, al3, al4])))

