import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.graph_objs.scatter._textfont as tfonte
import numpy as np
from pathlib import Path

st.set_page_config(page_title="Monitoramento Trocadores Pintura",layout="wide")

equipamentos = [
    f"S7M{n:02d}"
    for n in range(1, 19)
]

horas = [
        f"{h:02d}:00" 
        for h in range(5, 24)
    ] + ["00:00"]

dados_tabela = pd.DataFrame(
    np.zeros((len(equipamentos), len(horas))).round(decimals=0),
    index=equipamentos,
    columns=horas
)

dados_tabela.loc["S7M07","13:00"] = -4
dados_tabela.loc["S7M17","14:00"] = -1
dados_tabela.loc["S7M22","06:00"] = -1
dados_tabela.loc["S7M08","08:00"] = 2
dados_tabela.loc["S7M22","08:00"] = 2

oscilacao = dados_tabela.sum(axis=0).tolist()

# st.markdown(oscilacao)

css_file = Path(__file__).parent.parent / 'styles.css'

with open(css_file) as css:
    # carregar o css
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)
    # carregar a barra de titulo
    st.markdown("""
                <div class='title-bar'>
                    MONITORAMENTO HORA A HORA 
                </div>
                """,
                unsafe_allow_html=True)
    st.markdown('### TROCADORES DE TELAS')





# st.markdown(f"{equipamentos}")


c1, c2, c3 = st.columns([1,1,5])



with c1:
    st.markdown("""
        <div class='metric-card'>
            <div class='metric-label'>Valor Efetivo</div>
            <div class='metric-value'>-4</div>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div class='metric-card'>
            <div class='metric-label'>Valor Troca</div>
            <div class='metric-value'>4</div>
        </div>
    """, unsafe_allow_html=True)

with c3:

    fig = go.Figure()
    textfont = tfonte.Textfont(size=20)

    fig.add_trace(
        go.Scatter(
            x=horas,
            y=oscilacao,
            mode="lines+markers+text",
            text=oscilacao,
            textposition="top center",
            line=dict(color="#1f2a84", width=3),
            textfont=textfont
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
        title="Efetivo Hora a Hora",
        paper_bgcolor="white",
        plot_bgcolor="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# st.markdown(
#     "<div class='section-title'>Oscilação de Efetivo</div>",
#     unsafe_allow_html=True
# )

# df_oscilacao = pd.DataFrame({
#     f"{h} Efetivo": [v]
#     for h,v in zip(horas, oscilacao)
# })

# st.dataframe(
#     df_oscilacao,
#     use_container_width=True,
#     hide_index=True
# )

dados_tabela.loc["S7M07","13:00"] = -4
dados_tabela.loc["S7M17","14:00"] = -1
dados_tabela.loc["S7M22","06:00"] = -1
dados_tabela.loc["S7M08","08:00"] = 2
dados_tabela.loc["S7M22","08:00"] = 2

st.markdown(
    "<div class='section-title'>Hora a Hora</div>",
    unsafe_allow_html=True
)

def destacar(valor):
    if valor < 0:
        return (
            "background-color:#ff003c;"
            "color:white;"
            "font-weight:bold;"
        )
    elif valor > 0:
        return(
            "background-color:green;"
            "color:white;"
            "font-weight:bold;"
        )
    return ""

st.dataframe(
    dados_tabela.style.map(destacar),
    use_container_width=True,

)