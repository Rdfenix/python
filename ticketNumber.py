# Importação de uma blblioteca
import random

# Numeros randomicos de 0.0 a 1.0
r1 = random.random()
print(r1)

# Numeros randomicos de uma lista
r2 = random.choice([1, 2, 3, 4, 5, 6])
print(r2)

# Numeros randomicos de uma range , ex: 1 a 1000
r3 = random.randint(1, 1000)
print(r3)
