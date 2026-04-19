import os
os.system("cls")

num = int(input("Ingresa un número:"))
esPrimo=True

if num < 2:
    esPrimo =False
else: 
    for i in range(2, num):
        if num % i == 0:
            esPrimo= False
            break
if esPrimo:
    print(f'{num} este número es primo')
else:
    print(f'{num} el número no es primo')