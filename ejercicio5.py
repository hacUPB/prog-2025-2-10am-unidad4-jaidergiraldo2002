import random

numeros = []
for i in range(100):
    aleatorio = random.randint(100, 1000)
    numeros.append(aleatorio)
suma = 0
for i in numeros:
    suma += i
promedio = suma / len(numeros)
print(f"Promedio: {promedio}")

mayor = max(numeros)
menor = min(numeros)
print(f"Mayor: {mayor}")
print(f"Menor: {menor}")