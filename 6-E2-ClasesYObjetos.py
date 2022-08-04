class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def mostrarNombre(self):
        return(self.nombre)
    
    def mostrarNota(self):
        return(self.nota)
    
    def aprobo(self):
        return(self.nota >= 7)
    

alumno = Alumno("Cosme Fulanito", 6)
print(alumno.aprobo())







