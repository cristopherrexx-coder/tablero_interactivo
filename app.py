import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el dataset
df = pd.read_csv("vehicles_us.csv")

# Encabezado de la aplicación
st.header("Análisis Exploratorio de Datos de Vehículos")

# Botón para construir un histograma
if st.button("Crear Histograma"):
    st.write("Histograma de la columna 'clock_speed'")
    if 'clock_speed' in df.columns:
        fig = px.histogram(df, x='clock_speed', title='Histograma de Velocidad del Reloj')
    else:
        fig = px.histogram(df, x=df.columns[0], title=f'Histograma de {df.columns[0]}')
    st.plotly_chart(fig, use_container_width=True)