import random

def throwThreeCoins():
    moneda1 = random.randint(2, 3)
    moneda2 = random.randint(2, 3)
    moneda3 = random.randint(2, 3)
    resultados = [moneda1, moneda2, moneda3]
    return resultados

def sumarResultados (resultados):
    suma = 0
    for resultado in resultados:
        suma += resultado
    return suma

def clasificarTirada(suma):
    if suma == 6:
        return "continua"
    if suma == 7:
        return "continua"
    if suma == 8:
        return "partida"
    if suma == 9:
        return "partida"