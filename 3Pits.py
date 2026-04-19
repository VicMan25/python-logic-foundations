
autos = {
    "ligero": {"consumo": 0.1, "costo_litro": 5000, "costo_pit": 15000, "cambio_neumaticos": 50000},
    "alta_potencia": {"consumo": 0.2, "costo_litro": 5000, "costo_pit": 20000, "cambio_neumaticos": 100000}
}

tipo_auto = input("Ingrese el tipo de auto (Ligero-Alta_Potencia): ").lower()
distancia = float(input("Ingrese la distancia de la carrera en km: "))
num_pits = int(input("Ingrese el número de paradas en pits: "))
tiempo_pits = float(input("Ingrese el tiempo total en pits (minutos): "))
desgaste_neumaticos = float(input("Ingrese el porcentaje de desgaste de neumáticos (%): "))

if tipo_auto in autos:
    auto = autos[tipo_auto]

    combustible_necesario = auto["consumo"] * distancia
    costo_combustible = combustible_necesario * auto["costo_litro"]

    costo_pits = num_pits * auto["costo_pit"]

    penalidad = 0
    if tiempo_pits > 5:
        penalidad = 0.1 * costo_pits

    costo_neumaticos = 0
    if desgaste_neumaticos > 50:
        costo_neumaticos = auto["cambio_neumaticos"]

    costo_total = costo_combustible + costo_pits + penalidad + costo_neumaticos

    print("\n===== RESULTADOS =====")
    print(f"Combustible necesario: {combustible_necesario:} L")
    print(f"Costo del combustible: ${costo_combustible:}")
    print(f"Costo de pits: ${costo_pits:}")
    print(f"Penalidad por tiempo en pits: ${penalidad:}")
    print(f"Costo de cambio de neumáticos: ${costo_neumaticos:}")
    print(f"Costo total de la carrera: ${costo_total:}")

else:
    print("Tipo de auto inválido. Intente de nuevo.")
