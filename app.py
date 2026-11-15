import streamlit as st
import pandas as pd
from scraper import extraer_libros
from datetime import datetime

# Configuración inicial de la página web
st.set_page_config(
    page_title="Monitor de Precios Web",
    page_icon="📊",
    layout="centered"
)

st.title("Extractor de Precios y Catálogos")
st.write("Bienvenido a tu panel de control de Web Scraping. Extrae datos en tiempo real y expórtalos de inmediato.")

# Sección de configuración en la barra lateral (Sidebar)
st.sidebar.header("Configuración del Extractor")
url_input = st.sidebar.text_input(
    "URL del sitio web a escanear:", 
    value="http://books.toscrape.com/"
)

# Botón principal de acción
if st.sidebar.button("🚀 Ejecutar Scraping"):
    
    with st.spinner("Conectando con la página y extrayendo datos... Por favor espera."):
        # Ejecutamos el scraper con la URL ingresada
        productos = extraer_libros(url_input)
        
    if productos:
        st.success(f"¡Éxito! Se extrajeron {len(productos)} productos correctamente.")
        
        # Convertimos los datos a un DataFrame de Pandas para mostrarlos en pantalla
        df = pd.DataFrame(productos)
        
        # Mostramos una vista previa interactiva de la tabla en la web
        st.subheader("📋 Vista previa de los datos extraídos:")
        st.dataframe(df, use_container_width=True)
        
        # Generar archivos para descarga directa
        fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_base = "catalogo_extraido"
        
        csv_data = df.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
        
        # Botón de descarga para CSV
        st.sidebar.download_button(
            label="📥 Descargar en formato CSV",
            data=csv_data,
            file_name=f"{nombre_base}_{fecha_actual}.csv",
            mime="text/csv"
        )
        
    else:
        st.error("No se pudieron extraer datos. Revisa la URL o intenta de nuevo.")