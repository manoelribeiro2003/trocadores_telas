import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from pathlib import Path

st.set_page_config(
    page_title="Monitoramento TS7",
    layout="wide"
)

css_file = Path(__file__).parent / "styles.css"

with open(css_file) as css:
    # carregar o css
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)
    # carregar a barra de titulo
    st.markdown(
                f"""
                <div class='title-bar'>
                    MONITORAMENTO DAS OSCILAÇÕES DE EFETIVOS TS7
                </div>

                <div>
                
                </div>

                ## MONTAGEM

                """,
                unsafe_allow_html=True
            )

equipamentos = [
    "S7M01","S7M02","S7M03","S7M05",
    "S7M07","S7M08","S7M10","S7M11",
    "S7M12","S7M13","S7M14","S7M17",
    "S7M18","S7M19","S7M22"
]

horas = [
    "05:00","06:00","07:00","08:00",
    "09:00","10:00","11:00","12:00",
    "13:00","14:00","15:00"
]

oscilacao = [0, -1, 0, 2, 0, 0, 0, 0, -4, -1, 0]

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

    fig.add_trace(
        go.Scatter(
            x=horas,
            y=oscilacao,
            mode="lines+markers+text",
            text=oscilacao,
            textposition="top center",
            line=dict(color="#1f2a84", width=3)
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

dados = pd.DataFrame(
    np.zeros((len(equipamentos), len(horas))),
    index=equipamentos,
    columns=horas
)

dados.loc["S7M07","13:00"] = -4
dados.loc["S7M17","14:00"] = -1
dados.loc["S7M22","06:00"] = -1
dados.loc["S7M08","08:00"] = 2

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
    return ""

st.dataframe(
    dados.style.map(destacar),
    use_container_width=True
)