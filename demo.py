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

# prompt: Crear un filtro con el dataframe df de la columna region y otro con la columna state
import pandas as pd
import streamlit as st
import plotly.express as px
  
# Crea los filtros en Streamlit
region_filter = st.selectbox("Selecciona una Región", df['Region'].unique())
state_filter = st.selectbox("Selecciona un Estado", df['State'].unique())

# Filtra el DataFrame
filtered_df = df[(df['Region'] == region_filter) & (df['State'] == state_filter)]

# Muestra el DataFrame filtrado
st.write(filtered_df)

# Verificar si las columnas necesarias existen en el DataFrame
required_columns = ['Region', 'Sales', 'Category'] #Añade 'Category'
for col in required_columns:
    if col not in df.columns:
        st.error(f"Error: La columna '{col}' no existe en el DataFrame.")
        st.stop()
# Gráfico de pastel por categoría
if 'Category' in df.columns: #Verifica si la columna existe
    category_counts = filtered_df['Category'].value_counts()
    fig_pie = px.pie(values=category_counts.values, names=category_counts.index,
                     title='Distribución de Categorías')
    st.plotly_chart(fig_pie)
else:
  st.error("Error: La columna 'Category' no existe en el archivo.")
