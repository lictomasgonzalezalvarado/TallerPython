
class Inventario:
    # Inventario inicial de la librería
    inventario = {
        "978-3-16-148410-0": {
            "titulo": "Python para principiantes",
            "autor": "Juan Pérez",
            "cantidad": 10,
            "precio": 20.00
        },
        "978-0-262-13472-9": {
            "titulo": "Aprendiendo JavaScript",
            "autor": "Ana Gómez",
            "cantidad": 5,
            "precio": 35.50
        },
        "978-1-56619-909-4": {
            "titulo": "Java para expertos",
            "autor": "Carlos Ramírez",
            "cantidad": 2,
            "precio": 45.99
        }
    }

    # Función para actualizar el inventario
    def actualizar_inventario(self,isbn, cantidad):
        if isbn in self.inventario:
            self.inventario[isbn]["cantidad"] += cantidad
            print(f"Inventario actualizado para '{self.inventario[isbn]['titulo']}'. Nueva cantidad: {self.inventario[isbn]['cantidad']}")
        else:
            print("ISBN no encontrado en el inventario.")

    # Función para mostrar detalles de un libro
    def mostrar_detalles_libro(self,isbn):
        libro = self.inventario.get(isbn)
        if libro:
            print(f"Título: {libro['titulo']}\nAutor: {libro['autor']}\nCantidad: {libro['cantidad']}\nPrecio: ${libro['precio']}")
        else:
            print("ISBN no encontrado en el inventario.")

    # Función para calcular el valor total del inventario
    def valor_total_inventario(self):
        total = sum(libro["cantidad"] * libro["precio"] for libro in self.inventario.values())
        print(f"Valor total del inventario: ${total:.2f}")

if __name__ == '__main__':

    inv=Inventario()
    # Uso de las funciones
    inv.actualizar_inventario("978-3-16-148410-0", 5)  # Aumenta la cantidad de ejemplares de un libro
    inv.mostrar_detalles_libro("978-0-262-13472-9")  # Muestra los detalles de un libro
    inv.valor_total_inventario()
