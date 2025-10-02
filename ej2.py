#Solicitamos al usuario que ingrese un número entero
n=int(input("Elige un número:"))
#Se verifica si el número es par usando el operador módulo (%)
if n %2 == 0: 
	print(n, "Es número par")
else:
	print(n, "Es número impar")
 