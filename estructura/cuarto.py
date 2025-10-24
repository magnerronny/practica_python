numeros = [x for x in range(6)]
print(numeros)

cuadrado = [x**2 for x in numeros]
print(cuadrado)

pares =  [x for x in range(10) if x % 2== 0]
print(pares)

nombres = ["ana", "LUIS", "mArTa"]
normalizados = [n.title() for n in nombres]
print(normalizados)


usuarios = [
    {"nombre": "Ana", "activo": True},
    {"nombre": "Luis", "activo": False},
    {"nombre": "Marta", "activo": True}
]

activos = [x for x in usuarios if x["activo"] == True]
print(activos)

nombres_activos = [u["nombre"] for u in usuarios if u["activo"]]
print(nombres_activos)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = [num for fila in matriz for num in fila]
print(flatten)

ejemplo = [lista**2 for lista in range(1,21) if lista % 3 == 0]
print(f"los multiplos son: {ejemplo}")

cuadrados_multiplos_3 = [x**2 for x in range(1, 21) if x % 3 == 0]
print(cuadrados_multiplos_3)