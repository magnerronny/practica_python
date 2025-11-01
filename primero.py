fruts = ["apple", "banana", "cherry", "date"]

fruts.append("elderberry")
print(fruts)

fruts.remove("banana")
print(fruts)

coordenadas = (10, 32)
print(coordenadas)
print(coordenadas[0])

numbers = {1,3,1,2,3,4,3,32,4,5,6}
print(numbers)
a = {1,2,3}
b = {3,4,5}
print(a.union(b))
print(a.intersection(b))

persona = {"nombre": "carlos", "edad":32}

print(persona["nombre"])
persona["ciudad"] = "arequipa"
print(persona)

alumno = {
    "nombre":"angel",
    "edad": 32,
    "notas": [12,14,16]
}

promedio = sum(alumno["notas"])/len(alumno)
print(f"nota promedio es: {promedio}")

usuarios = [
    {"nombre": "Ana", "edad": 28, "activo": True},
    {"nombre": "Luis", "edad": 35, "activo": False},
    {"nombre": "Marta", "edad": 22, "activo": True}
]

activos = [u for u in usuarios if u["activo"] == True]
print(activos)

promedio = sum([u["edad"] for u in usuarios])/len(usuarios)
print(f"la edad promedio es: {promedio:.2f}")

ventas = {
    "ropa": [120, 250, 300],
    "comida": [80, 100, 150],
    "tecnología": [400, 700]
}

totalCategoria = {k:sum(i) for k, i in ventas.items()}
print(f"total de categorias: {totalCategoria}")
max_cat = max(totalCategoria, key=totalCategoria.get)
print(max_cat)

lista1 = ["ana@gmail.com", "luis@gmail.com", "marta@gmail.com"]
lista2 = ["marta@gmail.com", "sofia@gmail.com", "ana@gmail.com"]

set1, set2 = set(lista1), set(lista2)

print(set1.union(set2))
print(set1.intersection(set2))

# Cada estudiante tiene nombre, edad y una lista de (asignatura, nota)
estudiantes = [
    {"nombre": "Ana", "edad": 20, "notas": [("Matemáticas", 8), ("Historia", 9)]},
    {"nombre": "Luis", "edad": 21, "notas": [("Matemáticas", 6), ("Historia", 7)]},
    {"nombre": "Marta", "edad": 22, "notas": [("Matemáticas", 10), ("Historia", 8)]}
]

for est in estudiantes:
    promedio = sum([i for k, i in est["notas"]]) / len(est["notas"])
    print(f"{est["nombre"]} tiene el promedio de: {promedio:.2f}")
    

empresa = {
    "ventas":[{
                    "nombre": "jose",
                    "sueldo": 2343
               },
               {
                   "nombre": "mateo",
                   "sueldo": 2123
               }
            ],
    "marketing":
            [{
                    "nombre": "adair",
                    "sueldo": 1343
               },
               {
                   "nombre": "ciprian",
                   "sueldo": 9123
               }
            ],
    "IT":
    [{
                    "nombre": "roberto",
                    "sueldo": 4343
               },
               {
                   "nombre": "agustin",
                   "sueldo": 5123
               }
            ]

}

print(empresa)


total = {k: sum([i["sueldo"] for i in v]) for k,v in empresa.items()}
print(total)

sueldoMayor = 0
for emp in empresa.values():
    for i in emp:
        if i["sueldo"] > sueldoMayor:
            nombre = i["nombre"]
            sueldoMayor = i["sueldo"]
print(f"el empleado {nombre} tiene el mayor sueldo de {sueldoMayor}")


lista = [u for u in range(1,5)]
tupla = tuple(lista)
print(tupla)

tupla = (10,40,10)
print(tupla)
lista = list(tupla)
lista.append(50)
print(lista)


numeros = [1,2,2,3,34]
conjuntos = set(numeros)
print(conjuntos)

conjunto = {u for u in range(5,8)}
print(conjunto)
lista = list(conjunto)
print(lista)

pares = [("nombre","ana"), ("edad",24)]
diccionario = dict(pares)
print(diccionario)

persona = {"nombre":"luis", "edad":34}
claves = list(persona.keys())
print(claves)
valores = list(persona.values())
print(valores)
pares = list(persona.items())
print(pares)

import json
texto = '{"nombre":"carlos", "edad":25}'
diccionario = json.loads(texto)
print(diccionario)

nuevo_texto = json.dumps(diccionario)
print(nuevo_texto)
print(type(nuevo_texto))

datos = [
    ("nombre", "Marta"),
    ("edad", 22),
    ("activo", True)
]

diccionario = dict(datos)
print(diccionario)

valores = list(diccionario.values())
print(f"los valores son {valores}")

frutas = ["manzana", "banana", "cereza"]
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")

nombres = ["ana", "luis", "marta"]
mayus = [n.upper() for n in nombres]
print(mayus)

numeros = [1,2,3]
cua = {n:n**2 for n in numeros}
print(cua)

alumnos = {
    "Juan": [8, 7, 9],
    "Ana": [10, 9, 10],
    "Pedro": [6, 5, 7]
}

lista = {i:sum(v)/len(v) for i, v in alumnos.items()}

for k, v in lista.items():
    print(f"{k} tiene promedio {v:.2f}")

for i in range(1,20,4):
    print(i)

numeros = list(range(0, 20))
print(numeros)

for i in range(1, 4):
    for j in range(1,4):
        print(f"{i} x {j} = {i*j}")
    print("------------")