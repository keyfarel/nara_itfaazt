import streamlit as st
from streamlit_option_menu import option_menu
from views.styles import COLOR_PRIMARY, COLOR_SEC, COLOR_ACCENT
from models.data_service import DataService

def icon(name, size="1rem", color="inherit", class_name=""):
    return f'<i class="bi {name} {class_name}" style="font-size: {size}; color: {color};"></i>'

def card_metric(label, value, delta=None, icon_name="bi-activity"):
    delta_html = ""
    if delta:
        delta_html = f'<div class="metric-delta" style="color: #10B981;">{icon("bi-arrow-up-short")} {delta}</div>'
    
    return f"""
<div class="soft-card">
<div style="display:flex; justify-content:space-between; align-items:start;">
<div>
<div class="metric-label">{label}</div>
<div class="metric-value">{value}</div>
{delta_html}
</div>
<div style="background: #F0FDFA; padding: 10px; border-radius: 10px;">
{icon(icon_name, size="1.5rem", color=COLOR_PRIMARY)}
</div>
</div>
</div>
"""

def render_sidebar():
    with st.sidebar:
        # 1. Branding
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 20px;">
            <h2 style='color:{COLOR_PRIMARY}; margin:0; font-family:"Poppins", sans-serif;'>
                NARA<span style='color:{COLOR_ACCENT}'>.</span>
            </h2>
            <p style='font-size:0.75rem; color:{COLOR_SEC}; margin:0; letter-spacing: 0.5px;'>
                School Analytics System
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"<div style='height: 1px; background-color: #E2E8F0; margin-bottom: 25px;'></div>", unsafe_allow_html=True)
        
        # 2. Role Selection
        st.markdown(f"""
        <p style="font-size: 11px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">
            Login Sebagai
        </p>
        """, unsafe_allow_html=True)

        role = option_menu(
            menu_title=None, 
            options=["Guru", "Orang Tua", "Simulasi", "Panduan"], 
            icons=["person-video3", "house-heart", "controller", "book-half"], 
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "transparent"},
                "icon": {"color": "#64748B", "font-size": "14px"}, 
                "nav-link": {"font-size": "13px", "text-align": "left", "margin": "0px 0px 8px 0px", "padding": "10px 15px", "border-radius": "8px", "--hover-color": "#F1F5F9"},
                "nav-link-selected": {"background-color": COLOR_PRIMARY, "color": "white", "font-weight": "500"},
            }
        )

        # 3. Student Selection
        selected_child_name = None
        if role == "Orang Tua":
            st.markdown(f"<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
            st.markdown(f"""
            <p style="font-size: 11px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">
                Pilih Siswa
            </p>
            """, unsafe_allow_html=True)
            
            df = DataService.get_class_data()
            selected_child_name = st.selectbox(
                "Pilih Siswa", 
                df['Nama'], 
                label_visibility="collapsed"
            )

        # 4. Spacer
        st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)
        
        # 5. Footer Info
        st.markdown(f"""
        <div style="background-color: #F8FAFC; border: 1px solid #E2E8F0; color: #475569; padding: 12px; border-radius: 8px; font-size: 0.8rem;">
            <div style="display: flex; gap: 8px; align-items: start;">
                <div style="margin-top: 1px;">{icon('bi-broadcast', color='#3B82F6', size="0.9rem")}</div>
                <div>
                    <strong style="color: #1E293B;">Demo SIC Stage 4</strong><br>
                    <span style="font-size: 0.75rem; opacity: 0.8;">Samsung Innovation Campus Batch 7</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        return role, selected_child_name
