import streamlit as st
from app.database import get_tasks, save_task
from app.ai import edit_my_day


def show():
    st.title("🤖 Copiloto IA")
    st.write("Dile a la IA qué cambió en tu día.")

    current_tasks = get_tasks()

    user_message = st.text_area(
        "Ejemplo: Tengo que ir al banco urgente / No podré ir al gimnasio / Agrega pago de colegio el día 5"
    )

    if st.button("Actualizar mi día"):
        if not user_message:
            st.warning("Escribe qué quieres cambiar.")
            return

        result = edit_my_day(user_message, current_tasks)

        st.subheader("Resultado IA")
        st.json(result)

        if result.get("action") == "add_task":
            new_task = {
                "task": result.get("task", user_message),
                "time": result.get("time", "Hoy")
            }
            save_task(new_task)
            st.success("Tarea agregada a Mi Día.")
        else:
            st.info(result.get("recommendation", "La IA procesó tu solicitud."))


show()