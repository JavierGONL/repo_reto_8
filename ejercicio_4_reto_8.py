def factorial (numeroN = int)->int:
    if numeroN == 0:
        return 1
    else:
        return numeroN * factorial(numeroN - 1)
    
if __name__ == '__main__':
    numeroN = int(input("Ingrese un numero entero: "))
    print(f"El factorial de {numeroN} es {factorial(numeroN)}")