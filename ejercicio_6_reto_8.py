if __name__ == "__main__":
    
    numeroX = float(input("ingrese un numero real: "))
    numeroN = int(input("ingrese un numero natural(N>=0): "))
    primerX = numeroX
    for x in range(1,int(numeroN),1): 
        numeroX *= numeroX
        resultado = numeroX
    print(f"el cuadrado de {primerX} elevado a la {numeroN} es igual a {resultado}")