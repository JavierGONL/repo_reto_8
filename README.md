<div align='center'>
<figure> <img src="https://i.postimg.cc/ZYLWq9xH/error-418.png" alt="" width="300" height="auto"/></br>
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
import math
def factorial (numeroN = int)->int:
    if numeroN == 0:
        return 1
    else:
        return numeroN * factorial(numeroN - 1)
def funcion_exponencial (numeroX = float, numeroN : int = 120)-> float:
    resultado = 0
    for i in range(numeroN):
        serie_de_maclaurin = (numeroX**i)/(factorial(i))
        resultado += serie_de_maclaurin
    return resultado
def rango_de_error(numeroX, numeroN):
    maclaurin = funcion_exponencial(numeroX, numeroN)
    math_exp = math.exp(numeroX) 
    error_relativo = (math_exp - maclaurin) / math_exp
    porcentaje_error = abs(error_relativo) * 100
    return porcentaje_error
if __name__ == "__main__":
    numeroX = float(input("ingrese un numero real: "))    
    resultado = funcion_exponencial(numeroX)
    print(f"resultado de la aproximacion: {resultado} y el resultado real es {math.exp(numeroX)} y el rango de error es {rango_de_error(numeroX,120)}%")
```
9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
$$sin(x) \approx sin(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)!}$$
_________________________________________
```python
import math
def factorial (numeroN = int)->int:
    if numeroN == 0:
        return 1
    else:
        return numeroN * factorial(numeroN - 1)
def funcion_seno(numeroX: float, numeroN: float = 20) -> float:
    resultado = 0
    for n in range(numeroN + 1):
        seno_serie_maclaurin = ((-1) ** n) * ((numeroX) ** (2 * n + 1)) / factorial(2 * n + 1)
        resultado += seno_serie_maclaurin
    return resultado
def rango_de_error(numeroX, numeroN):
    maclaurin = funcion_seno(numeroX, numeroN)
    math_sin = math.sin(numeroX)
    error_relativo = (math_sin - maclaurin) / math_sin
    porcentaje_error = abs(error_relativo) * 100
    return porcentaje_error    
if __name__ == "__main__":
    numeroX = float(input("ingrese un numero: "))
    print(f"el resultado aproximado de la funcion seno es: {funcion_seno(numeroX)}, el verdadero es: {math.sin(numeroX)} y el rango de error es {rango_de_error(numeroX, 20)}%")    
```
10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
$$arctan(x) \approx arctan(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)}$$
_________________________________________
```python
import math
def funcion_arctan(numeroX, numeroN=200):
    series = 0
    for i in range( numeroN+1):
        termino = (-1)**i
        arctan_series_maclaurin = (numeroX**((2*i)+1))/(2*i+1)
        series += termino * arctan_series_maclaurin
    return series
def rango_de_error(numeroX, numeroN):
    maclaurin = funcion_arctan(numeroX, numeroN)
    math_arctan = math.atan(numeroX)
    error_relativo = (math_arctan - maclaurin) / math_arctan
    porcentaje_error = abs(error_relativo) * 100
    return porcentaje_error
if __name__ == "__main__":
    numeroX = float(input("ingrese un numeroen el rango(-1,1): "))
    if numeroX >1 or numeroX <-1:
        print("el numero ingresado no esta en el rango")
        exit()
    else:
        print(f"el resultado de la funcion arctan aproximada es {funcion_arctan(numeroX,)}, y el real es {math.atan(numeroX)} y el rango de error es aprox: {rango_de_error(numeroX, 200)}%")
```
