import streamlit as st
import pandas as pd
from app import carregar_planilha

st.set_page_config(layout="wide",initial_sidebar_state='expanded')
# st.title('Dados Planilha')

# CARREGAR PLANILHAS================================================================================

df_A = carregar_planilha(sheetname='Serigrafia - Reguladores', header=18, nrows=11, usecols='c:u')
df_A = df_A.set_index(df_A.columns[0])
df_A.columns=["Trocas 6h","Telas 6h","Trocas 7h","Telas 7h","Trocas 8h","Telas 8h","Trocas 9h","Telas 9h","Trocas 10h","Telas 10h","Trocas 11h","Telas 11h","Trocas 12h","Telas 12h","Trocas 13h","Telas 13h","Trocas 14h","Telas 14h"
            #   ,"Trocas 15h","Telas 15h","Trocas 16h","Telas 16h","Trocas 17h","Telas 17h","Trocas 18h","Telas 18h","Trocas 19h","Telas 19h","Trocas 20h","Telas 20h","Trocas 21h","Telas 21h","Trocas 22h","Telas 22h","Trocas 23h","Telas 23h","Trocas 00h","Telas 00h"
              ]

df_B = carregar_planilha(sheetname='Serigrafia - Reguladores', header=32, nrows=11, usecols='c:u')
df_B = df_B.set_index(df_B.columns[0])
df_B.columns=["Trocas 6h","Telas 6h","Trocas 7h","Telas 7h","Trocas 8h","Telas 8h","Trocas 9h","Telas 9h","Trocas 10h","Telas 10h","Trocas 11h","Telas 11h","Trocas 12h","Telas 12h","Trocas 13h","Telas 13h","Trocas 14h","Telas 14h"
            #   ,"Trocas 15h","Telas 15h","Trocas 16h","Telas 16h","Trocas 17h","Telas 17h","Trocas 18h","Telas 18h","Trocas 19h","Telas 19h","Trocas 20h","Telas 20h","Trocas 21h","Telas 21h","Trocas 22h","Telas 22h","Trocas 23h","Telas 23h","Trocas 00h","Telas 00h"
              ]


# PRINTAR DATAFRAME====================================================================================

c1, c2 = st.columns([8,5])

with c1:
    st.markdown('### Setor Serigrafia Hora a Hora (A) 1º Turno')
    st.dataframe(
        df_A,
        height=425,
        use_container_width=True
    )
    st.markdown('### Setor Serigrafia Hora a Hora (B) 1º Turno')
    st.dataframe(
        df_B,
        height=354,
        use_container_width=True
    )
