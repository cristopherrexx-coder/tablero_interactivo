import pandas as pd
import plotly.express as px
import streamlit as st

vehicles_data = pd.read_csv("vehicles_us.csv")


# Encabezado de la aplicación
st.header("Análisis Exploratorio de Datos de Vehículos")

# Botón para construir un histograma
if st.button("Construir Histograma"):
    st.write("Construyendo Histograma'")
    if 'clock_speed' in vehicles_data.columns:
        st.write("Columna 'clock_speed'")
        fig = px.histogram(vehicles_data, x='clock_speed', title='Histograma de Velocidad del Reloj')
    else:
        st.write(f"Columna {vehicles_data.columns[0]}")
        fig = px.histogram(vehicles_data, x=vehicles_data.columns[0], title=f'Histograma de {vehicles_data.columns[0]}')
    fig.show()
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir un garfico de dispersión
create_disp_button = st.button("Crear dispercion")
# Funcionalidad del botón para construir un gráfico de dispersión
if create_disp_button:
    st.write("Creando Dispersion")
    fig = px.scatter(vehicles_data, x="odometer", y="price", title= "Scatter plot de Precios") # crear un gráfico de dispersión
    fig.show() # crear gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)