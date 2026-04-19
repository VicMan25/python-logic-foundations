productos = {
    "producto a": {"costo_unitario": 10000, "descuento": 0.05, "costo_reposicion": 50000},
    "producto b": {"costo_unitario": 20000, "descuento": 0.10, "costo_reposicion": 80000},
    "producto c": {"costo_unitario": 30000, "descuento": 0.15, "costo_reposicion": 120000}
}

producto = input("Ingrese el producto (A-B-C): ").lower()
cantidad = int(input("Ingrese la cantidad en inventario: "))
cantidad_comprar = int(input("Ingrese la cantidad a comprar: "))

producto = f"producto {producto}"  

if producto in productos:
    costo_unitario = productos[producto]["costo_unitario"]
    costo_total = costo_unitario * cantidad_comprar

    if cantidad_comprar > 100:
        descuento = productos[producto]["descuento"]
        costo_descuento = costo_total * descuento
        costo_total -= costo_descuento  

    if cantidad < 50:
        costo_total += productos[producto]["costo_reposicion"]

    print("\n==== DETALLES DE LA COMPRA ====:")
    print(f"Producto: {producto}")
    print(f"Cantidad en inventario: {cantidad}")
    print(f"Cantidad a comprar: {cantidad_comprar}")
    print(f"Costo total: ${costo_total:}")
else:
    print("Error: Producto no válido.")
