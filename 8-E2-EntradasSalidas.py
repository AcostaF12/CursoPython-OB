import pickle


class Vehiculo:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def getNombre(self):
        return(self.nombre)

    def getPrecio(self):
        return(self.precio)

    def getAño(self):
        return(self.año)

    def __str__(self):
        return(f'Nombre: {self.nombre} \nPrecio: {self.precio} \nAño: {self.año}')

    def __repr__(self):
        return(f'Nombre: {self.nombre} Precio: {self.precio} Año: {self.año}')

v1 = Vehiculo('Nissan Skyline', 250000, 2006)
print(v1)

f = open('vehiculo1.bin', 'w+b')
pickle.dump(v1, f)


print('vehiculo1.bin')
f.close()