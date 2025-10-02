operacion=input("Elige una operación: (+,-,*,/)")
num1=int(input("Introduce el primer número:"))
num2=int(input("Introduce el segundo número:"))
match operacion:
	case "+":
		suma=num1 + num2	
		print("El resultado es",suma)
	case "-":
		resta=num1 - num2	
		print("El resultado es",resta)
	case "*":
		multiplicacion=num1 * num2	
		print("El resultado es",multiplicacion)
	case "/":
		if num2 == 0:	
			print("No puedes dividir por 0")
		else:
			division=num1 / num2
			print("El resultado es",division)

	