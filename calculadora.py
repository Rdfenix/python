def adicao(x, y):
	total =  x + y
	impressao(total)

def subtracao(x, y):
	total =  x - y
	impressao(total)

def divisao(x, y):
	total =  x // y
	impressao(total)

def multiplicacao(x, y):
	total = x * y
	impressao(total)

def transformInt(x):
	y = int(x)
	return y

def impressao(f):
	print("Resultado é: ", f, sep="")

def operacao(x, a, b):
	if x ==  1:
		adicao(a, b)
	elif x == 2:
		subtracao(a, b)
	elif x == 3:
		divisao(a, b)
	elif x == 4:
		multiplicacao(a, b)

def main():

	option = {1:adicao, 2: subtracao, 3:divisao, 4:multiplicacao }

	number1 = input('Informe o primeiro numero a ser calculado: ')
	number2 = input('Informe o segundo numero a ser calculado: ')
	opt = input('Informe a operação desejada: ')

	a = transformInt(number1)
	b = transformInt(number2)
	option = transformInt(opt)

	operacao(option, a, b)

main()