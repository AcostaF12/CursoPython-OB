from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def esPar(x):
    return(x % 2 == 0)

numerosPares = filter(esPar, numeros)

sumaTotal = reduce(lambda a,b: a + b,numerosPares)

print(sumaTotal)
