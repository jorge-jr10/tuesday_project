#importando bibliotecas necessárias
import streamlit as st
import pandas as pd
from PIL import Image
       
#definindo configurações de layout da pagina 
st.set_page_config(
        page_title="Controle de RCA's",
        page_icon="📈",  
        layout="wide",
        initial_sidebar_state="expanded")


#lendo o arquivo csv
df = pd.read_excel('TuesdayStatus - 29.10.24.xlsx')
           
# Barra lateral no Streamlit
st.header("V2 | Painel de Controle - RCA's")
           
st.sidebar.markdown('# Bem vindo(a)!')
           
st.sidebar.markdown("---")
           
st.sidebar.markdown('## Painel estruturado com linguagem Python')
           
st.sidebar.markdown("---")
           
st.sidebar.markdown("## Powered by Governance - TORRA")
           
#imagem TORRA
image = Image.open('torra-1024.png')
st.sidebar.image( image )
           
#estrutura da pagina
tab1, = st.tabs(['Visão geral'])
           
with tab1:
       with st.container():
              st.title("RCA's mapeados" )

              df['Data de Abertura'] = pd.to_datetime(df['Data de Abertura']).dt.strftime('%d/%m/%Y')
              
              st.table(df)
