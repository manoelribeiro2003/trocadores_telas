import streamlit as st
import pandas as pd

@st.cache_data
def carregar_planilha(sheetname:str, **data):
    if(data['header'] and data['line']):
        return pd.read_excel(
            'Setup - Geral - TS F.07 11.xlsm', 
            sheet_name=sheetname,
            header=data['header'],
            nrows=data['line']
        )
    return pd.read_excel('Setup - Geral - TS F.07 11.xlsm', sheet_name=sheetname)


pages = [
    st.Page("src/pages/1_pendente.py", title="Pendente", icon=":material/dashboard:"),
    st.Page("src/pages/2_Base_Custos_Mesa_Ser.py", title="Base Custos Mesas Serigrafia", icon=":material/analytics:"),
    st.Page("src/pages/3_Resumo_Trocas.py", title="Resumo de Trocas", icon=":material/description:"),
    st.Page("src/pages/4_dados.py", title="Dados Planilha", icon=":material/description:"),
    st.Page("src/pages/5_monitoramento.py", title="Monitoramento", icon=":material/description:"),
]


pg = st.navigation(pages, position="sidebar")

pg.run()