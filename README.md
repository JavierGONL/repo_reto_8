<div align='center'>
<figure> <img src="https://i.postimg.cc/ZYLWq9xH/error-418.png" alt="" width="300" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

# repo_reto_8

### 1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
________________________________
```python
#Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

if __name__ == "__main__":
    for i in range(1,101):
        print(f"{i} al cuadrado es {i**2}")
```
+ explicacion del codigo: al usar un ciclo for en el rango de 1 a 101, se imprime el numero i y su cuadrado respectivo cuadrado con la formula i**2

### 2.  Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
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
+ explicacion del codigo: al usar un ciclo for en el rango de 1 a 1000, se imprime el numero i y sube de a 2 asegurando que sea el siguiente par o el siguiente impar, en el caso de los impares se inicia en 1 y en el caso de los pares se inicia en 2
### 3.  Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
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
+ explicacion del codigo: se pide un numero entero, si el numero es par se imprime en forma descendente hasta 2, si el numero es impar se le resta 1 y se imprime en forma descendente hasta 2

### 4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
_________________________________________
```python
def factorial (numeroN = int)->int:
    if numeroN == 0:
        return 1
    else:
        return numeroN * factorial(numeroN - 1)    
if __name__ == '__main__':
    numeroN = int(input("Ingrese un numero entero: "))
    for i in range (1,numeroN,1):
        print(f"El factorial de {i} es {factorial(i)}")
```
+ explicacion del codigo: se crea una funcion llamada factorial que recibe un numero entero y retorna el factorial de ese numero, luego se crea un ciclo for que recorre desde 1 hasta el numero ingresado por el usuario y se imprime el factorial de cada numero en el rango
  
### 5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.
_________________________________________
```python
if __name__ == "__main__":
    numeroN = int(input("ingrese un numero: "))
    for n in range(1,numeroN + 1,1):
        print(f"el numero 2 elevado a la potencia {n} es {2**n}")
```
+ explicacion del codigo: se pide un numero entero, se crea un ciclo for que recorre desde 1 hasta el numero ingresado por el usuario y se imprime 2 elevado a la n
  
### 6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. **Disclaimer:** Trate de no utilizar el operador de potencia (**).
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
+ explicacion del codigo: se pide al usuario que ingrese un numero real y un numero natural, se crea una variable primerX que guarda el valor de numeroX, luego se crea un ciclo for que recorre desde 1 hasta el numero ingresado por el usuario y se multiplica el numeroX por si mismo, se guarda el resultado en la variable resultado esto hasta que el ciclo for llega a la iteracion n y se imprime el resultado

### 7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
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
    if tablas <= 10 and tablas > 0:
        print(f"las tablas de multiplicar del numero {tablas} es :")
        print(tablas_de_multiplicar(tablas))
    else: 
        print("solo numeros del 1 al 9 ya lo especifique")
```
+ explicacion del codigo: se crea una funcion llamada tablas_de_multiplicar que recibe un numero entero y crea un ciclo for que recorre desde 0 hasta el numero ingresado por el usuario multiplicado por 11, si x es igual al numero ingresado por el usuario multiplicado por 11 se rompe el ciclo y se imprime fin de las tablas, si no se imprime x, luego se pide al usuario que ingrese un numero entero y si el numero ingresado es menor o igual a 10 se imprime las tablas de multiplicar del numero ingresado por el usuario, si no se imprime que solo numeros del 1 al 9

### 8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
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
+ explicacion del codigo: creo una funcion que calcula el factorial de un numero luego una funcion llamada funcion_exponencial que recibe dos numeros, uno real y otro entero, se crea una variable resultado que almacena el valor 0, se crea un ciclo for que recorre desde 0 hasta el numero entero ingresado, se crea una variable serie_de_maclaurin que almacena el valor de elevar el numero real ingresado a la i y dividirlo por el factorial de i, se suma la variable serie_de_maclaurin a la variable resultado y se retorna resultado, luego se crea una funcion llamada rango_de_error que recibe dos numeros, uno real y otro entero, se crea una variable maclaurin que almacena el valor de la funcion_exponencial con los dos numeros ingresados, se crea una variable math_exp que almacena el valor de la funcion exp de la libreria math con el numero real ingresado, se crea una variable error_relativo que almacena el valor de la resta de math_exp menos maclaurin dividido por math_exp, se crea una variable porcentaje_error que almacena el valor absoluto de error_relativo multiplicado por 100, se retorna porcentaje_error, luego se pide al usuario que ingrese un numero real y se imprime el resultado de la aproximacion, el resultado real y el rango de error

### 9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
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
+ explicacion del codigo: creo una funcion que calcula el factorial de un numero luego una funcion llamada funcion_seno que recibe dos numeros, uno real y otro entero, se crea una variable resultado que almacena el valor 0, se crea un ciclo for que recorre desde 0 hasta el numero entero ingresado, se crea una variable seno_serie_maclaurin que almacena el valor de elevar -1 a la n y multiplicarlo por el numero real ingresado elevado a 2n+1 y dividirlo por el factorial de 2n+1, se suma la variable seno_serie_maclaurin a la variable resultado y se retorna resultado, luego se crea una funcion llamada rango_de_error que recibe dos numeros, uno real y otro entero, se crea una variable maclaurin que almacena el valor de la funcion_seno con los dos numeros ingresados, se crea una variable math_sin que almacena el valor de la funcion sin de la libreria math con el numero real ingresado, se crea una variable error_relativo que almacena el valor de la resta de math_sin menos maclaurin dividido por math_sin, se crea una variable porcentaje_error que almacena el valor absoluto de error_relativo multiplicado por 100, se retorna porcentaje_error, luego se pide al usuario que ingrese un numero real y se imprime el resultado de la aproximacion, el resultado real y el rango de error
  
### 10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
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
    numeroX = float(input("ingrese un numero en el rango(-1,1): "))
    if numeroX >1 or numeroX <-1:
        print("el numero ingresado no esta en el rango")
        exit()
    else:
        print(f"el resultado de la funcion arctan aproximada es {funcion_arctan(numeroX,)}, y el real es {math.atan(numeroX)} y el rango de error es aprox: {rango_de_error(numeroX, 200)}%")
```
+ explicacion del codigo: creo una funcion llamada funcion_arctan que recibe dos numeros, uno real y otro entero, se crea una variable series que almacena el valor 0, se crea un ciclo for que recorre desde 0 hasta el numero entero ingresado, se crea una variable termino que almacena el valor de elevar -1 a la i, se crea una variable arctan_series_maclaurin que almacena el valor de elevar el numero real ingresado a 2i+1 y dividirlo por 2i+1, se suma el producto de termino por arctan_series_maclaurin a la variable series y se retorna series, luego se crea una funcion llamada rango_de_error que recibe dos numeros, uno real y otro entero, se crea una variable maclaurin que almacena el valor de la funcion_arctan con los dos numeros ingresados, se crea una variable math_arctan que almacena el valor de la funcion atan de la libreria math con el numero real ingresado, se crea una variable error_relativo que almacena el valor de la resta de math_arctan menos maclaurin dividido por math_arctan, se crea una variable porcentaje_error que almacena el valor absoluto de error_relativo multiplicado por 100, se retorna porcentaje_error, luego se pide al usuario que ingrese un numero real en el rango de -1 a 1 y se imprime el resultado de la aproximacion, el resultado real y el rango de error
