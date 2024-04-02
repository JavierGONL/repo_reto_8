def tablas_de_multiplicar(tablas)->int:
    for x in range(0,int(tablas*11),tablas):
        if x == tablas*11:
            break
        print(x)
    return 'fin de las tablas'

if __name__ == "__main__":
    tablas = int(input("que tabla de multiplicar deseas(1-9):"))
    if tablas <= 10:
        print(f"las tablas de multiplicar del numero {tablas} es :")
        print(tablas_de_multiplicar(tablas))
    else: 
        print("solo numeros del 1 al 9 ya lo especifique")    