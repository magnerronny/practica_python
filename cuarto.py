numeros = list(range(0,6))
print(numeros)

cuadrados = [x**2 for x in range(7)]
print(cuadrados)

pares = list(range(0,11,2))
print(pares)
par = [x for x in range(10) if x %2 == 0]
print(par)

nombres = ["ana", "LUIS", "mArTa"]

normalizados = [n.title() for n in nombres]
print(normalizados)