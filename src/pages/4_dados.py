import streamlit as st
import pandas as pd
from app import carregar_planilha

st.set_page_config(layout="wide")
st.title('Dados Planilha')

df = carregar_planilha('Dados', header=3, line=24)

st.dataframe(
    df,
    height=700,
    use_container_width=True
)

def popular_trocas_pintura():
    horas = [
        f"{h:02d}:00"
        for h in range(5, 24)
    ] + ["00:00"]
    df = pd.Series()
    pass

df_teste = pd.DataFrame(
    columns=['Hora', 'Trocas', 'Telas', 'Troca de Cor'],
    # zip([])
)