price = input("Enter the price: \n")

try:
	price = float(price)
	print("Yeah! that's right, this is an number!")
	print('Your number is:', price)
except ValueError as err:
	print(err)