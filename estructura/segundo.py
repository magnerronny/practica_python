# class Usuario:
#     def __init__(self, nombre, correo):
#         self.nombre = nombre
#         self.correo = correo
    
#     def saludar(self):
#         print(f"hola, soy {self.nombre}. mi correo es {self.correo}")
    
# user1 = Usuario("Ana", "ana@mail.com")
# user2 = Usuario("Luis", "luis@mail.com")

# user1.saludar()
# user2.saludar()
# print(user1.nombre)  # Ana
# user1.nombre = "Ana Gómez"
# print(user1.nombre)  # Ana Gómez


# class Usuario:
#     def __init__(self, nombre, correo):
#         self.nombre = nombre
#         self.correo =  correo
#         self.activo = True
    
#     def desactivar(self):
#         self.activo =  False
    
#     def mostrar_info(self):
#         estado = "activo" if self.activo else "inactivo"
#         print(f"{self.nombre} ({self.correo}) esta en estado {self.activo}")

# user2 = Usuario("Luis", "luis@mail.com")
# user2.mostrar_info()
# user2.desactivar()
# user2.mostrar_info()


# class Usuario:
#     def __init__(self, nombre, correo, contraseña):
#         self.nombre = nombre
#         self.correo = correo
#         self.__contraseña = contraseña
#         self.activo = True
    
#     def verificar_contraseña(self, intento):
#         return intento == self.__contraseña

#     def descativar(self):
#         self.activo = False

# admin = Usuario("Admin", "admin@mail.com", "1234")

# # Verificar acceso
# print(admin.verificar_contraseña("1234"))  # True
# print(admin.verificar_contraseña("0000"))  # False

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def vender(self, cantidad):
        self.stock -= cantidad
    
    def mostrar(self):
        print(self.nombre, self.precio, self.stock)

producto1 = Producto('palta',234,5)
producto1 = Producto('atun',23,5)

producto1.vender(2)
producto1.mostrar()