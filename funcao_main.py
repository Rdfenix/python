# Função para tranformar a variavel em int
def transformInt(x):
	y = int(x)
	return y
# Função para realizar o calculo matematico de idade
def calculoIdade(x, y):
	return x - y

# Função main
def main():
	idadeUsuario = input('Qual a sua idade?:\n')
	idade = transformInt(idadeUsuario)

	anoAtual = input('Qual ano estamos?:\n')
	ano = transformInt(anoAtual)

	resultado = calculoIdade(ano, idade)

	print('Seu ano de nascimento é: ', resultado)

# Chamada da função main.
main()
