import streamlit as st
import pandas as pd
from app import carregar_planilha

st.set_page_config(layout="wide")
st.title('Resumo de Trocas')

df = carregar_planilha('Resumo_Trocas')

st.dataframe(
    df,
    height=700,
    use_container_width=True
)