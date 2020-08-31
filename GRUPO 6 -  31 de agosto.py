matricula = input('Numero da Matricula:')
nome1 = input('Nome do primeiro funcionario:')
salario1 = int(input('Salario do primeiro funcionario:'))
nome2 = input('Nome do segundo funcionario:')
salario2 = int(input('Salario do segundo funcionario:'))

desconto = salario1 * 5 / 100
novodesconto = salario1 - (salario1 * 5 / 100)
acrescimo = salario2 * 9 / 100
novoacrescimo = salario2 + (salario2 * 9 / 100)

print('Desconto do primeiro:', desconto)
print('Acrescimo do segundo:', acrescimo)
print('Salário final do',nome1,':', novodesconto)
print('Salário final do',nome2,':', novoacrescimo)
