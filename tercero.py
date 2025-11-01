class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def vender(self, cantidad):
        if cantidad <= self.stock:
            print(f"✅ Venta realizada: {cantidad} unidades de {self.nombre}")
        else:
            print(f"📦 Producto: {self.nombre} | 💰 Precio: ${self.precio} | 🏷️ Stock: {self.stock}")
    
    def mostrar_info(self):
        print(self.nombre)
        print(self.precio)
        print(self.stock)


p1 = Producto("Laptop", 1200, 10)
p2 = Producto("Teclado", 50, 20)

p1.mostrar_info()
p1.vender(3)
p1.mostrar_info()

p2.mostrar_info()
p2.vender(25)
