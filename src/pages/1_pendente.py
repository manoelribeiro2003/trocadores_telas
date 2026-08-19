import streamlit as st
import pandas as pd
from app import carregar_planilha

st.set_page_config(layout="wide")
st.title('Carga Pendente')

df = carregar_planilha('Pendente')

st.dataframe(
    df,
    height=700,
    use_container_width=True
)
