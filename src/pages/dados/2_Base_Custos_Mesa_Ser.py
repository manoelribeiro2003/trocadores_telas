import streamlit as st
import pandas as pd
from app import carregar_planilha

st.set_page_config(layout="wide")
st.title('Base Custos Mesas de Serigrafia')

df = carregar_planilha('Base_Custos_Mesa_Ser')

st.dataframe(
    df,
    height=700,
    use_container_width=True
)