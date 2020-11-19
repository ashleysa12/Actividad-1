# Reto 1, programa 4
things = ("Cepillo", "Mueble", "Monitor")
print("Tupla:", things)
print()

thingslist = list(things)
print("Tupla convertida en lista:", thingslist)
print()

thingslist.append("Marcador")
print("Lista con un elemento agregado:", thingslist)
print()

thingslist.remove("Mueble")
print("Lista con un elemento eliminado:", thingslist)
print()

things = tuple(thingslist)
print("Lista convertida en tupla:", things)
print()

print("¿Mueble se encuntra en la tupla?", "Mueble" in things)
print("¿Cuántas veces se repite la palabra Cepillo?", things.count("Cepillo"))
print("¿Cuál es el tamaño de la tupla?", len(things))
print()

tittle = ("Cosas")
print("Tupla unitaria:", tittle)
