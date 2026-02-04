import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

st.set_page_config(page_title="Asistente de Presupuestos Telecom", layout="wide")

st.title("calc_telecom: Generador de Presupuestos")
st.write("Basado en precios de [TodoTelecom.com](https://www.todotelecom.com)")

# Entrada de usuario
descripcion = st.text_area("Describe el trabajo a realizar:", 
                          placeholder="Ej: Instalación de antena satelital con 3 tomas...")

def buscar_precio(producto):
    # Nota: En un servidor real, Selenium requiere configuración adicional.
    # Aquí simulamos la conexión para que veas la estructura.
    url = f"https://www.todotelecom.combuscar?search_query={producto}"
    return url # Retorna el link para que el usuario verifique

if st.button("Generar Estudio y Presupuesto"):
    if descripcion:
        with st.spinner('Analizando catálogo de TodoTelecom...'):
            # Lógica de análisis de materiales
            materiales = []
            if "antena" in descripcion.lower():
                materiales.append({"Producto": "Antena Televes", "Precio Est.": "45.00€"})
            if "cable" in descripcion.lower():
                materiales.append({"Producto": "Bobina Cable Coaxial", "Precio Est.": "25.50€"})
            
            # Mostrar Resultados
            st.subheader("📋 Presupuesto Estimado")
            df = pd.DataFrame(materiales)
            st.table(df)
            
            st.subheader("🛠️ Estudio Técnico")
            col1, col2 = st.columns(2)
            with col1:
                st.success("**Puntos a Favor**\n- Materiales de alta gama.\n- Garantía oficial.")
            with col2:
                st.error("**Puntos en Contra**\n- Requiere orientación precisa.\n- Sensible a interferencias.")
    else:
        st.warning("Por favor, describe el trabajo primero.")
