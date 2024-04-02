<div align='center'>
<figure> <img src="https://i.postimg.cc/HkMddSNw/error-418.png" alt="" width="300" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

# repo_reto_8

1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
________________________________
```python
#Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

if __name__ == "__main__":
    for i in range(1,101):
        print(f"{i} al cuadrado es {i**2}")
```

2.  Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
_________________________________________
```python
#Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.


if __name__ == '__main__':
    print("Numeros impares desde 1 hasta 999")
    for i in range(1, 1000, 2):
        print(i)

    print("Numeros pares desde 2 hasta 1000")
    for i in range(2, 1001, 2):
        print(i)
```
3.  Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
_________________________________________
```python
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
```
4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
_________________________________________
```python
def factorial (numeroN = int)->int:
    if numeroN == 0:
        return 1
    else:
        return numeroN * factorial(numeroN - 1)
    
if __name__ == '__main__':
    numeroN = int(input("Ingrese un numero entero: "))
    print(f"El factorial de {numeroN} es {factorial(numeroN)}")
```
5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.
_________________________________________
```python
if __name__ == "__main__":
    numeroN : int = input("ingrese un numero: ")
    lista : int = [numeroN]
    for n in lista:
        print(2**n)
```
6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. **Disclaimer:** Trate de no utilizar el operador de potencia (**).
_________________________________________
```python
if __name__ == "__main__":
    
    numeroX = float(input("ingrese un numero real: "))
    numeroN = int(input("ingrese un numero natural(N>=0): "))
    primerX = numeroX
    for x in range(1,int(numeroN),1): 
        numeroX *= numeroX
        resultado = numeroX
    print(f"el cuadrado de {primerX} elevado a la {numeroN} es igual a {resultado}")
```
7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
_________________________________________
```python
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
```
8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
$$e^x \approx exp(x,n) \approx \sum_{i=0}^{n}\frac{x^i}{i!}$$
_________________________________________
```python

```
9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
$$sin(x) \approx sin(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)!}$$
_________________________________________
```python

```
10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
$$arctan(x) \approx arctan(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)}$$

**Disclaimer:** Para las aproximaciones de series determine con que valor n se obtiene menos del 0.1% de error.
_________________________________________
```python

```
