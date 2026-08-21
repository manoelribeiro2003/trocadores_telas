import streamlit as st
import pandas as pd
from app import carregar_planilha

st.set_page_config(layout="wide")
st.title('Dados Planilha')

# st.sidebar.selectbox(
#     "Setor",
#     ["Pintura", "Montagem", "Solda"]
# )



# CARREGAR PLANILHAS================================================================================

df_pintura = carregar_planilha(sheetname='Dados', header=3, nrows=20, usecols='B:E')
df_pintura = df_pintura.set_index(df_pintura.columns[0])
df_pintura.columns=['Trocas', 'Telas', 'Troca de Cor']

df_nec_pint = carregar_planilha(sheetname='Dados', header=3, nrows=21, usecols='G:J')
df_nec_pint = df_nec_pint.set_index(df_nec_pint.columns[0])
df_nec_pint.columns=['Conferente', 'Telas', 'Troca de Cor']

df_montagem = carregar_planilha(sheetname='Dados', header=3, nrows=20, usecols='L:O')
df_montagem = df_montagem.set_index(df_montagem.columns[0])
df_montagem.columns=['Trocas', 'Telas', 'Troca de Cor']

df_nec_mont = carregar_planilha(sheetname='Dados', header=3, nrows=21, usecols='Q:T')
df_nec_mont = df_nec_mont.set_index(df_nec_mont.columns[0])
df_nec_mont.columns=['Conferente', 'Telas', 'Troca de Cor']

df_serigrafia = carregar_planilha(sheetname='Dados', header=3, nrows=20, usecols='V:Y')
df_serigrafia = df_serigrafia.set_index(df_serigrafia.columns[0])
df_serigrafia.columns=['Trocas', 'Telas', 'Troca de Cor']

df_nec_serig = carregar_planilha(sheetname='Dados', header=3, nrows=21, usecols='AA:AD')
df_nec_serig = df_nec_serig.set_index(df_nec_serig.columns[0])
df_nec_serig.columns=['Conferente', 'Telas', 'Troca de Cor']


# PRINTAR DATAFRAMES====================================================================================
c1, c2 = st.columns([1,1])

with c1:
    st.markdown('Pintura')
    st.dataframe(
        df_pintura,
        height=750,
        use_container_width=True,
    )
with c2:
    st.markdown('Necessidade de MOI/MOA')
    st.dataframe(
        df_nec_pint,
        height=750,
        use_container_width=True
    )
    
c3, c4 = st.columns([1,1])

with c3:
    st.markdown('Montagem')
    st.dataframe(
        df_montagem,
        height=750,
        use_container_width=True
    )
with c4:
    st.markdown('Necessidade de MOI/MOA')
    st.dataframe(
        df_nec_mont,
        height=750,
        use_container_width=True
    )

c5, c6 = st.columns([1,1])

with c5:
    st.markdown('Serigrafia')
    st.dataframe(
        df_serigrafia,
        height=750,
        use_container_width=True
    )
with c6:
    st.markdown('Necessidade de MOI/MOA')
    st.dataframe(
        df_nec_serig,
        height=750,
        use_container_width=True
    )



def popular_trocas_pintura():
    horas = [
        f"{h:02d}:00"
        for h in range(5, 24)
    ] + ["00:00"]
    df = pd.Series()