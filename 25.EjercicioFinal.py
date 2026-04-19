import os
os.system("cls")

equipos = {
    1: {"nombre": "Real Madrid", "cuota": 2.0},
    2: {"nombre": "Barcelona", "cuota": 2.5},
    3: {"nombre": "Manchester City", "cuota": 3.0}
}

apuestas = []
total_recaudado = 0
apuestas_por_equipo = {1: 0, 2: 0, 3: 0}

def menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Apostar")
    print("2. Resumen de Apuestas")
    print("3. Salir")
    return input("Elige una opción: ")

def descuento(monto):
    if monto < 20000:
        return 0
    elif monto <= 50000:
        return 0.05
    else:
        return 0.1

while True:
    opcion = menu()

    if opcion == "1":
        nombre = input("\nNombre del apostador: ")

        print("\nEquipos disponibles:")
        for k, v in equipos.items():
            print(f"{k}. {v['nombre']} (Cuota x{v['cuota']})")

        eleccion = int(input("Elige un equipo (1-3): "))

        if eleccion not in equipos:
            print("Opción inválida.")
            continue

        monto = float(input("Valor de la apuesta ($): "))
        desc = descuento(monto)
        total = monto * (1 - desc)
        ganancia = total * equipos[eleccion]["cuota"]

        total_recaudado += total
        apuestas_por_equipo[eleccion] += total

        apuesta = (nombre, equipos[eleccion]["nombre"], monto, total, ganancia)
        apuestas.append(apuesta)

        print(f"\n {nombre} apostó ${monto:,.0f} al {equipos[eleccion]['nombre']}.")
        print(f"Descuento aplicado: {desc*100:.0f}%")
        print(f"Posible ganancia: ${ganancia:,.0f}\n")

    elif opcion == "2":
        print("\n=== RESUMEN DE APUESTAS ===")
        if not apuestas:
            print("No hay apuestas registradas.")
        else:
            for a in apuestas:
                print(f"{a[0]} → {a[1]} | Apostó ${a[2]:,.0f} | Posible ganancia ${a[4]:,.0f}")

            print("\nTotal recaudado: ${:,.0f}".format(total_recaudado))
            print("Apuestas por equipo:")
            for k, v in equipos.items():
                print(f"{v['nombre']}: ${apuestas_por_equipo[k]:,.0f}")

    elif opcion == "3":
        print("\n Gracias por jugar Apuestas ToñosBeth.........")
        break
    else:
        print("Opción inválida, intenta nuevamente.")
