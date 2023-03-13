#ARREGLO de colina
#Julia Esther de la Torre Herrera

import random

def generar_solucion_inicial(ciudades):
    """Genera una solución inicial aleatoria"""
    return random.sample(ciudades, len(ciudades))

def evaluar(solucion, distancias):
    """Evalúa la solución"""
    distancia_total = 0
    for i in range(len(solucion)-1):
        ciudad_actual = solucion[i]
        ciudad_siguiente = solucion[i+1]
        distancia_total += distancias[ciudad_actual][ciudad_siguiente]
    return distancia_total

def vecino(solucion):
    """Genera un vecino aleatorio"""
    vecino = solucion[:]
    idx1 = random.randint(0, len(vecino)-1)
    idx2 = random.randint(0, len(vecino)-1)
    vecino[idx1], vecino[idx2] = vecino[idx2], vecino[idx1]
    return vecino

def colinas(ciudades, distancias):
    """Algoritmo de colinas"""
    solucion_actual = generar_solucion_inicial(ciudades)
    evaluacion_actual = evaluar(solucion_actual, distancias)
    while True:
        vecino_actual = vecino(solucion_actual)
        evaluacion_vecino_actual = evaluar(vecino_actual, distancias)
        if evaluacion_vecino_actual < evaluacion_actual:
            solucion_actual = vecino_actual
            evaluacion_actual = evaluacion_vecino_actual
        else:
            break
    return solucion_actual

# Pedimos al usuario que introduzca las ciudades y las distancias entre ellas
ciudades = input("Introduce las ciudades separadas por coma: ").split(",")
distancias = {}
for ciudad in ciudades:
    distancias[ciudad] = {}
    for otra_ciudad in ciudades:
        if otra_ciudad == ciudad:
            distancias[ciudad][otra_ciudad] = 0
        else:
            distancias[ciudad][otra_ciudad] = float(input(f"Introduce la distancia entre {ciudad} y {otra_ciudad}: "))

# Ejecutamos el algoritmo de colinas
ruta_optima = colinas(ciudades, distancias)

# Mostramos la ruta óptima
print("La ruta óptima es:", ruta_optima)
print("La distancia total es:", evaluar(ruta_optima, distancias))

