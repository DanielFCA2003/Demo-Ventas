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

# Verificar si la columna 'Order Date' existe en el DataFrame
if 'Order Date' not in df.columns:
    st.error("Error: La columna 'Order Date' no existe en el DataFrame.")
    st.stop()

# Convertir la columna 'Order Date' a tipo datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# Verificar si hay valores nulos después de la conversión
if df['Order Date'].isnull().any():
    st.error("Error: Algunos valores en la columna 'Order Date' no se pudieron convertir a fechas.")
    st.stop()

# Extraer el año de la columna 'Order Date'
df['Year'] = df['Order Date'].dt.year

# Verificar si la columna 'Category' existe en el DataFrame
if 'Category' not in df.columns:
    st.error("Error: La columna 'Category' no existe en el DataFrame.")
    st.stop()

# Verificar si la columna 'Sub-Category' existe en el DataFrame
if 'Sub-Category' not in df.columns:
    st.error("Error: La columna 'Sub-Category' no existe en el DataFrame.")
    st.stop()

# Calcular el acumulado de ventas por año, categoría y subcategoría
ventas_acumuladas_por_anio_categoria_subcategoria = df.groupby(['Year', 'Category', 'Sub-Category'])['Sales'].sum().reset_index()

# Crear la gráfica de barras con Plotly Express
fig_bar_category_subcategory = px.bar(ventas_acumuladas_por_anio_categoria_subcategoria, 
                                      x='Year', y='Sales', color='Sub-Category', barmode='group',
                                      facet_col='Category',  # Divide las barras por categoría
                                      labels={'Year': 'Año', 'Sales': 'Ventas Acumuladas', 'Sub-Category': 'Subcategoría', 'Category': 'Categoría'},
                                      title='Ventas Acumuladas por Año, Categoría y Subcategoría')

# Mostrar la gráfica en Streamlit
st.plotly_chart(fig_bar_category_subcategory)

# Crear la gráfica de barras apiladas con Plotly Express
fig_bar_stacked = px.bar(ventas_acumuladas_por_anio_categoria_subcategoria, 
                         x='Year', y='Sales', color='Sub-Category', barmode='stack',
                         labels={'Year': 'Año', 'Sales': 'Ventas Acumuladas', 'Sub-Category': 'Subcategoría', 'Category': 'Categoría'},
                         title='Ventas Acumuladas por Año, Categoría y Subcategoría (Apiladas)',
                         facet_row='Category')  # Divide las categorías en filas

# Mostrar la gráfica en Streamlit
st.plotly_chart(fig_bar_stacked)

# Crear la gráfica de barras apiladas con Plotly Express
fig_bar_stacked_category = px.bar(ventas_acumuladas_por_anio_categoria_subcategoria, 
                                  x='Year', y='Sales', color='Sub-Category', barmode='stack',
                                  labels={'Year': 'Año', 'Sales': 'Ventas Acumuladas', 'Sub-Category': 'Subcategoría', 'Category': 'Categoría'},
                                  title='Ventas Acumuladas por Año, Categoría y Subcategoría (Apiladas por Categoría)',
                                  facet_col='Category')  # Divide las categorías en columnas

# Mostrar la gráfica en Streamlit
st.plotly_chart(fig_bar_stacked_category)

# Calcular el acumulado de ventas por año y categoría
ventas_acumuladas_por_anio_categoria = df.groupby(['Year', 'Category'])['Sales'].sum().reset_index()

# Crear la gráfica de línea con Plotly Express
fig_line_category = px.line(ventas_acumuladas_por_anio_categoria, 
                            x='Year', y='Sales', color='Category',
                            labels={'Year': 'Año', 'Sales': 'Ventas Acumuladas', 'Category': 'Categoría'},
                            title='Ventas Acumuladas por Año y Categoría')

# Mostrar la gráfica en Streamlit
st.plotly_chart(fig_line_category)

# Crear la gráfica de barras con Plotly Express
fig_bar_category = px.bar(ventas_acumuladas_por_anio_categoria, 
                          x='Year', y='Sales', color='Category',
                          labels={'Year': 'Año', 'Sales': 'Ventas Acumuladas', 'Category': 'Categoría'},
                          title='Ventas Acumuladas por Año y Categoría (Barras)')

# Mostrar la gráfica en Streamlit
st.plotly_chart(fig_bar_category)

# Calcular el acumulado de ventas por año
ventas_acumuladas_por_anio = df.groupby('Year')['Sales'].sum().reset_index()

# Crear la gráfica de línea con Plotly Express
fig_line = px.line(ventas_acumuladas_por_anio, x='Year', y='Sales',
                   labels={'Year': 'Año', 'Sales': 'Ventas Acumuladas'},
                   title='Ventas Acumuladas por Año')

# Mostrar la gráfica en Streamlit
st.plotly_chart(fig_line)

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
