nombre1 = input("nombre1:")
nombre2 = input("nombre2:")
if not nombre1.isnumeric() or not nombre2.isnumeric():
    raise SystemExit("Fin du programme")
nombre1 = int(nombre1)
nombre2 = int(nombre2)

operation = input("operation:")
match operation:
    case "+":
        resulat = nombre1 + nombre2
    case "*":
        resulat = nombre1 * nombre2
    case "-":
        resulat = nombre1 - nombre2
    case "/":
        if nombre2 == 0:
            raise SystemExit("Ne peux pas diviser par 0")
        resulat = nombre1 / nombre2
    case _:
        raise SystemExit("Operation  non reconnue")
print(resulat)