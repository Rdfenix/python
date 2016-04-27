import random

# Adiciona um numero inteiro, de modo randomico, a variavel num
num = random.randint(1,10)
print("Numero randominco: ", num)

# Fun
guess = int(input('Guess a number between 1 and 10: \n'))
num = 3

while guess != num:
	guess = int(input("Guess again: \n"))

print("You win!!")