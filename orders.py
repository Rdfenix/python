import random

orders = []
order = input("What would you like do to order? (Q to quit)")

while (order.upper() != 'Q'):
	found = menu.get(order)
	if found:
		orders.append(order)
	else:
		print("Menu item doesn't exist")
	

	order = input("Anything else? (Q to quit)")

print(orders)