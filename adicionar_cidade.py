city = []

num = int(input("Informe o numedo de cidades que você quer adicionar"))
count = 0

while count < num:
	city_name = input("Qual cidade: \n")
	city.append(city_name)
	count = count +  1

print(city)