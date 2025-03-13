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

# prompt: Usando streamlit, crear un filtro usando la columna region del dataframe df

import pandas as pd
import streamlit as st
import plotly.express as px

# Lee el archivo Excel
try:
    df = pd.read_excel('Salida Final Ventas.xlsx')
except FileNotFoundError:
    st.error("Error: El archivo 'Salida Final Ventas.xlsx' no se encontró en el directorio actual.")
    st.stop()
except Exception as e:
    st.error(f"Ocurrió un error al leer el archivo: {e}")
    st.stop()

# Verificar si la columna 'Region' existe en el DataFrame
if 'Region' not in df.columns:
    st.error("Error: La columna 'Region' no existe en el DataFrame.")
    st.stop()

if 'Sales' not in df.columns:
    st.error("Error: La columna 'Sales' no existe en el DataFrame.")
    st.stop()

# Obtener las regiones únicas del DataFrame
regiones_unicas = df['Region'].unique()

# Crear un multiselect para filtrar por región
regiones_seleccionadas = st.multiselect("Selecciona las regiones", regiones_unicas, default=regiones_unicas)

# Filtrar el DataFrame según las regiones seleccionadas
df_filtrado = df[df['Region'].isin(regiones_seleccionadas)]

# Mostrar el DataFrame filtrado
st.write(df_filtrado)

# Agrupa las ventas por región del DataFrame filtrado
ventas_por_region = df_filtrado.groupby('Region')['Sales'].sum().reset_index()

# Crea el gráfico de barras con Plotly Express
fig = px.bar(ventas_por_region, x='Region', y='Sales',
             labels={'Region': 'Región', 'Sales': 'Ventas Totales'},
             title='Ventas por Región')

# Muestra el gráfico en Streamlit
st.plotly_chart(fig)
