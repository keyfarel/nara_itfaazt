import streamlit as st
import pandas as pd
import numpy as np
import random
import time
from streamlit_option_menu import option_menu
from views.components import card_metric, icon
from views.styles import get_current_theme, THEMES

# --- Dummy Data Generators (Matching DataService Schema) ---
def get_dummy_class_data():
    """Generates dummy data matching the exact schema of DataService.get_class_data"""
    data = {
        'Nama': ['Andi (Sim)', 'Budi (Sim)', 'Citra (Sim)', 'Dewi (Sim)', 'Eko (Sim)', 'Fajar (Sim)', 'Gita (Sim)', 'Hadi (Sim)'],
        'Level': [3, 5, 2, 6, 1, 4, 3, 5],
        'XP': [320, 550, 180, 700, 80, 410, 350, 520],
        'Kelancaran_Avg': [75, 88, 50, 95, 40, 78, 65, 85], 
        'Status_Hari_Ini': ['Normal', 'Lancar', 'Terbata', 'Lancar', 'Terbata', 'Lancar', 'Normal', 'Lancar'],
        'Kata_Sulit': [[], ['Eks-tra'], ['Me-nga-pa'], [], ['Ba-ca', 'Tu-lis'], [], ['Me-nyan-yi'], []],
        'Diagnosis': [
            "Perlu latihan rutin.",
            "Sangat baik.",
            "Masih terbata-bata.",
            "Luar biasa.",
            "Perlu bimbingan khusus.",
            "Konsisten.",
            "Cukup baik.",
            "Bagus sekali."
        ]
    }
    return pd.DataFrame(data)

def get_dummy_student_data():
    """Generates dummy single student data matching DataService.get_student_data"""
    return {
        'Nama': 'Budi Santoso (Simulasi)',
        'Level': 5,
        'XP': 550,
        'Kelancaran_Avg': 88,
        'Status_Hari_Ini': 'Lancar',
        'Kata_Sulit': ['Me-nye-lam'],
        'Diagnosis': "Secara umum sangat lancar, hanya ragu di kata majemuk."
    }

# ==============================================================================
# GURU VIEW REPLICA (Shadowing views/guru_view.py)
# ==============================================================================

@st.dialog("Detail Siswa (Simulasi)", width="large")
def show_sim_student_detail(student):
    t = get_current_theme()
    # --- Profile Header ---
    st.markdown(f"""
    <div class="soft-card" style="display:flex; align-items:center; gap:20px; padding: 20px; border-left: 5px solid {t['primary']}; background: {t['card_bg']};">
        <div style="border-radius: 50%; overflow:hidden; width:80px; height:80px; border: 3px solid {t['primary']}; flex-shrink: 0;">
            <img src="https://img.freepik.com/free-vector/cute-owl-sitting-tree-branch-cartoon-vector-illustration_138676-2187.jpg?w=100" width="80" style="object-fit: cover;">
        </div>
        <div style="flex-grow: 1;">
            <div style="font-size: 0.85rem; color: {t['secondary']}; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">Siswa Kelas 1-A</div>
            <h3 style="margin:0; color:{t['primary']}; font-size: 1.5rem;">{student['Nama']}</h3>
            <div style="display: flex; gap: 10px; margin-top: 8px;">
                <span style="background:{t['primary']}; color:white; padding: 2px 10px; border-radius:12px; font-size:0.75rem; font-weight: 500;">Level {student['Level']}</span>
                <span style="background:{t['secondary']}20; color:{t['secondary']}; padding: 2px 10px; border-radius:12px; font-size:0.75rem;">Total XP: <b>{student['XP']}</b></span>
            </div>
        </div>
        <div style="text-align: right;">
             <div style="font-size: 0.75rem; color: {t['secondary']}; opacity: 0.8;">Kelancaran</div>
             <div style="font-size: 1.8rem; font-weight: 700; color: {t['primary']};">{student['Kelancaran_Avg']}%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- Detail Content ---
    c_chart, c_analysis = st.columns([1.5, 1])
    
    with c_chart:
        st.markdown(f"<h6 style='color:{t['secondary']}; margin-top: 10px;'>{icon('bi-graph-up', color=t['primary'])} Progress Mingguan</h6>", unsafe_allow_html=True)
        trend_data = pd.DataFrame({
            'Hari': ['Sen', 'Sel', 'Rab', 'Kam'], 
            'Skor': [random.randint(60,95) for _ in range(4)]
        })
        st.area_chart(trend_data.set_index('Hari'), color=t['primary'], height=220)

    with c_analysis:
        st.markdown(f"<h6 style='color:{t['secondary']}; margin-top: 10px;'>{icon('bi-cpu', color=t['primary'])} Analisis AI</h6>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="suggestion-box" style="font-size: 0.9rem; margin-bottom: 15px; color: {t['secondary']};">
            <b style="color: {t['primary']};">Feedback:</b><br>
            {student['Diagnosis']}
        </div>
        """, unsafe_allow_html=True)
        
        if len(student['Kata_Sulit']) > 0:
            st.markdown(f"<div style='font-size:0.85rem; font-weight:600; color:{t['accent']}; margin-bottom: 5px;'>Fokus Perbaikan ({len(student['Kata_Sulit'])} kata):</div>", unsafe_allow_html=True)
            html_tags = "".join([f"<span class='word-tag' style='font-size: 0.8rem;'>{w}</span>" for w in student['Kata_Sulit']])
            st.markdown(f"<div style='line-height: 1.6;'>{html_tags}</div>", unsafe_allow_html=True)
        else:
             st.markdown(f"""
            <div style="background-color:{t['background']}; border:1px solid {t['primary']}; padding: 10px; border-radius: 8px; text-align:center; font-size: 0.85rem; color: {t['primary']};">
                {icon('bi-check-circle-fill')} Tidak ada kata sulit.
            </div>
            """, unsafe_allow_html=True)

