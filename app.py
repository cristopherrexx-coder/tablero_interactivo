import pandas as pd
import plotly.express as px
import streamlit as st

vehicles_data = pd.read_csv("vehicles_us.csv")


# Encabezado de la aplicación
st.header("Análisis Exploratorio de Datos de Vehículos")

# Botón para construir un histograma
if st.button("Construir Histograma"):
    st.write("Histograma de la columna 'clock_speed'")
    if 'clock_speed' in vehicles_data.columns:
        fig = px.histogram(vehicles_data, x='clock_speed', title='Histograma de Velocidad del Reloj')
    else:
        fig = px.histogram(vehicles_data, x=vehicles_data.columns[0], title=f'Histograma de {vehicles_data.columns[0]}')
    fig.show()
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir un gráfico de dispersión
if st.button("Construir Scatter Plot"):
    st.write("Creando Dispersion")
    fig = px.scatter(vehicles_data, x="odometer", y="price") # crear un gráfico de dispersión
    fig.show() # crear gráfico de dispersión