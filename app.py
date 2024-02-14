import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

st.header('Anúncios de Veículos') 
     
car_data = pd.read_csv("C:\\Users\\drclo\\OneDrive\\Documentos\\Bootcamp\\projeto_web\\vehicles.csv") # lendo os dados
hist_button = st.button('Criar histograma') # criar um botão
     
if hist_button: # se o botão for clicado 
         # escrever uma mensagem
         st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
         
         # criar um histograma para odometer
         fig = px.histogram(car_data, x="odometer")
     
         # exibir um gráfico Plotly interativo
         st.plotly_chart(fig, use_container_width=True)
     
def gerar_grafico_dispersao(car_data, x_axis):
  fig = px.scatter(car_data, x=x_axis, y="price")
  fig.update_layout(title="Gráfico de Dispersão")
  st.plotly_chart(fig)

build_histogram = st.checkbox("Criar Histograma")
build_scatter_plot = st.checkbox("Criar Gráfico de Dispersão")

if build_histogram:
  st.write("Criando um histograma para a coluna odometer")
  fig = px.histogram(car_data, x="odometer")
  fig.update_layout(title="Histograma")
  st.plotly_chart(fig)

if build_scatter_plot:
  st.write("Criando um gráfico de dispersão para a coluna odometer")
  gerar_grafico_dispersao(car_data, "odometer")

  