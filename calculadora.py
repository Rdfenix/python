def adicao(x, y):
	total =  x + y
	impressao(total)

def subtracao(x, y):
	total =  x - y
	impressao(total)

def divisao(x, y):
	total =  x / y
	impressao(total)

def multiplicacao(x, y):
	total = x * y
	impressao(total)

def transformFloat(x):
	y = float(x)
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
	opt_choice = {1:'Adição', 2:'Subtração', 3:'Divisão', 4:'Multiplicação'}

	for number, name in opt_choice.items():
		print(number, ": ", name, sep="")

	number1 = input('Informe o primeiro numero a ser calculado: \n')
	number2 = input('Informe o segundo numero a ser calculado: \n')
	opt = input('Informe a operação desejada: \n')

	a = transformFloat(number1)
	b = transformFloat(number2)
	option = transformFloat(opt)

	operacao(option, a, b)

main()