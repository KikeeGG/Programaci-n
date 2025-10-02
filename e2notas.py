nota=int(input("Qué nota has sacado?"))
match nota:
    case >=90:
        print("Tu calificación es A")
    case >=80 and <90:
        print("Tu calificación es B")
    case >=70 and <80:
        print("Tu calificación es C")
    case >=60 and <70:
        print("Tu calificación es D")
    case _:
        print("Tu calificación es F")