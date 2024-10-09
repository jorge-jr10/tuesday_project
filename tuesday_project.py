#importando bibliotecas necessárias
import streamlit as st
import pandas as pd
from PIL import Image

#definindo senha de acesso
password = '161212'

input_password = st.text_input("Digite a palavra-chave:", type="password")

# Verificar se a palavra-chave está correta
if input_password == password:
        st.success("Acesso concedido!")
        
        # O resto do app vai aqui
        st.write("Bem-vindo ao aplicativo!")
        
    #definindo configurações de layout da pagina 
    st.set_page_config(
        page_title="Controle de RCA's",
        page_icon="📈",  
        layout="wide",
        initial_sidebar_state="expanded")
    
    #lendo o arquivo csv
    df = pd.read_excel('TuesdayStatus1.xlsx')
    
    # Barra lateral no Streamlit
    st.header("V1 | Painel de Controle - RCA's")
    
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
            st.table(df)
    
else:
    st.error("Palavra-chave incorreta. Tente novamente.")
