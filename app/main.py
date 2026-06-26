import streamlit as st
from app.database import init_state

st.set_page_config(
    page_title="Bolivia360",
    page_icon="🇧🇴",
    layout="wide"
)

init_state()

st.sidebar.title("🇧🇴 Bolivia360")
st.sidebar.caption("La IA que vuelve Bolivia más predecible.")

page = st.sidebar.radio(
    "Menú",
    ["Mi Día", "Reportar", "Bolivia en Vivo", "Copiloto IA"]
)

if page == "Mi Día":
    from app.pages.mi_dia import show
    show()

elif page == "Reportar":
    from app.pages.reportar import show
    show()

elif page == "Bolivia en Vivo":
    from app.pages.bolivia_en_vivo import show
    show()

elif page == "Copiloto IA":
    from app.pages.copiloto_ia import show
    show()