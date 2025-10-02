#Dejamos en 0 nuestras dos variables principales
suma_total=0
contador=0
#Se solicita al usuario que ingrese el primer número.
numero=int(input("Ingresa un número que se te ocurra:"))
#Comienza el bucle while, que continuará pidiendo números hasta que el usuario ingrese 0
while numero != 0:
	suma_total += numero
	contador +=1
	numero=int(input("Ingresa otro número:")) #De esta manera el programa sigue pidiendo numeros
#Si el número es 0 (y por tanto se ha terminado el bucle), se calcula el promedio
if numero == 0:
	media=suma_total / contador
	print(f"El promedio de los números que has introducido es:", media)