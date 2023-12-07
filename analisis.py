import matplotlib.pyplot as plt

# Datos de las edades
edades = [
    39, 46, 48, 61, 46, 43, 63, 45, 52, 43, 50, 43, 46, 41, 39, 38, 48, 46, 38, 41,
    42, 43, 52, 52, 44, 47, 60, 35, 61, 60, 36, 43, 59, 61, 54, 37, 56, 52, 42, 36, 43, 41,
    52, 54, 53, 49, 65, 46, 63
]

# Crear el histograma
plt.figure(figsize=(8, 6))
plt.hist(edades, bins=10, color='skyblue', edgecolor='black')
plt.title('Histograma de Edades')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.5)
plt.show()