suma = lambda a, b: a + b
print(suma(4,3))

def aplicar(f,x):
    return f(x)

doble = lambda n: n * 2

print(aplicar(doble,4))

numeros = [1, 2, 3, 4]
dobles = list(map(lambda x: x*2, numeros))
print(dobles)

numeros = list(range(10,31,5))
pares = list(filter(lambda x: x%2==0, numeros))
print(pares)

from functools import reduce

numeros = list(range(1,5))
producto = reduce(lambda a,b: a*b, numeros)
print(producto)


productos = [
    {"nombre": "Laptop", "precio": 1000, "activo": True},
    {"nombre": "Mouse", "precio": 50, "activo": False},
    {"nombre": "Teclado", "precio": 80, "activo": True},
    {"nombre": "Monitor", "precio": 200, "activo": True}
]

activos = list(filter(lambda x: x["activo"] == True, productos))
print(activos)
con_iva = list(map(lambda p: p["precio"] * 1.21, activos))
print(con_iva)

total = reduce(lambda a, b: a + b, con_iva)

print("Total de venta con IVA:", round(total, 2))
