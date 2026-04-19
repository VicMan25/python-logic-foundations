tarifas = {
    "futbol": {"día_hábil": 100000, "fin_de_semana": 150000},
    "tenis": {"día_hábil": 80000, "fin_de_semana": 120000},
    "baloncesto": {"día_hábil": 90000, "fin_de_semana": 130000}
}

cancha = input("Ingrese el tipo de cancha (Fútbol-Tenis-Baloncesto): ").lower()
dia = input("¿Es día hábil o fin de semana? (Hábil-Fin de semana): ").lower()
horas = int(input("Ingrese la cantidad de horas de reserva: "))
personas = int(input("Ingrese la cantidad de personas: "))
miembro = input("¿Tiene membresía? (si/no): ").lower()

if cancha in tarifas:
    if dia == "habil":
        tarifa_hora = tarifas[cancha]["día_hábil"]
    elif dia == "fin de semana":
        tarifa_hora = tarifas[cancha]["fin_de_semana"]
    else:
        print("Error: Día no válido.")
        exit()

    costo_base = tarifa_hora * horas

    if personas > 10:
        costo_base *= 0.90

    if miembro == "si":
        costo_base *= 0.95

    print("\n==== DETALLES DE LA RESERVA ====:")
    print(f"Tipo de cancha: {cancha.capitalize()}")
    print(f"Día: {dia.capitalize()}")
    print(f"Horas reservadas: {horas}")
    print(f"Número de personas: {personas}")
    print(f"Costo total: ${costo_base:,.2f}")
else:
    print("Error: Tipo de cancha no válido.")
