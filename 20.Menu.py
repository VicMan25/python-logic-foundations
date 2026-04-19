import os
os.system("cls")

#Victor Manuel Velasquez Benavides
#Anthony José Viveros Cabrera


def rango():
    num = 0
    while num <= 0:
        num = int(input("ingrese un numero mayor que 0 y menor que 5000: "))
    if num > 4000:
        print("Rango alto")
    elif num > 2000:
        print("Rango Medio")
    else:
        print("Rango bajo")

def division():
    num = int(input("ingrese un numero entre 10 y 90: "))
    if num >= 10 and num <=90:
        print("los numeros de", num, "son:")
        cantida = 0 
        for i in range (1,num+1):
            if num % i == 0:
                print(i)
                cantida += 1
        print("Cantida de divisiones", cantida)
    else:
        print("el numero esta fuera de rango")

   
def calcularCapital():
    print("---Proyección de Dinero a obtener---")
    capital = float(input("\nDigita el capital con el que se quiere cotizar:"))
    meses = int(input("\n¿A cuantos meses quieres realizar la cotización?"))
    interes=0.007
    for mes in range(1, meses + 1):
        capital *= (1 + interes)
        print(f"Mes {mes}: ${capital:.2f}")
        
def fibonacci():
    n = int(input("¿Cuántos números de Fibonacci quieres? "))
    
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
        
def contador():
    rep3 = 0
    rep4 = 0
    rep5 = 0
    rep6 = 0
    for i in range(8):
        num = int(input("Ingrese un número entre 3 y 6, 8 veces: "))
        if num == 3:
            rep3 = rep3 + 1
        elif num == 4:
            rep4 = rep4 + 1
        elif num == 5:
            rep5 = rep5 + 1
        elif num == 6:
            rep6 = rep6 + 1

    if rep3 > 0:
        print("3 se repite", rep3, "veces. potencia:", 3**rep3)
    if rep4 > 0:
        print("4 se repite", rep4, "veces. potencia:", 4**rep4)
    if rep5 > 0:
        print("5 se repite", rep5, "veces. potencia:", 5**rep5)
    if rep6 > 0:
        print("6 se repite", rep6, "veces. potencia:",6**rep6)
    

while True:
    
    opcion = input(
        "MENÚ:\n"
        "1. Serie de Fibonacci\n"
        "2. Divisores\n"
        "3. Rango\n"
        "4. Banco\n"
        "5. Contador\n"
        "6. Salir\n\n"
        
        "Ingresa tu elección: "
    )

    if opcion == "1":
        fibonacci()
        
    elif opcion == "2":
        division()
        
    elif opcion == "3":
        rango()
          
    elif opcion == "4":
        calcularCapital()
        
    elif opcion == "5":
        contador()
        
        
    elif opcion == "6":
        print("\nSaliendo del sistema...")
        break
    
        
    else:
        print("\n⚠ Opción inválida. Intenta nuevamente.")
        input("Presiona Enter para continuar...")