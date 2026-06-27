import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from app.database import init_state

st.set_page_config(
    page_title="Bolivia360",
    page_icon="🇧🇴",
    layout="wide"
)

init_state()

pg = st.navigation([
    st.Page("pages/mi_dia.py",          title="Mi Día",          icon="☀️"),
    st.Page("pages/reportar.py",         title="Reportar",        icon="📍"),
    st.Page("pages/bolivia_en_vivo.py",  title="Bolivia en Vivo", icon="🇧🇴"),
    st.Page("pages/copiloto_ia.py",      title="Copiloto IA",     icon="🤖"),
])
pg.run()

