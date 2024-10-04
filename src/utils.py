import random as rd
import numpy as np

def get_3_random_points_indexes(range):
    i1 = rd.randint(0, range)
    i2 = i3 = 0
    while i1 == i2:
        i2 = rd.randint(0, range)
    while i1 == i3 or i2 == i3:
        i3 = rd.randint(0, range)
    return i1, i2, i3

def distancia_punto_a_plano(A, B, C, D, punto):
    x0, y0, z0 = punto
    # Numerador: valor absoluto de Ax0 + By0 + Cz0 + D
    numerador = abs(A * x0 + B * y0 + C * z0 + D)
    
    # Denominador: raíz cuadrada de A^2 + B^2 + C^2
    denominador = np.sqrt(A**2 + B**2 + C**2)
    
    # Distancia
    distancia = numerador / denominador
    
    return distancia