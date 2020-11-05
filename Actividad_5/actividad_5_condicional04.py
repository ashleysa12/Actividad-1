# Reto 3.4: Condicionales If, Elif, Else
x = int(input("Introduzca primer valor: "))
y = int(input("Introduzca segundo valor: "))
print()

if (x == y):
    print("El número ", x, " y ", y, "son iguales")
elif (x > y):
    print("El número ", x, " es mayor que ", y)
else:
    print("El número ", x, " es menor que ", y)
