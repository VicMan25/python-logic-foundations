tarifas = {
    "america": 10000,
    "europa": 20000,
    "asia": 30000
}

destino = input("Ingrese el destino de su paquete (America-Europa-Asia): ").lower()
peso = float(input("Ingrese el peso del paquete en kg: "))
valor_declarado = float(input("Ingrese el valor declarado del paquete: "))
seguro = input("¿Desea incluir seguro? (Si/No): ").lower()
acceso= input("Es de dificil acceso? (Si/No): ").lower()

if destino in tarifas:

    costo_base = tarifas[destino] * peso

    costo_seguro = (0.01 * valor_declarado) if seguro == "Si" else 0
    
    costo_acceso = 20000 if acceso == "si" else 0
    
    costo_total = costo_base + costo_seguro + costo_acceso

    # Mostrar resultados
    print("\n===== COSTO DEL ENVÍO =====")
    print(f"Destino: {destino}")
    print(f"Peso del paquete: {peso:} kg")
    print(f"Costo base del envío: ${costo_base:}")
    print(f"Costo del seguro: ${costo_seguro:}")
    print(f"Costo del acceso: ${costo_acceso:}")
    print(f"Costo total del envío: ${costo_total:}")

else:
    print("Destino inválido. Intente de nuevo.")
