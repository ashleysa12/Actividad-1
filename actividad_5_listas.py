countries = ["Brasil", "Colombia", "EEUU", "Perú"]
capitals = ["Brasilia", "Bogotá", "Washington D.C.", "Lima"]
print("A continuación se mostrarán las listas:")
print(countries)
print(capitals)
print()

#  Reto 1: Appened
countries.append("México")
capitals.append("CDMX")
print("A continuación se mostrarán las listas con elementos agregados:")
print(countries)
print(capitals)
print()

# Reto 1: Insert
countries.insert(2, "Ecuador")
capitals.insert(2, "Quito")
print("A continuación se mostrarán las listas con elementos agregados \
en la posición 3:")
print(countries)
print(capitals)
print()

# Reto 1: Remove
countries.remove("EEUU")
capitals.remove("Washington D.C.")
print("A continuación se mostrarán las listas sin un elemento:")
print(countries)
print(capitals)
print()

# Reto 1: Pop
countries.pop()
capitals.pop()
print("A continuación se mostrarán las listas sin un elemento:")
print(countries)
print(capitals)
print()

# Reto 1: Extend
countries.extend(["Venezuela", 2020])
capitals.extend(["Caracas", 4.11])
print("A continuación se mostrarán las listas extendidas:")
print(countries)
print(capitals)
print()

# Reto 1: Index
print("A continuación se mostrará el índice de 'Venezuela' y 'Quito' \
respectivamente:")
print(countries.index("Venezuela"), "y", capitals.index("Quito"))
print()

# Reto 1: Concatenar
various = [2.86, 89, "Ashley"]
plus = countries + various
print("A continuación se mostrará una lista concatenada:")
print(plus)
print()

# Reto 1: Repetir
print("A continuación se mostrará una lista multiplicada:")
print(various * 3)
print()

# Reto 1: Consultar
print("A continuación se mostrará si se encuentran 'EEUU' y 89 \
en alguna lista:")
print("EEUU" in countries)
print(89 in various)
print()
