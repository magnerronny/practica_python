def validar_correo(correo):
    return "@" in correo and "." in correo

print(validar_correo("ana@mail.com"))  # True
print(validar_correo("ana#mail"))      # False


def calcular_precio_final(precio, iva):
    return precio + precio * iva

print(calcular_precio_final(100, 0.21))  # 121.0
print(calcular_precio_final(100, 0.21))  # 121.0 (siempre igual)

nuevo = [1,2,3]
dos = [4,5,6,76]

nuevs = nuevo + dos
print(nuevs)