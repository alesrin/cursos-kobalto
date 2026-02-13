"""
Playground — Operaciones vectorizadas
Módulo: NUMPY
Fecha: 2026-02-13 16:38

Enunciado:
Código escrito en el playground durante el estudio de la teoría

"""
import numpy as np
matriz = np.arange(1, 13).reshape(3, 4)
vector = np.array([10, 20, 30, 40])

print(matriz.shape)  # (3, 4)
print(vector.shape)  # (4,)

resultado = matriz + vector
print(resultado.shape)  # (3, 4)

# El vector se "repite" para cada fila
# Sin crear copias en memoria!