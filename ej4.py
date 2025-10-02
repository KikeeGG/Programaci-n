palabra=str(input("Escribe una palabra:"))
#Establecemos contador en 0 y lo que cosideramos la variable vocales
contador = 0
vocales = "aeiouAEIOU"
#Iterar sobre cada letra de la palabra
for letra in palabra:
	if letra in vocales: #Verificar si la letra es una vocal
		contador += 1
print(f"El número de vocales en", palabra, "es de:", contador)