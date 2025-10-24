# sumar = lambda a,b: a + b
# print(sumar(3,5))

# def aplicar(f,x):
#     return f(x)

# doble = lambda n: n ** 2
# print(aplicar(doble,4))

# numeros = [v for v in range(1,11)]

# doble = list(map(lambda x:x**2, numeros))
# print(doble)

# others = [v for v in range(10,31,5)]

# pares = list(filter(lambda x : x % 2==0, others))
# print(f"pares: {pares}")

# from functools import reduce
# numero = [i for i in range(1,5)]

# producto = reduce(lambda a, b: a * b, numero)
# print(f"producto {producto}")

# def aplicar_operacion(func, datos):
#     return [func(x) for x in datos]

# resultados = aplicar_operacion(lambda x : x * 2, [1, 2, 3])
# print(resultados)


# names = ["ana", "luis", "marta"]
# mayus = list(map(lambda n: n.title(), names))
# print(mayus)

# edades = [18, 25, 30, 15, 40]

# mayores = list(filter(lambda e: e >= 19, edades))
# print(mayores)

# numeros = [2, 3, 4]
# producto = reduce(lambda a, b: a * b, numeros)
# print(producto)

from functools import reduce
productos = [
    {"nombre": "Laptop", "precio": 1000, "activo": True},
    {"nombre": "Teclado", "precio": 80, "activo": True},
    {"nombre": "Mouse", "precio": 50, "activo": False},
    {"nombre": "Monitor", "precio": 200, "activo": True}
]

activities = list(filter( lambda p: p["activo"], productos))
con_iva = list(map(lambda p: {**p, "precio_con_iva":round(p["precio"]* 1.21, 2)}, activities))
total = reduce(lambda acc, p: acc + p["precio_con_iva"], con_iva, 0)
print(f"total: {total}")

productos = [
    {"nombre": "Laptop", "precio": 1000, "activo": True},
    {"nombre": "Teclado", "precio": 80, "activo": True},
    {"nombre": "Mouse", "precio": 50, "activo": False},
    {"nombre": "Monitor", "precio": 200, "activo": True}
]

activos = list(filter(lambda p: p["activo"], productos))
con_iva = list(map(lambda p: {**p, "precio_con_iva": round(p["precio"] * 1.21, 2)}, activos))
total = reduce(lambda acc, p: acc + p["precio_con_iva"], con_iva, 0)

print(con_iva)
print("💰 Total con IVA:", total)