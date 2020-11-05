# Reto 3.1: Condicionales If, Elif, Else
x = int(input("Introduzca su edad: "))
print()

if (x >= 18):
    print("Eres mayor de edad.")
elif (x < 0):
    print("No se puede tener una edad negativa.")
else:
    print("Eres menor de edad.")
