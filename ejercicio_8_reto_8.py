import math
def factorial (numeroN = int)->int:
    if numeroN == 0:
        return 1
    else:
        return numeroN * factorial(numeroN - 1)
def funcion_exponencial (numeroX = float, numeroN : int = 160)-> float:
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
    print(f"resultado de la aproximacion: {resultado} y el resultado real es {math.exp(numeroX)} y el rango de error es {rango_de_error(numeroX,160)}")