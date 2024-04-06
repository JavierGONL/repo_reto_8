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