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
    print(f"el resultado de la funcion arctan aproximada es {funcion_arctan(numeroX,)}, y el real es {math.atan(numeroX)} y el rango de error es aprox: {rango_de_error(numeroX, 200)}")