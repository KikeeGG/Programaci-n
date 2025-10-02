#Se solicita al usuario que ingrese un número positivo
n=int(input("Elige un número positivo:"))
#Si el número n oes positivo, lo hacemos saber
if n <=0:
	print(n, "no es un número positivo")
else:
#Si el número es positivo, se calcula la suma de los primeros n números naturales
	resultado= n*(n+1)/2
	print("El resultado es", resultado)