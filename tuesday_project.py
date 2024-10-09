import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Controle de RCA's",
    page_icon="📈",  
    layout="wide",
    initial_sidebar_state="expanded")

 
#lendo o arquivo csv

df = pd.read_excel('TuesdayStatus1.xlsx')


# Barra lateral no Streamlit

st.header('V1 | Painel de Controle - RCAs')

st.sidebar.markdown('# Bem vindo(a)!')
st.sidebar.markdown("---")
st.sidebar.markdown('## Painel estruturado com linguagem Python')
st.sidebar.markdown("---")
st.sidebar.markdown("## Powered by Governance - TORRA")

image = Image.open('torra-1024.png')
st.sidebar.image( image)

tab1, = st.tabs(['Visão geral'])

with tab1: 
    with st.container():
        st.title(' RCAs mapeados' )
        st.dataframe(df)
