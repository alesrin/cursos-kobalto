"""
Broadcasting con NumPy
Módulo: NUMPY-BROADCASTING
Fecha: 2026-02-05 18:40

Enunciado:
Operaciones entre arrays de diferente forma

"""
# Broadcasting con NumPy
# Operaciones entre arrays de diferente forma
# Generado: 5/2/2026

# === SETUP ===
import numpy as np

# === DATASET ===
import numpy as np

# Configurar semilla para reproducibilidad
np.random.seed(42)

# PRODUCTOS Y MESES - TechStore Dataset
productos = ['Portatil', 'Tablet', 'Smartphone', 'Auriculares']
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']

# MATRIZ DE UNIDADES VENDIDAS (4 productos x 12 meses)
unidades = np.array([
    np.random.randint(20, 50, 12),    # Portatil
    np.random.randint(30, 80, 12),    # Tablet
    np.random.randint(50, 120, 12),   # Smartphone
    np.random.randint(80, 200, 12)    # Auriculares
])

# PRECIOS UNITARIOS por producto
precios = np.array([899.99, 449.99, 699.99, 79.99])

# COSTES UNITARIOS por producto
costes = np.array([650, 280, 450, 35])

# DESCUENTOS MENSUALES
descuentos = np.array([0.0, 0.0, 0.05, 0.0, 0.0, 0.10, 0.15, 0.0, 0.0, 0.0, 0.20, 0.10])

print("Dataset TechStore cargado correctamente")
print(f"  unidades.shape: {unidades.shape}")
print(f"  precios.shape: {precios.shape}")
print(f"  costes.shape: {costes.shape}")
print(f"  descuentos.shape: {descuentos.shape}")


############################################################
# EJERCICIO 1: EXPLORA EL DATASET
############################################################
# Objetivo: Familiarizarte con los datos antes de operar

# EJERCICIO 0: Explora el Dataset
# Primero pulsa "Cargar Dataset"

# 1. Forma de cada array
print("=== DIMENSIONES ===")


# 2. Rango de unidades vendidas


# 3. Ventas del Portatil (primera fila)


# 4. Producto más caro y más barato


# 5. Meses con descuento



############################################################
# EJERCICIO 1: CALCULO DE INGRESOS
############################################################
# Objetivo: Aplicar broadcasting con vectores columna

# EJERCICIO 1: Calculo de ingresos
# Dataset ya disponible: unidades, precios, productos, meses

# 1. Convertir precios a vector columna


# 2. Calcular matriz de ingresos con broadcasting


# 3. Verificar formas


# 4. Ingreso total por producto (suma por filas)


# 5. Ingreso total por mes (suma por columnas)


# 6. Mes y producto con más ingresos



############################################################
# EJERCICIO 2: APLICACION DE DESCUENTOS
############################################################
# Objetivo: Broadcasting con vectores fila

# EJERCICIO 2: Aplicacion de descuentos
# Usa precios_col e ingresos del ejercicio anterior

# 1. Precios con descuento para cada mes
# Pista: factor_descuento = 1 - descuentos


# 2. Ingresos con descuento aplicado


# 3. Perdida por descuentos (diferencia)


# 4. Mes con mayor perdida


# 5. Porcentaje perdido en descuentos



############################################################
# EJERCICIO 3: ANALISIS DE BENEFICIOS
############################################################
# Objetivo: Combinar múltiples operaciones de broadcasting

# EJERCICIO 3: Analisis de beneficios
# Usa las variables de ejercicios anteriores

# 1. Margen unitario por producto (sin descuento)


# 2. Margen con descuento para cada mes
# Pista: necesitas costes_col


# 3. Beneficio total por producto/mes


# 4. Hay margenes negativos? Donde?
# Pista: usa np.where()


# 5. Beneficio anual por producto


# 6. EXTRA: Normalizacion con broadcasting
# Pista: usa keepdims=True