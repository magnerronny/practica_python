numeros = {1,2,3,4,5,3,33,3}
print(numeros)

a = {1, 2, 3}
b = {3, 4, 5}

print(a.intersection(b))
print(a.union(b))

coordenas = (1,2,2,3,4)
print(coordenas)
# coordenas(0) = 3
for i in coordenas:
    print(i)

usuarios = [
    {"nombre": "Ana", "edad": 28, "activo": True},
    {"nombre": "Luis", "edad": 35, "activo": False},
    {"nombre": "Marta", "edad": 22, "activo": True}
]

activos = [u for u in usuarios if u['activo']]
print(f"usuarios activos: {activos}")

# edad promedio
promedio = sum([u['edad'] for u in usuarios])/len(usuarios)
print(f"el promedio de las personas es: {promedio:.2f}")

# diccionario de listas
ventas = {
    "ropa": [120, 250, 300],
    "comida": [80, 100, 150],
    "tecnología": [400, 700]
}

totales = {k: sum(v) for k, v in ventas.items()}
print(totales)

max_cat = max(totales, key=totales.get)
print(max_cat)

lista1 = ["ana@gmail.com", "luis@gmail.com", "marta@gmail.com"]
lista2 = ["marta@gmail.com", "sofia@gmail.com", "ana@gmail.com"]

set1, set2 = set(lista1), set(lista2)
print(set1)
print(set2)

todos = set1 | set2
print(todos)
comunes = set1 & set2
print(comunes)

estudiantes = [
    {"nombre": "Ana", "edad": 20, "notas": [("Matemáticas", 8), ("Historia", 9)]},
    {"nombre": "Luis", "edad": 21, "notas": [("Matemáticas", 6), ("Historia", 7)]},
    {"nombre": "Marta", "edad": 22, "notas": [("Matemáticas", 10), ("Historia", 8)]}
]

for est in estudiantes:
    promedio = sum([n for _, n in est['notas']])/len(est["notas"])
    print(f"{est['nombre']} tiene el promedio  {promedio:.2f}")

empresa = {
    "ventas":[{'nombre':'jose','sueldo':1234}, {'nombre':'mateo','sueldo':4334},{'nombre':'mateo','sueldo':6124}],
    "marketing":[{'nombre':'estefano','sueldo':2234}],
    "IT":[{'nombre':'amadeo','sueldo':3434}]
}
total = {k:sum([vv['sueldo'] for vv in v]) for k, v in empresa.items()}

# alto = [[vv['sueldo'] for vv in v] for k, v in empresa.items()]
# more_Alt = []
# for value in alto:
#     for v in value:
#         more_Alt.append(v)
# print(max(more_Alt))

datos = [
    ("nombre", "Marta"),
    ("edad", 22),
    ("activo", True)
]

diccionarios = dict(datos)

lista  = list(u for k,u in diccionarios.items())
print(f"el diccionarios es:{diccionarios}")
print(f"la lista es: {lista}")