import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.graph_objs.scatter._textfont as tfonte
import numpy as np
from pathlib import Path
from app import carregar_planilha

# ================================================DEFINIÇÕES=========================================================================================
# Definir arquivo css 
css_file = Path(__file__).parent.parent / 'styles.css'

# Definição da configuração inicial da pagina 
st.set_page_config(page_title="Monitoramento Reguladores Serigrafia",layout="wide")

# Definição das horas
horas_1_turno = [f"{h:02d}:00" for h in range(6, 16)]
# horas_2_turno = [f"{h:02d}:00" for h in range(15, 24)] + ['00:00']

# Definição das colunas dos dataframes de monitoramento hora a hora 
colunas = [
    f"{palavra} {h}h" 
    for h in range(6, 16)
    for palavra in ['Trocas', 'Telas']
]

# Definição dos indices dos dataframes de monitoramento hora a hora
equipamentosA = ["Total A"] + [f"S7S{n:02d}" for n in range(1, 11)]
equipamentosB = ["Total B"] + [f"S7S{n:02d}" for n in range(11, 19)]

# Definição dos dataframes 
df_A_1_turno = carregar_planilha(sheetname='Serigrafia - Reguladores', header=18, nrows=11, usecols='d:w')
df_A_1_turno.index = equipamentosA
df_A_1_turno.columns = colunas
# ------------------------------------------------------------------------------------------------------
df_B_1_turno = carregar_planilha(sheetname='Serigrafia - Reguladores', header=32, nrows=10, usecols='d:w')
df_B_1_turno.index = equipamentosB
df_B_1_turno.columns = colunas

# carrega dataframe de necessidade de pessoas
df_nec_reg = carregar_planilha(sheetname='Serigrafia - Reguladores', header=2, nrows=4, usecols='d:w')  
sr_nec_reg_1_tur_A = df_nec_reg.loc[1]
sr_nec_reg_1_tur_A = sr_nec_reg_1_tur_A[(sr_nec_reg_1_tur_A.notna())]
sr_nec_reg_1_tur_A.index = horas_1_turno
sr_nec_reg_1_tur_A.name = 'Serigrafia A - 1º Turno'
sr_nec_reg_1_tur_A = sr_nec_reg_1_tur_A.apply(np.ceil)
max_osc = int(sr_nec_reg_1_tur_A.max() + 3)
min_osc = int(sr_nec_reg_1_tur_A.min() - 2)
oscilacao = [x for x in range(min_osc, max_osc)]

# =========================================== INSERIR HTML ===================================================================================================
with open(css_file) as css:
    # Carregar o css
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)
    # Inserir a barra de titulo azul
    st.markdown(f"<div class='title-bar'>MONITORAMENTO HORA A HORA {opcao = st.radio("Turno",["1º", "2º", "3º"],horizontal=True)} </div>",unsafe_allow_html=True)



# Inserir os graficos em duas colunas
c1, c2 = st.columns([1,1])
with c1:
    # Cria um grafico vazio sem tipo
    fig = go.Figure()

    # Adiciona uma serie do tipo Scatter ao grafico vazio
    fig.add_trace(
        go.Scatter(
            x=horas_1_turno,
            y=sr_nec_reg_1_tur_A,
            mode="lines+markers+text",
            text=sr_nec_reg_1_tur_A,
            textposition="top center",
            line=dict(color="#1f2a84", width=3),
            textfont=dict(size=16)
        )
    )

    fig.update_layout(
        height=250,
        margin=dict(
            l=10,
            r=10,
            t=30,
            b=10
        ),
        title="Necessidades de Reguladores - 1 Turno Setor A",
        paper_bgcolor="white",
        plot_bgcolor="white",
    )

    fig.update_yaxes(
        range=[min_osc, max_osc],
        tickmode="array",
        tickvals=oscilacao
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
# Função para colorir as colunas do dataframe das trocas/telas por hora
def colorir_colunas(col: pd.Series, df: pd.DataFrame):
    idx_col = df.columns.get_loc(col.name)
    cor_coluna = "#DDEBF7" if (idx_col // 2) % 2 == 0 else "#FCE4D6"
    estilos = [f"background-color: {cor_coluna}"] * len(col)
    estilos[0] = "background-color: #FFF2CC; font-weight: bold"
    return estilos

# Aplicar as cores
df_A_1_turno = df_A_1_turno.style.apply(
    lambda col: colorir_colunas(col, df_A_1_turno)
)
# Mostrar o dataframe na tela
st.dataframe(df_A_1_turno, height=424)

opcao = st.radio("Turno",["1º", "2º", "3º"],horizontal=True)