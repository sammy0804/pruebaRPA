class Inventario:
    def __init__(self):
        self.productos = {'dairy': [], 'cleaning': [], 'grain': []}
        self.stock = {'dairy': [], 'cleaning': [], 'grain': []}

    def agregar_o_actualizar_producto(self, grupo, producto, cantidad):
        if producto in self.productos[grupo]:
            index = self.productos[grupo].index(producto)
            self.stock[grupo][index] += cantidad
        else:
            self.productos[grupo].append(producto)
            self.stock[grupo].append(cantidad)

    def mostrar_inventario(self):
        for grupo in self.productos:
            print(f"Grupo: {grupo.upper()}")
            print(f"{'Producto':<20} {'Cantidad':>10}")
            print("-" * 31)  # Separador de encabezado
            for producto, cantidad in zip(self.productos[grupo], self.stock[grupo]):
                print(f"{producto:<20} {cantidad:>10}")
            print("")


    def mostrar_menu(self):
        while True:
            print("Menú del Inventario")
            print("1. Agregar/Actualizar Producto")
            print("2. Mostrar Inventario")
            print("3. Salir")
            print("")
            opcion = input("Seleccione una opción: ")
            print("")

            if opcion == '1':
                grupo = input("Ingrese el grupo del producto (dairy, cleaning, grain): ")
                producto = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                self.agregar_o_actualizar_producto(grupo, producto, cantidad)
                print("Producto agregado/actualizado correctamente.\n")
            elif opcion == '2':
                self.mostrar_inventario()
            elif opcion == '3':
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.\n")
