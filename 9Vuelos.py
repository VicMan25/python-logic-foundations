def calcular_precio_vuelo():
    clases = {
        "economica": {"base": 300000, "escala": 50000, "comida": 20000, "entretenimiento": 30000, "vip": "comida"},
        "ejecutiva": {"base": 600000, "escala": 75000, "comida": 30000, "entretenimiento": 40000, "vip": "entretenimiento"},
        "primera": {"base": 1200000, "escala": 100000, "comida": 0, "entretenimiento": 0, "vip": "escala"}
    }
    
    print("Seleccione la clase de vuelo: \n1. Económica \n2. Ejecutiva \n3. Primera Clase")
    opcion = int(input("Ingrese el número correspondiente: "))
    
    if opcion == 1:
        clase = "economica"
    elif opcion == 2:
        clase = "ejecutiva"
    elif opcion == 3:
        clase = "primera"
    else:
        print("Opción inválida.")
        return
    
    num_escalas = int(input("Ingrese la cantidad de escalas: "))
    incluir_comida = input("¿Desea comidas a bordo? (si/no): ").lower() == "si"
    incluir_entretenimiento = input("¿Desea entretenimiento? (si/no): ").lower() == "si"
    es_vip = input("¿Es cliente VIP? (si/no): ").lower() == "si"
    
    costo_base = clases[clase]["base"]
    costo_escalas = num_escalas * clases[clase]["escala"]
    costo_comida = clases[clase]["comida"] if incluir_comida else 0
    costo_entretenimiento = clases[clase]["entretenimiento"] if incluir_entretenimiento else 0
    
    total = costo_base + costo_escalas + costo_comida + costo_entretenimiento
    
    if es_vip:
        total *= 0.9 
        beneficio_vip = clases[clase]["vip"]
        if beneficio_vip == "comida":
            print("Como cliente VIP, recibe comidas gratis.")
        elif beneficio_vip == "entretenimiento":
            print("Como cliente VIP, recibe entretenimiento gratis.")
        elif beneficio_vip == "escala":
            total -= clases[clase]["escala"] 
            print("Como cliente VIP, obtiene una escala gratis.")
    
    print(f"El costo total del vuelo es: ${total:}")
    
calcular_precio_vuelo()
