import os
os.system("cls")

precios = {
    1: {1:20000, 2:15000, 3:12000},   # Pasto
    2: {1:30000, 2:25000, 3:20000},   # Cali
    3: {1:10000, 2:8000,  3:5000}     # Popayán
}

def desc(cantidad):
    if cantidad < 5:
        return 0
    elif cantidad <= 12:
        return 0.1
    else:
        return 0.2

def menu():
    print("\n--- VIAJES ---")
    print("1. Vender pasaje")
    print("2. Salir")
    opc = int(input("¿Cuál es su opción? "))
    return opc

def datos():
    print("\n--- DESTINOS ---")
    print("1. Pasto")
    print("2. Cali")
    print("3. Popayán")
    destino = int(input("Seleccione destino (1-3): "))

    print("\nClases disponibles:")
    print("1. Primera clase")
    print("2. Segunda clase")
    print("3. Tercera clase")
    clase = int(input("Seleccione clase (1-3): "))

    cantidad = int(input("¿Cuántos pasajes necesita? "))
    return destino, clase, cantidad

def valorPa(destino, clase):
    return precios[destino][clase]

def pago(cantidad, valorBase, descuento):
    subtotal = cantidad * valorBase
    total = subtotal - (subtotal * descuento)
    return total

def main():
    totalRecaudo = 0
    pasajesVendidos = {1:0, 2:0, 3:0}  # Para contar por destino

    while True:
        opc = menu()
        if opc == 1:
            destino, clase, cantidad = datos()

            if destino in precios and clase in precios[destino]:
                valorBase = valorPa(destino, clase)
                descuento = desc(cantidad)
                total = pago(cantidad, valorBase, descuento)
                totalRecaudo += total
                pasajesVendidos[destino] += cantidad
                print(f"\nEl valor a pagar es: ${total:,}")

        elif opc == 2:
            print("\n--- RESUMEN DE VENTAS ---")
            print(f"Pasto: {pasajesVendidos[1]} pasajes")
            print(f"Cali: {pasajesVendidos[2]} pasajes")
            print(f"Popayán: {pasajesVendidos[3]} pasajes")
            print(f"Total recaudado: ${totalRecaudo:,}")
            break
        else:
            print("Opción inválida")

main()
