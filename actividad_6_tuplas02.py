# Reto 1, programa 2
various = ("Carro", 123, "Moto", "Algo")
print("Tupla:", various)
print()

listvarious = list(various)
print("Tupla convertida en lista:", listvarious)
print()

listvarious.append(1618)
print("Lista con un elemento agregado:", listvarious)
print()

listvarious.remove("Algo")
print("Lista con un elemento eliminado:", listvarious)
print()

various = tuple(listvarious)
print("Lista convertida en tupla:", various)
print()

print("¿123 se encuntra en la tupla?", 123 in various)
print("¿5896 se encuentra en la tupla?", 5896 in various)
print()

print("¿Cuántas veces se repite la palabra Carro?", various.count("Carro"))
print("¿Cuál es el tamaño de la tupla?", len(various))
print()

unit = (31072001)
print("Tupla unitaria:", unit)
