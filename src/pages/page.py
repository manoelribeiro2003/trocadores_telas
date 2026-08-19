from pathlib import Path
import streamlit as st

css_file = Path(__file__).parent / "styles.css"

def carregar_html(**data):
    with open(css_file) as css:
        st.markdown(
            f"""

            <style>{css.read()}</style>", unsafe_allow_html=True
            <div class='title-bar'>
                MONITORAMENTO DAS OSCILAÇÕES DE EFETIVOS TS7
            </div>

            """,
            unsafe_allow_html=True
        )

