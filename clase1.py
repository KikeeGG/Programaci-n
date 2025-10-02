numero=int(input("Escribe un numero positivo:"))
contador = 0

for numeros in range(1, numero+1):
	if numeros %2 == 0:
		contador += 1
print("Hay", contador, "pares entre 1 y", numero)