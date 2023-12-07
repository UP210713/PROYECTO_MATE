# PROYECTO_MATE
Repositorio para el proyecto de matemáticas
Introducción. 

La enfermedad coronaria del corazón (CHD) es una de las principales causas de morbilidad y mortalidad a nivel mundial, lo que resalta la importancia de identificar y comprender sus factores de riesgo. El estudio de Framingham, un extenso proyecto de investigación cardiovascular, ha sido fundamental para descubrir y cuantificar los factores de riesgo asociados con la CHD. 
Esta investigación se centra en un conjunto diverso de variables, incluyendo demográficas, clínicas y de comportamiento, tales como la edad, el género, la presión arterial, el colesterol, la diabetes, el hábito de fumar, entre otros. Mediante la aplicación de un modelo de regresión logística, se busca determinar qué factores tienen mayor influencia en el riesgo de desarrollar CHD, proporcionando así insights valiosos que pueden ser utilizados en la prevención y manejo de esta enfermedad.
La precisión y relevancia de este análisis son cruciales, no solo para la comunidad médica, sino también para los individuos que buscan entender mejor los riesgos asociados con la enfermedad coronaria del corazón. Al proporcionar una evaluación detallada de los factores de riesgo, este estudio busca contribuir al cuerpo de conocimiento existente y apoyar las estrategias de intervención y prevención.



















Análisis Inferencial. 
Para realizar un análisis inferencial, podríamos enfocarnos en cómo ciertos factores de riesgo, como fumar, la hipertensión, el colesterol alto o la diabetes, influyen en el riesgo de desarrollar una enfermedad coronaria del corazón en diez años. Este tipo de análisis podría incluir la realización de pruebas estadísticas para determinar la significancia de estas relaciones.


Para realizar este análisis detalladamente, es necesario tomar en cuenta estos puntos, viendo la base de datos: 
Análisis exploratorio de datos (EDA): Obtener estadísticas descriptivas y visualizaciones para entender la distribución y relación entre las variables. 
Construcción del Modelo de regresión Logística: Dividirlos en conjuntos de entrenamiento y prueba. 
Evaluación del modelo: Utilizar métricas como matrices, gráficas y diagramas para evaluar el comportamiento de los datos.
Interpretación de los resultados: Analizar los coeficientes del modelo para entender la influencia de cada variable. 




Código. Histograma de edades. 
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























Código. Promedio, Mediana y estándar. 
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








Solución. 
Basándonos en los factores de riesgo que en la base de datos muestra y analizándolo mejor mediante las gráficas, creemos que estas pueden ser soluciones que pudieran generar menos enfermedades coronarias del corazón: 
Prevención y Manejo de la Hipertensión:
Programas de educación y concienciación sobre la importancia del control de la presión arterial.
Acceso a chequeos regulares de la presión arterial y tratamientos efectivos para aquellos diagnosticados con hipertensión.
Control del Tabaco:
Campañas para desalentar el inicio del hábito de fumar y promover la cesación del tabaco.
Proporcionar recursos y apoyo para la cesación del tabaquismo, como terapias de reemplazo de nicotina y programas de apoyo.
Gestión de la Diabetes:
Fomentar la detección temprana de la diabetes a través de pruebas regulares de glucosa en sangre.
Educación sobre la gestión de la diabetes, incluyendo dieta, ejercicio y adherencia a la medicación.
Promoción de Estilos de Vida Saludables:
Incentivar la actividad física regular y una dieta saludable para mantener un peso corporal adecuado y reducir el riesgo de CHD.
Programas comunitarios o en el lugar de trabajo para fomentar hábitos saludables.
Educación sobre Riesgos de CHD:
Informar al público sobre los factores de riesgo de CHD y cómo la modificación de estos factores puede reducir su riesgo.
Integrar la educación sobre salud del corazón en los programas escolares y comunitarios.

Link del código del programa de análisis. 







Conclusión. 

Tras realizar un análisis de los datos del estudio de Framingham utilizando la regresión logística, hemos obtenido datos significativos sobre los factores de riesgo asociados con la enfermedad coronaria del corazón (CHD) en un período de diez años. Nuestro modelo destacó la importancia de factores como la edad, la presión arterial sistólica, la diabetes y la prevalencia de accidentes cerebrovasculares e hipertensión.

Aunque el modelo mostró una buena predicción en los casos sin CHD, su capacidad para identificar correctamente casos con CHD fue muy corta. Esto quiere decir que, aunque el modelo es útil para descartar la enfermedad en individuos con bajo riesgo, no es tan eficiente para detectar todos los casos de alto riesgo.

Además, las visualizaciones generadas, como histogramas y gráficos de barras, proporcionaron una comprensión más profunda de la distribución de los datos y la importancia de las variables en el modelo. Estos hallazgos pueden ser útiles para la toma de decisiones en el ámbito de la salud pública y en el desarrollo de estrategias preventivas.

En conclusión, este proyecto nos ha permitido aplicar técnicas de análisis de datos y modelado estadístico para abordar un problema de salud real. A través de este proceso, hemos aprendido sobre la importancia de la interpretación de los resultados y un análisis más profundo para mejorar la precisión y la utilidad de los modelos predictivos en el entorno de la salud.
