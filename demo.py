# prompt: Imprimir dataframe usando streamlit

import streamlit as st
import pandas as pd

# Lee el archivo Excel
try:
  df = pd.read_excel('Salida Final Ventas.xlsx')
  # Muestra las primeras filas del DataFrame en Streamlit
  st.write(df)
except FileNotFoundError:
  st.error("Error: El archivo 'Salida Final Ventas.xlsx' no se encontró en el directorio actual.")
except Exception as e:
  st.error(f"Ocurrió un error al leer el archivo: {e}")

# prompt: Arma una grafica de las ventas por region del dataframe df usando streamlit

import pandas as pd
import streamlit as st
import plotly.express as px

# Lee el archivo Excel
try:
  df = pd.read_excel('Salida Final Ventas.xlsx')
  #print(df.head()) # Muestra las primeras filas del DataFrame
except FileNotFoundError:
  st.error("Error: El archivo 'Salida Final Ventas.xlsx' no se encontró en el directorio actual.")
  st.stop() # Detenemos la ejecución si no se encuentra el archivo
except Exception as e:
  st.error(f"Ocurrió un error al leer el archivo: {e}")
  st.stop()


# Verificar si la columna 'Region' existe en el DataFrame
if 'Region' not in df.columns:
    st.error("Error: La columna 'Region' no existe en el DataFrame.")
    st.stop()

if 'Sales' not in df.columns:
    st.error("Error: La columna 'Ventas' no existe en el DataFrame.")
    st.stop()


# Agrupa las ventas por región
ventas_por_region = df.groupby('Region')['Sales'].sum().reset_index()


# Crea el gráfico de barras con Plotly Express
fig = px.bar(ventas_por_region, x='Region', y='Sales', 
             labels={'Region': 'Región', 'Sales': 'Ventas Totales'},
             title='Ventas por Región')

# Muestra el gráfico en Streamlit
st.plotly_chart(fig)

import streamlit as st
import pandas as pd

# Supongamos que tienes un dataframe llamado df
# df = pd.read_csv('ruta_a_tu_archivo.csv')

# Crear algunas datos de ejemplo
data = {
    'region': ['Norte', 'Sur', 'Este', 'Oeste', 'Norte', 'Sur'],
    'valor': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

# Crear un filtro de selección basado en la columna 'region'
regiones = df['region'].unique()
region_seleccionada = st.sidebar.selectbox('Selecciona una región:', regiones)

# Filtrar el dataframe basado en la región seleccionada
df_filtrado = df[df['region'] == region_seleccionada]

# Mostrar el dataframe filtrado
st.write('Dataframe filtrado por región:', region_seleccionada)
st.dataframe(df_filtrado)
