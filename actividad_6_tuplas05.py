# Reto 1, programa 5
name = ("Ashley", "Andreina", 121186, "Edwar")
print("Tupla:", name)
print()

namelist = list(name)
print("Tupla convertida en lista:", namelist)
print()

namelist.append("Emir")
namelist.append("Alvaro")
print("Lista con un elemento agregado:", namelist)
print()

namelist.remove(121186)
print("Lista con un elemento eliminado:", namelist)
print()

name = tuple(namelist)
print("Lista convertida en tupla:", name)
print()

print("¿121186 se encuntra en la tupla?", 12186 in name)
print("¿Ashley se encuntra en la tupla?", "Ashley" in name)
print("¿Cuántas veces se repite el nombre Edwar?", name.count("Edwar"))
print("¿Cuál es el tamaño de la tupla?", len(name))
print()

tittle = ("Nombres")
print("Tupla unitaria:", tittle)
