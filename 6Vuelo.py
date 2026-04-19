#Precios segun clase de vuelo
costo_base_economica = 300000
costo_base_ejecutiva = 600000
costo_base_primera = 1200000

#Costa dependiendo escala
costo_escala_economica = 50000
costo_escala_ejecutiva = 75000
costo_escala_primera = 100000

#Costo equipaje
equipaje_menor_20kg_economica = 30000
equipaje_mayor_20kg_economica = 50000
equipaje_menor_20kg_ejecutiva = 20000
equipaje_mayor_20kg_ejecutiva = 40000
equipaje_menor_20kg_primera = 0
equipaje_mayor_20kg_primera = 0

#Descuento por fidelidad
descuento_fidelidad = 0.10

clase_vuelo = input("Ingrese la clase de vuelo (economica, ejecutiva, primera): ").lower()
escalas = int(input("Ingrese la cantidad de escalas: "))
peso_equipaje = float(input("Ingrese el peso del equipaje en kg: "))
es_fiel = input("¿Pertenece al programa de fidelidad? (si/no): ").lower() == "si"

if clase_vuelo == "economica":
    costo_base = costo_base_economica
    costo_escala = costo_escala_economica
    costo_equipaje = equipaje_mayor_20kg_economica if peso_equipaje >= 20 else equipaje_menor_20kg_economica
elif clase_vuelo == "ejecutiva":
    costo_base = costo_base_ejecutiva
    costo_escala = costo_escala_ejecutiva
    costo_equipaje = equipaje_mayor_20kg_ejecutiva if peso_equipaje >= 20 else equipaje_menor_20kg_ejecutiva
elif clase_vuelo == "primera":
    costo_base = costo_base_primera
    costo_escala = costo_escala_primera
    costo_equipaje = equipaje_mayor_20kg_primera if peso_equipaje >= 20 else equipaje_menor_20kg_primera
else:
    print("Clase de vuelo no válida.")
    exit()

subtotal = costo_base + (costo_escala * escalas) + costo_equipaje
monto_descuento = subtotal * descuento_fidelidad if es_fiel else 0
total = subtotal - monto_descuento

print("\n--- RESUMEN DEL VUELO ---")
print(f"Subtotal: ${subtotal:,.2f}")
print(f"Descuento de fidelidad (10%): -${monto_descuento:,.2f}")
print(f"TOTAL A PAGAR: ${total:,.2f}")
