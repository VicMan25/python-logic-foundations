tarifas = {
    "estandar": 10000,
    "expres": 20000
}

tipo_servicio = input("Ingrese el tipo de servicio (Estándar-Exprés): ").lower()
peso = float(input("Ingrese el peso del paquete en kg: "))
valor_declarado = float(input("Ingrese el valor declarado del paquete (0 si no desea seguro): "))
prioritario = input("¿El envío es prioritario? (si/no): ").lower()

if tipo_servicio in tarifas:
    
    costo_base = peso * tarifas[tipo_servicio]

    costo_seguro = valor_declarado * 0.02 if valor_declarado > 0 else 0

    recargo = costo_base * 0.10 if prioritario == "si" else 0

    costo_total = costo_base + costo_seguro + recargo

    print(f"\n ===== DETALLES DEL ENVIO ===== ")
    print(f"Tipo de servicio: {tipo_servicio}")
    print(f"Peso del paquete: {peso} kg")
    print(f"Costo base: ${costo_base:}")
    print(f"Costo del seguro: ${costo_seguro:}")
    print(f"Recargo por prioridad: ${recargo:}")
    print(f"Total a pagar: ${costo_total:}")

else:
    print("Error: Tipo de servicio no válido. Inténtelo de nuevo.")
