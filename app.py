import streamlit as st
import pandas as pd

# @st.cache_data
def carregar_planilha(sheetname:str, header: int = None, nrows: int = None, usecols: str = None, index_col: str | int = None):
    df = pd.read_excel(
        'Setup - Geral - TS F.07 11.xlsm', 
        sheet_name=sheetname,
        header=header,
        nrows=nrows,
        usecols=usecols,
        index_col=index_col
    )
    return df  

import streamlit as st

pages = {
    "Dados":[
        st.Page("src/pages/dados/1_pendente.py", title="Pendente", icon=":material/dashboard:"),
        st.Page("src/pages/dados/2_Base_Custos_Mesa_Ser.py", title="Base Custos Mesas Serigrafia", icon=":material/analytics:"),
        st.Page("src/pages/dados/3_Resumo_Trocas.py", title="Resumo de Trocas", icon=":material/description:"),
        st.Page("src/pages/dados/4_dados.py", title="Dados Planilha", icon=":material/description:"),
        st.Page("src/pages/dados/5_serigrafia_reguladores.py", title="Serigrafia Reguladores", icon=":material/description:"),
    ],
    "Monitoramento Reguladores": [
        st.Page("src/pages/monitoramento_reguladores/0_reg_serigrafia.py", title="Reguladores Serigrafia", icon=":material/description:"),
        st.Page("src/pages/monitoramento_reguladores/1_reg_montagem.py", title="Reguladores Montagem", icon=":material/description:"),
        st.Page("src/pages/monitoramento_reguladores/2_reg_pintura.py", title="Reguladores Pintura", icon=":material/description:"),
    ],
    "Monitoramento Trocades de Telas": [
        st.Page("src/pages/monitoramento_trocadores/0_troc_serigrafia.py", title="Trocadores Serigrafia", icon=":material/description:"),
        st.Page("src/pages/monitoramento_trocadores/1_troc_montagem.py", title="Trocadores Montagem", icon=":material/description:"),
        st.Page("src/pages/monitoramento_trocadores/2_troc_pintura.py", title="Trocadores Pintura", icon=":material/description:"),
    ],
}

st.navigation(pages, position="sidebar").run()