def render_sim_guru_header():
    t = get_current_theme()
    st.markdown(f"""
<div style="display: flex; align-items: center; gap: 10px; margin-bottom: -15px;">
{icon('bi-joystick', size="1.8rem", color=t['primary'])}
<h2 style="margin: 0; padding: 0; color: {t['primary']};">Dashboard Kelas (Simulasi)</h2>
</div>
""", unsafe_allow_html=True)
    
    st.markdown(f"<p style='color:{t['secondary']}; margin-left: 5px; opacity:0.8;'>Mode Simulasi: Data yang ditampilkan adalah dummy.</p>", unsafe_allow_html=True)
    st.divider()

def render_sim_guru_metrics(df):
    k1, k2, k3, k4 = st.columns(4)
    with k1: st.markdown(card_metric("Total Siswa", len(df), icon_name="bi-people-fill"), unsafe_allow_html=True)
    with k2: st.markdown(card_metric("Rata-rata Kelas", f"{df['Kelancaran_Avg'].mean():.0f}%"), unsafe_allow_html=True)
    with k3: 
        risk_count = len(df[df['Kelancaran_Avg'] < 50])
        st.markdown(card_metric("Perlu Bantuan", f"{risk_count} Siswa", icon_name="bi-exclamation-circle-fill"), unsafe_allow_html=True)
    with k4: st.markdown(card_metric("Top XP", df['XP'].max(), icon_name="bi-trophy-fill"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

def render_sim_guru_table(df):
    t = get_current_theme()
    st.markdown(f"""
<h5 style="display: flex; align-items: center; gap: 8px;">
{icon('bi-table', color=t['secondary'])} Daftar Siswa (Dummy)
</h5>
""", unsafe_allow_html=True)
    
    event = st.dataframe(
        df,
        column_config={
            "Nama": st.column_config.TextColumn("Nama Lengkap", width="medium"),
            "Kelancaran_Avg": st.column_config.ProgressColumn("Tingkat Kelancaran", format="%d%%", min_value=0, max_value=100),
            "Level": st.column_config.NumberColumn("Lvl", format="%d"),
            "Status_Hari_Ini": st.column_config.TextColumn("Status"),
            "XP": st.column_config.NumberColumn("XP", format="%d XP"),
            "Kata_Sulit": None, 
            "Diagnosis": None 
        },
        use_container_width=True,
        hide_index=True,
        on_select="rerun",
        selection_mode="single-row"
    )

    if len(event.selection.rows) > 0:
        show_sim_student_detail(df.iloc[event.selection.rows[0]])

def render_sim_guru():
    render_sim_guru_header()
    df = get_dummy_class_data()
    render_sim_guru_metrics(df)
    render_sim_guru_table(df)

# ==============================================================================
# ORTU VIEW REPLICA (Shadowing views/ortu_view.py)
# ==============================================================================

def render_sim_ortu_header(child_data):
    t = get_current_theme()
    st.markdown(f"""
    <div class="soft-card" style="border-left: 5px solid {t['primary']}; background-color: {t['card_bg']};">
        <div style="display:flex; align-items:center; gap:20px;">
            <img src="https://img.freepik.com/free-vector/wise-owl-with-graduation-cap-diploma_138676-3046.jpg?w=100" width="80" style="border-radius:12px;">
            <div>
                <h2 style="margin:0; color:{t['primary']}">{child_data['Nama']}</h2>
                <p style="margin:0; color:{t['secondary']}; font-size:0.95rem;">
                    {icon('bi-star-fill', color='#F59E0B')} Level {child_data['Level']} &nbsp;|&nbsp; ID: SIMULASI-001
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_sim_ortu_report(child_data):
    t = get_current_theme()
    st.markdown("<br>", unsafe_allow_html=True)
    col_stat, col_detail = st.columns([1, 2])
    
    with col_stat:
        st.markdown(f"""
        <div class="soft-card" style="text-align:center; padding: 40px 20px; background-color: {t['card_bg']};">
            <div style="font-size:0.9rem; color:{t['secondary']}; text-transform:uppercase; letter-spacing:1px; opacity:0.8;">Skor Kelancaran</div>
            <div style="font-size:3.5rem; font-weight:700; color:{t['primary']}; line-height:1.2;">
                {child_data['Kelancaran_Avg']}<span style="font-size:1.5rem">%</span>
            </div>
            <div style="margin-top:10px; font-size:0.85rem; background:#DCFCE7; color:#166534; display:inline-block; padding:4px 12px; border-radius:20px;">
                {icon('bi-graph-up-arrow')} Meningkat dari kemarin
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_detail:
        if len(child_data['Kata_Sulit']) > 0:
            st.markdown(f"""
            <div class="alert-box">
                <h5 style="margin:0; font-family:'Poppins';">{icon('bi-exclamation-triangle-fill')} Perlu Latihan Mandiri</h5>
                <p style="margin-top:5px; font-size:0.9rem; color:{t['text']}; opacity: 0.9;">
                    Anak Anda mengalami kesulitan mengeja kata-kata berikut hari ini:
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            tags = "".join([f"<span class='word-tag'>{w}</span>" for w in child_data['Kata_Sulit']])
            st.markdown(f"<div style='margin:15px 0;'>{tags}</div>", unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="suggestion-box">
                <b>{icon('bi-lightbulb', color=t['primary'])} Saran NARA AI:</b><br>
                <span style="font-size:0.95rem; color:{t['secondary']}">{child_data['Diagnosis']}</span>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="soft-card" style="background-color:{t['background']}; border:1px solid {t['primary']}; text-align:center;">
                <h4 style="color:{t['primary']};">{icon('bi-award-fill')} Luar Biasa!</h4>
                <p style="color:{t['text']};">Tidak ada kata sulit yang terdeteksi hari ini. Semua bacaan lancar.</p>
            </div>
            """, unsafe_allow_html=True)

def render_sim_ortu_monitoring():
    t = get_current_theme()
    st.markdown("<br>", unsafe_allow_html=True)
    c_btn, c_info = st.columns([1, 4])
    
    # Use local state for simulation monitoring to avoid conflicting with global monitoring state
    if 'sim_monitoring_active' not in st.session_state:
        st.session_state.sim_monitoring_active = False

    with c_btn:
        active = st.session_state.sim_monitoring_active
        if not active:
            if st.button("Mulai Sesi (Sim)", type="primary", use_container_width=True):
                st.session_state.sim_monitoring_active = True
                st.rerun()
        else:
            if st.button("Stop Sesi (Sim)", type="secondary", use_container_width=True):
                st.session_state.sim_monitoring_active = False
                st.rerun()
    
    with c_info:
        active = st.session_state.sim_monitoring_active
        if active:
            st.markdown(f"<div style='padding:8px; color:{t['primary']}; font-weight:600;'>{icon('bi-wifi', class_name='pulse-icon')} Device Connected (SIM-01)</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='padding:8px; color:{t['secondary']};'>{icon('bi-wifi-off')} Device Disconnected</div>", unsafe_allow_html=True)

    if st.session_state.sim_monitoring_active:
        chart_place = st.empty()
        st.caption("Real-time Speech-to-Text Stream (Simulated):")
        text_place = st.empty()
        
        sample_txt = "Ini adalah contoh teks yang sedang dibaca siswa dalam mode simulasi."
        words = sample_txt.split()
        current_words = []
        
        for i, w in enumerate(words):
            if not st.session_state.sim_monitoring_active: break
            chart_data = pd.DataFrame(np.random.uniform(0, 100, size=(1, 30))).T
            chart_place.bar_chart(chart_data, height=40, color=t['primary'])
            current_words.append(w)
            display_html = " ".join([f"<span class='highlight-active'>{word}</span>" if idx == i else word for idx, word in enumerate(current_words)])
            
            text_place.markdown(f"""
            <div class="live-terminal">
                {icon('bi-mic-fill', color=t['accent'])} Listening...<br><br>
                {display_html} <span style="animation: blink 1s infinite;">_</span>
            </div>
            """, unsafe_allow_html=True)
            time.sleep(0.5)
        
        text_place.markdown(f"""
        <div class="live-terminal" style="border-left-color: #10B981;">
            {icon('bi-check-circle-fill', color='#10B981')} Session Completed.<br><br>
            {sample_txt}
        </div>
        """, unsafe_allow_html=True)
        st.session_state.sim_monitoring_active = False
        if st.button("Reset Monitor"): st.rerun()
    else:
        st.markdown(f"""
        <div class="soft-card" style="text-align:center; padding:60px; border: 2px dashed #CBD5E1; background-color:{t['background']};">
            {icon('bi-headset', size="3rem", color="#94A3B8")}
            <h5 style="color:{t['secondary']}; margin-top:15px; opacity: 0.8;">Monitoring Siap</h5>
            <p style="font-size:0.9rem; color:{t['secondary']}; opacity: 0.6;">Tekan tombol 'Mulai Sesi' untuk menghubungkan ke audio stream.</p>
        </div>
        """, unsafe_allow_html=True)

def render_sim_ortu():
    child_data = get_dummy_student_data()

    render_sim_ortu_header(child_data)
    
    t = get_current_theme()
    nav_bg = t['card_bg'] if st.session_state.get("theme_mode") == "light" else "transparent"
    nav_hover = "#F8FAFC" if st.session_state.get("theme_mode") == "light" else "#1E293B"

    selected_tab = option_menu(
        menu_title=None, 
        options=["Laporan Harian", "Live Monitoring"], 
        icons=["journal-text", "mic"], 
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": t['secondary'], "font-size": "14px"}, 
            "nav-link": {
                "font-size": "14px", 
                "text-align": "center", 
                "margin": "0px 10px 0px 0px", 
                "border-radius": "8px", 
                "background-color": nav_bg, 
                "border": f"1px solid {t['border']}", 
                "color": t['secondary'],
                "--hover-color": nav_hover
            },
            "nav-link-selected": {"background-color": t['primary'], "color": "white", "border": f"1px solid {t['primary']}"},
        }
    )

    if selected_tab == "Laporan Harian":
        render_sim_ortu_report(child_data)
    elif selected_tab == "Live Monitoring":
        render_sim_ortu_monitoring()

# ==============================================================================
# MAIN VIEW CONTROLLER
# ==============================================================================

def view_simulation():
    # Only show role selection for simulation main page
    t = get_current_theme()
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 20px;">
        <span style="background-color: {t['background']}; padding: 5px 15px; border-radius: 20px; font-size: 0.8rem; color: {t['secondary']}; font-weight: 500; border: 1px solid {t['border']};">
            {icon('bi-info-circle')} Mode Simulasi
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    sim_role = option_menu(
        menu_title=None, 
        options=["Simulasi Guru", "Simulasi Orang Tua"], 
        icons=["person-video3", "house-heart"], 
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "transparent", "margin-bottom": "20px"},
            "nav-link": {"font-size": "14px", "text-align": "center", "margin": "0px 5px", "border-radius": "8px", "color": t['secondary']},
            "nav-link-selected": {"background-color": t['accent'], "color": "white"},
        }
    )

    if sim_role == "Simulasi Guru":
        render_sim_guru()
    else:
        render_sim_ortu()
