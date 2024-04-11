import streamlit as st
import pandas as pd
#configurando o titulo
st.set_page_config(page_title="MEu primeiro site")
#agrupando elementos em um container
with st.container():
    st.subheader("Meu primeiro site com streamlit")
    st.title("DashBoard de contratos")
    st.write("Informações sobre os contratos ")
    st.write("Quer aprender python [clique aqui](https://www.youtube.com/watch?v=h4UqMyldS7Q)")
@st.cache_data#decorator --> linha de codigo que adiciona uma funcionalidade para funcao que vem logo em baixo , vantagens ---> quando aplicamos ele, ele armazena no cache do usuario as informações que ele esta carreagando aqui , primeira vez geralmente demora mas depois ele flui melhor 
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela


with st.container():
    st.write('---')
    qtd_dias = st.selectbox('selecione o periodo',['7D','15D','30D'])
    numero_dias = int(qtd_dias.replace('D',''))
    dados = carregar_dados()
    dados = dados[-numero_dias:]
    st.area_chart(dados,x="Data",y="Contratos") 
