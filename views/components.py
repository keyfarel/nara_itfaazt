import streamlit as st
from streamlit_option_menu import option_menu
from views.styles import get_current_theme, THEMES
from models.data_service import DataService

def icon(name, size="1rem", color="inherit", class_name=""):
    return f'<i class="bi {name} {class_name}" style="font-size: {size}; color: {color};"></i>'

def card_metric(label, value, delta=None, icon_name="bi-activity"):
    t = get_current_theme()
    delta_html = ""
    if delta:
        delta_html = f'<div class="metric-delta" style="color: #10B981;">{icon("bi-arrow-up-short")} {delta}</div>'
    
    return f"""
<div class="soft-card">
<div style="display:flex; justify-content:space-between; align-items:start;">
<div>
<div class="metric-label" style="color:{t['secondary']}">{label}</div>
<div class="metric-value" style="color:{t['text']}">{value}</div>
{delta_html}
</div>
<div style="background: {t['background']}; padding: 10px; border-radius: 10px;">
{icon(icon_name, size="1.5rem", color=t['primary'])}
</div>
</div>
</div>
"""

def render_sidebar():
    with st.sidebar:
        # 1. Branding
        t = get_current_theme()
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 25px; margin-top: 10px;">
            <h1 style='color:{t['primary']}; margin:0; font-family:"Poppins", sans-serif; font-size: 2.8rem; font-weight: 800; letter-spacing: -1px;'>
                NARA<span style='color:{t['accent']}'>.</span>
            </h1>
            <p style='font-size:0.8rem; color:{t['secondary']}; margin:0; letter-spacing: 1px; font-weight: 500; opacity: 0.8;'>
                School Analytics System
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"<div style='height: 1px; background-color: {t['border']}; margin-bottom: 25px;'></div>", unsafe_allow_html=True)
        
        # 2. Role Selection
        st.markdown(f"""
        <p style="font-size: 11px; font-weight: 700; color: {t['secondary']}; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; opacity: 0.7;">
            Login Sebagai
        </p>
        """, unsafe_allow_html=True)

        # Determine option menu styles based on theme
        # Option Menu unfortunately uses inline styles heavily, so we map them carefully
        
        nav_bg = t['card_bg'] if st.session_state.get("theme_mode") == "light" else "transparent"
        nav_hover = "#F8FAFC" if st.session_state.get("theme_mode") == "light" else "#1E293B"

        role = option_menu(
            menu_title=None, 
            options=["Guru", "Orang Tua", "Simulasi", "Panduan"], 
            icons=["person-video3", "house-heart", "controller", "book-half"], 
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "transparent"},
                "icon": {"color": t['secondary'], "font-size": "14px"}, 
                "nav-link": {
                    "font-size": "14px", 
                    "text-align": "left", 
                    "margin": "0px 0px 8px 0px", 
                    "padding": "12px 15px", 
                    "border-radius": "10px", 
                    "color": t['secondary'],
                    "--hover-color": nav_hover
                },
                "nav-link-selected": {"background-color": t['primary'], "color": "white", "font-weight": "500"},
            }
        )

        # 3. Student Selection
        selected_child_name = None
        if role == "Orang Tua":
            st.markdown(f"<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
            st.markdown(f"""
            <p style="font-size: 11px; font-weight: 700; color: {t['secondary']}; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; opacity: 0.7;">
                Pilih Siswa
            </p>
            """, unsafe_allow_html=True)
            
            df = DataService.get_class_data()
            selected_child_name = st.selectbox(
                "Pilih Siswa", 
                df['Nama'], 
                label_visibility="collapsed"
            )

        # 4. Spacer & Theme Toggle
        st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
        
        # Theme Toggle
        current_mode = st.session_state.get("theme_mode", "light")
        enable_dark = st.toggle("Dark Mode", value=(current_mode == "dark"))
        new_mode = "dark" if enable_dark else "light"
        
        if new_mode != current_mode:
            st.session_state["theme_mode"] = new_mode
            st.rerun()

        # 5. Footer Info
        st.markdown(f"""
        <div style="background-color: {t['background']}; border: 1px solid {t['border']}; color: {t['secondary']}; padding: 12px; border-radius: 8px; font-size: 0.8rem; margin-top: 20px;">
            <div style="display: flex; gap: 8px; align-items: start;">
                <div style="margin-top: 1px;">{icon('bi-broadcast', color='#3B82F6', size="0.9rem")}</div>
                <div>
                    <strong style="color: {t['text']};">Demo SIC Stage 4</strong><br>
                    <span style="font-size: 0.75rem; opacity: 0.8;">Samsung Innovation Campus Batch 7</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        return role, selected_child_name
