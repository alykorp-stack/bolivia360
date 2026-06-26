import streamlit as st
from app.ai import analyze_report
from app.database import save_report


def show():
    st.title("📍 Reportar situación")
    st.write("Comparte lo que está pasando en tiempo real.")

    category = st.selectbox(
        "Tipo de reporte",
        [
            "Bloqueo",
            "Fila en trámite",
            "Gasolina",
            "Transporte",
            "Corte de agua/luz",
            "Colegio/Universidad",
            "Seguridad",
            "Otro"
        ]
    )

    location = st.text_input("Ubicación")
    description = st.text_area("Describe lo que está pasando")
    photo = st.file_uploader("Sube una foto opcional", type=["jpg", "png", "jpeg"])

    if st.button("Analizar y reportar"):
        if not description or not location:
            st.warning("Completa la ubicación y la descripción.")
            return

        report = analyze_report(description, location, category)
        
        saved_report, was_repeated = save_report(report)

        if was_repeated:
            st.success("Este reporte ya existía. Se actualizó el número de reportes y la confianza.")
        else:
            st.success("Nuevo reporte guardado.")

        st.write(f"Veces reportado: {saved_report.get('repeat_count', 1)}")
        st.write(f"Confianza actualizada: {saved_report.get('confidence', 0)}%")

        st.json(report)


show()

