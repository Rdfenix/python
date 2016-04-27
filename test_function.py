def transformInt(x):
	y = int(x)
	return y

def calculoIdade(x, y):
	return x - y

idadeUsuario = input('Qual a sua idade?:\n')
idade = transformInt(idadeUsuario)
anoAtual = input('Qual ano estamos?:\n')
ano = transformInt(anoAtual)

print('Seu ano de nascimento é: ', calculoIdade(ano, idade))

