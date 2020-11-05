# Reto 3.2: Condicionales If, Elif, Else
x = int(input("Introduzca un valor numérico: "))
print()

if (x % 4 == 0):
    print("El valor introducido es múltiplo de 2 y 4.")
elif (x % 2 == 0):
    print("El valor introducido es múltiplo de 2.")
else:
    print("No es múltiplo de 2.")
