datos = input("Introducir una lista de paises:\n")

paises = [pais for pais in datos.split(",")]

paisesOrdenados = (sorted(list(set(paises))))

print(paisesOrdenados)





