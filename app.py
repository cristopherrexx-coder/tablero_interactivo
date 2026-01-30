import pandas as pd
import plotly.express as px
import streamlit as st

vehicles_data = pd.read_csv("vehicles_us.csv")

st.header("Generar un histograma condatos vehiculares")
create_hist_button = st.button("Crear histograma")

if create_hist_button:
    #Escribir un mensaje
    st.write("'Creación de un histograma para el conjunto de datos de anuncios de venta de coches'")
    
    #Crear histograma
    fig = px.histogram(vehicles_data, x="odometer")

    #Mostrar un grafico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

create_disp_button = st.button("Crear dispercion")

if create_disp_button:
    #Escribir un mensaje
    st.write("Se crea grafico de dispersion")

    #crear grafico de dispersion
    disp_fig = px.scatter(vehicles_data, x="odometer")

    #mostrar grafico interactivo
    disp_fig.show()