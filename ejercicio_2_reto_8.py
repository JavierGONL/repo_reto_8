#Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.


if __name__ == '__main__':
    print("Numeros impares desde 1 hasta 999")
    for i in range(1, 1000, 2):
        print(i)

    print("Numeros pares desde 2 hasta 1000")
    for i in range(2, 1001, 2):
        print(i)