# 📊 Taller #1 – Estadística 3 (Ingeniería de Sistemas)

Este repositorio contiene una aplicación web interactiva desarrollada con **Streamlit** para el análisis estadístico de datos de estudiantes, enfocándose en la distribución geográfica y de salud (EPS).

---

## 🚀 Aplicación en Vivo

Puedes acceder a la versión desplegada de la herramienta a través del siguiente enlace:

👉 **[https://mitaller1estadistica3.streamlit.app/](https://mitaller1estadistica3.streamlit.app/)**

---

## 📝 Descripción del Proyecto

La aplicación procesa un conjunto de datos (`04 - estudiantes.csv`) y genera visualizaciones avanzadas para identificar patrones de concentración y dispersión. Las principales funcionalidades son:

### 1. Análisis de Pareto (80/20)
Genera diagramas de Pareto para las variables **Municipio de Residencia** y **EPS**. 
* **Barras:** Representan la frecuencia absoluta.
* **Línea Roja:** Representa la frecuencia relativa acumulada, permitiendo identificar qué municipios o entidades concentran la mayor cantidad de estudiantes.

### 2. Tabla Cruzada (Crosstab)
Una matriz de doble entrada que cruza los **Municipios** con las **EPS**. Es la base analítica para entender cuántos estudiantes de una zona específica pertenecen a cada entidad de salud.

### 3. Gráfica de Radar Multivariable
Una visualización tipo "telaraña" (Spider Chart) que permite comparar la cobertura de las EPS:
* Cada eje es un municipio.
* Cada polígono de color es una EPS.
* La escala es absoluta (0 a 113), permitiendo una comparación real y sin distorsiones entre las diferentes categorías.

---

## 🛠️ Tecnologías y Librerías

El proyecto está construido íntegramente en Python utilizando:

* **Streamlit:** Para la interfaz de usuario y el despliegue web.
* **Pandas:** Para la manipulación de DataFrames y creación de tablas de frecuencia.
* **Matplotlib:** Para el diseño personalizado de los gráficos (Pareto y Radar).
* **NumPy:** Para el cálculo de ángulos y geometría radial en los gráficos.

---

## 📁 Estructura del Repositorio

* `taller1.py`: Código fuente principal de la aplicación.
* `04 - estudiantes.csv`: Dataset con la información de los estudiantes.
* `requirements.txt`: Lista de dependencias para el despliegue.

---
**Desarrollado para la materia de Estadística 3** *Universidad Católica de Oriente (UCO)*