import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# --- Configuration & Styling ---
st.set_page_config(page_title="Zuber Chicago Launch Strategy", layout="wide")

st.title("🚖 Zuber: Estrategia de Lanzamiento en Chicago")
st.markdown("""
Esta aplicación presenta un análisis detallado del mercado de taxis en Chicago para apoyar el lanzamiento de **Zuber**.
Incluye un análisis de la competencia, segmentación geográfica e impacto del clima en la operación.
""")

# --- Sidebar for Data Loading ---
st.sidebar.header("Configuración de Datos")
uploaded_company = st.sidebar.file_uploader("Subir project_sql_result_01.csv (Compañías)", type="csv")
uploaded_neighborhood = st.sidebar.file_uploader("Subir project_sql_result_04.csv (Barrios)", type="csv")
uploaded_trips = st.sidebar.file_uploader("Subir project_sql_result_07.csv (Prueba Hipótesis)", type="csv")

# Function to load data with caching
@st.cache_data
def load_data(file, default_name):
    if file is not None:
        return pd.read_csv(file)
    try:
        return pd.read_csv(default_name)
    except FileNotFoundError:
        return None

company_trips = load_data(uploaded_company, 'project_sql_result_01.csv')
neighborhood_avg_trips = load_data(uploaded_neighborhood, 'project_sql_result_04.csv')
df_trips = load_data(uploaded_trips, 'project_sql_result_07.csv')

# --- Main Dashboard ---
if company_trips is not None and neighborhood_avg_trips is not None:
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Análisis de la Competencia")
        n_companies = st.slider("Número de empresas a mostrar", 5, 20, 10)
        top_companies = company_trips.sort_values(by='trips_amount', ascending=False).head(n_companies)
        
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        ax1.bar(top_companies['company_name'], top_companies['trips_amount'], color='skyblue')
        ax1.set_ylabel('Cantidad de Viajes')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig1)
        
        with st.expander("Ver datos de compañías"):
            st.dataframe(top_companies)

    with col2:
        st.subheader("📍 Segmentación Geográfica")
        n_neighborhoods = st.slider("Número de barrios a mostrar", 5, 20, 10)
        top_neighborhoods = neighborhood_avg_trips.sort_values(by='average_trips', ascending=False).head(n_neighborhoods)
        
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        ax2.bar(top_neighborhoods['dropoff_location_name'], top_neighborhoods['average_trips'], color='salmon')
        ax2.set_ylabel('Promedio de Viajes')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig2)

        with st.expander("Ver datos de barrios"):
            st.dataframe(top_neighborhoods)

    # --- Hypothesis Testing ---
    st.divider()
    st.header("⛈️ Prueba de Hipótesis: Impacto del Clima")
    
    if df_trips is not None:
        st.write("¿Afecta el clima la duración de los viajes desde el Loop hasta O'Hare?")
        
        good_weather = df_trips[df_trips['weather_conditions'] == 'Good']['duration_seconds']
        bad_weather = df_trips[df_trips['weather_conditions'] == 'Bad']['duration_seconds']
        
        results = stats.ttest_ind(good_weather, bad_weather, equal_var=False)
        alpha = 0.05
        
        c1, c2, c3 = st.columns(3)
        c1.metric("P-Value", f"{results.pvalue:.4f}")
        c2.metric("Promedio Buen Clima", f"{good_weather.mean():.1f}s")
        c3.metric("Promedio Mal Clima", f"{bad_weather.mean():.1f}s")
        
        if results.pvalue < alpha:
            st.error("Resultado: Se rechaza la hipótesis nula. El clima afecta significativamente la duración.")
        else:
            st.success("Resultado: No hay evidencia suficiente para rechazar la hipótesis nula.")
            
        st.info("**Conclusión estratégica:** Zuber debe ajustar sus algoritmos de ETA y precios dinámicos durante días lluviosos.")
    else:
        st.warning("Carga 'project_sql_result_07.csv' para ver el análisis estadístico.")

else:
    st.info("Por favor, asegúrate de que los archivos CSV estén en la carpeta del proyecto o súbelos usando la barra lateral.")