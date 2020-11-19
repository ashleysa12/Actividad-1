# Reto 2
company = {"nombre": "CILCCA",
           "rubro": "Licorero",
           "productos": ["Ron", "Vodka", "Tequila", "Vino"],
           "sucursales": {"Sede.Admi.": ["Caurimare", "Chuao"],
                          "Planta": ["Ocumare", "Yaracuy"],
                          "Distribuidora": "Valencia"
                          },
           "marcas": ("Ocumare", "Sunset", "Alxander", "Española")
           }

print("		Diccionario:")
print()
print("Nombre de la empresa:", company["nombre"])
print("Rubro de la empresa:", company["rubro"])
print("Algunos productos que produce la empresa:", company["productos"])
print("Las sucursales de la empresa son:", company["sucursales"])
print("Algunas marcas de la empresa son:", company["marcas"])
print()

print("		Claves del diccionario:")
print()
print(company.keys())
print()
print("		Valores del diccionario:")
print()
print(company.values())
print()
print("El tamaño del diccionario es:", len(company))
