prices = [2.50, 3.75, 8.00, 10.65]
total = 0

# Este for é muito parecido com o foreach em algumas linguagens.
for price in prices:
    print('Price is ', price)
    total = total + price
print('Total is', total)

average = total / len(prices)
print('AVG  is ', average)
