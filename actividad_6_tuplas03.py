# Reto 1, programa 3
b_day = (310701, 50198, 191066)
print("Tupla:", b_day)
print()

b_daylist = list(b_day)
print("Tupla convertida en lista:", b_daylist)
print()

b_daylist.append(121186)
b_daylist.append(121186)
print("Lista con un elemento agregado:", b_daylist)
print()

b_daylist.remove(310701)
print("Lista con un elemento eliminado:", b_daylist)
print()

b_day = tuple(b_daylist)
print("Lista convertida en tupla:", b_day)
print()

print("¿191066 se encuntra en la tupla?", 191066 in b_day)
print("¿Cuántas veces se repite la fecha 121186?", b_day.count(121186))
print("¿Cuál es el tamaño de la tupla?", len(b_day))
print()

tittle = ("Cumpleaños")
print("Tupla unitaria:", tittle)
