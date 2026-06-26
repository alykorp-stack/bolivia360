import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from app.database import get_reports


def show():
    st.title("🇧🇴 Bolivia en Vivo")
    st.write("Reportes ciudadanos analizados por IA.")

    reports = get_reports()

    if not reports:
        st.warning("Todavía no hay reportes.")
        return

    df = pd.DataFrame(reports)

    category = st.selectbox(
        "Filtrar por tipo",
        ["Todos"] + sorted(df["type"].dropna().unique().tolist())
    )

    if category != "Todos":
        df = df[df["type"] == category]

    st.subheader("Reportes recientes")

    for _, report in df.iterrows():
        st.write(f"### {report.get('summary', 'Reporte')}")
        st.write(f"📍 {report.get('location', '')}")
        st.write(f"Nivel: {report.get('severity', '')}")
        st.write(f"Confianza: {report.get('confidence', '')}%")
        st.write(f"Veces reportado: {report.get('repeat_count', 1)}")
        st.write(f"Recomendación: {report.get('recommendation', '')}")
        st.divider()

    st.subheader("Mapa demo")
    m = folium.Map(location=[-16.5, -68.15], zoom_start=12)
    folium.Marker(
        [-16.5, -68.15],
        popup="La Paz - reportes ciudadanos"
    ).add_to(m)

    st_folium(m, width=700, height=400)