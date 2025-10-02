edad=int(input("Qué edad tienes para ver la película?"))
if edad < 5:
	print("La entrada es gratis")
elif edad >= 5 and edad <= 12:
	print("La entrada cuesta 5 euros")
elif edad >= 13 and edad <= 17:
	print("La entrada cuesta 7 euros")
else:
	print("La entrada cuesta 10 euros")