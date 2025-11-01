# class Usuario:
#     def __init__(self, nombre, correo):
#         self.nombre = nombre
#         self.correo = correo
    
#     def saludar(self):
#         print(f"hola, soy {self.nombre}. mi correo es {self.correo}")
    
# user1 = Usuario("felix", "felix@gmail.com")
# user1.saludar()

# user1.nombre = "rafael"
# user1.saludar()


class Usuario:
    def __init__(self, nombre, correo, contraseña):
        self.nombre = nombre
        self.correo = correo
        self.__contraseña = contraseña
        self.activo = True
    
    def verificar_contraseña(self, intento):
        # print(intento)
        # print(self.__contraseña)
        return intento == self.__contraseña
    
    def desactivar(self):
        self.activo = False


admin = Usuario("Admin", "admin@mail.com", "1234")
print(admin.verificar_contraseña("DFSDF3"))
print(admin.verificar_contraseña("1234"))