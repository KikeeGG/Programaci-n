numero = int(input("Escribe un numero positivo: "))
contador = 0

for i in range(1, numero + 1):
    if i % 2 == 0:
        contador += 1

print("Hay", contador, "números pares entre 1 y", numero)
