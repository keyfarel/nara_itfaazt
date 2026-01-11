import streamlit as st
from views.styles import get_custom_css
from models.data_service import DataService
from views.components import render_sidebar
from views.guru_view import view_guru
from views.ortu_view import view_ortu
from views.manual_view import view_manual
from views.simulation_view import view_simulation

def configure_app():
    st.set_page_config(
        page_title="NARA School Analytics",
        page_icon=None,
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.markdown(get_custom_css(), unsafe_allow_html=True)

def main():
    configure_app()
    DataService.init_data()
    
    role, student_name = render_sidebar()

    if role == "Guru":
        view_guru()
    elif role == "Orang Tua":
        if student_name:
            view_ortu(student_name)
    elif role == "Simulasi":
        view_simulation()
    elif role == "Panduan":
        view_manual()

if __name__ == "__main__":
    main()
