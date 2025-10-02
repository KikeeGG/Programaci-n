import random
numeroSecreto = random.randint(1, 100)

numeroElegido=int(input("Estoy pensando en un número, ¡A ver si lo adivinas!:"))
while numeroElegido != numeroSecreto:
	if numeroElegido > numeroSecreto:
		print("Más pequeño")
	elif numeroElegido < numeroSecreto:
		print("Más grande")
	numeroElegido = int(input("Intenta otra vez:"))

print("Has acertado!", numeroElegido, "era la respuesta!")