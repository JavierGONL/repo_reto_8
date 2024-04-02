#Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

if __name__ == '__main__':
    numeroN = int(input("Ingrese un numero entero: "))
    if numeroN % 2 == 0:
        for i in range(numeroN,0,-2):
            print(i)
    else:
        numeroN = numeroN - 1
        for i in range(numeroN,0,-2):
            print(i)