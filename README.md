# 🚖 Zuber: Análisis Estratégico de Entrada al Mercado de Chicago

Este repositorio contiene una aplicación web interactiva desarrollada con **Streamlit** que analiza la dinámica del mercado de transporte compartido en Chicago. El objetivo principal es proporcionar insights basados en datos para el lanzamiento estratégico de **Zuber**.

## 📊 Descripción del Proyecto

El proyecto utiliza datos transaccionales de taxis y registros climáticos para resolver tres problemas de negocio críticos:
1.  **Benchmarking Competitivo:** Identificación de líderes de mercado y distribución de cuota de mercado.
2.  **Optimización Geográfica:** Análisis de destinos con mayor tráfico para la gestión eficiente de la flota.
3.  **Análisis de Sensibilidad Climática:** Prueba estadística de hipótesis sobre cómo el clima afecta los tiempos de traslado al aeropuerto.

## 🚀 Demo
Puedes acceder a la aplicación en vivo aquí: https://zuber-taxi-chicago.onrender.com

## 🛠️ Tecnologías Utilizadas
* **Python:** Lenguaje principal de análisis.
* **Pandas:** Manipulación y procesamiento de datos.
* **Matplotlib:** Visualizaciones estadísticas.
* **SciPy:** Ejecución de pruebas de hipótesis (T-Test de Welch).
* **Streamlit:** Framework para la creación de la interfaz web.
* **Render:** Plataforma de despliegue en la nube.

## 📂 Estructura del Repositorio
* `app.py`: Código fuente de la aplicación Streamlit.
* `notebook-zuber.ipynb`: Cuaderno Jupyter con el análisis exploratorio original.
* `requirements.txt`: Dependencias necesarias para ejecutar el proyecto.
* `data/`: Archivos CSV utilizados en el análisis (incluidos en el repo para persistencia).

## 🔧 Instalación y Ejecución Local

Si deseas ejecutar este proyecto localmente, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/zuber-chicago-analysis.git
   cd zuber-chicago-analysis
   ```

2. **Crear un entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Lanzar la aplicación:**
   ```bash
   streamlit run app.py
   ```

## 📈 Conclusiones Principales
* **Dominio de Mercado:** El mercado está altamente concentrado; se identificó a *Flash Cab* como el competidor principal.
* **Puntos Calientes:** Los barrios de *Loop, River North y Streeterville* concentran la mayor demanda operativa.
* **Factor Clima:** Se rechazó la hipótesis nula con un valor p < 0.05, confirmando que el clima adverso incrementa significativamente la duración de los viajes al Aeropuerto O'Hare, lo que justifica una estrategia de precios dinámicos.

---

### Contacto
Desarrollado por [Tu Nombre] - [Tu LinkedIn] - [Tu Portafolio]
