from difflib import SequenceMatcher
import streamlit as st
from app.mock_data import reports, tasks


def init_state():
    if "reports" not in st.session_state:
        st.session_state.reports = []

        for report in reports.copy():
            report["repeat_count"] = report.get("repeat_count", 1)
            st.session_state.reports.append(report)

    if "tasks" not in st.session_state:
        st.session_state.tasks = tasks.copy()


def similarity(a, b):
    return SequenceMatcher(None, a.lower().strip(), b.lower().strip()).ratio()


def is_repeated_report(new_report, existing_report):
    same_type = new_report.get("type", "").lower() == existing_report.get("type", "").lower()

    location_similarity = similarity(
        new_report.get("location", ""),
        existing_report.get("location", "")
    )

    summary_similarity = similarity(
        new_report.get("summary", ""),
        existing_report.get("summary", "")
    )

    return same_type and (location_similarity > 0.65 or summary_similarity > 0.60)


def get_reports():
    return st.session_state.reports


def save_report(new_report):
    for existing_report in st.session_state.reports:
        if is_repeated_report(new_report, existing_report):
            existing_report["repeat_count"] = existing_report.get("repeat_count", 1) + 1
            existing_report["confidence"] = min(
                100,
                existing_report.get("confidence", 60) + 5
            )
            return existing_report, True

    new_report["repeat_count"] = 1
    st.session_state.reports.insert(0, new_report)
    return new_report, False


def get_tasks():
    return st.session_state.tasks


def save_task(task):
    st.session_state.tasks.append(task)