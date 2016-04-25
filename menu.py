menu_prices = {
	'Knackered spam': 0.50, 'Pip pip Spam': 1.50, 'Squidgy Spam': 2.50, 'Smashing Spam': 3.50
}

for name, price in menu_prices.items():
	print(name, ': $', format(price, '.2f'), sep='')