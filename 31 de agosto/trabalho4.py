sistema = int(input('Quantidade de Alunos em Sistemas:'))
analise = int(input('Quantidade de Alunos em Analise:'))
quantidade = sistema + analise
pct1 = sistema/quantidade*100
pct2 = analise/quantidade*100
print('O total de alunos é:', quantidade)
print('a porcentagem de alunos é de {:.2f}%'.format(sistema))
print('a porcentagem de alunos é de {:.2f}%'.format(analise))