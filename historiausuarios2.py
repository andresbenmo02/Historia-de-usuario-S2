inventario = []

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")

    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio < 0:
            print("Error: El precio no puede ser negativo.")
            return
    except:
        print("Error: Precio invalido.")
        return

    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if cantidad < 0:
            print("Error: La cantidad no puede ser negativa.")
            return
    except:
        print("Error: Cantidad invalida.")
        return

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("Producto agregado correctamente.")

def mostrar_inventario():
    if len(inventario) == 0:
        print("El inventario esta vacio.")
    else:
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

def calcular_estadisticas():
    if len(inventario) == 0:
        print("No hay datos para calcular.")
        return

    total_valor = 0
    total_productos = 0

    for producto in inventario:
        total_valor += producto["precio"] * producto["cantidad"]
        total_productos += producto["cantidad"]

    print(f"Valor total del inventario: {total_valor}")
    print(f"Cantidad total de productos: {total_productos}")

continuar = "si"

while continuar == "si":
    print("\n--- MENU ---")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        calcular_estadisticas()
    elif opcion == "4":
        continuar = "no"
        print("Saliendo del programa...")
    else:
        print("Opcion invalida, intente nuevamente.")