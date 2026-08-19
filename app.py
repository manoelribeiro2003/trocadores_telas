import streamlit as st
import pandas as pd

@st.cache_data
def carregar_planilha(sheetname:str):
    return pd.read_excel('Setup - Geral - TS F.07 11.xlsm', sheet_name=sheetname)


pages = [
    st.Page("src/pages/1_pendente.py", title="Pendente", icon=":material/dashboard:"),
    st.Page("src/pages/2_Base_Custos_Mesa_Ser.py", title="Base Custos Mesas Serigrafia", icon=":material/analytics:"),
    st.Page("src/pages/3_Resumo_Trocas.py", title="Resumo de Trocas", icon=":material/description:"),
    st.Page("src/pages/dados.py", title="Dados", icon=":material/description:"),
]


pg = st.navigation(pages, position="sidebar")

pg.run()