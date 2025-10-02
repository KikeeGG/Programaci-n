palabra=input("Dame una palabra, la que tú quieras:") #Solicitamos al usuario una palabra
palabra_invertida="" #Inicializar una cadena vacía para la palabra invertida
#Se recorre la palabra inversa en el bucle for
for letra in range(len(palabra) -1, -1, -1):
	palabra_invertida += palabra[letra]
print("La palabra invertida es:", palabra_invertida) #Se imprime la palabra invertida

