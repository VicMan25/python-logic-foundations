#Tarifas segun nivel y modo de entrega
tarifas = {
    "basico": {"presencial": 500000, "virtual": 400000},
    "intermedio": {"presencial": 800000, "virtual": 600000},
    "avanzado": {"presencial": 1200000, "virtual": 1000000},
}

#Descuento para estudiantes recurrentes
descuento_recurrente = 0.10

nivel = input("Ingrese el nivel del curso (basico/intermedio/avanzado): ").lower()
modo = input("Ingrese el modo de entrega (presencial/virtual): ").lower()
es_recurrente = input("¿Es estudiante recurrente? (sí/no): ").lower()

if nivel in tarifas and modo in tarifas[nivel]:
    tarifa_base = tarifas[nivel][modo]
else:
    print("Nivel o modo de entrega no válido.")
    exit()

#Descuento si el estudiante es recurrente
descuento = 0
if es_recurrente == "sí" or es_recurrente == "si":
    descuento = tarifa_base * descuento_recurrente

#Costo final con descuento aplicado
tarifa_final = tarifa_base - descuento

print("\n--- RESUMEN DE PAGO ---")
print(f"Tarifa base del curso: ${tarifa_base:,.0f}")
print(f"Descuento aplicado: -${descuento:,.0f}")
print(f"TOTAL A PAGAR: ${tarifa_final:,.0f}")
