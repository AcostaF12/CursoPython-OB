from cmath import pi


def areaTriangulo(base, altura): 
    return((base * altura) / 2)

print(areaTriangulo(20, 50))


def areaCirculo(radio):
    return(pi * (radio**2))

print(areaCirculo(16))