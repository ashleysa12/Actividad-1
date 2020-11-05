# Reto 3.3: Condicionales If, Elif, Else
print('''
----- Menú -----
1. Primera opción
2. Segunda opción
''')
op = int(input("Introduzca el número de un opción: "))
print()

if (op == 1):
    print("Usted ha seleccionado la primera opción del menú.")
elif (op == 2):
    print("Usted ha seleccionado la segunda opción del menú.")
else:
    print("Introduzca una opción válida.")
