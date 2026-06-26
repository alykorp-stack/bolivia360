import streamlit as st
from app.mock_data import user_profile
from app.database import get_reports, get_tasks
from app.recommender import filter_relevant_reports
from app.ai import generate_my_day


def show():
    st.title("☀️ Mi Día")
    st.write("Resumen personalizado según tus tareas y reportes ciudadanos.")

    tasks = get_tasks()
    reports = get_reports()
    relevant_reports = filter_relevant_reports(user_profile, reports)

    st.subheader("✅ Checklist")
    for task in tasks:
        st.checkbox(f"{task['task']} — {task['time']}")

    st.subheader("⚠️ Alertas relevantes")
    if relevant_reports:
        for report in relevant_reports:
            st.info(
                f"**{report['summary']}**\n\n"
                f"Ubicación: {report['location']}\n\n"
                f"Confianza: {report['confidence']}%\n\n"
                f"Recomendación: {report['recommendation']}"
            )
    else:
        st.success("No hay alertas relevantes para ti por ahora.")

    if st.button("Generar resumen con IA"):
        summary = generate_my_day(user_profile, tasks, relevant_reports)
        st.subheader("🤖 Resumen IA")
        st.write(summary)