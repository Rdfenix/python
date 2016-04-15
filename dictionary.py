# Dicionario criado
my_things = {1:'skate', 2:'videogame', 3:'computer', 4:'glass', 5:'headphone'}
print(my_things[3])
result = my_things.get('Terra')

if result:
    print(result)
else:
    print('Não encontrado')
