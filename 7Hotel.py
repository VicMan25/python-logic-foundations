tarifas_habitacion = {
    "alta": {"estandar": 250000, "suite": 400000, "presidencial": 700000},
    "media": {"estandar": 250000, "suite": 400000, "presidencial": 700000},
    "baja": {"estandar": 250000, "suite": 400000, "presidencial": 700000}
}

servicios_adicionales = {
    "desayuno": {"alta": 20000, "media": 30000, "baja": 50000},
    "spa": {"alta": 50000, "media": 80000, "baja": 120000},
    "transporte": {"alta": 30000, "media": 40000, "baja": 60000}
}

descuentos_fidelidad = {
    "bronce": 0.05,
    "plata": 0.10,
    "oro": 0.15
}

temporada = input("Ingrese la temporada (Alta-Media-Baja): ").lower()
habitacion = input("Ingrese el tipo de habitación (Estándar-Suite-Presidencial): ").lower()
noches = int(input("Ingrese el número de noches: "))
fidelidad = input("Ingrese su nivel de fidelidad (Bronce-Plata-Oro): ").lower()

incluye_desayuno = input("¿Desea incluir desayuno? (Si/No): ").lower() == "si"
incluye_spa = input("¿Desea incluir spa? (Si/No): ").lower() == "si"
incluye_transporte = input("¿Desea incluir transporte al aeropuerto? (Si/No): ").lower() == "si"

if temporada in tarifas_habitacion and habitacion in tarifas_habitacion[temporada]:
    
    costo_base = tarifas_habitacion[temporada][habitacion] * noches

    costo_servicios = 0
    if incluye_desayuno:
        costo_servicios += servicios_adicionales["desayuno"][temporada] * noches
    if incluye_spa:
        costo_servicios += servicios_adicionales["spa"][temporada] * noches
    if incluye_transporte:
        costo_servicios += servicios_adicionales["transporte"][temporada] * 2

    descuento_noches = 0
    if noches > 7:
        descuento_noches = costo_base * 0.15

    descuento_fidelidad = costo_base * descuentos_fidelidad.get(fidelidad, 0)

    costo_total = (costo_base + costo_servicios) - (descuento_noches + descuento_fidelidad)

    print("\n===== DETALLE DE LA RESERVACIÓN =====")
    print(f"Temporada: {temporada}")
    print(f"Tipo de Habitación: {habitacion}")
    print(f"Número de noches: {noches}")
    print(f"Costo base: ${costo_base:}")
    print(f"Costo servicios adicionales: ${costo_servicios:}")
    print(f"Descuento (>7 noches): -${descuento_noches:}")
    print(f"Descuento Fidelidad ({fidelidad}): -${descuento_fidelidad:}")
    print(f"Costo total: ${costo_total:}")

else:
    print("Opción de temporada o habitación no válida. Intente nuevamente.")
