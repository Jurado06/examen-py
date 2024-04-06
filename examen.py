class Producto:
    def __init__(self, id, nombre, precio_unitario, pais_origen, unidades_existentes, garantia):
        self.id = id
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.pais_origen = pais_origen
        self.unidades_existentes = unidades_existentes
        self.garantia = garantia

class Inventario:
    def __init__(self):
        self.productos = []

    def registrar_producto(self, producto):
        self.productos.append(producto)

class Fruta:
    def __init__(self, id, nombre, precio_unitario, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
    
    def costo_total(self):
        return self.precio_unitario * self.cantidad


def main():
    inventario = Inventario()
    
    inventario.registrar_producto(Producto(1, "Manzana", 0.75, "Estados Unidos", 10, True))
    inventario.registrar_producto(Producto(2, "Papaya", 0.50, "Ecuador", 8, True))
    inventario.registrar_producto(Producto(3, "Fresa", 1.20, "Espana", 6, False))
    inventario.registrar_producto(Producto(4, "Pina", 1.80, "Costa Rica", 7, True))
    inventario.registrar_producto(Producto(5, "Uva", 2.00, "Italia", 9, False))
    inventario.registrar_producto(Producto(6, "Mango", 1.50, "Mexico", 5, True))
    inventario.registrar_producto(Producto(7, "Sandia", 3.00, "Espana", 4, False))
    inventario.registrar_producto(Producto(8, "Kiwi", 1.30, "Nueva Zelanda", 7, True))
    inventario.registrar_producto(Producto(9, "Naranja", 0.90, "Espana", 8, True))
    inventario.registrar_producto(Producto(10, "Uchuva", 0.60, "Mexico", 6, False))
    
    while True:
        print("\n1. Mostrar frutas existentes")
        print("2. Agregar nueva fruta al inventario")
        print("3. Mostrar costo total del salpicón")
        print("4. Mostrar frutas ordenadas por costo")
        print("5. Mostrar fruta más barata")
        print("6. Salir")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            print("\nFrutas existentes:")
            for producto in inventario.productos:
                print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio unitario: {producto.precio_unitario}, Cantidad: {producto.unidades_existentes}")
        
        elif opcion == 2:
            nueva_fruta = recibir_fruta_por_teclado()
            inventario.registrar_producto(nueva_fruta)
            print("¡Fruta agregada al inventario!")
        
        elif opcion == 3:
            mostrar_costo_total(inventario.productos)
            
        
        elif opcion == 4:
            mostrar_frutas_ordenadas_por_costo(inventario.productos)
        
        elif opcion == 5:
            mostrar_fruta_mas_barata(inventario.productos)
        
        elif opcion == 6:
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Intente de nuevo.")


def recibir_fruta_por_teclado():
    id = int(input("Ingrese el ID de la fruta: "))
    nombre = input("Ingrese el nombre de la fruta: ")
    precio_unitario = float(input("Ingrese el precio unitario de la fruta: "))
    cantidad = int(input("Ingrese la cantidad de la fruta: "))
    return Producto(id, nombre, precio_unitario, "", cantidad, False)

def mostrar_costo_total(frutas):
    costo_total = sum(fruta.precio_unitario * fruta.unidades_existentes for fruta in frutas)
    print(f"El costo total del salpicón es: {costo_total}")

def mostrar_frutas_ordenadas_por_costo(frutas):
    frutas_ordenadas = sorted(frutas, key=lambda x: x.precio_unitario * x.unidades_existentes, reverse=True)
    print("Frutas ordenadas de mayor a menor costo:")
    for fruta in frutas_ordenadas:
        print(f"ID: {fruta.id}, Nombre: {fruta.nombre}, Precio unitario: {fruta.precio_unitario}, Cantidad: {fruta.unidades_existentes}")

def mostrar_fruta_mas_barata(frutas):
    fruta_mas_barata = min(frutas, key=lambda x: x.precio_unitario)
    print(f"La fruta más barata es: {fruta_mas_barata.nombre}, Precio unitario: {fruta_mas_barata.precio_unitario}")

if __name__ == "__main__":
    main()
