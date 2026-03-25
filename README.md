# 📊 Taller #1 – Estadística 3 (Ingeniería de Sistemas)

Este repositorio contiene una aplicación web interactiva desarrollada con **Streamlit** para el análisis estadístico completo de datos de estudiantes. El taller está dividido en **dos partes**: análisis de variables cualitativas (distribución geográfica y de salud) y análisis de variables cuantitativas (notas académicas).

---

## 🚀 Aplicación en Vivo

Puedes acceder a la versión desplegada de la herramienta a través del siguiente enlace:

👉 **[https://mitaller1estadistica3.streamlit.app/](https://mitaller1estadistica3.streamlit.app/)**

---

## 📝 Descripción del Proyecto

La aplicación integra dos conjuntos de datos (`04 - estudiantes.csv` y `05 - notas1.csv`) y genera visualizaciones avanzadas para identificar patrones de concentración, dispersión y comportamiento estadístico en ambas fuentes.

---

## 📂 Parte 1 — Variables Cualitativas

Procesa el dataset `04 - estudiantes.csv` y analiza la distribución geográfica y de cobertura de salud de los estudiantes.

### 1. Análisis de Pareto (80/20)
Genera diagramas de Pareto para las variables **Municipio de Residencia** y **EPS**.
* **Barras:** Representan la frecuencia absoluta de cada categoría, ordenadas de mayor a menor.
* **Línea Roja:** Representa la frecuencia relativa acumulada, permitiendo identificar qué municipios o entidades concentran la mayor cantidad de estudiantes (principio 80/20).

### 2. Tabla Cruzada (Crosstab)
Una matriz de doble entrada construida con `pd.crosstab()` que cruza los **Municipios** con las **EPS**. Cada celda indica cuántos estudiantes de una zona específica pertenecen a cada entidad de salud. Es la base analítica para la gráfica radar.

### 3. Gráfica de Radar Multivariable
Una visualización tipo "telaraña" (Spider Chart) que compara la cobertura de las EPS en cada municipio:
* Cada **eje** es un municipio de residencia.
* Cada **polígono de color** representa una EPS distinta.
* La **escala es absoluta** (0 al máximo real de la tabla), permitiendo comparaciones directas sin distorsión por normalización.

---

## 📈 Parte 2 — Variables Cuantitativas

Procesa el dataset `05 - notas1.csv` y realiza un análisis estadístico detallado de 5 variables numéricas:

> **Variables analizadas:** Lógica y Programación · Estructuras de Datos · Machine Learning · Cálculo Diferencial · Arquitectura de Computadores

### 4. Tabla de Frecuencia por Intervalos
Construida con `pd.cut(data[variable], bins=6)`, divide el rango de notas en **6 intervalos de igual amplitud** y calcula:
* Frecuencia absoluta, relativa (%), acumulada y relativa acumulada (%).

### 5. Análisis de Cuartiles — Método de Tukey
Para cada variable se calculan los cuartiles y el rango intercuartílico (IQR) para detectar valores atípicos:

```python
Q1  = serie.quantile(0.25)
Q3  = serie.quantile(0.75)
fs  = Q3 - Q1                  # IQR
lim_inf = Q1 - 1.5 * fs        # Límite inferior de Tukey
lim_sup = Q3 + 1.5 * fs        # Límite superior de Tukey
```

Todo valor por debajo de `lim_inf` o por encima de `lim_sup` es clasificado como **valor atípico** y se reporta con alerta visual.

### 6. Análisis de Forma de la Distribución
* **Asimetría (skewness):** determina si la distribución tiene sesgo positivo, negativo o es simétrica.
* **Curtosis (Fisher):** clasifica la distribución como leptocúrtica (pico pronunciado), platicúrtica (aplanada) o mesocúrtica (normal).

### 7. Visualizaciones por Variable
Tres gráficas simultáneas para cada materia:
* **Boxplot:** muestra los cuartiles, bigotes y valores atípicos (marcados en rojo).
* **Dispersión:** visualiza cada estudiante como un punto; los atípicos aparecen como ✕ rojo.
* **Histograma con curva KDE:** frecuencia por intervalo con curva de densidad suavizada, media y mediana superpuestas.

### 8. Resumen Comparativo Final
Una tabla unificada con las métricas clave de las 5 variables (media, mediana, IQR, atípicos, asimetría, curtosis) acompañada de un **boxplot comparativo** con la línea de nota mínima aprobatoria (3.0).

---

## 🛠️ Tecnologías y Librerías

El proyecto está construido íntegramente en Python utilizando:

| Librería | Uso |
|---|---|
| **Streamlit** | Interfaz de usuario y despliegue web interactivo. |
| **Pandas** | Manipulación de DataFrames, tablas de frecuencia (`pd.cut`, `pd.crosstab`) y cálculo de cuartiles. |
| **Matplotlib** | Diseño personalizado de todos los gráficos (Pareto, Radar, Boxplot, Dispersión, Histograma). |
| **NumPy** | Cálculo de ángulos para la gráfica radar y arrays auxiliares para la dispersión. |
| **SciPy** | Cálculo exacto de asimetría (`stats.skew`), curtosis (`stats.kurtosis`) y curva KDE (`gaussian_kde`). |

---

## 📁 Estructura del Repositorio

```
📦 taller1-estadistica3/
├── taller1_completo.py       # Código fuente unificado (Parte 1 + Parte 2)
├── 04 - estudiantes.csv      # Dataset cualitativo: municipios y EPS
├── 05 - notas1.csv           # Dataset cuantitativo: notas académicas
└── requirements.txt          # Dependencias para el despliegue
```

### `requirements.txt`
```
streamlit
pandas
matplotlib
numpy
scipy
```

---

## 👤 Información Académica

| Campo | Detalle |
|---|---|
| **Estudiante** | Andres Felipe Velez Alcaraz |
| **Materia** | Estadística 3 |
| **Profesor** | Daniel Betancur Trujillo |
| **Carrera** | Ingeniería de Sistemas |
| **Universidad** | Universidad Católica de Oriente (UCO) |