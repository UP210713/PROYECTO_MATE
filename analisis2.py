import numpy as np

# Datos de las edades
edades = [
    39, 46, 48, 61, 46, 43, 63, 45, 52, 43, 50, 43, 46, 41, 39, 38, 48, 46, 38, 41,
    42, 43, 52, 52, 44, 47, 60, 35, 61, 60, 36, 43, 59, 61, 54, 37, 56, 52, 42, 36, 43, 41,
    52, 54, 53, 49, 65, 46, 63
]

# Cálculo del promedio
promedio = np.mean(edades)

# Cálculo de la mediana
mediana = np.median(edades)

# Cálculo de la desviación estándar
desviacion_estandar = np.std(edades)

# Mostrar los resultados
print(f"Promedio: {promedio}")
print(f"Mediana: {mediana}")
print(f"Desviación Estándar: {desviacion_estandar}")